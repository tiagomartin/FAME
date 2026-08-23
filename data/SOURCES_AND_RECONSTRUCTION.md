# External data sources and reconstruction

This document describes the external data dependencies of the FAME experiments, their provenance, the analytical inputs expected by the public code, and the current redistribution policy.

Raw third-party data are not included in this repository unless redistribution rights have been established. The repository instead provides the source information, expected input structures, temporal split definitions, frozen model and representation parameters, and archived numerical outputs required to audit the empirical results reported in the manuscript.

The availability of archived results should be distinguished from end-to-end re-execution. Analyses depending on external data can be re-executed only after the corresponding external inputs have been obtained and prepared as described below.

## 1. Fantasy-football study

### Required analytical input

The final fantasy-football notebooks expect the analytical dataset:

```text
data/raw/fantasy_football/cartola_base_modelagem_2021_2026.csv
```

The analytical source used during development covered 2021--2026. The experiments reported in the manuscript use observations from 2021--2025; no 2026 observations are used in the reported prospective evaluation.

The analytical dataset contains player-round observations and requires at least the following core fields:

```text
temporada
rodada_id
atleta_id
posicao_id
pontos_num
preco_num
media_num
jogos_num
```

The predictive pipeline additionally uses historical, scouting, market, contextual, and engineered variables. The public notebooks provide the executable specification of the variables consumed by each analysis, while the archived model-selection artifacts under `results/fantasy_football/` document the frozen predictive configurations used for the reported experiments.

### External source and provenance

Historical Cartola FC data can be obtained from publicly accessible historical archives and Cartola FC data interfaces.

One historical source used in academic and analytical applications is the caRtola project:

`https://github.com/henriquepgomide/caRtola`

The caRtola repository provides historical Cartola FC data together with extraction and processing code. The software distributed by that repository is licensed separately from the underlying Cartola FC data.

Cartola FC public API endpoints have also historically provided round-level market, player, match, and club information, including endpoints such as:

```text
https://api.cartolafc.globo.com/mercado/status
https://api.cartolafc.globo.com/atletas/mercado
https://api.cartolafc.globo.com/partidas/{rodada}
https://api.cartolafc.globo.com/clubes
```

Availability and behavior of external APIs may change independently of this repository.

### Redistribution and reproducibility status

The complete raw Cartola FC data and the authors' full player-level analytical dataset are not redistributed in FAME because redistribution rights for all underlying source data have not been established.

The repository therefore provides the components that can be shared independently of the raw third-party observations, including:

- temporal development, calibration, and evaluation definitions;
- frozen predictive hyperparameters;
- frozen ensemble weights;
- DOC candidate grids and frozen DOC parameters;
- model-selection summaries;
- out-of-time aggregate and round-level experimental results;
- temporal replication results;
- robustness and sensitivity analyses; and
- leakage, target-alignment, missing-market, and freeze audits.

These artifacts allow the numerical claims reported in the manuscript to be audited against the archived experimental outputs.

Full retraining of the fantasy-football predictive pipeline additionally requires reconstruction of the player-level analytical dataset from the external Cartola FC sources. Because the complete transformation from the external raw sources to the authors' analytical player-level dataset is not distributed in the current repository, the fantasy-football study should not be interpreted as providing source-to-result end-to-end reproducibility from a clean clone.

## 2. Energy study: TransnetBW load data

### Required analytical input

The final Energy temporal-replication analysis expects:

```text
data/raw/energy/transnetbw_actual_forecast_hourly_utc_2015_2025.csv
```

This analytical input contains the historical actual-load and day-ahead load-forecast series used to construct the daily peak-demand quantities required by the Energy experiments over 2015--2025.

The temporal development, calibration, and evaluation definitions derived for the manuscript experiments are archived separately under:

```text
data/energy/splits/
```

### Official source

TransnetBW publishes historical electricity-system and market data through its transparency and market-data services.

The source page used to identify the historical load data is:

