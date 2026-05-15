# Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan

This Biosimulant lab wraps `Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan` as a runnable epidemiology model with a companion visualization module.
Using the parameterized susceptible‐exposed‐infectious‐recovered model, we simulated the spread dynamics of coronavirus disease 2019 (COVID‐19) outbreak and impact of different control measures, condu. It can be used to explore transmission dynamics and compare scenario outcomes across conditions.

## What You'll See

The lab asks: Do intervention-modulated SEIR dynamics reduce the COVID-19 infection peak? It runs for 10.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Exposed, Infected, Susceptible, Recovered, and Total population, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan - timeseries visualization](assets/01-selected-state-variables-from-the-bundled-source-model.png)

*Time-series view for Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan, showing selected epidemiology state trajectories across the 10.0 simulation. The card is useful for reading peak timing, depletion, recovery, and persistence across Exposed, Infected, Susceptible, Recovered, and Total population.*

![Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan - bar visualization](assets/02-latest-finite-values-for-selected-epidemiology-observables.png)

*Latest-value comparison for Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan, ranking the finite end-of-run values for the selected epidemiology observables. This makes the dominant compartments and residual states easier to compare at the simulation endpoint.*

![Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan - table visualization](assets/03-visualisation-table.png)

*Summary table for Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan, collecting the run diagnostics reported by the visualization model, including duration simulated, observable coverage, largest change, and peak observable when available.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `sbml`
- Upstream source: `biomodels_ebi:BIOMD0000000984`
- License: `CC0`

## Inputs

| Input | Maps To | Notes |
|---|---|---|
| Transmission Rate | `epidemiology_sbml_fang2020_seir_model_of_covid_19_transmission_con_biomd0000000984_model.transmission_rate` | Uses the model default unless overridden at run time. |
| Baseline Transmission Rate | `epidemiology_sbml_fang2020_seir_model_of_covid_19_transmission_con_biomd0000000984_model.baseline_transmission_rate` | Uses the model default unless overridden at run time. |
| Recovery Rate | `epidemiology_sbml_fang2020_seir_model_of_covid_19_transmission_con_biomd0000000984_model.recovery_rate` | Uses the model default unless overridden at run time. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| Model state | `state` | Available to the visualization model and downstream workflows. |
| Simulation summary | `summary` | Available to the visualization model and downstream workflows. |
| Species labels | `species_labels` | Available to the visualization model and downstream workflows. |
| Exposed | `Exposed` | Available to the visualization model and downstream workflows. |
| Infected | `Infected` | Available to the visualization model and downstream workflows. |
| Susceptible | `Susceptible` | Available to the visualization model and downstream workflows. |
| Recovered | `Recovered` | Available to the visualization model and downstream workflows. |
| Total population | `Total_population` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `10.0`
- Communication step: `0.1`
- Capture run ID: `846d051e-d12c-42b0-a07b-59d97ba54011`

## Running Locally

```bash
biosimulant labs serve .
```
