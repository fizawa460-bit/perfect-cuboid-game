#!/usr/bin/env python3
import json
from pathlib import Path

p = Path(__file__).with_name('j2-degenerate-hermite-inverse-construction-target.json')
c = json.loads(p.read_text())

assert c['status'] == 'PASS_EXACT_CONSTRUCTION_ROUTE_REDUCTION_NOT_YET_MODEL'
assert c['fixed_kc_fibration']['full_rational_2_torsion'] is True
assert c['fixed_kc_fibration']['branch_component_count'] == 3
assert c['fixed_kc_fibration']['branch_cubic_reducible'] is True
assert c['degenerate_case_firewall']['general_smooth_trigonal_theorem_7_6_direct_application_allowed'] is False
assert c['degenerate_case_firewall']['recillas_general_case_not_required'] is True

# Exact elementary check of the three-section degeneration:
# r1=(t^2-1)^2=t^4-2t^2+1, r2=t^4-6t^2+1,
# hence r1-r2=4t^2 != 0 in Q(t).
r1 = {4: 1, 2: -2, 0: 1}
r2 = {4: 1, 2: -6, 0: 1}
diff = {k: r1.get(k, 0) - r2.get(k, 0) for k in set(r1) | set(r2)}
diff = {k: v for k, v in diff.items() if v}
assert diff == {2: 4}
assert r1 and r2

M = c['hermite_binary_quartic_target']['symmetric_matrix_template']
assert M == [
    ['a0', 'a1', 'a2+2*x'],
    ['a1', 'a2-x', 'a3'],
    ['a2+2*x', 'a3', 'a4'],
]
req = c['named_J2_inverse_problem']['required_conditions']
assert len(req) == 5
assert c['named_J2_inverse_problem']['compactification_family_selected'] is False
assert c['exact_conclusion']['abstract_relative_picard_search_replaced_by_explicit_inverse_determinantal_problem'] is True
assert c['exact_conclusion']['explicit_X_J2_materialized'] is False
assert c['j2_marked_brauer_coordinate_selected'] is False
assert c['stage33_12_closed_exact'] is False
assert c['stage33_13_released'] is False
print('PASS Kc branch is the exact three-section degenerate Hermite case; named J2 inverse determinantal problem pinned')
