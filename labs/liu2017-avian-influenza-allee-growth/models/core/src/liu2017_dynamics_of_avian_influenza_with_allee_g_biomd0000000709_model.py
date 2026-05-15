# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Liu2017 - Dynamics of Avian Influenza with Allee Growth Effect."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000709'
    _TITLE = 'Liu2017 - Dynamics of Avian Influenza with Allee Growth Effect'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['I_a', 'S_a', 'I_h', 'S_h', 'R_h']
    _SPECIES_LABELS = {'I_a': 'Infected Avian (I a)', 'S_a': 'Susceptible Avian (S a)', 'I_h': 'Infected Human (I h)', 'S_h': 'Susceptible Human (S h)', 'R_h': 'Recovered Human (R h)'}
    _PARAMETER_INPUTS = {'recovery_rate': ('gamma', 0.1, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'infected_avian_i_a': ('I_a', 'native SBML value', 'Infected Avian (I a). Maps to SBML symbol `I_a`.'), 'susceptible_avian_s_a': ('S_a', 'native SBML value', 'Susceptible Avian (S a). Maps to SBML symbol `S_a`.'), 'infected_human_i_h': ('I_h', 'native SBML value', 'Infected Human (I h). Maps to SBML symbol `I_h`.'), 'susceptible_human_s_h': ('S_h', 'native SBML value', 'Susceptible Human (S h). Maps to SBML symbol `S_h`.'), 'recovered_human_r_h': ('R_h', 'native SBML value', 'Recovered Human (R h). Maps to SBML symbol `R_h`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Liu2017DynamicsOfAvianInfluenzaWithAlleeGBiomd0000000709Model = CuratedEpidemiologySBMLModel
