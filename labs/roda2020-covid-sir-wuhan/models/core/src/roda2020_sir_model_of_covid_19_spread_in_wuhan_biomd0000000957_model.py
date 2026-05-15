# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Roda2020 - SIR model of COVID-19 spread in Wuhan."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000957'
    _TITLE = 'Roda2020 - SIR model of COVID-19 spread in Wuhan'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected', 'Susceptible', 'Recovered', 'Confirmed']
    _SPECIES_LABELS = {'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Confirmed': 'Confirmed'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 2.09e-07, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.')}
    _HEADLINE_OUTPUTS = {'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'confirmed': ('Confirmed', 'native SBML value', 'Confirmed. Maps to SBML symbol `Confirmed`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Roda2020SirModelOfCovid19SpreadInWuhanBiomd0000000957Model = CuratedEpidemiologySBMLModel
