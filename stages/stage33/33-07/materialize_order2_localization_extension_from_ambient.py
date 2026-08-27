#!/usr/bin/env python3
"""Compute the finite V4 order-2 localization connecting map from an exact ambient extension.

Input contract (row-vector/right-action convention):
    0 -> K=F2^14 --I--> M=F2^40 --P--> Q=F2^26 -> 0,
with Q carrying the trivial V4 action and K carrying the exact proper-Br2
actions already certified in proper-brauer2-from-discriminant.json.

This adapter does not construct M. It validates a supplied ambient V4 module,
chooses a deterministic linear section Q -> M, extracts the lift defects in K,
and reduces the resulting cocycles to the existing H^1(V4,K)=F2^16 receiver.

--self-test uses the split extension K direct_sum Q. That tests only the
adapter mechanics; it is not a computation of the project localization class.
"""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_RECEIVER = HERE / "order2-localization-receiver.json"
DEFAULT_BR2 = HERE / "proper-brauer2-from-discriminant.json"
KDIM, QDIM, MDIM, H1DIM = 14, 26, 40, 16


def die(msg):
    raise SystemExit(msg)


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_canonical(obj, label):
    claimed = obj.get("canonical_sha256")
    if not claimed:
        die(f"{label}: missing canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = canonical_sha256(body)
    if actual != claimed:
        die(f"{label}: canonical hash mismatch claimed={claimed} actual={actual}")


def binary_matrix(x, rows, cols, label):
    if not isinstance(x, list) or len(x) != rows:
        die(f"{label}: expected {rows} rows")
    out = []
    for r in x:
        if not isinstance(r, list) or len(r) != cols:
            die(f"{label}: expected shape {rows}x{cols}")
        rr = [int(v) for v in r]
        if any(v not in (0, 1) for v in rr):
            die(f"{label}: non-binary entry")
        out.append(rr)
    return out


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def zeros(r, c):
    return [[0] * c for _ in range(r)]


def add(a, b):
    if len(a) != len(b) or (a and len(a[0]) != len(b[0])):
        die("matrix xor shape mismatch")
    return [[x ^ y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def matmul(a, b):
    if not a:
        return []
    if not b or len(a[0]) != len(b):
        die("matrix multiply shape mismatch")
    bt = list(zip(*b))
    return [[sum(x & y for x, y in zip(row, col)) & 1 for col in bt] for row in a]


def transpose(a):
    return [list(col) for col in zip(*a)] if a else []


def rank2(rows, ncols=None):
    a = [[int(x) & 1 for x in row] for row in rows]
    if not a:
        return 0
    if ncols is None:
        ncols = len(a[0])
    if any(len(row) != ncols for row in a):
        die("rank shape mismatch")
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def solve_linear(a, b, label):
    """Deterministic solution of A x=b over F2; free variables are zero."""
    m = len(a)
    if m != len(b):
        die(f"{label}: rhs height mismatch")
    n = len(a[0]) if a else 0
    if any(len(row) != n for row in a):
        die(f"{label}: ragged matrix")
    aug = [[int(x) & 1 for x in row] + [int(rhs) & 1] for row, rhs in zip(a, b)]
    r = 0
    pivots = []
    for c in range(n):
        p = next((i for i in range(r, m) if aug[i][c]), None)
        if p is None:
            continue
        aug[r], aug[p] = aug[p], aug[r]
        for i in range(m):
            if i != r and aug[i][c]:
                aug[i] = [x ^ y for x, y in zip(aug[i], aug[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    if any(not any(row[:n]) and row[n] for row in aug):
        die(f"{label}: inconsistent linear system")
    x = [0] * n
    for i, c in enumerate(pivots):
        x[c] = aug[i][n]
    got = [sum(u & v for u, v in zip(row, x)) & 1 for row in a]
    if got != [int(v) & 1 for v in b]:
        die(f"{label}: solver verification failed")
    return x


def right_inverse(p):
    pt = transpose(p)
    s = []
    for j in range(QDIM):
        rhs = [1 if i == j else 0 for i in range(QDIM)]
        s.append(solve_linear(pt, rhs, f"section row {j}"))
    if matmul(s, p) != eye(QDIM):
        die("deterministic section failed S*P=I")
    return s


def coordinates_in_kernel(inclusion, defects, label):
    it = transpose(inclusion)
    out = []
    for j, d in enumerate(defects):
        out.append(solve_linear(it, d, f"{label} kernel coordinates row {j}"))
    if matmul(out, inclusion) != defects:
        die(f"{label}: kernel coordinate reconstruction failed")
    return out


def h1_coordinates(receiver, e_cc, e_ct, k_cc, k_ct):
    b1 = binary_matrix(
        receiver["finite_receiver_B1_basis_f2_28"], 4, 2 * KDIM, "receiver B1"
    )
    h1 = binary_matrix(
        receiver["finite_receiver_H1_quotient_representatives_f2_28"],
        H1DIM, 2 * KDIM, "receiver H1",
    )
    basis = b1 + h1
    if rank2(basis, 2 * KDIM) != 20:
        die("receiver B1+H1 basis rank regression")
    bt = transpose(basis)
    ng = add(k_cc, eye(KDIM))
    nh = add(k_ct, eye(KDIM))
    rows26 = []
    for j in range(QDIM):
        a, b = e_cc[j], e_ct[j]
        if matmul([a], ng)[0] != [0] * KDIM:
            die(f"source {j}: cc involution cocycle equation failed")
        if matmul([b], nh)[0] != [0] * KDIM:
            die(f"source {j}: ct involution cocycle equation failed")
        if matmul([a], nh)[0] != matmul([b], ng)[0]:
            die(f"source {j}: V4 commutation cocycle equation failed")
        coeff = solve_linear(bt, a + b, f"source {j} receiver coordinates")
        rows26.append(coeff[4:])
    return rows26, transpose(rows26)


def compute(ambient, receiver, br2):
    if ambient.get("schema") != "STAGE33_07_ORDER2_AMBIENT_V4_EXTENSION_V1":
        die("ambient schema mismatch")
    if ambient.get("kernel_dimension_f2") != KDIM:
        die("ambient kernel dimension mismatch")
    if ambient.get("quotient_dimension_f2") != QDIM:
        die("ambient quotient dimension mismatch")
    if ambient.get("ambient_dimension_f2") != MDIM:
        die("ambient dimension mismatch")
    if ambient.get("quotient_V4_action") != "TRIVIAL":
        die("ambient quotient V4 action must be TRIVIAL")

    inc = binary_matrix(ambient["kernel_inclusion_f2"], KDIM, MDIM, "kernel inclusion")
    proj = binary_matrix(ambient["quotient_projection_f2"], MDIM, QDIM, "quotient projection")
    a_cc = binary_matrix(ambient["ambient_cc_action_f2"], MDIM, MDIM, "ambient cc")
    a_ct = binary_matrix(ambient["ambient_ct_action_f2"], MDIM, MDIM, "ambient ct")
    k_cc = binary_matrix(br2["proper_Br2_cc_action_f2"], KDIM, KDIM, "kernel cc")
    k_ct = binary_matrix(br2["proper_Br2_ct_action_f2"], KDIM, KDIM, "kernel ct")

    if rank2(inc, MDIM) != KDIM:
        die("kernel inclusion rank regression")
    if rank2(proj, QDIM) != QDIM:
        die("quotient projection rank regression")
    if matmul(inc, proj) != zeros(KDIM, QDIM):
        die("projection after inclusion is not zero")
    im = eye(MDIM)
    if matmul(a_cc, a_cc) != im or matmul(a_ct, a_ct) != im:
        die("ambient generators are not involutions")
    if matmul(a_cc, a_ct) != matmul(a_ct, a_cc):
        die("ambient V4 generators do not commute")
    if matmul(k_cc, inc) != matmul(inc, a_cc):
        die("cc kernel inclusion is not equivariant")
    if matmul(k_ct, inc) != matmul(inc, a_ct):
        die("ct kernel inclusion is not equivariant")
    if matmul(a_cc, proj) != proj or matmul(a_ct, proj) != proj:
        die("ambient projection is not equivariant to the trivial quotient")

    section = right_inverse(proj)
    d_cc = add(matmul(section, a_cc), section)
    d_ct = add(matmul(section, a_ct), section)
    if matmul(d_cc, proj) != zeros(QDIM, QDIM):
        die("cc section defect does not land in kernel")
    if matmul(d_ct, proj) != zeros(QDIM, QDIM):
        die("ct section defect does not land in kernel")
    e_cc = coordinates_in_kernel(inc, d_cc, "cc")
    e_ct = coordinates_in_kernel(inc, d_ct, "ct")
    rows26, matrix16x26 = h1_coordinates(receiver, e_cc, e_ct, k_cc, k_ct)
    return {
        "deterministic_section_f2_26x40": section,
        "extension_defect_cc_in_kernel_f2_26x14": e_cc,
        "extension_defect_ct_in_kernel_f2_26x14": e_ct,
        "connecting_map_source_rows_f2_26x16": rows26,
        "connecting_map_delta_loc_f2_16x26": matrix16x26,
        "connecting_map_rank_f2": rank2(matrix16x26, QDIM),
        "nonzero_source_columns_1based": [
            j + 1 for j in range(QDIM)
            if any(matrix16x26[i][j] for i in range(H1DIM))
        ],
    }


def split_ambient(br2):
    k_cc = binary_matrix(br2["proper_Br2_cc_action_f2"], KDIM, KDIM, "kernel cc")
    k_ct = binary_matrix(br2["proper_Br2_ct_action_f2"], KDIM, KDIM, "kernel ct")
    inc = [eye(KDIM)[i] + [0] * QDIM for i in range(KDIM)]
    proj = [[0] * QDIM for _ in range(KDIM)] + eye(QDIM)

    def block_diag(k):
        return (
            [row + [0] * QDIM for row in k]
            + [[0] * KDIM + row for row in eye(QDIM)]
        )

    return {
        "schema": "STAGE33_07_ORDER2_AMBIENT_V4_EXTENSION_V1",
        "kernel_dimension_f2": KDIM,
        "quotient_dimension_f2": QDIM,
        "ambient_dimension_f2": MDIM,
        "quotient_V4_action": "TRIVIAL",
        "kernel_inclusion_f2": inc,
        "quotient_projection_f2": proj,
        "ambient_cc_action_f2": block_diag(k_cc),
        "ambient_ct_action_f2": block_diag(k_ct),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ambient", type=Path)
    ap.add_argument("--receiver", type=Path, default=DEFAULT_RECEIVER)
    ap.add_argument("--br2", type=Path, default=DEFAULT_BR2)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    receiver = load_json(args.receiver)
    br2 = load_json(args.br2)
    validate_canonical(receiver, "receiver")
    validate_canonical(br2, "proper Br2")
    if receiver.get("schema") != "STAGE33_07_ORDER2_LOCALIZATION_RECEIVER_V1":
        die("receiver schema mismatch")
    if receiver.get("finite_source_order2_dimension_f2") != QDIM:
        die("receiver source dimension regression")
    if receiver.get("finite_receiver_module_dimension_f2") != KDIM:
        die("receiver kernel dimension regression")
    if receiver.get("finite_receiver_H1_dimension_f2") != H1DIM:
        die("receiver H1 dimension regression")
    if br2.get("proper_geometric_Br2_dimension_f2") != KDIM:
        die("proper Br2 dimension regression")

    if args.self_test:
        if args.ambient:
            die("--self-test and --ambient are mutually exclusive")
        result = compute(split_ambient(br2), receiver, br2)
        if result["connecting_map_delta_loc_f2_16x26"] != zeros(H1DIM, QDIM):
            die("split-extension self-test produced nonzero connecting map")
        cert = {
            "schema": "STAGE33_07_ORDER2_AMBIENT_EXTENSION_ADAPTER_SELFTEST_V1",
            "test_extension": "SPLIT_K_DIRECT_SUM_Q",
            "kernel_dimension_f2": KDIM,
            "quotient_dimension_f2": QDIM,
            "ambient_dimension_f2": MDIM,
            "finite_receiver_H1_dimension_f2": H1DIM,
            "connecting_map_rank_f2": result["connecting_map_rank_f2"],
            "connecting_map_is_zero": True,
            "adapter_mechanics_certified": True,
            "project_ambient_extension_materialized": False,
            "project_localization_extension_class_computed": False,
            "absolute_delta_loc_computed": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        }
        cert["canonical_sha256"] = canonical_sha256(cert)
        if args.output:
            args.output.write_text(
                json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
            )
        print(json.dumps(cert, indent=2, sort_keys=True))
        return

    if not args.ambient:
        die("normal mode requires --ambient")
    ambient = load_json(args.ambient)
    validate_canonical(ambient, "ambient extension")
    result = compute(ambient, receiver, br2)
    cert = {
        "schema": "STAGE33_07_ORDER2_LOCALIZATION_FROM_AMBIENT_V1",
        "source_locks": {
            "ambient_file_sha256": file_sha256(args.ambient),
            "receiver_file_sha256": file_sha256(args.receiver),
            "proper_brauer2_file_sha256": file_sha256(args.br2),
        },
        "kernel_dimension_f2": KDIM,
        "quotient_dimension_f2": QDIM,
        "ambient_dimension_f2": MDIM,
        "finite_receiver_H1_dimension_f2": H1DIM,
        **result,
        "ambient_extension_exactness_verified": True,
        "finite_V4_delta_loc_matrix_computed": True,
        "absolute_delta_loc_computed": False,
        "absolute_H1_identified_with_finite_V4_H1": False,
        "boundary_residual_promoted_to_global_q_classes": False,
        "constant_cokernel_HS_d2_computed": False,
        "actual_index512_k3_glue_identified": False,
        "arithmetic_HS_closed": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_nonexistence_claim": False,
    }
    cert["canonical_sha256"] = canonical_sha256(cert)
    output = args.output or HERE / "order2-localization-extension-from-ambient.json"
    output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "finite_V4_delta_loc_matrix_computed": True,
        "matrix_shape": [H1DIM, QDIM],
        "rank_f2": result["connecting_map_rank_f2"],
        "output": str(output),
        "absolute_delta_loc_computed": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
