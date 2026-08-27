#!/usr/bin/env python3
"""Compute the Stage-A G_L restriction kernel from an explicit squareclass span.

Normal input describes a finite V4-stable subspace X of L*/L*2 containing all
squareclasses occurring in the real 14x26 restriction tensor.  With exact
row-action matrices on X and on K=Br(Sbar)[2], this consumer verifies that every
source image is fixed by the diagonal V4 action, computes the restriction-map
rank, and returns a deterministic basis of its kernel in F2^26.

It does not produce the project squareclasses.  --self-test exercises the
linear algebra on zero and rank-one invariant tensors only.
"""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "order2-gl-restriction-squareclass-contract.json"
BR2 = HERE / "proper-brauer2-from-discriminant.json"
FINREC = HERE / "order2-localization-receiver.json"
SDIM, KDIM = 26, 14


def die(msg):
    raise SystemExit(msg)


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, label):
    x = json.loads(path.read_text(encoding="utf-8"))
    h = x.get("canonical_sha256")
    if not h:
        die(f"{label}: missing canonical hash")
    body = dict(x)
    body.pop("canonical_sha256")
    got = canonical_sha256(body)
    if got != h:
        die(f"{label}: canonical hash mismatch {h} != {got}")
    return x


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def transpose(A):
    if not A:
        return []
    return [list(c) for c in zip(*A)]


def mm(A, B):
    if not A:
        return []
    if not B:
        if len(A[0]) == 0:
            return [[] for _ in A]
        die("matrix multiply empty right factor")
    if len(A[0]) != len(B):
        die("matrix multiply shape mismatch")
    bt = transpose(B)
    return [[sum(x & y for x, y in zip(row, col)) & 1 for col in bt] for row in A]


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def row_basis(rows, ncols):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        die("row-basis width regression")
    r = 0
    pivots = []
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = xor(a[i], a[r])
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a[:r], pivots


def rank2(rows, ncols):
    return len(row_basis(rows, ncols)[0])


def dot2(a, b):
    return sum(x & y for x, y in zip(a, b)) & 1


def nullspace_basis(equations, ncols):
    rref, pivots = row_basis(equations, ncols)
    pivotset = set(pivots)
    free = [j for j in range(ncols) if j not in pivotset]
    out = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for row, p in zip(rref, pivots):
            if row[f]:
                v[p] = 1
        if any(dot2(eq, v) for eq in equations):
            die("nullspace reconstruction failed")
        out.append(v)
    return out


def binary_square_matrix(x, n, label):
    if not isinstance(x, list) or len(x) != n:
        die(f"{label}: expected {n} rows")
    out = []
    for row in x:
        if not isinstance(row, list) or len(row) != n:
            die(f"{label}: expected {n}x{n}")
        rr = [int(v) for v in row]
        if any(v not in (0, 1) for v in rr):
            die(f"{label}: non-binary entry")
        out.append(rr)
    return out


def parse_tensors(raw, r):
    if not isinstance(raw, list) or len(raw) != SDIM:
        die(f"restriction tensors: expected {SDIM} source tensors")
    out = []
    for s, C in enumerate(raw):
        if not isinstance(C, list) or len(C) != KDIM:
            die(f"source tensor {s}: expected {KDIM} coefficient rows")
        CC = []
        for row in C:
            if not isinstance(row, list) or len(row) != r:
                die(f"source tensor {s}: expected {KDIM}x{r}")
            rr = [int(v) for v in row]
            if any(v not in (0, 1) for v in rr):
                die(f"source tensor {s}: non-binary entry")
            CC.append(rr)
        out.append(CC)
    return out


def transform_tensor(C, BK, BX, r):
    # Coordinates C[k,x] transform as BK^T * C * BX under row actions.
    if r == 0:
        return [[] for _ in range(KDIM)]
    return mm(mm(transpose(BK), C), BX)


def flatten(C):
    return [v for row in C for v in row]


