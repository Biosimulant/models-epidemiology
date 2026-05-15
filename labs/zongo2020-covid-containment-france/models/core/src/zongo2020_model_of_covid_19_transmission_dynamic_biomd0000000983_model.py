# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Zongo2020 - model of COVID-19 transmission dynamics under containment measures in France."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000983'
    _TITLE = 'Zongo2020 - model of COVID-19 transmission dynamics under containment measures in France'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S_u', 'I_u', 'S_c', 'E', 'I_r', 'R', 'Q']
    _SPECIES_LABELS = {'S_u': 'Susceptible unconfined', 'I_u': 'Infected unreported', 'S_c': 'Susceptible confined', 'E': 'Exposed', 'I_r': 'Infected reported', 'R': 'Recovered', 'Q': 'Quarantined'}
    _PARAMETER_INPUTS = {'transmission_probability': ('beta', 2.115e-08, 'native model units', 'COVID-19 transmission probability parameter. Maps to SBML symbol `beta`.'), 'incubation_rate': ('sigma', 0.2, 'native model units', 'Exposed-to-infected progression parameter. Maps to SBML symbol `sigma`.'), 'containment_quarantine_rate': ('q', 0.83, 'native model units', 'Containment/quarantine transition parameter. Maps to SBML symbol `q`.'), 'confinement_fraction': ('p', 0.93, 'native model units', 'Fraction assigned to confined susceptible population. Maps to SBML symbol `p`.'), 'unreported_infection_fraction': ('f', 0.2, 'native model units', 'Unreported-infection fraction parameter. Maps to SBML symbol `f`.')}
    _HEADLINE_OUTPUTS = {'susceptible_unconfined': ('S_u', 'native SBML value', 'Susceptible unconfined. Maps to SBML symbol `S_u`.'), 'infected_unreported': ('I_u', 'native SBML value', 'Infected unreported. Maps to SBML symbol `I_u`.'), 'susceptible_confined': ('S_c', 'native SBML value', 'Susceptible confined. Maps to SBML symbol `S_c`.'), 'exposed': ('E', 'native SBML value', 'Exposed. Maps to SBML symbol `E`.'), 'infected_reported': ('I_r', 'native SBML value', 'Infected reported. Maps to SBML symbol `I_r`.'), 'recovered': ('R', 'native SBML value', 'Recovered. Maps to SBML symbol `R`.'), 'quarantined': ('Q', 'native SBML value', 'Quarantined. Maps to SBML symbol `Q`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Zongo2020ModelOfCovid19TransmissionDynamicBiomd0000000983Model = CuratedEpidemiologySBMLModel
