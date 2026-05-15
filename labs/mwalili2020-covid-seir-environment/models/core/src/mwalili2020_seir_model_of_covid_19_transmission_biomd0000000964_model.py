# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Mwalili2020 - SEIR model of COVID-19 transmission and environmental pathogen prevalence."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000964'
    _TITLE = 'Mwalili2020 - SEIR model of COVID-19 transmission and environmental pathogen prevalence'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected_Asymptomatic', 'Exposed', 'Infected_Symptomatic', 'Susceptible', 'Recovered', 'Pathogen_0']
    _SPECIES_LABELS = {'Infected_Asymptomatic': 'Infected Asymptomatic', 'Exposed': 'Exposed', 'Infected_Symptomatic': 'Infected Symptomatic', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Pathogen_0': 'Pathogen'}
    _PARAMETER_INPUTS = {'incubation_rate': ('sigma', 0.0018, 'native model units', 'Incubation/progression-rate parameter. Maps to SBML symbol `sigma`.')}
    _HEADLINE_OUTPUTS = {'infected_asymptomatic': ('Infected_Asymptomatic', 'native SBML value', 'Infected Asymptomatic. Maps to SBML symbol `Infected_Asymptomatic`.'), 'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infected_symptomatic': ('Infected_Symptomatic', 'native SBML value', 'Infected Symptomatic. Maps to SBML symbol `Infected_Symptomatic`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'pathogen': ('Pathogen_0', 'native SBML value', 'Pathogen. Maps to SBML symbol `Pathogen_0`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Mwalili2020SeirModelOfCovid19TransmissionBiomd0000000964Model = CuratedEpidemiologySBMLModel
