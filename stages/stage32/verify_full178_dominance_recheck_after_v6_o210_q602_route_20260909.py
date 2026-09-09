#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'stages/stage32/full178-dominance-recheck-after-v6-o210-q602-route-20260909.json'
ACTIVE = ROOT / 'stages/stage32/proof/ACTIVE-FRONTIER.json'
EX5 = ROOT / 'stages/stage32-ex5/MAIN-STATE.json'

OLD_SCHEMA = 'STAGE32EX5_MAIN_COMPACT_STATE_V3_BC2_AUDITED_CHECKPOINT'
CURRENT_SCHEMA = 'STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC'


def verify_historical_v3(e, hist):
    rc = e['receiver_contract']
    assert rc['row_count'] == hist['row_count']
    assert rc['status_counts'] == hist['status_counts']
    assert rc['source_lock_complete'] is True
    assert rc['receiver_ledger_complete'] is True
    assert rc['receiver_ledger_coverage_certified'] is True
    assert rc['V6_O210_Q602_treated_as_definition_of_all_receivers'] is False

    # Historical BC2 infrastructure checkpoint semantics.
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


def verify_current_v4(e, hist):
    # The old 185-row receiver ledger remains historical provenance in the
    # retained dominance packet.  Current EX5 no longer uses that ledger as its
    # live routing contract; it is now an auxiliary producer for 32-01 FULL178.
    auth = e['stage32_main_authority']
    assert auth['control_mode'] == 'FULL178_AND_FINAL_MILESTONE_CHAIN'
    assert auth['primary_incomplete_id'] == '32-01'
    assert auth['primary_incomplete_name'] == 'FULL178'
    assert auth['V6_is_current_attack_target'] is False
    assert auth['O210_is_current_attack_target'] is False
    assert auth['Q602_is_current_attack_target'] is False
    assert auth['historical_formal_q602_residues'] == [73, 97, 235]
    assert auth['historical_formal_q602_residues_are_current_survivors'] is False

    prov = e['historical_formal_provenance']
    assert prov['q602_residue_triple'] == [73, 97, 235]
    assert prov['q602_residue_triple_semantics'] == 'HISTORICAL_FORMAL_PROVENANCE_NOT_CURRENT_SURVIVOR_POPULATION'
    assert prov['v6_o210_q602_current_research_status'] == 'NOT_CURRENT_TARGETS'
    assert prov['old_no_q602_o210_credit_semantics'] == 'HISTORICAL_CREDIT_FIREWALL'

    # Preserve the exact historical receiver packet values rather than
    # pretending they are the current EX5 target definition.
    assert hist['unibranch_degree_row_count'] == 183
    assert hist['row_count'] == 185
    assert hist['status_counts'] == {'CLOSED': 5, 'OPEN': 180, 'UNKNOWN': 0, 'CONDITIONAL': 0, 'OUT_OF_SCOPE': 0}
    assert hist['V6_O210_Q602_treated_as_definition_of_all_receivers'] is False

    iface = e['full178_interface']
    assert iface['stage32_consumption_node'] == 'stages/stage32/32-01-178/nodes/N150/STATE.json'
    assert iface['newer_ex5_progress_auto_promoted_to_main'] is False
    assert iface['population_wide_full178_adapter_complete'] is False
    assert iface['effectivity_or_actual_curve_existence_proved_by_interface'] is False

    frontier = e['frontier']
    assert frontier['runtime_exceptional_index_to_projective_node_bridge_complete'] is True
    assert frontier['picard64_exact_completion_interface_available'] is True
    assert frontier['closed_local_terminal_rank_prefix'] == [0, 398]
    assert frontier['whole_g1_d008_e4_stratum_closed'] is False
    assert frontier['FULL178_complete'] is False
    assert frontier['stage32_main_primary_incomplete_remains_32_01'] is True
    assert frontier['population_wide_main_consumable_result_complete'] is False

    assert e['credit']['receiver_credit'] is False
    assert e['credit']['FULL178_complete'] is False
    assert e['credit']['stage32_main_credit'] is False
    assert e['firewalls']['local_block_unsat_promoted_to_FULL178'] is False
    assert e['firewalls']['ex5_progress_auto_promoted_to_stage32_main'] is False
    assert e['firewalls']['stage32_final_milestone_claimed'] is False


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

    hist = x['ex5_receiver_scope']
    assert hist['unibranch_degree_row_count'] == 183
    assert hist['row_count'] == 185
    assert hist['status_counts'] == {'CLOSED': 5, 'OPEN': 180, 'UNKNOWN': 0, 'CONDITIONAL': 0, 'OUT_OF_SCOPE': 0}
    assert hist['V6_O210_Q602_treated_as_definition_of_all_receivers'] is False

    schema = e.get('schema')
    if schema == OLD_SCHEMA:
        verify_historical_v3(e, hist)
    elif schema == CURRENT_SCHEMA:
        verify_current_v4(e, hist)
    else:
        raise AssertionError(f'unsupported EX5 MAIN-STATE schema: {schema}')

    d = x['decision']
    assert d['full178_dominated_by_v6_o210_q602_nonexistence'] is False
    assert d['full178_remains_independent_main_closure_obligation'] is True
    assert d['ex5_remains_attack_lane'] is True
    assert all(v is False for v in x['firewalls'].values())

    print('PASS_STAGE32_FULL178_NOT_DOMINATED_BY_V6_O210_Q602_SCOPE')
    print(f'ex5_state_schema={schema}')
    if schema == CURRENT_SCHEMA:
        print('current_stage32_mode=FULL178_AND_FINAL_MILESTONE_CHAIN')
        print('historical_q602_residues=[73,97,235]:PROVENANCE_ONLY')


if __name__ == '__main__':
    main()
