# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Weitz2020 - SIR model of COVID-19 transmission with shielding."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000963'
    _TITLE = 'Weitz2020 - SIR model of COVID-19 transmission with shielding'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected', 'Susceptible', 'Recovered']
    _SPECIES_LABELS = {'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 0.25, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.'), 'recovery_rate': ('gamma', 0.1, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Weitz2020SirModelOfCovid19TransmissionWitBiomd0000000963Model = CuratedEpidemiologySBMLModel
