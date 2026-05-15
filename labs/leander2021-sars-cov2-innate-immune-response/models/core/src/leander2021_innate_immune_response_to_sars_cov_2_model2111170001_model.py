# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Leander2021 - innate immune response to SARS-CoV-2 in the alveolar epithelium."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2111170001'
    _TITLE = 'Leander2021 - innate immune response to SARS-CoV-2 in the alveolar epithelium'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V', 'A1', 'A2', 'A2_act', 'I', 'M_act', 'F', 'T', 'D']
    _SPECIES_LABELS = {'V': 'Viral load', 'A1': 'Alveolar type I cells', 'A2': 'ACE2-positive type II alveolar cells', 'A2_act': 'Activated ACE2-positive type II alveolar cells', 'I': 'Infected cells', 'M_act': 'Activated macrophages', 'F': 'Interferon signal', 'T': 'T cell response', 'D': 'Damaged cells'}
    _PARAMETER_INPUTS = {'viral_infection_rate': ('beta', 0.16666, 'native model units', 'Viral infection-rate parameter. Maps to SBML symbol `beta`.'), 'virus_clearance_rate': ('gamma', 7.73, 'native model units', 'Virus clearance-rate parameter. Maps to SBML symbol `gamma`.'), 'viral_production_rate': ('pV', 3.18, 'native model units', 'Virus production-rate parameter. Maps to SBML symbol `pV`.'), 'macrophage_activation_rate': ('kM', 0.0003, 'native model units', 'Macrophage activation-rate parameter. Maps to SBML symbol `kM`.')}
    _HEADLINE_OUTPUTS = {'viral_load': ('V', 'native SBML value', 'Viral load. Maps to SBML symbol `V`.'), 'alveolar_type_1_cells': ('A1', 'native SBML value', 'Alveolar type I cells. Maps to SBML symbol `A1`.'), 'ace2_positive_type_2_cells': ('A2', 'native SBML value', 'ACE2-positive type II alveolar cells. Maps to SBML symbol `A2`.'), 'activated_ace2_positive_type_2_cells': ('A2_act', 'native SBML value', 'Activated ACE2-positive type II alveolar cells. Maps to SBML symbol `A2_act`.'), 'infected_cells': ('I', 'native SBML value', 'Infected cells. Maps to SBML symbol `I`.'), 'activated_macrophages': ('M_act', 'native SBML value', 'Activated macrophages. Maps to SBML symbol `M_act`.'), 'interferon_signal': ('F', 'native SBML value', 'Interferon signal. Maps to SBML symbol `F`.'), 't_cell_response': ('T', 'native SBML value', 'T cell response. Maps to SBML symbol `T`.'), 'damaged_cells': ('D', 'native SBML value', 'Damaged cells. Maps to SBML symbol `D`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Leander2021InnateImmuneResponseToSarsCov2Model2111170001Model = CuratedEpidemiologySBMLModel
