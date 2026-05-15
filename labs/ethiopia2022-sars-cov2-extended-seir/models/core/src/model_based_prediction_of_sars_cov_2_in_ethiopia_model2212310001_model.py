# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Model-based prediction of SARS-CoV-2 in Ethiopia: Extended SEIR model."""

from __future__ import annotations

from typing import Any

from biosim.contrib.sbml import TelluriumSBMLBioModule


class CuratedEpidemiologySBMLModel(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2212310001'
    _TITLE = 'Model-based prediction of SARS-CoV-2 in Ethiopia: Extended SEIR model'
    _TIME_UNIT = 'day'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Sus_com', 'Exp_com', 'Infc_com', 'Rec_com', 'Sus_hcw', 'Exp_hcw', 'Infc_hcw', 'Rec_hcw']
    _SPECIES_LABELS = {'Sus_com': 'Susceptible community', 'Exp_com': 'Exposed community', 'Infc_com': 'Infected community', 'Rec_com': 'Recovered community', 'Sus_hcw': 'Susceptible healthcare workers', 'Exp_hcw': 'Exposed healthcare workers', 'Infc_hcw': 'Infected healthcare workers', 'Rec_hcw': 'Recovered healthcare workers'}
    _PARAMETER_INPUTS = {'community_transmission_rate': ('beta_0', 0.13, 'native model units', 'Community SARS-CoV-2 transmission parameter. Maps to SBML symbol `beta_0`.'), 'incubation_period': ('kappa_inverse', 2.77777777777778, 'native model units', 'Incubation-period parameter. Maps to SBML symbol `kappa_inverse`.'), 'recovery_period': ('gamma_inverse', 10.0, 'native model units', 'Recovery-period parameter. Maps to SBML symbol `gamma_inverse`.'), 'initial_infected': ('I_0', 10.0, 'native model units', 'Initial infected count parameter. Maps to SBML symbol `I_0`.')}
    _HEADLINE_OUTPUTS = {'susceptible_community': ('Sus_com', 'native SBML value', 'Susceptible community. Maps to SBML symbol `Sus_com`.'), 'exposed_community': ('Exp_com', 'native SBML value', 'Exposed community. Maps to SBML symbol `Exp_com`.'), 'infected_community': ('Infc_com', 'native SBML value', 'Infected community. Maps to SBML symbol `Infc_com`.'), 'recovered_community': ('Rec_com', 'native SBML value', 'Recovered community. Maps to SBML symbol `Rec_com`.'), 'susceptible_healthcare_workers': ('Sus_hcw', 'native SBML value', 'Susceptible healthcare workers. Maps to SBML symbol `Sus_hcw`.'), 'exposed_healthcare_workers': ('Exp_hcw', 'native SBML value', 'Exposed healthcare workers. Maps to SBML symbol `Exp_hcw`.'), 'infected_healthcare_workers': ('Infc_hcw', 'native SBML value', 'Infected healthcare workers. Maps to SBML symbol `Infc_hcw`.'), 'recovered_healthcare_workers': ('Rec_hcw', 'native SBML value', 'Recovered healthcare workers. Maps to SBML symbol `Rec_hcw`.')}

    def inputs(self) -> dict[str, Any]:
        specs = super().inputs()
        specs.pop('integration_step', None)
        return specs


ModelBasedPredictionOfSarsCov2InEthiopiaModel2212310001Model = CuratedEpidemiologySBMLModel
