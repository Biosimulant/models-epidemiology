# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ghanbari2020 - forecasting the second wave of COVID-19 in Iran."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000976'
    _TITLE = 'Ghanbari2020 - forecasting the second wave of COVID-19 in Iran'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected_weak_immune_system', 'Infected_strong_immune_system', 'Susceptible', 'Recovered']
    _SPECIES_LABELS = {'Infected_weak_immune_system': 'Infected weak immune system', 'Infected_strong_immune_system': 'Infected strong immune system', 'Susceptible': 'Susceptible', 'Recovered': 'Recovered'}
    _PARAMETER_INPUTS = {'transmission_rate': ('alpha', 0.55, 'native model units', 'COVID-19 transmission parameter. Maps to SBML symbol `alpha`.'), 'weak_immunity_recovery_rate': ('gamma_1', 0.1, 'native model units', 'Recovery-rate parameter for weak-immune infected group. Maps to SBML symbol `gamma_1`.'), 'strong_immunity_recovery_rate': ('gamma_2', 0.061, 'native model units', 'Recovery-rate parameter for strong-immune infected group. Maps to SBML symbol `gamma_2`.'), 'lockdown_start_day': ('Lockdown_start', 19.0, 'day', 'Lockdown start time. Maps to SBML symbol `Lockdown_start`.'), 'lockdown_end_day': ('Lockdown_end', 33.0, 'day', 'Lockdown end time. Maps to SBML symbol `Lockdown_end`.')}
    _HEADLINE_OUTPUTS = {'infected_weak_immune_system': ('Infected_weak_immune_system', 'native SBML value', 'Infected weak immune system. Maps to SBML symbol `Infected_weak_immune_system`.'), 'infected_strong_immune_system': ('Infected_strong_immune_system', 'native SBML value', 'Infected strong immune system. Maps to SBML symbol `Infected_strong_immune_system`.'), 'susceptible': ('Susceptible', 'native SBML value', 'Susceptible. Maps to SBML symbol `Susceptible`.'), 'recovered': ('Recovered', 'native SBML value', 'Recovered. Maps to SBML symbol `Recovered`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Ghanbari2020ForecastingTheSecondWaveOfCoviBiomd0000000976Model = CuratedEpidemiologySBMLModel
