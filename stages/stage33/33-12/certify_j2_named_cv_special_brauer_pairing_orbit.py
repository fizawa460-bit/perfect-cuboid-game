#!/usr/bin/env python3
"""Deterministic verifier for the Stage33-12 named-CV pairing-orbit adapter."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "j2-named-cv-special-brauer-pairing-orbit.json"
d = json.loads(CERT.read_text(encoding="utf-8"))
assert d["schema"] == "STAGE33_12_J2_NAMED_CV_SPECIAL_BRAUER_PAIRING_ORBIT_V1"
assert d["status"] == "PASS_EXACT_NAMED_CV_PAIRING_ORBIT_SELECTED_NOT_MARKED_COORDINATE"
assert d["class2_budget_batch"] == 2

s2 = sp.sqrt(2)
i = sp.I

# Exact E:y^2=x^3-x group law.
def simp(x):
    return sp.simplify(sp.expand(x))

def neg(P):
    return None if P is None else (P[0], -P[1])

def add(P,Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1,y1=P; x2,y2=Q
    if simp(x1-x2) == 0:
        if simp(y1+y2) == 0:
            return None
        m=simp((3*x1**2-1)/(2*y1))
    else:
        m=simp((y2-y1)/(x2-x1))
    x3=simp(m**2-x1-x2)
    y3=simp(m*(x1-x3)-y1)
    return (x3,y3)

def same(P,Q):
    if P is None or Q is None:
        return P is None and Q is None
    return simp(P[0]-Q[0]) == 0 and simp(P[1]-Q[1]) == 0

def onE(P):
    return P is None or simp(P[1]**2-(P[0]**3-P[0])) == 0

J1=(sp.Integer(0),sp.Integer(0))
J2=(sp.Integer(1),sp.Integer(0))
J12=(sp.Integer(-1),sp.Integer(0))
P1=(-1-s2,-i*(2+s2))
P3=(1-s2,2-s2)
P5=(1+s2,-2-s2)
P7=(-1+s2,i*(2-s2))
for P in (J1,J2,J12,P1,P3,P5,P7):
    assert onE(P)

assert same(add(P3,neg(P5)),J12)
assert same(add(P3,P5),J1)
assert same(add(P1,neg(P7)),J2)
assert same(add(P1,P7),J1)

# Standard symplectic Weil pairing on E[2]. Coordinates are abstract F2
# coordinates J1=(1,0), J2=(0,1), J12=(1,1). Return +1/-1.
coords={"0":(0,0),"J1":(1,0),"J2":(0,1),"J1+J2":(1,1)}
def e2(a,b):
    x1,x2=coords[a]; y1,y2=coords[b]
    exponent=(x1*y2-x2*y1) & 1
    return -1 if exponent else 1

assert e2("J2","J1+J2") == -1
assert e2("J2","J2") == 1
selected=[1 if e2("J2","J1+J2")==-1 else 0,
          1 if e2("J2","J2")==-1 else 0]
assert selected == [1,0]
assert d["weil_pairing_evaluation"]["selected_orbit_invariant"] == selected
assert d["weil_pairing_evaluation"]["selected_raw_orbit_members"] == ["0100","0111","1000","1011"]

# Full four-class character table against D_L=J12, D_R=J2.
table={}
for T in ("0","J1","J2","J1+J2"):
    table[T]=[
        1 if e2(T,"J1+J2")==-1 else 0,
        1 if e2(T,"J2")==-1 else 0,
    ]
assert table == {"0":[0,0],"J1":[1,1],"J2":[1,0],"J1+J2":[0,1]}
assert d["complete_four_class_regression"]["0"] == [0,0]
assert d["complete_four_class_regression"]["J1"] == [1,1]
assert d["complete_four_class_regression"]["J2"] == [1,0]
assert d["complete_four_class_regression"]["J1+J2"] == [0,1]
assert len({tuple(v) for v in table.values()}) == 4

fw=d["firewalls"]
assert fw["named_cv_j2_pairing_orbit_selected"] is True
assert fw["selected_pairing_orbit"] == [1,0]
assert fw["pairing_orbit_bits_equal_marked_brauer_bits"] is False
assert fw["j2_marked_coordinate_selected"] is False
assert fw["stage33_12_closed_exact"] is False
assert fw["stage33_13_released"] is False
assert fw["theorem_credit"] is False
assert fw["receiver_credit"] is False
assert fw["endpoint_credit"] is False
assert fw["perfect_cuboid_existence_claim"] is False
assert fw["perfect_cuboid_nonexistence_claim"] is False

print(json.dumps({
    "success": True,
    "named_cv_j2": "J2=(1,0) on E:y^2=x^3-x",
    "D_L": "J1+J2",
    "D_R": "J2",
    "selected_pairing_orbit": selected,
    "marked_brauer_coordinate_selected": False,
    "next_exact_leaf": d["next_exact_leaf"],
}, indent=2, sort_keys=True))
