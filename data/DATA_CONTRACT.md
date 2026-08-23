# Input data contracts

## Fantasy-football analytical file

The code performs an explicit check for the following mandatory columns:

| Column | Role |
|---|---|
| `temporada` | season/year |
| `rodada_id` | round identifier |
| `atleta_id` | player identifier |
| `posicao_id` | position identifier |
| `pontos_num` | realized fantasy score |
| `preco_num` | player market price |
| `media_num` | platform historical mean |
| `jogos_num` | number of matches/appearances |

The notebook also consumes additional variables when available, including status, price
variation, club identifiers, scouting variables, lagged/rolling features, and engineered
decision-oriented variables. The notebook remains the authoritative executable specification.

The analytical key is:

```text
(atleta_id, temporada, rodada_id)
```

and duplicate keys are rejected.

## Energy TransnetBW file

The temporal Energy notebook is the authoritative specification for the exact input column
names used after loading the compiled TransnetBW file. Before public release, run
`scripts/validate_external_data.py` on the final input file and commit the resulting schema
report under `reproducibility/`.

## RTS-GMLC generator table

The expected source file is the official:

```text
RTS_Data/SourceData/gen.csv
```

from the GridMod/RTS-GMLC repository.
