# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Giordano2020 - SIDARTHE model of COVID-19 spread in Italy."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000955'
    _TITLE = 'Giordano2020 - SIDARTHE model of COVID-19 spread in Italy'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected', 'Susceptible', 'Diagnosed', 'Ailing', 'Recognized', 'Threatened', 'Healed', 'Extinct']
    _SPECIES_LABELS = {'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Diagnosed': 'Diagnosed', 'Ailing': 'Ailing', 'Recognized': 'Recognized', 'Threatened': 'Threatened', 'Healed': 'Healed', 'Extinct': 'Extinct'}
    _PARAMETER_INPUTS = {'undetected_transmission_rate': ('alpha', 0.57, 'native model units', 'Transmission parameter from infected undetected cases. Maps to SBML symbol `alpha`.'), 'diagnosed_transmission_rate': ('beta', 0.011, 'native model units', 'Transmission parameter from diagnosed cases. Maps to SBML symbol `beta`.'), 'ailing_transmission_rate': ('gamma', 0.456, 'native model units', 'Transmission parameter from ailing cases. Maps to SBML symbol `gamma`.'), 'recognition_rate': ('epsilon', 0.171, 'native model units', 'Diagnosis/recognition transition parameter. Maps to SBML symbol `epsilon`.'), 'severe_progression_rate': ('mu', 0.017, 'native model units', 'Progression parameter toward threatened/severe state. Maps to SBML symbol `mu`.'), 'healing_rate': ('lambda', 0.034, 'native model units', 'Healing/recovery transition parameter. Maps to SBML symbol `lambda`.')}
    _HEADLINE_OUTPUTS = {'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'diagnosed': ('Diagnosed', 'native SBML value', 'Diagnosed. Maps to SBML symbol `Diagnosed`.'), 'ailing': ('Ailing', 'native SBML value', 'Ailing. Maps to SBML symbol `Ailing`.'), 'recognized': ('Recognized', 'native SBML value', 'Recognized. Maps to SBML symbol `Recognized`.'), 'threatened': ('Threatened', 'native SBML value', 'Threatened. Maps to SBML symbol `Threatened`.'), 'healed': ('Healed', 'native SBML value', 'Healed. Maps to SBML symbol `Healed`.'), 'extinct': ('Extinct', 'native SBML value', 'Extinct. Maps to SBML symbol `Extinct`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Giordano2020SidartheModelOfCovid19SpreadIBiomd0000000955Model = CuratedEpidemiologySBMLModel
