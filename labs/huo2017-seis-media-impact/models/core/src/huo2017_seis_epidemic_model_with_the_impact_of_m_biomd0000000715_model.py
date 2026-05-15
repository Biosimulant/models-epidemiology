# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Huo2017 - SEIS epidemic model with the impact of media."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000715'
    _TITLE = 'Huo2017 - SEIS epidemic model with the impact of media'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E', 'I', 'S', 'M', 'N']
    _SPECIES_LABELS = {'E': 'Exposed Individuals (E)', 'I': 'Infected Individuals (I)', 'S': 'Susceptible Individuals (S)', 'M': 'Message (M)', 'N': 'Total population (N)'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 0.8, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.'), 'recovery_rate': ('gamma', 0.7, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'exposed_individuals_e': ('E', 'native SBML value', 'Exposed Individuals (E). Maps to SBML symbol `E`.'), 'infected_individuals_i': ('I', 'native SBML value', 'Infected Individuals (I). Maps to SBML symbol `I`.'), 'susceptible_individuals_s': ('S', 'native SBML value', 'Susceptible Individuals (S). Maps to SBML symbol `S`.'), 'message_m': ('M', 'native SBML value', 'Message (M). Maps to SBML symbol `M`.'), 'total_population_n': ('N', 'native SBML value', 'Total population (N). Maps to SBML symbol `N`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Huo2017SeisEpidemicModelWithTheImpactOfMBiomd0000000715Model = CuratedEpidemiologySBMLModel
