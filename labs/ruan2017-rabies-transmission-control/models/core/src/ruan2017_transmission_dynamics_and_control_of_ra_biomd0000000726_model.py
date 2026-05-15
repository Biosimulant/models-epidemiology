# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ruan2017 - Transmission dynamics and control of rabies in China."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000726'
    _TITLE = 'Ruan2017 - Transmission dynamics and control of rabies in China'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E_h', 'I_h', 'E_d', 'I_d', 'S_d', 'R_d', 'S_h', 'R_h']
    _SPECIES_LABELS = {'E_h': 'Exposed humans (E h)', 'I_h': 'Infectious humans (I h)', 'E_d': 'Exposed dogs (E d)', 'I_d': 'Infectious dogs (I d)', 'S_d': 'Susceptible dogs (S d)', 'R_d': 'Recovered dogs (R d)', 'S_h': 'Susceptible humans (S h)', 'R_h': 'Recovered humans (R h)'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 1.58e-07, 'native model units', 'Transmission-rate parameter. Maps to SBML symbol `beta`.'), 'recovery_rate': ('gamma', 0.4, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.'), 'incubation_rate': ('sigma', 6.0, 'native model units', 'Incubation/progression-rate parameter. Maps to SBML symbol `sigma`.')}
    _HEADLINE_OUTPUTS = {'exposed_humans_e_h': ('E_h', 'native SBML value', 'Exposed humans (E h). Maps to SBML symbol `E_h`.'), 'infectious_humans_i_h': ('I_h', 'native SBML value', 'Infectious humans (I h). Maps to SBML symbol `I_h`.'), 'exposed_dogs_e_d': ('E_d', 'native SBML value', 'Exposed dogs (E d). Maps to SBML symbol `E_d`.'), 'infectious_dogs_i_d': ('I_d', 'native SBML value', 'Infectious dogs (I d). Maps to SBML symbol `I_d`.'), 'susceptible_dogs_s_d': ('S_d', 'native SBML value', 'Susceptible dogs (S d). Maps to SBML symbol `S_d`.'), 'recovered_dogs_r_d': ('R_d', 'native SBML value', 'Recovered dogs (R d). Maps to SBML symbol `R_d`.'), 'susceptible_humans_s_h': ('S_h', 'native SBML value', 'Susceptible humans (S h). Maps to SBML symbol `S_h`.'), 'recovered_humans_r_h': ('R_h', 'native SBML value', 'Recovered humans (R h). Maps to SBML symbol `R_h`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Ruan2017TransmissionDynamicsAndControlOfRaBiomd0000000726Model = CuratedEpidemiologySBMLModel
