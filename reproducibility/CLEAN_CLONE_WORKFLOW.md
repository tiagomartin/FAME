# Clean-clone reproduction workflow

This document describes how to inspect the archived manuscript artifacts and how to prepare a clean environment for re-executing the FAME analyses.

The curated `results/` directory contains the numerical evidence archived with the manuscript. Fresh notebook executions write to `reproduced/` and do not overwrite the archived results.

The workflow distinguishes between:

1. auditing the archived manuscript results; and
2. re-executing the analyses after the required external data have been supplied.

## 1. Clone the repository

```bash
git clone https://github.com/tiagomartin/FAME.git
cd FAME
```

The manuscript experiments were executed using Python 3.13.14.

Create a Python 3.13 virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell, activation can normally be performed with:

```powershell
.\.venv\Scripts\Activate.ps1
```

If local PowerShell execution policy prevents activation, the environment can be used directly without changing the system execution policy:

```powershell
.\.venv\Scripts\python.exe --version
```

On Unix-like systems:

```bash
source .venv/bin/activate
```

## 2. Install the computational environment

The direct Python dependencies and the versions associated with the manuscript experiments are pinned in the repository-level `requirements.txt`.

Install them with:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

When using the virtual environment directly on Windows without activation:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

A clean-clone installation of the pinned dependencies was successfully verified under Python 3.13 before the manuscript-associated reproducibility release.

## 3. Prepare external data

Run:

```bash
python scripts/prepare_external_data.py
```

On Windows without virtual-environment activation:

```powershell
.\.venv\Scripts\python.exe scripts\prepare_external_data.py
```

The preparation script:

- creates the expected external-data directories;
- retrieves the RTS-GMLC generator table from the official GridMod repository when it is not already present;
- checks whether the Cartola analytical dataset is present; and
- checks whether the TransnetBW analytical dataset is present.

The script does not automatically download or reconstruct the Cartola FC or TransnetBW analytical inputs.

Their provenance, expected locations, redistribution status, and current reproducibility boundaries are documented in:

```text
data/SOURCES_AND_RECONSTRUCTION.md
```

After preparation, a clean clone without the non-redistributed external datasets is expected to report:

```text
Cartola analytical dataset: NOT FOUND
TransnetBW analytical dataset: NOT FOUND
RTS-GMLC generator table: FOUND
```

This is expected behavior and does not indicate a failure of the preparation script.

## 4. Validate external inputs

Run:

```bash
python scripts/validate_external_data.py
```

or, on Windows without environment activation:

```powershell
.\.venv\Scripts\python.exe scripts\validate_external_data.py
```

The validator checks the presence and basic structural requirements of the external analytical inputs.

For the fantasy-football input, validation includes:

- required core columns;
- player-season-round key uniqueness; and
- presence of manuscript seasons 2021--2025.

For the TransnetBW input, validation includes:

- required analytical columns;
- valid UTC timestamps;
- presence of study years 2015--2025; and
- numeric completeness of actual-load and day-ahead forecast fields.

For RTS-GMLC, the validator confirms that the generator table is present, readable, and non-empty.

When Cartola and TransnetBW data have not yet been supplied, the validation command is expected to terminate with:

```text
FAILED
```

while reporting the two missing external files and successfully validating RTS-GMLC.

This behavior is intentional. A successful full validation requires all external analytical inputs.

## 5. Expected external-data structure

After all required external inputs have been supplied, the relevant directory structure is:

```text
data/
└── raw/
    ├── fantasy_football/
    │   └── cartola_base_modelagem_2021_2026.csv
    └── energy/
        ├── transnetbw_actual_forecast_hourly_utc_2015_2025.csv
        └── RTS-GMLC/
            └── RTS_Data/
                └── SourceData/
                    └── gen.csv
```

The `data/raw/` directory is excluded from version control by default.

## 6. Audit archived manuscript results

Access to the external raw or analytical datasets is not required to inspect the numerical artifacts archived with the manuscript.

Use:

```text
reproducibility/artifact_manifest.csv
```

to map manuscript claims and analyses to the corresponding files under `results/` and to the associated analysis notebooks.

This provides the primary audit trail:

```text
manuscript claim
        ↓
artifact_manifest.csv
        ↓
archived machine-readable result
        ↓
analysis notebook
```

The archived results should not be overwritten during reproduction attempts.

## 7. Reproduce fantasy-football experiments

After supplying and validating the required fantasy-football analytical input, run the notebooks in the following order:

```text
code/fantasy_football/FAME_fantasy_football_primary.ipynb
code/fantasy_football/FAME_temporal_replication_H1.ipynb
code/fantasy_football/FAME_temporal_replication_H2.ipynb
code/fantasy_football/FAME_temporal_replications_comparison.ipynb
```

Fresh outputs are written under:

```text
reproduced/fantasy_football/
├── primary/
├── H1/
├── H2/
└── comparison/
```

The archived manuscript artifacts remain under `results/fantasy_football/`.

## 8. Reproduce Energy experiments

After supplying and validating the required TransnetBW analytical input and preparing the RTS-GMLC generator data, run:

```text
code/energy/FAME_energy_temporal_replication.ipynb
code/energy/FAME_energy_scientific_synthesis.ipynb
```

Fresh outputs are written under:

```text
reproduced/energy/temporal_replication/
```

The archived manuscript artifacts remain under `results/energy/`.

## 9. Compare fresh and archived outputs

Use:

```text
reproducibility/artifact_manifest.csv
```

to identify the archived artifact associated with each manuscript result.

Fresh outputs generated under `reproduced/` can then be compared with the corresponding machine-readable evidence under `results/`.

Because some analyses contain stochastic components, comparisons should follow the numerical summaries, frozen parameters, and uncertainty procedures documented by the corresponding experiment rather than assuming byte-for-byte identity of every generated file.

## 10. Reproducibility boundaries

The clean-clone workflow supports two distinct activities.

### Archived-result audit

The repository can be cloned and the archived numerical evidence can be inspected without obtaining the non-redistributed Cartola FC and TransnetBW datasets.

### Analysis re-execution

Re-execution requires the corresponding external analytical inputs to be placed at the documented paths and to pass `scripts/validate_external_data.py`.

The repository does not currently claim complete raw-source-to-result reconstruction for the Cartola analytical dataset or the compiled TransnetBW analytical dataset. These limitations and the corresponding data provenance are documented explicitly in `data/SOURCES_AND_RECONSTRUCTION.md`.

## Design principle

The public notebooks use repository-relative paths and separate newly generated outputs from the archived manuscript artifacts.

They do not rely on author-machine absolute paths, and future-period outcomes are not used to update the frozen prediction-to-decision representation evaluated prospectively.
