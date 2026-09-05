#!/usr/bin/env python3
"""Verify 35EX-35 Goal4A: the fourth square adds no 2-adic receiver after face parity."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / 'stages/stage35-ex/MAIN-STATE.json'
ART = ROOT / 'stages/stage35-ex/35ex-35/goal4a-two-adic-automatic-square.json'

BASE = '29ba60e69549a89eba7fab936516d17fa517dd2c'
PARENT_MERGE = '5a79ace1a48bcff04e48b021afee75af3a40b8c1'
PARENT_HEAD = 'ea7dffd56ed85e9d8511e04e6aa5b13acfc9f6d3'
PARENT_REVIEW = 5121283524
PARENT_CI_RUN = 33965441116
PARENT_CI_JOB = 101304624506
V36 = 'STAGE35_EX_PESCH_E1_STATE_V36_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE_PENDING_AUDIT'

state = json.loads(STATE.read_text())
art = json.loads(ART.read_text())
assert state['schema'] == V36 and state['stage'] == '35-EX'
assert state['base_main_sha'] == BASE
assert state['current']['unit'] == '35EX-35_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE_TEST'
assert state['current']['status'] == 'PROVISIONAL_GOAL4A_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert state['claims']['goal4a_two_adic_test_completed'] is True
assert state['claims']['goal4_full_test_completed'] is False

assert art['schema'] == 'STAGE35_EX_35_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE_V1'
assert art['base_main_sha'] == BASE
p = art['parent_35ex35_authority']
assert p['promotion_pr'] == 1609
assert p['hostile_reaudit_review_id'] == PARENT_REVIEW
assert p['exact_head_sha'] == PARENT_HEAD
assert p['exact_head_ci_run'] == PARENT_CI_RUN
assert p['exact_head_ci_job'] == PARENT_CI_JOB
assert p['merge_sha'] == PARENT_MERGE

# Elementary 2-adic square criterion regression: odd squares modulo 2^k are
# exactly the units congruent to 1 modulo 8, for the checked lifting range.
for k in range(3, 13):
    mod = 1 << k
    odd_squares = {(r * r) % mod for r in range(1, mod, 2)}
    units_1_mod_8 = {u for u in range(1, mod, 2) if u % 8 == 1}
    assert odd_squares == units_1_mod_8, (k, len(odd_squares), len(units_1_mod_8))

# Exhaust the audited parity branch modulo 2^7.  For A odd and B,C divisible
# by 4, S/A^2 lies in 1+16 Z/128Z and is therefore an odd square class.
mod = 128
odd_squares = {(r * r) % mod for r in range(1, mod, 2)}
for A in range(1, mod, 2):
    inv_a2 = pow((A * A) % mod, -1, mod)
    for B in range(0, mod, 4):
        for C in range(0, mod, 4):
            S = (A * A + B * B + C * C) % mod
            ratio = (S * inv_a2) % mod
            assert ratio % 16 == 1
            assert ratio in odd_squares

res = art['goal4a_result']
assert res['two_adic_space_square_condition_automatic'] is True
assert res['new_two_adic_valuation_restriction'] is False
assert res['new_two_adic_squareclass_receiver'] is False
assert res['forced_output_parity'] == 'any 2-adic square root W is odd'
assert res['forced_output_parity_is_new_input_restriction'] is False

scope = art['scope_boundary']
assert scope['odd_prime_local_conditions_tested'] is False
assert scope['global_integer_space_square_tested'] is False
assert scope['fourth_square_globally_redundant_claimed'] is False
assert scope['private_gcd_route_fully_fail_closed'] is False
assert scope['next_unit'] == '35EX-35_GOAL4B_ODD_PRIME_OR_FINITE_SQUARECLASS_RECEIVER_TEST'

ars = art['arsenal']
assert ars['S34_W01_status'] == 'PREFLIGHT_ONLY_NOT_TRIGGERED'
assert ars['S34_W03_status'] == 'GATED_NO_EXACT_JOINT_LOCAL_WITNESS'
assert ars['S31_W01_status'] == 'GATED_NO_EXACT_GENUS_ONE_QUARTIC_ADAPTER'

fw = art['credit_firewall']
for key in [
    'goal4_full_test_completed', 'new_fourth_square_restriction_obtained',
    'universal_torsor_constructed', 'finite_squareclass_receiver_obtained',
    'E1_proved', 'R29_PESCH_E1_closed', 'R29_FIB2_closed',
    'J12_PARAMETRIC_closed', 'stage35_closed',
    'perfect_cuboid_existence_claim', 'perfect_cuboid_nonexistence_claim',
]:
    assert fw[key] is False, key
assert fw['goal4a_two_adic_test_completed'] is True

print('PASS STAGE35_EX_35_GOAL4A_TWO_ADIC_AUTOMATIC_SQUARE')
