# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Lee2018 - Avian human bilinear incidence (BI) model."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000716'
    _TITLE = 'Lee2018 - Avian human bilinear incidence (BI) model'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['I_a', 'S_h', 'I_b', 'S_b']
    _SPECIES_LABELS = {'I_a': 'Infected Human (I a)', 'S_h': 'Susceptible human (S h)', 'I_b': 'Infected bird (I b)', 'S_b': 'Susceptible bird (S b)'}
    _PARAMETER_INPUTS = {'bird_to_human_transmission': ('beta_bh', 1.62354134956875e-10, 'native model units', 'Bird-to-human avian influenza transmission parameter. Maps to SBML symbol `beta_bh`.'), 'bird_to_bird_transmission': ('beta_b', 0.00346731269415168, 'native model units', 'Bird-to-bird avian influenza transmission parameter. Maps to SBML symbol `beta_b`.'), 'environmental_transmission': ('beta_v', 0.00173365634707584, 'native model units', 'Environmental/vector-mediated avian influenza transmission parameter. Maps to SBML symbol `beta_v`.'), 'infected_bird_culling_rate': ('c', 0.0, 'native model units', 'Infected-bird culling/control parameter. Maps to SBML symbol `c`.'), 'human_quarantine_rate': ('q', 0.0, 'native model units', 'Human quarantine/control parameter. Maps to SBML symbol `q`.')}
    _HEADLINE_OUTPUTS = {'infected_human_i_a': ('I_a', 'native SBML value', 'Infected Human (I a). Maps to SBML symbol `I_a`.'), 'susceptible_human_s_h': ('S_h', 'native SBML value', 'Susceptible human (S h). Maps to SBML symbol `S_h`.'), 'infected_bird_i_b': ('I_b', 'native SBML value', 'Infected bird (I b). Maps to SBML symbol `I_b`.'), 'susceptible_bird_s_b': ('S_b', 'native SBML value', 'Susceptible bird (S b). Maps to SBML symbol `S_b`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Lee2018AvianHumanBilinearIncidenceBiModelBiomd0000000716Model = CuratedEpidemiologySBMLModel
