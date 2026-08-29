#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).with_name('j2-marked-brauer-exhaustive-view-audit.json')
d=json.loads(p.read_text())
assert d['schema']=='STAGE33_12_J2_MARKED_BRAUER_EXHAUSTIVE_VIEW_AUDIT_V1'
assert d['receiver']=='NAMED_CV_J2_TO_BR_KC_2_EQUALS_HOM_T_KC_Z2'
assert d['candidate_count_before']==3 and d['candidate_count_after']==3
assert d['blind_pass_performed'] is True and d['exhaustive_view_audit_performed'] is True
views={x['id']:x for x in d['blind_generated_views']}
assert views['TWISTED_TRANSCENDENTAL_KERNEL_RECONSTRUCTION']['status']=='LIVE'
assert views['FINITE_REDUCTION_FROBENIUS_ONLY']['status']=='EQUIVALENT'
assert views['DIRECT_PERIOD_OR_CYCLE_PAIRING']['status']=='BLOCKED'
assert d['post_blind_comparison']['kernel_minimum_norm_to_functional']=={'4':[0,1],'8':[1,0],'12':[1,1]}
assert d['selected_next_route']=='TWISTED_TRANSCENDENTAL_KERNEL_RECONSTRUCTION'
assert d['cycle_route_status']=='PASS_NEW_GATE_FROM_STRONGER_VIEW'
assert d['stage33_12_closed_exact'] is False
assert d['stage33_13_released'] is False
assert not d['theorem_credit'] and not d['receiver_credit'] and not d['endpoint_credit']
print('PASS j2 marked Brauer exhaustive view audit')
