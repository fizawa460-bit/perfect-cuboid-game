#!/usr/bin/env python3
"""Promote the exact J2 Picard-adjoint source and named Kummer relation into live state.

This changes internal Stage33-12 machine state only.  It deliberately does not
count the weight-two J2 source relation as a materialized standard matrix column
and does not close/release any parent unit.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
S33=HERE.parent
CONTROLLER=S33/'controller.json'
RESULT=HERE/'result.md'
ADJ=HERE/'j2-picard-adjoint-proper-br2.json'
REL=HERE/'j2-named-kummer-source-target-relation.json'
U2=HERE/'j2-semantic-u2-full-surface-at2.json'
EXPECTED={
 ADJ:'066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8',
 U2:'60b6d058459f7745f6fa3f9b6d3b44f1610e12ff46c42e3133ec574f71613039',
}
def csha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,expected=None):
 x=json.loads(p.read_text()); b=dict(x); h=b.pop('canonical_sha256'); assert h==csha(b),p
 if expected is not None: assert h==expected,p
 return x,h
adj,_=load(ADJ,EXPECTED[ADJ]); rel,rh=load(REL); u2,_=load(U2,EXPECTED[U2])
p=adj['proper_brauer2_pullback']; r=rel['exact_linear_relation']
assert p['proper_Br2_14D_coordinate_f2']==[1,0,0,1,1,0,0,0,0,0,0,0,0,0]
assert p['retained_10D_coordinate_f2']==[0,1,1,0,0,0,0,0,0,0]
assert r['standard_column_equation_1based']=='C2 + C3 = h_J2'
assert r['standard_basis_columns_materialized_total_after_this_relation']==0
c=json.loads(CONTROLLER.read_text())
c['schema']='STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V51_J2_PICARD_ADJOINT_RELATION_RANK1'
c['current'].update({
 'substep':'ACCUMULATE_INDEPENDENT_NAMED_KUMMER_SOURCE_TARGET_RELATIONS',
 'active_missing_interface':'STANDARD_RETAINED10_KUMMER_MATRIX_NEEDS_INDEPENDENT_SOURCE_TARGET_RELATIONS',
 'next_exact_leaf':'MATERIALIZE_NEXT_INDEPENDENT_Q_DEFINED_PROPER_BR2_SOURCE_WITH_EXACT_75D_KUMMER_IMAGE_AND_REQUIRE_SOURCE_RELATION_RANK_INCREASE',
})
s=c['stage33_12']
s.update({
 'corrected_J2_proper_Br2_14D_coordinate_materialized':True,
 'corrected_J2_proper_Br2_14D_coordinate_f2':p['proper_Br2_14D_coordinate_f2'],
 'corrected_J2_proper_Br2_14D_coordinate_weight':p['proper_Br2_14D_weight'],
 'corrected_J2_retained_10D_domain_coordinate_materialized':True,
 'corrected_J2_retained_10D_domain_coordinate_f2':p['retained_10D_coordinate_f2'],
 'corrected_J2_retained_10D_domain_coordinate_weight':p['retained_10D_weight'],
 'corrected_J2_semantic_u2_full_surface_A_T_2_coordinate_materialized':True,
 'corrected_J2_semantic_u2_full_surface_A_T_2_coordinate_f2':u2['semantic_u2_pullback']['full_surface_A_T_2_coordinates_f2'],
 'corrected_J2_semantic_u2_full_surface_certificate':'stages/stage33/33-12/j2-semantic-u2-full-surface-at2.json',
 'corrected_J2_semantic_u2_full_surface_certificate_sha256':EXPECTED[U2],
 'corrected_J2_picard_adjoint_proper_Br2_certificate':'stages/stage33/33-12/j2-picard-adjoint-proper-br2.json',
 'corrected_J2_picard_adjoint_proper_Br2_certificate_sha256':EXPECTED[ADJ],
 'corrected_J2_named_source_target_relation_materialized':True,
 'corrected_J2_named_source_target_relation':'stages/stage33/33-12/j2-named-kummer-source-target-relation.json',
 'corrected_J2_named_source_target_relation_sha256':rh,
 'corrected_J2_named_source_standard_basis_support_1based':[2,3],
 'corrected_J2_named_standard_column_relation_1based':'C2 + C3 = h_J2',
 'finite_v4_kummer_named_relations_materialized':1,
 'finite_v4_kummer_named_relation_rank_f2':1,
 'finite_v4_kummer_columns_materialized':0,
 'first_exact_kummer_column_materialized':False,
 'minimal_missing_exact_datum':'ADDITIONAL_INDEPENDENT_NAMED_SOURCE_TARGET_RELATIONS_OR_ONE_STANDARD_BASIS_LIFT_TO_SPLIT_RETAINED10_RELATIONS',
 'corrected_J2_order4_route_status':'SUPERSEDED_BY_EXACT_PICARD_ADJOINT_FOR_PROPER_BR2_SOURCE_PLACEMENT',
})
for item in s.get('logical_internal_sequence',[]):
 if item.get('id')=='33-13': item['status']='CURRENT_NAMED_RELATION_RANK_1_STANDARD_COLUMNS_0_OF_10'
c['execution'].update({
 'advance_scope':'STAGE33_12_INTERNAL_33_13_KUMMER_RELATION_ACCUMULATION_ONLY_NO_PARENT_RECLOSURE',
 'heavy_actions_authorized':False,
 'next_item':'Stage33-12_33-13_MATERIALIZE_NEXT_INDEPENDENT_NAMED_SOURCE_TARGET_RELATION',
})
c['loop_state'].update({
 'active':True,
 'stagnation_count':0,
 'last_cycle_route_status':'PASS_J2_PICARD_ADJOINT_SOURCE_AND_NAMED_RELATION_RANK1',
 'last_new_view':'Degree-2 Picard adjunction directly materializes corrected J2 as proper14 [1,0,0,1,1,0,0,0,0,0,0,0,0,0] and retained10 [0,1,1,0,0,0,0,0,0,0]. The locked 75D J2 target therefore gives the exact relation C2+C3=h_J2. Because the retained source has weight two, no standard basis column is individually materialized; accumulate independent named source-target relations instead of fake column credit.'
})
c['audit_scope']='STAGE33_12_INTERNAL_33_13_NAMED_KUMMER_RELATION_ACCUMULATION'
c['advance_scope']='STAGE33_12_INTERNAL_33_13_KUMMER_RELATION_ACCUMULATION_ONLY_NO_PARENT_RECLOSURE'
c['next_item']='Stage33-12_33-13_MATERIALIZE_NEXT_INDEPENDENT_NAMED_SOURCE_TARGET_RELATION'
assert c['release_gates']['stage33_12_closed_exact'] is False
assert c['release_gates']['stage33_07_reclosed'] is False
assert c['release_gates']['stage33_08_released'] is False
assert c['merge_allowed'] is False and c['theorem_credit'] is False and c['receiver_credit'] is False and c['endpoint_credit'] is False
assert c['perfect_cuboid_existence_claim'] is False and c['perfect_cuboid_nonexistence_claim'] is False
CONTROLLER.write_text(json.dumps(c,indent=2,sort_keys=False)+'\n')
marker='## J2 Picard-adjoint source and named Kummer relation — exact\n'
text=RESULT.read_text()
section=f'''\n\n{marker}\nThe degree-2 Picard pullback matrix now determines the adjoint map on the transcendental mod-2 quotients directly.  This bypasses the superseded order-4 half-lift ambiguity and fixes corrected named J2 exactly in the current full-surface proper-Br2 coordinates.\n\n```text\nJ2_PROPER_BR2_14D=[1,0,0,1,1,0,0,0,0,0,0,0,0,0]\nJ2_RETAINED_10D=[0,1,1,0,0,0,0,0,0,0]\nJ2_PICARD_ADJOINT_SHA256={EXPECTED[ADJ]}\n```\n\nThe retained 10D coordinate has weight two.  Therefore the already locked nonzero 75D named J2 target does **not** individually determine standard matrix column 2 or 3.  The exact new information is the rank-one source-target relation\n\n```text\nM * [0,1,1,0,0,0,0,0,0,0]^T = h_J2\nC2 + C3 = h_J2\nNAMED_SOURCE_TARGET_RELATION_RANK_F2=1\nSTANDARD_KUMMER_COLUMNS_MATERIALIZED=0/10\nRELATION_SHA256={rh}\n```\n\nCounting this as `1/10` standard columns would violate the retained-basis contract.  The next exact leaf is to materialize another independent named proper-Br2 source together with its exact 75D Kummer image, increasing the source-relation rank until standard columns can be solved.  Stage33-12 remains open; no parent reclosure, downstream release, theorem, receiver, endpoint, or perfect-cuboid claim is promoted.\n'''
if marker not in text: RESULT.write_text((text.rstrip()+section).rstrip()+'\n')
print(json.dumps({'success':True,'controller_schema':c['schema'],'relation_sha256':rh,'named_relation_rank':1,'standard_columns':0},sort_keys=True))
