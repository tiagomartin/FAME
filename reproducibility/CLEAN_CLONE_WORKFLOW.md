# Clean-clone reproduction workflow

The curated `results/` directory contains the numerical evidence archived with the paper.
Fresh notebook executions write to `reproduced/` and never overwrite those archived results.

## 1. Clone and create an environment

```bash
git clone https://github.com/tiagomartin/FAME.git
cd FAME
python -m venv .venv
```

Activate the environment and install the dependencies listed in `requirements.txt`.
Before the final public release, that file should be replaced by the exact versions used
for the submitted results.

## 2. Prepare external data

```bash
python scripts/prepare_external_data.py
python scripts/validate_external_data.py
```

The helper retrieves the official RTS-GMLC generator table. Cartola FC and TransnetBW
inputs must be supplied according to `data/SOURCES_AND_RECONSTRUCTION.md`.

Optional environment-variable overrides are supported:

```text
FAME_CARTOLA_DATA
FAME_TRANSNETBW_DATA
FAME_RTS_GEN_DATA
FAME_CBC_EXE
```

## 3. Reproduce fantasy-football experiments

Run, in order:

```text
code/fantasy_football/FAME_fantasy_football_primary.ipynb
code/fantasy_football/FAME_temporal_replication_H1.ipynb
code/fantasy_football/FAME_temporal_replication_H2.ipynb
code/fantasy_football/FAME_temporal_replications_comparison.ipynb
```

Outputs are written to:

```text
reproduced/fantasy_football/
├── primary/
├── H1/
├── H2/
└── comparison/
```

## 4. Reproduce Energy experiments

Run:

```text
code/energy/FAME_energy_temporal_replication.ipynb
code/energy/FAME_energy_scientific_synthesis.ipynb
```

Outputs are written to:

```text
reproduced/energy/temporal_replication/
```

## 5. Compare against archived paper artifacts

Use `reproducibility/artifact_manifest.csv` to map manuscript claims to the curated
files in `results/`. The fresh outputs under `reproduced/` can then be compared with
the archived paper evidence.

## Design principle

The public notebooks deliberately use repository-relative paths. They do not search the
user's computer recursively for data files and do not contain author-machine paths.
