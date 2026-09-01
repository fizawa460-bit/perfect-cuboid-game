#!/usr/bin/env python3
"""Certify the corrected named J2 source-to-target Kummer relation.

The retained proper-Br2 domain basis is fixed.  The corrected J2 source is not
a standard retained basis vector: its coordinate is e2+e3.  Therefore the exact
new information is the rank-one linear relation C2+C3=J2_target, not one
materialized standard matrix column.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ADJOINT = HERE / 'j2-picard-adjoint-proper-br2.json'
TARGET = HERE / 'j2-named-v4-h1-target-before-source-orientation.json'
DOMAIN = HERE / 'full-surface-pic2-kummer-target.json'
OUT = HERE / 'j2-named-kummer-source-target-relation.json'
LOCKS = {
    ADJOINT: '066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8',
    TARGET: '4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3',
    DOMAIN: '384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890',
}

def csha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def locked(p):
    x=json.loads(p.read_text()); b=dict(x); h=b.pop('canonical_sha256')
    assert h==LOCKS[p]==csha(b), p
    return x

a=locked(ADJOINT); t=locked(TARGET); d=locked(DOMAIN)
p=a['proper_brauer2_pullback']
s10=p['retained_10D_coordinate_f2']; s14=p['proper_Br2_14D_coordinate_f2']
assert s10 == [0,1,1,0,0,0,0,0,0,0]
basis=d['proper_invariant_domain']['basis_rows_original_proper_br2_coordinates_f2']
recon=[0]*14
for bit,row in zip(s10,basis):
    if bit: recon=[x^(int(y)&1) for x,y in zip(recon,row)]
assert recon==s14
img=t['retained_H1_projection']['coordinates_f2']
assert len(img)==75 and sum(img)==15 and t['retained_H1_projection']['nonzero'] is True
support=[i+1 for i,b in enumerate(s10) if b]
assert support==[2,3]
out={
 'schema':'STAGE33_12_J2_NAMED_KUMMER_SOURCE_TARGET_RELATION_V1',
 'stage':'33-12',
 'status':'PASS_EXACT_NAMED_SOURCE_TARGET_RELATION_MATERIALIZED',
 'source_locks':{
   'picard_adjoint_proper_br2_sha256':LOCKS[ADJOINT],
   'named_J2_V4_H1_target_sha256':LOCKS[TARGET],
   'retained_domain_and_H1_basis_sha256':LOCKS[DOMAIN],
 },
 'source':{
   'named_class':'J2',
   'proper_Br2_14D_coordinate_f2':s14,
   'retained_10D_coordinate_f2':s10,
   'retained_standard_basis_support_1based':support,
   'nonzero':any(s10),
 },
 'target':{
   'ambient_dimension_f2':75,
   'coordinates_f2':img,
   'coordinate_weight':sum(img),
   'nonzero':any(img),
 },
 'exact_linear_relation':{
   'matrix_shape_target_by_source':[75,10],
   'equation':'M * s_J2 = h_J2 over F2',
   'standard_column_equation_1based':'C2 + C3 = h_J2',
   'source_relation_rank_contribution_f2':1,
   'named_source_target_relations_materialized':1,
   'standard_basis_columns_individually_determined_by_this_relation':[],
   'standard_basis_columns_materialized_total_after_this_relation':0,
   'first_exact_standard_basis_column_materialized':False,
   'reason':'s_J2 has weight 2 in the locked retained10 basis; one image relation does not determine C2 or C3 separately.',
 },
 'next_exact_leaf':{
   'goal':'ACCUMULATE_INDEPENDENT_NAMED_SOURCE_TARGET_RELATIONS_UNTIL_STANDARD_COLUMNS_CAN_BE_SOLVED',
   'minimum_useful_next_datum':'one additional exact named source vector and its 75D Kummer image that raises source-relation rank',
   'basis_change_without_explicit_adapter_allowed':False,
 },
 'promotion_firewall':{
   'proper_Br2_14D_coordinate_materialized':True,
   'retained_10D_coordinate_materialized':True,
   'named_source_target_relation_materialized':True,
   'finite_v4_kummer_standard_columns_materialized':0,
   'stage33_12_closed_exact':False,
   'stage33_13_released':False,
   'theorem_credit':False,
   'receiver_credit':False,
   'endpoint_credit':False,
   'perfect_cuboid_existence_claim':False,
   'perfect_cuboid_nonexistence_claim':False,
 }
}
out['canonical_sha256']=csha(out)
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'source10':s10,'support':support,'target_weight':sum(img),'canonical_sha256':out['canonical_sha256']},sort_keys=True))
