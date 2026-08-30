#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent
C=json.loads((H/'j2-full-galois-discriminant-fixedness-rejection.json').read_text())
P=json.loads((H/'j2-semantic-kc-picard-basis.json').read_text())
D=json.loads((H/'j2-semantic-kc-discriminant-2torsion-target.json').read_text())
R=json.loads((H/'j2-picard-discriminant-galois-functional-rejection.json').read_text())
assert C['schema']=='STAGE33_12_J2_FULL_GALOIS_DISCRIMINANT_FIXEDNESS_REJECTION_V1'
assert P['canonical_sha256']==C['source_locks']['semantic_picard_basis_canonical_sha256']=='c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0'
assert D['canonical_sha256']==C['source_locks']['semantic_discriminant_target_canonical_sha256']=='0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df'
assert R['canonical_sha256']==C['source_locks']['prior_ct_rejection_canonical_sha256']=='ae980dae7e33ecf58e35d697dde1c1be20c98c170bde6b6b9591e9b1f8680e54'
slots=[2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54]
assert P['curve_slots_1based']==slots==C['exact_intersection_reconstruction']['semantic_curve_slots_1based']
# Direct exact intersectionK evaluation of Stoll's linear-section equations for
# CsK[51], CsK[53] against the 17 semantic curves. The final genus-one block
# meets none of the 12 A1 nodes, so raw and resolved pairings agree.
v51=[1,1,1,1,1,1,1,2,2,1,1,1,2,2,0,4,0]
v53=[1,1,1,1,1,1,1,2,2,1,1,1,0,0,2,0,4]
E=C['exact_intersection_reconstruction']
assert E['CsK51_raw_and_resolved_pairing_vector']==v51
assert E['CsK53_raw_and_resolved_pairing_vector']==v53
assert E['CsK51_singular_node_incidence_count']==0==E['CsK53_singular_node_incidence_count']
# semantic positions 16,17 are CsK[52],CsK[54]. Equality of all pairings with
# the full semantic PicK basis, whose Gram determinant is -32, identifies the
# Picard classes exactly.
assert P['gram17'][16]==v51                 # [CsK51]=[CsK54]
assert P['gram17'][15]==v53                 # [CsK53]=[CsK52]
assert P['incidence17x12'][15]==[0]*12 and P['incidence17x12'][16]==[0]*12
assert P['semantic_gram20_determinant']==-32 and P['semantic_basis_index_in_picK']==1
assert C['stoll_complex_conjugation']['slot_permutation_1based']==[[51,54],[52,53]]
G=C['full_galois_action_on_semantic_discriminant_2torsion']
assert G['cc']['u1_fixed'] and G['cc']['u2_fixed']
assert G['ct']['u1_fixed'] and G['ct']['u2_fixed']
assert G['all_three_nonzero_candidates_fixed_by_cc_and_ct'] and G['fixed_subspace_dimension_f2']==2
assert len(D['nonzero_semantic_2torsion_candidates'])==3
assert C['j2_coordinate_materialized'] is False
assert C['stage33_12_closed_exact'] is False and C['stage33_13_released'] is False
for k in ('theorem_credit','receiver_credit','endpoint_credit','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'): assert C[k] is False
x=dict(C); exp=x.pop('canonical_sha256'); got=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest(); assert got==exp,(got,exp)
print(json.dumps({'status':'PASS_EXACT','cc_fixed_dimension_f2':2,'full_galois_candidate_count':3,'canonical_sha256':exp},sort_keys=True))
