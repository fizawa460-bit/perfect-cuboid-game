#!/usr/bin/env python3
"""Verify Goal4I: naive 2-adic scalar descent is unavailable; no nonlinear self-map is certified."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4i-v2-infinite-descent-self-map-preflight.json'
G4A = ROOT / 'stages/stage35-ex/35ex-35/goal4a-two-adic-automatic-square.json'
DECOMP = ROOT / 'stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json'
state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())
g4a = json.loads(G4A.read_text())
dec = json.loads(DECOMP.read_text())

assert state['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V46_GOAL4I_V2_SELF_MAP_PREFLIGHT_PENDING_LATER_AUDIT'
assert art['schema'] == 'STAGE35_EX_35_GOAL4I_V2_INFINITE_DESCENT_SELF_MAP_PREFLIGHT_V1'
assert art['stacked_on_pr'] == 1637
assert art['provisional_parent_goal4h_snapshot'] == 'ec4d078984bf1ce6b5b8707615c1690eaa62e512'

# Audited parity inputs are exact.
assert g4a['input_from_audited_goals_1_to_3']['edge_parity'] == 'exactly one of A,B,C is odd'
assert g4a['input_from_audited_goals_1_to_3']['even_edge_divisibility'] == 'both even edges are divisible by 4'
assert g4a['goal4a_result']['two_adic_space_square_condition_automatic'] is True
assert g4a['goal4a_result']['new_two_adic_valuation_restriction'] is False
assert dec['goal2_primitive_parity_coprimality_dictionary']['edge_parity_theorem'] == 'exactly one of A,B,C is odd; the two even edges are divisible by 4'
assert 'unequal' in dec['goal2_primitive_parity_coprimality_dictionary']['valuation_note']

# If exactly one edge is odd, the minimum 2-adic valuation of the edge triple is zero.
# Therefore no primitive endpoint admits a common scalar division by 2.
for vals in ((0,2,3),(0,4,2),(0,5,8)):
    assert min(vals) == 0

gate = art['descent_gate']
assert gate['common_scalar_two_descent']['available'] is False
assert gate['divide_only_even_edges']['certified_self_map'] is False
assert gate['nonlinear_v2_self_map']['repository_asset_found'] is False
assert gate['nonlinear_v2_self_map']['source_locked_formula_available'] is False
assert gate['nonlinear_v2_self_map']['height_decrease_proved'] is False

res = art['result']
assert res['minimum_v2_scalar_descent_route_closed'] is True
assert res['parity_dictionary_alone_implies_infinite_descent'] is False
assert res['genuine_nonlinear_v2_infinite_descent_proved_impossible'] is False
assert res['genuine_nonlinear_v2_infinite_descent_constructed'] is False
assert res['branch_pruning_obtained'] is False

assert state['current']['unit'] == '35EX-35_GOAL4I_GENUINE_V2_INFINITE_DESCENT_SELF_MAP_PREFLIGHT'
assert state['claims']['goal4i_executed'] is True
assert state['claims']['minimum_v2_scalar_descent_route_closed'] is True
assert state['claims']['genuine_nonlinear_v2_infinite_descent_constructed'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False
print('PASS STAGE35_EX_35_GOAL4I_NAIVE_V2_SCALAR_DESCENT_BLOCKED_NO_NONLINEAR_SELF_MAP')
