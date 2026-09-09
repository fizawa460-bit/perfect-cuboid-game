#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'stages/stage32/full178-dominance-recheck-after-v6-o210-q602-route-20260909.json'
ACTIVE = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'
EX5 = ROOT / 'stages/stage32-ex5/MAIN-STATE.json'


def main():
    x = json.loads(ART.read_text())
    a = json.loads(ACTIVE.read_text())
    e = json.loads(EX5.read_text())

    assert x['schema'] == 'STAGE32_FULL178_DOMINANCE_RECHECK_AFTER_V6_O210_Q602_ROUTE_V1'
    assert x['status'] == 'EXACT_SCOPE_RECHECK_FULL178_NOT_DOMINATED'

    claims = {c['claim_id']: c for c in a['claims']}
    f = claims['S32.FULL178.NUMERICAL_CENSUS.V1']
    assert f['scope'] == x['full178_scope']
    assert f['frontier_status'] == 'ACTIVE_INCOMPLETE'
    assert f['authority_status'] == 'DECLARED_GOAL'

    # The retained scope packet records the pre-BC2 receiver inventory.  The
    # merged BC2 state preserves the same 185-row ledger and 5/180 split, but
    # no longer duplicates the derived unibranch_degree_row_count field.
    hist = x['ex5_receiver_scope']
    assert hist['unibranch_degree_row_count'] == 183
    assert hist['row_count'] == 185
    assert hist['status_counts'] == {'CLOSED': 5, 'OPEN': 180, 'UNKNOWN': 0, 'CONDITIONAL': 0, 'OUT_OF_SCOPE': 0}
    assert hist['V6_O210_Q602_treated_as_definition_of_all_receivers'] is False

    rc = e['receiver_contract']
    assert rc['row_count'] == hist['row_count']
    assert rc['status_counts'] == hist['status_counts']
    assert rc['source_lock_complete'] is True
    assert rc['receiver_ledger_complete'] is True
    assert rc['receiver_ledger_coverage_certified'] is True
    assert rc['V6_O210_Q602_treated_as_definition_of_all_receivers'] is False

    # BC2 is an audited infrastructure checkpoint only.  It neither closes a
    # receiver nor turns the independent FULL178 census into a theorem.
    assert e['authority']['current_bc2_authority'] == 'AUDITED'
    assert e['authority']['current_bc2_claim_id'] == 'S32.EX5.BC2_NODE_SUPPORT_SPAN_CHECKPOINT.V1'
    assert e['frontier']['bc2_materially_new_route_admitted'] is True
    assert e['frontier']['bc2_01b_runtime_node_coordinate_bridge_complete'] is False
    assert e['frontier']['nontrivial_receiver_effect_obtained'] is False
    assert e['frontier']['qualified_independent_route_established'] is False
    assert e['credit']['receiver_credit'] is False
    assert e['credit']['FULL178_complete'] is False
    assert e['credit']['stage32_main_credit'] is False
    assert e['firewalls']['receiver_row_closed_by_bc2_checkpoint'] is False
    assert e['firewalls']['FULL178_closed'] is False
    assert e['firewalls']['stage32_main_credit'] is False
    assert e['firewalls']['stage32_closed'] is False

    d = x['decision']
    assert d['full178_dominated_by_v6_o210_q602_nonexistence'] is False
    assert d['full178_remains_independent_main_closure_obligation'] is True
    assert d['ex5_remains_attack_lane'] is True
    assert all(v is False for v in x['firewalls'].values())

    print('PASS_STAGE32_FULL178_NOT_DOMINATED_BY_V6_O210_Q602_SCOPE')


if __name__ == '__main__':
    main()
