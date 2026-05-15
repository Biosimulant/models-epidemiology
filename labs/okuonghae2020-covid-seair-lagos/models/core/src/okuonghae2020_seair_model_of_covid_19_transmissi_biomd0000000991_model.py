# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Okuonghae2020 - SEAIR model of COVID-19 transmission in Lagos, Nigeria."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000991'
    _TITLE = 'Okuonghae2020 - SEAIR model of COVID-19 transmission in Lagos, Nigeria'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['asymptomatic', 'exposed', 'deceased', 'susceptible', 'recovered', 'symptomatic', 'detected', 'detected_cumulative']
    _SPECIES_LABELS = {'asymptomatic': 'Asymptomatic', 'exposed': 'Exposed', 'deceased': 'Deceased', 'susceptible': 'Susceptible', 'recovered': 'Recovered', 'symptomatic': 'Symptomatic', 'detected': 'Detected', 'detected_cumulative': 'Detected cumulative'}
    _PARAMETER_INPUTS = {'incubation_rate': ('sigma', 0.192307692307692, 'native model units', 'Incubation/progression-rate parameter. Maps to SBML symbol `sigma`.')}
    _HEADLINE_OUTPUTS = {'asymptomatic': ('asymptomatic', 'native SBML value', 'Asymptomatic. Maps to SBML symbol `asymptomatic`.'), 'exposed': ('exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `exposed`.'), 'deceased': ('deceased', 'native SBML value', 'Deceased. Maps to SBML symbol `deceased`.'), 'susceptible': ('susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `susceptible`.'), 'recovered': ('recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `recovered`.'), 'symptomatic': ('symptomatic', 'native SBML value', 'Symptomatic. Maps to SBML symbol `symptomatic`.'), 'detected': ('detected', 'native SBML value', 'Detected. Maps to SBML symbol `detected`.'), 'detected_cumulative': ('detected_cumulative', 'native SBML value', 'Detected cumulative. Maps to SBML symbol `detected_cumulative`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Okuonghae2020SeairModelOfCovid19TransmissiBiomd0000000991Model = CuratedEpidemiologySBMLModel
