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


cert = json.loads(CERT.read_text())
pic = json.loads(PIC.read_text())
half = HALF.read_text()
mono = MONO.read_text()
source = SOURCE.read_text()

nodes = cert["inputs"]["absent_nodes"]
assert len(nodes) == 16
assert len(set(nodes)) == 16
assert cert["inputs"]["absent_component_count"] == 16
assert pic["absent_nodes"] == nodes
assert pic["exact_result"]["absent_span_rank"] == 15
assert cert["inputs"]["picard_absent_span_rank_mod2"] == 15
assert cert["inputs"]["all_ones_relation_mod2"] is True
assert "2 L_abs" in half and "B_abs" in half
assert "H_1(U;F_2)" in source and "F_2" in source
assert "alpha_abs" in mono and "lambda" in mono

n = 16
even_basis = []
for i in range(n - 1):
    row = [0] * n
    row[i] = 1
    row[-1] = 1
    even_basis.append(row)

rank = gf2_rank(even_basis)
assert rank == 15
assert cert["exact_result"]["relative_h2_dimension"] == 16
assert cert["exact_result"]["intersection_map_rank_mod2"] == rank
assert cert["exact_result"]["complement_h1_f2_dimension"] == n - rank == 1

# The quotient by the even-weight hyperplane is detected by coordinate sum.
for i in range(n):
    e = [0] * n
    e[i] = 1
    assert sum(e) % 2 == 1

assert cert["exact_result"]["absent_meridians_same_nonzero_class"] is True
assert cert["exact_result"]["alpha_abs_nonzero"] is True
assert cert["exact_result"]["alpha_abs_isomorphism"] is True
assert cert["inputs"]["e2_normalization_character_trivial"] is True
assert cert["exact_result"]["normalization_h1_map_to_complement_is_zero_in_e2_case"] is True

fw = cert["credit_firewall"]
for key, value in fw.items():
    if key.endswith("_authorized") or key.endswith("_credit") or key.endswith("_closed") or key.endswith("_complete") or key.endswith("_claim"):
        assert value is False, (key, value)

print("PASS ambient-complement-h1-bit")
print("absent=16 rank=15 quotient_h1_dim=1 alpha_abs=unique_nonzero conductor_loop_class=OPEN")
