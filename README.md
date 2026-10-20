# FAME

**Prediction-to-decision representations for constrained resource allocation**

FAME is a modular predictive-prescriptive framework that connects predictive information, parameterized prediction-to-decision representations, and constrained optimization to support operational resource-allocation decisions.

The framework separates predictive performance from realized decision utility. In particular, improvements in predictive accuracy do not necessarily translate into proportional improvements in downstream operational outcomes.

This repository contains the research code, curated experimental artifacts, robustness analyses, figures, and documentation supporting the FAME research program.

## FAME v1.1.0 — Companion research tracks

Version 1.1.0 extends the FAME reproducibility infrastructure to support two complementary research tracks concerned with prediction-to-decision representations.

### FAME/DOC — Temporal transferability

This track investigates the learning, calibration stability, and temporal transferability of prediction-to-decision representations through **Decision-Oriented Calibration (DOC)**.

DOC selects representation parameters using historical realized utility. Once calibrated, the representation is frozen and evaluated in subsequent chronological periods.

The central research question is:

> Do historically decision-calibrated representations preserve operational value when transferred to future environments?

The analysis distinguishes predictive transfer from representation transfer. Changes in predictive performance and changes in downstream decision utility need not evolve proportionally.

Three application domains are examined:

- **Fantasy football:** chronological transfer of decision-calibrated representations under team-selection constraints.
- **Energy:** temporal transfer and robustness of representations used in constrained operational decisions.
- **GPU allocation:** calibration, frozen temporal transfer, and external comparisons with Native GFS under matched deployment origins.

The theoretical analysis distinguishes calibration estimation error, temporal representation shift, and representation-class approximation error.

**Research resources**

- [Manuscript scope](docs/MANUSCRIPTS.md)
- [Reproducibility map](docs/REPRODUCIBILITY_MAP.md)
- [FAME/DOC reproducibility materials](reproducibility/fame_doc/)
- [GPU allocation application](applications/gpu_allocation/)

### DRR/DRVM — Post-deployment validity monitoring

This research track examines the continued validity of a frozen prediction-to-decision representation after deployment.

It introduces **Decision-Representation Regret (DRR)** and the **Decision-Representation Validity Monitor (DRVM)**, together with reference-risk robustness, monitorability analysis, and post-alert representation renewal.

The central research question is:

> When has a frozen representation accumulated enough downstream evidence to warrant operational review?

**Research resources**

- [Manuscript scope](docs/MANUSCRIPTS.md)
- [Reproducibility map](docs/REPRODUCIBILITY_MAP.md)
- [DRR/DRVM reproducibility materials](reproducibility/drvm/)

---

## GPU Allocation Application

The repository includes a dedicated GPU resource-allocation application of FAME and Decision-Oriented Calibration (DOC).

The application examines how historically calibrated prediction-to-decision representations behave when transferred to future deployment periods.

The computational experiments cover predictive baselines, representation calibration, frozen temporal transfer, and matched-origin comparisons with Native GFS.

### Experimental organization

The GPU application contains seven principal notebooks:

| Notebook | Experimental component |
|---|---|
| `FAME_GPU_01_data_audit_v2.ipynb` | Data inspection and audit |
| `FAME_GPU_02_predictive_baselines.ipynb` | Predictive baselines |
| `FAME_GPU_03B_demand_alignment_binding_audit.ipynb` | Demand alignment and binding audit |
| `FAME_GPU_04A_DOC_calibration_v3_parallel.ipynb` | Decision-Oriented Calibration |
| `FAME_GPU_04B_frozen_transfer_parallel_v4.ipynb` | Frozen temporal transfer |
| `FAME_GPU_04C.ipynb` | Additional GPU experimental analysis |
| `FAME_GPU_05_v7_matched_origin_GFS.ipynb` | Matched-origin Native GFS benchmark |

The accompanying results directory contains machine-readable experimental outputs, diagnostic summaries, and figures.

### Interpretation of the GPU comparisons

The GPU experiments distinguish two comparisons.

**1. Incremental DOC contribution**

DOC is compared with a fixed FAME reference under the relevant evaluation protocol. This comparison assesses the incremental operational value associated with selecting the prediction-to-decision representation through historical calibration.

**2. External FAME–GFS comparison**

FAME is also compared with Native GFS using matched deployment origins.

The overall difference between FAME and Native GFS must not be attributed entirely to DOC. It includes the difference associated with the fixed FAME reference and the incremental contribution of DOC.

The matched-origin comparison is an external operational benchmark, not a causal ablation of the FAME architecture.

