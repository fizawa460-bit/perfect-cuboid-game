#!/usr/bin/env python3
"""Verify Goal4AO: canonical source 2-adic marking does not empty the known A/B Brauer span."""
from __future__ import annotations
import hashlib, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=lambda s: ROOT/s
ART=P('stages/stage35-ex/35ex-35/goal4ao-source-marked-two-class-bm-nonempty.json')
SRC=P('stages/stage35-ex/35ex-35/goal4ao-source-marked-two-class-bm-nonempty-source-lock.md')
S31=P('stages/stage35-ex/35ex-31/primitive-source-marking-endpoint-equivalence.md')
C31=P('stages/stage35-ex/35ex-31/primitive-source-marking-certificate.json')
A32=P('stages/stage35-ex/35ex-32/post-population-equivalence-breadth-audit.json')
OLD=P('stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json')
AN=P('stages/stage35-ex/35ex-35/goal4an-known-two-class-upc-bm-nonempty.json')
STATE=P('stages/stage35-ex/MAIN-STATE.json')
EXPECTED='e86b7318aa7593b99ab83bed49dbcd2bdbac05e0c828088e7c9917efd97ff858'
V74='STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED'

def blob(path:Path)->str:
    b=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def checkcanon(obj:dict)->None:
    x=dict(obj); got=x.pop('canonical_sha256')
    calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert got==calc==EXPECTED,(got,calc)

def v2_fraction(q:Fraction)->int:
    n=abs(q.numerator); d=q.denominator
    vn=0; vd=0
    while n and n%2==0: vn+=1; n//=2
    while d%2==0: vd+=1; d//=2
    return vn-vd

assert blob(SRC)=='7df55a7ec70fd5ecf37a21819f089dc85bc8299e'
assert blob(S31)=='01aa855c32289a467fb66759e25dc90f18df9f80'
assert blob(C31)=='9f28f4aaeccf3a48cf8c02745708845783dc1788'
assert blob(A32)=='7ca86e3f961d5fc21060a5466599b9622ed91af7'
assert blob(OLD)=='537ca589cd45112cca4c8f8091f5c8c77264e70d'
assert blob(AN)=='e1ada2bf0d985f1ae58434f7542400a0cb1260d7'

state=json.loads(STATE.read_text())
assert state['schema']==V74
assert state['last_audited_authority']['hostile_review_id']==5142248509
assert state['claims']['brauer_manin_obstruction_obtained'] is False
assert state['claims']['E1_proved'] is False

c31=json.loads(C31.read_text())
assert c31['source_endpoint']['source_parity']==['v2(x)>0','v2(y)>0']
assert c31['source_endpoint']['master_v2_dichotomy']=='v2(x)!=v2(y)'
assert c31['reverse_adapter']['marked_endpoint_to_two_primitive_euclid_triples'] is True
assert c31['reverse_adapter']['marked_endpoint_to_master_hit'] is True
assert c31['reverse_adapter']['marked_endpoint_to_E1_counterexample'] is True
assert c31['endpoint_population']['rational_face_diagonals_force_pairwise_distinct_edge_v2'] is True
assert c31['endpoint_population']['unique_minimum_v2_edge'] is True
assert c31['endpoint_population']['minimum_edge_normalization_satisfies_source_marking'] is True

a32=json.loads(A32.read_text())
assert a32['authority']['final_exact_head_sha']=='9f1d3d73f41377bddb1296a3e6fc95b5e2fd8dd7'
assert a32['authority']['merged_main_sha']=='8211bb0ef80de61ecf39c3b97743c58f1193187a'
er=a32['exact_receiver']
assert er['audited_source_equivalence']=='Stage35 E1 counterexamples modulo source-pair swap are equivalent to this population'
assert er['canonical_2adic_fact']=='the three edge v2-valuations are pairwise distinct, so every endpoint orbit has a unique minimum-v2 edge'

old=json.loads(OLD.read_text())
sp=old['common_zero_specialization']['point']
assert sp=={'x':'272/225','y':'0','p':'353/225','q':'1','z':'272/225','w':'353/225'}
assert old['common_zero_specialization']['smooth_on_affine_surface'] is True
assert old['common_zero_specialization']['outside_selected_open_only_because']=='y=0'
rp=old['restricted_product_repair']
assert rp['bad_place_method'].startswith('P0-local nonzero-y deformation')
assert rp['integral_U_PC_Zl_point_for_every_prime_l_ge_173'] is True
assert rp['restricted_product_integrality_proved'] is True

an=json.loads(AN.read_text())
assert an['canonical_sha256']=='e005301a33644d217fd05559126962faf1bc7279b73f473ec3a7cb3bd3e44721'
assert an['route_result']['known_two_class_UPC_BM_set_nonempty'] is True
assert an['brauer_argument']['constructed_restricted_adele_orthogonal_to_span_A_B'] is True

x=Fraction(272,225)
assert v2_fraction(x)==4
# Q_2 neighborhoods of 0 contain nonzero y with arbitrarily large v2(y).
# Therefore any sufficiently small deformation neighborhood can be intersected with v2(y)>4.
for N in (5,6,8,12):
    y=Fraction(2**N,1)
    assert v2_fraction(y)>4 and v2_fraction(y)!=v2_fraction(x)

art=json.loads(ART.read_text()); checkcanon(art)
spa=art['source_population_adapter']
assert spa['hostile_audited'] is True
assert spa['normalized_source_marking']==['v2(x)>0','v2(y)>0','v2(x)!=v2(y)']
assert spa['unique_minimum_v2_edge'] is True
assert spa['marked_endpoint_reconstructs_primitive_source'] is True
loc=art['local_population']
assert loc['necessary_local_relaxation_of_audited_source_population'] is True
assert loc['arbitrary_adele_globalizes_to_primitive_source_claimed'] is False
ta=art['two_adic_anchor']
assert ta['v2_x']==4
assert ta['such_deformations_exist_in_every_sufficiently_small_neighborhood'] is True
assert ta['surface_square_roots_preserved_by_35ex22_local_deformation'] is True
assert ta['source_marking_satisfied'] is True
ba=art['brauer_argument']
assert ba['goal4an_restricted_adele_reused_except_at_2'] is True
assert ba['two_adic_choice_can_lie_in_common_A_B_local_constancy_neighborhood'] is True
assert ba['two_adic_source_marking_and_A_B_evaluation_preservation_simultaneous'] is True
assert ba['constructed_source_marked_local_relaxation_adele_orthogonal_to_span_A_B'] is True
rr=art['route_result']
assert rr['source_marked_local_relaxation_known_two_class_BM_set_nonempty'] is True
assert rr['canonical_2adic_source_marking_rescues_known_two_class_BM_obstruction'] is False
assert rr['actual_discrete_global_source_population_BM_nonempty_claimed'] is False
assert rr['full_BrU_or_Bra_completeness_claimed'] is False
assert all(v is False for v in art['credit_firewall'].values())
print('STAGE35_EX_GOAL4AO_SOURCE_MARKED_TWO_CLASS_BM_NONEMPTY=PASS')
print('v2_x=4; choose v2_y>4 inside the same local-constancy neighborhood')
print('source_marked_local_relaxation_known_two_class_BM_set_nonempty=true')
print('next='+rr['next'])
print('canonical_sha256='+EXPECTED)
