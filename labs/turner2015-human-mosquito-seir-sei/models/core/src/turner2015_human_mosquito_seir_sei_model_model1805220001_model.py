# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Turner2015 - Human/Mosquito SEIR/SEI Model."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1805220001'
    _TITLE = 'Turner2015 - Human/Mosquito SEIR/SEI Model'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed_Human', 'Infected_Human', 'Exposed_Mosquito', 'Infected_Mosquito', 'Susceptible_Human', 'Susceptible_Mosquito', 'Recovered']
    _SPECIES_LABELS = {'Exposed_Human': 'Exposed Human', 'Infected_Human': 'Infected Human', 'Exposed_Mosquito': 'Exposed Mosquito', 'Infected_Mosquito': 'Infected Mosquito', 'Susceptible_Human': 'Susceptible Human', 'Susceptible_Mosquito': 'Susceptible Mosquito', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'human_to_mosquito_transmission': ('Human_B_hv', 0.02, 'native model units', 'Human-to-mosquito transmission parameter. Maps to SBML symbol `Human_B_hv`.'), 'mosquito_to_human_transmission': ('Vector_B_vh', 0.02, 'native model units', 'Mosquito-to-human transmission parameter. Maps to SBML symbol `Vector_B_vh`.'), 'human_recovery_rate': ('Human_gamma', 0.003704, 'native model units', 'Human recovery-rate parameter. Maps to SBML symbol `Human_gamma`.'), 'mosquito_mortality_rate': ('Vector_u1', 0.1429, 'native model units', 'Mosquito mortality parameter. Maps to SBML symbol `Vector_u1`.')}
    _HEADLINE_OUTPUTS = {'exposed_human': ('Exposed_Human', 'native SBML value', 'Exposed Human. Maps to SBML symbol `Exposed_Human`.'), 'infected_human': ('Infected_Human', 'native SBML value', 'Infected Human. Maps to SBML symbol `Infected_Human`.'), 'exposed_mosquito': ('Exposed_Mosquito', 'native SBML value', 'Exposed Mosquito. Maps to SBML symbol `Exposed_Mosquito`.'), 'infected_mosquito': ('Infected_Mosquito', 'native SBML value', 'Infected Mosquito. Maps to SBML symbol `Infected_Mosquito`.'), 'susceptible_human': ('Susceptible_Human', 'native SBML value', 'Susceptible Human. Maps to SBML symbol `Susceptible_Human`.'), 'susceptible_mosquito': ('Susceptible_Mosquito', 'native SBML value', 'Susceptible Mosquito. Maps to SBML symbol `Susceptible_Mosquito`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Turner2015HumanMosquitoSeirSeiModelModel1805220001Model = CuratedEpidemiologySBMLModel
