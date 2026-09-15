#!/usr/bin/env python3
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
MATRIX_SHA256 = "d15f8d93410f8d448cb92de3be81e3a8a01dcc34ec39ddb0c37a78126b0ab3d4"
WITNESS_ROWS = [
    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
    25,26,27,28,33,41,49,53,54,55,56,61,69,77,89,90,91,92,97,
    98,99,100,107,115,123,131,135,136,137,138,331,332,333,334,
    335,339,343,363,395,396,397,399,403,
]
LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-H1-TORSION-KILL.md",
        "8ab59d0582e3a0c33c867244f00d2ab8f23c9346",
    ),
    "SOURCE_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/ARMSTRONG-FIBER-PRODUCT-H1-SOURCE-NOTE.md",
        "ff1581420337745b1718a0b55b2d8049244277de",
    ),
    "HURWITZ": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY.md",
        "c91f97b738faa66a49a068824f9b8c3739d4a8fa",
    ),
    "INTERMEDIATE_H_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL-CERTIFICATE.json",
        "983dc26d0fbed5f524f2bfda5f5bda86a7d8f890",
    ),
    "IRREGULARITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-IRREGULARITY-TORSION-REFINEMENT-CERTIFICATE.json",
        "4f0e8872ad03427348b0f16d1cdd14711e67d4b1",
    ),
    "ANTIINVARIANT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ANTIINVARIANT-CLASS-DECOMPOSITION-CERTIFICATE.json",
        "727e332aa551313f7fb127c77145dc24535b6080",
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


def invword(w):
    return [-a for a in reversed(w)]


# Base generators: 1..8=x_i, 9..16=y_i.
# H=(Z/2)^2 is encoded as bit values 0,1,2,3.
def h_image(g):
    if 1 <= g <= 4 or 9 <= g <= 12:
        return 1
    if 5 <= g <= 8 or 13 <= g <= 16:
        return 2
    raise AssertionError(g)


T = {0: [], 1: [1], 2: [5], 3: [1, 5]}
TY = {0: [], 1: [9], 2: [13], 3: [9, 13]}
KEYS = [(c, g) for c in range(4) for g in range(1, 17)]
KEY_INDEX = {k: i for i, k in enumerate(KEYS)}


def reduce_free(w):
    st = []
    for a in w:
        if st and st[-1] == -a:
            st.pop()
        else:
            st.append(a)
    return st


def coset_word(w):
    c = 0
    for a in w:
        c ^= h_image(abs(a))
    return c


def rewrite_coeffs(w):
    """Abelianized Reidemeister-Schreier rewrite for a word in F=ker(psi)."""
    c = 0
    out = [0] * len(KEYS)
    for a in w:
        g = abs(a)
        if a > 0:
            out[KEY_INDEX[(c, g)]] += 1
            c ^= h_image(g)
        else:
            c2 = c ^ h_image(g)
            out[KEY_INDEX[(c2, g)]] -= 1
            c = c2
    req(c == 0, "rewrite word not in fiber-product subgroup")
    return out


def relation_matrix():
    rows = []

    # Trivial Schreier generators for the chosen transversal.
    for c, g in KEYS:
        cp = c ^ h_image(g)
        sw = reduce_free(T[c] + [g] + invword(T[cp]))
        if not sw:
            row = [0] * len(KEYS)
            row[KEY_INDEX[(c, g)]] = 1
            rows.append(row)

    # Delta x Delta relators.
    rels = []
    for g in range(1, 17):
        rels.append([g, g])
    rels.append(list(range(1, 9)))
    rels.append(list(range(9, 17)))
    for i in range(1, 9):
        for j in range(9, 17):
            rels.append([i, j, -i, -j])

    for c in range(4):
        for rel in rels:
            w = T[c] + rel + invword(T[c])
            req(coset_word(w) == 0, "bad Schreier relator coset")
            row = rewrite_coeffs(w)
            if any(row):
                rows.append(row)

    req(len(rows) == 331, f"unexpected pre-Armstrong row count {len(rows)}")

    # Armstrong fixed-point relations.  For each inertia type, each pair of
    # cone generators and each relative conjugator H-coset is represented.
    for xs, ys in ((range(1, 5), range(9, 13)), (range(5, 9), range(13, 17))):
        for delta in range(4):
            b = TY[delta]
            for i in xs:
                for j in ys:
                    w = [i] + b + [j] + invword(b)
                    req(coset_word(w) == 0, "bad fixed-pair coset")
                    row = rewrite_coeffs(w)
                    req(any(row), "unexpected zero fixed-pair relation")
                    rows.append(row)

    req(len(rows) == 459, f"unexpected final row count {len(rows)}")
    return rows


def bareiss_det(a):
    """Exact fraction-free determinant; row swaps only, no floating point."""
    a = [list(map(int, row)) for row in a]
    n = len(a)
    req(all(len(row) == n for row in a), "determinant matrix not square")
    sign = 1
    prev = 1
    for k in range(n - 1):
        pivot = k
        while pivot < n and a[pivot][k] == 0:
            pivot += 1
        if pivot == n:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pk = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pk - a[i][k] * a[k][j]
                req(num % prev == 0, "Bareiss non-exact division")
                a[i][j] = num // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pk
    return sign * a[n - 1][n - 1]


def main():
    root = repo_root()
    for key, (rel, want) in LOCKS.items():
        p = root / rel
        req(p.is_file(), f"missing source {key}")
        req(git_blob_sha1(p) == want, f"SOURCE_LOCK_FAIL {key}")

    rows = relation_matrix()
    canonical = "\n".join(",".join(map(str, row)) for row in rows).encode()
    req(hashlib.sha256(canonical).hexdigest() == MATRIX_SHA256, "relation matrix identity")

    req(len(WITNESS_ROWS) == 64 and len(set(WITNESS_ROWS)) == 64, "witness row set")
    minor = [rows[i] for i in WITNESS_ROWS]
    det = bareiss_det(minor)
    req(det == 1, f"unimodular witness determinant {det}")

    # A unimodular 64x64 minor means the 459 relation rows generate Z^64.
    # Thus the abelianization after Armstrong fixed-point normal closure is zero.
    print("PASS STAGE32_MB104_000707_E2_AMBIENT_H1_TORSION_KILL_V1")
    print("rows=459 vars=64 witness_det=1 H1(X_H,Z)=0 => H1(Y,Z)=0 => Pic^tau(Y)=0 => w~0")
    print("conductor transition open; e2 open; credit 0")


if __name__ == "__main__":
    main()
