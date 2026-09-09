#!/usr/bin/env python3
import json
import subprocess
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DR/fixed-p2-v4-elliptic-quotient-proselmer-reduction-preflight.json'
SOURCE=ROOT/'stages/stage36/36-09DR/v4-elliptic-quotient-isogeny-source-lock.md'
DQ=ROOT/'stages/stage36/36-09DQ/fixed-p2-global-2primary-adelic-annihilator-preflight.json'

def git_hash(p):
    return subprocess.check_output(['git','hash-object',str(p)],text=True,cwd=ROOT).strip()

def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

assert git_hash(CERT)=='c212f0430fb5b4d04ee0887e303a73fb303657c8'
assert git_hash(SOURCE)=='e546e1a731dfd6b270641eb1adb026847f8b838e'
assert git_hash(DQ)=='4c41228d23f9088bfbea8b68c94b2a26948f8691'
c=json.loads(CERT.read_text())
dq=json.loads(DQ.read_text())
assert c['schema']=='STAGE36_36_09DR_FIXED_P2_V4_ELLIPTIC_QUOTIENT_PROSELMER_REDUCTION_PREFLIGHT_V1'
assert c['status']=='PASS_EXPLICIT_Q_V4_ELLIPTIC_QUOTIENT_ISOGENY_PROSELMER_2PRIMARY_TRANSPORT_MISSING'
assert c['batch_parent']['36_09DQ_exact_green_head']=='b121fc0f23eba3241f35cf64a13d45cba7eaa213'
assert c['batch_parent']['36_09DQ_exact_head_ci']=='34231468694/102078401099'
assert c['batch_parent']['36_09DQ_promotion_replay_head']=='befe11f72c3bc6f228ac02299f4d370ec600baa2'
assert c['batch_parent']['36_09DQ_promotion_replay_ci']=='34231707077/102079208526'
assert dq['adelic_tate_map']['kernel']=='image(T_2 Sel(J))'
assert dq['scope_firewalls']['retained_open_curve_proSelmer_intersection_computed'] is False

# Expand the four quadratic factors exactly, ascending powers of t.
f=[F(1)]
for q in [F(4),F(1,4),F(9),F(1,9)]:
    f=pmul(f,[q,F(0),F(1)])
expected=[F(1),F(0),F(481,36),F(0),F(733,18),F(0),F(481,36),F(0),F(1)]
assert f==expected
# Even reciprocal polynomial verifies tau and reciprocal sigma/rho preserve C.
assert f==list(reversed(f))
assert all(f[i]==0 for i in [1,3,5,7])

A=F(481,36); B=F(733,18)
# sigma: u=t+1/t, Y=z/t^2.
sigma_u2=-4+A
sigma_c=2-2*A+B
assert sigma_u2==F(337,36) and sigma_c==F(16)
assert F(9,4)+F(64,9)==sigma_u2
assert F(9,4)*F(64,9)==sigma_c
# rho: v=t-1/t, Y=z/t^2.
rho_v2=4+A
rho_c=2+2*A+B
assert rho_v2==F(625,36) and rho_c==F(625,9)
assert F(25,4)+F(100,9)==rho_v2
assert F(25,4)*F(100,9)==rho_c
# Full V4 quotient s=t^2+t^-2.
assert -2+B==F(697,18)

# Rational points on the three genus-one quotients and the genus-zero total quotient.
def eval_even_quartic(x,a,b): return x**4+a*x**2+b
assert F(25,3)**2 == eval_even_quartic(F(2),F(337,36),F(16))
assert F(25,3)**2 == eval_even_quartic(F(0),F(625,36),F(625,9))
assert F(25,3)**2 == F(2)**2 + A*F(2) + F(697,18)
assert f[0]==1  # E_tau point (x,y)=(0,1).

# Pullback differential directions in basis (dt/z, t dt/z, t^2 dt/z).
M=[[0,1,0],[-1,0,1],[1,0,1]]
det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
     -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
     +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
assert det==2
assert c['differential_check']['determinant']==2
assert c['isogeny_result']['Q_isogeny_constructed'] is True
assert c['isogeny_result']['proSelmer_product_identification_obtained'] is False
assert c['isogeny_result']['isogeny_2primary_kernel_cokernel_computed'] is False
assert c['route_result']['next_leaf']=='36-09DS_FIXED_P2_ELLIPTIC_QUOTIENT_2PRIMARY_ISOGENY_TRANSPORT_PREFLIGHT'
for k in ['global_2primary_Brauer_set_nonempty','global_2primary_Brauer_set_empty','Brauer_Manin_obstruction_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_nonexistence_claim']:
    assert c['scope_firewalls'][k] is False,k
print('36-09DR verified: explicit Q-V4 action, three genus-one quotients, genus-zero total quotient, and full-rank differential Q-isogeny. 2-primary isogeny transport and all downstream credit remain closed.')
