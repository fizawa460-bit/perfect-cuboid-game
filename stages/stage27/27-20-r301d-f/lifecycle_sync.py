#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
cp=ROOT/'stages/stage27/27-controller.json'
ctl=json.loads(cp.read_text(encoding='utf-8'))
R=ctl['derived_routes']

R['Stage27-20-r301'].update({
  'status':'PARALLEL_PREFLIGHT_AUDITED_PASS_MERGED',
  'audit_status':'PASS',
  'audit_record':'stages/stage27/27-20-r301/audit.md',
  'pr':1041,
  'audit_commit':'6b1f4a3747dc6935822989581d85386f0adfa4aa',
  'merge_commit':'1c3c4537e6bddad857e56477298c82d466822919',
  'advance_allowed':True,
  'merge_allowed':True,
})

common_pass={
  'status':'INTERMEDIATE_AUDITED_PASS_MERGED',
  'trigger_checkpoint':40,
  'route_kind':'UPPER_REENTRY_PREFLIGHT',
  'source_stage':'Stage20',
  'audit_status':'PASS',
  'audit_record':'stages/stage27/27-20-r301a-c/audit.md',
  'pr':1042,
  'audit_commit':'c8b012b1c7618438b534d42a4c326750d9cafbed',
  'merge_commit':'1b80ac0d7b62a3098acd81148fac7dc81d90eacc',
  'advance_to_checkpoint50':False,
  'parallel_route':True,
  'advance_allowed':True,
  'merge_allowed':True,
  'strict_sub_sqrt_upper_proved':False,
  'new_mu_lt_half_proved':False,
  'true_N2_exponent_identified':False,
}
R['Stage27-20-r301a']={**common_pass,
  'route_serial':'20-r301a','parent_route':'Stage27-20-r301',
  'purpose':'derive the actual space-diagonal degree-two completion cover on the common two-face host',
  'space_diagonal_double_cover_derived':True,
  'space_diagonal_branch_bidegree':'4_4',
  'space_diagonal_corner_multiplicity':'2_each',
  'space_diagonal_branch_class':'-2K_Y',
  'space_diagonal_K3_type_canonical_class_level':True,
  'full_smooth_K3_classification_proved':False,
  'next_derived_route':'27-20-r301b'}
R['Stage27-20-r301b']={**common_pass,
  'route_serial':'20-r301b','parent_route':'Stage27-20-r301a',
  'purpose':'compare the space-diagonal cover with the Stage20 third-face K3 cover',
  'same_base_host':True,'same_branch_divisor_class':True,'same_K3_canonical_type':True,
  'same_branch_divisor':False,'birational_equivalence_proved':False,
  'stage20_local_densities_transfer':False,
  'next_derived_route':'27-20-r301c'}
R['Stage27-20-r301c']={**common_pass,
  'route_serial':'20-r301c','parent_route':'Stage27-20-r301b',
  'purpose':'freeze the legal thin-cover transfer gate for the actual space-diagonal cover',
  'space_diagonal_thin_cover_architecture_reusable':True,
  'space_diagonal_thin_cover_fixed_power_theorem_proved':False,
  'next_derived_route':'27-20-r301d'}

pending={
  'status':'BATCH_SUBMITTED_PENDING_FRESH_AUDIT',
  'trigger_checkpoint':40,
  'route_kind':'UPPER_REENTRY_PREFLIGHT',
  'source_stage':'Stage20',
  'audit_status':'PENDING',
  'batch_audit_group':'Stage27-20-r301d-f',
  'parallel_route':True,
  'advance_to_checkpoint50':False,
  'advance_allowed':False,
  'merge_allowed':False,
  'strict_sub_sqrt_upper_proved':False,
  'new_mu_lt_half_proved':False,
  'true_N2_exponent_identified':False,
}
R['Stage27-20-r301d']={**pending,
  'route_serial':'20-r301d','parent_route':'Stage27-20-r301c',
  'purpose':'prove the target-specific state-G local blocker transfer for space-diagonal completion',
  'space_diagonal_state_G_reduction_proved':True,
  'space_diagonal_local_blocker_mass_formula_proved':True,
  'space_diagonal_delta_2':'2/9',
  'space_diagonal_delta_p':'2(p-chi4(p))/(p^2+6p+1)',
  'all_stage20_local_factors_transfer':False,
  'next_derived_route':'27-20-r301e'}
R['Stage27-20-r301e']={**pending,
  'route_serial':'20-r301e','parent_route':'Stage27-20-r301d',
  'purpose':'transfer the growing-prime host blocker sieve to the larger space-diagonal completion population and compare it with the half-power theorem',
  'space_diagonal_growing_prime_sieve_transfer_proved':True,
  'space_diagonal_host_sieve_bound':'B(log B)^5/(log log B)^2',
  'N2_host_sieve_bound_proved':True,
  'host_sieve_beats_current_half_power':False,
  'sieve_factor_multiplied_with_half_power':False,
  'next_derived_route':'27-20-r301f'}
R['Stage27-20-r301f']={**pending,
  'route_serial':'20-r301f','parent_route':'Stage27-20-r301e',
  'purpose':'factor the actual space-diagonal branch on torus coordinates and derive the squareclass receiver',
  'space_diagonal_torus_factorization_proved':True,
  'space_diagonal_torus_factorization':'(q1^2+q2^2)(q1^2*q2^2+1)',
  'space_diagonal_squareclass_receiver_derived':True,
  'gaussian_norm_factor_structure_identified':True,
  'squareclass_support_fixed_power_bound_proved':False,
  'squareclass_fiber_fixed_power_saving_proved':False,
  'next_derived_route':'27-20-r301g'}

ctl['safety']['stage20_state_G_blocker_transferred_without_target_reduction']=False
ctl['safety']['stage20_host_sieve_multiplied_with_half_power']=False
ctl['safety']['space_diagonal_squareclass_factorization_promoted_to_power_saving']=False
# Preserve the active r402 checkpoint state; this is a parallel route.
cp.write_text(json.dumps(ctl,indent=2)+'\n',encoding='utf-8')
