# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Sarkar2020 - SAIR model of COVID-19 transmission with quarantine measures in India."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000977'
    _TITLE = 'Sarkar2020 - SAIR model of COVID-19 transmission with quarantine measures in India'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Susceptible', 'Infected', 'Asymptomatic', 'Susceptible_quarantined', 'Exposed_quarantined', 'Recovered']
    _SPECIES_LABELS = {'Susceptible': 'Susceptible', 'Infected': 'Infected', 'Asymptomatic': 'Asymptomatic', 'Susceptible_quarantined': 'Susceptible quarantined', 'Exposed_quarantined': 'Infected quarantined', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta_s', 0.8799, 'native model units', 'COVID-19 transmission-rate parameter. Maps to SBML symbol `beta_s`.'), 'asymptomatic_fraction': ('rho_s', 0.3199, 'native model units', 'Asymptomatic infection fraction parameter. Maps to SBML symbol `rho_s`.'), 'quarantine_transition_rate': ('xi_q', 0.13369, 'native model units', 'Quarantine transition parameter. Maps to SBML symbol `xi_q`.'), 'infected_recovery_rate': ('gamma_i', 0.07151, 'native model units', 'Symptomatic infected recovery-rate parameter. Maps to SBML symbol `gamma_i`.'), 'asymptomatic_recovery_rate': ('gamma_a', 0.0168, 'native model units', 'Asymptomatic recovery-rate parameter. Maps to SBML symbol `gamma_a`.')}
    _HEADLINE_OUTPUTS = {'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'infected': ('Infected', 'native SBML value', 'Infected. Maps to SBML symbol `Infected`.'), 'asymptomatic': ('Asymptomatic', 'native SBML value', 'Asymptomatic. Maps to SBML symbol `Asymptomatic`.'), 'susceptible_quarantined': ('Susceptible_quarantined', 'native SBML value', 'Susceptible quarantined. Maps to SBML symbol `Susceptible_quarantined`.'), 'infected_quarantined': ('Exposed_quarantined', 'native SBML value', 'Infected quarantined. Maps to SBML symbol `Exposed_quarantined`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Sarkar2020SairModelOfCovid19TransmissionWBiomd0000000977Model = CuratedEpidemiologySBMLModel
