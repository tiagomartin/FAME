# Data

Raw third-party data are not committed to this repository by default.

For exact sources, redistribution decisions, expected filenames, and reconstruction
instructions, see:

- [`SOURCES_AND_RECONSTRUCTION.md`](SOURCES_AND_RECONSTRUCTION.md)
- [`DATA_CONTRACT.md`](DATA_CONTRACT.md)

The repository does include temporal split definitions and processed experimental artifacts
required to audit the manuscript's reported results.

To create the expected raw-data directory structure and retrieve the official RTS-GMLC
generator table, run:

```bash
python scripts/prepare_external_data.py
python scripts/validate_external_data.py
```

Cartola FC and TransnetBW source data must be supplied according to the source-specific
instructions.
