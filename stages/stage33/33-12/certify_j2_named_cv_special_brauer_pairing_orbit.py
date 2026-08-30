#!/usr/bin/env python3
"""Dependency-free exact verifier for the Stage33-12 named-CV pairing orbit."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "j2-named-cv-special-brauer-pairing-orbit.json"
d = json.loads(CERT.read_text(encoding="utf-8"))
assert d["schema"] == "STAGE33_12_J2_NAMED_CV_SPECIAL_BRAUER_PAIRING_ORBIT_V1"
assert d["status"] == "PASS_EXACT_NAMED_CV_PAIRING_ORBIT_SELECTED_NOT_MARKED_COORDINATE"
assert d["class2_budget_batch"] == 2

# K = Q(sqrt(2), i), represented as
# a + b*r + i*(c + d*r), r^2=2.
def q2_add(x,y): return (x[0]+y[0], x[1]+y[1])
def q2_neg(x): return (-x[0],-x[1])
def q2_mul(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def q2_inv(x):
    den=x[0]*x[0]-2*x[1]*x[1]
    assert den != 0
    return (x[0]/den,-x[1]/den)

def K(a=0,b=0,c=0,e=0): return (F(a),F(b),F(c),F(e))
def kadd(x,y): return tuple(x[j]+y[j] for j in range(4))
def kneg(x): return tuple(-u for u in x)
def ksub(x,y): return kadd(x,kneg(y))
def kmul(x,y):
    u=(x[0],x[1]); v=(x[2],x[3])
    p=(y[0],y[1]); q=(y[2],y[3])
    re=q2_add(q2_mul(u,p),q2_neg(q2_mul(v,q)))
    im=q2_add(q2_mul(u,q),q2_mul(v,p))
    return (re[0],re[1],im[0],im[1])
def kinv(x):
    u=(x[0],x[1]); v=(x[2],x[3])
    den=q2_add(q2_mul(u,u),q2_mul(v,v))
    dinv=q2_inv(den)
    re=q2_mul(u,dinv); im=q2_mul(q2_neg(v),dinv)
    return (re[0],re[1],im[0],im[1])
def kdiv(x,y): return kmul(x,kinv(y))
def keq(x,y): return x==y
def kzero(x): return x==K()
def kpow(x,n):
    out=K(1); base=x
    while n:
        if n&1: out=kmul(out,base)
        base=kmul(base,base); n//=2
    return out

def scale(n,x): return tuple(F(n)*u for u in x)

ZERO=K(); ONE=K(1); MINUS_ONE=K(-1)
R=K(0,1); I=K(0,0,1,0)

def negP(P): return None if P is None else (P[0],kneg(P[1]))
def onE(P):
    if P is None: return True
    x,y=P
    return kzero(ksub(kpow(y,2),ksub(kpow(x,3),x)))
def addP(P,Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if keq(x1,x2):
        if kzero(kadd(y1,y2)): return None
        m=kdiv(ksub(scale(3,kpow(x1,2)),ONE),scale(2,y1))
    else:
        m=kdiv(ksub(y2,y1),ksub(x2,x1))
    x3=ksub(ksub(kpow(m,2),x1),x2)
    y3=ksub(kmul(m,ksub(x1,x3)),y1)
    return (x3,y3)
def sameP(P,Q):
    if P is None or Q is None: return P is None and Q is None
    return keq(P[0],Q[0]) and keq(P[1],Q[1])

J1=(ZERO,ZERO)
J2=(ONE,ZERO)
J12=(MINUS_ONE,ZERO)
P1=(kneg(kadd(ONE,R)), kneg(kmul(I,kadd(K(2),R))))
P3=(ksub(ONE,R), ksub(K(2),R))
P5=(kadd(ONE,R), kneg(kadd(K(2),R)))
P7=(ksub(R,ONE), kmul(I,ksub(K(2),R)))
for P in (J1,J2,J12,P1,P3,P5,P7):
    assert onE(P)

# Exact contact-cycle identities.
assert sameP(addP(P3,negP(P5)),J12)
assert sameP(addP(P3,P5),J1)
assert sameP(addP(P1,negP(P7)),J2)
assert sameP(addP(P1,P7),J1)

# Standard symplectic Weil pairing on E[2].
coords={"0":(0,0),"J1":(1,0),"J2":(0,1),"J1+J2":(1,1)}
def e2(a,b):
    x1,x2=coords[a]; y1,y2=coords[b]
    return -1 if ((x1*y2-x2*y1)&1) else 1

selected=[1 if e2("J2","J1+J2")==-1 else 0,
          1 if e2("J2","J2")==-1 else 0]
assert selected == [1,0]
assert d["weil_pairing_evaluation"]["selected_orbit_invariant"] == selected
assert d["weil_pairing_evaluation"]["selected_raw_orbit_members"] == ["0100","0111","1000","1011"]

table={T:[1 if e2(T,"J1+J2")==-1 else 0,
          1 if e2(T,"J2")==-1 else 0]
       for T in ("0","J1","J2","J1+J2")}
assert table == {"0":[0,0],"J1":[1,1],"J2":[1,0],"J1+J2":[0,1]}
for key,value in table.items():
    assert d["complete_four_class_regression"][key] == value
assert len({tuple(v) for v in table.values()}) == 4

fw=d["firewalls"]
assert fw["named_cv_j2_pairing_orbit_selected"] is True
assert fw["selected_pairing_orbit"] == [1,0]
for key in [
    "pairing_orbit_bits_equal_marked_brauer_bits",
    "j2_marked_coordinate_selected",
    "j2_twisted_transcendental_kernel_identified",
    "j2_explicit_torsor_surface_materialized",
    "stage33_12_closed_exact",
    "stage33_13_released",
    "heavy_actions_authorized",
    "theorem_credit",
    "receiver_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False

print(json.dumps({
    "success":True,
    "D_L":"J1+J2",
    "D_R":"J2",
    "selected_pairing_orbit":selected,
    "marked_brauer_coordinate_selected":False,
    "next_exact_leaf":d["next_exact_leaf"],
},indent=2,sort_keys=True))
