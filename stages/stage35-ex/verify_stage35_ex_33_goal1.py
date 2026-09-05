#!/usr/bin/env python3
"""Verify 35EX-33 small goal 1: primitive integral endpoint normalization."""
from __future__ import annotations
import json
from fractions import Fraction
from itertools import permutations, product
from math import gcd, lcm
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-33/primitive-integral-endpoint-normalization.json'

art=json.loads(ART.read_text())
assert art['schema']=='STAGE35_EX_33_PRIMITIVE_INTEGRAL_ENDPOINT_NORMALIZATION_V1'
assert art['stage']=='35-EX'
assert art['unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert art['small_goal']==1
assert art['status']=='PROVISIONAL_EXACT_LEMMA_NO_RECEIVER_CREDIT'
claims=art['statement']['claims']
assert 'Prim(lambda*e)=Prim(e) for every lambda in Q_{>0}' in claims
assert 'the primitive positive integer representative of a positive rational ray is unique' in claims
assert 'Prim is equivariant for permutations of the three edge coordinates' in claims
assert 'rational_square_integrality' in art['proof']
assert art['gaussian_handoff']['legal_next_objects']==['F_AB=A+iB','F_AC=A+iC','F_BC=B+iC']
assert art['gaussian_handoff']['exact_norms_available_next']==[
    'Norm(F_AB)=D_AB^2','Norm(F_AC)=D_AC^2','Norm(F_BC)=D_BC^2'
]
assert len(art['historical_no_recharge_firewall']['forbidden_as_new_credit'])==7
assert 'EQUIVALENT or BLOCKED' in art['historical_no_recharge_firewall']['fail_close']
cf=art['credit_firewall']
assert cf['primitive_integral_normalization_exact'] is True
for key in ('perfect_cuboid_exists','perfect_cuboid_nonexistence_proved','gaussian_compatibility_theorem_proved','E1_proved','R29_PESCH_E1_closed','stage35_closed'):
    assert cf[key] is False, key

def prim(vals: tuple[Fraction,Fraction,Fraction])->tuple[int,int,int]:
    L=lcm(*(x.denominator for x in vals))
    ints=[x.numerator*(L//x.denominator) for x in vals]
    g=gcd(gcd(ints[0],ints[1]),ints[2])
    return tuple(x//g for x in ints)

# Deterministic regression of the exact normalization identities on a bounded rational grid.
vals=sorted({Fraction(n,d) for n in range(1,4) for d in range(1,4)})
scales=vals
for e in product(vals, repeat=3):
    p=prim(e)
    assert gcd(gcd(*p[:2]),p[2])==1
    for lam in scales:
        assert prim(tuple(lam*x for x in e))==p
    for perm in permutations(range(3)):
        ep=tuple(e[i] for i in perm)
        assert prim(ep)==tuple(p[i] for i in perm)

# Rational-square integrality regression: a reduced rational with integral square has denominator 1.
for u in range(0,31):
    for v in range(1,16):
        r=Fraction(u,v)
        if (r*r).denominator==1:
            assert r.denominator==1

print('PASS STAGE35_EX_33_GOAL1_PRIMITIVE_INTEGRAL_ENDPOINT_NORMALIZATION')
