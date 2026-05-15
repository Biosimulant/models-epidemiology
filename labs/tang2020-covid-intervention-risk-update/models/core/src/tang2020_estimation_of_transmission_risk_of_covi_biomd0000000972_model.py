# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Tang2020 - Estimation of transmission risk of COVID-19 and impact of public health interventions - update."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000972'
    _TITLE = 'Tang2020 - Estimation of transmission risk of COVID-19 and impact of public health interventions - update'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Exposed_quarantined', 'Susceptible_quarantined', 'Exposed', 'Infected', 'Hospitalised', 'Susceptible', 'Recovered', 'Asymptomatic']
    _SPECIES_LABELS = {'Exposed_quarantined': 'Exposed quarantined', 'Susceptible_quarantined': 'Susceptible quarantined', 'Exposed': 'Exposed', 'Infected': 'Infected', 'Hospitalised': 'Hospitalised', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered', 'Asymptomatic': 'Asymptomatic'}
    _PARAMETER_INPUTS = {'transmission_probability': ('beta', 2.1011e-08, 'native model units', 'Transmission probability parameter. Maps to SBML symbol `beta`.'), 'exposed_progression_rate': ('sigma', 0.142857, 'native model units', 'Exposed-to-infectious progression parameter. Maps to SBML symbol `sigma`.'), 'daily_contact_rate': ('c', 14.781, 'native model units', 'Daily contact-rate parameter. Maps to SBML symbol `c`.'), 'quarantine_probability': ('q', 1.2858e-05, 'native model units', 'Quarantine probability parameter. Maps to SBML symbol `q`.'), 'hospitalization_rate': ('delta_I', 0.13266, 'native model units', 'Infected-to-hospitalised transition parameter. Maps to SBML symbol `delta_I`.')}
    _HEADLINE_OUTPUTS = {'exposed_quarantined': ('Exposed_quarantined', 'native SBML value', 'Exposed quarantined. Maps to SBML symbol `Exposed_quarantined`.'), 'susceptible_quarantined': ('Susceptible_quarantined', 'native SBML value', 'Susceptible quarantined. Maps to SBML symbol `Susceptible_quarantined`.'), 'exposed': ('Exposed', 'native SBML value', 'Exposed. Maps to SBML symbol `Exposed`.'), 'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'hospitalised': ('Hospitalised', 'native SBML value', 'Hospitalised. Maps to SBML symbol `Hospitalised`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.'), 'asymptomatic': ('Asymptomatic', 'native SBML value', 'Asymptomatic. Maps to SBML symbol `Asymptomatic`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Tang2020EstimationOfTransmissionRiskOfCoviBiomd0000000972Model = CuratedEpidemiologySBMLModel
