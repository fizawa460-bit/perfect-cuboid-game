#!/usr/bin/env python3
"""Verify Goal4H: direct S33-PW07 Brauer adapter transfer is hypothesis-blocked."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4h-vertical-brauer-source-lock-preflight.json'
S33 = ROOT / 'stages/stage33/MAIN-STATE.json'
CARD = ROOT / 'docs/arsenal/cards/provisional/S33-PW07.md'
state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())
s33 = json.loads(S33.read_text())
card = CARD.read_text()

assert state['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V45_GOAL4H_VERTICAL_BRAUER_ADAPTER_PREFLIGHT_PENDING_LATER_AUDIT'
assert art['schema'] == 'STAGE35_EX_35_GOAL4H_VERTICAL_BRAUER_SOURCE_LOCK_PREFLIGHT_V1'
assert art['stacked_on_pr'] == 1637
assert art['provisional_parent_goal4g_snapshot'] == '8c96c43a3e39732f2c93cfa871855ccc96ff534e'

# Arsenal card is discovery-only and states the exact adapter hypotheses.
for needle in (
    'Maturity | **PROVISIONAL**',
    'TORSOR_BRAUER_INTEGRAL_KERNEL_ADAPTER',
    'exact common cocycle',
    'intended relative Jacobian',
    'valid Brauer/OS dictionary',
    'resolved literal representative',
):
    assert needle in card, needle
assert 'Frozen discovery snapshot only. The live Stage controller and current source locks override this card.' in card

# Live Stage33 revalidation: it has not yet materialized the type-safe marked Brauer image/full H2(mu2) lift.
assert s33['schema'] == art['live_stage33_revalidation']['schema']
assert s33['current']['active_missing_interface'] == art['live_stage33_revalidation']['current_missing_interface']
front = s33['current_exact_frontier']
assert front['a2_02_marked_brauer_image_computed'] is False
assert front['e3_marked_brauer_image_from_boundary_functions_materialized'] is False
assert front['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False
assert s33['candidate_audit_gate']['status'] == 'PENDING_HOSTILE_AUDIT'

inv = art['stage35_endpoint_inventory']
assert inv['exact_endpoint_equations'] is True
assert inv['private_edge_gcd_six_variable_decomposition'] is True
assert inv['stage35_specific_nonconstant_brauer_class'] is False
assert inv['stage35_specific_exact_common_cocycle'] is False
assert inv['stage35_specific_relative_jacobian'] is False
assert inv['stage35_specific_genus_one_torsor_with_intended_jacobian'] is False
assert inv['stage35_specific_literal_divisor_cartier_representative'] is False
assert inv['brauer_os_identification_for_endpoint_fibration'] is False

matrix = art['hypothesis_matrix']
for k in ('exact_common_cocycle','intended_relative_jacobian','valid_brauer_os_dictionary','semilinear_descent','literal_representative'):
    assert matrix[k].startswith('FAIL_')
assert matrix['integral_kernel_hypotheses'] == 'NOT_REACHED'

res = art['result']
assert res['S33_PW07_direct_transfer_applicable'] is False
assert res['repository_has_ready_stage35_brauer_adapter'] is False
assert res['brauer_manin_obstruction_obtained'] is False
assert res['nonobvious_vertical_brauer_mathematical_route_proved_impossible'] is False

assert state['current']['unit'] == '35EX-35_GOAL4H_NONOBVIOUS_VERTICAL_BRAUER_ENDPOINT_FIBRATION_SOURCE_LOCK_PREFLIGHT'
assert state['claims']['goal4h_executed'] is True
assert state['claims']['S33_PW07_direct_transfer_applicable'] is False
assert state['claims']['nonobvious_vertical_brauer_route_closed'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False
print('PASS STAGE35_EX_35_GOAL4H_S33_PW07_DIRECT_TRANSFER_HYPOTHESIS_BLOCKED')
