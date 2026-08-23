# External data sources and reconstruction

This document records the external data dependencies required for an end-to-end
reproduction of the FAME experiments. Raw third-party data are intentionally not
committed to this repository by default.

## 1. Fantasy-football study

### Required analytical input

The final fantasy-football notebooks expect a file named:

```text
cartola_base_modelagem_YYYY_YYYY.csv
```

For the primary experiment, the analytical source used during development covered
2021--2026, while the reported experiment filters the data to 2021--2025 and explicitly
uses no 2026 rows.

The notebooks require at least these core fields:

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

Additional historical, scouting, market, contextual, and engineered variables are used by
the predictive pipeline. The exact features selected by the final code can be inspected in
the notebook and the model-selection artifacts under `results/fantasy_football/`.

### Public source / historical archive

A public historical source commonly used for Cartola FC research is:

- caRtola project: https://github.com/henriquepgomide/caRtola

The caRtola repository states that it provides historical raw Cartola FC data and extraction /
processing code. Its repository software is distributed under the MIT License. The underlying
Cartola FC platform data may remain subject to the original provider's terms.

The Cartola FC public API endpoints have also historically been used to collect round-level
market and player information, for example:

```text
https://api.cartolafc.globo.com/mercado/status
https://api.cartolafc.globo.com/atletas/mercado
https://api.cartolafc.globo.com/partidas/{rodada}
https://api.cartolafc.globo.com/clubes
```

### Redistribution decision

**Current public-repository policy:** do not redistribute the complete raw Cartola FC data
or the authors' full analytical player-level dataset until the applicable source/provider terms
have been verified for redistribution.

Instead, this repository publishes:

- temporal split definitions;
- frozen hyperparameters and representation parameters;
- model-selection summaries;
- out-of-time aggregate and round-level experimental results;
- robustness analyses;
- leakage/freeze audits.

This is sufficient to audit the numerical claims reported in the manuscript, but not yet to
retrain the complete predictive pipeline from a clean clone.

## 2. Energy study: TransnetBW load data

### Required analytical input

The final temporal-replication notebook expects:

```text
data/raw/energy/transnetbw_actual_forecast_hourly_utc_2015_2025.csv
```

The file must contain the hourly actual-load and day-ahead forecast information used to
construct daily peak demand over 2015--2025.

### Official source

TransnetBW publishes historical market/transparency data and provides downloadable load
series through its Market Data / Key Figures pages:

https://www.transnetbw.de/en/transparency/market-data/key-figures

The public page provides historical downloads extending back through the study period.

### Redistribution decision

The repository does **not** currently redistribute the authors' compiled 2015--2025
TransnetBW CSV. The final public release should either:

1. document the precise monthly files and reconstruction code used to build the compiled
   CSV; or
2. redistribute the compiled dataset only after confirming that TransnetBW's applicable
   data-use terms permit that form of redistribution.

Until that check is completed, the reproducible and conservative option is source citation +
reconstruction instructions.

## 3. Energy study: RTS-GMLC generation fleet

### Required input

The final Energy notebook expects the RTS-GMLC generator table corresponding to:

```text
RTS_Data/SourceData/gen.csv
```

### Official source

Official repository:

https://github.com/GridMod/RTS-GMLC

The RTS-GMLC repository states that the SourceData folder contains the open CSV
representation of the test system.

The repository's data-use notice grants the right to use, copy, and distribute the data,
provided that the complete notice accompanies copies and DOE/NREL/Alliance are credited
in publications resulting from use of the data.

### Redistribution decision

For maximum provenance clarity, FAME does not need to vendor the RTS-GMLC source data.
The recommended workflow is to retrieve `gen.csv` directly from the official repository
during setup. A helper script is provided in `scripts/prepare_external_data.py`.

## 4. Directory expected after external-data setup

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

The `data/raw/` directory is ignored by Git by default.
