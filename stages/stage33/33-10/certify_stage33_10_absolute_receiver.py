#!/usr/bin/env python3
"""Certify Stage33-10: ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER.

This is a receiver-identification stage, not the 26-column localization stage.
Starting from the source-locked 14-dimensional F2 Galois module
K=Br(Sbar)[2], we construct an explicit V4-equivariant basis proving

  K ~= F2^6
       + Ind_{G_{Q(i)}}^{G_Q}(F2)^3
       + Ind_{G_{Q(sqrt(-2))}}^{G_Q}(F2).

The action on K factors through L=Q(i,sqrt(2))/Q.  Continuous Shapiro then
gives the exact absolute degree-one receiver

  H^1(G_Q,K)
    ~= Hom_cont(G_Q,F2)^6
       + Hom_cont(G_{Q(i)},F2)^3
       + Hom_cont(G_{Q(sqrt(-2))},F2).

This explicitly replaces the invalid finite-V4 shortcut.  Stage33-11 must
compute the 26 arithmetic localization directions in this absolute receiver;
this script does not manufacture any of those classes.

Shapiro source locator used by the stage contract:
  Neukirch--Schmidt--Wingberg, Cohomology of Number Fields, Prop. 1.6.3
  (continuous cohomology of profinite groups).
"""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
BR2 = STAGE33 / "33-07" / "proper-brauer2-from-discriminant.json"
ARITH = STAGE33 / "33-07" / "arithmetic-hs-descent-problem.json"
PREV = STAGE33 / "33-09" / "handoff.json"
OUT = HERE / "absolute-h1-receiver-certified.json"

EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_ARITH = "5304ef5372eae904b75ea9e261516117a7386fab44ede6c28b9ad437371a50e2"
EXPECTED_33_09 = "9d385fd8ccddbf2d6f5289d944c4e80523ba39310d165c0741d9b5c33698e573"
EXPECTED_33_09_CLOSURE = "6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7"
N = 14


def die(msg):
    raise SystemExit(msg)


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected, label):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256", None)
    actual = canonical_sha256(body)
    if claimed != expected or actual != expected:
        die(f"{label} source lock moved: claimed={claimed} actual={actual} expected={expected}")
    return obj


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mat_xor(a, b):
    return [[x ^ y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x & y for x, y in zip(row, col)) & 1 for col in bt] for row in a]


def apply(v, m):
    out = [0] * len(m[0])
    for i, bit in enumerate(v):
        if bit:
            out = xor(out, m[i])
    return out


def row_basis(rows, ncols=N):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        die("GF2 row width regression")
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


def rank(rows, ncols=N):
    return len(row_basis(rows, ncols))


def rref_system(eq_rows, rhs, nvars=N):
    a = [[int(x) & 1 for x in row] + [int(b) & 1] for row, b in zip(eq_rows, rhs)]
    if any(len(row) != nvars + 1 for row in a):
        die("linear-system width regression")
    pivots = []
    r = 0
    for c in range(nvars):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = xor(a[i], a[r])
        pivots.append(c)
        r += 1
    for row in a:
        if not any(row[:nvars]) and row[nvars]:
            return None, None, None
    return a, pivots, r


def solve_constraints(constraints):
    """constraints is [(matrix, target_row_vector), ...] for row x*M=target."""
    eq_rows = []
    rhs = []
    for m, target in constraints:
        if len(target) != N:
            die("constraint target width regression")
        for j in range(N):
            eq_rows.append([m[i][j] for i in range(N)])
            rhs.append(target[j])
    a, pivots, _ = rref_system(eq_rows, rhs)
    if a is None:
        return None
    x = [0] * N
    for i, p in enumerate(pivots):
        x[p] = a[i][N]
    return x


