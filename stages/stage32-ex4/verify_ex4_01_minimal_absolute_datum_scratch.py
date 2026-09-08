#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "ex4-01-minimal-absolute-datum-contract-scratch.json"
EXPECTED = "feb6d20d2972d96a7ac5054c252ed3e2a87cad6bd4102c061877722b49d70928"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    field = "canonical_sha256_without_this_field" if "canonical_sha256_without_this_field" in body else "canonical_sha256"
    claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def load_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), lock["path"]
    if "blob_sha1" in lock:
        assert blob_sha1(path) == lock["blob_sha1"], lock["path"]
    doc = json.loads(path.read_text())
    if "canonical_sha256" in lock:
        assert canonical(doc) == lock["canonical_sha256"], lock["path"]
    return doc


class Qr:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, other):
        if not isinstance(other, Qr):
            other = Qr(other)
        return Qr(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Qr(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return Qr(other) - self

    def __mul__(self, other):
        if not isinstance(other, Qr):
            other = Qr(other)
        return Qr(self.a * other.a - 2 * self.b * other.b, self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def inv(self):
        den = self.a * self.a + 2 * self.b * self.b
        assert den
        return Qr(self.a / den, -self.b / den)

    def __eq__(self, other):
        if not isinstance(other, Qr):
            other = Qr(other)
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((self.a, self.b))


Q0 = Qr()
Q1 = Qr(1)
R = Qr(0, 1)


def q_eye():
    return ((Q1, Q0), (Q0, Q1))


def q_mul(A, B):
    return tuple(
        tuple(sum((A[i][k] * B[k][j] for k in range(2)), Q0) for j in range(2))
        for i in range(2)
    )


def q_inv(A):
    a, b = A[0]
    c, d = A[1]
    det_inv = (a * d - b * c).inv()
    return ((d * det_inv, -b * det_inv), (-c * det_inv, a * det_inv))


def q_pow(A, n):
    if n < 0:
        return q_pow(q_inv(A), -n)
    out = q_eye()
    while n:
        if n & 1:
            out = q_mul(out, A)
        A = q_mul(A, A)
        n //= 2
    return out


def q_neg(A):
    return tuple(tuple(-x for x in row) for row in A)


def q_trace(A):
    return A[0][0] + A[1][1]


def close_group(gens):
    I = q_eye()
    group = {I}
    stack = [I]
    while stack:
        a = stack.pop()
        for g in gens:
            b = q_mul(a, g)
            if b not in group:
                group.add(b)
                stack.append(b)
    return group


def element_order(A):
    x = q_eye()
    for n in range(1, 97):
        x = q_mul(x, A)
        if x == q_eye():
            return n
    raise AssertionError("order bound exceeded")


def commutes(A, B):
    return q_mul(A, B) == q_mul(B, A)


def mod2_const(x: Qr) -> int:
    assert x.a.denominator == 1 and x.b.denominator == 1
    return int(x.a) & 1


LINES = {"L1": (1, 0), "L2": (0, 1), "L3": (1, 1)}
LINE_NAME = {v: k for k, v in LINES.items()}
SOURCE_PHI2 = {"Z1": "Z1", "Z2": "Z3", "Z3": "Z2"}
SOURCE_PHI6 = {"Z1": "Z3", "Z2": "Z1", "Z3": "Z2"}


def act_w(A, v):
    x, y = v
    return (
        (mod2_const(A[0][0]) * x + mod2_const(A[0][1]) * y) & 1,
        (mod2_const(A[1][0]) * x + mod2_const(A[1][1]) * y) & 1,
    )


def perm_w(A):
    return {name: LINE_NAME[act_w(A, v)] for name, v in LINES.items()}


def compose(p, q):
    return {z: p[q[z]] for z in q}


def equivariant_maps(a, b):
    pa, pb = perm_w(a), perm_w(b)
    out = []
    for vals in itertools.permutations(("L1", "L2", "L3")):
        f = dict(zip(("Z1", "Z2", "Z3"), vals))
        if all(f[SOURCE_PHI2[z]] == pa[f[z]] for z in f) and all(
            f[SOURCE_PHI6[z]] == pb[f[z]] for z in f
        ):
            out.append(f)
    return out


def delta_line(pair):
    maps = equivariant_maps(*pair)
    assert len(maps) == 1
    return maps[0]["Z3"]


cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED

ex400 = load_lock(cert["source_locks"]["ex4_00"])
cec = load_lock(cert["source_locks"]["cecotti_trace_orientation"])
hdeck = load_lock(cert["source_locks"]["audited_hdeck_direction"])
trans = load_lock(cert["source_locks"]["audited_line_to_residue"])

assert ex400["decision"]["result"] == "EX4_00_SOURCE_LOCK_AND_TYPED_MARKING_GRAPH_COMPLETE_ON_SCRATCH_BRANCH"
assert ex400["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert hdeck["abstract_character_to_w_binding"]["chi_u_canonical_pair"] == "Z3"
assert hdeck["abstract_character_to_w_binding"]["abstract_class_name"] == "delta_0inf"
assert hdeck["abstract_character_to_w_binding"]["retained_F2_4_coordinate_line_identified"] is False
assert trans["retained_residue_filter"]["surviving_residues_decimal"] == [73, 97, 235]
assert trans["retained_residue_filter"]["image_lines_in_W"] == [
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
]

source = cec["W_line_consequence"]["source_pair_permutations"]
assert source["phi2"] == SOURCE_PHI2
assert source["phi6"] == SOURCE_PHI6
source_product = compose(SOURCE_PHI2, SOURCE_PHI6)
assert source_product == {"Z1": "Z2", "Z2": "Z1", "Z3": "Z3"}

S = ((Q1, Q1 + R), (Q0, -Q1))
T = ((Q1, Q1), (-Q1, Q0))
Tinv = q_inv(T)
P = q_mul(S, Tinv)
minusI = q_neg(q_eye())

assert perm_w(P) == {"L1": "L3", "L2": "L2", "L3": "L1"}

G = close_group((S, T))
assert len(G) == 48
center = {h for h in G if all(commutes(h, g) for g in G)}
assert center == {q_eye(), minusI}

pairs = []
for s in G:
    if q_pow(s, 2) != q_eye():
        continue
    for t in G:
        if q_pow(t, 3) != minusI:
            continue
        if q_pow(q_mul(s, t), 4) != minusI:
            continue
        if len(close_group((s, t))) != 48:
            continue
        if q_trace(q_mul(s, t)) != R:
            continue
        pairs.append((s, t))
assert len(pairs) == 24

assert all(len(equivariant_maps(s, t)) == 1 for s, t in pairs)
maps = [tuple(equivariant_maps(s, t)[0][z] for z in ("Z1", "Z2", "Z3")) for s, t in pairs]
map_counts = Counter(maps)
assert len(map_counts) == 6
assert set(map_counts.values()) == {4}
delta_counts = Counter(m[2] for m in maps)
assert delta_counts == Counter({"L1": 8, "L2": 8, "L3": 8})

line_action_image = {tuple(perm_w(h)[x] for x in ("L1", "L2", "L3")) for h in G}
assert len(line_action_image) == 6
kerG = {h for h in G if perm_w(h) == {"L1": "L1", "L2": "L2", "L3": "L3"}}
assert len(kerG) == 8
assert Counter(element_order(h) for h in kerG) == Counter({4: 6, 2: 1, 1: 1})
assert all(q_mul(h, h) in center for h in kerG)

fix_s = [pair for pair in pairs if pair[0] == S]
fix_t = [pair for pair in pairs if pair[1] == Tinv]
fix_p = [pair for pair in pairs if q_mul(pair[0], pair[1]) == P]
assert len(fix_s) == 2
assert Counter(delta_line(p) for p in fix_s) == Counter({"L2": 1, "L3": 1})
assert len(fix_t) == 3
assert Counter(delta_line(p) for p in fix_t) == Counter({"L1": 1, "L2": 1, "L3": 1})
assert len(fix_p) == 4
assert Counter(delta_line(p) for p in fix_p) == Counter({"L2": 4})

amb = cert["current_ambiguity"]
assert amb["retained_group_order"] == 48
assert amb["center_order"] == 2
assert amb["trace_plus_r_admissible_pair_count"] == 24
assert amb["residual_identification_group_order"] == 24
assert amb["induced_W_line_action_image"] == "S3"
assert amb["induced_W_line_action_order"] == 6
assert amb["kernel_in_G_order"] == 8
assert amb["kernel_in_G_structure"] == "Q8"
assert amb["kernel_after_center_quotient_order"] == 4
assert amb["kernel_after_center_quotient_structure"] == "V4"
assert amb["delta0inf_image_counts"] == {"L1": 8, "L2": 8, "L3": 8}

anchor = cert["product_anchor"]
assert anchor["source_product_pair_action"] == source_product
assert anchor["source_product_unique_fixed_pair"] == "Z3"
assert anchor["retained_product_W_action"] == perm_w(P)
assert anchor["retained_product_unique_fixed_W_line"] == "L2"
assert anchor["if_exact_product_binding_is_supplied"]["compatible_plus_r_pair_count"] == 4
assert anchor["if_exact_product_binding_is_supplied"]["delta0inf_image_counts"] == {"L1": 0, "L2": 4, "L3": 0}
assert anchor["if_exact_product_binding_is_supplied"]["unique_absolute_W_line"] == "L2"
assert anchor["if_exact_product_binding_is_supplied"]["corresponding_Q602_residue"] == 97
assert anchor["if_exact_product_binding_is_supplied"]["residue_excluded"] is False

cmp = cert["natural_anchor_comparison"]
assert cmp["fix_phi2_to_S"]["compatible_plus_r_pair_count"] == 2
assert cmp["fix_phi2_to_S"]["delta0inf_possible_lines"] == ["L2", "L3"]
assert cmp["fix_phi2_to_S"]["sufficient_for_absolute_line"] is False
assert cmp["fix_phi6_to_Tinverse"]["compatible_plus_r_pair_count"] == 3
assert cmp["fix_phi6_to_Tinverse"]["delta0inf_possible_lines"] == ["L1", "L2", "L3"]
assert cmp["fix_phi6_to_Tinverse"]["sufficient_for_absolute_line"] is False
assert cmp["fix_product_phi2phi6_to_STinverse"]["compatible_plus_r_pair_count"] == 4
assert cmp["fix_product_phi2phi6_to_STinverse"]["delta0inf_possible_lines"] == ["L2"]
assert cmp["fix_product_phi2phi6_to_STinverse"]["sufficient_for_absolute_line"] is True

decision = cert["decision"]
assert decision["current_absolute_W_line_identified"] is False
assert decision["current_absolute_Q602_residue_identified"] is False
assert decision["next_leaf"] == "EX4-02_SOURCE_INVENTORY_FOR_EXACT_PRODUCT_ELEMENT_BINDING"
assert decision["retained_claim_dag_sync_performed"] is False
assert decision["Q602_excluded"] is False
assert decision["O210_excluded"] is False
assert decision["stage32_main_credit"] is False
assert not any(cert["firewalls"].values())

print("STAGE32EX4_EX4_01_MINIMAL_ABSOLUTE_DATUM_CONTRACT_SCRATCH_COMPLETE")
print(f"certificate_canonical={EXPECTED}")
print("residual_identification_group_order=24 induced_W_line_action=S3 kernel_mod_center=V4")
print("trace_plus_r_pairs=24 delta_images=L1:8,L2:8,L3:8")
print("fix_phi2_to_S -> L2/L3; fix_phi6_to_Tinv -> L1/L2/L3")
print("exact_product_binding phi2*phi6 -> S*T^-1 forces Z3 -> L2 -> residue97 conditionally")
print("current_absolute_line=false Q602_excluded=false O210_excluded=false Stage32_MAIN_credit=false")
