#!/usr/bin/env python3
"""Dependency-free exact regression for the Stage33-05 named ell_J2 representative.

We work in Q(sqrt(2))[t,a].  The branch equation is
F=t^2(1-a^2)^2+a^2(1-t^2)^2.
The Stage33-05 normalization map z=z(a) and Hilbert-90 identity imply that
ell_Q is a base-field scalar times a square modulo F.  Since the geometric
Creutz--Viray quotient is L^*/(K^* L^{*2}), this representative is zero there.
"""
from dataclasses import dataclass
from typing import Dict, Tuple
import json, hashlib
from pathlib import Path

Mon = Tuple[int,int]  # (a exponent, t exponent)
Coeff = Tuple[int,int] # x + y*sqrt(2)

@dataclass(frozen=True)
class P:
    d: Dict[Mon,Coeff]
    def __add__(self,o):
        o=toP(o); r=dict(self.d)
        for m,c in o.d.items():
            x,y=r.get(m,(0,0)); u,v=c; q=(x+u,y+v)
            if q==(0,0): r.pop(m,None)
            else: r[m]=q
        return P(r)
    __radd__=__add__
    def __neg__(self): return P({m:(-c[0],-c[1]) for m,c in self.d.items()})
    def __sub__(self,o): return self+(-toP(o))
    def __rsub__(self,o): return toP(o)-self
    def __mul__(self,o):
        o=toP(o); r={}
        for (ai,ti),(x,y) in self.d.items():
            for (aj,tj),(u,v) in o.d.items():
                # (x+y*s)(u+v*s), s^2=2
                c=(x*u+2*y*v,x*v+y*u); m=(ai+aj,ti+tj)
                p,q=r.get(m,(0,0)); r[m]=(p+c[0],q+c[1])
        return P({m:c for m,c in r.items() if c!=(0,0)})
    __rmul__=__mul__
    def __pow__(self,n):
        r=toP(1)
        for _ in range(n): r=r*self
        return r
    def __eq__(self,o): return self.d==toP(o).d

def toP(x):
    if isinstance(x,P): return x
    return P({(0,0):(int(x),0)}) if x else P({})

a=P({(1,0):(1,0)}); t=P({(0,1):(1,0)}); s=P({(0,0):(0,1)})
one=toP(1)
q=t**4-6*t**2+one
Dp=t**2-2*t-one
F=t**2*(one-a**2)**2 + a**2*(one-t**2)**2

znum=2*t**2*(one-a**2)-(one-t**2)**2
zden=one-t**2
assert znum**2-q*zden**2 == 4*t**2*F

# f2=(t+1+s)/(t-1+s), g=(znum+(t-r3)(t-r4)zden)/znum
# with r3=s-1 and r4=1-s.
f2num=t+one+s
f2den=t-one+s
gnum=znum + (t-(s-one))*(t-(one-s))*zden
gden=znum
ellnum=4*(a**2*t**2+t**4-4*t**2+2)
ellden=(t**2-one)*Dp
cleared=ellnum*f2den*gden**2 - f2num*gnum**2*ellden
Q=4*t**2*(
    4*a**2*t**3-4*a**2*t**2+4*s*a**2*t**2
    +3*t**5-3*t**4+3*s*t**4-12*t**3+2*s*t**3
    -14*s*t**2+16*t**2-2*s*t+5*t-9+7*s
)
assert cleared == F*Q

cert={
  "schema":"STAGE33_12_J2_CV_LCLASS_ZERO_REGRESSION_V1",
  "status":"PASS_EXACT_UPSTREAM_REPRESENTATIVE_CONTRADICTION",
  "source_lock":{
    "stage33_05_script":"stages/stage33/33-05/j2_arithmetic_descent.py",
    "stage33_05_blob_sha1":"a63be5592c793c3812da99275478f14dd0d2687b",
    "creutz_viray_surfaces":"arXiv:1306.3251v3, Section 2.3 / Theorem 2.5 / Corollary 5.4",
    "creutz_viray_curves":"arXiv:1403.2924, Lemma 4.6 / Proposition 5.1"
  },
  "branch_equation":"F=t^2*(1-a^2)^2+a^2*(1-t^2)^2",
  "normalization_map":"z=(2*t^2*(1-a^2)-(1-t^2)^2)/(1-t^2)",
  "normalization_identity":"znum^2-q*zden^2=4*t^2*F",
  "hilbert90_scalar":"f2=(t+1+sqrt(2))/(t-1+sqrt(2)) in Qbar(t)^*",
  "cleared_hilbert90_identity_verified_mod_F":True,
  "consequence":"ell_Q=f2*g^2 in Qbar(t)[a]/(F), hence [ell_Q]=0 in Lbar^*/(Kbar^* Lbar^{*2})",
  "stage33_05_named_representative_geometric_nontriviality_supported":False,
  "stage33_05_named_representative_credit":"REVOKED_PENDING_REPAIR",
  "batch3_live_class2_routes_zero_supported":False,
  "class2_no_go":"REVOKED_BY_HOSTILE_AUDIT",
  "class3_promotion_allowed":False,
  "next_exact_leaf":"REPAIR_OR_REPLACE_THE_STAGE33_05_NAMED_J2_CV_REPRESENTATIVE_THEN_COMPUTE_CREUTZ_VIRAY_LEMMA_4_6_E2_COCYCLE",
  "stage33_12_closed_exact":False,
  "stage33_13_released":False,
  "theorem_credit":False,
  "receiver_credit":False,
  "endpoint_credit":False,
  "perfect_cuboid_existence_claim":False,
  "perfect_cuboid_nonexistence_claim":False
}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest()
path=Path(__file__).with_name("j2-cv-lclass-zero-regression.json")
path.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(cert,indent=2,sort_keys=True))
