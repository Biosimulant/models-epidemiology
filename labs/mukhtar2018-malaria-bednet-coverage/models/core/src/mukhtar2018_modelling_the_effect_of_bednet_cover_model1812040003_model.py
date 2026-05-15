# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Mukhtar2018 - Modelling the effect of bednet coverage on malaria transmission in South Sudan."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1812040003'
    _TITLE = 'Mukhtar2018 - Modelling the effect of bednet coverage on malaria transmission in South Sudan'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'E', 'I', 'A', 'R', 'X', 'Y', 'Z']
    _SPECIES_LABELS = {'S': 'Susceptible humans', 'E': 'Exposed humans', 'I': 'Infected humans', 'A': 'Asymptomatic humans', 'R': 'Recovered humans', 'X': 'Susceptible mosquitoes', 'Y': 'Exposed mosquitoes', 'Z': 'Infectious mosquitoes'}
    _PARAMETER_INPUTS = {'bednet_coverage_factor': ('phi', 0.89, 'native model units', 'LLIN/bednet coverage factor. Maps to SBML symbol `phi`.'), 'mosquito_biting_rate': ('b', 0.4356804, 'native model units', 'Mosquito biting-rate parameter. Maps to SBML symbol `b`.'), 'mosquito_transmission_rate': ('beta', 0.876511672605679, 'native model units', 'Mosquito infection/transmission parameter. Maps to SBML symbol `beta`.'), 'human_recovery_rate': ('alpha_1', 0.02169197, 'native model units', 'Human recovery-rate parameter. Maps to SBML symbol `alpha_1`.')}
    _HEADLINE_OUTPUTS = {'susceptible_humans': ('S', 'native SBML value', 'Susceptible humans. Maps to SBML symbol `S`.'), 'exposed_humans': ('E', 'native SBML value', 'Exposed humans. Maps to SBML symbol `E`.'), 'infected_humans': ('I', 'native SBML value', 'Infected humans. Maps to SBML symbol `I`.'), 'asymptomatic_humans': ('A', 'native SBML value', 'Asymptomatic humans. Maps to SBML symbol `A`.'), 'recovered_humans': ('R', 'native SBML value', 'Recovered humans. Maps to SBML symbol `R`.'), 'susceptible_mosquitoes': ('X', 'native SBML value', 'Susceptible mosquitoes. Maps to SBML symbol `X`.'), 'exposed_mosquitoes': ('Y', 'native SBML value', 'Exposed mosquitoes. Maps to SBML symbol `Y`.'), 'infectious_mosquitoes': ('Z', 'native SBML value', 'Infectious mosquitoes. Maps to SBML symbol `Z`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Mukhtar2018ModellingTheEffectOfBednetCoverModel1812040003Model = CuratedEpidemiologySBMLModel
