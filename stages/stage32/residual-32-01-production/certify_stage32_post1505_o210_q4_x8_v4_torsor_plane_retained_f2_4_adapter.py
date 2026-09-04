#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECTED_CANONICAL = "eab4d86ffe89ff0e87d197cffb34e8b556ae530cab826dab34c1007664a4af28"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
    return doc


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def deriv(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


def add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def neg(a):
    return [-x for x in a]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def bracket(a, b):
    return add(mul(deriv(a), b), neg(mul(deriv(b), a)))


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def matvec_mod2(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) & 1 for i in range(len(a))]


def bits_to_vec(bits: int, n: int = 8):
    return [(bits >> i) & 1 for i in range(n)]


def vec_to_bits(v):
    return sum((int(v[i]) & 1) << i for i in range(len(v)))


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


def t_matrix_mod2(bits: int):
    x = bits_to_vec(bits)
    entries = [(x[0], x[1]), (x[2], x[3]), (x[4], x[5]), (x[6], x[7])]
    out = [[0] * 4 for _ in range(4)]
    # Exact retained module order from post1503: e1,e2,eps*e1,eps*e2.
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


def dagger_bits(bits: int) -> int:
    x = bits_to_vec(bits)
    t = [[(x[0], x[1]), (x[2], x[3])], [(x[4], x[5]), (x[6], x[7])]]
    tt = [[t[j][i] for j in range(2)] for i in range(2)]
    h = [[(0, 0), (1, 1)], [(1, 1), (0, 0)]]
    d = dual_matmul(dual_matmul(h, tt), h)
    flat = [d[0][0], d[0][1], d[1][0], d[1][1]]
    coords = []
    for aa, bb in flat:
        coords.extend([aa, bb])
    return vec_to_bits(coords)


