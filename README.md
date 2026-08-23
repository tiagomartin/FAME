# FAME

FAME is a modular prediction-to-decision framework for constrained resource allocation.

This repository contains the curated code, processed experimental artifacts, robustness analyses, figures, and supplementary material accompanying the manuscript:

**Temporal Transferability of Prediction-to-Decision Representations in Constrained Resource Allocation**

## Repository purpose

The repository is organized to make the paper's empirical claims auditable. It separates predictive development, decision-oriented calibration (DOC), frozen prediction-to-decision representations, future out-of-time evaluation, and retrospective robustness/diagnostic analyses.

Future-period outcomes are not used to reselect the representation evaluated prospectively.

## Repository structure

```text
FAME/
├── code/
│   ├── fantasy_football/
│   └── energy/
├── data/
│   ├── fantasy_football/splits/
│   └── energy/splits/
├── results/
│   ├── fantasy_football/
│   │   ├── model_selection/
│   │   ├── calibration/
│   │   ├── evaluation/
│   │   ├── robustness/
│   │   └── audit/
│   └── energy/
│       ├── temporal_replications/
│       ├── robustness/
│       └── audit/
├── figures/
│   ├── main/
│   └── supplementary/
├── supplementary/
└── reproducibility/
```


## Reproducibility status

For the current verification level, see `reproducibility/REPRODUCIBILITY_STATUS.md`. The archived results are fully auditable; a clean-clone end-to-end rerun remains pending until the documented external datasets are supplied.


The repository currently provides the curated numerical artifacts required to audit the
manuscript. Full end-to-end execution from a clean clone additionally requires the external/raw
data sources described in `data/README.md`. See `reproducibility/NOTEBOOK_AUDIT.md` before
running the notebooks.

## Code

The `code/` directory contains the notebooks used for the final fantasy-football and Energy experiments reported in the manuscript. Development/debug notebooks and obsolete intermediate versions were intentionally excluded from the public repository.


## Notebook format

All public notebooks in `code/` contain executable code cells only. Markdown/raw cells,
inline comments, standalone comments, outputs, and execution counts were removed from the
public copies. Scientific documentation is kept in the repository Markdown files and in the
manuscript rather than inside the notebooks.

## Data

Raw third-party data are **not redistributed by default** in this repository. The repository includes temporal split definitions and processed experimental artifacts that can be shared. See `data/README.md` and `data/SOURCES_AND_RECONSTRUCTION.md` for the data policy, provenance, and reconstruction guidance.

## Main reproducibility artifacts

### Fantasy football

The repository includes temporal development folds, frozen predictive hyperparameters and ensemble weights, DOC weight grid and frozen DOC weights, bootstrap stability results, out-of-time 2025 operational summaries, temporal replication comparisons, component ablation, captain-selection sensitivity, target-alignment and missing-next-market audits, local calibration sensitivity, and leakage/freeze audits.

### Energy

The repository includes temporal replication definitions, frozen representation parameters, the extended-theta robustness experiment, capacity-margin × VOLL robustness summaries, and replication-level/model-level summaries.

## Reproducing paper claims

See `reproducibility/artifact_manifest.csv`, which maps manuscript claims and analyses to the corresponding repository artifacts and code.

## Supplementary material

The LaTeX source for the Supplementary Material is available in `supplementary/`.

## Software environment

Exact package versions should be recorded before the public release in `reproducibility/environment.yml` or `reproducibility/requirements.txt`.

## Citation

Citation metadata are provided in `CITATION.cff`. The archived release DOI can be added after creating a versioned release.

## License

The original source code in this repository is released under the MIT License unless otherwise indicated. Third-party datasets, external software, and external test systems retain their original licenses and terms of use. The MIT License does **not** apply to third-party data.