Results across deployment origins are reported as temporal experimental diagnostics and should not automatically be interpreted as independent and identically distributed replications or population-level inference.

The experiments do not establish universal superiority across GPU workloads, operational conditions, or deployment environments.

**Access the application:**

[GPU allocation notebooks, results, and documentation](applications/gpu_allocation/)

---

## Repository purpose

The repository is organized to make the empirical claims of the FAME research program auditable.

For FAME/DOC, it distinguishes:

1. Predictive development and predictive performance.
2. Parameterized prediction-to-decision representations.
3. Constrained optimization.
4. Historical calibration using realized utility.
5. Frozen representation transfer to future periods.
6. Retrospective robustness and diagnostic analyses.

Predictive models and contextual information may be updated according to the experimental protocol, while the representation parameters selected through DOC remain frozen during the corresponding future evaluation.

Future-period outcomes are not used to reselect the representation evaluated prospectively.

## Repository structure

```text
FAME/
├── applications/
│   └── gpu_allocation/
│       ├── README.md
│       ├── notebooks/
│       └── resultados/
│
├── code/
│   ├── fantasy_football/
│   └── energy/
│
├── data/
│   ├── fantasy_football/
│   │   └── splits/
│   └── energy/
│       └── splits/
│
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
│
├── figures/
│   ├── main/
│   └── supplementary/
│
├── supplementary/
│
├── reproducibility/
│   ├── fame_doc/
│   ├── drvm/
│   ├── CLEAN_CLONE_WORKFLOW.md
│   ├── artifact_manifest.csv
│   ├── artifact_manifest_v1.1.0.csv
│   └── checksums.sha256
│
├── docs/
│   ├── MANUSCRIPTS.md
│   └── REPRODUCIBILITY_MAP.md
│
├── release/
│   ├── RELEASE_NOTES_v1.1.0.md
│   ├── GITHUB_UPDATE_PLAN.md
│   └── ZENODO_METADATA_v1.1.0.md
│
├── scripts/
├── README.md
├── CITATION.cff
├── CHANGELOG.md
├── requirements.txt
├── .zenodo.json
└── .gitignore
```

The GPU application is maintained in `applications/gpu_allocation/`, independently of the existing fantasy-football and energy directories.

## Reproducibility status

The repository provides curated numerical artifacts, temporal split definitions, frozen representation parameters, analysis code, and supporting documentation for auditing the empirical claims.

Archived results can be inspected without access to the original raw datasets.

Re-execution of experiments that depend on external or third-party data additionally requires the corresponding analytical inputs and computational environment.

Data provenance, redistribution restrictions, and reconstruction guidance are documented in:

- [Data documentation](data/README.md)
- [Sources and reconstruction](data/SOURCES_AND_RECONSTRUCTION.md)
- [Clean-clone workflow](reproducibility/CLEAN_CLONE_WORKFLOW.md)

The repository does not claim complete raw-source-to-result reconstruction for third-party datasets whose full transformation pipelines or original inputs are not redistributed.

The GPU application provides notebooks and archived experimental outputs. Availability of these artifacts does not, by itself, establish that every experiment can be re-executed without additional inputs or environment-specific dependencies.

## Code and notebook format

The `code/` directory contains the notebooks associated with the final fantasy-football and energy experiments.

The `applications/gpu_allocation/notebooks/` directory contains the principal computational notebooks associated with the GPU application.

Public notebooks have been prepared to emphasize executable computational content. Scientific explanations, experimental scope, interpretation, and reproducibility boundaries are provided through the repository documentation and associated manuscripts.

The GPU notebooks and archived outputs should be treated as versioned research artifacts. The availability of stored results does not imply that every notebook has been independently re-executed in a clean environment.

## Data

Raw third-party datasets are not redistributed by default.

The repository includes shareable temporal split definitions and processed experimental artifacts.

External sources, expected input structures, redistribution considerations, and reconstruction instructions are described in the corresponding data documentation.

## Main reproducibility artifacts

### Fantasy football

The repository includes:

- Temporal development folds and chronological evaluation definitions.
- Frozen predictive hyperparameters and ensemble weights.
- DOC candidate grids and selected representation weights.
- Bootstrap stability results.
- Out-of-time operational summaries.
- Temporal replication comparisons.
- Component ablation analyses.
- Captain-selection sensitivity analyses.
- Target-alignment and missing-next-market audits.
- Local calibration sensitivity analyses.
- Leakage and freeze audits.

### Energy

The repository includes:

