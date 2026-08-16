#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
def text(rel):
    p=ROOT/rel; assert p.exists(),rel; return p.read_text(encoding='utf-8')
def data(rel): return json.loads(text(rel))

def add(a,b):
    n=max(len(a),len(b)); o=[Fraction(0)]*n
    for i,v in enumerate(a): o[i]+=v
    for i,v in enumerate(b): o[i]+=v
    while len(o)>1 and o[-1]==0:o.pop()
    return o
def scale(a,s): return [v*s for v in a]
def mul(a,b):
    o=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    while len(o)>1 and o[-1]==0:o.pop()
    return o
def pw(a,n):
    o=[Fraction(1)]
    for _ in range(n):o=mul(o,a)
    return o
def ev(a,x):
    o=Fraction(0)
    for c in reversed(a):o=o*x+c
    return o

reg=data('stages/stage25/25-reentry-20/directional-registry.json')
ctrl=data('stages/stage25/25-reentry-controller.json')
r501=text('stages/stage25/25-50/r501-parametric-positive-power.md')
r502=text('stages/stage25/25-60/r502-primitive-height-no-upgrade.md')
r502a=text('stages/stage25/25-60/audit-recheck.md')
st24=text('stages/stage24/final.md')
a10=text('stages/stage25/25-reentry-10/audit.md')
a20=text('stages/stage25/25-reentry-20/audit.md')
proof=text('stages/stage25/25-reentry-20/directional-quarter-power.md')

assert reg['task_id']=='Stage25-u24-r002a' and reg['phase']==20
assert reg['authorization']['phase10_pr']==1002
assert reg['authorization']['phase10_merge_commit']=='5cb7dc8792faf575c1e21fce8166f094af6d7b14'
assert 'AUDIT_VERDICT=PASS' in a10 and 'AUDIT_VERDICT=PASS' in a20

# Exact R501 a-cone algebra remains independently machine-checked.
t=[Fraction(0),Fraction(1)]; t2=pw(t,2); t4=pw(t,4)
A=scale(mul(t2,add(t4,[Fraction(-9)])),16)
f=add(t4,add(scale(t2,-10),[Fraction(9)])); g=add(t4,add(scale(t2,2),[Fraction(9)]))
B=mul(f,g); C=scale(mul(mul(t,add(t2,[Fraction(3)])),f),4)
Q1=[Fraction(9),-12,2,-4,1]; Q2=[Fraction(9),12,-10,-4,1]
prod=[Fraction(1)]
for r in (3,1,-1,-3):prod=mul(prod,[Fraction(-r),Fraction(1)])
assert add(B,scale(C,-1))==mul(prod,Q1)
assert add(A,scale(C,-1))==scale(mul(mul(t,add(t2,[Fraction(3)])),Q2),-4)
x0=Fraction(9,2)
assert ev(Q1,x0)==Fraction(657,16)
assert ev(Q2,Fraction(5))==Fraction(-56)
H=[Fraction(3),-5,-3,1]; Hp=[Fraction(-5),-6,3]
assert ev(H,x0)>0 and ev(Hp,x0)>0

for marker in (r'A^2+C^2=D_{AC}^2',r'B^2+C^2=D_{BC}^2',r'N_2(B)\gg B^{1/4}','PARAMETER_FIBER_BOUND=8','THIRD_FACE_EXCEPTION_CURVE_GENUS=7'):
    assert marker in r501,marker
assert '0<A<B<C' in r502
assert 'R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))' in r502
assert 'R502_EXACT_FAMILY_GROWTH_ACCEPTED=Theta(B^(1/4))' in r502a
assert 'DIRECTIONAL_THEOREM=M2,j(B)~C_j B(log B)^5 for j=a,b,c with C_j>0' in st24

d=reg['directional_families']; assert set(d)=={'a','b','c'}
assert d['a']['cone']=='9/2<t<5' and d['a']['canonical_shared_edge']=='a'
assert d['b']['canonical_shared_edge']=='b' and d['c']['canonical_shared_edge']=='c'
assert reg['global_surface']['global_exponent_upgraded'] is False
assert reg['scope_firewall']['true_N2_exponent_identified'] is False

p20=ctrl['phase20_submission']
assert p20['audit_status']=='PASS' and p20['stronger_result_proved'] is True
assert p20['new_reusable_weapon_proved'] is True
assert p20['accepted_theorem']=='N2,j(B)>>_j B^(1/4) for j=a,b,c'
assert p20['pr']==1003 and p20['merge_commit']=='1d88e8e3254a383620e221df8a1a1039ebeabcd4'
assert ctrl['phases']['10']['status']=='AUDITED_PASS_MERGED'
assert ctrl['stage26_gate']['stage26_allowed'] is False

if ctrl['current_phase']==20:
    assert ctrl['status'].startswith('PHASE20_')
else:
    assert ctrl['current_phase'] in (30,40,50,60,70)
    r8=ctrl['r008a_submission']
    assert r8['audit_status']=='PASS' and r8['status']=='AUDITED_PASS_MERGED'
    assert r8['merge_commit']=='11075adf8e30c73e5058790ee6ed6e2a9b6c9e2b'
    assert not any(x['route_id']=='Stage25-um-r008a' and x['blocks_next_phase'] for x in ctrl['propagation_queue'])

for marker in ('ALL_SHARED_EDGE_DIRECTIONS_POSITIVE_POWER=true','GLOBAL_N2_EXPONENT_UPGRADED=false','TRUE_N2_EXPONENT_IDENTIFIED=false','PERFECT_CUBOID_CONCLUSION=NONE'):
    assert marker in proof,marker

print('STAGE25_REENTRY_PHASE20_AUTHORIZATION=PASS')
print('STAGE25_REENTRY_PHASE20_R501_A_CONE_ALGEBRA=PASS')
print('STAGE25_REENTRY_PHASE20_R501_R502_SOURCE_BINDING=PASS')
print('STAGE25_REENTRY_PHASE20_DIRECTIONAL_ADAPTER=PASS')
print('STAGE25_REENTRY_PHASE20_POST_PHASE_LIFECYCLE=PASS')
print('STAGE26_GATE=BLOCKED_VALID')
