# models-epidemiology

Curated collection of **epidemiology** and **infectious disease** simulation models for the **biosim** platform. This repository contains comprehensive computational models of disease transmission, outbreak dynamics, intervention strategies, and host-pathogen interactions, with extensive COVID-19, malaria, and other infectious disease models.

## What's Inside

### Models (61 packages)

Each model is a self-contained simulation component with a `model.yaml` manifest.

**Epidemiology & Infectious Diseases** — disease transmission, outbreak modeling, and public health interventions:

#### COVID-19 Models
- `epidemiology-sbml-bertozzi2020-sir-model-of-scenarios-of-covid-19` — SIR scenarios for COVID-19 spread
- `epidemiology-sbml-giordano2020-sidarthe-model-of-covid-19-spread-i` — SIDARTHE compartmental model for Italy
- `epidemiology-sbml-carcione2020-deterministic-seir-simulation-of-a` — Deterministic SEIR for COVID-19
- `epidemiology-sbml-fang2020-seir-model-of-covid-19-transmission-con` — SEIR with control measures
- `epidemiology-sbml-hou2020-seir-model-of-covid-19-transmission-in-w` — SEIR for Wuhan transmission
- `epidemiology-sbml-cuadros2020-sihrd-spatiotemporal-model-of-covid` — SIHRD spatiotemporal dynamics
- `epidemiology-sbml-ghanbari2020-forecasting-the-second-wave-of-covi` — Second wave forecasting
- `epidemiology-sbml-by-covid-knowledge-graph-a-comprehensive-network` — COVID-19 knowledge graph network
- `epidemiology-sbml-covid-19-immunotherapy-a-mathematical-model` — Immunotherapy mathematical models
- `epidemiology-sbml-delattre2020-sars-cov-2-infected-human-lung-cell` — SARS-CoV-2 infected lung cells
- `epidemiology-sbml-gianlupi2022-antiviral-timing-potency-and-hetero` — Antiviral treatment timing and heterogeneity
- `epidemiology-sbml-juhasz2022-in-silico-evaluation-of-paxlovid-s-ph` — Paxlovid pharmacological evaluation
- `epidemiology-sbml-iar22-sars-cov-2-balf1-sars-cov-2-infection-mode` — SARS-CoV-2 BALF1 infection model

#### Malaria Models
- `epidemiology-sbml-chitnis2008-mathematical-model-of-malaria-transm` — Mathematical model of malaria transmission
- `epidemiology-sbml-ducrot2009-malaria-transmission-in-two-host-type` — Two-host-type malaria transmission
- `epidemiology-sbml-garira2019-a-coupled-multiscale-model-to-guide-m` — Multi-scale malaria control guidance

#### Other Infectious Diseases
- `epidemiology-sbml-chitnis2012-model-rift-valley-fever-transmission` — Rift Valley fever transmission
- `epidemiology-sbml-ho2019-mathematical-models-of-transmission-dynam` — General transmission dynamics
- `epidemiology-sbml-huo2017-seis-epidemic-model-with-the-impact-of-m` — SEIS with media impact
- `epidemiology-sbml-iar22-influenza-recon2-a-collection-of-cell-type` — Influenza cell-type-specific models

#### Host-Pathogen & Metabolic Models
- `epidemiology-sbml-bannerman2020-integrated-model-of-the-human-airw` — Integrated human airway model
- `epidemiology-sbml-fang2011-genome-scale-metabolic-network-of-burkh` — Burkholderia genome-scale metabolism
- `epidemiology-sbml-burbano2023-hgfsignaling-in-fattyliverdisease` — HGF signaling in fatty liver disease

#### Intervention & Control Strategies
- `epidemiology-sbml-kc2021-a-machine-learning-platform-to-estimate-a` — ML platform for intervention estimation

**Note:** This repository contains 61 models total, with major focus on COVID-19 (13+ models), malaria transmission, and general epidemiological frameworks. For a complete list, see the `models/` directory.

## Layout

```
models-epidemiology/
├── models/<model-slug>/     # One model package per folder, each with model.yaml
├── libs/                    # Shared helper code for curated models
├── templates/model-pack/    # Starter template for new model packs
├── scripts/                 # Manifest and entrypoint validation scripts
├── docs/                    # Governance documentation
└── .github/workflows/       # CI/CD pipeline
```

## How It Works

### Model Interface

Every model implements the `biosim.BioModule` interface:

- **`inputs()`** — declares named input signals the module consumes
- **`outputs()`** — declares named output signals the module produces
- **`advance_to(t)`** — advances the model's internal state to time `t`

Most curated models include Python source under `src/` and are wired together via `space.yaml` in composed simulations without additional code.

