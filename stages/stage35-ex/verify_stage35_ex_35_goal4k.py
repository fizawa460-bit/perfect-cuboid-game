#!/usr/bin/env python3
from __future__ import annotations
import json, math
from fractions import Fraction
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4k-ratio-discriminant-biquartic-quotient-preflight.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
a=json.loads(ART.read_text()); s=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4K_RATIO_DISCRIMINANT_BIQUARTIC_QUOTIENT_PREFLIGHT_V1'
assert a['base_main_sha']==s['base_main_sha']

u,v=sp.symbols('u v', nonzero=True)
U,V,z,H=sp.symbols('U V z H')
t=2*u/(1-u**2)
w=(1+u**2)/(1-u**2)
x=sp.factor(t*(1-v**2)/(1+v**2))
y=sp.factor(t*(2*v)/(1+v**2))
assert sp.factor(x**2+y**2-t**2)==0
assert sp.factor(w**2-1-t**2)==0

D=(1-u**2)*(1+v**2)
Fx=sp.expand(D**2+(2*u*(1-v**2))**2)
Fy=sp.expand(D**2+(4*u*v)**2)
def even_uv_to_UV(expr):
    out=0
    for (eu,ev),coef in sp.Poly(sp.expand(expr),u,v).terms():
        assert eu%2==0 and ev%2==0
        out += coef*U**(eu//2)*V**(ev//2)
    return sp.expand(out)
Fp=sp.factor(even_uv_to_UV(Fx)); Fm=sp.factor(even_uv_to_UV(Fy))
AV=(1+V)**2; BV=V**2-6*V+1
assert sp.factor(Fp-(AV*(U**2+1)+2*BV*U))==0
assert sp.factor(Fm-(AV*(U**2+1)-2*BV*U))==0
assert sp.factor(Fp-Fm-4*BV*U)==0

# Ratio z^2=Fp/Fm gives a reciprocal quadratic for U.
ratio_eq=sp.factor(AV*(z**2-1)*(U**2+1)-2*BV*U*(z**2+1))
L=2*BV*(z**2+1)/(AV*(z**2-1))
assert sp.factor(ratio_eq/(AV*(z**2-1))-(U**2-L*U+1))==0
K2=sp.factor(BV**2*(z**2+1)**2-AV**2*(z**2-1)**2)
P=sp.factor(((V-1)**2-4*V*z**2)*((V-1)**2*z**2-4*V))
assert sp.factor(K2-4*P)==0

quart=sp.Poly(sp.expand(P),z)
disc=sp.factor(sp.discriminant(quart.as_expr(),z))
expected=256*V**2*(V-1)**4*(V+1)**8*(V**2-6*V+1)**4
assert sp.factor(disc-expected)==0
Bpoly=sp.Poly(V**2-6*V+1,V)
assert sp.discriminant(Bpoly.as_expr(),V)==32
assert sp.factor(P.subs(z,1)-BV**2)==0
assert sp.factor(P.subs(z,-1)-BV**2)==0

# Reconstruction from the discriminant quotient: H^2=P makes U solve the reciprocal quadratic.
Urec=(BV*(z**2+1)+2*H)/(AV*(z**2-1))
num=sp.together(Urec**2-L*Urec+1).as_numer_denom()[0]
red=sp.rem(sp.Poly(sp.expand(num),H),sp.Poly(H**2-P,H)).as_expr()
assert sp.factor(red)==0

# Generic (not physical-base) witness that the quotient forgets the common F+/F- squareclass.
def ratsq(q:Fraction)->bool:
    if q<0:return False
    return math.isqrt(q.numerator)**2==q.numerator and math.isqrt(q.denominator)**2==q.denominator
V0=Fraction(3,7); z0=Fraction(-1,2); H0=Fraction(20,49); U0=Fraction(3,5)
A0=(1+V0)**2; B0=V0*V0-6*V0+1
P0=((V0-1)**2-4*V0*z0*z0)*((V0-1)**2*z0*z0-4*V0)
assert H0*H0==P0
Fp0=A0*(U0*U0+1)+2*B0*U0; Fm0=A0*(U0*U0+1)-2*B0*U0
assert Fp0/Fm0==z0*z0
assert not ratsq(Fp0) and not ratsq(Fm0)

assert a['genus_one_receiver']['genus']==1
assert a['genus_one_receiver']['S31_W01_triggered_for_next_adapter'] is True
assert a['converse_boundary']['receiver_is_necessary_for_endpoint'] is True
assert a['converse_boundary']['no_endpoint_equivalence_claim'] is True
assert a['credit_firewall']['new_exact_genus_one_receiver_obtained'] is True
assert a['credit_firewall']['E1_proved'] is False
assert s['schema']=='STAGE35_EX_PESCH_E1_STATE_V48_GOAL4K_RATIO_DISCRIMINANT_GENUS_ONE_QUOTIENT_PENDING_LATER_AUDIT'
assert s['current']['unit']=='35EX-35_GOAL4K_RATIO_DISCRIMINANT_BIQUARTIC_QUOTIENT_PREFLIGHT'
assert s['claims']['goal4k_executed'] is True
assert s['claims']['new_exact_genus_one_receiver_obtained'] is True
assert s['claims']['E1_proved'] is False
print('PASS STAGE35_EX_35_GOAL4K_RATIO_DISCRIMINANT_BIQUARTIC_QUOTIENT_PREFLIGHT_V1')
