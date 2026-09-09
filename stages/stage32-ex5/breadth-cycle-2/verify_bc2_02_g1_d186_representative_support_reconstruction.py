#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def load(path):
    return json.loads((ROOT / path).read_text())


def det_fraction(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    n = len(a)
    sign = 1
    out = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign *= -1
        pv = a[col][col]
        out *= pv
        for j in range(col, n):
            a[col][j] /= pv
        for r in range(col + 1, n):
            f = a[r][col]
            if f == 0:
                continue
            for j in range(col, n):
                a[r][j] -= f * a[col][j]
    return sign * out


artifact = json.loads((HERE / "bc2-02-g1-d186-representative-support-reconstruction.json").read_text())
audit = load("stages/stage32/32-21/32-21bl-joint-integer-witness-audit.json")
witness = load("stages/stage32/32-21/32-21bl-joint-integer-witness.json")
adapter = load("stages/stage32/32-21/post-21bl-picard64-witness-adapter.json")
bc01a = load("stages/stage32-ex5/breadth-cycle-2/bc2-01a-exceptional-pairing-bridge.json")
bc01b = load("stages/stage32-ex5/breadth-cycle-2/bc2-01b-runtime-node-coordinate-bridge.json")
manifest = load("stages/stage32/residual-32-01-production/full178-manifest.json")

assert artifact["status"] == "PASS_ONE_EXACT_REPRESENTATIVE_CANDIDATE_FULL178_PENDING"
assert audit["ordinal"] == 1617
assert audit["target"]["row_id"] == "g1-d186"
assert audit["triple"] == [76, -55, -96]
assert adapter["target"]["ordinal"] == 1617
assert adapter["target"]["row_id"] == "g1-d186"
assert adapter["target"]["triple"] == [76, -55, -96]
assert len(witness["witness_r_reduced"]) == 59
assert "g1-d186" in sum(manifest["m_class_rows"].values(), [])

pairings = adapter["all140"]["pairings"]
assert len(pairings) == 140
last48 = pairings[92:140]
assert last48 == artifact["exceptional_support"]["pairings_last48"]
assert sum(last48) == 266 == artifact["exceptional_support"]["exceptional_mass_sum"]
zeros = [k for k, v in enumerate(last48) if v == 0]
support = [k for k, v in enumerate(last48) if v > 0]
assert zeros == [1, 5, 6, 7]
assert support == artifact["exceptional_support"]["positive_support_indices_0based"]
assert len(support) == 44
assert bc01a["established"]["exceptional_indices_0based"] == [92, 139]

bridge_rows = {r["runtime_index_0based"]: r for r in bc01b["rows"]}
selected = artifact["exact_projective_span_checksum"]["supported_runtime_indices_used"]
assert all(k in support for k in selected)
coords = []
for k in selected:
    row = bridge_rows[k]
    assert row["retained_exceptional_index_0based"] == k
    assert row["all140_index_0based"] == 92 + k
    coords.append([int(x) for x in row["canonical_stoll_coordinates"]])
assert coords == artifact["exact_projective_span_checksum"]["rows"]
det = det_fraction(coords)
assert det == 16
assert artifact["exact_projective_span_checksum"]["homogeneous_vector_rank"] == 7
assert artifact["exact_projective_span_checksum"]["support_spans_P6"] is True

assert artifact["firewalls"]["full178_complete"] is False
assert artifact["firewalls"]["stage32_main_credit"] is False
assert artifact["firewalls"]["merge_authorized"] is False
print("STAGE32EX5_BC2_02_G1_D186_REPRESENTATIVE_SUPPORT_RECONSTRUCTION_OK")