def compute(inp, contract, br2, finrec):
    if inp.get("schema") != "STAGE33_07_ORDER2_GL_RESTRICTION_FINITE_SPAN_V1":
        die("input schema mismatch")
    if inp.get("field") != "L=Q(i,sqrt(2))":
        die("input field mismatch")
    if inp.get("source_dimension_f2") != SDIM or inp.get("coefficient_dimension_f2") != KDIM:
        die("input dimension mismatch")
    r = int(inp.get("squareclass_span_dimension_f2", -1))
    if r < 0:
        die("negative squareclass span dimension")
    labels = inp.get("squareclass_basis_labels")
    if not isinstance(labels, list) or len(labels) != r or len(set(labels)) != r:
        die("squareclass basis labels regression")
    Xcc = binary_square_matrix(inp.get("squareclass_cc_action_f2"), r, "squareclass cc")
    Xct = binary_square_matrix(inp.get("squareclass_ct_action_f2"), r, "squareclass ct")
    if r:
        Ir = eye(r)
        if mm(Xcc, Xcc) != Ir or mm(Xct, Xct) != Ir or mm(Xcc, Xct) != mm(Xct, Xcc):
            die("squareclass span does not carry a V4 action")
    Kcc = binary_square_matrix(br2["proper_Br2_cc_action_f2"], KDIM, "K cc")
    Kct = binary_square_matrix(br2["proper_Br2_ct_action_f2"], KDIM, "K ct")
    tensors = parse_tensors(inp.get("restriction_source_tensors_f2"), r)

    for s, C in enumerate(tensors):
        if transform_tensor(C, Kcc, Xcc, r) != C:
            die(f"source {s+1}: restriction tensor not cc-fixed")
        if transform_tensor(C, Kct, Xct, r) != C:
            die(f"source {s+1}: restriction tensor not ct-fixed")

    width = KDIM * r
    images = [flatten(C) for C in tensors]
    rank = rank2(images, width)
    equations = transpose(images) if width else []
    kernel = nullspace_basis(equations, SDIM)
    if len(kernel) != SDIM - rank:
        die("Stage-A kernel dimension regression")
    for v in kernel:
        image = [0] * width
        for coeff, row in zip(v, images):
            if coeff:
                image = xor(image, row)
        if any(image):
            die("Stage-A kernel basis verification failed")

    source_names = [x["name"] for x in finrec["finite_source_basis"]]
    cert = {
        "schema": "STAGE33_07_ORDER2_GL_RESTRICTION_KERNEL_FROM_SPAN_V1",
        "source_locks": {
            "squareclass_contract_sha256": contract["canonical_sha256"],
            "proper_brauer2_sha256": br2["canonical_sha256"],
            "finite_localization_receiver_sha256": finrec["canonical_sha256"],
            "input_sha256": inp["canonical_sha256"],
        },
        "field": "L=Q(i,sqrt(2))",
        "source_dimension_f2": SDIM,
        "source_basis_names": source_names,
        "coefficient_dimension_f2": KDIM,
        "squareclass_span_dimension_f2": r,
        "squareclass_basis_labels": labels,
        "diagonal_V4_invariance_verified_for_all_source_images": True,
        "Stage_A_target_coordinate_dimension_f2": width,
        "Stage_A_restriction_rank_f2": rank,
        "Stage_A_kernel_dimension_f2": len(kernel),
        "Stage_A_kernel_basis_f2_26": kernel,
        "Stage_A_kernel_basis_source_expressions": [
            [source_names[j] for j, bit in enumerate(v) if bit] for v in kernel
        ],
        "all_26_restrictions_zero": rank == 0,
        "all_26_restrictions_independent": rank == SDIM,
        "Stage_B_descended_V4_domain_dimension_f2": len(kernel),
        "Stage_B_finite_delta_computed": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_nonexistence_claim": False,
    }
    cert["canonical_sha256"] = canonical_sha256(cert)
    return cert