def nullspace_constraints(maps):
    eq_rows = []
    rhs = []
    for m in maps:
        for j in range(N):
            eq_rows.append([m[i][j] for i in range(N)])
            rhs.append(0)
    a, pivots, _ = rref_system(eq_rows, rhs)
    if a is None:
        die("homogeneous system unexpectedly inconsistent")
    free = [c for c in range(N) if c not in pivots]
    basis = []
    for f in free:
        x = [0] * N
        x[f] = 1
        for i, p in enumerate(pivots):
            if a[i][f]:
                x[p] = 1
        basis.append(x)
    return basis


def extend_independent(seed, candidates, target_rank=None):
    out = list(seed)
    current = rank(out)
    for v in candidates:
        nr = rank(out + [v])
        if nr > current:
            out.append(v)
            current = nr
            if target_rank is not None and current == target_rank:
                break
    return out


def zero(v):
    return not any(v)


br2 = load_locked(BR2, EXPECTED_BR2, "proper Br2")
arith = load_locked(ARITH, EXPECTED_ARITH, "arithmetic HS problem")
prev = load_locked(PREV, EXPECTED_33_09, "Stage33-09 handoff")
if prev.get("status") != "CLOSED_EXACT":
    die("Stage33-09 is not exact-closed")
if prev.get("source_locks", {}).get("stage33_09_closure_sha256") != EXPECTED_33_09_CLOSURE:
    die("Stage33-09 closure source lock moved")
if prev.get("next_item") != "Stage33-10_ABSOLUTE_H1_AND_GALOIS_DESCENT_ADAPTER":
    die("Stage33-09 handoff no longer releases Stage33-10")

finite = arith["boundary_candidates_not_yet_promoted_to_global_q_classes"]["finite_ramified_after_u44"]
if (finite["minimal_invariant_factor_generators"], finite["order2_factors"], finite["order4_factors"]) != (26, 23, 3):
    die("26-direction arithmetic source contract moved")

cc = [[int(x) & 1 for x in row] for row in br2["proper_Br2_cc_action_f2"]]
ct = [[int(x) & 1 for x in row] for row in br2["proper_Br2_ct_action_f2"]]
if len(cc) != N or len(ct) != N or any(len(r) != N for r in cc + ct):
    die("proper Br2 action shape regression")
I = eye(N)
if matmul(cc, cc) != I or matmul(ct, ct) != I or matmul(cc, ct) != matmul(ct, cc):
    die("source-locked actions are not a V4 representation")
Nc = mat_xor(cc, I)
Nt = mat_xor(ct, I)

# Exact fixed-space profile from the matrices, not just stored metadata.
rcc = rank(Nc)
rct = rank(Nt)
joint = nullspace_constraints([Nc, Nt])
fixed_cc = N - rcc
fixed_ct = N - rct
fixed_joint = len(joint)
if (fixed_cc, fixed_ct, fixed_joint) != (10, 13, 10):
    die(f"proper Br2 fixed-space profile moved: {(fixed_cc, fixed_ct, fixed_joint)}")
if br2.get("proper_Br2_fixed_dimensions") != {"cc": 10, "ct": 13, "joint_v4": 10}:
    die("stored proper Br2 fixed dimensions disagree with direct recomputation")

# The claimed permutation decomposition forces Ncc*Nct=Nct*Ncc=0; verify it.
Z = [[0] * N for _ in range(N)]
if matmul(Nc, Nt) != Z or matmul(Nt, Nc) != Z:
    die("nilpotent cross-term obstructs the claimed permutation decomposition")

# Im(Nt) is the invariant line of the unique block on which both generators
# swap.  It must lie inside Im(Nc).
im_t = row_basis(Nt)
im_c = row_basis(Nc)
if len(im_t) != 1 or len(im_c) != 4:
    die("nilpotent image ranks moved")
y_both = im_t[0]
if rank(im_c + [y_both]) != 4:
    die("Im(Nt) is not contained in Im(Nc)")

# Build a deterministic basis y_both,y1,y2,y3 of Im(Nc).
y_basis = extend_independent([y_both], im_c, target_rank=4)
if len(y_basis) != 4:
    die("could not complete Im(Nc) basis")

