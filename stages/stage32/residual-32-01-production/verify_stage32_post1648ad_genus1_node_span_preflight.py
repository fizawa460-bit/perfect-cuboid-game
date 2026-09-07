#!/usr/bin/env python3
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648ad-genus1-node-span-preflight.json"
PARENT = HERE / "post1648ac-galois-v4-common-support-interface-wall.json"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
NODES = ROOT / "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json"

cert = json.loads(CERT.read_text())
parent = json.loads(PARENT.read_text())
v6 = json.loads(V6.read_text())
nodes = json.loads(NODES.read_text())

claimed = cert["canonical_sha256_without_this_field"]
body = dict(cert)
body.pop("canonical_sha256_without_this_field")
actual = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
assert actual == claimed == "9bb1381f529d2c1674527ff35ec7a06cd6da537bce68ab80616bbfb0f6fa9557"

assert parent["canonical_sha256_without_this_field"] == "9f3e922a48b8131c6f86f81dc3e203fe05cc8fae01f86073edf66cbc93095158"
assert v6["canonical_sha256_without_this_field"] == "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
assert nodes["canonical_sha256"] == "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
assert nodes["exceptional_count"] == 48
assert nodes["field"] == "L=Q(i,sqrt(2)); all materialized coordinates lie in Q(i)"
assert nodes["field_element_encoding"] == "[real_numerator,real_denominator,i_numerator,i_denominator]; sqrt2 and i*sqrt2 coefficients are exactly zero"

exc_pairings = v6["witness"]["all140_pairings"][-48:]
assert len(exc_pairings) == 48
assert v6["witness"]["positive_exceptional_support"] == 47
assert [i for i, x in enumerate(exc_pairings) if x == 0] == [5] == v6["witness"]["zero_exceptional_indices"]
positive = [i for i, x in enumerate(exc_pairings) if x > 0]
assert len(positive) == 47

models = nodes["exceptional_models"]
assert [m["exceptional_id"] for m in models] == [f"EXC_{i:03d}" for i in range(1, 49)]

ZERO = (Fraction(0), Fraction(0))
def z(enc):
    a, b, c, d = enc
    return (Fraction(a, b), Fraction(c, d))
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x): return (-x[0], -x[1])
def sub(x, y): return add(x, neg(y))
def mul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def inv(x):
    den = x[0]*x[0] + x[1]*x[1]
    assert den
    return (x[0]/den, -x[1]/den)
def div(x, y): return mul(x, inv(y))
def nz(x): return x != ZERO

def rank(rows):
    a = [r[:] for r in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        p = next((j for j in range(r, m) if nz(a[j][c])), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pivot = a[r][c]
        a[r] = [div(x, pivot) for x in a[r]]
        for j in range(m):
            if j != r and nz(a[j][c]):
                q = a[j][c]
                a[j] = [sub(a[j][k], mul(q, a[r][k])) for k in range(n)]
        r += 1
        if r == m:
            break
    return r

rows = [[z(e) for e in models[i]["node_point_ambient_P6_L_basis"]] for i in positive]
assert all(len(row) == 7 for row in rows)
full_rank = rank(rows)
assert full_rank == 7

chosen = []
chosen_rows = []
for i, row in zip(positive, rows):
    if rank(chosen_rows + [row]) > len(chosen_rows):
        chosen.append(i)
        chosen_rows.append(row)
    if len(chosen) == 6:
        break

assert chosen == [0, 1, 2, 4, 8, 9]
assert rank(chosen_rows) == 6
assert [f"EXC_{i+1:03d}" for i in chosen] == ["EXC_001", "EXC_002", "EXC_003", "EXC_005", "EXC_009", "EXC_010"]

r = cert["exact_replay"]
assert r["positive_exceptional_count"] == 47
assert r["zero_exceptional_indices_0based"] == [5]
assert r["positive_node_span_vector_rank"] == 7
assert r["deterministic_rank6_indices_0based"] == chosen
assert r["deterministic_rank6_vector_rank"] == 6
assert r["six_positive_nodes_spanning_hyperplane_found"] is True

d = cert["decision"]
assert d["Q602_excluded"] is False
assert d["O210_excluded"] is False
assert d["O212_plus_advance_allowed"] is False
assert cert["fixed_target"]["surviving_residues_decimal"] == [73, 97, 235]
assert cert["conditional_geometric_reading"]["actual_effective_integral_carrier_proved"] is False
assert cert["conditional_geometric_reading"]["actual_carrier_equation_or_ideal_materialized"] is False
assert cert["verdict"] == "PASS_STAGE32_POST1648AD_GENUS1_NODE_SPAN_NONEXCLUSION"

print(json.dumps({
    "verdict": "PASS_STAGE32_POST1648AD_GENUS1_NODE_SPAN_NONEXCLUSION",
    "certificate_canonical_sha256": claimed,
    "positive_exceptional_count": 47,
    "positive_node_span_vector_rank": full_rank,
    "rank6_exceptional_ids": [f"EXC_{i+1:03d}" for i in chosen],
    "rank6": 6,
    "Q602_excluded": False,
    "O210_excluded": False,
    "survivors_current_credit": [73, 97, 235],
}, sort_keys=True))
