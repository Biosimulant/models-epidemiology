# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Smith&Moore2004 - The SIR model for the spread of HongKong Flu."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000001045'
    _TITLE = 'Smith&Moore2004 - The SIR model for the spread of HongKong Flu'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected', 'Susceptible', 'Recovered']
    _SPECIES_LABELS = {'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 0.5, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.')}
    _HEADLINE_OUTPUTS = {'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Smithandmoore2004TheSirModelForTheSpreadOBiomd0000001045Model = CuratedEpidemiologySBMLModel
