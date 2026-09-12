from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError

ROOT = Path(__file__).resolve().parents[1]

RAW = ROOT / "data" / "raw"
FANTASY_DIR = RAW / "fantasy_football"
ENERGY_DIR = RAW / "energy"
RTS_DIR = ENERGY_DIR / "RTS-GMLC" / "RTS_Data" / "SourceData"

CARTOLA_FILE = FANTASY_DIR / "cartola_base_modelagem_2021_2026.csv"

TRANSNETBW_FILE = (
    ENERGY_DIR
    / "transnetbw_actual_forecast_hourly_utc_2015_2025.csv"
)

RTS_GEN_FILE = RTS_DIR / "gen.csv"

RTS_GEN_URL = (
    "https://raw.githubusercontent.com/GridMod/RTS-GMLC/"
    "master/RTS_Data/SourceData/gen.csv"
)

for directory in (FANTASY_DIR, ENERGY_DIR, RTS_DIR):
    directory.mkdir(parents=True, exist_ok=True)

if RTS_GEN_FILE.exists():
    print(f"RTS-GMLC generator data already present: {RTS_GEN_FILE}")
else:
    try:
        print(f"Downloading RTS-GMLC generator data from:")
        print(RTS_GEN_URL)

        urlretrieve(RTS_GEN_URL, RTS_GEN_FILE)

        print(f"Saved to: {RTS_GEN_FILE}")

    except (HTTPError, URLError) as exc:
        raise RuntimeError(
            "Unable to retrieve RTS-GMLC gen.csv from the official "
            "GridMod repository."
        ) from exc

print()
print("External-data status")
print("--------------------")

print(
    "Cartola analytical dataset:",
    "FOUND" if CARTOLA_FILE.exists() else "NOT FOUND",
)

print(
    "TransnetBW analytical dataset:",
    "FOUND" if TRANSNETBW_FILE.exists() else "NOT FOUND",
)

print(
    "RTS-GMLC generator table:",
    "FOUND" if RTS_GEN_FILE.exists() else "NOT FOUND",
)

print()

if not CARTOLA_FILE.exists():
    print(f"Required external file: {CARTOLA_FILE}")

if not TRANSNETBW_FILE.exists():
    print(f"Required external file: {TRANSNETBW_FILE}")

print()
print(
    "See data/SOURCES_AND_RECONSTRUCTION.md "
    "for provenance and acquisition information."
)