def make_input(r, Xcc, Xct, tensors, labels):
    x = {
        "schema": "STAGE33_07_ORDER2_GL_RESTRICTION_FINITE_SPAN_V1",
        "field": "L=Q(i,sqrt(2))",
        "source_dimension_f2": SDIM,
        "coefficient_dimension_f2": KDIM,
        "squareclass_span_dimension_f2": r,
        "squareclass_basis_labels": labels,
        "squareclass_cc_action_f2": Xcc,
        "squareclass_ct_action_f2": Xct,
        "restriction_source_tensors_f2": tensors,
    }
    x["canonical_sha256"] = canonical_sha256(x)
    return x


def self_test(contract, br2, finrec):
    # Test 1: zero restriction in a one-dimensional trivial squareclass span.
    zero = [[[0] for _ in range(KDIM)] for _ in range(SDIM)]
    inp0 = make_input(1, [[1]], [[1]], zero, ["selftest_trivial_squareclass"])
    c0 = compute(inp0, contract, br2, finrec)
    if c0["Stage_A_restriction_rank_f2"] != 0 or c0["Stage_A_kernel_dimension_f2"] != SDIM:
        die("zero self-test failed")

    # Test 2: one source maps to a nonzero jointly V4-fixed coefficient vector.
    Kcc = binary_square_matrix(br2["proper_Br2_cc_action_f2"], KDIM, "K cc")
    Kct = binary_square_matrix(br2["proper_Br2_ct_action_f2"], KDIM, "K ct")
    I = eye(KDIM)
    Ng = [[Kcc[i][j] ^ I[i][j] for j in range(KDIM)] for i in range(KDIM)]
    Nh = [[Kct[i][j] ^ I[i][j] for j in range(KDIM)] for i in range(KDIM)]
    fixed = nullspace_basis(transpose(Ng) + transpose(Nh), KDIM)
    if len(fixed) != 10:
        die(f"joint fixed coefficient regression {len(fixed)}")
    v = fixed[0]
    one = [[[0] for _ in range(KDIM)] for _ in range(SDIM)]
    for k, bit in enumerate(v):
        one[0][k][0] = bit
    inp1 = make_input(1, [[1]], [[1]], one, ["selftest_trivial_squareclass"])
    c1 = compute(inp1, contract, br2, finrec)
    if c1["Stage_A_restriction_rank_f2"] != 1 or c1["Stage_A_kernel_dimension_f2"] != SDIM - 1:
        die("rank-one self-test failed")

    cert = {
        "schema": "STAGE33_07_ORDER2_GL_RESTRICTION_SPAN_CONSUMER_SELFTEST_V1",
        "zero_case": {
            "rank_f2": c0["Stage_A_restriction_rank_f2"],
            "kernel_dimension_f2": c0["Stage_A_kernel_dimension_f2"],
        },
        "rank_one_case": {
            "coefficient_joint_fixed_dimension_f2": len(fixed),
            "rank_f2": c1["Stage_A_restriction_rank_f2"],
            "kernel_dimension_f2": c1["Stage_A_kernel_dimension_f2"],
        },
        "diagonal_V4_tensor_action_checked": True,
        "project_squareclasses_used": False,
        "project_Stage_A_restriction_computed": False,
        "absolute_delta_loc_computed": False,
        "theorem_credit": False,
        "endpoint_credit": False,
    }
    cert["canonical_sha256"] = canonical_sha256(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    contract = load_locked(CONTRACT, "squareclass contract")
    br2 = load_locked(BR2, "proper Br2")
    finrec = load_locked(FINREC, "finite localization receiver")

    if args.self_test:
        if args.input:
            die("--self-test and --input are mutually exclusive")
        cert = self_test(contract, br2, finrec)
    else:
        if not args.input:
            die("normal mode requires --input")
        inp = load_locked(args.input, "restriction finite-span input")
        cert = compute(inp, contract, br2, finrec)

    if args.output:
        args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
