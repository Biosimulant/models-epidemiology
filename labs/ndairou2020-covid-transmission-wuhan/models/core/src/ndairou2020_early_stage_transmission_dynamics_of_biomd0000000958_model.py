# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ndairou2020 - early-stage transmission dynamics of COVID-19 in Wuhan."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000958'
    _TITLE = 'Ndairou2020 - early-stage transmission dynamics of COVID-19 in Wuhan'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed', 'Infectious', 'Hospitalised', 'Fatalities', 'Susceptible', 'Recovered', 'Super_spreaders', 'Asymptomatic']
    _SPECIES_LABELS = {'Exposed': 'Exposed', 'Infectious': 'Infectious', 'Hospitalised': 'Hospitalised', 'Fatalities': 'Fatalities', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Super_spreaders': 'Super spreaders', 'Asymptomatic': 'Asymptomatic'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 2.8, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.')}
    _HEADLINE_OUTPUTS = {'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infectious': ('Infectious', 'native SBML value', 'Infectious. Maps to SBML symbol `Infectious`.'), 'hospitalised': ('Hospitalised', 'native SBML value', 'Hospitalised. Maps to SBML symbol `Hospitalised`.'), 'fatalities': ('Fatalities', 'native SBML value', 'Fatalities. Maps to SBML symbol `Fatalities`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'super_spreaders': ('Super_spreaders', 'native SBML value', 'Super spreaders. Maps to SBML symbol `Super_spreaders`.'), 'asymptomatic': ('Asymptomatic', 'native SBML value', 'Asymptomatic. Maps to SBML symbol `Asymptomatic`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Ndairou2020EarlyStageTransmissionDynamicsOfBiomd0000000958Model = CuratedEpidemiologySBMLModel
