#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-04b-bolza-rosati-weierstrass-plane-source-lock.json"
ADAPTER = ROOT / "stages/stage32/residual-32-01-production/post1473-boundary-label-weierstrass-adapter.json"
GATE = ROOT / "stages/stage32-ex3/scratch/ex3-04-common-v4-character-correspondence-gate.json"

art = json.loads(ART.read_text(encoding="utf-8"))
adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
gate = json.loads(GATE.read_text(encoding="utf-8"))

assert art["status"] == "SCRATCH_PROVISIONAL_SOURCE_LOCK_NOT_RETAINED"
assert adapter["canonical_sha256_without_this_field"] == "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
assert gate["diagnostic_verdict"]["EX3_04_common_V4_character_gate_obtained"] is True

# Project cusp binding: ids 1..6 correspond to +1,0,+i,infinity,-i,-1 in the retained adapter.
expected_label_to_id = {33:6,34:6,35:1,36:1,37:5,38:3,39:5,40:3,41:4,42:4,43:2,44:2}
assert {int(k): int(v) for k,v in adapter["boundary_label_to_weierstrass_id"].items()} == expected_label_to_id
assert adapter["cusp_pairs"] == {"Z1":[1,6], "Z2":[3,5], "Z3":[2,4]}

# Hermitian polarization over O=Z[s], s^2=-2.
# Represent a+b*s by (a,b).
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
zero=(0,0); one=(1,0)
M = [[(2,0),(1,1)],[(1,-1),(2,0)]]
Minv = [[(2,0),(-1,-1)],[(-1,1),(2,0)]]
assert M[1][0] == conj(M[0][1])
det = add(mul(M[0][0],M[1][1]), neg(mul(M[0][1],M[1][0])))
assert det == one
for i in range(2):
    for j in range(2):
        v=zero
        for k in range(2): v=add(v,mul(M[i][k],Minv[k][j]))
        assert v == (one if i==j else zero)
# Sylvester criterion for this 2x2 Hermitian form: first principal minor 2>0 and det=1>0.
assert M[0][0] == (2,0) and det == one

# J[2] as even subsets of six Weierstrass points modulo complement.
# The three Beauville pair classes are disjoint pairs covering all six points.
FULL=(1<<6)-1
def mask(pair):
    m=0
    for i in pair: m |= 1 << (i-1)
    return m
pairs=[(1,6),(3,5),(2,4)]
ms=[mask(p) for p in pairs]
assert ms[0] & ms[1] == ms[0] & ms[2] == ms[1] & ms[2] == 0
assert ms[0] ^ ms[1] ^ ms[2] == FULL
# FULL is the zero class modulo complement, hence lambda1+lambda2+lambda3=0.
def canon(m): return min(m, m ^ FULL)
assert canon(ms[0]^ms[1]^ms[2]) == 0
assert len({canon(m) for m in ms}) == 3
# Weil pairing of disjoint pair classes is trivial: intersection cardinality mod 2 is zero.
for i in range(3):
    for j in range(i+1,3):
        assert ((ms[i] & ms[j]).bit_count() % 2) == 0

rem=art["remaining_comparison_gap"]
assert rem["U_source_locked_in_weierstrass_coordinates"] is True
assert rem["Bolza_Rosati_source_locked_in_E2_coordinates"] is True
assert rem["explicit_symplectic_identification_weierstrass_J2_to_E2_mod2_coordinates"] is False
assert art["diagnostic_verdict"]["basis_comparison_gap_open"] is True
assert art["diagnostic_verdict"]["O210_excluded"] is False
assert all(v is False for v in art["firewalls"].values())

print("PASS EX3-04b scratch Bolza Rosati / H4 Weierstrass-plane source-lock")
print("M=[[2,1+s],[1-s,2]], s^2=-2, det(M)=1")
print("U nonzero pair classes: (1,6),(3,5),(2,4); rank 2 Lagrangian")
print("remaining exact gap: symplectic comparison U -> (O/2O)^2 in the chosen E^2 basis")
