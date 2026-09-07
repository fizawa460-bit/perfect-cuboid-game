#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BX/fixed-p-q2-branch-filter-integration-preflight.json'
BW=ROOT/'stages/stage36/36-09BW/general-aw-branch-prime2-taxonomy-preflight.json'; BWV=ROOT/'stages/stage36/verify_stage36_36_09BW.py'
BV=ROOT/'stages/stage36/36-09BV/fixed-p-q-reservoir-branch-filter-integration-preflight.json'; BVV=ROOT/'stages/stage36/verify_stage36_36_09BV.py'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'; BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'; STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e6fd1aec8391c2e9a82eab45c3498afcec99ad44'; PARENT='db0b78e7134db9984b2dd59c0b0313172dfabdf4'; PCI='34123947133/101748106404'
CERT_BLOB='9edd1343c38005d2d47954e2652b43b02079c160'
LOCKS={BW:'d7feb3e6b86c5c93bae999f8836840e64fbd5fb5',BWV:'d698612571fbe7171dc17099eca7db7d012f3dd2',BV:'11b2b927f04c6a7ad151d2456fc79d27329b8dad',BVV:'345fdf7c8133883c3eb261e1313ee56a7b9d7f7f',BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',BUV:'64b889c2dde22d021fb2933b976311d903f57dce',AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df'}
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p):return git('hash-object',str(p.relative_to(ROOT)))
def v2(n):
 c=0
 while n and n%2==0:c+=1;n//=2
 return c
def load_bu():
 s=importlib.util.spec_from_file_location('bu',BUV);m=importlib.util.module_from_spec(s);assert s.loader;s.loader.exec_module(m);return m
def counts(mod,a,b):
 rows=mod.ae_outer(a,b);Q=a*a+b*b;D=a*b*(a-b)*(a+b);sig=v2(Q);delta=v2(D)
 q=[r for r in rows if r[-1]];same=[r for r in q if r[0]%8==r[1]%8];final=[r for r in same if not(r[6]==1 and delta==2*sig+2-r[5])]
 return len(rows),len(q),len(same),len(final)
def main():
 assert blob(CERT)==CERT_BLOB
 for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
 subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT);subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text());bw=json.loads(BW.read_text());bv=json.loads(BV.read_text())
 assert c['base_main_sha']==BASE and c['batch_parent']=={'pr':1693,'36_09BW_exact_head':PARENT,'36_09BW_exact_head_ci':PCI}
 assert bw['route_result']['next_leaf']=='36-09BX_FIXED_P_Q2_BRANCH_FILTER_INTEGRATION_PREFLIGHT'
 assert bv['sound_fixed_p_exclusion_rule']['unconditional'] is True and bv['sound_fixed_p_exclusion_rule']['converse'] is False
 p=c['fixed_p_branch_only_pipeline'];s=c['sound_exclusion_rule'];r=c['route_result'];fw=c['scope_firewalls']
 assert p['all_integrated_rows_are_necessary'] is True and p['remaining_alpha_tie_gates_integrated_as_row_filters'] is False
 assert s['converse'] is False and s['surviving_branch_is_Q2_point'] is False and s['surviving_branch_is_receiver_point'] is False and s['parameter_exclusion_requires_zero_survivors'] is True
 mod=load_bu();assert counts(mod,1,2)==(14,8,6,4);assert counts(mod,2,11)==(158,77,52,30)
 d=c['exact_fixed_p_diagnostics'];assert tuple(d['p_1_over_2'][k] for k in ['AW_AE_outer','after_Q_row','after_AB_residue_filter','after_critical_deep_filter'])==(14,8,6,4);assert tuple(d['p_2_over_11'][k] for k in ['AW_AE_outer','after_Q_row','after_AB_residue_filter','after_critical_deep_filter'])==(158,77,52,30)
 assert r['fixed_p_q2_branch_only_filter_integration_complete'] is True and r['sound_zero_survivor_exclusion_rule'] is True and r['remaining_q2_point_dependent_gates'] is True
 assert r['fixed_p_parameter_exclusion_obtained'] is False and r['candidate_parameter_set_shrunk'] is False and r['receiver_closed'] is False
 assert r['next_leaf']=='36-09BY_REMAINING_Q2_ALPHA_TIE_GATE_PARAMETER_PULLBACK_PREFLIGHT'
 for k in ['surviving_branch_implies_Q2_point','surviving_branch_implies_receiver_point','remaining_alpha_tie_gates_row_only','full_Q2_local_solubility_classified_for_general_AW_branch','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:assert fw[k] is False
 st=json.loads(STATE.read_text());assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V113_36_09BX_FIXED_P_Q2_BRANCH_FILTER_INTEGRATION'
 assert st['status']=='HOSTILE_AUDIT_REPAIR_COMPLETE_PENDING_REAUDIT'
 assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
 b=st['authority_frontier']['36-09BW'];assert b['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and b['exact_head']==PARENT and b['exact_head_ci']==PCI
 x=st['authority_frontier']['36-09BX'];assert x['certificate_blob_sha']==CERT_BLOB and x['FIXED_P_Q2_BRANCH_ONLY_FILTER_INTEGRATION_COMPLETE'] is True and x['SOUND_ZERO_SURVIVOR_EXCLUSION_RULE'] is True
 assert st['current']['next_exact_leaf']=='36-09BY_REMAINING_Q2_ALPHA_TIE_GATE_PARAMETER_PULLBACK_PREFLIGHT'
 assert st['current']['unit']=='36-09BX-REAUDIT-CHECKPOINT'
 assert st['current']['next_owner']=='HOSTILE_REAUDIT_PR_1693'
 assert st['current']['substantive_batch_pr_continues'] is False
 assert st['current']['hostile_audit_checkpoint_reached'] is True
 assert st['current']['36_09BY_entry_allowed'] is False
 assert st['promotion_gates']['36_09BX_failed_audit_review']==5132495760
 assert st['promotion_gates']['36_09BX_hostile_reaudit_passed'] is False
 assert st['promotion_gates']['36_09BY_unlocked'] is False
 for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:assert st['claims'][k] is False
 print('36-09BX verified: mathematics remains exact (14->8->6->4 and 158->77->52->30); hostile audit FAIL 5132495760 is fail-closed, and BY is locked pending re-audit PASS.')
if __name__=='__main__':main()
