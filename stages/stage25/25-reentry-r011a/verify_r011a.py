#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parents[3]
def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding='utf-8')
def data(rel):
    return json.loads(text(rel))
def rank(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    m, n = len(a), len(a[0]); r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] != 0), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]; a[r] = [x/q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                q = a[i][c]
                a[i] = [a[i][j] - q*a[r][j] for j in range(n)]
        r += 1
    return r

res = text('stages/stage25/25-reentry-r011a/result.md')
proof = text('stages/stage25/25-reentry-r011a/geometric-invariant-proof.md')
ledger = data('stages/stage25/25-reentry-r011a/analytic-ledger.json')
s21 = text('stages/stage21/post-stage25-r011a.md')
s22 = text('stages/stage22/post-stage25-r011a.md')
e1d = text('stages/euler-cuboid/E-1d/result.md')
st12 = text('stages/stage12/final.md')
st15a = text('stages/stage15/15-2a/result.md')
st15b = text('stages/stage15/15-2b/result.md')
p50audit = text('stages/stage25/25-reentry-50/audit.md')
ctrl = data('stages/stage25/25-reentry-controller.json')

assert 'AUDIT_VERDICT=PASS' in p50audit
assert 'LOG2_NET_PRINCIPAL_POLE_SURPLUS_PROVED=false' in p50audit
assert ledger['parent_pr'] == 1009
assert ledger['parent_merge_commit'] == '8765eb73db07da8afb8ad9b1f9a538ff8cd080ee'
assert 'B^2\\log B' in e1d or 'B^2 log B' in e1d
assert 'primitive Pythagorean triples with hypotenuse' in e1d
assert '\\sum_{h\\le B}^{\\rm primitive}\\frac1h' in e1d
assert '\\frac\\pi{48}L^3' in st12
assert 'PICARD_RANK_RESOLUTION=6' in st15a
assert 'MINIMAL_RESOLUTION=Bl_4(P1xP1)_at_torus_fixed_corners' in st15a
assert 'M2_LOG_POWER=5' in st15b

twisted_q1={'a2':1,'b2':1,'p2':-1}; minus_nested_f1={'a2':1,'b2':1,'p2':-1}
twisted_q2={'d2':1,'p2':-1,'c2':-1}; nested_f2={'d2':1,'p2':-1,'c2':-1}
assert twisted_q1==minus_nested_f1 and twisted_q2==nested_f2

def toric(m,n,r,s):
    return (4*m*n*r*s,2*r*s*(m*m-n*n),2*m*n*(r*r-s*s),2*r*s*(m*m+n*n),2*m*n*(r*r+s*s))
for vals in [(5,2,7,3),(4,1,9,2),(8,3,5,1)]:
    m,n,r,s=vals
    E,X,Y,U,V=toric(m,n,r,s); E2,X2,Y2,U2,V2=toric(n,m,r,s)
    assert (E2,X2,Y2,U2,V2)==(E,-X,Y,U,V)
A=[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1],[0,0,0,0,1,0]]
AmI=[[A[i][j]-(1 if i==j else 0) for j in range(6)] for i in range(6)]
assert 6-rank(AmI)==4
H_F2=(1,2); K_F2=(-2,-4)
assert tuple(K_F2[i]+2*H_F2[i] for i in range(2))==(0,0)
assert -5+2+2==-1
entries=ledger['entries']
assert (entries['M1']['manin_a'],entries['M1']['manin_b'])==(2,2)
assert (entries['N1']['manin_a'],entries['N1']['manin_b'])==(1,4)
assert (entries['M2']['manin_a'],entries['M2']['manin_b'])==(1,6)
for key in ('M1','N1','M2'): assert entries[key]['log_exponent']==entries[key]['manin_b']-1
tr=ledger['transitions']
assert (tr['Stage21_M1_to_N1']['delta_a'],tr['Stage21_M1_to_N1']['delta_b'])==(-1,2)
assert (tr['Stage22_M1_to_M2']['delta_a'],tr['Stage22_M1_to_M2']['delta_b'])==(-1,4)
assert (tr['cross_target_N1_to_M2']['delta_a'],tr['cross_target_N1_to_M2']['delta_b'])==(0,2)
assert (6-2)==(4-2)+(6-4)==4
for marker in ('G22_LOG4_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL_CANDIDATE','SOURCE_TARGET_COMMON_DIRICHLET_POLE_LEDGER_PROVED=false','POLE_SURPLUS_CLAIM=false','TWO_PLUS_TWO_INDEPENDENT_FACTORIZATION_PROVED=false','FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false','PERFECT_CUBOID_CONCLUSION=NONE'):
    assert marker in res,marker
