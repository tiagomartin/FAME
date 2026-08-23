# Reproducibility

This directory contains only the files required to understand and verify the
reproducibility workflow of the FAME experiments.

## Files

- `CLEAN_CLONE_WORKFLOW.md` — execution order and clean-clone reproduction procedure.
- `artifact_manifest.csv` — maps manuscript claims/results to the corresponding
  repository artifacts and reproduction code.

The archived numerical evidence used in the manuscript is stored under `results/`.
Fresh executions should write to `reproduced/`, preserving the archived paper results.

External data requirements and acquisition instructions are documented under `data/`.
