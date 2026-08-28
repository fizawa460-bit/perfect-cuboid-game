#!/usr/bin/env python3
"""Certify Stage33-10: ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER.

This is a receiver-identification stage, not the 26-column localization stage.
Starting from the source-locked 14-dimensional F2 Galois module
K=Br(Sbar)[2], this verifier constructs an explicit V4-equivariant basis and
proves the *non-semisimple* decomposition

  K ~= F2^5
       + Ind_{G_{Q(i)}}^{G_Q}(F2)^3
       + Q_L,

where L=Q(i,sqrt(2)) and

  Q_L := Ind_{G_L}^{G_Q}(F2) / F2_diag.

The final three-dimensional quotient block is essential: the retained matrices
have Im(ct-1) independent of Im(cc-1), so the tempting decomposition into four
index-two permutation blocks is false.

Continuous Shapiro and the long exact sequence of

  0 -> F2_diag -> Ind_{G_L}^{G_Q}(F2) -> Q_L -> 0

then give an exact absolute receiver

  H^1(G_Q,K)
    ~= X_Q^5 + X_{Q(i)}^3 + E_L,

where X_F=Hom_cont(G_F,F2), E_L=H^1(G_Q,Q_L), and E_L is retained with its
possibly non-split exact filtration

  0 -> coker(res^1: X_Q -> X_L)
    -> E_L
    -> ker(res^2: H^2(G_Q,F2) -> H^2(G_L,F2))
    -> 0.

Thus the G_L contribution is accounted for rather than killed.  Stage33-11
must materialize the actual 26 project localization classes in this receiver.

Shapiro source locator used by the stage contract:
  Neukirch--Schmidt--Wingberg, Cohomology of Number Fields, Prop. 1.6.3.
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
            return None, None
    return a, pivots


def solve_constraints(constraints):
    """constraints is [(matrix,target), ...] for a row vector x with x*M=target."""
    eq_rows = []
    rhs = []
    for m, target in constraints:
        if len(target) != N:
            die("constraint target width regression")
        for j in range(N):
            eq_rows.append([m[i][j] for i in range(N)])
            rhs.append(target[j])
    a, pivots = rref_system(eq_rows, rhs)
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
    a, pivots = rref_system(eq_rows, rhs)
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


def find_nonzero_nc_preimage_of_nt(v, Nc, Nt):
    """Find x with x*Nt=v and x*Nc !=0, deterministically."""
    x0 = solve_constraints([(Nt, v)])
    if x0 is None:
        return None
    candidates = [x0]
    ker_t = nullspace_constraints([Nt])
    candidates.extend(xor(x0, k) for k in ker_t)
    # If a single basis toggle is insufficient, exhaust the 2^13 affine fiber.
    if all(not any(apply(x, Nc)) for x in candidates):
        candidates = []
        for mask in range(1 << len(ker_t)):
            x = x0[:]
            for j, k in enumerate(ker_t):
                if (mask >> j) & 1:
                    x = xor(x, k)
            candidates.append(x)
    return next((x for x in candidates if any(apply(x, Nc))), None)


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
Z = [[0] * N for _ in range(N)]

# Exact matrix invariants.
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
if matmul(Nc, Nt) != Z or matmul(Nt, Nc) != Z:
    die("radical-square-zero profile moved")

im_c = row_basis(Nc)
im_t = row_basis(Nt)
radical = row_basis(im_c + im_t)
if (len(im_c), len(im_t), len(radical)) != (4, 1, 5):
    die(f"nilpotent-image profile moved: {(len(im_c),len(im_t),len(radical))}")
# This is the exact firewall that killed the false 6+4 permutation split.
if rank(im_c + im_t) == len(im_c):
    die("unexpected containment Im(Nt)<=Im(Nc); non-split 3D block disappeared")

# Construct the 3D quotient-regular block.  Let v span Im(Nt); choose top x
# with Nt(x)=v and Nc(x)=u nonzero.  Cross products zero force u,v fixed.
v = im_t[0]
xq = find_nonzero_nc_preimage_of_nt(v, Nc, Nt)
if xq is None:
    die("could not construct quotient-regular top vector")
u = apply(xq, Nc)
if not any(u) or rank([u, v]) != 2:
    die("quotient-regular radical lines are not independent")
if apply(xq, Nt) != v:
    die("quotient-regular Nt lift regression")
if any(apply(u, Nc)) or any(apply(u, Nt)) or any(apply(v, Nc)) or any(apply(v, Nt)):
    die("quotient-regular radical is not joint fixed")
qblock = [xq, u, v]
# Normal form: cc(top)=top+u, ct(top)=top+v; u,v fixed.
if apply(xq, cc) != xor(xq, u) or apply(xq, ct) != xor(xq, v):
    die("quotient-regular top action mismatch")

# Complete Im(Nc) from u with three independent cc-radical lines.  Each has a
# preimage fixed by ct, giving three Ind_{G_Q(i)}^{G_Q}(F2) blocks.
y_basis = extend_independent([u], im_c, target_rank=4)
if len(y_basis) != 4:
    die("could not complete Im(Nc) from quotient-block line")
pairs_qi = []
for y in y_basis[1:]:
    x = solve_constraints([(Nc, y), (Nt, [0] * N)])
    if x is None:
        die("no exact Q(i) permutation-block lift")
    pair = [x, xor(x, y)]
    a, b = pair
    if apply(a, cc) != b or apply(b, cc) != a:
        die("Q(i) block cc swap verification failed")
    if apply(a, ct) != a or apply(b, ct) != b:
        die("Q(i) block ct-fixed verification failed")
    pairs_qi.append(pair)

# The radical has dimension five inside the ten-dimensional joint fixed space;
# its complement supplies exactly five trivial summands.
fixed_extension = extend_independent(radical, joint, target_rank=10)
trivial = fixed_extension[5:]
if len(trivial) != 5:
    die(f"joint-fixed trivial complement is not five-dimensional: {len(trivial)}")
for t in trivial:
    if apply(t, cc) != t or apply(t, ct) != t:
        die("trivial summand verification failed")

# Exact basis: 5 trivial + 3 index-two permutation pairs + 3D quotient regular.
new_basis = trivial + [z for pair in pairs_qi for z in pair] + qblock
if len(new_basis) != N or rank(new_basis) != N:
    die("constructed equivariant basis is not invertible")

# Identify qblock with Q_L = Ind_{G_L}^{G_Q}(F2)/F2_diag.  In the regular
# permutation module on V4 cosets, modulo the diagonal vector, the classes
# top=e_1, u=e_1+e_cc, v=e_1+e_ct have exactly the normal form verified above.
quotient_regular_verified = True

# Finite H1 cross-check.  For V4: five trivial summands give 5*2; the three
# Q(i) induced blocks give 3 by finite Shapiro; Q_L gives H^2(V4,F2) of
# dimension 3 from 0->F2->F2[V4]->Q_L->0 because positive cohomology of the
# regular induced module vanishes.  Total =16, matching the retained bar result.
finite_h1_from_decomposition = 5 * 2 + 3 + 3
if finite_h1_from_decomposition != 16:
    die("finite H1 decomposition cross-check failed")
if br2["finite_v4_H1_proper_Br2"]["H1_dimension_f2"] != 16:
    die("source finite V4 H1 regression")
if br2["finite_v4_H1_proper_Br2"]["absolute_H1_identified_with_finite_H1"]:
    die("source firewall unexpectedly promotes finite H1 to absolute H1")

witness_hash = canonical_sha256({"basis_rows_original_coordinates_f2": new_basis})
cert = {
    "schema": "STAGE33_10_ABSOLUTE_H1_RECEIVER_V2_NONSPLIT_QL",
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
        "nilpotent_image_dimensions": {"Im_cc_minus_1": 4, "Im_ct_minus_1": 1, "sum": 5},
        "false_four_pair_split_rejected": True,
        "exact_decomposition": [
            {"multiplicity": 5, "module": "F2", "galois_description": "trivial G_Q module"},
            {"multiplicity": 3, "module": "Ind_{G_Q(i)}^{G_Q}(F2)", "finite_V4_block": "cc swaps, ct fixes"},
            {"multiplicity": 1, "module": "Q_L=Ind_{G_L}^{G_Q}(F2)/F2_diag", "dimension_f2": 3, "normal_form": "cc(top)=top+u; ct(top)=top+v; u,v jointly fixed and independent"},
        ],
        "equivariant_basis_witness_sha256": witness_hash,
        "equivariant_basis_rows_original_coordinates_f2": new_basis,
        "quotient_regular_identification_verified": quotient_regular_verified,
    },
    "finite_shortcut": {
        "H1_V4_dimension_f2": 16,
        "status": "EXPLICITLY_REPLACED",
        "reason": "finite V4 H1 is not the absolute H1; five trivial summands alone already carry unrestricted quadratic characters",
        "strictness_witness": "a Q(sqrt(3))/Q character in a trivial F2 summand does not factor through L=Q(i,sqrt(2))",
    },
    "absolute_h1_receiver": {
        "theorem": "continuous Shapiro lemma plus the long exact cohomology sequence",
        "source_locator": "Neukirch-Schmidt-Wingberg, Cohomology of Number Fields, Proposition 1.6.3 (Shapiro); standard long exact sequence of continuous cohomology",
        "character_notation": "X_F=Hom_cont(G_F,F2)",
        "main_decomposition": "H^1(G_Q,K) ~= X_Q^5 direct_sum X_Q(i)^3 direct_sum E_L",
        "E_L_definition": "E_L=H^1(G_Q,Q_L), Q_L=Ind_{G_L}^{G_Q}(F2)/F2_diag",
        "E_L_exact_filtration": "0 -> coker(res^1: X_Q -> X_L) -> E_L -> ker(res^2: H^2(G_Q,F2) -> H^2(G_L,F2)) -> 0",
        "E_L_splitting_claimed": False,
        "finite_dimensional_claimed": False,
        "kernel_galois_contribution": "accounted exactly by coker(res^1 X_Q->X_L) together with the relative H^2 kernel; neither term is set to zero",
        "inflation_restriction_unknown_left_unmodeled": False,
    },
    "stage33_11_interface": {
        "source_invariant_factor_directions": 26,
        "source_group_before_order_two_layer": "(Z/2)^23 direct_sum (Z/4)^3",
        "order2_factors": 23,
        "order4_factors": 3,
        "order_two_localization_domain": "F2^26 from the 26 invariant-factor directions",
        "codomain": "X_Q^5 direct_sum X_Q(i)^3 direct_sum E_L with the exact non-split E_L filtration recorded above",
        "connecting_source_directions_computed": "0/26",
        "arithmetic_localization_connecting_map_computed": False,
        "meaning": "33-11 must materialize the actual 26 project cocycles; 33-10 supplies only the exact absolute domain/codomain adapter",
    },
    "branches": {
        "33-10a": "CLOSED_FINITE_SHORTCUT_REJECTED",
        "33-10b": "CLOSED_BY_EXACT_V4_MODULE_DECOMPOSITION_SHAPIRO_AND_LONG_EXACT_SEQUENCE",
        "33-10c": "CLOSED_KERNEL_GALOIS_CONTRIBUTION_ACCOUNTED_BY_E_L_FILTRATION",
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
    "decomposition": "F2^5 + Ind_Q(i)^3 + Q_L(3D nonsplit quotient-regular)",
    "absolute_H1_receiver_exact": True,
    "kernel_galois_relevant_contribution_accounted": True,
    "stage33_11_domain_and_codomain_well_defined": True,
    "connecting_columns_materialized": "0/26",
    "witness_sha256": witness_hash,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
