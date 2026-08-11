#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-s7-62/result.md': ['RANGE_STABLE_ARITHMETIC_SATURATION_FORCES_COLLISION_ENERGY=true','FORCED_COLLISION_ENERGY_EXPONENT=1'],
    'stages/stage14/14-Work-biX21/result.md': ['GLOBAL_RANGE_STABLE_HEAVY_MOVER_PRIME_PROVED=true','GLOBAL_HEAVY_MOVER_STATE_MASS_EXPONENT=1/2'],
    'stages/stage14/14-4dv/result.md': ['FIXED_PRIME_PLUS_PLUS_COLLISION_EQUATION_TAUTOLOGICAL=true'],
    'stages/stage14/14-4dw/result.md': ['SQRT_OBSTRUCTION_REDUCED_TO_FIXED_PRIME_PRIMITIVE_DIVISOR_PAIR_PHYSICAL_MASK_MASS=true'],
}
for rel, needles in locks.items():
    text=(ROOT/rel).read_text()
    for needle in needles:
        assert needle in text, (rel,needle)

for D,A in [(5,2),(13,8),(35,14),(77,33),(221,85)]:
    g=gcd(D-A,D+A)
    assert (2*gcd(D,A)) % g == 0

def prim(a,b):
    g=gcd(a,b)
    return (a//g,b//g)
for v1,v2 in [((6,15),(10,25)),((14,21),(22,33)),((9,24),(15,40))]:
    assert v1[0]*v2[1] == v2[0]*v1[1]
    assert prim(*v1) == prim(*v2)

ell=5
states=[(1,3),(3,1),(1,7),(7,1)]
for r1,s1 in states:
    n1=r1*r1+s1*s1
    assert n1%(2*ell)==0
    x1=n1//(2*ell)
    for r2,s2 in states:
        n2=r2*r2+s2*s2
        assert n2%(2*ell)==0
        x2=n2//(2*ell)
        delta=r1*s2-r2*s1
        sigma=r1*r2+s1*s2
        assert n1*n2 == delta*delta+sigma*sigma
        assert delta*delta+sigma*sigma == 4*ell*ell*x1*x2
        assert x2*n1 == x1*n2 == 2*ell*x1*x2

ell=5; rho=2
v1=(2,1); v2=(7,1); v3=(3,1)
assert (rho*rho+1)%ell==0
for r,s in (v1,v2): assert (r-rho*s)%ell==0
delta=v1[0]*v2[1]-v2[0]*v1[1]
sigma=v1[0]*v2[0]+v1[1]*v2[1]
assert delta%ell==0 and sigma%ell==0
assert (v3[0]+rho*v3[1])%ell==0
delta=v1[0]*v3[1]-v3[0]*v1[1]
sigma=v1[0]*v3[0]+v1[1]*v3[1]
assert delta%ell!=0 and sigma%ell!=0

res=(ROOT/'stages/stage14/14-s7-63/result.md').read_text()
for needle in [
    'STAGE14_S7_63=COMPLETE_PROPORTIONAL_COLLISION_ENERGY_PEEL_ON_PRIMITIVE_DIVISOR_PAIR_MASS',
    'MERGED_4DW_PRIMITIVE_DIVISOR_PAIR_REDUCTION_IMPORTED=true',
    'PROPORTIONAL_COLLISION_ENERGY_UPPER_EXPONENT=1/2',
    'NONPROPORTIONAL_COLLISION_ENERGY_LOWER_EXPONENT=1',
    'NONPROPORTIONAL_COLLISION_PAIR_ADDS_FRESH_CODIMENSION=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'S7_63_NEW_AUXILIARY_H_NEEDED=false',
    'NEXT=Stage14-s7-64',
]: assert needle in res, needle

print({'stage':'14-s7-63','prop_energy_upper':'1/2','nonprop_energy_lower':'1','fresh_pair_codimension':False,'current_exponent':'1/2','next':'Stage14-s7-64'})
