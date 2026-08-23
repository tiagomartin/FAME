"""Validate the presence and basic structure of external FAME input data."""

from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

files = {
    "fantasy_football": RAW / "fantasy_football" / "cartola_base_modelagem_2021_2026.csv",
    "transnetbw": RAW / "energy" / "transnetbw_actual_forecast_hourly_utc_2015_2025.csv",
    "rts_gmlc_gen": RAW / "energy" / "RTS-GMLC" / "RTS_Data" / "SourceData" / "gen.csv",
}

failed = False

for label, path in files.items():
    print(f"\n[{label}] {path}")
    if not path.exists():
        print("  MISSING")
        failed = True
        continue
    print(f"  present ({path.stat().st_size:,} bytes)")
    try:
        df = pd.read_csv(path, nrows=50)
        print(f"  readable CSV; {len(df.columns)} columns")
        print("  columns:", ", ".join(map(str, df.columns)))
    except Exception as exc:
        print("  ERROR reading CSV:", exc)
        failed = True

ff = files["fantasy_football"]
if ff.exists():
    req = {
        "temporada", "rodada_id", "atleta_id", "posicao_id",
        "pontos_num", "preco_num", "media_num", "jogos_num"
    }
    cols = set(pd.read_csv(ff, nrows=1).columns)
    missing = sorted(req - cols)
    if missing:
        print("\nFantasy-football mandatory columns missing:", missing)
        failed = True
    else:
        print("\nFantasy-football mandatory-column check: OK")

sys.exit(1 if failed else 0)
