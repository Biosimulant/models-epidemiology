# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ho2019 - Mathematical models of transmission dynamics and vaccine strategies in Hong Kong during the 2017-2018 winter influenza season (Simple)."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000851'
    _TITLE = 'Ho2019 - Mathematical models of transmission dynamics and vaccine strategies in Hong Kong during the 2017-2018 winter influenza season (Simple)'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['I', 'R', 'S', 'V', 'V_e']
    _SPECIES_LABELS = {'I': 'Infected', 'R': 'Recovered', 'S': 'Susceptible', 'V': 'Vector', 'V_e': 'Vector e'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 2.7516, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.'), 'recovery_rate': ('gamma', 2.1272, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.')}
    _HEADLINE_OUTPUTS = {'infected': ('I', 'native SBML value', 'Infected. Maps to SBML symbol `I`.'), 'recovered': ('R', 'native SBML value', 'Recovered. Maps to SBML symbol `R`.'), 'susceptible': ('S', 'native SBML value', 'Susceptible. Maps to SBML symbol `S`.'), 'vector': ('V', 'native SBML value', 'Vector. Maps to SBML symbol `V`.'), 'vector_e': ('V_e', 'native SBML value', 'Vector e. Maps to SBML symbol `V_e`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Ho2019MathematicalModelsOfTransmissionDynamBiomd0000000851Model = CuratedEpidemiologySBMLModel
