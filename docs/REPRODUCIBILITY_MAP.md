# Reproducibility map

## FAME/DOC temporal-transferability manuscript

Folder: `reproducibility/fame_doc/`

| Scientific component | Main artifact |
|---|---|
| Fantasy-football main analysis | `FAME_IJDSA_v11_1_CORRIGIDO_FINAL.ipynb` |
| 2024 DOC calibration/test analysis | `FAME_DOC_02_calibracao_teste_KBS_v4_1_ablation_corrigido.ipynb` |
| H2 temporal replication | `FAME_temporal_replication_H2_2021_2022_2023_2024.ipynb` |
| Energy DOC calibration | `FAME_Energy_05_v2.1_DOC_Calibration_i7_12700K.ipynb` |
| Energy temporal robustness | `FAME_Energy_TemporalReplication_v3.2_RobustnessMargins.ipynb` |

The existing v1.0.2 archive contains additional processed outputs, temporal
split definitions, frozen parameters, and audit artifacts used by the transfer
study. v1.1.0 preserves that material and adds an explicit companion-manuscript
organization.

## DRR/DRVM monitoring manuscript

Folder: `reproducibility/drvm/`

| Scientific component | Main artifact |
|---|---|
| Null audit, finite-horizon power/delay, monitorability | `FAME_DRVM_final_validation_v8.ipynb` |
| Real fantasy-football and Energy deployment replays | `FAME_DRVM_real_applications_v10.ipynb` |
| Temporal reference-risk and baseline-uplift stress tests | `FAME_DRVM_temporal_robustness_v12.ipynb` |
| Machine-readable Monte Carlo outputs | `mc_results_v8.zip` |
| Real-replay outputs | `results_drvm_real_v10.zip` |
| Temporal robustness outputs | `results_drvm_temporal_robustness_v12.zip` |

## Audit principle

Every public numerical claim should be traceable to:

1. a versioned notebook or script;
2. a machine-readable result artifact where feasible;
3. a fixed chronological protocol;
4. a frozen parameter definition;
5. a repository release tag and corresponding Zenodo archive.
