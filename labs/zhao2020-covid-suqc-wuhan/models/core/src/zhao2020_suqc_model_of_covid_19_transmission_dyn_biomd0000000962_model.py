# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Zhao2020 - SUQC model of COVID-19 transmission dynamics in Wuhan, Hubei, and China."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000962'
    _TITLE = 'Zhao2020 - SUQC model of COVID-19 transmission dynamics in Wuhan, Hubei, and China'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Unquarantined_Infected', 'Quarantined_Infected', 'Confirmed_Infected', 'Cumulative_Infected', 'Susceptible']
    _SPECIES_LABELS = {'Unquarantined_Infected': 'Unquarantined Infected', 'Quarantined_Infected': 'Quarantined Infected', 'Confirmed_Infected': 'Confirmed Infected', 'Cumulative_Infected': 'Cumulative Infected', 'Susceptible': 'Susceptible'}
    _PARAMETER_INPUTS = {'reproduction_number': ('R', 4.7092, 'dimensionless', 'Reproduction-number parameter. Maps to SBML symbol `R`.'), 'transmission_rate': ('beta', 0.05, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.'), 'incubation_rate': ('sigma', 0.0, 'native model units', 'Incubation/progression-rate parameter. Maps to SBML symbol `sigma`.')}
    _HEADLINE_OUTPUTS = {'unquarantined_infected': ('Unquarantined_Infected', 'native SBML value', 'Unquarantined Infected. Maps to SBML symbol `Unquarantined_Infected`.'), 'quarantined_infected': ('Quarantined_Infected', 'native SBML value', 'Quarantined Infected. Maps to SBML symbol `Quarantined_Infected`.'), 'confirmed_infected': ('Confirmed_Infected', 'native SBML value', 'Confirmed Infected. Maps to SBML symbol `Confirmed_Infected`.'), 'cumulative_infected': ('Cumulative_Infected', 'native SBML value', 'Cumulative Infected. Maps to SBML symbol `Cumulative_Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Zhao2020SuqcModelOfCovid19TransmissionDynBiomd0000000962Model = CuratedEpidemiologySBMLModel
