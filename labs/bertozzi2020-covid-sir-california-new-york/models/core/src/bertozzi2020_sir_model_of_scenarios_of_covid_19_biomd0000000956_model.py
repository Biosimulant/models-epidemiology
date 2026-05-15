# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Bertozzi2020 - SIR model of scenarios of COVID-19 spread in CA and NY."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000956'
    _TITLE = 'Bertozzi2020 - SIR model of scenarios of COVID-19 spread in CA and NY'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected', 'Susceptible', 'Recovered']
    _SPECIES_LABELS = {'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'reproduction_number': ('Ro', 2.7, 'dimensionless', 'Basic reproduction number parameter. Maps to SBML symbol `Ro`.'), 'recovery_rate': ('gamma', 0.14, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Bertozzi2020SirModelOfScenariosOfCovid19Biomd0000000956Model = CuratedEpidemiologySBMLModel
