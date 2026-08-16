#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def read_csv(rel: str):
    with (ROOT / rel).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def data(rel: str):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def text(rel: str):
    return (ROOT / rel).read_text(encoding='utf-8')


m2_rows = read_csv('stages/stage18/18-20/counts.csv')
m3_rows = read_csv('stages/stage20/20-20/counts.csv')
panel = read_csv('stages/stage26/26-20/finite-panel.csv')
reg = data('stages/stage26/26-20/finite-registry.json')
ctrl = data('stages/stage26/26-controller.json')
result = text('stages/stage26/26-20/result.md')
num_index = text('docs/stage14-num-reuse-index.md')
contract_audit = text('stages/stage26/26-10/audit.md')

assert 'AUDIT_VERDICT=PASS' in contract_audit
assert ctrl['entry_gate']['stage26_allowed'] is True
assert ctrl['checkpoint10']['audit_record'] == 'stages/stage26/26-10/audit.md'
assert ctrl['checkpoint10']['merge_commit'] == '03ad11b0df214f95c4c077a3b22d12ffe391d160'
assert ctrl['checkpoint_status']['10'] == 'PROVED_AUDITED_PASS_MERGED'

assert len(m2_rows) == len(m3_rows) == len(panel) == 8
assert [r['B'] for r in m2_rows] == [r['B'] for r in m3_rows] == [r['B'] for r in panel]

for s2, s3, out in zip(m2_rows, m3_rows, panel):
    B = int(s2['B'])
    m2 = int(s2['M2'])
    m3 = int(s3['M3'])
    assert int(out['B']) == B
    assert int(out['M2']) == m2
    assert int(out['M3']) == m3
    H = m2 + m3
    P = m2 + 3*m3
    assert int(out['H_ge2']) == H
    assert int(out['P_raw']) == P
    r = Fraction(m3, m2)
    phi = Fraction(m3, H)
    theta = Fraction(3*m3, P)
    assert Fraction(out['r_M3_over_M2']) == r
    assert Fraction(out['Phi']) == phi
    assert Fraction(out['Theta']) == theta
    assert theta == Fraction(3)*phi/(1 + 2*phi)
    assert phi == theta/(3 - 2*theta)
    if phi == 0:
        assert out['Theta_over_Phi'] == 'NA'
    else:
        assert Fraction(out['Theta_over_Phi']) == theta/phi
        assert theta/phi < 3

assert reg['compatibility']['population_match'] is True
assert reg['compatibility']['cutoff_match'] is True
assert reg['compatibility']['multiplicity_match'] is True
assert reg['compatibility']['space_diagonal_required'] is False
assert reg['unmatched_extended_M3']['transition_ratio_allowed'] is False
assert reg['num_reuse']['stage14_num_population_match'] == 'NO_MATCH_SPACE_DIAGONAL_POPULATION'
assert 'The Stage14 integral-space census is not the Stage15/18 ambient exactly-two population.' in num_index

for marker in (
    'FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false',
    'TRUE_M3_EXPONENT_IDENTIFIED=false',
    'SQUARE_ROOT_LAW_CLAIMED=false',
    'MONOTONIC_COMPLETION_RATE_CLAIMED=false',
    'INTEGRAL_SPACE_CENSUS_SUBSTITUTED=false',
    'PERFECT_CUBOID_CONCLUSION=NONE',
):
    assert marker in result, marker

c20 = ctrl['checkpoint20']
if c20['audit_status'] == 'PENDING':
    assert ctrl['state']['CURRENT_CHECKPOINT'] == 20
    assert ctrl['checkpoint_status']['20'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
    assert ctrl['state']['AUDIT_STATUS'] == 'PENDING'
    assert ctrl['state']['ADVANCE_ALLOWED'] is False
    assert ctrl['state']['MERGE_ALLOWED'] is False
    assert ctrl['next_expected_command'] == 'Stage26-audit'
elif c20['audit_status'] == 'PASS' and c20.get('merge_commit') is None:
    assert ctrl['state']['CURRENT_CHECKPOINT'] == 20
    assert ctrl['checkpoint_status']['20'] == 'PROVED_AUDITED_PASS_AWAITING_MERGE'
    assert ctrl['state']['AUDIT_STATUS'] == 'PASS'
    assert ctrl['state']['ADVANCE_ALLOWED'] is True
    assert ctrl['state']['MERGE_ALLOWED'] is True
    assert ctrl['checkpoint_status']['30'] == 'BLOCKED_UNTIL_CHECKPOINT20_MERGE'
    assert ctrl['next_expected_command'] == 'merge PR #1015; then Stage26-main-batch'
    audit = text('stages/stage26/26-20/audit.md')
    assert 'AUDIT_VERDICT=PASS' in audit
elif c20['audit_status'] == 'PASS' and c20.get('merge_commit'):
    assert ctrl['checkpoint_status']['20'] == 'PROVED_AUDITED_PASS_MERGED'
    assert c20['pr'] == 1015
    assert c20['merge_commit'] == 'f1e2d7b718757a85f6b1d2fce25ae442b5c22a87'
    assert ctrl['state']['CURRENT_CHECKPOINT'] >= 30
    assert text('stages/stage26/26-20/audit.md').find('AUDIT_VERDICT=PASS') >= 0
else:
    raise AssertionError(c20['audit_status'])

print('STAGE26_20_SOURCE_CSV_JOIN=PASS')
print('STAGE26_20_EXACT_MULTIPLICITY_BRIDGE=PASS')
print('STAGE26_20_FINITE_PANEL=PASS')
print('STAGE26_20_STAGE14_NUM_FIREWALL=PASS')
print('STAGE26_20_NO_ASYMPTOTIC_PROMOTION=PASS')
print(f"STAGE26_20_LIFECYCLE={ctrl['checkpoint_status']['20']}")
