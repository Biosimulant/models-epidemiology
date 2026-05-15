# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for COVID-19 immunotherapy A mathematical model."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2202230002'
    _TITLE = 'COVID-19 immunotherapy A mathematical model'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VL_tratamento', 'V_tratamento', 'A_I_tratamento', 'N_at_tratamento', 'I_12_tratamento', 'I_ab_tratamento', 'B_tratamento', 'Inib_tratamento']
    _SPECIES_LABELS = {'VL_tratamento': 'Treated viral load', 'V_tratamento': 'Treated free virus', 'A_I_tratamento': 'Treated infected epithelial cells', 'N_at_tratamento': 'Treated activated neutrophils', 'I_12_tratamento': 'Treated interleukin 12', 'I_ab_tratamento': 'Treated antibody response', 'B_tratamento': 'Treated B cells', 'Inib_tratamento': 'Treatment inhibition signal'}
    _PARAMETER_INPUTS = {'virus_clearance_rate': ('c', 10.0, 'native model units', 'Virus clearance-rate parameter. Maps to SBML symbol `c`.'), 'virus_production_rate': ('p', 400.0, 'native model units', 'Virus production-rate parameter. Maps to SBML symbol `p`.'), 'infected_cell_death_rate': ('delta', 4.0, 'native model units', 'Infected-cell loss parameter. Maps to SBML symbol `delta`.'), 'immune_activation_rate': ('epsilon', 0.02, 'native model units', 'Immune activation/progression parameter. Maps to SBML symbol `epsilon`.')}
    _HEADLINE_OUTPUTS = {'treated_viral_load': ('VL_tratamento', 'native SBML value', 'Treated viral load. Maps to SBML symbol `VL_tratamento`.'), 'treated_free_virus': ('V_tratamento', 'native SBML value', 'Treated free virus. Maps to SBML symbol `V_tratamento`.'), 'treated_infected_epithelial_cells': ('A_I_tratamento', 'native SBML value', 'Treated infected epithelial cells. Maps to SBML symbol `A_I_tratamento`.'), 'treated_activated_neutrophils': ('N_at_tratamento', 'native SBML value', 'Treated activated neutrophils. Maps to SBML symbol `N_at_tratamento`.'), 'treated_interleukin_12': ('I_12_tratamento', 'native SBML value', 'Treated interleukin 12. Maps to SBML symbol `I_12_tratamento`.'), 'treated_antibody_response': ('I_ab_tratamento', 'native SBML value', 'Treated antibody response. Maps to SBML symbol `I_ab_tratamento`.'), 'treated_b_cells': ('B_tratamento', 'native SBML value', 'Treated B cells. Maps to SBML symbol `B_tratamento`.'), 'treatment_inhibition_signal': ('Inib_tratamento', 'native SBML value', 'Treatment inhibition signal. Maps to SBML symbol `Inib_tratamento`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Covid19ImmunotherapyAMathematicalModelModel2202230002Model = CuratedEpidemiologySBMLModel
