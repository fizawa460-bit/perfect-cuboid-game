#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path
p=Path(__file__).with_name('j2-twisted-poincare-torsor-target.json')
c=json.loads(p.read_text())
assert c['status']=='PASS_EXACT_TARGET_REFINEMENT_NOT_YET_EXPLICIT_MODEL'
assert c['fixed_input']['order_of_J2']==2
assert c['fixed_input']['J2_geometrically_nontrivial'] is True
assert c['exact_torsor_consequences']['relative_jacobian_of_X_J2']=='J^0(X_J2) ~= Kc'
assert c['exact_torsor_consequences']['X_J2_has_section'] is False
assert c['exact_torsor_consequences']['multisection_index']==2
assert c['twisted_poincare_interface']['correct_space']=='X_J2 x_{P1} Kc over the smooth base'
assert c['existing_repo_data_reuse']['direct_graph_lift_to_sha_promotion_allowed'] is False
assert c['j2_explicit_torsor_surface_materialized'] is False
assert c['j2_marked_brauer_coordinate_selected'] is False
assert c['stage33_12_closed_exact'] is False
assert c['stage33_13_released'] is False
subprocess.run([sys.executable, str(Path(__file__).with_name('certify_j2_degenerate_hermite_inverse_construction_target.py'))], check=True)
print('PASS J2 target refined to nontrivial index-2 genus-one K3 torsor / twisted-Poincare descent')
