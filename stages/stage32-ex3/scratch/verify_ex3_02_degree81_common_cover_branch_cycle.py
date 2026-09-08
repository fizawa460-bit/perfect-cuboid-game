#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-02-degree81-common-cover-branch-cycle.json"
art = json.loads(ART.read_text(encoding="utf-8"))

assert art["status"] == "SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED"
fi = art["fixed_input"]
assert fi["degree_N_to_X4_second"] == 81
assert fi["degree_Y_to_C0_second"] == 81
assert fi["ramification_Y_to_C0_second"] == 48
assert fi["ramification_Y_to_N"] == 210
assert fi["C0_to_X4_branch_value_count"] == 6

# Global bookkeeping for six distinguished cusp values.
# Let k be the total number of cycles in their S_81 branch cycles.
# RH for N(g=1)->P1 of degree 81 gives total ramification 162.
# The common quadratic pullback has 210 branch points, hence 210 odd cycles.
for k in range(324, 349):
    r_n_cusp = 486 - k
    r_n_out = k - 324
    r_y_cusp = 696 - 2 * k
    r_y_out = 2 * r_n_out
    assert r_n_cusp + r_n_out == 162
    assert r_y_cusp >= 0
    assert r_y_cusp + r_y_out == 48
assert art["six_cusp_branch_cycle_ledger"]["forced_k_range"] == [324, 348]

N = 81

def identity() -> list[int]:
    return list(range(N))

def compose(p: list[int], q: list[int]) -> list[int]:
    return [p[q[i]] for i in range(N)]

def involution(edges: list[tuple[int, int]]) -> list[int]:
    p = identity()
    used: set[int] = set()
    for u, v in edges:
        assert u != v and u not in used and v not in used
        used.add(u)
        used.add(v)
        p[u], p[v] = v, u
    return p

def cycle_lengths(p: list[int]) -> list[int]:
    seen = [False] * N
    out: list[int] = []
    for i in range(N):
        if seen[i]:
            continue
        j = i
        length = 0
        while not seen[j]:
            seen[j] = True
            length += 1
            j = p[j]
        out.append(length)
    return out

def ramification(p: list[int]) -> int:
    return sum(e - 1 for e in cycle_lengths(p))

A = [(i, i + 1) for i in range(0, 69, 3)]
B = [(i, i + 1) for i in range(1, 69, 3)]
C = [(i, i + 1) for i in range(2, 69, 3)]
assert len(A) == len(B) == len(C) == 23

a = involution(A)
b = involution(B)
c = involution(C)

for p in (a, b, c):
    lens = cycle_lengths(p)
    assert lens.count(1) == 35
    assert lens.count(2) == 23
    assert len(lens) == 58
    assert ramification(p) == 23
    assert compose(p, p) == identity()

cusps = [a, a, b, b, c, c]
k = sum(len(cycle_lengths(p)) for p in cusps)
odd_cycles = sum(sum(1 for e in cycle_lengths(p) if e % 2) for p in cusps)
r_n_cusp = sum(ramification(p) for p in cusps)
assert k == 348
assert odd_cycles == 210
assert r_n_cusp == 138

# At a branch value of C0->X4, normalized t^e=s^2 contributes e-gcd(e,2)
# to Y->C0. For the witness all cusp cycles have e in {1,2}, so this is zero.
r_y_cusp = 0
for p in cusps:
    for e in cycle_lengths(p):
        d = 1 if e % 2 else 2
        r_y_cusp += e - d
assert r_y_cusp == 0

# Twelve interior transpositions, each used as an adjacent repeated pair.
# This supplies 24 simple branch values away from the six cusps.
T_edges = [(69 + j, 70 + j) for j in range(11)] + [(0, 80)]
assert len(T_edges) == 12
interior_unique = [involution([edge]) for edge in T_edges]
interior_cycles: list[list[int]] = []
for t in interior_unique:
    assert ramification(t) == 1
    interior_cycles.extend([t, t])

branch_cycles = cusps + interior_cycles
prod = identity()
for p in branch_cycles:
    prod = compose(prod, p)
assert prod == identity()

# Transitivity: the generator edges contain the path 0-1-...-80.
generators = [a, b, c] + interior_unique
orbit = {0}
while True:
    expanded = orbit | {g[x] for g in generators for x in orbit}
    if expanded == orbit:
        break
    orbit = expanded
assert len(orbit) == 81

r_n_out = sum(ramification(p) for p in interior_cycles)
assert r_n_out == 24
assert r_n_cusp + r_n_out == 162
assert -2 * 81 + 162 == 0  # 2g(N)-2

# Away from the six branch values, the quadratic base change is etale,
# so each N ramification contribution lifts twice.
r_y_out = 2 * r_n_out
assert r_y_out == 48
assert r_y_cusp + r_y_out == 48

v = art["diagnostic_verdict"]
assert v["degree81_RH_contradiction"] is False
assert v["ramification48_independent_obstruction"] is False
assert v["abstract_second_projection_population_empty"] is False
assert v["explicit_abstract_second_projection_witness_obtained"] is True
assert v["EX3_02_exclusion_obtained"] is False
assert all(value is False for value in art["firewalls"].values())

print("PASS EX3-02 scratch degree-81 common-cover branch-cycle witness")
print("six cusps: (a,a,b,b,c,c), each type 2^23 1^35")
print("k=348; odd cusp cycles=210; N cusp ramification=138")
print("24 simple interior branch values; N total ramification=162; genus N=1")
print("base-change ramification: cusp=0, interior=48, total Y->C0=48")
print("verdict: second projection alone is nonpruning at abstract common-cover level")
