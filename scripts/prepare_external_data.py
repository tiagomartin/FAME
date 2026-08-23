"""Prepare external data directories and retrieve redistributable public inputs.

This script intentionally does not download Cartola FC or TransnetBW data automatically.
Those sources require source-specific acquisition/reconstruction steps documented in
data/SOURCES_AND_RECONSTRUCTION.md.

RTS-GMLC gen.csv is retrieved from the official GridMod repository.
"""

from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
FF = RAW / "fantasy_football"
ENERGY = RAW / "energy"
RTS = ENERGY / "RTS-GMLC" / "RTS_Data" / "SourceData"

RTS_GEN_URL = (
    "https://raw.githubusercontent.com/GridMod/RTS-GMLC/master/"
    "RTS_Data/SourceData/gen.csv"
)

for directory in (FF, ENERGY, RTS):
    directory.mkdir(parents=True, exist_ok=True)

target = RTS / "gen.csv"
if not target.exists():
    print(f"Downloading RTS-GMLC generator data to {target}")
    urlretrieve(RTS_GEN_URL, target)
else:
    print(f"RTS-GMLC generator data already present: {target}")

print()
print("External files still required:")
print(
    FF / "cartola_base_modelagem_2021_2026.csv"
)
print(
    ENERGY / "transnetbw_actual_forecast_hourly_utc_2015_2025.csv"
)
print()
print("See data/SOURCES_AND_RECONSTRUCTION.md for acquisition instructions.")
