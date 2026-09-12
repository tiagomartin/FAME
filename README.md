# FAME — Framework for Allocation with Modular Evaluation

FAME is a modular predictive-prescriptive research framework for learning,
evaluating, and monitoring **prediction-to-decision representations** in
constrained optimization systems.

The repository now supports two complementary research tracks:

1. **FAME/DOC — temporal transferability**
   - learns an intermediate prediction-to-decision representation using
     downstream realized utility;
   - freezes that representation before future evaluation;
   - studies whether decision-calibrated representations transfer across time.

2. **DRR/DRVM — post-deployment validity monitoring**
   - defines Decision-Representation Regret (DRR);
   - monitors a frozen representation using an anytime-valid
     Decision-Representation Validity Monitor (DRVM);
   - studies representation separability, monitorability, temporal
     reference-risk robustness, and post-alert representation renewal.

These tracks are scientifically complementary but use distinct empirical
outputs and distinct inferential questions. See
[`docs/MANUSCRIPTS.md`](docs/MANUSCRIPTS.md) and
[`docs/REPRODUCIBILITY_MAP.md`](docs/REPRODUCIBILITY_MAP.md).

## Repository

Source repository:

https://github.com/tiagomartin/FAME

## Current public archive

The most recent previously archived release is:

**FAME v1.0.2**
DOI: **10.5281/zenodo.22072076**

Release **v1.1.0** extends the public reproducibility archive with the two
companion manuscript tracks described above. After the new Zenodo version is
published, the version-specific v1.1.0 DOI should be added here.

## Research architecture

The core FAME architecture separates:

```text
prediction
    ↓
prediction-to-decision representation
    ↓
constrained optimization
    ↓
realized downstream utility
```

A parameterized representation may be written as

```text
v_t(phi) = g_phi(theta_hat_t, z_t)
```

and DOC estimates `phi` using downstream realized utility in a chronological
calibration period. The selected representation is then frozen before future
evaluation.

The DRVM companion work begins after freezing: it asks whether the same
representation remains operationally valid as predictive inputs, contexts,
and operating conditions evolve.

## Companion manuscripts

### A. Temporal transferability of learned prediction-to-decision representations

**Working title**

*Temporal Transferability of Learned Prediction-to-Decision Representations in
Predictive-Prescriptive Systems*

Main scientific question:

> Do historically decision-calibrated prediction-to-decision representations
> preserve operational value when transferred to future environments?

Reproducibility materials:

[`reproducibility/fame_doc/`](reproducibility/fame_doc/)

Primary analyses include:

- three fantasy-football calibration-to-evaluation transitions;
- DOC calibration stability;
- retrospective displacement of favorable representation regions;
- nine expanding-window Energy transfer replications;
- predictive-versus-operational transfer analysis.

### B. Continuous validity monitoring of frozen prediction-to-decision representations

**Working title**

*Continuous Validity Monitoring of Frozen Prediction-to-Decision
Representations for Constrained Optimization*

Main scientific question:

> When has a frozen representation accumulated enough downstream evidence to
> warrant operational review?

Reproducibility materials:

[`reproducibility/drvm/`](reproducibility/drvm/)

Primary analyses include:

- controlled null/power Monte Carlo experiments;
- monitorability calculations;
- fantasy-football and Energy historical deployment replays;
- temporal reference-risk stress tests;
- baseline-uplift sensitivity;
- post-alert representation-renewal design.

## Reproducibility boundaries

The repository provides analysis code, processed experimental artifacts,
temporal protocol definitions, frozen parameters, robustness analyses, and
machine-readable outputs. Raw third-party data are not redistributed when
redistribution rights have not been established.

Archived numerical outputs are intended to permit auditing of manuscript
claims without redistribution of restricted raw data. Full re-execution of
analyses that depend on external third-party data requires the corresponding
external analytical inputs described in the repository documentation.

## Versioning

- `v1.0.2` — reproducibility archive for the original FAME temporal-transfer study.
- `v1.1.0` — companion-manuscript release separating:
  - FAME/DOC temporal transferability;
  - DRR/DRVM post-deployment monitoring and renewal.

See [`CHANGELOG.md`](CHANGELOG.md).

## Citation

Until article-specific DOIs become available, cite the software/reproducibility
archive using [`CITATION.cff`](CITATION.cff). Manuscript-specific citation
metadata will be added after acceptance/publication.

## License

This update does not change the repository's existing license. See the
repository `LICENSE` file.

## Authors

- Tiago Martins Pereira — Universidade Federal de Ouro Preto (UFOP)
- Diana Campos de Oliveira — Universidade Federal de Ouro Preto (UFOP)
