# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Carcione2020 - Deterministic SEIR simulation of a COVID-19 outbreak."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000974'
    _TITLE = 'Carcione2020 - Deterministic SEIR simulation of a COVID-19 outbreak'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed', 'Infected', 'Deceased', 'Susceptible', 'Recovered', 'Total_population']
    _SPECIES_LABELS = {'Exposed': 'Exposed', 'Infected': 'Infected', 'Deceased': 'Deceased', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Total_population': 'Total population'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 0.833, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.'), 'recovery_rate': ('gamma', 0.125, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.'), 'incubation_rate': ('epsilon', 0.33333, 'native model units', 'Incubation/progression-rate parameter. Maps to SBML symbol `epsilon`.')}
    _HEADLINE_OUTPUTS = {'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'deceased': ('Deceased', 'native SBML value', 'Deceased. Maps to SBML symbol `Deceased`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'total_population': ('Total_population', 'native SBML value', 'Total population. Maps to SBML symbol `Total_population`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Carcione2020DeterministicSeirSimulationOfABiomd0000000974Model = CuratedEpidemiologySBMLModel
