#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path
p=Path(__file__).with_name('j2-brauer-to-sha-leray-edge-interface.json')
c=json.loads(p.read_text())
assert c['status']=='PASS_EXACT_INTERFACE_REDUCTION_NOT_YET_COORDINATE'
assert c['source_lock']['stage33_05_descent_presentation_cocycle_blob_sha1']=='02b5a13150f7bf9beb56712498c66acae008e1d8'
assert c['semantic_distinction']['stage33_05_J2_presentation_connecting_cocycle']=='0'
assert c['exact_conclusion']['stage33_05_fixed_LcE_lift_is_not_sha_triviality'] is True
assert c['rejected_shortcuts_retained']['naive_branch_partition_E2_triple']==['1','2','2']
assert c['rejected_shortcuts_retained']['naive_branch_partition_after_Qbar']==['1','1','1']
assert c['required_materialization']['cocycle_condition']=='D_ij + D_jk + D_ki = 0'
assert c['j2_brauer_to_sha_leray_edge_materialized'] is False
assert c['j2_marked_brauer_coordinate_selected'] is False
assert c['stage33_12_closed_exact'] is False
assert c['stage33_13_released'] is False
subprocess.run([sys.executable, str(Path(__file__).with_name('certify_j2_twisted_poincare_torsor_target.py'))], check=True)
print('PASS Brauer-to-Sha Leray edge interface pinned; target refined to index-2 genus-one K3 torsor / twisted-Poincare descent')
