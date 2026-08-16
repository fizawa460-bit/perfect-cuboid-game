#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
def text(rel):
    p=ROOT/rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')
def data(rel): return json.loads(text(rel))

res=text('stages/stage25/25-reentry-50/result.md')
reg=data('stages/stage25/25-reentry-50/mechanism-registry.json')
back=data('stages/stage25/25-reentry-50/backflow-proposals.json')
s21=text('stages/stage21/final.md')
s16s=text('stages/stage16s/final.md')
s17=text('stages/stage17/final.md')
r010=text('stages/stage25/25-reentry-r010a/audit.md')
ctrl=data('stages/stage25/25-reentry-controller.json')

assert 'AUDIT_VERDICT=PASS' in r010
assert reg['authorization']['r010a_pr']==1008
assert reg['authorization']['r010a_merge_commit']=='9d2e767697a33195e756af6b366cb6f0548494d3'

assert 'M1(B)~3/(4*pi^2) B^2 log B' in s21
assert 'N1(B)~kappa/(24*pi) B(log B)^3' in s21
assert 'C_raw(B)=2 sum_{P<=B} H(P)L_B(P)' in s21
assert 'full principal multiplicative sector' in s21
assert 'every nonprincipal effective sector loses at least one pole' in s21
assert 'AMBIENT_RATIO=N_S^all(B)/U(B) ~ [9 zeta(3)/(8 pi G)]/B' in s16s
assert 'INTRINSIC_POLYNOMIAL_SPACE_COST=ONE_POWER_OF_B' in s16s
assert 'N_1(B)\\sim\\frac{\\kappa}{24\\pi}B(\\log B)^3' in s17

# Certified conclusion: +2 is a log-power surplus localized to target principal shared-P bulk.
p=reg['principal_sector']
assert p['net_log_power_surplus_relative_to_source']==2
assert p['principal_sector_carries_main_term'] is True
assert p['every_nonprincipal_effective_sector_loses_at_least_one_pole'] is True
assert p['net_principal_pole_surplus_proved'] is False
assert p['source_target_common_pole_ledger_proved'] is False
assert 'LOG2_NET_LOG_POWER_SURPLUS=2' in res
assert 'LOG2_LOCALIZED_TO_SHARED_P_PRINCIPAL_BULK=true' in res
assert 'LOG2_NET_PRINCIPAL_POLE_SURPLUS_PROVED=false' in res
assert 'SOURCE_TARGET_COMMON_POLE_LEDGER_PROVED=false' in res

# No illicit factorization or pole subtraction.
g=reg['open_gate']
assert g['H_one_log_and_L_one_log_proved'] is False
assert g['individual_pole_slots_named'] is False
assert g['independent_factor_product_proved'] is False
assert g['source_target_common_pole_ledger_proved'] is False
assert 'H_AND_L_ONE_LOG_EACH_PROVED=false' in res
assert 'TWO_INDEPENDENT_LOG_FACTORS_PROVED=false' in res

# G22 bridge remains a question, not a 2+2 theorem.
assert reg['g22_bridge']['stage21_net_log_surplus']==2
assert reg['g22_bridge']['stage22_net_log_surplus']==4
assert reg['g22_bridge']['two_plus_two_mechanism_proved'] is False
assert back['queued_derived_routes']==['Stage25-um-r011a']
assert back['phase60_allowed'] is False
assert 'G22_FINE_MECHANISM_CLOSED=false' in res
assert 'PERFECT_CUBOID_CONCLUSION=NONE' in res

# Lifecycle: submission and audited-pass-awaiting-merge are both valid.
p50=ctrl['phase50_submission']
if p50['audit_status']=='PENDING':
    assert p50['advance_allowed'] is False
    assert p50['merge_allowed'] is False
    assert ctrl['phases']['60']['status']=='BLOCKED_UNTIL_PHASE50_DERIVED_ROUTE'
else:
    assert p50['audit_status']=='PASS'
    assert p50['advance_allowed'] is True
    assert p50['merge_allowed'] is True
    assert ctrl['status']=='PHASE50_AUDITED_PASS_AWAITING_MERGE_AND_DERIVED_ROUTE'
    assert ctrl['propagation_queue'][-1]['route_id']=='Stage25-um-r011a'
    assert ctrl['propagation_queue'][-1]['status']=='AUTHORIZED_BY_PHASE50_AUDIT_AWAITING_PARENT_MERGE'
    assert ctrl['phases']['60']['status']=='BLOCKED_UNTIL_R011A_AUDIT_PASS_MERGE'
assert ctrl['stage26_gate']['stage26_allowed'] is False

print('STAGE25_REENTRY_PHASE50_SOURCE_TARGET_CONTROL=PASS')
print('STAGE25_REENTRY_PHASE50_SHARED_P_LOCALIZATION=PASS')
print('STAGE25_REENTRY_PHASE50_LOG_POWER_SURPLUS=PASS')
print('STAGE25_REENTRY_PHASE50_POLE_OVERCLAIM_FIREWALL=PASS')
print('STAGE25_REENTRY_PHASE50_G22_BRIDGE=PASS')
print('STAGE26_GATE=BLOCKED_VALID')
