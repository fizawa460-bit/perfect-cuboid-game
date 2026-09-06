#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4l-stage14-pythagorean-elliptic-rankjump-receiver.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
a=json.loads(ART.read_text()); s=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4L_STAGE14_PYTHAGOREAN_ELLIPTIC_RANKJUMP_RECEIVER_V1'
assert a['base_main_sha']==s['base_main_sha']

def git_blob_sha(path:Path)->str:
    b=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert git_blob_sha(ROOT/'docs/arsenal/cards/formal/S31-W01.md')=='122a6c1c5c871c1c7b797017e854de8ec55e7c50'
assert git_blob_sha(ROOT/'stages/stage14/archive/stage14-4af-specialization-triple.md')=='f14d6840d10aaa36df63b2d4a70a07d509b596ce'

p,z,eta,X,Y=sp.symbols('p z eta X Y', nonzero=True)
q=sp.factor((p**2-1)/(2*p)); h=sp.factor((p**2+1)/(2*p)); c=sp.factor((p**2-1)/(2*p**2))
u14=sp.factor((p-1)/(p+1))
assert sp.factor(1+q**2-h**2)==0
assert sp.factor(q-2*u14/(1-u14**2))==0
quart=sp.factor((p**2-z**2)*(z**2-p**-2))
Xf=sp.factor(c*(z-p)/(z+1/p))
Yf=sp.factor((p**4-1)/(4*p**3)*eta/(z+1/p)**2)
err=sp.together(Yf**2-Xf*(Xf-1)*(Xf+q**2)).as_numer_denom()[0]
red=sp.rem(sp.Poly(sp.expand(err),eta),sp.Poly(eta**2-quart,eta)).as_expr()
assert sp.factor(red)==0
zinv=sp.factor(-(X+(p**2-1)/2)/(p*(X-c)))
assert sp.factor(zinv.subs(X,Xf)-z)==0
etainv=sp.factor(Y*(zinv+1/p)**2*4*p**3/(p**4-1))
# round-trip eta on elliptic image
assert sp.factor(etainv.subs({X:Xf,Y:Yf})-eta)==0

# Exact exceptional branch correspondence.
assert sp.factor(Xf.subs(z,p))==0
assert sp.factor(Xf.subs(z,-p)-1)==0
assert sp.factor(Xf.subs(z,1/p)+q**2)==0
# z=-1/p is the sole affine denominator pole and is assigned to O.
rhs_c=sp.factor(c*(c-1)*(c+q**2))
neg_square=-((p**2-1)*(p**2+1)/(4*p**3))**2
assert sp.factor(rhs_c-neg_square)==0
# Hence X=c has no rational E-point for rational retained p (negative nonzero square).

# Goal4K ratio quadratic: branch squares force U=+/-1.
v,zz=sp.symbols('v zz', nonzero=True)
V=v**2; AV=(1+V)**2; BV=V**2-6*V+1
pv=sp.factor((V-1)/(2*v))
L=sp.factor(2*BV*(zz+1)/(AV*(zz-1)))
assert sp.factor(L.subs(zz,pv**2)-2)==0
assert sp.factor(L.subs(zz,pv**-2)+2)==0
# Order-4 x coordinates map exactly to z=+/-1.
z_of_X=sp.factor(-(X+(p**2-1)/2)/(p*(X-c)))
assert sp.factor(z_of_X.subs(X,1-h)-1)==0
assert sp.factor(z_of_X.subs(X,1+h)+1)==0

# Semantic source-lock assertions: only exact reusable Stage14 conclusions are consumed.
st14=(ROOT/'stages/stage14/archive/stage14-4af-specialization-triple.md').read_text()
for needle in ['PYTHAGOREAN_BASE_GENERIC_MW_RANK=0','TORSION_EXACT_Z2xZ4_ON_GENUINE_BASES=true','PYTHAGOREAN_BASE_FIBERS=I4_X6']:
    assert needle in st14
assert a['torsion_exclusion_on_physical_endpoint']['conclusion']=='every physical endpoint maps to a non-torsion E_q(Q) point'
assert a['rank_jump_receiver']['stage14_generic_geometric_rank']==0
assert a['rank_jump_receiver']['new_receiver_obtained'] is True
assert a['credit_boundary']['uniform_rank_jump_exclusion_obtained'] is False
assert a['credit_boundary']['E1_proved'] is False
assert s['schema']=='STAGE35_EX_PESCH_E1_STATE_V49_GOAL4L_STAGE14_PYTHAGOREAN_ELLIPTIC_RANKJUMP_RECEIVER_PENDING_LATER_AUDIT'
assert s['claims']['goal4l_executed'] is True
assert s['claims']['physical_endpoint_implies_positive_rank_specialization'] is True
assert s['claims']['E1_proved'] is False and s['claims']['stage35_closed'] is False
print('PASS STAGE35_EX_35_GOAL4L_STAGE14_PYTHAGOREAN_ELLIPTIC_RANKJUMP_RECEIVER_V1')
