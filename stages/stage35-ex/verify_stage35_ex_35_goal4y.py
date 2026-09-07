#!/usr/bin/env python3
"""Verify Goal4Y: both Goal4X H1 generators survive UPic transgression with independent boundary residues."""
from __future__ import annotations
import json, runpy, subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
a=json.loads(ART.read_text())
st=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4Y_OPEN_RECEIVER_UPIC_TWO_CLASS_LIFT_V1'
assert a['base_main_sha']=='8a04691d03f8ec17cf2236aab3d0f0d2dbde3fc3'
assert a['parent']['source_head_sha']=='0a8af929e004815bc9eb5749535885edda0835df'
assert a['parent']['snapshot_blob_sha']=='423e3154c1db1d8d9eaa145eb574137d3afcb3c3'

def blob(path:str)->str:
    return subprocess.check_output(['git','hash-object',str(ROOT/path)],text=True).strip()
for k in ['goal4y_source_lock','goal4x','goal4x_verifier','goal4v','obvious_symbol_layer']:
    x=a['source_locks'][k]
    assert blob(x['path'])==x['blob_sha'], k

# The rational point used to identify Br_a(U) with H^2(Q,UPic(Ubar)).
x=Fraction(3,4); y=Fraction(0); p=Fraction(5,4); q=Fraction(1); z=Fraction(3,4); w=Fraction(5,4)
assert p*p==1+x*x
assert q*q==1+y*y
assert z*z==x*x+y*y
assert w*w==1+x*x+y*y
assert p*q*z*w != 0  # four independent Jacobian columns give rank 4.
assert a['open_receiver']['rational_point_certified'] is True

ns=runpy.run_path(str(ROOT/'stages/stage35-ex/compute_stage35_ex_35_goal4y.py'))
out=ns['out']
assert out['success'] is True
assert out['unit_kernel_rank']==3
I3=[[1,0,0],[0,1,0],[0,0,1]]
assert out['unit_kernel_action_cc']==I3
assert out['unit_kernel_action_ct']==I3
assert out['boundary_orbits_fixed']==24
assert out['boundary_orbits_size2']==4
assert out['finite_residue_character_coordinate_count']==52
assert out['h1_two_generator_positions_0based']==[12,13]
assert out['both_two_step_transgressions_vanish'] is True
assert out['two_residue_vectors_independent'] is True
assert len(out['classes'])==2

exp=a['boundary_residue_representatives']['classes']
for got,want in zip(out['classes'],exp):
    assert got['smith_h1_position_0based']==want['goal4x_smith_position_0based']
    assert got['unit_transgression_3cocycle_is_coboundary'] is True
    assert got['finite_boundary_residue_support_0based']==want['residue_vector_support_0based']
    assert len(got['finite_boundary_residue_vector_bits'])==52
    assert any(got['finite_boundary_residue_vector_bits'])
assert out['classes'][0]['finite_boundary_residue_vector_bits'] != out['classes'][1]['finite_boundary_residue_vector_bits']

up=a['extended_picard_complex']
assert up['boundary_rank']==32 and up['boundary_image_rank']==29
assert up['unit_kernel_rank']==3 and up['pic_Sbar_rank']==64 and up['pic_Ubar_rank']==35
assert up['unit_kernel_galois_action_trivial'] is True
assert up['full_Br_a_U_computed'] is False
lift=a['two_step_lift']
assert lift['both_unit_kernel_3cocycles_integral_coboundaries'] is True
assert lift['both_goal4x_generators_survive_to_H2_UPic'] is True
assert lift['Br_a_U_identification_available_from_U_Q_point'] is True
assert lift['independent_algebraic_brauer_classes_certified']==2
assert lift['full_algebraic_brauer_group_dimension_claimed'] is False
br=a['brauer_route']
assert br['at_least_two_independent_nonconstant_algebraic_classes_exist'] is True
assert br['full_Br_a_U_computed'] is False
assert br['explicit_quaternion_or_cyclic_algebra_representatives_materialized'] is False
assert br['local_evaluations_computed'] is False
assert br['verticality_to_genus5_fibration_proved'] is False
assert br['brauer_manin_obstruction_obtained'] is False

assert st['schema']=='STAGE35_EX_PESCH_E1_STATE_V62_GOAL4Y_TWO_ALGEBRAIC_BRAUER_CLASSES_WITH_BOUNDARY_RESIDUES_PENDING_EXPLICIT_SYMBOL_AND_AUDIT'
assert st['current']['unit']=='35EX-35_GOAL4Y_OPEN_RECEIVER_HS_PURITY_RESIDUE_TWO_CLASS_LIFT_PREFLIGHT'
assert st['current']['next']=='35EX-35_GOAL4Z_OPEN_RECEIVER_TWO_ALGEBRAIC_CLASSES_EXPLICIT_SYMBOL_ADAPTER_PREFLIGHT'
assert st['claims']['open_receiver_unit_lattice_rank']==3
assert st['claims']['open_receiver_unit_galois_action_trivial'] is True
assert st['claims']['open_receiver_H1_two_class_transgression_trivial'] is True
assert st['claims']['open_receiver_two_independent_algebraic_brauer_classes_exist'] is True
assert st['claims']['open_receiver_purity_localization_residue_representatives_computed'] is True
assert st['claims']['open_receiver_algebraic_brauer_group_computed'] is False
assert st['claims']['open_receiver_explicit_rational_symbol_representatives_computed'] is False
assert st['claims']['open_receiver_local_evaluations_computed'] is False
assert st['claims']['brauer_manin_obstruction_obtained'] is False
assert st['claims']['E1_proved'] is False
print('PASS Stage35-EX Goal4Y: rank-3 trivial unit layer, both H1 generators lift to two independent Br_a(U) classes with exact boundary residues; explicit symbols/evaluations remain pending')