# Unique both-swap block: find x with x*Nc=x*Nt=y_both.
x_both = solve_constraints([(Nc, y_both), (Nt, y_both)])
if x_both is None:
    die("no exact both-swap lift vector")
pair_both = [x_both, xor(x_both, y_both)]

# Three cc-swap / ct-fixed blocks.
pairs_cc = []
for y in y_basis[1:]:
    x = solve_constraints([(Nc, y), (Nt, [0] * N)])
    if x is None:
        die("no exact cc-swap/ct-fixed lift vector")
    pairs_cc.append([x, xor(x, y)])

# Six trivial summands are a complement of Im(Nc) inside the joint fixed space.
trivial = extend_independent(im_c, joint, target_rank=10)[4:]
if len(trivial) != 6:
    die(f"joint fixed complement is not six-dimensional: {len(trivial)}")

# New basis ordering: 6 trivial, 3 Q(i)-permutation pairs, 1 Q(sqrt(-2)) pair.
new_basis = trivial + [v for pair in pairs_cc for v in pair] + pair_both
if len(new_basis) != N or rank(new_basis) != N:
    die("constructed equivariant basis is not invertible")

# Verify every block action directly in original coordinates.
for v in trivial:
    if apply(v, cc) != v or apply(v, ct) != v:
        die("trivial block action verification failed")
for a, b in pairs_cc:
    if apply(a, cc) != b or apply(b, cc) != a:
        die("Q(i) permutation block cc swap failed")
    if apply(a, ct) != a or apply(b, ct) != b:
        die("Q(i) permutation block ct fixed action failed")
a, b = pair_both
if apply(a, cc) != b or apply(b, cc) != a or apply(a, ct) != b or apply(b, ct) != a:
    die("Q(sqrt(-2)) permutation block action failed")

# Finite H1 cross-check: 6 trivial summands contribute dim 2 each for V4,
# while each index-two permutation summand contributes dim 1 by finite Shapiro.
finite_h1_from_decomposition = 6 * 2 + 3 + 1
if finite_h1_from_decomposition != 16:
    die("decomposition H1 cross-check failed")
if br2["finite_v4_H1_proper_Br2"]["H1_dimension_f2"] != 16:
    die("source finite V4 H1 regression")
if br2["finite_v4_H1_proper_Br2"]["absolute_H1_identified_with_finite_H1"]:
    die("source firewall unexpectedly promotes finite H1 to absolute H1")