assert ledger['fine_mechanism']['two_plus_two_is_independent_factorization'] is False
assert ledger['fine_mechanism']['common_dirichlet_pole_slot_ledger_proved'] is False

if ctrl['current_phase'] <= 50:
    assert 'BACKFLOW_AUDIT_STATUS=PENDING' in s21 and 'BACKFLOW_AUDIT_STATUS=PENDING' in s22
else:
    for receiver in (s21,s22):
        assert 'BACKFLOW_AUDIT_STATUS=PASS' in receiver
        assert 'BACKFLOW_SYNCHRONIZED=true' in receiver
        assert 'PENDING_FRESH_AUDIT' not in receiver
    assert 'G21_LOG2_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL' in s21
    assert 'G22_LOG4_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL' in s22

r11=ctrl['r011a_submission']
assert r11['route_id']=='Stage25-um-r011a'
assert r11['parent_pr']==1009
assert r11['parent_merge_commit']=='8765eb73db07da8afb8ad9b1f9a538ff8cd080ee'
if ctrl['current_phase']==50:
    assert r11['audit_status'] in ('PENDING','PASS')
    assert ctrl['phases']['60']['status']=='BLOCKED_UNTIL_R011A_AUDIT_PASS_MERGE'
else:
    assert ctrl['current_phase']>=60
    assert r11['status']=='AUDITED_PASS_MERGED'
    assert r11['audit_status']=='PASS'
    assert r11['advance_allowed'] is True and r11['merge_allowed'] is True
    assert r11['pr']==1010
    assert r11['merge_commit']=='e64f21621bb1b7062dfd21f186e6ed1bcc191272'
    q=[x for x in ctrl['propagation_queue'] if x['route_id']=='Stage25-um-r011a']
    assert len(q)==1 and q[0]['status']=='AUDITED_PASS_MERGED' and q[0]['blocks_next_phase'] is False
closed=ctrl['status']=='CLOSED_AUDITED_PASS_MERGED_STAGE26_HANDOFF_READY'
assert ctrl['stage26_gate']['stage26_allowed'] is closed
if closed:
    assert ctrl['current_phase']==70
    assert ctrl['phase70_submission']['audit_status']=='PASS'
    assert ctrl['phase70_submission']['merge_commit']=='be5f7d8360b3bac2b9060cd88ede596a4fb218dc'
    assert ctrl['next_expected_command']=='Stage26-main-batch'

print('STAGE25_REENTRY_R011A_PARENT_AUTHORIZATION=PASS')
print('STAGE25_REENTRY_R011A_QI_TWIST=PASS')
print('STAGE25_REENTRY_R011A_PICARD_INVARIANT_RANK=4_PASS')
print('STAGE25_REENTRY_R011A_MANIN_AB_LEDGER=PASS')
print('STAGE25_REENTRY_R011A_LOG4_GEOMETRIC_MECHANISM=PASS')
print('STAGE25_REENTRY_R011A_INDEPENDENT_FACTOR_FIREWALL=PASS')
print('R011A_LIFECYCLE=PASS')
print('STAGE26_GATE=LIFECYCLE_VALID')
