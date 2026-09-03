#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
    return doc


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def block_diag(g):
    z = [[0] * 4 for _ in range(4)]
    return [g[i] + z[i] for i in range(4)] + [z[i] + g[i] for i in range(4)]


def vec_to_bits(v):
    return sum((int(v[i]) & 1) << i for i in range(len(v)))


def bits_to_vec(bits: int, n: int = 8):
    return [(bits >> i) & 1 for i in range(n)]


def matvec_mod2(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) & 1 for i in range(len(a))]


def rank_mod2(rows):
    a = [row[:] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c] & 1), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(m):
            if i != r and (a[i][c] & 1):
                a[i] = [(x ^ y) for x, y in zip(a[i], a[r])]
        r += 1
    return r


def t_matrix_mod2(bits: int):
    x = bits_to_vec(bits)
    entries = [(x[0], x[1]), (x[2], x[3]), (x[4], x[5]), (x[6], x[7])]
    out = [[0] * 4 for _ in range(4)]
    # module basis: e1,e2,eps*e1,eps*e2; eps^2=0
    for j in range(4):
        q = [0, 0, 0, 0]
        q[j] = 1
        c, d = q[:2], q[2:]
        oc, od = [0, 0], [0, 0]
        for i in range(2):
            for k in range(2):
                aa, bb = entries[2 * i + k]
                oc[i] ^= aa & c[k]
                od[i] ^= (aa & d[k]) ^ (bb & c[k])
        col = [oc[0], oc[1], od[0], od[1]]
        for i in range(4):
            out[i][j] = col[i]
    return out


def dual_add(u, v):
    return (u[0] ^ v[0], u[1] ^ v[1])


def dual_mul(u, v):
    return (u[0] & v[0], (u[0] & v[1]) ^ (u[1] & v[0]))


def dual_matmul(a, b):
    out = [[(0, 0), (0, 0)], [(0, 0), (0, 0)]]
    for i in range(2):
        for j in range(2):
            s = (0, 0)
            for k in range(2):
                s = dual_add(s, dual_mul(a[i][k], b[k][j]))
            out[i][j] = s
    return out


def dagger_bits(bits: int) -> int:
    x = bits_to_vec(bits)
    t = [[(x[0], x[1]), (x[2], x[3])], [(x[4], x[5]), (x[6], x[7])]]
    tt = [[t[j][i] for j in range(2)] for i in range(2)]
    # H mod 2 = H^{-1} mod 2 = [[0,1+eps],[1+eps,0]].
    h = [[(0, 0), (1, 1)], [(1, 1), (0, 0)]]
    d = dual_matmul(dual_matmul(h, tt), h)
    flat = [d[0][0], d[0][1], d[1][0], d[1][1]]
    coords = []
    for aa, bb in flat:
        coords.extend([aa, bb])
    return vec_to_bits(coords)


def common_fixed_dim(bits: int) -> int:
    t = t_matrix_mod2(bits)
    td = t_matrix_mod2(dagger_bits(bits))
    rows = []
    for m in (t, td):
        for i in range(4):
            rows.append([m[i][j] ^ (1 if i == j else 0) for j in range(4)])
    return 4 - rank_mod2(rows)


