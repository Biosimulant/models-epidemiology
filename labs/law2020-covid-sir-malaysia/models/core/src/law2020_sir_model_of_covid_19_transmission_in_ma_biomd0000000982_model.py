# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000982'
    _TITLE = 'Law2020 - SIR model of COVID-19 transmission in Malyasia with time-varying parameters'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected', 'Susceptible', 'Removed']
    _SPECIES_LABELS = {'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Removed': 'Removed'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 0.4114, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.')}
    _HEADLINE_OUTPUTS = {'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'removed': ('Removed', 'native SBML value', 'Removed. Maps to SBML symbol `Removed`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Law2020SirModelOfCovid19TransmissionInMaBiomd0000000982Model = CuratedEpidemiologySBMLModel
