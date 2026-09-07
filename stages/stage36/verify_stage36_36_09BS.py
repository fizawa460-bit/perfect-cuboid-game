#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BS/fixed-p-outer-branch-full-cover-local-gate-adapter-preflight.json'; BR=ROOT/'stages/stage36/36-09BR/ay-mordell-weil-congruence-applicability-preflight.json'; BRV=ROOT/'stages/stage36/verify_stage36_36_09BR.py'; AW=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'; BA=ROOT/'stages/stage36/36-09BA/ay-auxiliary-genusone-open-points-preflight.json'; BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'; BH=ROOT/'stages/stage36/36-09BH/bad-place-full-cover-valuation-preflight.json'; BO=ROOT/'stages/stage36/36-09BO/q-reservoir-full-qq-cancellation-preflight.json'; STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='727b3f34c4d850e868aff64483aeb99861b13c7c'; BR_HEAD='0fca8cdf580d07f6993a27f7277deb23bcfe5c21'; BR_CI='34113964982/101716342974'; CERT_BLOB='273f3f33762861fe809929bd8e32dd5153c0a781'
LOCKS={BR:'8d7f7c89fa48ab313eaaa31bbf22ad8430f9a6f7',BRV:'62e491772783806ba9880ac6af3969551933b160',AW:'c1970a020803275ba87b249229e319367fa8f811',BA:'2f31c89b2760f2270fa0ea21106ef97a3ec0840b',BB:'e4b63fd500d05ff5dc704e0c08409edee5895053',BH:'76487371ed363868af18a9fa0f6f7e1367d28f27',BO:'138749fde9766cd217fcb4622ccdebcb45730c2e'}
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def main():
 assert blob(CERT)==CERT_BLOB
 for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
 subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT); subprocess.check_call(['git','merge-base','--is-ancestor',BR_HEAD,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); br=json.loads(BR.read_text()); aw=json.loads(AW.read_text()); ba=json.loads(BA.read_text()); bb=json.loads(BB.read_text()); bh=json.loads(BH.read_text()); bo=json.loads(BO.read_text())
 assert c['batch_parent']=={'pr':1693,'36_09BR_exact_head':BR_HEAD,'36_09BR_exact_head_ci':BR_CI}
 assert br['next_route']['leaf']=='36-09BS_FIXED_P_OUTER_BRANCH_FULL_COVER_LOCAL_GATE_ADAPTER_PREFLIGHT'
 assert aw['fixed_p_outer_enumerator']['outer_superset'] is True and aw['fixed_p_exclusion_rule']['unconditional'] is True
 assert ba['AY_branch']['squareclasses']=='A=B=D=1, C=odd_sf(D0), eta=sign(D0), f=1, e=(1+v2(D0)) mod2'
 assert ba['receiver_intersection_firewall']['auxiliary_C_AY_open_point_implies_top_receiver'] is False
 assert bb['route_result']['receiver_restricted_intersection_exact'] is True
 assert bh['branch_discriminant_support']['new_odd_reservoir_from_full_cover']=='Q=a^2+b^2'
 assert bo['combined_bad_place_local_status']['all_bad_place_local_square_layers_classified'] is True
 a=c['adapter_audit']; safe=c['safe_credit']
 assert a['AW_branch_population_equals_AY_branch_population'] is False
 assert a['AY_is_one_explicit_AW_compatible_branch'] is True
 assert a['filtering_AY_branch_only_excludes_fixed_p_receiver'] is False
 assert a['directly_attach_BH_BO_gate_to_every_AW_branch'] is False
 assert safe['AY_branch_fixed_p_local_elimination_possible_in_principle'] is True
 assert safe['whole_fixed_p_receiver_parameter_elimination_from_AY_gates_alone'] is False
 assert safe['whole_AW_family_parameter_elimination_interface_complete'] is False
 assert c['route_result']['next_leaf']=='36-09BT_GENERAL_AW_SQUARECLASS_BRANCH_FULL_COVER_LOCAL_MODEL_PREFLIGHT'
 st=json.loads(STATE.read_text()); assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V108_36_09BS_POPULATION_ADAPTER'
 bs=st['authority_frontier']['36-09BS']; assert bs['certificate_blob_sha']==CERT_BLOB and bs['AW_BRANCH_POPULATION_EQUALS_AY'] is False and bs['GENERAL_AW_BRANCH_LOCAL_MODEL_OBTAINED'] is False
 assert st['current']['next_exact_leaf']=='36-09BT_GENERAL_AW_SQUARECLASS_BRANCH_FULL_COVER_LOCAL_MODEL_PREFLIGHT' and st['current']['36_09BT_entry_allowed'] is True
 for k in ['finite_exhaustive_H1_twist_family','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']: assert st['claims'][k] is False
 print('36-09BS verified: AW fixed-p outer population is larger than the AY branch. BH-BO local gates are AY-specific and cannot eliminate a whole parameter without a general-branch adapter or independent non-AY discharge. BT selected.')
if __name__=='__main__': main()
