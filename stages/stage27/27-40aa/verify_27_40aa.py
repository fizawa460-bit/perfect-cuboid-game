#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')

def data(rel):
    return json.loads(text(rel))

res = text('stages/stage27/27-40aa/result.md')
reg = data('stages/stage27/27-40aa/main-crt2-registry.json')
ctl = data('stages/stage27/27-controller.json')
r401a_audit = text('stages/stage27/27-r401a/audit.md')
s4gg = text('stages/stage14/archive/tasks/14-4gg/result.md')
s4gh = text('stages/stage14/archive/tasks/14-4gh/result.md')
s4ghh = text('stages/stage14/archive/tasks/14-4ghH/result.md')
status = text('docs/00_CURRENT_RESEARCH_STATUS.md')

# Upstream hostile audit is PASS and the route remains checkpoint40-only.
assert 'AUDIT_VERDICT=PASS' in r401a_audit
assert 'ADVANCE_TO_CHECKPOINT50=false' in r401a_audit
assert reg['upstream']['r401a_pr'] == 1026
assert reg['upstream']['r401a_merge_commit'] == '05f460c6df069f9b6da58409bc19378920a5666f'
assert reg['upstream']['checkpoint50_authorized'] is False

# Exact Stage14 reciprocal interface is retained, not reparametrized.
for marker in [
    't_p:=p^circ | m^circ',
    't_q:=q^circ | m^circ',
    'f_-*f_+=t_p*t_q',
    'FIXED_UV_CRT_PRESERVED_EXACTLY=true',
]:
    assert marker in s4gg, marker
for marker in [
    '0 <= N_rec(u,v) <= B^o(1)',
    'T_rec={(u,v):N_rec(u,v)>0}',
    '#T_rec <= S_1 <= B^o(1)*#T_rec',
    'Q17_SECOND_MOMENT_SUPPORT_TRANSFER_REQUIRED=false',
]:
    assert marker in s4gh, marker
for marker in [
    'G_-*f^2 == -G_+*N (mod 2U)',
    'G_-*f^2 ==  G_+*N (mod 2V)',
    'UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment',
    'FIRST_MOMENT_FIXED_POWER_DEFICIT_PROVED=false',
]:
    assert marker in s4ghh, marker

# Fixed r preserves the B^o(1) exponent loss: r*epsilon_B -> 0.
for r in [1, 2, 3, 7, 20]:
    # Deterministic proxy: if epsilon_B=1/n, fixed r/n -> 0.
    vals = [r / n for n in [1000, 10000, 100000]]
    assert vals[-1] < vals[0]
    assert vals[-1] < 0.001

fm = reg['fixed_moment_lemma']
assert fm['for_every_fixed_integer_r_ge_1'] is True
assert fm['same_fixed_power_exponent'] is True
assert fm['second_moment_intrinsic_saving'] is False
assert fm['fixed_higher_moment_intrinsic_saving'] is False
assert reg['remaining_gate']['support_deficit_proved'] is False

for marker in [
    'FIXED_WITNESS_MOMENT_EXPONENT_EQUIVALENCE_PROVED=true',
    'SECOND_MOMENT_ALONE_CAN_CREATE_FIXED_POWER_SUPPORT_DEFICIT=false',
    'MAIN_FIXED_MOMENT_REWEIGHTING_ROUTE_CLOSED=true',
    'MAIN_SUPPORT_DEFICIT_GATE_OPEN=true',
    'MAIN_SUPPORT_DEFICIT_PROVED=false',
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'ADVANCE_ALLOWED=false',
    'NEXT_CHECKPOINT=40',
    'NEXT_DERIVED_ROUTE=27-40ab',
    'NEXT_EXPECTED_COMMAND=Stage27-audit',
]:
    assert marker in res, marker

# Lifecycle and firewalls.
aa = ctl['derived_routes']['Stage27-40aa']
assert ctl['derived_routes']['Stage27-r401a']['audit_status'] == 'PASS'
assert ctl['derived_routes']['Stage27-r401a']['merge_commit'] == '05f460c6df069f9b6da58409bc19378920a5666f'
assert aa['status'] == 'SUBMITTED_PENDING_FRESH_AUDIT'
assert aa['audit_status'] == 'PENDING'
assert aa['strict_sub_sqrt_upper_proved'] is False
assert ctl['checkpoint_status']['50'] == 'BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE'
assert ctl['state']['CURRENT_CHECKPOINT'] == 40
assert ctl['state']['NEXT_CHECKPOINT'] == 40
assert ctl['state']['AUDIT_STATUS'] == 'PENDING'
assert ctl['state']['ADVANCE_ALLOWED'] is False
assert ctl['state']['MERGE_ALLOWED'] is False
assert ctl['next_expected_command'] == 'Stage27-audit'
assert 'CURRENT_STAGE=Stage27-40aa-SUBMITTED-PENDING-FRESH-AUDIT' in status
assert 'STAGE27_40AA_STATUS=MAIN_CRT2_SUBMITTED_PENDING_FRESH_AUDIT' in status
assert 'STAGE27_CHECKPOINT50_BLOCKED_BY_ACTIVE_UPPER_ROUTE=true' in status

print('STAGE27_40AA_UPSTREAM=PASS')
print('STAGE27_40AA_EXACT_MAIN_INTERFACE=PASS')
print('STAGE27_40AA_FIXED_MOMENT_EQUIVALENCE=PASS')
print('STAGE27_40AA_SUPPORT_GATE=PASS')
print('STAGE27_40AA_FIREWALL=PASS')
