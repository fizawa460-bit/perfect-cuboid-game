#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-01-etale105-orbifold-monodromy.json"
art = json.loads(ART.read_text(encoding="utf-8"))

assert art["status"] == "SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED"
assert art["fixed_input"]["degree_N_to_X4_first"] == 105
assert art["fixed_input"]["degree_Y_to_C0_first"] == 105
assert art["fixed_input"]["ramification_Y_to_C0_first"] == 0
assert art["fixed_input"]["degree_C0_to_X4"] == 2
assert art["fixed_input"]["C0_to_X4_branch_value_count"] == 6

# Local normalized base change t^e=s^2: d=gcd(e,2),
# ramification to C0 is e/d. Etaleness forces e in {1,2}.
for e in range(1, 16):
    d = 1 if e % 2 else 2
    etale_to_c0 = (e // d == 1)
    assert etale_to_c0 == (e in {1, 2})
    if e in {1, 2}:
        ram_to_N = 2 // d
        assert (ram_to_N == 2) == (e == 1)

# RH for z:N(g=1)->X4(g=0), degree 105.
Rz = 2 * 105
assert Rz == 210

# Explicit six-involution branch-cycle witness on 105 points.
COLS = 35
N = 3 * COLS

def idx(r: int, j: int) -> int:
    return 3 * (j % COLS) + r

def identity() -> list[int]:
    return list(range(N))

def compose(p: list[int], q: list[int]) -> list[int]:
    return [p[q[i]] for i in range(N)]

def transposition_count(p: list[int]) -> int:
    return sum(1 for i in range(N) if p[i] > i)

a = identity()
b = identity()
c = identity()
for j in range(COLS):
    a[idx(0,j)], a[idx(1,j)] = idx(1,j), idx(0,j)
    b[idx(1,j)], b[idx(2,j)] = idx(2,j), idx(1,j)
    x, y = idx(2,j), idx(0,j+1)
    c[x], c[y] = y, x

for p in (a,b,c):
    assert compose(p,p) == identity()
    assert transposition_count(p) == 35
    assert sum(1 for i in range(N) if p[i] == i) == 35

cycles = [a,a,b,b,c,c]
prod = identity()
for p in cycles:
    prod = compose(prod,p)
assert prod == identity()
assert sum(transposition_count(p) for p in cycles) == 210

# Connectedness/transitivity of the generated action.
orbit = {0}
while True:
    expanded = orbit | {p[x] for p in (a,b,c) for x in orbit}
    if expanded == orbit:
        break
    orbit = expanded
assert len(orbit) == 105

# Riemann-Hurwitz genus of the degree-105 P1 cover.
two_g_minus_2 = -2 * 105 + 210
assert two_g_minus_2 == 0
assert art["explicit_abstract_witness"]["resulting_N_genus"] == 1

# Symmetric cusp profile of the witness: b_i=a_i=35 for six cusps.
b_i = [35] * 6
a_i = [105 - 2*b for b in b_i]
assert a_i == [35] * 6
assert sum(b_i) == 210
assert sum(a_i) == 210
assert all(a + 2*b == 105 for a,b in zip(a_i,b_i))

v = art["diagnostic_verdict"]
assert v["first_projection_RH_contradiction"] is False
assert v["abstract_monodromy_population_empty"] is False
assert v["explicit_abstract_monodromy_witness_obtained"] is True
assert v["EX3_01_exclusion_obtained"] is False
assert all(value is False for value in art["firewalls"].values())

print("PASS EX3-01 scratch degree-105 orbifold monodromy witness")
print("branch cycles: (a,a,b,b,c,c), each 2^35 1^35")
print("product-one: yes; transitive: yes; total ramification: 210; genus N: 1")
print("verdict: first projection alone is nonpruning at abstract-cover level")
