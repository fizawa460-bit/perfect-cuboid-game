#!/usr/bin/env python3
"""Verify Goal4AN: the two fixed known algebraic classes do not empty U_PC(A_Q)."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
P=lambda s: ROOT/s
ART=P('stages/stage35-ex/35ex-35/goal4an-known-two-class-upc-bm-nonempty.json')
SRC=P('stages/stage35-ex/35ex-35/goal4an-known-two-class-upc-bm-nonempty-source-lock.md')
OLD=P('stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json')
OLDMD=P('stages/stage35-ex/35ex-22/obvious-surface-brauer-symbol-blocker.md')
G4Y=P('stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json')
G4Z=P('stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization-source-lock.md')
G4AK=P('stages/stage35-ex/35ex-35/goal4ak-explicit-fb-assembly.json')
G4AL=P('stages/stage35-ex/35ex-35/goal4al-positive-real-class-b-evaluation.json')
G4AM=P('stages/stage35-ex/35ex-35/goal4am-enlarged-finite-local-population-bm-nonempty-blocker.json')
STATE=P('stages/stage35-ex/MAIN-STATE.json')
EXPECTED='e005301a33644d217fd05559126962faf1bc7279b73f473ec3a7cb3bd3e44721'
V74='STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED'
def blob(path:Path)->str:
    b=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def checkcanon(obj):
    x=dict(obj); got=x.pop('canonical_sha256'); calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest(); assert got==calc==EXPECTED,(got,calc)
assert blob(SRC)=='694b23125c59dfd3cd44152c982ac6667391fbf0'
assert blob(OLDMD)=='8be8f94accba0253ad1221ce0025eacdb4537a97'
assert blob(OLD)=='537ca589cd45112cca4c8f8091f5c8c77264e70d'
assert blob(G4Y)=='9351c92747365838cda92d98854ad136df1847d5'
assert blob(G4Z)=='3a1c2174ee6e45bb693791ae2e974ed2f27fe2a3'
assert blob(G4AK)=='5c543b8e5172e19cdb143ba69fcaa55098e5920f'
assert blob(G4AL)=='abe071018509954ff6572fa29ab927ef537d3135'
state=json.loads(STATE.read_text()); assert state['schema']==V74; assert state['last_audited_authority']['hostile_review_id']==5142248509; assert state['claims']['open_receiver_local_evaluations_computed'] is False; assert state['claims']['brauer_manin_obstruction_obtained'] is False; assert state['claims']['E1_proved'] is False
old=json.loads(OLD.read_text()); rp=old['restricted_product_repair']; assert old['surface']['open']=='x*y*p*q*z*w!=0'; assert old['common_zero_specialization']['smooth_on_affine_surface'] is True; assert old['common_zero_specialization']['outside_selected_open_only_because']=='y=0'; assert rp['good_prime_threshold']==173; assert rp['integral_U_PC_Zl_point_for_every_prime_l_ge_173'] is True; assert rp['restricted_product_integrality_proved'] is True; assert rp['common_zero_evaluation_adele_exists'] is True
y=json.loads(G4Y.read_text()); assert y['goal4x_H1_source']['structure']=='Z/2 x Z/2'; assert y['two_step_lift']['independent_algebraic_brauer_classes_certified']==2; assert y['extended_picard_complex']['full_Br_a_U_computed'] is False; assert y['brauer_route']['full_Br_a_U_computed'] is False
ak=json.loads(G4AK.read_text()); assert ak['explicit_rational_function']['class_B_symbol']=='(-1,F_B)'; assert ak['explicit_rational_function']['definition']=='F_B := A31 / B31'
al=json.loads(G4AL.read_text()); assert al['canonical_sha256']=='cd0830cf69988b3745eeb0d4725761ffd997696fcf3cb7329727087c1c709d56'; assert al['result']['class_B_positive_real_component_invariant']=='1/2'
am=json.loads(G4AM.read_text()); assert am['canonical_sha256']=='a04eabc03f1b58f3395d670fc13a81e277d2766b5e80e2b0d5d084dc34d5a5ee'; assert am['route_result']['enlarged_population_BM_nonempty'] is True
art=json.loads(ART.read_text()); checkcanon(art)
assert art['population']['primitive_source_reverse_population_equivalence_proved'] is False
assert art['known_classes']['independent_count']==2; assert art['known_classes']['known_two_classes_exhaust_full_algebraic_brauer_claimed'] is False; assert art['known_classes']['transcendental_brauer_computed'] is False
assert art['anchor_point']['outside_U_PC_only_because_y_zero'] is True
assert art['restricted_product_input']['integral_U_PC_Zl_point_for_every_prime_l_ge_173'] is True; assert art['restricted_product_input']['restricted_product_integrality_proved_by_35ex22'] is True
ba=art['brauer_argument']; assert ba['constructed_restricted_adele_orthogonal_to_A'] is True; assert ba['constructed_restricted_adele_orthogonal_to_B'] is True; assert ba['constructed_restricted_adele_orthogonal_to_span_A_B'] is True
rr=art['route_result']; assert rr['known_two_class_UPC_BM_set_nonempty'] is True; assert rr['known_two_class_span_can_empty_UPC_adelic_population'] is False; assert rr['full_BrU_BM_nonempty_on_UPC_claimed'] is False; assert rr['actual_primitive_source_population_BM_nonempty_claimed'] is False
assert all(v is False for v in art['credit_firewall'].values())
print('STAGE35_EX_GOAL4AN_KNOWN_TWO_CLASS_UPC_BM_NONEMPTY=PASS')
print('known_two_class_UPC_BM_set_nonempty=true')
print('B_positive_real_invariant=1/2_not_standalone_obstruction')
print('next='+rr['next'])
print('canonical_sha256='+EXPECTED)
