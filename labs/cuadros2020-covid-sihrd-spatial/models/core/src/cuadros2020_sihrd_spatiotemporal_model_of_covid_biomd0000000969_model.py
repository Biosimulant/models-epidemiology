# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Cuadros2020 - SIHRD spatiotemporal model of COVID-19 transmission in Ohio."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000969'
    _TITLE = 'Cuadros2020 - SIHRD spatiotemporal model of COVID-19 transmission in Ohio'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Infected_Low_risk_counties', 'Infected_Counties_with_airports', 'Infected_Counties_with_highways', 'Hospitalised_Low_risk_counties', 'Hospitalised_Counties_with_airports', 'Hospitalised_Counties_with_highways', 'ICU_Low_risk_counties', 'ICU_Counties_with_airports']
    _SPECIES_LABELS = {'Infected_Low_risk_counties': 'Infected Low risk counties', 'Infected_Counties_with_airports': 'Infected Counties with airports', 'Infected_Counties_with_highways': 'Infected Counties with highways', 'Hospitalised_Low_risk_counties': 'Hospitalised Low risk counties', 'Hospitalised_Counties_with_airports': 'Hospitalised Counties with airports', 'Hospitalised_Counties_with_highways': 'Hospitalised Counties with highways', 'ICU_Low_risk_counties': 'ICU Low risk counties', 'ICU_Counties_with_airports': 'ICU Counties with airports'}
    _PARAMETER_INPUTS = {'airport_county_transmission_rate': ('lambda_Counties_with_airports', 0.41, 'native model units', 'Transmission parameter for counties with airports. Maps to SBML symbol `lambda_Counties_with_airports`.'), 'highway_county_transmission_rate': ('lambda_Counties_with_highways', 0.23, 'native model units', 'Transmission parameter for counties with highways. Maps to SBML symbol `lambda_Counties_with_highways`.'), 'low_risk_county_transmission_rate': ('lambda_Low_risk_counties', 0.13, 'native model units', 'Transmission parameter for low-risk counties. Maps to SBML symbol `lambda_Low_risk_counties`.'), 'recovery_rate': ('gamma', 0.02, 'native model units', 'Recovery-rate parameter. Maps to SBML symbol `gamma`.'), 'hospital_to_icu_rate': ('phi', 0.04, 'native model units', 'Hospital-to-ICU transition parameter. Maps to SBML symbol `phi`.')}
    _HEADLINE_OUTPUTS = {'infected_low_risk_counties': ('Infected_Low_risk_counties', 'native SBML value', 'Infected Low risk counties. Maps to SBML symbol `Infected_Low_risk_counties`.'), 'infected_counties_with_airports': ('Infected_Counties_with_airports', 'native SBML value', 'Infected Counties with airports. Maps to SBML symbol `Infected_Counties_with_airports`.'), 'infected_counties_with_highways': ('Infected_Counties_with_highways', 'native SBML value', 'Infected Counties with highways. Maps to SBML symbol `Infected_Counties_with_highways`.'), 'hospitalised_low_risk_counties': ('Hospitalised_Low_risk_counties', 'native SBML value', 'Hospitalised Low risk counties. Maps to SBML symbol `Hospitalised_Low_risk_counties`.'), 'hospitalised_counties_with_airports': ('Hospitalised_Counties_with_airports', 'native SBML value', 'Hospitalised Counties with airports. Maps to SBML symbol `Hospitalised_Counties_with_airports`.'), 'hospitalised_counties_with_highways': ('Hospitalised_Counties_with_highways', 'native SBML value', 'Hospitalised Counties with highways. Maps to SBML symbol `Hospitalised_Counties_with_highways`.'), 'icu_low_risk_counties': ('ICU_Low_risk_counties', 'native SBML value', 'ICU Low risk counties. Maps to SBML symbol `ICU_Low_risk_counties`.'), 'icu_counties_with_airports': ('ICU_Counties_with_airports', 'native SBML value', 'ICU Counties with airports. Maps to SBML symbol `ICU_Counties_with_airports`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


Cuadros2020SihrdSpatiotemporalModelOfCovidBiomd0000000969Model = CuratedEpidemiologySBMLModel
