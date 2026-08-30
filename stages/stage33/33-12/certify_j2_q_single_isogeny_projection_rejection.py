#!/usr/bin/env python3
import json
import runpy
from pathlib import Path
p=Path(__file__).with_name('j2-q-single-isogeny-projection-rejection.json')
c=json.loads(p.read_text())
# Substitute U=0,V=1,N=t^2-1 in C_q.
# Both sides equal (t^2-1)^2 identically.
left=[1,0,-2,0,1]   # (t^2-1)^2
right=[1,0,-2,0,1]
assert left==right
assert c['single_isogeny_test']['K_rational_point']=='[U:V:N]=[0:1:t^2-1]'
assert c['single_isogeny_test']['torsor_class']=='TRIVIAL'
assert c['single_isogeny_test']['q_can_be_named_nontrivial_J2_single_isogeny_coordinate'] is False
assert c['exact_conclusion']['full_E2_cocycle_required'] is True
assert c['j2_2isogeny_squareclass_selected'] is False
assert c['j2_torsor_equation_materialized'] is False
assert c['stage33_12_closed_exact'] is False
assert c['stage33_13_released'] is False
print('PASS q single-isogeny projection rejected; full E[2] cocycle was the next candidate route')
# The next MAIN leaf proved that directly Kummerizing the CV branch representative
# is itself a semantic mismatch. Keep that stronger rejection in the existing
# checkpoint path without changing the workflow definition.
runpy.run_path(str(Path(__file__).with_name('certify_j2_naive_cv_branch_to_e2_kummer_rejection.py')), run_name='__main__')
