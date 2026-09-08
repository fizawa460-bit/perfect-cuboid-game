#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-04c-bolza-unique-h4-plane-coordinate-lock.json"
PREV = ROOT / "stages/stage32-ex3/scratch/ex3-04b-bolza-rosati-weierstrass-plane-source-lock.json"

art = json.loads(ART.read_text(encoding="utf-8"))
prev = json.loads(PREV.read_text(encoding="utf-8"))
assert art["status"] == "SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED"
assert prev["H4_character_plane_in_weierstrass_coordinates"]["rank_F2"] == 2
assert prev["H4_character_plane_in_weierstrass_coordinates"]["lagrangian"] is True

# O = Z[s], s^2=-2. Elements are pairs (a,b)=a+b*s.
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
zero=(0,0)
M=[[(2,0),(1,1)],[(1,-1),(2,0)]]

def herm(v,w):
    out=zero
    for i in range(2):
        for j in range(2):
            out=add(out,mul(conj(v[i]),mul(M[i][j],w[j])))
    return out

# Exact finite bound. Under the complex embedding s=i*sqrt(2), M has eigenvalues
# 2 +/- sqrt(3), so H(v,v)=2 implies
#   ||v||^2 <= 2/(2-sqrt(3)) = 4+2sqrt(3) < 8.
# For an O-coordinate a+b*s, |a+b*s|^2=a^2+2b^2. Consequently every
# norm-2 column has |a|,|c|<=2 and |b|,|d|<=1. The [-2,2]x[-1,1]
# product box is therefore exhaustive, with no heuristic boundary argument.
vecs=[]
for a,b,c,d in itertools.product(range(-2,3), range(-1,2), range(-2,3), range(-1,2)):
    v=((a,b),(c,d))
    if herm(v,v)==(2,0):
        vecs.append(v)
assert len(vecs)==24

auts=[]
for v in vecs:
    for w in vecs:
        if herm(v,w)==(1,1) and herm(w,v)==(1,-1):
            auts.append((v,w))
assert len(auts)==48

# Reduce the O-linear action mod 2. R=O/2O=F2[e]/(e^2).
def elem_action(e):
    a,b=e[0]&1,e[1]&1
    # basis (1,e): (a+b e)(x+y e)=a x + (b x+a y)e
    return ((a,0),(b,a))

def act4(A, v):
    # v bits are (x1_const,x1_e,x2_const,x2_e).
    cols=A
    rows=((cols[0][0],cols[1][0]),(cols[0][1],cols[1][1]))
    xin=((v>>0)&1,(v>>1)&1)
    yin=((v>>2)&1,(v>>3)&1)
    inputs=(xin,yin)
    out=[]
    for r in range(2):
        oc=oe=0
        for k in range(2):
            B=elem_action(rows[r][k])
            x,y=inputs[k]
            oc ^= (B[0][0]*x) ^ (B[0][1]*y)
            oe ^= (B[1][0]*x) ^ (B[1][1]*y)
        out.extend([oc&1,oe&1])
    return out[0] | (out[1]<<1) | (out[2]<<2) | (out[3]<<3)

mod_actions={tuple(act4(A,v) for v in range(16)) for A in auts}
assert len(mod_actions)==24

# All 2-dimensional F2-subspaces of F2^4.
subspaces=set()
for a,b in itertools.combinations(range(1,16),2):
    subspaces.add(frozenset((0,a,b,a^b)))
assert len(subspaces)==35

invariant=[]
for U in subspaces:
    if all(frozenset(action[v] for v in U)==U for action in mod_actions):
        invariant.append(U)
assert len(invariant)==1
# bits 1 and 3 are (s,0) and (0,s).
expected=frozenset((0,2,8,10))
assert invariant[0]==expected

lat=art["exact_lattice_enumeration"]
assert lat["polarized_O_lattice_automorphisms"]==48
assert lat["distinct_mod2_actions_on_J2"]==24
assert lat["rank2_F2_subspaces_of_J2"]==35
assert lat["rank2_subspaces_invariant_under_all_mod2_actions"]==1
assert art["diagnostic_verdict"]["basis_comparison_gap_closed_without_explicit_basis_matrix"] is True
assert art["diagnostic_verdict"]["O210_excluded"] is False
assert all(v is False for v in art["firewalls"].values())

print("PASS EX3-04c scratch unique Bolza H4 plane coordinate lock")
print("exact norm bound: |a|,|c|<=2 and |b|,|d|<=1")
print("polarized O-lattice automorphisms=48; distinct mod2 actions=24")
print("unique invariant rank-2 plane = span_F2{(s,0),(0,s)} = s*(O/2O)^2")
print("H4 correspondence filter: T mod (s) in GL(2,F2)")
