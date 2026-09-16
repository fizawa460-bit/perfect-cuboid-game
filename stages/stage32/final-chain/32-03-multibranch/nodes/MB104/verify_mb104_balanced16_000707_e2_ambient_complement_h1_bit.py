#!/usr/bin/env python3
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

CERT = BASE / "GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-COMPLEMENT-H1-BIT-CERTIFICATE.json"
PIC = BASE / "GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-DESCENT-PARITY-CERTIFICATE.json"
HALF = BASE / "GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md"
MONO = BASE / "GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-KUMMER-MONODROMY.md"
SOURCE = BASE / "CUBOID-SURFACE-COMPLEMENT-MOD2-HOMOLOGY-SOURCE-NOTE.md"


def gf2_rank(rows):
    rows = [sum((int(v) & 1) << j for j, v in enumerate(row)) for row in rows]
    rank = 0
    while rows:
        pivot = max(rows)
        if pivot == 0:
            break
        rows.remove(pivot)
        bit = 1 << (pivot.bit_length() - 1)
        rows = [r ^ pivot if r & bit else r for r in rows]
        rank += 1
    return rank


def det_bareiss(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            assert swap is not None
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


cert = json.loads(CERT.read_text())
pic = json.loads(PIC.read_text())
half = HALF.read_text()
mono = MONO.read_text()
source = SOURCE.read_text()

assert cert["schema_version"] == "stage32-mb104-ambient-complement-h1-bit-v2"
nodes = cert["inputs"]["absent_nodes"]
assert len(nodes) == 16 and len(set(nodes)) == 16
assert cert["inputs"]["absent_component_count"] == 16
assert cert["inputs"]["absent_self_intersection"] == -2
assert pic["absent_nodes"] == nodes
assert pic["exact_result"]["absent_span_rank"] == 15
assert cert["inputs"]["picard_absent_span_rank_mod2"] == 15
assert cert["inputs"]["all_ones_relation_mod2"] is True
assert cert["inputs"]["surface_h1_z_zero"] is True
assert "2 L_abs" in half and "B_abs" in half
assert "H_1(U,Z) ~= Z/2" in source
assert "IMAGE-Z" in source and "LINK-Z" in source
assert "alpha_abs" in mono and "lambda" in mono

n = 16
even_basis = []
for i in range(n - 1):
    row = [0] * n
    row[i] = 1
    row[-1] = 1
    even_basis.append(row)
assert gf2_rank(even_basis) == 15

# Integral even-sum lattice basis: e_i+e_16 for i<16 and 2e_16.
index_basis = [row[:] for row in even_basis]
last = [0] * n
last[-1] = 2
index_basis.append(last)
assert abs(det_bareiss(index_basis)) == 2

res = cert["exact_result"]
assert res["relative_h2_integral_rank"] == 16
assert res["intersection_map_contains_2Z16"] is True
assert res["intersection_map_rank_mod2"] == 15
assert res["intersection_map_image_integral"] == "{v in Z^16 : sum(v_i) even}"
assert res["intersection_image_index_integral"] == 2
assert res["smith_invariant_factors_model"] == [1] * 15 + [2]
assert res["complement_h1_integral"] == "Z/2"
assert res["complement_h1_f2_dimension"] == 1

# Every meridian basis vector has quotient bit one; every even-weight vector has bit zero.
for i in range(n):
    e = [0] * n
    e[i] = 1
    assert sum(e) % 2 == 1
for row in even_basis:
    assert sum(row) % 2 == 0

assert res["absent_meridians_same_nonzero_class"] is True
assert res["alpha_abs_nonzero"] is True
assert res["alpha_abs_unique_nonzero"] is True
assert res["alpha_abs_isomorphism"] is True
assert cert["inputs"]["e2_normalization_character_trivial"] is True
assert res["normalization_h1_map_to_complement_is_zero_in_e2_case"] is True
assert "Gamma.B_abs mod 2" in res["linking_evaluator"]

wolfram = cert["wolfram_crosscheck"]
assert wolfram["relation_matrix_shape"] == [31, 16]
assert wolfram["smith_diagonal"] == [1] * 15 + [2]
assert wolfram["index"] == 2 and wolfram["quotient"] == "Z/2"

fw = cert["credit_firewall"]
for key, value in fw.items():
    if key.endswith("_authorized") or key.endswith("_credit") or key.endswith("_closed") or key.endswith("_complete") or key.endswith("_claim"):
        assert value is False, (key, value)

print("PASS ambient-complement-h1-bit-v2")
print("image=even-sum-lattice index=2 H1(U,Z)=Z/2 alpha_abs=linking-parity conductor_loop_class=OPEN")
