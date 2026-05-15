# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Garira2019 - A coupled multiscale model to guide malaria control and elimination."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2003190008'
    _TITLE = 'Garira2019 - A coupled multiscale model to guide malaria control and elimination'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S_H', 'I_H', 'P_V', 'S_V', 'I_V', 'G_H']
    _SPECIES_LABELS = {'S_H': 'Susceptible humans', 'I_H': 'Infected humans', 'P_V': 'Vector parasite load', 'S_V': 'Susceptible vectors', 'I_V': 'Infected vectors', 'G_H': 'Human gametocyte load'}
    _PARAMETER_INPUTS = {'mosquito_to_human_transmission': ('beta_H', 0.3, 'native model units', 'Mosquito-to-human malaria transmission parameter. Maps to SBML symbol `beta_H`.'), 'human_to_mosquito_transmission': ('beta_V', 0.2, 'native model units', 'Human-to-mosquito malaria transmission parameter. Maps to SBML symbol `beta_V`.'), 'human_recovery_rate': ('gamma_H', 0.25, 'native model units', 'Human recovery-rate parameter. Maps to SBML symbol `gamma_H`.'), 'mosquito_mortality_rate': ('mu_V', 0.12, 'native model units', 'Mosquito mortality parameter. Maps to SBML symbol `mu_V`.'), 'gametocyte_production_rate': ('alpha_g', 96.0, 'native model units', 'Within-human gametocyte production parameter. Maps to SBML symbol `alpha_g`.')}
    _HEADLINE_OUTPUTS = {'susceptible_humans': ('S_H', 'native SBML value', 'Susceptible humans. Maps to SBML symbol `S_H`.'), 'infected_humans': ('I_H', 'native SBML value', 'Infected humans. Maps to SBML symbol `I_H`.'), 'vector_parasite_load': ('P_V', 'native SBML value', 'Vector parasite load. Maps to SBML symbol `P_V`.'), 'susceptible_vectors': ('S_V', 'native SBML value', 'Susceptible vectors. Maps to SBML symbol `S_V`.'), 'infected_vectors': ('I_V', 'native SBML value', 'Infected vectors. Maps to SBML symbol `I_V`.'), 'human_gametocyte_load': ('G_H', 'native SBML value', 'Human gametocyte load. Maps to SBML symbol `G_H`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Garira2019ACoupledMultiscaleModelToGuideMModel2003190008Model = CuratedEpidemiologySBMLModel
