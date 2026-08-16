#!/usr/bin/env python3
from pathlib import Path
import csv, io, json, math

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')

def data(rel):
    return json.loads(text(rel))

res = text('stages/stage27/27-20/result.md')
panel = list(csv.DictReader(io.StringIO(text('stages/stage27/27-20/finite-panel.csv'))))
reg = data('stages/stage27/27-20/finite-registry.json')
ctl = data('stages/stage27/27-controller.json')
a10 = text('stages/stage27/27-10/audit.md')
s19counts = text('stages/stage19/19-20/counts.csv')
s24num = text('stages/stage24/24-14num-r203/result.md')
s19final = text('stages/stage19/final.md')

assert 'AUDIT_VERDICT=PASS' in a10
assert ctl['checkpoint_status']['10'] == 'CONTRACT_AUDITED_PASS_MERGED'
assert ctl['checkpoint10']['pr'] == 1021
assert ctl['checkpoint10']['merge_commit'] == 'f509bba40197262051aad2f22775583b1571a6f5'

for token in ['1000,2','2000,5','5000,15','10000,25','20000,42','50000,62','100000,89']:
    assert token in s19counts, token
for token in ['200000 | 1896505 | 116','500000 | 5899985 | 188','1000000 | 13817725 | 255','98        101         56']:
    assert token in s24num, token
assert 'N_2(500{,}000{,}000)=3495' in s19final
assert '(N_a,N_b,N_c)=(1374,1371,750)' in s19final

rows = [(int(r['B']), int(r['N2'])) for r in panel]
expected = [(1000,2),(2000,5),(5000,15),(10000,25),(20000,42),(50000,62),(100000,89),(200000,116),(500000,188),(1000000,255),(500000000,3495)]
assert rows == expected

for i,r in enumerate(panel):
    B,N = int(r['B']), int(r['N2'])
    assert abs(float(r['N2_over_B_quarter']) - N/(B**0.25)) < 1e-9
    assert abs(float(r['N2_over_sqrt_B']) - N/math.sqrt(B)) < 1e-9
    if i:
        B0,N0 = rows[i-1]
        ae = math.log(N/N0)/math.log(B/B0)
        assert abs(float(r['alpha_eff_from_previous']) - ae) < 1e-9

alpha = math.log(3495/255)/math.log(500000000/1000000)
assert abs(alpha - 0.4212373601119138) < 1e-12
assert abs(reg['derived']['alpha_eff_1m_500m'] - alpha) < 1e-9
assert reg['population_match'] is True
assert reg['cutoff_match'] is True
assert reg['multiplicity_match'] is True
assert reg['interpretation']['true_exponent_identified'] is False
assert reg['interpretation']['finite_data_used_as_asymptotic_proof'] is False
assert reg['firewalls']['half_power_disproved'] is False
assert reg['firewalls']['quarter_power_sharp_proved'] is False
assert reg['firewalls']['perfect_cuboid_conclusion'] == 'NONE'

for marker in [
    'BROAD_WINDOW_ALPHA_EFF_1M_TO_500M=0.421237360',
    'FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false',
    'TRUE_N2_EXPONENT_IDENTIFIED=false',
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
]:
    assert marker in res, marker

assert ctl['checkpoint_status']['20'] == 'DERIVED_EXACT_FINITE_SUBMITTED_PENDING_FRESH_AUDIT'
assert ctl['checkpoint20']['evidence_level'] == 'DERIVED_EXACT_FINITE'
assert ctl['checkpoint20']['finite_data_used_as_asymptotic_proof'] is False
assert ctl['state']['CURRENT_CHECKPOINT'] == 20
assert ctl['state']['NEXT_CHECKPOINT'] == 30
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-audit'

print('STAGE27_20_EXACT_SOURCE_JOIN=PASS')
print('STAGE27_20_DERIVED_FINITE_METRICS=PASS')
print('STAGE27_20_DIRECTIONAL_DIAGNOSTIC=PASS')
print('STAGE27_20_ASYMPTOTIC_FIREWALL=PASS')
