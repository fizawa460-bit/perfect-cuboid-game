#!/usr/bin/env python3
"""Profile restriction of the retained 16D finite V4 localization receiver.

This treats all 26 source directions uniformly.  It computes only a structural
constraint on the receiver:

    H^1(V4,K) -> H^1(<cc>,K) x H^1(<ct>,K),

where K = Br(Sbar)[2].  No chosen Gersten lift, connecting-map column, or
arithmetic localization class is promoted by this leaf.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BR2 = HERE / "proper-brauer2-from-discriminant.json"
RECEIVER = HERE / "order2-localization-receiver.json"
OUTPUT = HERE / "v4-h1-generator-restriction-profile.json"

EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_RECEIVER = "9280846c6e7ae8a043e36c7b5498f11476901567b229b94e953b79afab891bda"
N = 14
H1DIM = 16


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256", None)
    actual = canonical_sha256(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"source lock moved for {path.name}: {claimed} {actual}")
    return obj


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def row_basis(rows, ncols):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        raise SystemExit("GF2 row width regression")
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = xor(a[i], a[r])
        r += 1
        if r == len(a):
            break
    return a[:r]


def rank2(rows, ncols):
    return len(row_basis(rows, ncols))


def quotient_image_rank(images, quotient_subspace, ncols):
    """Dimension of span(images) in F2^n / quotient_subspace."""
    base_rank = rank2(quotient_subspace, ncols)
    return rank2(quotient_subspace + images, ncols) - base_rank


def main():
    br2 = load_locked(BR2, EXPECTED_BR2)
    receiver = load_locked(RECEIVER, EXPECTED_RECEIVER)

    G = [[int(x) & 1 for x in row] for row in br2["proper_Br2_cc_action_f2"]]
    H = [[int(x) & 1 for x in row] for row in br2["proper_Br2_ct_action_f2"]]
    I = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    Ng = [[G[i][j] ^ I[i][j] for j in range(N)] for i in range(N)]
    Nh = [[H[i][j] ^ I[i][j] for j in range(N)] for i in range(N)]

    bcc = row_basis(Ng, N)
    bct = row_basis(Nh, N)
    fixed = br2["proper_Br2_fixed_dimensions"]
    cc_h1_c2_dim = 2 * int(fixed["cc"]) - N
    ct_h1_c2_dim = 2 * int(fixed["ct"]) - N
    if cc_h1_c2_dim != 6 or ct_h1_c2_dim != 12:
        raise SystemExit("C2 H1 dimension regression")
    if len(bcc) != N - int(fixed["cc"]) or len(bct) != N - int(fixed["ct"]):
        raise SystemExit("C2 coboundary rank regression")

    reps = [
        [int(x) & 1 for x in row]
        for row in receiver["finite_receiver_H1_quotient_representatives_f2_28"]
    ]
    if len(reps) != H1DIM or any(len(row) != 2 * N for row in reps):
        raise SystemExit("finite V4 H1 representative shape regression")
    if receiver["finite_receiver_H1_dimension_f2"] != H1DIM:
        raise SystemExit("finite V4 H1 dimension regression")

    imgs_cc = [row[:N] for row in reps]
    imgs_ct = [row[N:] for row in reps]
    rank_cc = quotient_image_rank(imgs_cc, bcc, N)
    rank_ct = quotient_image_rank(imgs_ct, bct, N)

    joint_subspace = [row + [0] * N for row in bcc] + [[0] * N + row for row in bct]
    pair_images = [a + b for a, b in zip(imgs_cc, imgs_ct)]
    rank_joint = quotient_image_rank(pair_images, joint_subspace, 2 * N)

    if not (0 <= rank_cc <= cc_h1_c2_dim):
        raise SystemExit("cc restriction rank escaped C2 H1")
    if not (0 <= rank_ct <= ct_h1_c2_dim):
        raise SystemExit("ct restriction rank escaped C2 H1")
    if not (max(rank_cc, rank_ct) <= rank_joint <= H1DIM):
        raise SystemExit("joint restriction rank regression")

    cert = {
        "schema": "STAGE33_07_V4_H1_GENERATOR_RESTRICTION_PROFILE_V2",
        "source_locks": {
            "proper_brauer2_from_discriminant_sha256": EXPECTED_BR2,
            "order2_localization_receiver_sha256": EXPECTED_RECEIVER,
        },
        "receiver": {
            "module": "K=proper geometric Br(Sbar)[2]",
            "H1_V4_dimension_f2": H1DIM,
            "H1_cc_C2_dimension_f2": cc_h1_c2_dim,
            "H1_ct_C2_dimension_f2": ct_h1_c2_dim,
        },
        "restriction_profile": {
            "cc_rank_f2": rank_cc,
            "cc_kernel_dimension_f2": H1DIM - rank_cc,
            "ct_rank_f2": rank_ct,
            "ct_kernel_dimension_f2": H1DIM - rank_ct,
            "joint_rank_f2": rank_joint,
            "joint_kernel_dimension_f2": H1DIM - rank_joint,
        },
        "exact_consequence": {
            "all_26_connecting_columns_share_this_same_receiver_restriction_profile": True,
            "one_generator_equivariance_of_project_lifts_claimed": False,
            "connecting_matrix_columns_materialized": 0,
            "finite_v4_delta_loc_computed": False,
            "middle_gersten_module_action_materialized": False,
        },
        "next_exact_leaf": "L33-07-MATERIALIZE-GENUINE-MIDDLE-GERSTEN-CC-CT-LIFT-DIFFERENCE-COCYCLES-FOR-ALL-26-SOURCES",
        "stage33_progress": "6/11",
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    }
    cert["canonical_sha256"] = canonical_sha256(cert)
    OUTPUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "cc_restriction_rank_f2": rank_cc,
        "cc_kernel_dimension_f2": H1DIM - rank_cc,
        "ct_restriction_rank_f2": rank_ct,
        "ct_kernel_dimension_f2": H1DIM - rank_ct,
        "joint_restriction_rank_f2": rank_joint,
        "joint_kernel_dimension_f2": H1DIM - rank_joint,
        "connecting_matrix_columns_materialized": "0/26",
        "certificate_sha256": cert["canonical_sha256"],
        "next": cert["next_exact_leaf"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
