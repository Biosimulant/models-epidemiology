# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Chitnis2008 - Mathematical model of malaria transmission."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000949'
    _TITLE = 'Chitnis2008 - Mathematical model of malaria transmission'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed_Human', 'Infected_Human', 'Exposed_Mosquito', 'Infected_Mosquito', 'Susceptible_Human', 'Susceptible_Mosquito', 'Recovered']
    _SPECIES_LABELS = {'Exposed_Human': 'Exposed Human', 'Infected_Human': 'Infected Human', 'Exposed_Mosquito': 'Exposed Mosquito', 'Infected_Mosquito': 'Infected Mosquito', 'Susceptible_Human': 'Susceptible Human', 'Susceptible_Mosquito': 'Susceptible Mosquito', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'human_to_mosquito_transmission': ('Beta_hv', 0.022, 'native model units', 'Human-to-mosquito malaria transmission parameter. Maps to SBML symbol `Beta_hv`.'), 'mosquito_to_human_transmission': ('Beta_vh', 0.24, 'native model units', 'Mosquito-to-human malaria transmission parameter. Maps to SBML symbol `Beta_vh`.'), 'human_recovery_rate': ('gamma_h', 0.0035, 'native model units', 'Human recovery-rate parameter. Maps to SBML symbol `gamma_h`.'), 'mosquito_mortality_rate': ('u_1v', 0.033, 'native model units', 'Adult mosquito mortality parameter. Maps to SBML symbol `u_1v`.')}
    _HEADLINE_OUTPUTS = {'exposed_human': ('Exposed_Human', 'native SBML value', 'Exposed Human. Maps to SBML symbol `Exposed_Human`.'), 'infected_human': ('Infected_Human', 'native SBML value', 'Infected Human. Maps to SBML symbol `Infected_Human`.'), 'exposed_mosquito': ('Exposed_Mosquito', 'native SBML value', 'Exposed Mosquito. Maps to SBML symbol `Exposed_Mosquito`.'), 'infected_mosquito': ('Infected_Mosquito', 'native SBML value', 'Infected Mosquito. Maps to SBML symbol `Infected_Mosquito`.'), 'susceptible_human': ('Susceptible_Human', 'native SBML value', 'Susceptible Human. Maps to SBML symbol `Susceptible_Human`.'), 'susceptible_mosquito': ('Susceptible_Mosquito', 'native SBML value', 'Susceptible Mosquito. Maps to SBML symbol `Susceptible_Mosquito`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Chitnis2008MathematicalModelOfMalariaTransmBiomd0000000949Model = CuratedEpidemiologySBMLModel