witness_hash = canonical_sha256({"basis_rows_original_coordinates_f2": new_basis})
cert = {
    "schema": "STAGE33_10_ABSOLUTE_H1_RECEIVER_V1",
    "stage": "33-10",
    "name": "ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER",
    "source_locks": {
        "proper_brauer2_from_discriminant_sha256": EXPECTED_BR2,
        "arithmetic_hs_descent_problem_sha256": EXPECTED_ARITH,
        "stage33_09_handoff_sha256": EXPECTED_33_09,
        "stage33_09_closure_sha256": EXPECTED_33_09_CLOSURE,
        "testa_stoll_upstream_git_blob_sha1": prev["source_locks"]["upstream_git_blob_sha1"],
    },
    "coefficient_module": {
        "module": "K=Br(Sbar)[2]",
        "dimension_f2": 14,
        "splitting_field": "L=Q(i,sqrt(2))",
        "quotient": "Gal(L/Q)=V4=<cc,ct>",
        "fixed_dimensions": {"cc": fixed_cc, "ct": fixed_ct, "joint_v4": fixed_joint},
        "exact_permutation_decomposition": [
            {"multiplicity": 6, "module": "F2", "galois_description": "trivial G_Q module"},
            {"multiplicity": 3, "module": "Ind_{G_Q(i)}^{G_Q}(F2)", "finite_V4_block": "cc swaps, ct fixes"},
            {"multiplicity": 1, "module": "Ind_{G_Q(sqrt(-2))}^{G_Q}(F2)", "finite_V4_block": "cc and ct both swap"},
        ],
        "equivariant_basis_witness_sha256": witness_hash,
        "equivariant_basis_rows_original_coordinates_f2": new_basis,
    },
    "finite_shortcut": {
        "H1_V4_dimension_f2": 16,
        "status": "EXPLICITLY_REPLACED",
        "reason": "finite V4 H1 is only the quotient-factor part; the exact absolute receiver contains unrestricted quadratic-character groups",
        "strictness_witness": "the Q(sqrt(3))/Q character in a trivial F2 summand does not factor through L=Q(i,sqrt(2))",
    },
    "absolute_h1_receiver": {
        "theorem": "continuous Shapiro lemma",
        "source_locator": "Neukirch-Schmidt-Wingberg, Cohomology of Number Fields, Proposition 1.6.3",
        "isomorphism": "H^1(G_Q,K) ~= Hom_cont(G_Q,F2)^6 direct_sum Hom_cont(G_Q(i),F2)^3 direct_sum Hom_cont(G_Q(sqrt(-2)),F2)",
        "finite_dimensional_claimed": False,
        "kernel_galois_contribution": "included exactly in the unrestricted character groups; no zero-kernel assumption is made",
        "inflation_restriction_transgression_left_unaccounted": False,
    },
    "stage33_11_interface": {
        "source_invariant_factor_directions": 26,
        "source_group_before_order_two_layer": "(Z/2)^23 direct_sum (Z/4)^3",
        "order2_factors": 23,
        "order4_factors": 3,
        "order_two_localization_domain": "F2^26 from the 26 named invariant-factor directions",
        "codomain": "Hom_cont(G_Q,F2)^6 direct_sum Hom_cont(G_Q(i),F2)^3 direct_sum Hom_cont(G_Q(sqrt(-2)),F2)",
        "connecting_source_directions_computed": "0/26",
        "arithmetic_localization_connecting_map_computed": False,
        "meaning": "33-11 must materialize the actual 26 project cocycles in this exact absolute receiver; 33-10 supplies only the domain/codomain adapter",
    },
    "branches": {
        "33-10a": "CLOSED_FINITE_SHORTCUT_REJECTED",
        "33-10b": "CLOSED_BY_EXACT_MODULE_DECOMPOSITION_AND_SHAPIRO",
        "33-10c": "CLOSED_KERNEL_GALOIS_CONTRIBUTION_INCLUDED_IN_CHARACTER_GROUPS",
        "33-10d": "NOT_NEEDED_AFTER_10E",
        "33-10e": "CLOSED_EXACT",
    },
    "exit_condition": {
        "absolute_h1_receiver_exact": True,
        "finite_v4_shortcut_status_proved_valid_or_explicitly_replaced": True,
        "kernel_galois_relevant_contribution_accounted": True,
        "stage33_11_domain_and_codomain_well_defined": True,
    },
    "firewalls": {
        "connecting_matrix_columns_materialized": "0/26",
        "arithmetic_localization_connecting_map_computed": False,
        "arithmetic_hs_closed": False,
        "stage33_07_closed": False,
        "stage33_08_released": False,
        "stage33_progress": "6/11",
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
    "next_item": "Stage33-11_ARITHMETIC_LOCALIZATION_CONNECTING_MAP",
    "next_expected_command": "Stage33-main-batch",
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "finite_H1_V4_dimension_f2": 16,
    "decomposition": "F2^6 + Ind_Q(i)^3 + Ind_Q(sqrt(-2))",
    "absolute_H1_receiver_exact": True,
    "kernel_galois_relevant_contribution_accounted": True,
    "stage33_11_domain_and_codomain_well_defined": True,
    "connecting_columns_materialized": "0/26",
    "witness_sha256": witness_hash,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