- Temporal replication definitions.
- Frozen representation parameters.
- Extended-theta robustness experiments.
- Capacity-margin and value-of-lost-load robustness summaries.
- Replication-level and model-level summaries.
- Diagnostics relating predictive changes to operational outcomes.

### GPU allocation

The repository includes:

- Data inspection and alignment audits.
- Predictive baseline experiments.
- DOC representation calibration.
- Frozen temporal transfer experiments.
- Deployment-origin operational summaries.
- Matched-origin comparisons with Native GFS.
- Machine-readable results and diagnostic figures.
- Runtime and execution-related outputs where archived.

The GPU experiments distinguish the incremental DOC comparison from the external FAME–GFS benchmark.

## Reproducing manuscript claims

The file [`reproducibility/artifact_manifest.csv`](reproducibility/artifact_manifest.csv) provides the existing mapping between manuscript claims and archived research artifacts.

The GPU application has its own documentation and experimental outputs under [`applications/gpu_allocation/`](applications/gpu_allocation/).

The GPU application is included in the FAME v1.2.0 Zenodo archive (https://doi.org/10.5281/zenodo.23506235). The existing release-specific artifact manifests may not yet enumerate all GPU files; consult `applications/gpu_allocation/` for the GPU notebooks and outputs.

## Computational environment

The previously documented manuscript experiments used **Python 3.13.14**.

The Python dependencies associated with the existing reproducibility environment are recorded in [`requirements.txt`](requirements.txt).

A virtual environment can be created using:

```bash
python -m venv .venv
```

Install the documented dependencies with:

```bash
python -m pip install -r requirements.txt
```

The existing clean-clone verification applies to the environment and artifacts documented for that verification.

The GPU application may require additional dependencies, computational resources, external datasets, or environment-specific configuration. Its complete execution environment should be verified separately before claiming end-to-end reproducibility.

## Clean-clone workflow

Instructions for verifying the previously documented repository artifacts are available in:

[`reproducibility/CLEAN_CLONE_WORKFLOW.md`](reproducibility/CLEAN_CLONE_WORKFLOW.md)

The workflow distinguishes between auditing archived manuscript results and re-executing analyses that require external analytical inputs.

GPU-specific reproducibility information is available through the application directory.

## Supplementary material and computational artifacts

The LaTeX source and supporting files for the scientific Supplementary Material are maintained in [`supplementary/`](supplementary/).

Computational notebooks and machine-readable experimental outputs are distributed through the public GitHub repository and versioned Zenodo archives. The GPU application is included in FAME v1.2.0 (https://doi.org/10.5281/zenodo.23506235).

The GPU notebooks are not intended to be submitted as separate notebook attachments to the journal. Instead, the associated manuscript can cite the permanent archived research artifacts.

A GitHub commit and a Zenodo deposit serve different purposes: the former records repository development, whereas the latter provides a citable, versioned research archive.

## Versioning and Zenodo archive

### FAME v1.2.0 — GPU Allocation and DOC Experiments

The versioned research archive includes the GPU allocation notebooks, archived experimental outputs, and accompanying documentation, alongside the existing FAME/DOC and DRR/DRVM research materials.

**Version-specific DOI:**  
https://doi.org/10.5281/zenodo.23506235

The GPU experiments distinguish the incremental contribution of DOC relative to a fixed FAME reference from the external matched-origin benchmark against Native GFS. The latter is not a causal architecture ablation. Archived outputs are auditable, but complete re-execution may require additional inputs and environment-specific configuration.

### FAME v1.1.0

Companion research tracks and DRR/DRVM computational artifacts.

**Version-specific DOI:**  
https://doi.org/10.5281/zenodo.22730680

### FAME v1.0.2

Previous reproducibility hardening release.

**Version-specific DOI:**  
https://doi.org/10.5281/zenodo.22072076

### FAME concept DOI

The concept DOI identifies the FAME archive across versions and resolves to the latest published version.

**Concept DOI:**  
https://doi.org/10.5281/zenodo.22071477

## Citation

Citation metadata for FAME and its associated research outputs are provided in [`CITATION.cff`](CITATION.cff).

For reproducibility, readers should cite the version-specific Zenodo DOI corresponding to the exact research artifacts used.

For general reference to the FAME software and research program, the concept DOI may be used.

## License

Original source code in this repository is released under the MIT License unless otherwise indicated.

Third-party datasets, external software, and external test systems retain their original licenses and terms of use.

The MIT License does not automatically extend to third-party datasets or externally licensed artifacts.