def fixes_w(bits: int, w_basis):
    t = t_matrix_mod2(bits)
    td = t_matrix_mod2(dagger_bits(bits))
    return all(matvec_mod2(t, w) == w and matvec_mod2(td, w) == w for w in w_basis)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()

    cert_path = ROOT / args.check
    cert = json.loads(cert_path.read_text())
    assert cert["schema"] == "STAGE32_POST1505_O210_Q4_X8_V4_TORSOR_PLANE_RETAINED_F2_4_ADAPTER_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    locks = cert["source_locks"]
    abstract_w = load_json_lock(locks["audited_abstract_W"])
    principal = load_json_lock(locks["principal_rosati"])
    upstream = load_json_lock(locks["upstream_relative_v4_coupling"])

    note_path = ROOT / locks["source_note"]["path"]
    assert note_path.is_file()
    assert blob_sha1(note_path) == locks["source_note"]["blob_sha1"]
    note = note_path.read_text()

    # Audited W and retained CM/basis inputs.
    assert locks["audited_abstract_W"]["hostile_reaudit_review"] == 5099888513
    assert abstract_w["torsor_plane"]["retained_F2_4_coordinates_identified"] is False
    assert abstract_w["torsor_plane"]["richelot_kernel_for_factorization"] is True
    assert abstract_w["weierstrass_model"]["factorization"] == "x^5-x = x*(x^2-1)*(x^2+1)"
    assert principal["quadratic_order"]["relation"] == "r^2=-2"
    assert principal["principal_polarization"]["riemann_form_basis"] == ["e1", "e2", "r*e1", "r*e2"]

    # Exact self-Richelot calculation, with coefficient arrays in ascending order.
    p = [0, 1]       # x
    q = [-1, 0, 1]  # x^2 - 1
    s = [1, 0, 1]   # x^2 + 1
    coeff_matrix = [
        [p[0], q[0], s[0]],
        [p[1], q[1], s[1]],
        [0, q[2], s[2]],
    ]
    delta = det3(coeff_matrix)
    assert delta == 2
    b_qs = bracket(q, s)
    b_sp = bracket(s, p)
    b_pq = bracket(p, q)
    assert b_qs == [0, 4]
    assert b_sp == q
    assert b_pq == neg(s)
    f = mul(mul(p, q), s)
    numerator = mul(mul(b_qs, b_sp), b_pq)
    assert numerator == [-4 * x for x in f]  # 4*Delta*(-1/2) = -4
    rc = cert["self_richelot_calculation"]
    assert rc["Delta"] == delta
    assert rc["fhat_over_f"] == "-1/2"
    assert rc["cm_relation"] == "r^2=-2"
    assert rc["curve_isomorphism"] == "iota:(x,yhat)->(x,r*yhat)"
    assert rc["iota_differential_scalar"] == "1/r"
    assert rc["richelot_analytic_scalar"] == "1"
    assert rc["transported_self_endomorphism"] == "[r]"
    assert rc["kernel_equals_audited_W"] is True

    for needle in [
        "fhat = -(1/2) p q s",
        "rho := R o iota_*^{-1}",
        "W = ker([r] : J(C0) -> J(C0))",
        "W = span_F2{(0,0,1,0),(0,0,0,1)}",
    ]:
        assert needle in note, needle

    # Retained lattice multiplication by r.
    m_r = [
        [0, 0, -2, 0],
        [0, 0, 0, -2],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]
    m_r_mod2 = [[x & 1 for x in row] for row in m_r]
    adapter = cert["retained_F2_4_adapter"]
    assert adapter["ordered_basis"] == ["e1", "e2", "r*e1", "r*e2"]
    assert adapter["multiplication_by_r_matrix"] == m_r
    assert adapter["multiplication_by_r_mod2"] == m_r_mod2

    kernel = []
    for bits in range(16):
        v = bits_to_vec(bits, 4)
        if matvec_mod2(m_r_mod2, v) == [0, 0, 0, 0]:
            kernel.append(v)
    expected_kernel = [[0,0,0,0],[0,0,1,0],[0,0,0,1],[0,0,1,1]]
    assert kernel == expected_kernel
    w_basis = adapter["W_basis_vectors"]
    assert w_basis == [[0,0,1,0],[0,0,0,1]]
    assert adapter["W_nonzero_vectors"] == expected_kernel[1:]
    assert adapter["W_dimension"] == 2
    assert adapter["W_equals_kernel_r_mod2"] is True
    assert adapter["arbitrary_symplectic_basis_used"] is False

    # Exact pointwise filter of the already-audited 28 post1503 survivors.
    source_28 = upstream["q602_mod2_preflight"]["surviving_residue_classes_decimal"]
    assert len(source_28) == 28
    survivors = [bits for bits in source_28 if fixes_w(bits, w_basis)]
    expected_16 = [65,67,73,75,97,99,105,107,193,195,201,203,225,227,233,235]
    assert survivors == expected_16
    test = cert["q602_pointwise_exact_W_test"]
    assert test["input_residues_decimal"] == source_28
    assert test["input_residue_count"] == 28
    assert test["condition"] == "T|W=id and T^dagger|W=id"
    assert test["surviving_residue_count"] == 16
    assert test["surviving_residues_decimal"] == survivors
    assert test["surviving_residues_hex"] == [f"0x{x:02x}" for x in survivors]
    assert test["removed_residue_count"] == 12
    assert test["Q602_excluded"] is False

    dec = cert["decision"]
    assert dec["retained_F2_4_adapter_identified"] is True
    assert dec["pointwise_28_to_16_pruning"] is True
    assert dec["Q602_excluded"] is False
    assert dec["O210_excluded"] is False
    assert dec["O212_plus_authorized"] is False

    print(json.dumps({
        "schema": cert["schema"],
        "canonical": EXPECTED_CANONICAL,
        "Delta": delta,
        "fhat_over_f": "-1/2",
        "W_basis": w_basis,
        "Q602_residues": {"input": 28, "survivors": 16, "values": survivors},
        "Q602_excluded": False,
        "O210_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
