#!/usr/bin/env python3
import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
O="stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json"
EJ="stages/stage36/36-09EJ/bounded-rho-sel2-exact-computation-preflight.json"
SOURCE="stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-source-lock.md"
CERT="stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-preflight.json"

def blob(p): return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p): return json.loads((ROOT/p).read_text())
expected={
 O:"6a2678ebedba40e13277100441361039ee47ca28",
 EJ:"7ff288962132cae21f30a3c7b05ee1e5b5680c91",
 SOURCE:"ea2dfd429fb9e10f067bf998ac31510287afa5dc",
 CERT:"f6af11a0f7fd8a303531b2a587b7446c382a84c5",
}
for p,s in expected.items(): assert blob(p)==s,(p,blob(p),s)
o=load(O); ej=load(EJ); c=load(CERT)
assert o['top_genus3_exact_factorization']['normalized_model']=='C3_p: y^2=(t^2+p^2)*(t^2+p^(-2))*(t^2+c^2)*(t^2+c^(-2))'
assert o['notation_separation']['physical_base_quantities']['c']=='(p+1)/(p-1)'
assert ej['criterion_consumption']['expanded_fixed_parameter_registry_count']==14
assert ej['criterion_consumption']['new_parameter_outside_EG_orbit_excluded'] is True

def cf(p): return (p+1)/(p-1)
def orbit(p):
    cp=cf(p)
    return sorted({abs(p),abs(1/p),abs(cp),abs(1/cp)})

def coeffs(p):
    cp=cf(p)
    return sorted([p*p,1/(p*p),cp*cp,1/(cp*cp)])

seeds=[Fraction(2),Fraction(1,5),Fraction(2,7),Fraction(2,9)]
expected_orbits=[
 [Fraction(1,3),Fraction(1,2),Fraction(2),Fraction(3)],
 [Fraction(1,5),Fraction(2,3),Fraction(3,2),Fraction(5)],
 [Fraction(2,7),Fraction(5,9),Fraction(9,5),Fraction(7,2)],
 [Fraction(2,9),Fraction(7,11),Fraction(11,7),Fraction(9,2)],
]
for p,exp in zip(seeds,expected_orbits):
    got=orbit(p); assert got==exp,(p,got,exp)
    base=coeffs(p)
    for q in got: assert coeffs(q)==base,(p,q)
    assert cf(1/p)==-cf(p)
    assert cf(cf(p))==p

old={Fraction(s) for s in ej['criterion_consumption']['expanded_fixed_parameter_registry']}
union=set()
for p in seeds: union.update(orbit(p))
assert len(old)==14
assert union-old=={Fraction(7,11),Fraction(11,7)}
assert len(union)==16
inc=sorted(union)
assert [str(x) for x in inc]==c['receiver_consequence']['expanded_registry_increasing']
assert c['receiver_consequence']['new_excluded_parameters']==['7/11','11/7']
assert c['receiver_consequence']['expanded_registry_count']==16
assert c['receiver_consequence']['new_fixed_parameter_receiver_sectors_empty'] is True
assert c['literal_orbit_theorem']['positive_literal_orbit_complete'] is True
for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
print('36-09EK verified: the 14 exact EJ exclusions close under literal C3 orbit to 16 values, adding exactly 7/11 and 11/7; no exhaustive-ledger/full-receiver/endpoint credit.')