def d4_counts(max_norm: int):
    # Standard D4 = {z in Z^4 : sum z_i even}, with simple roots
    # a1=e1-e2, a2=e2-e3, a3=e3-e4, a4=e3+e4.
    counts = [[0] * 16 for _ in range(max_norm + 1)]
    r = range(-math.isqrt(max_norm), math.isqrt(max_norm) + 1)
    for z1 in r:
        n1 = z1 * z1
        for z2 in r:
            n2 = n1 + z2 * z2
            if n2 > max_norm:
                continue
            y1, y2 = z1, z1 + z2
            for z3 in r:
                n3 = n2 + z3 * z3
                if n3 > max_norm:
                    continue
                for z4 in r:
                    n = n3 + z4 * z4
                    if n > max_norm or ((z1 + z2 + z3 + z4) & 1):
                        continue
                    y4 = (z3 + z4 + y2) // 2
                    y3 = y4 - z4
                    residue = (y1 & 1) | ((y2 & 1) << 1) | ((y3 & 1) << 2) | ((y4 & 1) << 3)
                    counts[n][residue] += 1
    return counts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()

    cert_path = ROOT / args.check
    cert = json.loads(cert_path.read_text())
    assert cert["schema"] == "STAGE32_POST1503_O210_Q4_RELATIVE_V4_TORSOR_MOD2_COUPLING_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    assert cert["canonical_sha256_without_this_field"] == "312aa78d5a89c7c4d48e0afc2988e5ecf2b605d68820d123fea8ca8c48f6d669"

    locks = cert["source_locks"]
    repair = load_lock(locks["audited_rosati_repair"])
    x8 = load_lock(locks["x8_v4_quotient"])
    d4 = load_lock(locks["d4d4_trace"])
    principal = load_lock(locks["principal_rosati"])
    note_path = ROOT / locks["source_note"]["path"]
    assert note_path.is_file()
    assert blob_sha1(note_path) == locks["source_note"]["blob_sha1"]
    note = note_path.read_text()

    # Audited repaired target and exact Q=602 boundary.
    assert repair["fixed_target"]["O"] == 210
    assert repair["corrected_rosati_arithmetic"]["Gamma_square"] == 15806
    assert repair["corrected_rosati_arithmetic"]["sigma"] == 1204
    assert repair["corrected_rosati_arithmetic"]["Q"] == 602
    assert repair["decision"]["O210_excluded"] is False

    # Relative V4 geometry used by the new coupling theorem.
    assert x8["exact_group_checks"]["Gamma_prime_4_over_Gamma8_order"] == 4
    assert x8["exact_group_checks"]["Gamma_prime_4_over_Gamma8_free_on_X8"] is True
    assert x8["quotient_geometry"]["X8_to_C0_degree"] == 4
    assert x8["quotient_geometry"]["X8_to_C0_etale"] is True
    pm = d4["pair_map_birationality"]
    assert pm["cover"] == "X=P/H_diag -> C0 x C0=P/(H x H)"
    assert pm["deck_group"] == "(H x H)/H_diag ~= V4"
    assert pm["finite_etale_degree"] == 4
    assert pm["projection_degrees"] == [105, 81]
    assert pm["pair_map_birational"] is True

    for needle in [
        "f1^* Z ~= f2^* Z",
        "W := span_F2",
        "T_12(alpha) = f2_* f2^*(alpha) = 81 alpha = alpha",
        "T_21(alpha) = f1_* f1^*(alpha) = 105 alpha = alpha",
        "common two-dimensional fixed subspace",
        "28` residue classes",
    ]:
        assert needle in note, needle

    # Exact retained Rosati lattice and D4 + D4 change of basis.
    a = d4["trace_lattice"]["gram_matrix"]
    columns = d4["trace_lattice"]["unimodular_change_of_basis_columns"]
    u = transpose(columns)
    g = d4["trace_lattice"]["d4_gram"]
    assert matmul(transpose(u), matmul(a, u)) == block_diag(g)
    assert d4["trace_lattice"]["isometry"] == "U^t*A*U = D4 direct-sum D4"

    # Principal polarization reduction modulo 2.
    assert principal["principal_polarization"]["hermitian_matrix"] == [["2", "1+r"], ["1-r", "2"]]
    assert principal["rosati"]["H_inverse"] == [["2", "-1-r"], ["-1+r", "2"]]

    target = 602
    counts = d4_counts(target)
    xcounts = {}
    for n in range(target + 1):
        for r1, c1 in enumerate(counts[n]):
            if not c1:
                continue
            for r2, c2 in enumerate(counts[target - n]):
                if not c2:
                    continue
                ybits = r1 | (r2 << 4)
                xbits = vec_to_bits(matvec_mod2(u, bits_to_vec(ybits)))
                xcounts[xbits] = xcounts.get(xbits, 0) + c1 * c2

    dist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    survivors = []
    survivor_vectors = 0
    for bits, count in sorted(xcounts.items()):
        dim = common_fixed_dim(bits)
        dist[dim] += 1
        if dim >= 2:
            survivors.append(bits)
            survivor_vectors += count

    total_vectors = sum(xcounts.values())
    expected_survivors = [20,60,65,67,69,73,75,77,81,97,99,105,107,113,150,190,193,195,199,201,203,207,211,225,227,233,235,243]
    assert len(xcounts) == 96
    assert total_vectors == 1312836096
    assert dist == {0: 32, 1: 36, 2: 24, 3: 3, 4: 1}
    assert survivors == expected_survivors
    assert survivor_vectors == 382918016

    pre = cert["q602_mod2_preflight"]
    assert pre["Q"] == target
    assert pre["realized_residue_class_count"] == len(xcounts)
    assert pre["total_integral_shell_count"] == total_vectors
    assert pre["common_fixed_dimension_distribution"] == {str(k): v for k, v in dist.items()}
    assert pre["surviving_residue_class_count"] == len(survivors) == 28
    assert pre["surviving_integral_vector_count"] == survivor_vectors
    assert pre["surviving_residue_classes_decimal"] == survivors
    assert pre["surviving_residue_classes_hex"] == [f"0x{x:02x}" for x in survivors]
    assert pre["removed_residue_class_count"] == 68
    assert pre["exclusion"] is False

    coupling = cert["relative_v4_coupling"]
    assert coupling["W_dimension"] == 2
    assert coupling["projection_degrees"] == [105, 81]
    assert "Fix(T) intersect Fix(T^dagger)" in coupling["rosati_form"]

    dec = cert["decision"]
    assert dec["new_source_locked_coupling_evidence_created"] is True
    assert dec["generic_common_cover_inference_reopened"] is False
    assert dec["Q602_excluded"] is False
    assert dec["O210_excluded"] is False
    assert dec["O212_plus_authorized"] is False
    assert dec["next_exact_leaf"] == "O210_Q4_IDENTIFY_EXACT_X8_V4_TORSOR_PLANE_W_IN_BOLZA_J2"

    print("PASS_POST1503_RELATIVE_V4_MOD2_COUPLING_Q602_RESIDUES_96_TO_28_NONEXCLUSION")


if __name__ == "__main__":
    main()
