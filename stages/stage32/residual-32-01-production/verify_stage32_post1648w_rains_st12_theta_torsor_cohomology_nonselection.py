#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

CERT_PATH = HERE / "post1648w-rains-st12-theta-torsor-cohomology-nonselection.json"
EXPECTED_CERT = "af2fa5b0f5e64a33040f2135015745aeb22ea7f94a1c454730e00bab7a4c3aad"


def canonical_sha(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_locked(lock: dict) -> dict:
    p = ROOT / lock["path"]
    assert p.is_file(), p
    if "git_blob_sha1" in lock:
        assert blob_sha1(p) == lock["git_blob_sha1"]
    doc = json.loads(p.read_text(encoding="utf-8"))
    if "canonical_sha256" in lock:
        assert canonical_sha(doc) == lock["canonical_sha256"]
        assert doc["canonical_sha256_without_this_field"] == lock["canonical_sha256"]
    return doc


def addv(a, b):
    return tuple((x ^ y) for x, y in zip(a, b))


def mat_vec(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(4)) & 1 for i in range(4))


def mat_mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) & 1 for j in range(4)) for i in range(4))


I = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))


def mat_pow(A, n):
    out = I
    for _ in range(n):
        out = mat_mul(out, A)
    return out


def group_close(gens):
    seen = {I}
    q = [I]
    while q:
        X = q.pop()
        for g in gens:
            Y = mat_mul(X, g)
            if Y not in seen:
                seen.add(Y)
                q.append(Y)
    return seen


def rank_f2(rows):
    A = [list(map(lambda x: x & 1, row)) for row in rows]
    if not A:
        return 0
    nr, nc = len(A), len(A[0])
    r = 0
    for c in range(nc):
        p = next((i for i in range(r, nr) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(nr):
            if i != r and A[i][c]:
                A[i] = [x ^ y for x, y in zip(A[i], A[r])]
        r += 1
    return r


def qr_entry(x):
    assert isinstance(x, list) and len(x) == 2
    return int(x[0]), int(x[1])


def real_matrix_mod2(M):
    alpha, beta = qr_entry(M[0][0]), qr_entry(M[0][1])
    gamma, delta = qr_entry(M[1][0]), qr_entry(M[1][1])
    aa, ab = alpha
    ba, bb = beta
    ca, cb = gamma
    da, db = delta
    R = [
        [aa, ba, -2 * ab, -2 * bb],
        [ca, da, -2 * cb, -2 * db],
        [ab, bb, aa, ba],
        [cb, db, ca, da],
    ]
    return tuple(tuple(x & 1 for x in row) for row in R)


def main():
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    assert canonical_sha(cert) == EXPECTED_CERT
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT

    V = load_locked(cert["source_locks"]["post1648V"])
    J = load_locked(cert["source_locks"]["post1648J"])
    note_path = ROOT / cert["source_locks"]["source_note"]["path"]
    assert blob_sha1(note_path) == cert["source_locks"]["source_note"]["git_blob_sha1"]

    assert V["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
    assert V["decision"]["survivors_current_credit"] == [73, 97, 235]

    tgt = J["target_named_generator_trace_test"]
    S = real_matrix_mod2(tgt["S_equals_b4"])
    T = real_matrix_mod2(tgt["T_equals_minus_b3"])

    expected_S = (
        (1, 1, 0, 0),
        (0, 1, 0, 0),
        (0, 1, 1, 1),
        (0, 0, 0, 1),
    )
    expected_T = (
        (1, 1, 0, 0),
        (1, 0, 0, 0),
        (0, 0, 1, 1),
        (0, 0, 1, 0),
    )
    assert S == expected_S and T == expected_T
    ST = mat_mul(S, T)
    assert mat_pow(S, 2) == I
    assert mat_pow(T, 3) == I
    assert mat_pow(ST, 4) == I
    assert len(group_close((S, T))) == 24

    vecs = [tuple(v) for v in itertools.product((0, 1), repeat=4)]
    zero = (0, 0, 0, 0)

    def cocycle_ok(a, b):
        if addv(a, mat_vec(S, a)) != zero:
            return False
        if addv(addv(b, mat_vec(T, b)), mat_vec(mat_pow(T, 2), b)) != zero:
            return False
        c = addv(a, mat_vec(S, b))
        acc = zero
        for k in range(4):
            acc = addv(acc, mat_vec(mat_pow(ST, k), c))
        return acc == zero

    Z = {(a, b) for a in vecs for b in vecs if cocycle_ok(a, b)}
    assert len(Z) == 32

    B = set()
    for v in vecs:
        a = addv(v, mat_vec(S, v))
        b = addv(v, mat_vec(T, v))
        B.add((a, b))
    assert len(B) == 16
    assert B <= Z

    nonzero = Z - B
    assert len(nonzero) == 16

    IT_rows = [[I[i][j] ^ T[i][j] for j in range(4)] for i in range(4)]
    assert rank_f2(IT_rows) == 4

    t_components = {b for _, b in nonzero}
    assert t_components == set(vecs)

    W = {
        "L1": (0, 0, 1, 0),
        "L2": (0, 0, 0, 1),
        "L3": (0, 0, 1, 1),
    }
    assert set(W.values()) <= t_components

    calc = cert["H1_exact_calculation"]
    assert cert["retained_mod2_action"]["quotient_group_order_on_A2"] == 24
    assert calc["constraint_rank"] == 3
    assert calc["Z1_dimension"] == 5 and calc["Z1_count"] == 32
    assert calc["B1_dimension"] == 4 and calc["B1_count"] == 16
    assert calc["H1_dimension"] == 1 and calc["H1_count"] == 2
    assert calc["unique_nonzero_class_representative_count"] == 16
    assert calc["I_plus_T_rank"] == 4 and calc["I_plus_T_invertible"] is True
    assert calc["nonzero_class_T_component_range"] == "ALL_16_VECTORS_OF_A2"

    sem = cert["semantic_boundary"]
    assert sem["distinguished_theta_characteristic_point_obtained"] is False
    assert sem["distinguished_semicharacter_in_retained_basis_obtained"] is False
    assert sem["distinguished_cocycle_representative_obtained"] is False

    dec = cert["decision"]
    assert dec["rains_natural_theta_torsor_class_materialized"] is True
    assert dec["rains_theta_torsor_route_selects_absolute_W_line"] is False
    assert dec["explicit_target_half_characteristic_or_semicharacter_materialized"] is False
    assert dec["absolute_delta0inf_retained_W_line_identified"] is False
    assert dec["survivors_current_credit"] == [73, 97, 235]
    assert dec["Q602_excluded"] is False
    assert dec["O210_excluded"] is False
    assert dec["O212_plus_advance_allowed"] is False
    assert not any(cert["firewalls"].values())

    print("POST1648W_RAINS_ST12_THETA_TORSOR_COHOMOLOGY_NONSELECTION_COMPLETE")
    print(f"certificate_canonical={EXPECTED_CERT}")
    print("target_mod2_group_order=24 H1_dim=1 Z1=32 B1=16 nonzero_class_reps=16")
    print("I_plus_T_rank=4 nonzero_class_T_components=all_16_A2_vectors")
    print("retained_W_lines_seen=L1,L2,L3")
    print("absolute_delta0inf_retained_W_line_identified=false")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")


if __name__ == "__main__":
    main()
