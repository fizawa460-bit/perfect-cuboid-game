#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT_PATH = ROOT / "stages/stage32-ex4/ex4-04-retained-ppav-cm-marking-adapter-scratch.json"
EXPECTED = "4929ce8ecf3e12a894445c19ac390dd723960ae315f8fa1ec06110d5e868a5cc"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
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


class Qr:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = F(a)
        self.b = F(b)

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
        return Qr(
            self.a * other.a - 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def conj(self):
        return Qr(self.a, -self.b)

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


def mul(A, B):
    return tuple(
        tuple(sum((A[i][k] * B[k][j] for k in range(len(B))), Q0) for j in range(len(B[0])))
        for i in range(len(A))
    )


def adj(A):
    return tuple(tuple(A[j][i].conj() for j in range(len(A))) for i in range(len(A[0])))


def eye2():
    return ((Q1, Q0), (Q0, Q1))


def inv2(A):
    a, b = A[0]
    c, d = A[1]
    deti = (a * d - b * c).inv()
    return ((d * deti, -b * deti), (-c * deti, a * deti))


def close_group(gens):
    G = {eye2()}
    stack = [eye2()]
    while stack:
        a = stack.pop()
        for g in gens:
            b = mul(a, g)
            if b not in G:
                G.add(b)
                stack.append(b)
    return G


def hpair(v, w, H):
    Hw = (
        H[0][0] * w[0] + H[0][1] * w[1],
        H[1][0] * w[0] + H[1][1] * w[1],
    )
    return v[0].conj() * Hw[0] + v[1].conj() * Hw[1]


def const_mod2(x: Qr) -> int:
    assert x.a.denominator == 1
    return int(x.a) & 1


LINES = {(1, 0): "L1", (0, 1): "L2", (1, 1): "L3"}
LINE_VECTORS = [(1, 0), (0, 1), (1, 1)]


def W_matrix(A):
    return (
        (const_mod2(A[0][0]), const_mod2(A[0][1])),
        (const_mod2(A[1][0]), const_mod2(A[1][1])),
    )


def act2(M, v):
    return (
        (M[0][0] * v[0] + M[0][1] * v[1]) & 1,
        (M[1][0] * v[0] + M[1][1] * v[1]) & 1,
    )


def W_perm(A):
    M = W_matrix(A)
    return tuple(LINES[act2(M, v)] for v in LINE_VECTORS)


cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED

ex3 = load_lock(cert["repo_source_locks"]["ex4_03_preflight"])
principal = load_lock(cert["repo_source_locks"]["principal_rosati"])
cecotti = load_lock(cert["repo_source_locks"]["cecotti_trace_orientation"])

assert ex3["decision"]["absolute_W_line_identified"] is False
assert principal["quadratic_order"]["relation"] == "r^2=-2"
assert principal["principal_polarization"]["hermitian_matrix"] == [["2", "1+r"], ["1-r", "2"]]
assert principal["principal_polarization"]["riemann_form_basis"] == ["e1", "e2", "r*e1", "r*e2"]
assert principal["principal_polarization"]["riemann_form_matrix"] == [
    [0, 1, 2, 1],
    [-1, 0, 1, 2],
    [-2, -1, 0, 2],
    [-1, -2, -2, 0],
]

assert cecotti["target_named_generator_trace_test"]["S_equals_b4"] == [
    [["1", 0], ["1", "1"]],
    [[0, 0], ["-1", 0]],
]
assert cecotti["target_named_generator_trace_test"]["T_equals_minus_b3"] == [
    [["1", 0], ["1", 0]],
    [["-1", 0], [0, 0]],
]

HR = ((Qr(2), Q1 + R), (Q1 - R, Qr(2)))
HD = (
    (Q1, -(Q1 + R) * F(1, 2)),
    (-(Q1 - R) * F(1, 2), Q1),
)
D = ((Q1, Q0), (Q0, Qr(-1)))
twoHD = tuple(tuple(Qr(2) * x for x in row) for row in HD)
assert mul(mul(adj(D), HR), D) == twoHD

S = ((Q1, Q1 + R), (Q0, Qr(-1)))
T = ((Q1, Q1), (Qr(-1), Q0))
assert mul(mul(adj(S), HR), S) == HR
assert mul(mul(adj(T), HR), T) == HR
G = close_group((S, T))
assert len(G) == 48

# Exhaust the full integral unitary group. A column v of a unitary matrix
# has v^* H_R v = 2. Since lambda_min(H_R)=2-sqrt(3),
# ||v||^2 <= 2/(2-sqrt(3)) = 4+2sqrt(3) < 8.
# For an entry a+b*r, |a+b*r|^2=a^2+2b^2, so |a|<=2, |b|<=1.
vals = [
    Qr(a, b)
    for a in range(-2, 3)
    for b in range(-1, 2)
    if a * a + 2 * b * b <= 7
]
norm2_vectors = [
    (x, y)
    for x in vals
    for y in vals
    if hpair((x, y), (x, y), HR) == Qr(2)
]
assert len(norm2_vectors) == 24

unitaries = set()
for c1 in norm2_vectors:
    for c2 in norm2_vectors:
        if hpair(c1, c2, HR) != Q1 + R:
            continue
        A = ((c1[0], c2[0]), (c1[1], c2[1]))
        assert mul(mul(adj(A), HR), A) == HR
        unitaries.add(A)

assert len(unitaries) == 48
assert unitaries == G

# All scaled source-to-retained principal-polarized CM isometries are A*D.
scaled = {mul(A, D) for A in G}
assert len(scaled) == 48
for P in scaled:
    assert mul(mul(adj(P), HR), P) == twoHD

# D is identity mod 2; the remaining 48 target automorphisms act as full S3 on W.
assert W_matrix(D) == ((1, 0), (0, 1))
perm_counts = {}
for A in G:
    p = W_perm(A)
    perm_counts[p] = perm_counts.get(p, 0) + 1
assert len(perm_counts) == 6
assert set(perm_counts.values()) == {8}

for src in LINE_VECTORS:
    counts = {"L1": 0, "L2": 0, "L3": 0}
    for A in G:
        counts[LINES[act2(W_matrix(A), src)]] += 1
    assert counts == {"L1": 16, "L2": 16, "L3": 16}

kernel = [A for A in G if W_perm(A) == ("L1", "L2", "L3")]
assert len(kernel) == 8
for line in ("L1", "L2", "L3"):
    idx = ("L1", "L2", "L3").index(line)
    stabilizer = [A for A in G if W_perm(A)[idx] == line]
    assert len(stabilizer) == 16

# The literal +r product has one fixed W-line, but its integral-unitary
# conjugacy class distributes that fixed line equally across all three lines.
STi = mul(S, inv2(T))
conjs = {mul(mul(A, STi), inv2(A)) for A in G}
assert len(conjs) == 6
fixed_counts = {"L1": 0, "L2": 0, "L3": 0}
for X in conjs:
    M = W_matrix(X)
    fixed = [LINES[v] for v in LINE_VECTORS if act2(M, v) == v]
    assert len(fixed) == 1
    fixed_counts[fixed[0]] += 1
assert fixed_counts == {"L1": 2, "L2": 2, "L3": 2}

assert cert["decision"]["absolute_W_line_identified"] is False
assert cert["decision"]["absolute_Q602_residue_identified"] is False
assert cert["decision"]["Q602_excluded"] is False
assert cert["decision"]["O210_excluded"] is False
assert cert["decision"]["stage32_main_credit"] is False
assert not any(cert["firewalls"].values())

print("PASS_STAGE32EX4_EX4_04_RETAINED_PPAV_CM_ANCHOR_SCRATCH")
print(f"certificate_canonical={EXPECTED}")
print("deraux_to_retained_one_map=D=diag(1,-1), D^*H_R D=2H_D")
print("full_Zr_principal_unitary_group=48, W_action=S3, kernel=8, line_stabilizer=16")
print("each_fixed_W_line_image_counts=L1:16,L2:16,L3:16")
print("STinv_conjugacy_fixed_lines=L1:2,L2:2,L3:2")
print("absolute_W_line=false absolute_residue=false Q602_excluded=false O210_excluded=false")
