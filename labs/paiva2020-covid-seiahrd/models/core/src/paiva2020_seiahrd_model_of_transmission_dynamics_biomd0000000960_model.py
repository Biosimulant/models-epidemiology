# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Paiva2020 - SEIAHRD model of transmission dynamics of COVID-19."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000960'
    _TITLE = 'Paiva2020 - SEIAHRD model of transmission dynamics of COVID-19'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed', 'Infectious', 'Hospitalized', 'Deceased', 'Susceptible', 'Recovered', 'Asymptomatic', 'Cumulative_Cases']
    _SPECIES_LABELS = {'Exposed': 'Exposed', 'Infectious': 'Infectious', 'Hospitalized': 'Hospitalized', 'Deceased': 'Deceased', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Asymptomatic': 'Asymptomatic', 'Cumulative_Cases': 'Cumulative Cases'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta_1', 0.334, 'native model units', 'COVID-19 transmission-rate parameter. Maps to SBML symbol `beta_1`.'), 'incubation_rate': ('kappa', 0.44, 'native model units', 'Exposed-to-infectious progression parameter. Maps to SBML symbol `kappa`.'), 'asymptomatic_fraction': ('rho', 0.053, 'native model units', 'Asymptomatic-branch fraction parameter. Maps to SBML symbol `rho`.'), 'hospitalization_rate': ('mu', 1.64, 'native model units', 'Hospitalization-rate parameter. Maps to SBML symbol `mu`.'), 'hospital_mortality_rate': ('delta_H', 0.008, 'native model units', 'Hospital mortality parameter. Maps to SBML symbol `delta_H`.'), 'infectious_mortality_rate': ('delta_I', 0.003, 'native model units', 'Infectious mortality parameter. Maps to SBML symbol `delta_I`.')}
    _HEADLINE_OUTPUTS = {'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infectious': ('Infectious', 'native SBML value', 'Infectious. Maps to SBML symbol `Infectious`.'), 'hospitalized': ('Hospitalized', 'native SBML value', 'Hospitalized. Maps to SBML symbol `Hospitalized`.'), 'deceased': ('Deceased', 'native SBML value', 'Deceased. Maps to SBML symbol `Deceased`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'asymptomatic': ('Asymptomatic', 'native SBML value', 'Asymptomatic. Maps to SBML symbol `Asymptomatic`.'), 'cumulative_cases': ('Cumulative_Cases', 'native SBML value', 'Cumulative Cases. Maps to SBML symbol `Cumulative_Cases`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Paiva2020SeiahrdModelOfTransmissionDynamicsBiomd0000000960Model = CuratedEpidemiologySBMLModel
