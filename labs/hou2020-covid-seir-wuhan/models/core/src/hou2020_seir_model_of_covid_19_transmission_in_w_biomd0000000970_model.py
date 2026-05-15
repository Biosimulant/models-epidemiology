# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Hou2020 - SEIR model of COVID-19 transmission in Wuhan."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000970'
    _TITLE = 'Hou2020 - SEIR model of COVID-19 transmission in Wuhan'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed', 'Infected', 'Susceptible', 'Recovered', 'Total_Population']
    _SPECIES_LABELS = {'Exposed': 'Exposed', 'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Total_Population': 'Total Population'}
    _PARAMETER_INPUTS = {'recovery_rate': ('gamma', 0.048, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'total_population': ('Total_Population', 'native SBML value', 'Total Population. Maps to SBML symbol `Total_Population`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Hou2020SeirModelOfCovid19TransmissionInWBiomd0000000970Model = CuratedEpidemiologySBMLModel
