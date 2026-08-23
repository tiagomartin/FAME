"""Compare fresh reproduction outputs against archived manuscript artifacts.

The comparison is intentionally conservative:
- CSV files are aligned by common columns and sorted deterministically.
- Numeric columns are compared using configurable absolute and relative tolerances.
- Non-numeric columns must match exactly after normalization.
- Missing files are reported explicitly.

Run after reproducing the notebooks:
    python scripts/compare_reproduced_results.py
"""

from __future__ import annotations

from pathlib import Path
import math
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ARCHIVED = ROOT / "results"
REPRODUCED = ROOT / "reproduced"
REPORT = ROOT / "reproducibility" / "reproduction_comparison_report.csv"

ATOL = 1e-8
RTOL = 1e-6

# Archived artifact -> reproduced artifact
PAIRS = [
    (
        ARCHIVED / "fantasy_football" / "calibration" / "frozen_doc_weights.csv",
        REPRODUCED / "fantasy_football" / "primary" / "03_calibracao_decisao" / "frozen_doc_weights.csv",
        "FF frozen DOC weights",
    ),
    (
        ARCHIVED / "fantasy_football" / "calibration" / "doc_calibration_bootstrap_stability.csv",
        REPRODUCED / "fantasy_football" / "primary" / "03_calibracao_decisao" / "doc_calibration_bootstrap_stability.csv",
        "FF DOC bootstrap stability",
    ),
    (
        ARCHIVED / "fantasy_football" / "evaluation" / "operational_summary_2025.csv",
        REPRODUCED / "fantasy_football" / "primary" / "04_resultados_2025" / "operational_summary_2025.csv",
        "FF 2025 operational summary",
    ),
    (
        ARCHIVED / "fantasy_football" / "evaluation" / "strategy_bootstrap_ci_2025.csv",
        REPRODUCED / "fantasy_football" / "primary" / "04_resultados_2025" / "strategy_bootstrap_ci_2025.csv",
        "FF 2025 bootstrap intervals",
    ),
    (
        ARCHIVED / "fantasy_football" / "evaluation" / "fame_temporal_replications_comparison.csv",
        REPRODUCED / "fantasy_football" / "comparison" / "fame_temporal_replications_comparison.csv",
        "FF temporal replication comparison",
    ),
    (
        ARCHIVED / "fantasy_football" / "robustness" / "ablation_summary_2025.csv",
        REPRODUCED / "fantasy_football" / "primary" / "04_resultados_2025" / "ablation_summary_2025.csv",
        "FF 2025 ablation",
    ),
    (
        ARCHIVED / "fantasy_football" / "robustness" / "captain_summary.csv",
        REPRODUCED / "fantasy_football" / "primary" / "04_resultados_2025" / "captain_summary.csv",
        "FF captain sensitivity",
    ),
    (
        ARCHIVED / "fantasy_football" / "audit" / "target_alignment_audit.csv",
        REPRODUCED / "fantasy_football" / "primary" / "06_auditoria" / "target_alignment_audit.csv",
        "FF target-alignment audit",
    ),
    (
        ARCHIVED / "energy" / "robustness" / "global_robustness_summary_by_model.csv",
        REPRODUCED / "energy" / "temporal_replication" / "global_robustness_summary_by_model.csv",
        "Energy global robustness by model",
    ),
    (
        ARCHIVED / "energy" / "robustness" / "robustness_margin_voll_summary.csv",
        REPRODUCED / "energy" / "temporal_replication" / "robustness_margin_voll_summary.csv",
        "Energy margin x VOLL robustness",
    ),
    (
        ARCHIVED / "energy" / "robustness" / "theta_freezes_margin_voll.csv",
        REPRODUCED / "energy" / "temporal_replication" / "theta_freezes_margin_voll.csv",
        "Energy theta freezes",
    ),
]

def normalize_object_series(s: pd.Series) -> pd.Series:
    return (
        s.astype("string")
         .fillna("<NA>")
         .str.strip()
         .str.replace(r"\s+", " ", regex=True)
    )

def compare_csv(a: Path, b: Path):
    da = pd.read_csv(a)
    db = pd.read_csv(b)

    common = [c for c in da.columns if c in db.columns]
    if not common:
        return False, "no common columns"

    # Restrict to common columns so harmless extra audit columns do not fail the check.
    da = da[common].copy()
    db = db[common].copy()

    if len(da) != len(db):
        return False, f"row_count archived={len(da)} reproduced={len(db)}"

    # Deterministic row order using all non-numeric columns first.
    key_cols = [c for c in common if not pd.api.types.is_numeric_dtype(da[c])]
    if key_cols:
        da = da.sort_values(key_cols, kind="stable").reset_index(drop=True)
        db = db.sort_values(key_cols, kind="stable").reset_index(drop=True)
    else:
        da = da.reset_index(drop=True)
        db = db.reset_index(drop=True)

    details = []
    ok = True

    for c in common:
        if pd.api.types.is_numeric_dtype(da[c]) and pd.api.types.is_numeric_dtype(db[c]):
            xa = pd.to_numeric(da[c], errors="coerce").to_numpy(dtype=float)
            xb = pd.to_numeric(db[c], errors="coerce").to_numpy(dtype=float)
            same_nan = np.isnan(xa) & np.isnan(xb)
            good = np.isclose(xa, xb, atol=ATOL, rtol=RTOL, equal_nan=True)
            if not bool(np.all(good)):
                ok = False
                idx = np.where(~good)[0][:5].tolist()
                details.append(f"{c}: numeric mismatch rows={idx}")
        else:
            sa = normalize_object_series(da[c])
            sb = normalize_object_series(db[c])
            good = sa.eq(sb)
            if not bool(good.all()):
                ok = False
                idx = good[~good].index[:5].tolist()
                details.append(f"{c}: text mismatch rows={idx}")

    return ok, "OK" if ok else "; ".join(details)

def main():
    rows = []
    any_failure = False

    for archived, reproduced, label in PAIRS:
        if not archived.exists():
            rows.append([label, str(archived.relative_to(ROOT)), str(reproduced.relative_to(ROOT)),
                         "ARCHIVED_MISSING", ""])
            any_failure = True
            continue
        if not reproduced.exists():
            rows.append([label, str(archived.relative_to(ROOT)), str(reproduced.relative_to(ROOT)),
                         "REPRODUCED_MISSING", ""])
            any_failure = True
            continue

        ok, detail = compare_csv(archived, reproduced)
        rows.append([label, str(archived.relative_to(ROOT)), str(reproduced.relative_to(ROOT)),
                     "PASS" if ok else "FAIL", detail])
        any_failure = any_failure or not ok

    report = pd.DataFrame(rows, columns=[
        "check", "archived_path", "reproduced_path", "status", "detail"
    ])
    report.to_csv(REPORT, index=False)
    print(report.to_string(index=False))
    print(f"\nReport written to: {REPORT}")
    sys.exit(1 if any_failure else 0)

if __name__ == "__main__":
    main()
