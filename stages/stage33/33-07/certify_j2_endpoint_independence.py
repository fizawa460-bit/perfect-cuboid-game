#!/usr/bin/env python3
"""Certify that endpoint J2 is a separate proper-transcendental order-2 class.

The coordinate-sign quotient gives a rational map from the smooth proper cuboid
surface S to the proper K3 K_c.  At every codimension-one point of regular S,
the map extends to the DVR by properness of K_c.  Therefore a Brauer class on
K_c pulls back unramified at every divisorial valuation of S; purity places the
pullback in Br(S).  The exact Q_2 scan then shows that this pulled-back class is
not constant.  Testa--Stoll Theorem 10 says Br_1(S)/Br(Q)=0, so the class is
proper-transcendental and cannot be absorbed by BR0B or by the nonextendable
boundary-residue quotient.
"""
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent

def load(p): return json.loads(p.read_text(encoding='utf-8'))

k3=load(S33/'33-05'/'audit-state.json')
probe=load(HERE/'j2-endpoint-q2-pullback.json')
scan=load(HERE/'j2-endpoint-q2-variation.json')
inj=load(HERE/'full-br0b-boundary-injection.json')
finite=load(HERE/'br0g-finite-ramified-residue-presentation.json')

assert k3['unit_status']=='CLOSED' and k3['q_relevant_surviving_dim']==1
assert k3['q_surviving_geometric_br2_basis']==['J2'] and k3['j2_q_descent_certified']
assert probe['j2_endpoint_pullback_nonzero_certified'] and probe['corestriction_invariant']=='1/2'
assert scan['both_invariants_0_and_half_observed'] and scan['evaluation_nonconstant_on_endpoint_Q2_locus_certified']
assert any(r['invariant']=='0' for r in scan['evaluations'])
assert any(r['invariant']=='1/2' for r in scan['evaluations'])
assert inj['proper_cuboid_surface_H1_Q_Pic']==0 and inj['full_br0b_boundary_map_injective']
assert finite['finite_ramified_boundary_residue_module_exact']

cert={
 'schema':'STAGE33_07_J2_ENDPOINT_INDEPENDENCE_V1',
 'source_locks':{
   'stage33_05_audit':'stages/stage33/33-05/audit-state.json',
   'stage33_05_j2':'stages/stage33/33-05/j2_arithmetic_descent.py',
   'coordinate_k3_quotient':'stages/stage29/29-02ha/coordinate-k3-subcover-adapter.md: Sbar -> Kbar_c coordinate-sign quotient; K_c is its proper K3 resolution',
   'physical_boundary_gersten':'stages/stage29/29-02f/boundary-gersten-receiver.md: proper Brauer classes have zero physical-boundary residues',
   'properness_valuative_criterion':'Stacks Project Tag 0BX5, Lemma 29.43.1',
   'brauer_purity':'purity/Gersten exact sequence 0 -> Br(S) -> Br(Q(S)) -> direct_sum_{D in S^(1)} H^1(k(D),Q/Z), as already frozen in Stage29-02f',
   'testa_stoll':'Damiano Testa; Michael Stoll, The surface parametrizing cuboids, Theorem 10: H^1(Q,Pic S)=0 and Br_1(S)/Br(Q)=0',
   'q2_variation':'stages/stage33/33-07/j2-endpoint-q2-variation.json',
 },
 'rational_map':'S --rational--> K_c induced by the Q-defined coordinate-sign quotient',
 'source_class':'J2 in Br(K_c)[2]',
 'source_class_q_defined':True,
 'source_class_unramified_on_proper_k3':True,
 'codimension_one_extension_argument':{
   'S_regular':True,
   'K_c_proper':True,
   'local_ring_at_each_prime_divisor_is_DVR':True,
   'rational_map_extends_over_each_codimension_one_DVR':True,
   'pulled_back_J2_residue_at_every_prime_divisor_of_S':'0',
 },
 'endpoint_pullback_boundary_residue_zero':True,
 'endpoint_pullback_extends_to_proper_BrS':True,
 'endpoint_q2_evaluation_values_observed':['0','1/2'],
 'endpoint_q2_evaluation_nonconstant':True,
 'endpoint_pullback_not_in_image_BrQ':True,
 'proper_algebraic_brauer_mod_constants_zero':True,
 'endpoint_J2_proper_transcendental':True,
 'endpoint_J2_order':2,
 'endpoint_J2_nonzero_mod_constants':True,
 'duplicate_separation':{
   'from_BR0B':True,
   'reason_BR0B':'every nonzero BR0B class has nonzero boundary character by the certified full injection, whereas endpoint J2 has zero boundary residue',
   'from_BR0G_boundary_quotient':True,
   'reason_BR0G':'BR0G contributes boundary residue classes modulo the BR0B constant-character image; endpoint J2 lies in the zero-residue proper kernel',
   'from_line9':True,
   'reason_line9':'Stage33-06 endpoint line9 survivor dimension is zero',
 },
 'j2_duplicate_quotient_exact':True,
 'j2_inventory_entry':{
   'class_id':'K3-J2-ENDPOINT',
   'primary_order':'2',
   'exact_order':2,
   'provenance':['Stage33-05 K_c Creutz--Viray J2','Stage33-07 endpoint rational pullback'],
   'q_defined':True,
   'proper_unramified':True,
   'boundary_residue':'0',
   'nonconstant_q2_evaluation_witnesses':{'s=3':'1/2','s=8':'0'},
 },
 'remaining_residual_kernel':'R33-BR2A-ADAPTED-TWO-PRIMARY-GLOBAL-RELATION-SYMBOL-MATRIX',
 'next_exact_leaf':'L33-07-ASSEMBLE-BLOCK-RELATION-SYMBOL-MATRIX-AND-COMPLETE-INVENTORY',
 'relation_matrix_exact_for_two_primary_branch':False,
 'symbol_matrix_exact_for_two_primary_branch':False,
 'trivial_algebraic_duplicate_quotient_exact':True,
 'unresolved_unknown_in_scope':1,
 'unit_status':'RUNNING','unit_closed':False,'downstream_released':False,
 'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':True,
 'theorem_credit_scope':'Testa--Stoll Theorem 10 plus standard properness/purity only',
 'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(canonical).hexdigest()
(HERE/'j2-endpoint-independence.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({
 'success':True,
 'J2_boundary_residue_zero':True,
 'J2_nonconstant_mod_BrQ':True,
 'J2_proper_transcendental':True,
 'J2_duplicate_quotient_exact':True,
 'remaining_kernel':cert['remaining_residual_kernel'],
 'certificate_sha256':cert['canonical_sha256'],
},indent=2,sort_keys=True))
