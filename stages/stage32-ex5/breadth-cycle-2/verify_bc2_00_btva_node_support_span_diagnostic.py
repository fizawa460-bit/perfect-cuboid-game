#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
LIVE_STATE=ROOT/'stages'/'stage32-ex5'/'MAIN-STATE.json'
FROZEN=HERE/'verify_bc2_00_btva_node_support_span_diagnostic_v4.py'
V31='STAGE32EX5_MAIN_COMPACT_STATE_V31_BC2_38_AUDIT_CONSUMED_BC2_39_EXECUTION'
V32='STAGE32EX5_MAIN_COMPACT_STATE_V32_BC2_39_TARGETED_REPLAY_AUDIT_BOUNDARY'

def req(x,m):
    if not x: raise SystemExit('FAIL: '+m)

def main():
    state=json.loads(LIVE_STATE.read_text()); schema=state['schema']
    allowed={
      'STAGE32EX5_MAIN_COMPACT_STATE_V15_BC2_30_AUDIT_CONSUMED_BC2_31_RECOVERY_EXECUTION','STAGE32EX5_MAIN_COMPACT_STATE_V16_BC2_31_FRESH_REPLAY_AUDIT_BOUNDARY','STAGE32EX5_MAIN_COMPACT_STATE_V17_BC2_31_AUDIT_CONSUMED_BC2_32_EXECUTION','STAGE32EX5_MAIN_COMPACT_STATE_V18_BC2_32_TARGETED_REPLAY_AUDIT_BOUNDARY','STAGE32EX5_MAIN_COMPACT_STATE_V19_BC2_32_AUDIT_CONSUMED_BC2_33_EXECUTION','STAGE32EX5_MAIN_COMPACT_STATE_V20_BC2_33_TARGETED_REPLAY_AUDIT_BOUNDARY','STAGE32EX5_MAIN_COMPACT_STATE_V21_BC2_33_AUDIT_CONSUMED_BC2_34_EXECUTION','STAGE32EX5_MAIN_COMPACT_STATE_V22_BC2_34_TARGETED_REPLAY_AUDIT_BOUNDARY','STAGE32EX5_MAIN_COMPACT_STATE_V23_BC2_34_AUDIT_CONSUMED_BC2_35_EXECUTION','STAGE32EX5_MAIN_COMPACT_STATE_V24_BC2_35_TARGETED_REPLAY_AUDIT_BOUNDARY','STAGE32EX5_MAIN_COMPACT_STATE_V25_BC2_35_AUDIT_CONSUMED_BC2_36_EXECUTION','STAGE32EX5_MAIN_COMPACT_STATE_V26_BC2_36_TARGETED_REPLAY_AUDIT_BOUNDARY','STAGE32EX5_MAIN_COMPACT_STATE_V27_BC2_36_AUDIT_CONSUMED_BC2_37_EXECUTION','STAGE32EX5_MAIN_COMPACT_STATE_V28_BC2_37_TARGETED_REPLAY_AUDIT_BOUNDARY','STAGE32EX5_MAIN_COMPACT_STATE_V29_BC2_37_AUDIT_CONSUMED_BC2_38_EXECUTION','STAGE32EX5_MAIN_COMPACT_STATE_V30_BC2_38_TARGETED_REPLAY_AUDIT_BOUNDARY',V31,V32}
    req(schema in allowed,'live EX5 schema drift')
    b=state['bootstrap']; req(b['active_work_pr']==1776 and b['work_branch']=='stage32ex5-bc2-25-boundary33-mainbatch' and b['merge_authorized'] is False,'work surface')
    a=state['intermediate_audit_boundary']; f=state['frontier']; cur=state['current']; req(a['last_hostile_audit_status']=='PASS','audit PASS missing')
    if schema == V32:
        req(a['last_hostile_audit_exact_head']=='5e1d07e4c92fbecff9bfa89b0bfb65cdaf564a71' and a['last_hostile_audit_review_id']==5190676180,'BC2-38 audit receipt drift')
        req(a['freeze_active'] is True and a['new_audit_boundary_exists'] is True and a['re_audit_required'] is True and a['bc2_39_execution_authorized'] is False,'BC2-39 audit boundary drift')
        req(cur['status']=='BC2_39_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED' and cur['next_route']=='HOSTILE_AUDIT_BC2_39_TARGETED_REPLAY','BC2-39 audit route drift')
        req(f['e8_bc2_38_audited'] is True and f['e8_bc2_39_executed'] is True and f['e8_bc2_39_audited'] is False and f['e8_bc2_39_new_parent_unsat_count']==7 and f['e8_bc2_39_remaining_unknown_count']==23 and f['e8_bc2_39_sat_count']==0 and f['e8_known_parent_unsat_count_lower_bound']==7306 and f['e8_bc2_39_candidate_known_parent_unsat_count_lower_bound']==7313,'BC2-39 V32 frontier drift')
    elif schema == V31:
        req(a['last_hostile_audit_exact_head']=='5e1d07e4c92fbecff9bfa89b0bfb65cdaf564a71' and a['last_hostile_audit_review_id']==5190676180,'BC2-38 audit receipt drift')
        req(a['freeze_active'] is False and a['new_audit_boundary_exists'] is False and a['re_audit_required'] is False and a['bc2_39_execution_authorized'] is True,'BC2-39 execution authority drift')
        req(cur['status']=='BC2_38_HOSTILE_AUDIT_PASS_CONSUMED_BC2_39_EXECUTION_AUTHORIZED' and cur['next_route']=='BC2_39_REFINE_REMAINING_FRESH_UNKNOWN_SET','BC2-39 route drift')
        req(f['e8_bc2_38_audited'] is True and f['e8_bc2_39_executed'] is False and f['e8_bc2_39_target_unknown_count']==30 and f['e8_known_parent_unsat_count_lower_bound']==7306,'BC2-39 V31 frontier drift')
    elif schema.endswith('BC2_38_TARGETED_REPLAY_AUDIT_BOUNDARY'):
        req(a['last_hostile_audit_exact_head']=='9852fcec959962607da3290100291a60185e7104' and a['last_hostile_audit_review_id']==5189412496,'BC2-37 audit receipt drift')
        req(a['freeze_active'] is True and a['new_audit_boundary_exists'] is True and a['re_audit_required'] is True and a['bc2_38_execution_authorized'] is False,'BC2-38 audit boundary drift')
        req(cur['status']=='BC2_38_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED' and cur['next_route']=='HOSTILE_AUDIT_BC2_38_TARGETED_REPLAY','BC2-38 audit route drift')
        req(f['e8_bc2_37_audited'] is True and f['e8_bc2_38_executed'] is True and f['e8_bc2_38_audited'] is False and f['e8_bc2_38_new_parent_unsat_count']==4 and f['e8_bc2_38_remaining_unknown_count']==30 and f['e8_bc2_38_sat_count']==0 and f['e8_known_parent_unsat_count_lower_bound']==7302 and f['e8_bc2_38_candidate_known_parent_unsat_count_lower_bound']==7306,'BC2-38 V30 frontier drift')
    elif schema.endswith('BC2_38_EXECUTION'):
        req(a['last_hostile_audit_exact_head']=='9852fcec959962607da3290100291a60185e7104' and a['last_hostile_audit_review_id']==5189412496,'BC2-37 audit receipt drift')
        req(a['freeze_active'] is False and a['new_audit_boundary_exists'] is False and a['re_audit_required'] is False and a['bc2_38_execution_authorized'] is True,'BC2-38 execution authority drift')
        req(cur['next_route']=='BC2_38_REFINE_REMAINING_FRESH_UNKNOWN_SET','BC2-38 route drift')
        req(f['e8_bc2_37_audited'] is True and f['e8_bc2_38_executed'] is False and f['e8_bc2_38_target_unknown_count']==34 and f['e8_known_parent_unsat_count_lower_bound']==7302,'BC2-38 frontier drift')
    elif schema.endswith('BC2_37_TARGETED_REPLAY_AUDIT_BOUNDARY'):
        req(a['freeze_active'] is True and f['e8_bc2_37_remaining_unknown_count']==34,'BC2-37 boundary drift')
    elif schema.endswith('BC2_37_EXECUTION'):
        req(a['freeze_active'] is False and f['e8_bc2_36_audited'] is True and f['e8_bc2_37_target_unknown_count']==41,'BC2-37 execution drift')
    elif schema.endswith('BC2_36_TARGETED_REPLAY_AUDIT_BOUNDARY'):
        req(a['freeze_active'] is True and f['e8_bc2_36_remaining_unknown_count']==41,'BC2-36 boundary drift')

    if schema not in {V31,V32}:
        req(f['e8_bc2_30_audited'] is True and f['e8_bc2_31_exact_remaining172_recovered'] is False and f['e8_bc2_19_unknown_parent_count']==236 and f['e8_bc2_30_unretained_unknown_identity_count']==172,'historical frontier drift')
    req(f['FULL178_complete'] is False and f['e8_whole_first_block_unsat'] is False and state['credit']['stage32_main_credit'] is False,'local work promoted')

    spec=importlib.util.spec_from_file_location('bc2_00_v4_frozen',FROZEN); req(spec is not None and spec.loader is not None,'cannot load frozen verifier')
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    compat=json.loads(json.dumps(state)); compat['schema']='STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC'
    ma=compat.setdefault('stage32_main_authority',{}); ma.setdefault('control_mode','FULL178_AND_FINAL_MILESTONE_CHAIN'); ma.setdefault('primary_incomplete_id','32-01'); ma.setdefault('Q602_is_current_attack_target',False); ma.setdefault('historical_formal_q602_residues_are_current_survivors',False)
    prior=compat.setdefault('prior_audited_authority',{}); c=prior.setdefault('cycle1',{}); c.setdefault('breadth_cycle','EX5_BREADTH_CYCLE_1'); c.setdefault('authority_status','AUDITED'); c.setdefault('scope_firewall','EX5_BREADTH_CYCLE_1_ONLY')
    e=prior.setdefault('early_bc2',{}); e.setdefault('claim_id','S32.EX5.BC2_NODE_SUPPORT_SPAN_CHECKPOINT.V1')
    compat.setdefault('frontier',{}).setdefault('runtime_exceptional_index_to_projective_node_bridge_complete',True)
    class P:
        def read_text(self,*args,**kwargs): return json.dumps(compat)
    module.MAIN_STATE=P(); module.main(); print('PASS BC2-00 historical replay under live EX5 schema',schema)

if __name__=='__main__': main()
