#!/usr/bin/env python3
"""Verify Goal4AM: the enlarged full-U(Qp) finite population is Brauer-Manin nonempty."""
from __future__ import annotations
import hashlib,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4am-enlarged-finite-local-population-bm-nonempty-blocker.json'
SRC=ROOT/'stages/stage35-ex/35ex-35/goal4am-enlarged-finite-local-population-bm-nonempty-blocker-source-lock.md'
G4Y=ROOT/'stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json'
G4AL=ROOT/'stages/stage35-ex/35ex-35/goal4al-positive-real-class-b-evaluation.json'
G4Q=ROOT/'stages/stage35-ex/35ex-35/goal4q-compactification-picard-galois-brauer-candidate-preflight.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
EXPECTED_CANONICAL='a04eabc03f1b58f3395d670fc13a81e277d2766b5e80e2b0d5d084dc34d5a5ee'
V74='STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED'
def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def canonical(o:dict)->str:
    x=dict(o); got=x.pop('canonical_sha256'); calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest(); assert got==calc==EXPECTED_CANONICAL,(got,calc); return got
assert blob(SRC)=='e219e03986b95e81b2c48455761e382bed800649'
assert blob(G4Y)=='9351c92747365838cda92d98854ad136df1847d5'
assert blob(G4AL)=='abe071018509954ff6572fa29ab927ef537d3135'
assert blob(G4Q)=='b1795368ad35e357f7ce5a544c871c665e7b59f9'
state=json.loads(STATE.read_text()); assert state['schema']==V74; assert state['last_audited_authority']['hostile_review_id']==5142248509; assert state['claims']['brauer_manin_obstruction_obtained'] is False; assert state['claims']['E1_proved'] is False
g4y=json.loads(G4Y.read_text()); rp=g4y['open_receiver']['rational_smooth_point']; assert rp=={'x':'3/4','y':'0','p':'5/4','q':'1','z':'3/4','w':'5/4'}; assert g4y['open_receiver']['rational_point_certified'] is True
g4al=json.loads(G4AL.read_text()); assert g4al['canonical_sha256']=='cd0830cf69988b3745eeb0d4725761ffd997696fcf3cb7329727087c1c709d56'; assert g4al['result']['class_B_positive_real_component_invariant']=='1/2'
g4q=json.loads(G4Q.read_text()); assert g4q['singular_locus']['all_nodes_type']=='A1_ordinary_double_point'; assert g4q['infinity_boundary']['all_components_Q_defined'] is True
x=Fraction(3,4); y=Fraction(1,4); p2=Fraction(25,16); q2=Fraction(17,16); z2=Fraction(10,16); w2=Fraction(26,16)
assert p2==1+x*x; assert q2==1+y*y; assert z2==x*x+y*y; assert w2==1+x*x+y*y; assert x>0 and y>0 and p2>0 and q2>0 and z2>0 and w2>0; assert x!=0 and Fraction(5,4)!=0
art=json.loads(ART.read_text()); canonical(art); assert art['rational_smooth_point']['goal4y_certified'] is True; assert art['real_path']['surface_equations_exact'] is True; assert art['real_path']['P0_and_positive_endpoint_same_real_connected_component'] is True; assert art['argument']['diagonal_P0_adelic_is_BM_orthogonal'] is True; assert art['argument']['all_brauer_real_evaluations_unchanged'] is True; assert art['argument']['modified_adelic_point_BM_orthogonal_to_full_BrU'] is True
rr=art['route_result']; assert rr['enlarged_population_BM_nonempty'] is True; assert rr['full_UQp_local_evaluation_can_prove_BM_emptiness_for_E1'] is False; assert rr['primitive_reverse_adapter_can_be_avoided_by_this_enlargement'] is False; assert all(v is False for v in art['credit_firewall'].values())
print('STAGE35_EX_GOAL4AM_ENLARGED_POPULATION_BM_NONEMPTY_BLOCKER=PASS'); print('enlarged_population_BM_nonempty=true'); print('next='+rr['next']); print('canonical_sha256='+EXPECTED_CANONICAL)
