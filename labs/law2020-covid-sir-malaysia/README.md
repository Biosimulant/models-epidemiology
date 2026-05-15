# Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters

This Biosimulant lab wraps `Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters` as a runnable epidemiology model with a companion visualization module.
The susceptible-infectious-removed (SIR) model offers the simplest framework to study transmission dynamics of COVID-19, however, it does not factor in its early depleting trend observed during a lock. It can be used to explore transmission dynamics and compare scenario outcomes across conditions.

## What You'll See

The lab asks: How does the Malaysia SIR model evolve under its time-varying transmission assumptions? It runs for 10.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Infected, Susceptible, and Removed, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters - timeseries visualization](assets/01-selected-state-variables-from-the-bundled-source-model.png)

*Time-series view for Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters, showing selected epidemiology state trajectories across the 10.0 simulation. The card is useful for reading peak timing, depletion, recovery, and persistence across Infected, Susceptible, and Removed.*

![Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters - bar visualization](assets/02-latest-finite-values-for-selected-epidemiology-observables.png)

*Latest-value comparison for Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters, ranking the finite end-of-run values for the selected epidemiology observables. This makes the dominant compartments and residual states easier to compare at the simulation endpoint.*

![Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters - table visualization](assets/03-visualisation-table.png)

*Summary table for Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters, collecting the run diagnostics reported by the visualization model, including duration simulated, observable coverage, largest change, and peak observable when available.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `sbml`
- Upstream source: `biomodels_ebi:BIOMD0000000982`
- License: `CC0`

## Inputs

| Input | Maps To | Notes |
|---|---|---|
| Transmission Rate | `epidemiology_sbml_law2020_sir_model_of_covid_19_transmission_in_ma_biomd0000000982_model.transmission_rate` | Uses the model default unless overridden at run time. |

## Outputs

| Output | Maps To | Role |
|---|---|---|
| Model state | `state` | Available to the visualization model and downstream workflows. |
| Simulation summary | `summary` | Available to the visualization model and downstream workflows. |
| Species labels | `species_labels` | Available to the visualization model and downstream workflows. |
| Infected | `Infected` | Available to the visualization model and downstream workflows. |
| Susceptible | `Susceptible` | Available to the visualization model and downstream workflows. |
| Removed | `Removed` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `10.0`
- Communication step: `0.1`
- Capture run ID: `d1303832-7934-4751-99dc-c94a5e6f5042`

## Running Locally

```bash
biosimulant labs serve .
```
