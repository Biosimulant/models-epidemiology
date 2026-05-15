# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Mukhta2018-the effect of bednet coverage on malaria transmission in South Sudan."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2003160003'
    _TITLE = 'Mukhta2018-the effect of bednet coverage on malaria transmission in South Sudan'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S1', 'E1', 'I1', 'A1', 'R1', 'X1', 'Y1', 'Z1']
    _SPECIES_LABELS = {'S1': 'Susceptible humans', 'E1': 'Exposed humans', 'I1': 'Infected humans', 'A1': 'Asymptomatic humans', 'R1': 'Recovered humans', 'X1': 'Susceptible mosquitoes', 'Y1': 'Exposed mosquitoes', 'Z1': 'Infectious mosquitoes'}
    _PARAMETER_INPUTS = {'bednet_coverage_factor': ('phi', 0.89, 'native model units', 'LLIN/bednet coverage factor. Maps to SBML symbol `phi`.'), 'mosquito_biting_rate': ('b', 0.4356804, 'native model units', 'Mosquito biting-rate parameter. Maps to SBML symbol `b`.'), 'mosquito_transmission_rate': ('beta', 0.876511672605679, 'native model units', 'Mosquito infection/transmission parameter. Maps to SBML symbol `beta`.'), 'human_recovery_rate': ('alpha_1', 0.02169197, 'native model units', 'Human recovery-rate parameter. Maps to SBML symbol `alpha_1`.')}
    _HEADLINE_OUTPUTS = {'susceptible_humans': ('S1', 'native SBML value', 'Susceptible humans. Maps to SBML symbol `S1`.'), 'exposed_humans': ('E1', 'native SBML value', 'Exposed humans. Maps to SBML symbol `E1`.'), 'infected_humans': ('I1', 'native SBML value', 'Infected humans. Maps to SBML symbol `I1`.'), 'asymptomatic_humans': ('A1', 'native SBML value', 'Asymptomatic humans. Maps to SBML symbol `A1`.'), 'recovered_humans': ('R1', 'native SBML value', 'Recovered humans. Maps to SBML symbol `R1`.'), 'susceptible_mosquitoes': ('X1', 'native SBML value', 'Susceptible mosquitoes. Maps to SBML symbol `X1`.'), 'exposed_mosquitoes': ('Y1', 'native SBML value', 'Exposed mosquitoes. Maps to SBML symbol `Y1`.'), 'infectious_mosquitoes': ('Z1', 'native SBML value', 'Infectious mosquitoes. Maps to SBML symbol `Z1`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Mukhta2018TheEffectOfBednetCoverageOnMalaModel2003160003Model = CuratedEpidemiologySBMLModel
