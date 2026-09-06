#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4o-spinor-norm-ternary-form-preflight.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
a=json.loads(ART.read_text()); s=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4O_SPINOR_NORM_TERNARY_FORM_PREFLIGHT_V1'
assert a['base_main_sha']==s['base_main_sha']
assert a['stacked_parent']['hostile_audited'] is False
assert a['endpoint_equations']['space']=='W^2=A^2+B^2+C^2'
forms=a['obvious_ternary_forms_checked']
assert len(forms)==4
assert forms[0]['endpoint_representation']=='q3(A,B,C)=W^2'
assert forms[0]['spinor_or_genus_representation_obstruction_can_exclude_endpoint'] is False
for f in forms[1:]:
    assert f['target']=='0'
    assert f['spinor_or_genus_isotropy_obstruction_can_exclude_endpoint'] is False
b=a['exact_boundary']
assert b['obvious_single_form_spinor_route_closed'] is True
assert b['new_local_or_spinor_branch_pruning_obtained'] is False
assert b['cross_face_lattice_or_spinor_correspondence_constructed'] is False
assert b['cross_face_spinor_method_proved_impossible'] is False
assert s['schema']=='STAGE35_EX_PESCH_E1_STATE_V52_GOAL4O_TERNARY_SPINOR_TAUTOLOGY_FAILCLOSE_PENDING_LATER_AUDIT'
assert s['current']['unit']=='35EX-35_GOAL4O_SPINOR_NORM_TERNARY_FORM_PREFLIGHT'
assert s['claims']['goal4o_executed'] is True
assert s['claims']['obvious_ternary_spinor_route_closed'] is True
assert s['claims']['nontrivial_spinor_obstruction_obtained'] is False
assert s['claims']['E1_proved'] is False and s['claims']['stage35_closed'] is False
assert s['claims']['perfect_cuboid_nonexistence_claim'] is False
print('PASS STAGE35_EX_35_GOAL4O_SPINOR_NORM_TERNARY_FORM_PREFLIGHT_V1')
