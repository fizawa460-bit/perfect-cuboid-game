from pathlib import Path
import json

p = Path(__file__).with_name('ex1-05m-castelnuovo-severi-two-projection-preflight.json')
d = json.loads(p.read_text())

x = d['exact_numeric_replay']
assert x['d1'] == 105
assert x['d2'] == 81
assert x['g1'] == 2
assert x['g2'] == 2
assert (x['d1'] - 1) * (x['d2'] - 1) == 8320
assert x['d1'] * x['g1'] + x['d2'] * x['g2'] == 372
B = x['d1'] * x['g1'] + x['d2'] * x['g2'] + (x['d1'] - 1) * (x['d2'] - 1)
assert B == 8692 == x['castelnuovo_severi_bound']

genera = [106 + r for r in range(29)]
assert min(genera) == 106 and max(genera) == 134
assert all(g <= B for g in genera)
assert min(B - g for g in genera) == 8558

assert 2 * x['d1'] * x['d2'] == 17010 == x['maximum_pair_image_self_intersection']
assert 17010 - x['Gamma_square'] == 1204 == x['self_intersection_defect'] == x['sigma']
assert B - x['Gamma_arithmetic_genus'] == 602 == x['arithmetic_genus_ceiling_defect'] == x['Q_Rosati']
assert (2 * x['d1'] * x['d2'] - x['Gamma_square']) // 2 == 602

for r in range(29):
    gD = 106 + r
    delta = 7984 - r
    assert B - gD == 8586 - r
    assert (B - gD) - delta == 602

q = d['decision']
assert q['Q_states_entering'] == 29
assert q['Q_states_excluded'] == 0
assert q['Q_states_leaving'] == 29
assert q['new_independent_obstruction'] is False
assert q['route_status'] == 'DOMINATED_EXACT_REEXPRESSION_OF_ROSATI_DEFECT_NONPRUNING'

print('PASS_EX1_05M_CS_ROSATI_DEFECT_IDENTITY')
