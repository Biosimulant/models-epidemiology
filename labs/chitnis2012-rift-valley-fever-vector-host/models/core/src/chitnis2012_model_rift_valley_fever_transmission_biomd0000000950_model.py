# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Chitnis2012 - Model Rift Valley Fever transmission between cattle and mosquitoes (Model 1)."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000950'
    _TITLE = 'Chitnis2012 - Model Rift Valley Fever transmission between cattle and mosquitoes (Model 1)'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S_h', 'A_h', 'I_h', 'R_h', 'S_v', 'E_v', 'I_v']
    _SPECIES_LABELS = {'S_h': 'Susceptible cattle', 'A_h': 'Asymptomatic cattle', 'I_h': 'Infected cattle', 'R_h': 'Recovered cattle', 'S_v': 'Susceptible mosquitoes', 'E_v': 'Exposed mosquitoes', 'I_v': 'Infected mosquitoes'}
    _PARAMETER_INPUTS = {'cattle_to_mosquito_transmission': ('beta_hv', 0.21, 'native model units', 'Cattle-to-mosquito Rift Valley fever transmission parameter. Maps to SBML symbol `beta_hv`.'), 'mosquito_to_cattle_transmission': ('beta_vh', 0.7, 'native model units', 'Mosquito-to-cattle Rift Valley fever transmission parameter. Maps to SBML symbol `beta_vh`.'), 'cattle_recovery_rate': ('gamma_h', 0.25, 'native model units', 'Cattle recovery-rate parameter. Maps to SBML symbol `gamma_h`.'), 'mosquito_birth_rate': ('psi_v', 0.1, 'native model units', 'Mosquito recruitment/birth parameter. Maps to SBML symbol `psi_v`.'), 'mosquito_mortality_rate': ('u_v', 0.05, 'native model units', 'Mosquito mortality parameter. Maps to SBML symbol `u_v`.')}
    _HEADLINE_OUTPUTS = {'susceptible_cattle': ('S_h', 'native SBML value', 'Susceptible cattle. Maps to SBML symbol `S_h`.'), 'asymptomatic_cattle': ('A_h', 'native SBML value', 'Asymptomatic cattle. Maps to SBML symbol `A_h`.'), 'infected_cattle': ('I_h', 'native SBML value', 'Infected cattle. Maps to SBML symbol `I_h`.'), 'recovered_cattle': ('R_h', 'native SBML value', 'Recovered cattle. Maps to SBML symbol `R_h`.'), 'susceptible_mosquitoes': ('S_v', 'native SBML value', 'Susceptible mosquitoes. Maps to SBML symbol `S_v`.'), 'exposed_mosquitoes': ('E_v', 'native SBML value', 'Exposed mosquitoes. Maps to SBML symbol `E_v`.'), 'infected_mosquitoes': ('I_v', 'native SBML value', 'Infected mosquitoes. Maps to SBML symbol `I_v`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Chitnis2012ModelRiftValleyFeverTransmissionBiomd0000000950Model = CuratedEpidemiologySBMLModel
