#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECTED_CANONICAL = "4925170377af7c77a97d36e562cdabd58241030f22a9644f1fa2a8ee627002c3"
EXPECTED_TRACE_VALUES = [-68,-60,-52,-44,-36,-28,-20,-12,-4,4,12,20,28,36,44,52,60,68]
EXPECTED_TRACE_COUNTS = [512,50688,205568,451200,716800,1036288,1320448,1442560,1613312,1613312,1442560,1320448,1036288,716800,451200,205568,50688,512]
EXPECTED_DIAGONAL = [118,126,134,142,150,158,166,174,182,190,198,206,214,222,230,238,246,254]


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json(lock: dict) -> dict:
    p = ROOT / lock["path"]
    assert p.is_file() and blob_sha1(p) == lock["blob_sha1"], p
    d = json.loads(p.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(d) == lock["canonical_sha256"], p
    return d


def transpose(M):
    return [list(x) for x in zip(*M)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def mv_mod2(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) & 1 for i in range(len(A))]


def inv_mod2(A):
    n = len(A)
    X = [[A[i][j] & 1 for j in range(n)] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    r = 0
    for c in range(n):
        p = next(i for i in range(r, n) if X[i][c])
        X[r], X[p] = X[p], X[r]
        for i in range(n):
            if i != r and X[i][c]:
                X[i] = [a ^ b for a, b in zip(X[i], X[r])]
        r += 1
    return [row[n:] for row in X]


def d4_half(v):
    a,b,c,d = v
    return a*a + b*b + c*c + d*d - b*(a+c+d)


def enumerate_block(parity, with_trace):
    # If m<=301, completed squares give |b|<35 and |a|,|c|,|d|<=35.
    out = defaultdict(Counter) if with_trace else defaultdict(int)
    for a in range(-35, 36):
        if (a & 1) != parity[0]: continue
        for b in range(-34, 35):
            if (b & 1) != parity[1]: continue
            for c in range(-35, 36):
                if (c & 1) != parity[2]: continue
                for d in range(-35, 36):
                    if (d & 1) != parity[3]: continue
                    m = d4_half((a,b,c,d))
                    if m > 301: continue
                    if with_trace:
                        out[m][-2*b + 4*d] += 1
                    else:
                        out[m] += 1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    cert = json.loads((ROOT / args.check).read_text())
    assert cert["schema"] == "STAGE32_POST1518_O210_Q602_RESIDUE73_TRACE_SPECTRUM_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    locks = cert["source_locks"]
    gauge = load_json(locks["audited_marked_gauge_orbit"])
    tr = load_json(locks["d4d4_trace_reduction"])
    note = ROOT / locks["source_note"]["path"]
    assert note.is_file() and blob_sha1(note) == locks["source_note"]["blob_sha1"]
    assert locks["audited_marked_gauge_orbit"]["hostile_reaudit_review"] == 5108049622
    assert gauge["marked_gauge_normalization"]["canonical_residue"] == 73
    assert gauge["decision"]["Q602_excluded"] is False
    ext = locks["correspondence_trace_external"]
    assert ext["locator"] == "Chapter 10, Section 10.1, equation (10.1)"
    assert ext["exact_supported_fact"] == "t(D)=d1+d2-(D,Delta)=tr((u_D)_r)"

    tl = tr["trace_lattice"]
    assert tl["coordinate_order"] == cert["audited_input"]["coordinate_order"]
    A = tl["gram_matrix"]
    # JSON records columns; turn them into the matrix U.
    U = transpose(tl["unimodular_change_of_basis_columns"])
    D4 = tl["d4_gram"]
    zero = [[0]*4 for _ in range(4)]
    target = [D4[i] + zero[i] for i in range(4)] + [zero[i] + D4[i] for i in range(4)]
    assert mm(mm(transpose(U), A), U) == target

    residue = cert["audited_input"]["canonical_residue_decimal"]
    xpar = [(residue >> i) & 1 for i in range(8)]
    assert xpar == cert["audited_input"]["x_parity"] == [1,0,0,1,0,0,1,0]
    ypar = mv_mod2(inv_mod2(U), xpar)
    assert ypar == cert["d4d4_reduction"]["y_parity"] == [1,0,0,0,1,0,1,0]

    # Tr_Q(T)=2*(t11.a+t22.a), pulled through x=U*y.
    ell = [2,0,0,0,0,0,2,0]
    ell_y = [sum(ell[i] * U[i][j] for i in range(8)) for j in range(8)]
    assert ell_y == [0,-2,0,4,0,0,0,0]

    # Pure congruence proof: m2=2 mod4, m1=3 mod4, hence y2=2 mod4 and trace=4 mod8.
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    if [a&1,b&1,c&1,d&1] == [1,0,1,0]:
                        assert d4_half((a,b,c,d)) % 4 == 2
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    if [a&1,b&1,c&1,d&1] == [1,0,0,0] and d4_half((a,b,c,d)) % 4 == 3:
                        assert b % 4 == 2 and (-2*b + 4*d) % 8 == 4
    assert cert["rational_trace"]["trace_mod8"] == 4
    assert cert["diagonal_intersection"]["mod8"] == (186 - 4) % 8 == 6

    # Exact 4+4 shell spectrum.
    b1 = enumerate_block((1,0,0,0), True)
    b2 = enumerate_block((1,0,1,0), False)
    trace_counts = Counter()
    for m1, tc in b1.items():
        n2 = b2.get(301-m1, 0)
        if not n2: continue
        for t, n1 in tc.items():
            trace_counts[t] += n1*n2
    values = sorted(trace_counts)
    counts = [trace_counts[t] for t in values]
    assert values == EXPECTED_TRACE_VALUES
    assert counts == EXPECTED_TRACE_COUNTS
    assert sum(counts) == 13674752
    assert all(t % 8 == 4 for t in values)
    diag = sorted(186-t for t in values)
    assert diag == EXPECTED_DIAGONAL and all(x % 8 == 6 for x in diag)

    spec = cert["exact_spectrum"]
    assert spec["residue73_q602_vector_count"] == sum(counts)
    assert spec["trace_values"] == values
    assert spec["trace_counts"] == [{"trace":t,"count":trace_counts[t]} for t in values]
    assert spec["diagonal_intersection_values"] == diag

    dec, fw = cert["decision"], cert["firewalls"]
    assert dec["arithmetic_exclusion"] is False and dec["Q602_excluded"] is False and dec["O210_excluded"] is False
    assert dec["O212_plus_authorized"] is False and dec["promotion_requires_hostile_audit"] is True
    assert fw["geometric_realization_of_lattice_points_inferred"] is False
    assert fw["old_rosati_nonexclusion_reopened"] is False and fw["locator_search_reopened"] is False
    assert fw["heavy_compute_authorized"] is False and fw["receiver_credit"] is False and fw["theorem_credit"] is False
    print("PASS: Stage32 canonical residue 73 at Q602 has exact trace spectrum +/-{4,12,...,68}; Tr=4 mod8 and (Gamma,Delta)=6 mod8; no O210 exclusion.")


if __name__ == "__main__":
    main()
