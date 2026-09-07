#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648j-cecotti-trace-orientation-correction.json"
EXPECTED = "3f6fd55ced259c6f28949df61865e22d43a669a50bdaf2adf5ddcd88411a48ec"


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
    assert path.is_file()
    assert blob_sha1(path) == lock["blob_sha1"]
    doc = json.loads(path.read_text())
    assert canonical(doc) == lock["canonical_sha256"]
    return doc


# K = Q(s,i), s^2=2, i^2=-1, basis (1,s,i,s*i).
class K:
    __slots__ = ("c",)

    def __init__(self, a=0, b=0, c=0, d=0):
        self.c = (F(a), F(b), F(c), F(d))

    def __add__(self, other):
        if not isinstance(other, K):
            other = K(other)
        return K(*(x + y for x, y in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return K(*(-x for x in self.c))

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return K(other) - self

    def __mul__(self, other):
        if not isinstance(other, K):
            other = K(other)
        a, b, c, d = self.c
        e, f, g, h = other.c
        return K(
            a * e + 2 * b * f - c * g - 2 * d * h,
            a * f + b * e - c * h - d * g,
            a * g + 2 * b * h + c * e + 2 * d * f,
            a * h + b * g + c * f + d * e,
        )

    __rmul__ = __mul__

    def __eq__(self, other):
        if not isinstance(other, K):
            other = K(other)
        return self.c == other.c

    def __hash__(self):
        return hash(self.c)


K0 = K()
K1 = K(1)
KR = K(0, 0, 0, 1)


def k_from_coeffs(xs):
    return K(*(F(str(x)) for x in xs))


def kmat(rows):
    return tuple(tuple(k_from_coeffs(x) for x in row) for row in rows)


def k_eye(n):
    return tuple(tuple(K1 if i == j else K0 for j in range(n)) for i in range(n))


def k_mul(A, B):
    return tuple(
        tuple(sum((A[i][k] * B[k][j] for k in range(len(B))), K0) for j in range(len(B[0])))
        for i in range(len(A))
    )


def k_pow(A, n):
    out = k_eye(len(A))
    while n:
        if n & 1:
            out = k_mul(out, A)
        A = k_mul(A, A)
        n //= 2
    return out


def k_neg(A):
    return tuple(tuple(-x for x in row) for row in A)


def k_trace(A):
    return sum((A[i][i] for i in range(len(A))), K0)


# Q(r), r^2=-2, for the retained lattice group.
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


def mod2_const(x: Qr) -> int:
    assert x.a.denominator == 1 and x.b.denominator == 1
    return int(x.a) & 1


LINES = {"L1": (1, 0), "L2": (0, 1), "L3": (1, 1)}
LINE_NAME = {v: k for k, v in LINES.items()}


def act_w(A, v):
    x, y = v
    return (
        (mod2_const(A[0][0]) * x + mod2_const(A[0][1]) * y) & 1,
        (mod2_const(A[1][0]) * x + mod2_const(A[1][1]) * y) & 1,
    )


def perm_w(A):
    return {name: LINE_NAME[act_w(A, v)] for name, v in LINES.items()}


SOURCE_PHI2 = {"Z1": "Z1", "Z2": "Z3", "Z3": "Z2"}
SOURCE_PHI6 = {"Z1": "Z3", "Z2": "Z1", "Z3": "Z2"}


def equivariant_maps(a, b):
    pa, pb = perm_w(a), perm_w(b)
    out = []
    for vals in itertools.permutations(("L1", "L2", "L3")):
        f = dict(zip(("Z1", "Z2", "Z3"), vals))
        if all(f[SOURCE_PHI2[z]] == pa[f[z]] for z in f) and all(f[SOURCE_PHI6[z]] == pb[f[z]] for z in f):
            out.append(f)
    return out


cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED
b = load_lock(cert["source_locks"]["post1648b"])
_ = load_lock(cert["source_locks"]["principal_rosati"])
assert b["decision"]["conditional_survivor_if_generator_pair_bound"] == 235
assert b["finite_equivariant_preflight"]["conditional_generator_binding"] == "phi2 -> S=b4 AND phi6 -> T=-b3 on one common marked ppav identification"

curve = cert["exact_curve_differential_representation"]
M2 = kmat(curve["phi2_matrix_coefficients"])
M6 = kmat(curve["phi6_matrix_coefficients"])
I2 = k_eye(2)
assert k_pow(M2, 2) == I2
assert k_pow(M6, 3) == k_neg(I2)
assert k_pow(k_mul(M2, M6), 4) == k_neg(I2)
assert k_trace(M2) == K0
assert k_trace(M6) == K1
assert k_trace(k_mul(M2, M6)) == KR
assert curve["traces"]["phi2_phi6"] == "+r"

S = ((Q1, Q1 + R), (Q0, -Q1))
T = ((Q1, Q1), (-Q1, Q0))
Tinv = q_inv(T)
minusI = q_neg(q_eye())
assert q_pow(S, 2) == q_eye()
assert q_pow(T, 3) == minusI
assert q_pow(q_mul(S, T), 4) == minusI
assert q_trace(S) == Q0
assert q_trace(T) == Q1
assert q_trace(q_mul(S, T)) == -R
assert q_trace(q_mul(S, Tinv)) == R
assert cert["target_named_generator_trace_test"]["traces"] == {"S": "0", "T": "1", "S*T": "-r", "S*T^-1": "+r"}
assert cert["target_named_generator_trace_test"]["literal_B7_to_S_B8_to_T_compatible"] is False

G = close_group((S, T))
assert len(G) == 48
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
        pairs.append((s, t))
assert len(pairs) == 48

trace_counts = Counter(q_trace(q_mul(s, t)) for s, t in pairs)
assert trace_counts == Counter({-R: 24, R: 24})


def conjugate_pair(h, pair):
    hi = q_inv(h)
    s, t = pair
    return q_mul(q_mul(h, s), hi), q_mul(q_mul(h, t), hi)


minus_orbit = {conjugate_pair(h, (S, T)) for h in G}
plus_orbit = {conjugate_pair(h, (S, Tinv)) for h in G}
assert len(minus_orbit) == len(plus_orbit) == 24
assert minus_orbit.isdisjoint(plus_orbit)
assert minus_orbit | plus_orbit == set(pairs)
assert all(q_trace(q_mul(s, t)) == -R for s, t in minus_orbit)
assert all(q_trace(q_mul(s, t)) == R for s, t in plus_orbit)

literal = equivariant_maps(S, Tinv)
assert literal == [{"Z1": "L1", "Z2": "L3", "Z3": "L2"}]

maps = []
for pair in plus_orbit:
    em = equivariant_maps(*pair)
    assert len(em) == 1
    maps.append(tuple(em[0][z] for z in ("Z1", "Z2", "Z3")))
map_counts = Counter(maps)
assert len(map_counts) == 6
assert set(map_counts.values()) == {4}
delta_counts = Counter(m[2] for m in maps)
assert delta_counts == Counter({"L1": 8, "L2": 8, "L3": 8})

enum = cert["ordered_generator_pair_enumeration"]
assert enum["target_group_order"] == 48
assert enum["ordered_generating_pairs"] == 48
assert enum["inner_conjugacy_orbits"] == 2
assert enum["orbit_sizes"] == [24, 24]
assert enum["cecotti_B7_B8_trace_orbit"] == "+r"

wc = cert["W_line_consequence"]
assert wc["literal_plus_r_unique_pair_to_line"] == literal[0]
assert wc["literal_plus_r_conditional_delta0inf_residue_decimal"] == 97
assert wc["literal_plus_r_conditional_only_not_current_credit"] is True
assert wc["all_plus_r_inner_conjugates"]["distinct_W_line_bijections"] == 6
assert wc["all_plus_r_inner_conjugates"]["delta0inf_image_counts"] == {"L1": 8, "L2": 8, "L3": 8}

corr = cert["correction_to_post1648b"]
assert corr["old_conditional_residue_decimal"] == 235
assert corr["new_exact_status"] == "RULED_OUT_FOR_THE_SPECIFIC_CECOTTI_B7_B8_PAIR_BY_HOLOMORPHIC_DIFFERENTIAL_TRACE"

dec = cert["decision"]
assert dec["survivors_current_credit"] == [73, 97, 235]
assert dec["absolute_delta0inf_retained_W_line_identified"] is False
assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
assert dec["O212_plus_advance_allowed"] is False
assert not any(cert["firewalls"].values())

print("POST1648J_CECOTTI_TRACE_ORIENTATION_CORRECTION_COMPLETE")
print(f"certificate_canonical={EXPECTED}")
print("curve_trace_phi2phi6=+r named_trace_ST=-r named_trace_STinv=+r")
print("ordered_generator_pairs=48 inner_orbits=2 sizes=24,24")
print("specific_B7_B8_to_S_T=ruled_out literal_plus_representative_delta0inf=L2 residue97_conditional_only")
print("plus_r_inner_conjugates_W_bijections=6 delta0inf_images=L1:8,L2:8,L3:8")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
