#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BR/ay-mordell-weil-congruence-applicability-preflight.json'
BQ=ROOT/'stages/stage36/36-09BQ/relative-factor-squareclass-branch-exhaustiveness-preflight.json'
BQV=ROOT/'stages/stage36/verify_stage36_36_09BQ.py'
BA=ROOT/'stages/stage36/36-09BA/ay-auxiliary-genusone-open-points-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
AI=ROOT/'stages/stage36/36-09AI/j1728-congruent-number-jacobian-preflight.json'
W02=ROOT/'docs/arsenal/cards/formal/S34-W02.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='727b3f34c4d850e868aff64483aeb99861b13c7c'; BQ_HEAD='1cf7c32bba0324ccd0b21ed11eee4876540621ea'; BQ_CI='34113674318/101715419885'; CERT_BLOB='8d7f7c89fa48ab313eaaa31bbf22ad8430f9a6f7'
LOCKS={BQ:'22847973ab424f8a35b49bd3c7a7f32086ba846a',BQV:'befd2a4e16ac413340c283663bd80a4cd1e7e312',BA:'2f31c89b2760f2270fa0ea21106ef97a3ec0840b',BB:'e4b63fd500d05ff5dc704e0c08409edee5895053',AI:'c5af6c4dde67532ea8d592e74aed187c72bbed4e',W02:'13d41be776fcd2edcd258f11bd28c5a6596de45b'}
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def main():
 assert blob(CERT)==CERT_BLOB
 for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
 subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT); subprocess.check_call(['git','merge-base','--is-ancestor',BQ_HEAD,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); bq=json.loads(BQ.read_text()); ba=json.loads(BA.read_text()); bb=json.loads(BB.read_text()); ai=json.loads(AI.read_text()); card=W02.read_text()
 assert c['batch_parent']=={'pr':1693,'36_09BQ_exact_head':BQ_HEAD,'36_09BQ_exact_head_ci':BQ_CI}
 assert bq['route_result']['next_leaf']=='36-09BR_AY_MORDELL_WEIL_CONGRUENCE_APPLICABILITY_PREFLIGHT'
 assert '| Role | `GLOBAL_MORDELL_WEIL_CONGRUENCE_EXCLUSION` |' in card
 assert 'proved full MW basis/generator and complete torsion subgroup' in card
 assert ai['route_result']['Mordell_Weil_rank_classified'] is False
 assert ba['positive_rank_and_infinitude']['rank_E_n_Q_at_least']==1
 assert bb['route_result']['receiver_restricted_intersection_exact'] is True
 m=c['current_MW_credit']; a=c['applicability_result']
 assert m['full_rank_proved'] is False and m['full_free_basis_generators_proved'] is False and m['generator_index_saturation_proved'] is False
 assert a['S34_W02_shape_match'] is True and a['S34_W02_current_authority_applicable'] is False and a['uniform_route_impossibility_proved'] is False
 assert a['route_status']=='BLOCKED_CURRENT_AUTHORITY_MISSING_FULL_MW_NOT_IMPOSSIBILITY'
 assert c['next_route']['leaf']=='36-09BS_FIXED_P_OUTER_BRANCH_FULL_COVER_LOCAL_GATE_ADAPTER_PREFLIGHT'
 st=json.loads(STATE.read_text()); assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V107_36_09BR_MW_APPLICABILITY'
 br=st['authority_frontier']['36-09BR']; assert br['certificate_blob_sha']==CERT_BLOB and br['S34_W02_CURRENTLY_APPLICABLE'] is False and br['UNIFORM_ROUTE_IMPOSSIBILITY_PROVED'] is False
 assert st['current']['next_exact_leaf']=='36-09BS_FIXED_P_OUTER_BRANCH_FULL_COVER_LOCAL_GATE_ADAPTER_PREFLIGHT' and st['current']['36_09BS_entry_allowed'] is True
 for k in ['finite_exhaustive_H1_twist_family','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']: assert st['claims'][k] is False
 print('36-09BR verified: S34-W02 shape matches AY, but full MW basis/rank/saturation is not certified for the parameter-varying E_n family. Route is currently inapplicable, not impossible; BS fixed-p outer/local-gate adapter selected.')
if __name__=='__main__': main()
