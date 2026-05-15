# Chitnis2008 - Mathematical model of malaria transmission

This Biosimulant lab wraps `Chitnis2008 - Mathematical model of malaria transmission` as a runnable epidemiology model with a companion visualization module.
Mathematical model of malaria transmission for low and high transmission rates. It can be used to explore transmission dynamics and compare scenario outcomes across conditions.

## What You'll See

The lab asks: Which human and mosquito compartments carry malaria persistence in the baseline run? It runs for 10.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Exposed Human, Infected Human, Exposed Mosquito, Infected Mosquito, Susceptible Human, and Susceptible Mosquito, and related outputs, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Chitnis2008 - Mathematical model of malaria transmission - timeseries visualization](assets/01-selected-state-variables-from-the-bundled-source-model.png)

*Time-series view for Chitnis2008 - Mathematical model of malaria transmission, showing selected epidemiology state trajectories across the 10.0 simulation. The card is useful for reading peak timing, depletion, recovery, and persistence across Exposed Human, Infected Human, Exposed Mosquito, Infected Mosquito, Susceptible Human, and Susceptible Mosquito, and related outputs.*

![Chitnis2008 - Mathematical model of malaria transmission - bar visualization](assets/02-latest-finite-values-for-selected-epidemiology-observables.png)

*Latest-value comparison for Chitnis2008 - Mathematical model of malaria transmission, ranking the finite end-of-run values for the selected epidemiology observables. This makes the dominant compartments and residual states easier to compare at the simulation endpoint.*

![Chitnis2008 - Mathematical model of malaria transmission - table visualization](assets/03-visualisation-table.png)

*Summary table for Chitnis2008 - Mathematical model of malaria transmission, collecting the run diagnostics reported by the visualization model, including duration simulated, observable coverage, largest change, and peak observable when available.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `sbml`
- Upstream source: `biomodels_ebi:BIOMD0000000949`
- License: `CC0`

## Inputs

| Input | Maps To | Notes |
|---|---|---|
| Human To Mosquito Transmission | `epidemiology_sbml_chitnis2008_mathematical_model_of_malaria_transm_biomd0000000949_model.human_to_mosquito_transmission` | Uses the model default unless overridden at run time. |
| Mosquito To Human Transmission | `epidemiology_sbml_chitnis2008_mathematical_model_of_malaria_transm_biomd0000000949_model.mosquito_to_human_transmission` | Uses the model default unless overridden at run time. |
| Human Recovery Rate | `epidemiology_sbml_chitnis2008_mathematical_model_of_malaria_transm_biomd0000000949_model.human_recovery_rate` | Uses the model default unless overridden at run time. |
| Mosquito Mortality Rate | `epidemiology_sbml_chitnis2008_mathematical_model_of_malaria_transm_biomd0000000949_model.mosquito_mortality_rate` | Uses the model default unless overridden at run time. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| Model state | `state` | Available to the visualization model and downstream workflows. |
| Simulation summary | `summary` | Available to the visualization model and downstream workflows. |
| Species labels | `species_labels` | Available to the visualization model and downstream workflows. |
| Exposed Human | `Exposed_Human` | Available to the visualization model and downstream workflows. |
| Infected Human | `Infected_Human` | Available to the visualization model and downstream workflows. |
| Exposed Mosquito | `Exposed_Mosquito` | Available to the visualization model and downstream workflows. |
| Infected Mosquito | `Infected_Mosquito` | Available to the visualization model and downstream workflows. |
| Susceptible Human | `Susceptible_Human` | Available to the visualization model and downstream workflows. |
| Susceptible Mosquito | `Susceptible_Mosquito` | Available to the visualization model and downstream workflows. |
| Recovered | `Recovered` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `10.0`
- Communication step: `0.1`
- Capture run ID: `964fe409-bb4d-432e-a2e3-8e658724a426`

## Running Locally

```bash
biosimulant labs serve .
```
