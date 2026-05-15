# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000984'
    _TITLE = 'Fang2020 - SEIR model of COVID-19 transmission considering government interventions in Wuhan'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed', 'Infected', 'Susceptible', 'Recovered', 'Total_population']
    _SPECIES_LABELS = {'Exposed': 'Exposed', 'Infected': 'Infected', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Total_population': 'Total population'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 1.0, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.'), 'baseline_transmission_rate': ('beta_o', 0.1, 'native model units', 'Baseline transmission-rate parameter. Maps to SBML symbol `beta_o`.'), 'recovery_rate': ('gamma', 0.097561, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'total_population': ('Total_population', 'native SBML value', 'Total population. Maps to SBML symbol `Total_population`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Fang2020SeirModelOfCovid19TransmissionConBiomd0000000984Model = CuratedEpidemiologySBMLModel
