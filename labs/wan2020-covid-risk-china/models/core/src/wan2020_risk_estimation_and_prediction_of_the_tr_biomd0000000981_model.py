# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Wan2020 - risk estimation and prediction of the transmission of COVID-19 in maninland China excluding Hubei province."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000981'
    _TITLE = 'Wan2020 - risk estimation and prediction of the transmission of COVID-19 in maninland China excluding Hubei province'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Recovered_from_hospitals', 'Susceptible_isolated', 'Exposed', 'Infected', 'Hospitalised', 'Deceased', 'Susceptible', 'Recovered', 'Asymptomatic', 'Total_reported_cases', 'Quarantined']
    _SPECIES_LABELS = {'Recovered_from_hospitals': 'Recovered from hospitals', 'Susceptible_isolated': 'Susceptible isolated', 'Exposed': 'Exposed', 'Infected': 'Infected', 'Hospitalised': 'Hospitalised', 'Deceased': 'Deceased', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 0.054043, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.')}
    _HEADLINE_OUTPUTS = {'recovered_from_hospitals': ('Recovered_from_hospitals', 'native SBML value', 'Recovered from hospitals. Maps to SBML symbol `Recovered_from_hospitals`.'), 'susceptible_isolated': ('Susceptible_isolated', 'native SBML value', 'Susceptible isolated. Maps to SBML symbol `Susceptible_isolated`.'), 'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'hospitalised': ('Hospitalised', 'native SBML value', 'Hospitalised. Maps to SBML symbol `Hospitalised`.'), 'deceased': ('Deceased', 'native SBML value', 'Deceased. Maps to SBML symbol `Deceased`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Wan2020RiskEstimationAndPredictionOfTheTrBiomd0000000981Model = CuratedEpidemiologySBMLModel
