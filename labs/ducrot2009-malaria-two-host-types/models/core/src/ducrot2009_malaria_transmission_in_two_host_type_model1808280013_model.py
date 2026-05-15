# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ducrot2009 - Malaria transmission in two host types."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1808280013'
    _TITLE = 'Ducrot2009 - Malaria transmission in two host types'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s_e', 'e_e', 'i_e', 'e_a', 'i_a', 'r_a', 'e_v', 'i_v']
    _SPECIES_LABELS = {'s_e': 'Susceptible non-immune humans', 'e_e': 'Exposed non-immune humans', 'i_e': 'Infectious non-immune humans', 'e_a': 'Exposed semi-immune humans', 'i_a': 'Infectious semi-immune humans', 'r_a': 'Immune semi-immune humans', 'e_v': 'Exposed mosquitoes', 'i_v': 'Infectious mosquitoes'}
    _PARAMETER_INPUTS = {'mosquito_to_nonimmune_transmission': ('c_ve', 0.07, 'native model units', 'Mosquito-to-non-immune-human transmission parameter. Maps to SBML symbol `c_ve`.'), 'mosquito_to_semi_immune_transmission': ('c_va', 0.022, 'native model units', 'Mosquito-to-semi-immune-human transmission parameter. Maps to SBML symbol `c_va`.'), 'nonimmune_to_mosquito_transmission': ('c_ev', 0.45, 'native model units', 'Non-immune-human-to-mosquito transmission parameter. Maps to SBML symbol `c_ev`.'), 'semi_immune_to_mosquito_transmission': ('c_av', 0.35, 'native model units', 'Semi-immune-human-to-mosquito transmission parameter. Maps to SBML symbol `c_av`.')}
    _HEADLINE_OUTPUTS = {'susceptible_nonimmune_humans': ('s_e', 'native SBML value', 'Susceptible non-immune humans. Maps to SBML symbol `s_e`.'), 'exposed_nonimmune_humans': ('e_e', 'native SBML value', 'Exposed non-immune humans. Maps to SBML symbol `e_e`.'), 'infectious_nonimmune_humans': ('i_e', 'native SBML value', 'Infectious non-immune humans. Maps to SBML symbol `i_e`.'), 'exposed_semi_immune_humans': ('e_a', 'native SBML value', 'Exposed semi-immune humans. Maps to SBML symbol `e_a`.'), 'infectious_semi_immune_humans': ('i_a', 'native SBML value', 'Infectious semi-immune humans. Maps to SBML symbol `i_a`.'), 'immune_semi_immune_humans': ('r_a', 'native SBML value', 'Immune semi-immune humans. Maps to SBML symbol `r_a`.'), 'exposed_mosquitoes': ('e_v', 'native SBML value', 'Exposed mosquitoes. Maps to SBML symbol `e_v`.'), 'infectious_mosquitoes': ('i_v', 'native SBML value', 'Infectious mosquitoes. Maps to SBML symbol `i_v`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Ducrot2009MalariaTransmissionInTwoHostTypeModel1808280013Model = CuratedEpidemiologySBMLModel
