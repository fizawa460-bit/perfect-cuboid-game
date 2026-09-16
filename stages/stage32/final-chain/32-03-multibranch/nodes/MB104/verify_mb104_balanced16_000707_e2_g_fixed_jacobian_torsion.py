#!/usr/bin/env python3
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
PASS = "PASS STAGE32_MB104_000707_E2_G_FIXED_JACOBIAN_TORSION_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-G-FIXED-JACOBIAN-TORSION.md",
        "3163ec6480041f6634bdff2ed8454bd99cb7e36b",
    ),
    "EXTERNAL_PRODUCT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXTERNAL-PRODUCT-PICARD-REDUCTION-CERTIFICATE.json",
        "8ee4c7a3b3f445c9f34cb7b37f55a22fd7e99a06",
    ),
    "SIX_BRANCH_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-SIX-BRANCH-HURWITZ-PASSPORT.md",
        "d421c11ecd6577234823b6e9604c8cc99ce48fec",
    ),
    "PRODUCT_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PRODUCT-CORRESPONDENCE-LINEARIZATION.md",
        "2c2db567db6a3c33762b2ff3d7f39f885a95b974",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def repo_root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mmul(a, b):
    req(len(a[0]) == len(b), "matrix dimension")
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def msub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def transpose(a):
    return [list(r) for r in zip(*a)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def add_g(a, b):
    return tuple((x + y) & 1 for x, y in zip(a, b))


def unit_diagonalize(a_in):
    """Use only unimodular integer row/column operations with unit pivots.

    Returns transformed matrix A, column transform T, its inverse Ti, and the
    number of unit pivots.  The explicit Ti updates make the quotient basis
    replay independent of any external Smith-normal-form package.
    """
    a = [row[:] for row in a_in]
    m, n = len(a), len(a[0])
    t = eye(n)
    ti = eye(n)
    rank = 0
    for k in range(min(m, n)):
        pos = None
        for i in range(k, m):
            for j in range(k, n):
                if abs(a[i][j]) == 1:
                    pos = (i, j)
                    break
            if pos is not None:
                break
        if pos is None:
            break
        i, j = pos
        a[k], a[i] = a[i], a[k]
        if j != k:
            for row in a:
                row[k], row[j] = row[j], row[k]
            for row in t:
                row[k], row[j] = row[j], row[k]
            ti[k], ti[j] = ti[j], ti[k]
        if a[k][k] == -1:
            a[k] = [-x for x in a[k]]

        for i2 in range(m):
            if i2 != k and a[i2][k]:
                q = a[i2][k]
                a[i2] = [a[i2][c] - q * a[k][c] for c in range(n)]

        for j2 in range(n):
            if j2 != k and a[k][j2]:
                q = a[k][j2]
                for i2 in range(m):
                    a[i2][j2] -= q * a[i2][k]
                for i2 in range(n):
                    t[i2][j2] -= q * t[i2][k]
                # inverse update for C^{-1}: row k <- row k + q row j2
                ti[k] = [ti[k][c] + q * ti[j2][c] for c in range(n)]
        rank += 1

    req(mmul(t, ti) == eye(n), "column transform right inverse")
    req(mmul(ti, t) == eye(n), "column transform left inverse")
    return a, t, ti, rank


def submatrix(a, r0, r1, c0, c1):
    return [row[c0:c1] for row in a[r0:r1]]


root = repo_root()
for name, (rel, expected) in LOCKS.items():
    p = root / rel
    req(p.is_file(), f"missing lock {name}: {rel}")
    got = git_blob_sha1(p)
    req(got == expected, f"SOURCE_LOCK_FAIL {name}: {got} != {expected}")

note = (root / LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
six_branch = (root / LOCKS["SIX_BRANCH_NOTE"][0]).read_text(encoding="utf-8")
product_note = (root / LOCKS["PRODUCT_NOTE"][0]).read_text(encoding="utf-8")
ext_cert = json.loads((root / LOCKS["EXTERNAL_PRODUCT_CERT"][0]).read_text(encoding="utf-8"))

req(ext_cert.get("active_leaf") == ACTIVE, "external-product active leaf")
req(ext_cert.get("scope", {}).get("case") == "e=2", "external-product e2 scope")
req(ext_cert.get("deduction", {}).get("factor_classes_G_invariant") is True, "factor G-invariance")
req(ext_cert.get("credit_firewall", {}).get("e2_closed") is False, "external-product e2 firewall")

for token in [
    "C8/G` is `P^1` with six order-two branch values, two for each of the three singular stabilizer types",
    "G ~= (Z/2)^3",
]:
    req(token in six_branch, f"six-branch token missing: {token}")

for token in [
    "G=(Z/2)^3",
    "The three singular involutions `s1,s2,s3` each have eight fixed points",
    "The other four nonidentity elements are fixed-point-free",
]:
    req(token in product_note, f"product-action token missing: {token}")

for token in [
    "J(C8)^G ~= (Z/2)^5",
    "|J(C8)^G| = 32",
    "32 * 32 = 1024",
    "No e=2 closure is claimed",
]:
    req(token in note, f"semantic token missing: {token}")

# ---------------------------------------------------------------------------
# Exact orbifold-cover / Reidemeister--Schreier replay.
# Re-coordinate the three independent singular involutions to the standard
# basis e1,e2,e3.  The six branch loops occur in equal-inertia pairs.
# ---------------------------------------------------------------------------
G = list(itertools.product([0, 1], repeat=3))
mon = {
    1: (1, 0, 0),
    2: (1, 0, 0),
    3: (0, 1, 0),
    4: (0, 1, 0),
    5: (0, 0, 1),
    6: (0, 0, 1),
}


def tword(g):
    out = []
    if g[0]:
        out.append(1)
    if g[1]:
        out.append(3)
    if g[2]:
        out.append(5)
    return out


def invword(w):
    return [-x for x in reversed(w)]


def free_reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


sword = {}
for g in G:
    for i in range(1, 7):
        gp = add_g(g, mon[i])
        sword[(g, i)] = free_reduce(tword(g) + [i] + invword(tword(gp)))

trivial = {k for k, w in sword.items() if not w}
gens = [k for g in G for k in [(g, i) for i in range(1, 7)] if k not in trivial]
index = {k: j for j, k in enumerate(gens)}
req(len(trivial) == 7, "seven trivial Schreier generators")
req(len(gens) == 41, "41 nontrivial Schreier generators")


def rewrite(word):
    cur = (0, 0, 0)
    out = [0] * len(gens)
    for letter in word:
        i = abs(letter)
        if letter > 0:
            key = (cur, i)
            if key in index:
                out[index[key]] += 1
            cur = add_g(cur, mon[i])
        else:
            new = add_g(cur, mon[i])
            key = (new, i)
            if key in index:
                out[index[key]] -= 1
            cur = new
    req(cur == (0, 0, 0), "rewritten word lies in kernel")
    return out


relators = [[i, i] for i in range(1, 7)] + [[1, 2, 3, 4, 5, 6]]
relations = []
for g in G:
    tg = tword(g)
    for r in relators:
        relations.append(rewrite(tg + r + invword(tg)))
req(len(relations) == 56, "56 Schreier relations")

red, t, ti, rel_rank = unit_diagonalize(relations)
req(rel_rank == 31, "31 primitive unit pivots")
req(all(red[i][j] == (1 if i == j else 0) for i in range(31) for j in range(41)), "relation I31 block")
req(all(red[i][j] == 0 for i in range(31, 56) for j in range(41)), "relation residual zero")
req(41 - rel_rank == 10, "genus-five H1 rank 10")


def action41(h):
    th = tword(h)
    return [rewrite(th + sword[key] + invword(th)) for key in gens]


q = {}
for h in G:
    m = action41(h)
    new = mmul(mmul(ti, m), t)
    req(all(new[i][j] == 0 for i in range(31) for j in range(31, 41)), f"relation submodule stable {h}")
    q[h] = submatrix(new, 31, 41, 31, 41)

for a in G:
    for b in G:
        req(mmul(q[a], q[b]) == q[add_g(a, b)], f"deck group law {a},{b}")

basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
req(trace(q[(0, 0, 0)]) == 10, "identity H1 trace")
for h in basis:
    req(trace(q[h]) == -6, f"singular H1 trace {h}")
for h in G:
    if h != (0, 0, 0) and h not in basis:
        req(trace(q[h]) == 2, f"free H1 trace {h}")

# ---------------------------------------------------------------------------
# Exact fixed torus.  For row-coordinate deck matrices Q, column coordinates
# satisfy (Q-I)^T v in Z^10.  The Smith factors are certified without an
# external SNF package: first split five unit factors, then divide the residual
# even block by two and split five more unit factors.
# ---------------------------------------------------------------------------
i10 = eye(10)
bmat = []
for h in basis:
    bmat.extend(transpose(msub(q[h], i10)))
req(len(bmat) == 30 and len(bmat[0]) == 10, "fixed matrix dimensions")

bred, _, _, first_units = unit_diagonalize(bmat)
req(first_units == 5, "five unit fixed-matrix factors")
req(all(bred[i][j] == (1 if i == j else 0) for i in range(5) for j in range(10)), "fixed I5 block")
req(all(bred[i][j] == 0 for i in range(5, 30) for j in range(5)), "fixed lower-left zero")
req(all(bred[i][j] % 2 == 0 for i in range(5, 30) for j in range(5, 10)), "residual fixed block even")

half = [[bred[i][j] // 2 for j in range(5, 10)] for i in range(5, 30)]
hred, _, _, second_units = unit_diagonalize(half)
req(second_units == 5, "five residual half-unit factors")
req(all(hred[i][j] == (1 if i == j else 0) for i in range(5) for j in range(5)), "residual half I5")
req(all(hred[i][j] == 0 for i in range(5, 25) for j in range(5)), "residual half zero")

# Therefore SNF(B)=diag(1^5,2^5), so the fixed real torus modulo the integral
# lattice is (Z/2)^5.
fixed_size = 2 ** 5
req(fixed_size == 32, "full-G fixed Jacobian size")
req(fixed_size * fixed_size == 1024, "ordered factor-pair count")

for forbidden in [
    "e2_closed: true",
    "receiver_credit: true",
    "theorem_credit: true",
    "endpoint_credit: true",
    "perfect_cuboid_nonexistence_claim: true",
]:
    req(forbidden not in note, f"forbidden credit token: {forbidden}")

print(PASS)
