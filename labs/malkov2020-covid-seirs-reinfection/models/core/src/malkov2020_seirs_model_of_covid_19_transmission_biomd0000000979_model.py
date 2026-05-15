# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Malkov2020 - SEIRS model of COVID-19 transmission with reinfection."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000979'
    _TITLE = 'Malkov2020 - SEIRS model of COVID-19 transmission with reinfection'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed', 'Infected', 'Susceptible', 'Recovered', 'Total_population']
    _SPECIES_LABELS = {'Exposed': 'Exposed', 'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Total_population': 'Total population'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 0.16668, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.'), 'recovery_rate': ('gamma', 0.05556, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.'), 'incubation_rate': ('sigma', 0.19231, 'native model units', 'Incubation/progression-rate parameter. Maps to SBML symbol `sigma`.')}
    _HEADLINE_OUTPUTS = {'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'total_population': ('Total_population', 'native SBML value', 'Total population. Maps to SBML symbol `Total_population`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Malkov2020SeirsModelOfCovid19TransmissionBiomd0000000979Model = CuratedEpidemiologySBMLModel
