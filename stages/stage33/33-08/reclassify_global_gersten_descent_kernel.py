#!/usr/bin/env python3
"""Reclassify the remaining Stage33-08 gap after direct theorem-scope verification.

The Stage33-07 global presentation cited Panin--Zainoulline/Bloch--Ogus as if
compatible residue data on the whole smooth cuboid surface automatically lifted
to a global Brauer class.  Panin--Zainoulline Theorem 1.1 is a SEMI-LOCAL
statement.  For a global surface the Bloch--Ogus Gersten resolution is a
flasque resolution; the middle cohomology of global sections need not vanish
without an additional global H^3 / Zariski-H^1 argument.

A new 2026 source repairs the *geometric* part for this particular surface:
the minimal resolution of the cuboid surface is simply connected.  Hence for
all finite n (char 0), H^1_et(Sbar,Z/n)=0 and Poincare duality gives
H^3_et(Sbar,mu_n^2)=0.  Thus compatible finite residue data do lift over Qbar.
What remains is arithmetic descent of those geometric lifts to Q, modulo the
proper transcendental Brauer group.  Horie--Yamauchi's H^2 decomposition shows
the proper transcendental l-adic rank is 14, so this is a genuine nonzero
Galois module rather than a vacuous correction.

This file does not revoke a hostile-audited predecessor by itself.  It freezes
a predecessor re-audit kernel and prevents Stage33-08/09 from consuming the
unsupported global-Q lift claim until the arithmetic descent obstruction is
computed exactly.
"""
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
p07=(S33/'33-07'/'materialize_global_two_primary_presentation.py').read_text(encoding='utf-8')
ctl=json.loads((S33/'controller.json').read_text(encoding='utf-8'))
x=json.loads((HERE/'u44-j2-explicit-representatives.json').read_text())
q=json.loads((HERE/'saturated-q-unit-generators.json').read_text())
old=json.loads((HERE/'global-gersten-csa-effectivity-kernel.json').read_text())

assert 'Panin--Zainoulline Gersten complex with finite mu_n' in p07
assert 'coefficient_gersten_exponent_preserving_lifts = True' in p07
assert ctl['stage33_progress']=='7/11'
assert ctl['stage33_07']['unit_status']=='CLOSED'
assert q['full_rank14_saturated_unit_lattice_generated']
assert x['u44_explicit_representatives_complete'] and x['u44_generator_count']==44
assert x['j2_generic_exact_representative_complete']
assert old['unit_status']=='BLOCKED_NEW_KERNEL'

# Source-locked mathematical inputs.  These are theorem-scope statements, not
# newly granted endpoint credit.
sources={
 'panin_zainoulline':{
   'id':'arXiv:math/0203128v1',
   'locator':'Theorem 1.1; abstract/introduction',
   'exact_scope':'U=Spec O_{X,x} for a finite set of points x; U is semi-local regular of geometric type; Gersten exactness is asserted for this U',
 },
 'enriquez_jarossay_saettone_svoray':{
   'id':'arXiv:2310.12710v3',
   'locator':'Theorem A / Corollary A',
   'exact_used_statement':'the cuboid surface and its minimal resolution have trivial complex fundamental group',
 },
 'horie_yamauchi':{
   'id':'arXiv:2512.22520',
   'locator':'Theorem 1.1(1)-(3)',
   'exact_used_statement':'Pic(Sbar) has rank 64; H^2 contains weight-3 modular factors h16^3*h32*h8^3, giving a 14-dimensional proper transcendental l-adic part',
 },
 'bloch_ogus_global':{
   'locator':'global Gersten is a flasque resolution; global-section middle cohomology is H^1_Zar(S,H^2(mu_n^2)) and injects into H^3_et(S,mu_n^2)',
 }
}

cert={
 'schema':'STAGE33_08_GLOBAL_GERSTEN_ARITHMETIC_DESCENT_RECLASSIFICATION_V1',
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
 'required_arithmetic_check':'compute the G_Q descent/HS obstruction for the boundary residue lift classes, including the interaction with the 14-dimensional proper transcendental Brauer module; do not infer Q-defined classes from residue invariance alone',
 'affected_claims_pending_predecessor_reaudit':[
   'Stage33-04 arithmetic Q-defined BR0G constant-character completeness',
   'Stage33-04 arithmetic Q-defined R17/O12 lift completeness',
   'Stage33-07 complete relevant Q-defined class inventory for those BR0G families',
   'Stage33-07 noncanonical finite Gersten splitting over Q'
 ],
 'unaffected_direct_prefix':{
   'full_U_D_explicit_q_rational_basis_rank':14,
   'br0b_left_explicit_parametric_representatives':True,
   'U44_direct_q_defined_quaternion_representatives':44,
   'J2_direct_q_defined_generic_corestriction_CSA':True,
   'seven_line_endpoint_zero':True
 },
 'supersedes_kernel_id':'R33-BR2B-GLOBAL-GERSTEN-CSA-SECTION-EFFECTIVITY',
 'new_kernel_id':'R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT',
 'new_kernel_exposed':True,
 'predecessor_reaudit_required':True,
 'stage33_07_formal_audited_status_not_mutated_by_this_main_batch':True,
 'stage33_progress_formal_pending_reaudit':'7/11',
 'stage33_08_status':'BLOCKED_NEW_KERNEL',
 'stage33_08_unit_closed':False,
 'stage33_09_released':False,
 'advance_allowed':False,
 'next_exact_leaf':'L33-REPAIR-COMPUTE-ARITHMETIC-HS-DESCENT-OF-BR0G-RESIDUE-LIFTS',
 'theorem_credit':False,
 'endpoint_credit':False,
 'perfect_cuboid_nonexistence_claim':False
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'global-gersten-arithmetic-descent-kernel.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'GEOMETRIC_GLOBAL_LIFT_OVER_QBAR':True,'ARITHMETIC_Q_DESCENT':False,'PREDECESSOR_REAUDIT_REQUIRED':True,'NEW_KERNEL_ID':cert['new_kernel_id'],'FORMAL_STAGE33_PROGRESS':'7/11','STAGE33_09_RELEASED':False,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
