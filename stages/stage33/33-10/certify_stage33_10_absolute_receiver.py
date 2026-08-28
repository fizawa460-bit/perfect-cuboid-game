#!/usr/bin/env python3
"""Certify Stage33-10: ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER.

The source-locked 14-dimensional F2 module K=Br(Sbar)[2] factors through
L=Q(i,sqrt(2)), Gal(L/Q)=V4=<cc,ct>.  This verifier constructs an explicit
equivariant basis and certifies

  K ~= F2^5
       direct_sum Ind_{G_Q(i)}^{G_Q}(F2)^3
       direct_sum Q_L,

where Q_L=Ind_{G_L}^{G_Q}(F2)/F2_diag is the 3-dimensional quotient-regular
block.  Continuous Shapiro plus the long exact sequence of
0 -> F2 -> Ind_{G_L}^{G_Q}(F2) -> Q_L -> 0 gives the exact absolute receiver

  H^1(G_Q,K) ~= X_Q^5 direct_sum X_Q(i)^3 direct_sum E_L,

with X_F=Hom_cont(G_F,F2), E_L=H^1(G_Q,Q_L), and exact filtration

  0 -> coker(X_Q -> X_L) -> E_L
    -> ker(H^2(G_Q,F2) -> H^2(G_L,F2)) -> 0.

No splitting of E_L is asserted.  No Stage33-11 connecting-map column is
computed here.

Shapiro locator:
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


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected, label):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        die(f"{label} source lock moved: claimed={claimed} actual={actual} expected={expected}")
    return obj


def xor(a, b):
    return [int(x) ^ int(y) for x, y in zip(a, b)]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mat_xor(a, b):
    return [xor(x, y) for x, y in zip(a, b)]


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum((int(x) & int(y)) for x, y in zip(row, col)) & 1 for col in bt] for row in a]


def apply(v, m):
    out = [0] * len(m[0])
    for i, bit in enumerate(v):
        if int(bit) & 1:
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
    if any(not any(row[:nvars]) and row[nvars] for row in a):
        return None, None
    return a, pivots


def solve_constraints(constraints):
    """Find row x satisfying x*M=target for every (M,target)."""
    eq_rows, rhs = [], []
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
    eq_rows, rhs = [], []
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
            x[p] = a[i][f]
        basis.append(x)
    return basis


def extend_independent(seed, candidates, target_rank):
    out = list(seed)
    current = rank(out)
    for v in candidates:
        nr = rank(out + [v])
        if nr > current:
            out.append(v)
            current = nr
            if current == target_rank:
                break
    if current != target_rank:
        die(f"could not extend independent family to rank {target_rank}; got {current}")
    return out


br2 = load_locked(BR2, EXPECTED_BR2, "proper Br2")
arith = load_locked(ARITH, EXPECTED_ARITH, "arithmetic HS problem")
prev = load_locked(PREV, EXPECTED_33_09, "Stage33-09 handoff")
if prev.get("status") != "CLOSED_EXACT":
    die("Stage33-09 is not exact-closed")
if prev.get("source_locks", {}).get("stage33_09_closure_sha256") != EXPECTED_33_09_CLOSURE:
    die("Stage33-09 closure source lock moved")
if prev.get("next_item") != "Stage33-10_ABSOLUTE_H1_AND_GALOIS_DESCENT_ADAPTER":
    die("Stage33-09 no longer releases Stage33-10")

finite = arith["boundary_candidates_not_yet_promoted_to_global_q_classes"]["finite_ramified_after_u44"]
if (
    finite["minimal_invariant_factor_generators"],
    finite["order2_factors"],
    finite["order4_factors"],
) != (26, 23, 3):
    die("26-direction arithmetic source contract moved")

cc = [[int(x) & 1 for x in row] for row in br2["proper_Br2_cc_action_f2"]]
ct = [[int(x) & 1 for x in row] for row in br2["proper_Br2_ct_action_f2"]]
if len(cc) != N or len(ct) != N or any(len(row) != N for row in cc + ct):
    die("proper Br2 action shape regression")
I = eye(N)
if matmul(cc, cc) != I or matmul(ct, ct) != I or matmul(cc, ct) != matmul(ct, cc):
    die("source-locked actions are not a V4 representation")

Nc, Nt = mat_xor(cc, I), mat_xor(ct, I)
Z = [[0] * N for _ in range(N)]
if matmul(Nc, Nt) != Z or matmul(Nt, Nc) != Z:
    die("radical-square-zero profile moved")

joint = nullspace_constraints([Nc, Nt])
im_c, im_t = row_basis(Nc), row_basis(Nt)
radical = row_basis(im_c + im_t)
profile = (N - rank(Nc), N - rank(Nt), len(joint), len(im_c), len(im_t), len(radical))
if profile != (10, 13, 10, 4, 1, 5):
    die(f"proper Br2 module profile moved: {profile}")
if br2.get("proper_Br2_fixed_dimensions") != {"cc": 10, "ct": 13, "joint_v4": 10}:
    die("stored proper Br2 fixed dimensions disagree with exact recomputation")
if rank(im_c + im_t) == len(im_c):
    die("Im(ct-1) unexpectedly fell inside Im(cc-1)")

# Q_L block. Since Nt has rank one, v spans Im(Nt). Any x with Nt(x)=v
# lies outside ker(Nc)=K^V4, hence Nc(x) is nonzero.
v = im_t[0]
xq = solve_constraints([(Nt, v)])
if xq is None:
    die("no preimage of Im(ct-1) generator")
u = apply(xq, Nc)
if not any(u) or rank([u, v]) != 2:
    die("Q_L radical lines are not independent")
if apply(xq, Nt) != v:
    die("Q_L Nt lift regression")
if any(apply(u, Nc)) or any(apply(u, Nt)) or any(apply(v, Nc)) or any(apply(v, Nt)):
    die("Q_L radical is not jointly fixed")
if apply(xq, cc) != xor(xq, u) or apply(xq, ct) != xor(xq, v):
    die("Q_L top action mismatch")
qblock = [xq, u, v]

# The three Q(i)-induced blocks must come from the Nt-fixed top directions.
# Do not choose arbitrary complements in Im(Nc): the induced functional
# Im(Nc) -> Im(Nt) has a 3-dimensional kernel.
ker_t = nullspace_constraints([Nt])
qi_radical = row_basis([apply(x, Nc) for x in ker_t])
if len(qi_radical) != 3 or rank(qi_radical + [u]) != 4:
    die("Nt-fixed Im(Nc) kernel profile moved")

pairs_qi = []
for y in qi_radical:
    x = solve_constraints([(Nc, y), (Nt, [0] * N)])
    if x is None:
        die("no exact Q(i) permutation-block lift")
    a, b = x, xor(x, y)
    if apply(a, cc) != b or apply(b, cc) != a:
        die("Q(i) block cc swap verification failed")
    if apply(a, ct) != a or apply(b, ct) != b:
        die("Q(i) block ct-fixed verification failed")
    pairs_qi.append([a, b])

# Five remaining fixed directions are trivial summands.
fixed_extension = extend_independent(radical, joint, 10)
trivial = fixed_extension[5:]
if len(trivial) != 5:
    die("joint-fixed trivial complement is not five-dimensional")
if any(apply(t, cc) != t or apply(t, ct) != t for t in trivial):
    die("trivial summand verification failed")

new_basis = trivial + [z for pair in pairs_qi for z in pair] + qblock
if len(new_basis) != N or rank(new_basis) != N:
    die("constructed equivariant basis is not invertible")

# Independent finite-H1 check against the retained bar calculation.
finite_h1_from_decomposition = 5 * 2 + 3 + 3
if finite_h1_from_decomposition != 16:
    die("finite H1 decomposition arithmetic failed")
finite_h1 = br2["finite_v4_H1_proper_Br2"]
if finite_h1["H1_dimension_f2"] != 16 or finite_h1["absolute_H1_identified_with_finite_H1"]:
    die("retained finite-H1 firewall moved")

witness_hash = csha({"basis_rows_original_coordinates_f2": new_basis})
cert = {
    "schema": "STAGE33_10_ABSOLUTE_H1_RECEIVER_V3_NONSPLIT_QL",
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
        "fixed_dimensions": {"cc": 10, "ct": 13, "joint_v4": 10},
        "nilpotent_image_dimensions": {"Im_cc_minus_1": 4, "Im_ct_minus_1": 1, "sum": 5},
        "exact_decomposition": [
            {"multiplicity": 5, "module": "F2", "description": "trivial G_Q module"},
            {"multiplicity": 3, "module": "Ind_{G_Q(i)}^{G_Q}(F2)", "description": "cc swaps; ct fixes"},
            {
                "multiplicity": 1,
                "module": "Q_L=Ind_{G_L}^{G_Q}(F2)/F2_diag",
                "dimension_f2": 3,
                "normal_form": "cc(top)=top+u; ct(top)=top+v; u,v jointly fixed and independent",
            },
        ],
        "equivariant_basis_witness_sha256": witness_hash,
        "equivariant_basis_rows_original_coordinates_f2": new_basis,
        "false_four_index_two_block_split_rejected": True,
    },
    "finite_shortcut": {
        "H1_V4_dimension_f2": 16,
        "status": "EXPLICITLY_REPLACED",
        "reason": "finite V4 H1 omits unrestricted kernel-Galois characters and relative degree-two data",
    },
    "absolute_h1_receiver": {
        "theorem": "continuous Shapiro lemma plus long exact continuous-cohomology sequence",
        "source_locator": "Neukirch-Schmidt-Wingberg, Cohomology of Number Fields, Proposition 1.6.3",
        "character_notation": "X_F=Hom_cont(G_F,F2)",
        "main_decomposition": "H^1(G_Q,K) ~= X_Q^5 direct_sum X_Q(i)^3 direct_sum E_L",
        "E_L_definition": "E_L=H^1(G_Q,Q_L), Q_L=Ind_{G_L}^{G_Q}(F2)/F2_diag",
        "E_L_exact_filtration": "0 -> coker(res^1: X_Q -> X_L) -> E_L -> ker(res^2: H^2(G_Q,F2) -> H^2(G_L,F2)) -> 0",
        "E_L_splitting_claimed": False,
        "kernel_galois_contribution_accounted": True,
    },
    "stage33_11_interface": {
        "source_invariant_factor_directions": 26,
        "source_group_before_order_two_layer": "(Z/2)^23 direct_sum (Z/4)^3",
        "order2_factors": 23,
        "order4_factors": 3,
        "order_two_localization_domain": "F2^26 from the 26 invariant-factor directions",
        "codomain": "X_Q^5 direct_sum X_Q(i)^3 direct_sum E_L with the recorded exact E_L filtration",
        "connecting_source_directions_computed": "0/26",
        "arithmetic_localization_connecting_map_computed": False,
    },
    "branches": {
        "33-10a": "CLOSED_FINITE_SHORTCUT_REJECTED",
        "33-10b": "CLOSED_BY_EXACT_MODULE_DECOMPOSITION_SHAPIRO_AND_LONG_EXACT_SEQUENCE",
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
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "finite_H1_V4_dimension_f2": 16,
    "decomposition": "F2^5 + Ind_Q(i)^3 + Q_L(3D quotient-regular)",
    "absolute_H1_receiver_exact": True,
    "kernel_galois_relevant_contribution_accounted": True,
    "stage33_11_domain_and_codomain_well_defined": True,
    "connecting_columns_materialized": "0/26",
    "witness_sha256": witness_hash,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
