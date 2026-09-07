#!/usr/bin/env python3
"""V91C1V scratch diagnostic: exact actual-prime -> pinned known-curve components.

No Stage33 credit. Replays V91C1S, constructs the 92 Testa--Stoll known
curves in the exact pinned cuboids.magma order, and asks which geometric known
curves are contained in each strict-prime ideal appearing in the swap23
package difference after scalar extension to Q(i,sqrt(2)).
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S_PATH = HERE / "diagnose_e3_v91c1s_swap23_prime_attached_cech_difference.py"
K_PATH = HERE.parent / "33-07" / "certify_two_coordinate_swap_picard_rows.py"
SIDE_PRODUCER = HERE.parent / "33-07" / "certify_boundary_side_p1_crossing_coordinates.py"

sns = runpy.run_path(str(S_PATH))
assert sns["result"]["success"] is True
sys.path.insert(0, str(K_PATH.parent))
kns = runpy.run_path(str(K_PATH))

variables = sns["variables"]
a1, a2, a3, b1, b2, b3, c = variables
Q = sns["Q"]
ens = sns["ens"]
eps = [1, -1]
rt2 = sp.sqrt(2)

known_generators = []
known_meta = []

def add_known(family, group, signs, linear_generators):
    known_generators.append(Q + list(linear_generators))
    known_meta.append({
        "class_index_1based": len(known_generators),
        "family": family,
        "group": group,
        "signs": dict(signs),
    })

# Exact transcription of pinned Cuboids/cuboids.magma:
# C1s := 4 blocks of 8; first three use e1,e2,e3 order, fourth e3,e2,e1.
for e1 in eps:
    for e2 in eps:
        for e3 in eps:
            add_known("C1", 1, {"e1": e1, "e2": e2, "e3": e3},
                      [a1, a2 + e1*b3, a3 + e2*b2, b1 + e3*c])
for e1 in eps:
    for e2 in eps:
        for e3 in eps:
            add_known("C1", 2, {"e1": e1, "e2": e2, "e3": e3},
                      [a2, a3 + e1*b1, a1 + e2*b3, b2 + e3*c])
for e1 in eps:
    for e2 in eps:
        for e3 in eps:
            add_known("C1", 3, {"e1": e1, "e2": e2, "e3": e3},
                      [a3, a1 + e1*b2, a2 + e2*b1, b3 + e3*c])
for e3 in eps:
    for e2 in eps:
        for e1 in eps:
            add_known("C1", 4, {"e1": e1, "e2": e2, "e3": e3},
                      [c, sp.I*a1 + e1*b1, sp.I*a2 + e2*b2, sp.I*a3 + e3*b3])

# C2s := 3 blocks of 4, each e1,e2.
for e1 in eps:
    for e2 in eps:
        add_known("C2", 1, {"e1": e1, "e2": e2},
                  [b1, sp.I*a2 + e1*a3, a1 + e2*c])
for e1 in eps:
    for e2 in eps:
        add_known("C2", 2, {"e1": e1, "e2": e2},
                  [b2, sp.I*a3 + e1*a1, a2 + e2*c])
for e1 in eps:
    for e2 in eps:
        add_known("C2", 3, {"e1": e1, "e2": e2},
                  [b3, sp.I*a1 + e1*a2, a3 + e2*c])

# C3s := 6 blocks of 8. The first three use e1,e2,e3 order, the last
# three use e3,e2,e1 exactly as in the pinned source.
for e1 in eps:
    for e2 in eps:
        for e3 in eps:
            add_known("C3", 1, {"e1": e1, "e2": e2, "e3": e3},
                      [a1 + e1*a2, rt2*a1 + e2*b3, b1 + e3*b2])
for e1 in eps:
    for e2 in eps:
        for e3 in eps:
            add_known("C3", 2, {"e1": e1, "e2": e2, "e3": e3},
                      [a2 + e1*a3, rt2*a2 + e2*b1, b2 + e3*b3])
for e1 in eps:
    for e2 in eps:
        for e3 in eps:
            add_known("C3", 3, {"e1": e1, "e2": e2, "e3": e3},
                      [a3 + e1*a1, rt2*a3 + e2*b2, b3 + e3*b1])
for e3 in eps:
    for e2 in eps:
        for e1 in eps:
            add_known("C3", 4, {"e1": e1, "e2": e2, "e3": e3},
                      [sp.I*a1 + e1*c, sp.I*b2 + e2*b3, sp.I*rt2*a1 + e3*b1])
for e3 in eps:
    for e2 in eps:
        for e1 in eps:
            add_known("C3", 5, {"e1": e1, "e2": e2, "e3": e3},
                      [sp.I*a2 + e1*c, sp.I*b3 + e2*b1, sp.I*rt2*a2 + e3*b2])
for e3 in eps:
    for e2 in eps:
        for e1 in eps:
            add_known("C3", 6, {"e1": e1, "e2": e2, "e3": e3},
                      [sp.I*a3 + e1*c, sp.I*b1 + e2*b2, sp.I*rt2*a3 + e3*b3])

assert len(known_generators) == 92
assert len(kns["known"]) == 140

# Source-lock the first-24 C1 ordering and the EXC numbering to the retained
# Magma producer itself. Its generated JSON is intentionally not required to
# be checked in: the producer uses Position(pts,p), checks p in Cs[j], and its
# j->(family,e1,e2,e3) formula is reproduced below.
producer_text = SIDE_PRODUCER.read_text(encoding="utf-8")
for snippet in [
    "for j in [1..24] do",
    "fam := (j-1) div 8;",
    "r := (j-1) mod 8;",
    "e1 := [1,-1][(r div 4)+1];",
    "e2 := [1,-1][((r div 2) mod 2)+1];",
    "e3 := [1,-1][(r mod 2)+1];",
    "pos:=Position(pts,p);",
    "assert pos ne 0 and p in Cs[j];",
    '"upstream_C1s_index_1based": side',
    '"exceptional_id": f"EXC_{point:03d}"',
]:
    assert snippet in producer_text, snippet
for j in range(1, 25):
    r = (j - 1) % 8
    expected_signs = {
        "e1": [1, -1][r // 4],
        "e2": [1, -1][(r // 2) % 2],
        "e3": [1, -1][r % 2],
    }
    meta = known_meta[j - 1]
    assert meta["family"] == "C1"
    assert meta["group"] == ((j - 1) // 8) + 1
    assert meta["signs"] == expected_signs

extension = [sp.I, rt2]
known_gbs = [
    sp.groebner(gens, *variables, order="grevlex", extension=extension)
    for gens in known_generators
]

def contained_known_classes(generators):
    out = []
    for j, gb in enumerate(known_gbs, start=1):
        if all(sp.expand(gb.reduce(sp.expand(g))[1]) == 0 for g in generators):
            out.append(j)
    return out

all_prime_generators = dict(sns["canonical_generators"])
for source_id, generators in sns["canonical_generators"].items():
    acted = [
        ens["apply_word_expr"](poly, sns["WORD"], variables)
        for poly in generators
    ]
    image_id, _basis = ens["canonical_ideal"](acted, variables)
    assert image_id == sns["prime_action"][source_id]
    all_prime_generators.setdefault(image_id, acted)

needed = sorted(sns["strict_package_difference"])
assert len(needed) == sns["result"]["strict_package_difference_nonzero_coefficients"]
matches = {
    prime_id: contained_known_classes(all_prime_generators[prime_id])
    for prime_id in needed
}

result = {
    "success": True,
    "credit": False,
    "marker": "V91C1V_ACTUAL_PRIME_TO_KNOWN140_GEOMETRIC_LOCATOR_SCRATCH",
    "pinned_known_curve_count": len(known_generators),
    "strict_difference_prime_count": len(needed),
    "strict_difference_prime_known_component_matches": matches,
    "match_count_histogram": {
        str(n): sum(len(v) == n for v in matches.values())
        for n in sorted(set(len(v) for v in matches.values()))
    },
    "all_needed_primes_have_known_components": all(matches[p] for p in needed),
    "exceptional_locator_rule": "EXC_j -> known140 class 92+j",
    "exceptional_locator_source_locked": True,
    "pic2_cech_difference_class_computed": False,
    "a2_02_swap23_seed_fixed_mod_pic2": False,
    "a2_02_marked_brauer_image_excluded_from_mask20": False,
}
print(__import__("json").dumps(result, sort_keys=True))
