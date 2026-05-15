# Hou2020 - SEIR model of COVID-19 transmission in Wuhan

This Biosimulant lab wraps `Hou2020 - SEIR model of COVID-19 transmission in Wuhan` as a runnable epidemiology model with a companion visualization module.
A novel coronavirus pneumonia, first identified in Wuhan City and referred to as COVID-19 by the World Health Organization, has been quickly spreading to other cities and countries. It can be used to explore transmission dynamics and compare scenario outcomes across conditions.

## What You'll See

The lab asks: When does the Wuhan SEIR outbreak peak in the baseline run? It runs for 10.0 time units with a communication step of 0.1. The run uses the model defaults declared by the curated SBML wrapper. The generated visualizations focus on Exposed, Infected, Susceptible, Recovered, and Total Population, combining trajectory, endpoint-comparison, and summary-table views from one completed dark-mode run.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

![Hou2020 - SEIR model of COVID-19 transmission in Wuhan - timeseries visualization](assets/01-selected-state-variables-from-the-bundled-source-model.png)

*Time-series view for Hou2020 - SEIR model of COVID-19 transmission in Wuhan, showing selected epidemiology state trajectories across the 10.0 simulation. The card is useful for reading peak timing, depletion, recovery, and persistence across Exposed, Infected, Susceptible, Recovered, and Total Population.*

![Hou2020 - SEIR model of COVID-19 transmission in Wuhan - bar visualization](assets/02-latest-finite-values-for-selected-epidemiology-observables.png)

*Latest-value comparison for Hou2020 - SEIR model of COVID-19 transmission in Wuhan, ranking the finite end-of-run values for the selected epidemiology observables. This makes the dominant compartments and residual states easier to compare at the simulation endpoint.*

![Hou2020 - SEIR model of COVID-19 transmission in Wuhan - table visualization](assets/03-visualisation-table.png)

*Summary table for Hou2020 - SEIR model of COVID-19 transmission in Wuhan, collecting the run diagnostics reported by the visualization model, including duration simulated, observable coverage, largest change, and peak observable when available.*

<!-- BIOSIMULANT_VISUALS_END -->

## Model Context

- Core model: `models/core`
- Visualization model: `models/visualisation`
- Standard: `sbml`
- Upstream source: `biomodels_ebi:BIOMD0000000970`
- License: `CC0`

## Inputs

| Input | Maps To | Notes |
|---|---|---|
| Recovery Rate | `epidemiology_sbml_hou2020_seir_model_of_covid_19_transmission_in_w_biomd0000000970_model.recovery_rate` | Uses the model default unless overridden at run time. |

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
| Total Population | `Total_Population` | Available to the visualization model and downstream workflows. |

## Runtime

- Duration: `10.0`
- Communication step: `0.1`
- Capture run ID: `8ce5d732-a00f-4015-a445-e5855a4b2160`

## Running Locally

```bash
biosimulant labs serve .
```
