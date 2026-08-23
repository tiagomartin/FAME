from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

FILES = {
    "fantasy_football": (
        RAW
        / "fantasy_football"
        / "cartola_base_modelagem_2021_2026.csv"
    ),
    "transnetbw": (
        RAW
        / "energy"
        / "transnetbw_actual_forecast_hourly_utc_2015_2025.csv"
    ),
    "rts_gmlc_gen": (
        RAW
        / "energy"
        / "RTS-GMLC"
        / "RTS_Data"
        / "SourceData"
        / "gen.csv"
    ),
}

FAILED = False


def report_failure(message):
    global FAILED
    FAILED = True
    print(f"  FAIL: {message}")


def report_ok(message):
    print(f"  OK: {message}")


def read_csv_checked(path, label):
    try:
        df = pd.read_csv(path)
        report_ok(
            f"{label} is readable "
            f"({len(df):,} rows, {len(df.columns)} columns)"
        )
        return df

    except Exception as exc:
        report_failure(
            f"{label} could not be read as CSV: {exc}"
        )
        return None


for label, path in FILES.items():
    print()
    print(f"[{label}]")
    print(path)

    if not path.exists():
        report_failure("file not found")
        continue

    report_ok(
        f"file present ({path.stat().st_size:,} bytes)"
    )


ff_path = FILES["fantasy_football"]

if ff_path.exists():
    ff = read_csv_checked(
        ff_path,
        "fantasy-football analytical dataset",
    )

    if ff is not None:
        required_columns = {
            "temporada",
            "rodada_id",
            "atleta_id",
            "posicao_id",
            "pontos_num",
            "preco_num",
            "media_num",
            "jogos_num",
        }

        missing = sorted(
            required_columns.difference(ff.columns)
        )

        if missing:
            report_failure(
                "missing mandatory columns: "
                + ", ".join(missing)
            )
        else:
            report_ok(
                "all mandatory fantasy-football columns are present"
            )

        key = [
            "atleta_id",
            "temporada",
            "rodada_id",
        ]

        if all(column in ff.columns for column in key):
            duplicates = ff.duplicated(
                key,
                keep=False,
            )

            if duplicates.any():
                report_failure(
                    f"{int(duplicates.sum()):,} rows have "
                    "duplicate player-season-round keys"
                )
            else:
                report_ok(
                    "player-season-round key is unique"
                )

        if "temporada" in ff.columns:
            seasons = sorted(
                pd.to_numeric(
                    ff["temporada"],
                    errors="coerce",
                )
                .dropna()
                .astype(int)
                .unique()
            )

            print(
                "  seasons present:",
                seasons,
            )

            required_seasons = {
                2021,
                2022,
                2023,
                2024,
                2025,
            }

            missing_seasons = sorted(
                required_seasons.difference(seasons)
            )

            if missing_seasons:
                report_failure(
                    "missing manuscript seasons: "
                    + ", ".join(
                        map(str, missing_seasons)
                    )
                )
            else:
                report_ok(
                    "all manuscript seasons 2021--2025 are present"
                )


transnetbw_path = FILES["transnetbw"]

if transnetbw_path.exists():
    energy = read_csv_checked(
        transnetbw_path,
        "TransnetBW analytical dataset",
    )

    if energy is not None:
        required_columns = {
            "timestamp_utc",
            "actual_load_mw",
            "dayahead_forecast_mw",
        }

        missing = sorted(
            required_columns.difference(
                energy.columns
            )
        )

        if missing:
            report_failure(
                "missing mandatory TransnetBW columns: "
                + ", ".join(missing)
            )

        else:
            report_ok(
                "all mandatory TransnetBW columns are present"
            )

            timestamps = pd.to_datetime(
                energy["timestamp_utc"],
                errors="coerce",
                utc=True,
            )

            invalid = timestamps.isna().sum()

            if invalid:
                report_failure(
                    f"{invalid:,} invalid UTC timestamps"
                )
            else:
                report_ok(
                    "all timestamps are valid UTC datetimes"
                )

                years = sorted(
                    timestamps.dt.year.unique()
                )

                print(
                    "  years present:",
                    years,
                )

                required_years = set(
                    range(2015, 2026)
                )

                missing_years = sorted(
                    required_years.difference(
                        years
                    )
                )

                if missing_years:
                    report_failure(
                        "missing Energy study years: "
                        + ", ".join(
                            map(str, missing_years)
                        )
                    )
                else:
                    report_ok(
                        "all Energy study years 2015--2025 are present"
                    )

            for column in [
                "actual_load_mw",
                "dayahead_forecast_mw",
            ]:
                values = pd.to_numeric(
                    energy[column],
                    errors="coerce",
                )

                missing_values = values.isna().sum()

                if missing_values:
                    report_failure(
                        f"{column} contains "
                        f"{missing_values:,} missing/non-numeric values"
                    )
                else:
                    report_ok(
                        f"{column} is numeric and complete"
                    )


rts_path = FILES["rts_gmlc_gen"]

if rts_path.exists():
    gen = read_csv_checked(
        rts_path,
        "RTS-GMLC generator table",
    )

    if gen is not None:
        if len(gen) == 0:
            report_failure(
                "RTS-GMLC generator table is empty"
            )
        else:
            report_ok(
                "RTS-GMLC generator table contains data"
            )


print()
print("Validation summary")
print("------------------")

if FAILED:
    print("FAILED")
    sys.exit(1)

print("PASSED")
sys.exit(0)
