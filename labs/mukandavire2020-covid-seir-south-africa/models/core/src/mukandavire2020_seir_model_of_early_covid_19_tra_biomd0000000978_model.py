# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Mukandavire2020 - SEIR model of early COVID-19 transmission in South Africa."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000978'
    _TITLE = 'Mukandavire2020 - SEIR model of early COVID-19 transmission in South Africa'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed', 'Infected', 'Susceptible', 'Recovered']
    _SPECIES_LABELS = {'Exposed': 'Exposed', 'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 1.3, 'native model units', 'COVID-19 transmission-rate parameter. Maps to SBML symbol `beta`.'), 'exposed_progression_rate': ('sigma', 0.311, 'native model units', 'Exposed-to-infected progression parameter. Maps to SBML symbol `sigma`.'), 'recovery_rate': ('gamma', 0.3389830508, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Mukandavire2020SeirModelOfEarlyCovid19TraBiomd0000000978Model = CuratedEpidemiologySBMLModel
