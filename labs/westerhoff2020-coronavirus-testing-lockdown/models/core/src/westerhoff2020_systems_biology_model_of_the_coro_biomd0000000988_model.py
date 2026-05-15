# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Westerhoff2020 - systems biology model of the coronavirus pandemic 2020."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000988'
    _TITLE = 'Westerhoff2020 - systems biology model of the coronavirus pandemic 2020'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['uninfected_tested_0', 'uninfected_nontested_0', 'infected_tested_0', 'infected_nontested_0', 'infected_tested_div10', 'dead_corona_tested_0', 'dead_corona_nontested_0', 'recovered_tested_0', 'recovered_nontested_0', 'symptoms_tested_0', 'symptoms_nontested_0', 'dead_noncorona_0']
    _SPECIES_LABELS = {'uninfected_tested_0': 'Uninfected tested', 'uninfected_nontested_0': 'Uninfected nontested', 'infected_tested_0': 'Infected tested', 'infected_nontested_0': 'Infected nontested', 'infected_tested_div10': 'Infected tested div10', 'dead_corona_tested_0': 'Dead corona tested', 'dead_corona_nontested_0': 'Dead corona nontested', 'recovered_tested_0': 'Recovered tested'}
    _PARAMETER_INPUTS = {'social_distance': ('Social_Distance', 534700.0, 'native model units', 'Social-distance intervention parameter. Maps to SBML symbol `Social_Distance`.'), 'lockdown_severity': ('Government_induced_isolation_factor_0', 10.0, 'native model units', 'Lockdown-severity intervention parameter. Maps to SBML symbol `Government_induced_isolation_factor_0`.'), 'random_testing_rate': ('Testing_Randome', 0.0008, 'native model units', 'Random testing-rate parameter. Maps to SBML symbol `Testing_Randome`.'), 'symptom_testing_rate': ('Testing_for_Symptoms', 500.0, 'native model units', 'Symptom-driven testing-rate parameter. Maps to SBML symbol `Testing_for_Symptoms`.')}
    _HEADLINE_OUTPUTS = {'uninfected_tested': ('uninfected_tested_0', 'native SBML value', 'Uninfected tested. Maps to SBML symbol `uninfected_tested_0`.'), 'uninfected_nontested': ('uninfected_nontested_0', 'native SBML value', 'Uninfected nontested. Maps to SBML symbol `uninfected_nontested_0`.'), 'infected_tested': ('infected_tested_0', 'native SBML value', 'Infected tested. Maps to SBML symbol `infected_tested_0`.'), 'infected_nontested': ('infected_nontested_0', 'native SBML value', 'Infected nontested. Maps to SBML symbol `infected_nontested_0`.'), 'infected_tested_div10': ('infected_tested_div10', 'native SBML value', 'Infected tested div10. Maps to SBML symbol `infected_tested_div10`.'), 'dead_corona_tested': ('dead_corona_tested_0', 'native SBML value', 'Dead corona tested. Maps to SBML symbol `dead_corona_tested_0`.'), 'dead_corona_nontested': ('dead_corona_nontested_0', 'native SBML value', 'Dead corona nontested. Maps to SBML symbol `dead_corona_nontested_0`.'), 'recovered_tested': ('recovered_tested_0', 'native SBML value', 'Recovered tested. Maps to SBML symbol `recovered_tested_0`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Westerhoff2020SystemsBiologyModelOfTheCoroBiomd0000000988Model = CuratedEpidemiologySBMLModel