`https://www.transnetbw.de/en/transparency/market-data/key-figures`

Historical availability, file organization, naming conventions, and download interfaces are controlled by TransnetBW and may change independently of FAME.

### Reconstruction and redistribution status

The authors' compiled 2015--2025 TransnetBW analytical CSV is not redistributed in this repository.

Re-execution of the Energy temporal-replication analysis therefore requires the user to obtain the corresponding historical actual-load and day-ahead forecast observations from the official TransnetBW source and construct the analytical input expected by the notebook.

The required destination is:

```text
data/raw/energy/transnetbw_actual_forecast_hourly_utc_2015_2025.csv
```

The compiled input must represent the study period 2015--2025 and contain the actual-load and day-ahead forecast information required by the public Energy notebook.

The repository archives the temporal split definitions, frozen representation parameters, robustness results, and numerical outputs used in the manuscript. These artifacts permit auditing of the reported Energy results independently of redistribution of the compiled third-party load dataset.

The current repository does not claim raw-source-to-analytical-file reproducibility for the TransnetBW component because the precise historical download manifest and complete source-to-CSV transformation used to construct the compiled analytical input are not currently distributed.

## 3. Energy study: RTS-GMLC generation fleet

### Required input

The Energy analysis uses the RTS-GMLC generator table:

```text
RTS_Data/SourceData/gen.csv
```

Within the FAME external-data directory, the expected location is:

```text
data/raw/energy/RTS-GMLC/RTS_Data/SourceData/gen.csv
```

### Official source

The RTS-GMLC test system is publicly available from the official repository:

`https://github.com/GridMod/RTS-GMLC`

The `RTS_Data/SourceData/` directory of that repository contains the CSV representation of the test system used by the FAME Energy analysis.

Users should consult the RTS-GMLC repository for the applicable data-use notice, attribution requirements, and current distribution terms.

### Reconstruction

FAME does not vendor a duplicate copy of the RTS-GMLC source data. The generator table should instead be retrieved from the official RTS-GMLC repository.

The external-data preparation helper is:

```text
scripts/prepare_external_data.py
```

After preparation, the required generator table should be available at:

```text
data/raw/energy/RTS-GMLC/RTS_Data/SourceData/gen.csv
```

This component is therefore externally sourced but reconstructible from the identified public repository.

## 4. Expected external-data directory

After all required external inputs have been supplied, the expected directory structure is:

```text
data/
├── raw/
│   ├── fantasy_football/
│   │   └── cartola_base_modelagem_2021_2026.csv
│   └── energy/
│       ├── transnetbw_actual_forecast_hourly_utc_2015_2025.csv
│       └── RTS-GMLC/
│           └── RTS_Data/
│               └── SourceData/
│                   └── gen.csv
├── fantasy_football/
│   └── splits/
└── energy/
    └── splits/
```

The `data/raw/` directory is excluded from version control by default.

## 5. Reproducibility boundaries

The FAME repository distinguishes three levels of reproducibility support.

### Archived-result auditability

The numerical artifacts stored under `results/`, together with `reproducibility/artifact_manifest.csv`, allow the principal empirical claims reported in the manuscript to be traced to archived machine-readable outputs and the corresponding analysis code.

### Re-execution with supplied external inputs

The public notebooks can be used with the external analytical inputs placed at the expected paths documented above.

### Raw-source-to-result reproduction

Raw-source-to-result reproduction additionally requires a fully specified transformation from each external source to the analytical inputs consumed by the notebooks.

This level is currently supported for externally retrievable components for which the complete acquisition/preparation procedure is distributed, such as the RTS-GMLC generator input.

For the fantasy-football analytical dataset and the compiled TransnetBW load dataset, the repository provides provenance, input expectations, archived experimental artifacts, and analysis code, but does not currently claim complete raw-source-to-result reproducibility.

These boundaries are stated explicitly to distinguish the auditability of the manuscript-associated archived results from stronger claims of end-to-end reconstruction of third-party analytical datasets.
