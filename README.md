# FAME

FAME is a modular prediction-to-decision framework for constrained resource allocation.

This repository contains the curated code, processed experimental artifacts, robustness analyses, figures, and supplementary material accompanying the manuscript:

**Temporal Transferability of Prediction-to-Decision Representations in Constrained Resource Allocation**

## Repository purpose

The repository is organized to make the paper's empirical claims auditable. It separates predictive development, decision-oriented calibration (DOC), frozen prediction-to-decision representations, future out-of-time evaluation, and retrospective robustness and diagnostic analyses.

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

The repository provides the curated numerical artifacts, temporal split definitions, frozen parameters, analysis code, and supporting documentation required to audit the empirical claims reported in the manuscript.

The archived results can be inspected without access to the original raw datasets. End-to-end re-execution of analyses that depend on external or third-party data additionally requires the corresponding source data described in `data/README.md` and `data/SOURCES_AND_RECONSTRUCTION.md`.

The clean-clone verification procedure is documented in `reproducibility/CLEAN_CLONE_WORKFLOW.md`.

## Code

The `code/` directory contains the notebooks used for the final fantasy-football and Energy experiments reported in the manuscript. Development, debugging, and obsolete intermediate notebooks were intentionally excluded from the public repository.

## Notebook format

All public notebooks in `code/` contain executable code cells only. Markdown and raw cells, inline and standalone comments, stored outputs, and execution counts were removed from the public copies.

Scientific documentation is provided in the repository Markdown files and in the manuscript rather than inside the notebooks.

## Data

Raw third-party data are not redistributed by default in this repository.

The repository includes temporal split definitions and processed experimental artifacts that can be shared. Data provenance, external sources, expected input structures, redistribution considerations, and reconstruction guidance are documented in `data/README.md` and `data/SOURCES_AND_RECONSTRUCTION.md`.

## Main reproducibility artifacts

### Fantasy football

The repository includes:

- temporal development folds;
- frozen predictive hyperparameters and ensemble weights;
- DOC weight grid and frozen DOC weights;
- bootstrap stability results;
- out-of-time 2025 operational summaries;
- temporal replication comparisons;
- component ablation analyses;
- captain-selection sensitivity analyses;
- target-alignment and missing-next-market audits;
- local calibration sensitivity analyses; and
- leakage and freeze audits.

### Energy

The repository includes:

- temporal replication definitions;
- frozen representation parameters;
- extended-theta robustness experiments;
- capacity-margin × VOLL robustness summaries; and
- replication-level and model-level summaries.

## Reproducing paper claims

The file `reproducibility/artifact_manifest.csv` maps manuscript claims and analyses to the corresponding archived artifacts and analysis code.

This mapping is intended to provide a direct audit trail from the results reported in the manuscript to the machine-readable outputs and code stored in the repository.

## Computational environment

The manuscript experiments were executed using **Python 3.13.14**.

The direct Python dependencies and the versions used in the manuscript-associated computational environment are recorded in `requirements.txt`.

A compatible virtual environment can be created with:

```bash
python -m venv .venv
```

Activate the environment and install the required dependencies with:

```bash
python -m pip install -r requirements.txt
```

The archived numerical results in `results/` correspond to the manuscript-associated computational environment documented above.

## Clean-clone workflow

Instructions for verifying the repository from a clean clone are provided in:

`reproducibility/CLEAN_CLONE_WORKFLOW.md`

Because some experiments rely on external or third-party datasets that are not redistributed in this repository, the clean-clone workflow distinguishes between:

1. auditing the archived manuscript results; and
2. re-executing analyses after supplying the required external data.

## Supplementary material

The LaTeX source and supporting files for the Supplementary Material are available in `supplementary/`.

## Citation

Citation metadata for the FAME software and the associated manuscript are provided in `CITATION.cff`.

The manuscript-associated software release is archived on Zenodo:

**FAME v1.0.1**  
**DOI: 10.5281/zenodo.22071478**

The Zenodo concept DOI representing all versions of FAME is:

**DOI: 10.5281/zenodo.22071477**

## License

The original source code in this repository is released under the MIT License unless otherwise indicated.

Third-party datasets, external software, and external test systems retain their original licenses and terms of use. The MIT License does not apply to third-party data.