### Model Standards

All models in this repository:
- Use SBML (Systems Biology Markup Language) format
- Are sourced from BioModels and COVID-19 Disease Maps
- Include tellurium runtime for SBML execution
- Provide `state` output for monitoring simulation results
- Support configurable timesteps via `min_dt` parameter

### Epidemiological Model Types

Common compartmental models included:
- **SIR**: Susceptible-Infected-Recovered
- **SEIR**: Susceptible-Exposed-Infected-Recovered
- **SEIS**: Susceptible-Exposed-Infected-Susceptible
- **SIDARTHE**: Susceptible-Infected-Diagnosed-Ailing-Recognized-Threatened-Healed-Extinct
- **SIHRD**: Susceptible-Infected-Hospitalized-Recovered-Dead

### Running Models

Models are loaded and executed by the `biosim-platform`. The platform reads `model.yaml`, instantiates the model from its entrypoint, and runs the simulation loop at the configured timestep for the specified duration.

Models can be composed to simulate multi-scale outbreak dynamics, intervention scenarios, and public health policy evaluation.

## Getting Started

### Prerequisites

- Python 3.11+
- `biosim` framework

### Install biosim

```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

### Create a New Model

1. Copy `templates/model-pack/` to `models/<your-model-slug>/`
2. Edit `model.yaml` with metadata, entrypoint, and pinned dependencies
3. Implement your module (subclass `biosim.BioModule` or use compartmental framework)
4. Add epidemiology-specific tags and categorization
5. Validate: `python scripts/validate_manifests.py && python scripts/check_entrypoints.py`

### Using Models in Spaces

To integrate epidemiology models into scenario simulations:

1. Reference models by `manifest_path` (e.g., `models/epidemiology-sbml-bertozzi2020-sir-model-of-scenarios-of-covid-19/model.yaml`)
2. Wire model outputs to inputs for intervention scenarios
3. Compose multi-model simulations for policy evaluation
4. Configure runtime parameters and simulation duration

## Linking in biosim-platform

- Models can be linked with explicit paths:
  - `models/epidemiology-sbml-giordano2020-sidarthe-model-of-covid-19-spread-i/model.yaml`
- Epidemiology models can be composed with metabolic, immune, or pharmacological models for multi-scale disease modeling

## External Repos

External authors can keep models in independent repositories and link them directly in `biosim-platform`. This repository is curated, not exclusive.

## Validation & CI

Three scripts enforce repository integrity on every push:

| Script | Purpose |
|--------|---------|
| `scripts/validate_manifests.py` | Schema validation for all model.yaml files |
| `scripts/check_entrypoints.py` | Verifies Python entrypoints are importable and callable |
| `scripts/check_public_boundary.sh` | Prevents business-sensitive content in this public repo |

The CI pipeline (`.github/workflows/ci.yml`) runs: **secret scan** → **manifest validation** → **smoke sandbox** (Docker).

## Contributing

- All dependencies must use exact version pinning (`==`)
- Model slugs use kebab-case with domain prefix (`epidemiology-sbml-`)
- Models must follow the `biosim.BioModule` interface
- SBML models use tellurium runtime for execution
- Pre-commit hooks enforce trailing whitespace, EOF newlines, YAML syntax, and secret detection
- See [docs/PUBLIC_INTERNAL_BOUNDARY.md](docs/PUBLIC_INTERNAL_BOUNDARY.md) for content policy

## Domain-Specific Notes

**Epidemiology Focus Areas:**
- **Compartmental Models**: SIR, SEIR, SEIS, SIDARTHE, SIHRD frameworks
- **COVID-19 Pandemic**: Transmission dynamics, intervention scenarios, spatial spread, variant modeling
- **Vector-Borne Diseases**: Malaria and Rift Valley fever transmission with vector populations
- **Intervention Strategies**: Vaccination, social distancing, antiviral treatment, quarantine policies
- **Spatial Dynamics**: Geographic spread, metapopulation models, spatiotemporal forecasting
- **Host-Pathogen Interactions**: Within-host viral dynamics, immune response, treatment effects
- **Public Health Policy**: Scenario analysis, forecasting, resource allocation

**Common Features:**
- Time-dependent transmission rates (e.g., reflecting policy changes)
- Age-structured populations
- Healthcare capacity constraints
- Stochastic vs deterministic formulations
- Parameter estimation from outbreak data

## License

This repository is dual-licensed:

- **Code** (scripts, templates, Python modules): Apache-2.0 (`LICENSE-CODE.txt`)
- **Model/content** (manifests, docs, wiring/config): CC BY 4.0 (`LICENSE-CONTENT.txt`)

Attribution guidance: `ATTRIBUTION.md`
