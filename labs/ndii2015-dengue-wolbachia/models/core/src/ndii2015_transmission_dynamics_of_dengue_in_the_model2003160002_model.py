# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ndii2015-transmission dynamics of dengue in the presence of Wolbachia."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2003160002'
    _TITLE = 'Ndii2015-transmission dynamics of dengue in the presence of Wolbachia'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S_H', 'E_H', 'I_H', 'R_H', 'S_N', 'I_N', 'S_W', 'I_W']
    _SPECIES_LABELS = {'S_H': 'Susceptible human', 'E_H': 'Exposed human', 'I_H': 'Infected human', 'R_H': 'Recovered human', 'S_N': 'Susceptible non-Wolbachia', 'I_N': 'Infected non-Wolbachia', 'S_W': 'Susceptible Wolbachia', 'I_W': 'Infected Wolbachia'}
    _PARAMETER_INPUTS = {'human_incubation_rate': ('sigma', 0.2, 'native model units', 'Human exposed-to-infectious dengue progression parameter. Maps to SBML symbol `sigma`.'), 'wolbachia_transmission_reduction': ('c', 0.95, 'native model units', 'Wolbachia-associated transmission reduction/compatibility parameter. Maps to SBML symbol `c`.'), 'human_recovery_rate': ('gamma_H', 0.181818181818182, 'native model units', 'Human dengue recovery-rate parameter. Maps to SBML symbol `gamma_H`.'), 'non_wolbachia_mosquito_birth_rate': ('b_N', 0.63, 'native model units', 'Non-Wolbachia mosquito birth parameter. Maps to SBML symbol `b_N`.'), 'wolbachia_mosquito_birth_rate': ('b_W', 0.5985, 'native model units', 'Wolbachia mosquito birth parameter. Maps to SBML symbol `b_W`.')}
    _HEADLINE_OUTPUTS = {'susceptible_human': ('S_H', 'native SBML value', 'Susceptible human. Maps to SBML symbol `S_H`.'), 'exposed_human': ('E_H', 'native SBML value', 'Exposed human. Maps to SBML symbol `E_H`.'), 'infected_human': ('I_H', 'native SBML value', 'Infected human. Maps to SBML symbol `I_H`.'), 'recovered_human': ('R_H', 'native SBML value', 'Recovered human. Maps to SBML symbol `R_H`.'), 'susceptible_non_wolbachia': ('S_N', 'native SBML value', 'Susceptible non-Wolbachia. Maps to SBML symbol `S_N`.'), 'infected_non_wolbachia': ('I_N', 'native SBML value', 'Infected non-Wolbachia. Maps to SBML symbol `I_N`.'), 'susceptible_wolbachia': ('S_W', 'native SBML value', 'Susceptible Wolbachia. Maps to SBML symbol `S_W`.'), 'infected_wolbachia': ('I_W', 'native SBML value', 'Infected Wolbachia. Maps to SBML symbol `I_W`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Ndii2015TransmissionDynamicsOfDengueInTheModel2003160002Model = CuratedEpidemiologySBMLModel
