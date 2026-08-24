#!/usr/bin/env python3
"""Reclassify the global Gersten gap as arithmetic HS descent.

Hostile-audit correction: Stage33-04 is a boundary-residue adapter and did not
claim a complete Q-defined global Brauer-class list. The theorem-scope
regression therefore reopens Stage33-07 global integration credit, not the
Stage33-04 boundary computation.
"""
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
p07=(S33/'33-07'/'materialize_global_two_primary_presentation.py').read_text(encoding='utf-8')
ctl=json.loads((S33/'controller.json').read_text(encoding='utf-8'))
s04=json.loads((S33/'33-04'/'audit-state.json').read_text(encoding='utf-8'))
x=json.loads((HERE/'u44-j2-explicit-representatives.json').read_text())
q=json.loads((HERE/'saturated-q-unit-generators.json').read_text())
old=json.loads((HERE/'global-gersten-csa-effectivity-kernel.json').read_text())

assert 'Panin--Zainoulline Gersten complex with finite mu_n' in p07
assert 'coefficient_gersten_exponent_preserving_lifts = True' in p07
assert ctl['stage33_progress'] in ('6/11','7/11')
assert ctl['stage33_07']['unit_status'] in ('CLOSED','BLOCKED_NEW_KERNEL')
assert s04['unit_status']=='CLOSED'
assert s04['firewalls']['complete_q_defined_brauer_class_list'] is False
assert q['full_rank14_saturated_unit_lattice_generated']
assert x['u44_explicit_representatives_complete'] and x['u44_generator_count']==44
assert x['j2_generic_exact_representative_complete']
assert old['unit_status']=='BLOCKED_NEW_KERNEL'

sources={
 'panin_zainoulline':{
   'id':'arXiv:math/0203128v1',
   'locator':'Theorem 1.1; abstract/introduction',
   'exact_scope':'U=Spec O_{X,x} for a finite set of points x; U is semi-local regular of geometric type; Gersten exactness is asserted for this U',
 },
 'enriquez_jarossay_saettone_svoray':{
   'id':'arXiv:2310.12710v3',
   'locator':'abstract / main simply-connectedness result',
   'exact_used_statement':'the cuboid surface and its minimal resolution have trivial complex fundamental group',
 },
 'horie_yamauchi':{
   'id':'arXiv:2512.22520v3',
   'locator':'Theorem 1.1 and Section 2',
   'exact_used_statement':'Pic(Sbar) has rank 64 and b2(S)=78, hence proper transcendental l-adic rank 14',
 },
 'bloch_ogus_global':{
   'locator':'global Gersten complex middle homology is H^1_Zar(S,H^2); the Bloch-Ogus spectral sequence injects this term into total H^3 for a surface',
 }
}

cert={
 'schema':'STAGE33_08_GLOBAL_GERSTEN_ARITHMETIC_DESCENT_RECLASSIFICATION_V2_HOSTILE_AUDIT',
 'stage33_unit':'33-08','pr':1375,
 'source_locks':sources,
 'predecessor_statement_checked':'stages/stage33/33-07/materialize_global_two_primary_presentation.py',
 'panin_zainoulline_theorem_scope_semilocal':True,
 'stage33_07_used_coefficient_gersten_as_global_surface_surjectivity':True,
 'cited_panin_zainoulline_theorem_alone_justifies_that_global_surjectivity':False,
 'global_bloch_ogus_middle_obstruction_must_be_checked':True,
 'cuboid_minimal_resolution_simply_connected':True,
 'geometric_H1_et_mod_n_zero_for_all_finite_n':True,
 'geometric_H3_et_mu_n2_zero_by_poincare_duality':True,
 'geometric_global_compatible_residue_lift_over_Qbar_repaired':True,
 'proper_transcendental_l_adic_rank':14,
 'proper_transcendental_module_nonzero':True,
 'arithmetic_Q_descent_of_geometric_residue_lifts_certified':False,
 'required_arithmetic_check':'compute the G_Q/Hochschild-Serre descent obstruction for the geometric BR0G residue lifts, including interaction with the proper geometric Brauer module; do not infer Q-defined global classes from invariant residue data alone',
 'stage33_04_boundary_adapter_remains_audited_closed':True,
 'stage33_04_complete_q_defined_global_class_list_was_never_claimed':True,
 'predecessor_reaudit_targets':['33-07'],
 'affected_claims_pending_predecessor_reaudit':[
   'Stage33-07 complete relevant Q-defined global class inventory for the BR0G boundary-residue families',
   'Stage33-07 noncanonical finite Gersten splitting over Q',
   'Stage33-07 global direct-sum presentation of BR0G constant-character and finite ramified lifts'
 ],
 'unaffected_direct_prefix':{
   'full_U_D_explicit_q_rational_basis_rank':14,
   'br0b_left_explicit_parametric_representatives':True,
   'U44_direct_q_defined_quaternion_representatives':44,
   'J2_direct_q_defined_generic_corestriction_CSA':True,
   'seven_line_endpoint_zero':True,
   'stage33_04_boundary_residue_presentation':True
 },
 'supersedes_kernel_id':'R33-BR2B-GLOBAL-GERSTEN-CSA-SECTION-EFFECTIVITY',
 'new_kernel_id':'R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT',
 'new_kernel_exposed':True,
 'predecessor_reaudit_required':True,
 'stage33_07_effective_status_after_hostile_audit':'BLOCKED_NEW_KERNEL',
 'stage33_progress_effective_after_hostile_audit':'6/11',
 'stage33_08_status':'BLOCKED_NEW_KERNEL',
 'stage33_08_unit_closed':False,
 'stage33_09_released':False,
 'advance_allowed_to_downstream':False,
 'next_exact_leaf':'L33-07-REPAIR-COMPUTE-ARITHMETIC-HS-DESCENT-OF-BR0G-RESIDUE-LIFTS',
 'theorem_credit':False,
 'endpoint_credit':False,
 'perfect_cuboid_nonexistence_claim':False
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'global-gersten-arithmetic-descent-kernel.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'STAGE33_04_REMAINS_CLOSED':True,'STAGE33_07_EFFECTIVE_STATUS':'BLOCKED_NEW_KERNEL','GEOMETRIC_GLOBAL_LIFT_OVER_QBAR':True,'ARITHMETIC_Q_DESCENT':False,'NEW_KERNEL_ID':cert['new_kernel_id'],'EFFECTIVE_STAGE33_PROGRESS':'6/11','STAGE33_09_RELEASED':False,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
