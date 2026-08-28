#!/usr/bin/env python3
"""Certify the exact Stage33-10 absolute H1 receiver.

The finite V4 H1 from Stage33-07 is not the absolute G_Q receiver. We put the
exact proper geometric Br[2] V4-module into a deterministic direct-sum normal
form, then apply Shapiro, Kummer, and the long exact sequence attached to the
one non-permutation quotient block.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
N = 14


def canonical_hash(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str | None = None):
    obj = json.loads(path.read_text(encoding="utf-8"))
    got = canonical_hash(obj)
    if obj.get("canonical_sha256") != got:
        raise SystemExit(f"canonical hash regression: {path}")
    if expected is not None and got != expected:
        raise SystemExit(f"source lock moved: {path}: {got}")
    return obj, got


def git_blob_sha(path: Path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def rank2(rows):
    a = [[int(x) & 1 for x in row] for row in rows]
    if not a:
        return 0
    r = 0
    n = len(a[0])
    for c in range(n):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) & 1 for j in range(len(B[0]))] for i in range(len(A))]


def xor_matrix(A, B):
    return [[A[i][j] ^ B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mask_to_row(v, n=N):
    return [(v >> i) & 1 for i in range(n)]


def act(v, M):
    row = mask_to_row(v, len(M))
    out = [sum(row[i] * M[i][j] for i in range(len(M))) & 1 for j in range(len(M))]
    m = 0
    for i, b in enumerate(out):
        if b:
            m |= 1 << i
    return m


def delta(v, M):
    return v ^ act(v, M)


def add_to_basis(basis, v):
    x = v
    for b in basis:
        p = b.bit_length() - 1
        if (x >> p) & 1:
            x ^= b
    if x == 0:
        return False
    p = x.bit_length() - 1
    for i, b in enumerate(basis):
        if (b >> p) & 1:
            basis[i] = b ^ x
    basis.append(x)
    basis.sort(reverse=True)
    return True


def independent(vs):
    b = []
    for v in vs:
        add_to_basis(b, v)
    return len(b)


def target_actions():
    cc = eye(N)
    ct = eye(N)
    # basis: t1..t5, (w1,x1),(w2,x2),(w3,x3),(w4,z,x4)
    for x, w in ((6, 5), (8, 7), (10, 9), (13, 11)):
        cc[x][w] ^= 1
    ct[13][12] ^= 1
    return cc, ct


proper, proper_sha = load_locked(
    S33 / "33-07" / "proper-brauer2-from-discriminant.json",
    "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
)
handoff09, handoff09_sha = load_locked(
    S33 / "33-09" / "handoff.json",
    "9d385fd8ccddbf2d6f5289d944c4e80523ba39310d165c0741d9b5c33698e573",
)
extractor = S33 / "33-03" / "extract_galois_action.py"
extractor_blob = git_blob_sha(extractor)
if extractor_blob != "d81c00d3d361a8a08283150cc9fb6271cac8731f":
    raise SystemExit("Stage33-03 named cc/ct source lock moved")
if handoff09["status"] != "CLOSED_EXACT" or not all(handoff09["exit_condition"].values()):
    raise SystemExit("Stage33-09 prerequisite regression")
if handoff09["source_locks"]["stage33_09_closure_sha256"] != "6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7":
    raise SystemExit("Stage33-09 closure source lock moved")
if proper["proper_geometric_Br2_dimension_f2"] != N:
    raise SystemExit("proper Br[2] dimension regression")
if proper["finite_v4_H1_proper_Br2"]["H1_dimension_f2"] != 16:
    raise SystemExit("finite V4 H1 regression")
if proper["finite_v4_H1_proper_Br2"]["absolute_H1_identified_with_finite_H1"]:
    raise SystemExit("historical finite/absolute firewall regressed")

Bcc = [[int(x) & 1 for x in row] for row in proper["proper_Br2_cc_action_f2"]]
Bct = [[int(x) & 1 for x in row] for row in proper["proper_Br2_ct_action_f2"]]
I = eye(N)
zero = [[0] * N for _ in range(N)]
if mm(Bcc, Bcc) != I or mm(Bct, Bct) != I or mm(Bcc, Bct) != mm(Bct, Bcc):
    raise SystemExit("proper Br[2] V4 action regression")
Ncc = xor_matrix(Bcc, I)
Nct = xor_matrix(Bct, I)
if mm(Ncc, Ncc) != zero or mm(Nct, Nct) != zero or mm(Ncc, Nct) != zero or mm(Nct, Ncc) != zero:
    raise SystemExit("radical-square-zero module regression")

allv = range(1 << N)
common_fixed = [v for v in allv if delta(v, Bcc) == 0 and delta(v, Bct) == 0]
cc_fixed = [v for v in allv if delta(v, Bcc) == 0]
ct_fixed = [v for v in allv if delta(v, Bct) == 0]
if (len(cc_fixed), len(ct_fixed), len(common_fixed)) != (1 << 10, 1 << 13, 1 << 10):
    raise SystemExit("fixed-space census regression")

im_cc, im_ct = [], []
for i in range(N):
    add_to_basis(im_cc, delta(1 << i, Bcc))
    add_to_basis(im_ct, delta(1 << i, Bct))
combined_image = list(im_cc)
for b in im_ct:
    add_to_basis(combined_image, b)
if (len(im_cc), len(im_ct), len(combined_image)) != (4, 1, 5):
    raise SystemExit("radical image dimensions regression")
if set(cc_fixed) != set(common_fixed):
    raise SystemExit("ker(cc-1) must equal joint invariant space")

# The unique ct-arrow gives the 3-dimensional quotient-regular block. Three
# complementary cc-arrows give Q(i) permutation blocks. Five invariant
# directions remain as trivial direct summands.
x4 = next(v for v in allv if delta(v, Bct) != 0)
w4 = delta(x4, Bcc)
z = delta(x4, Bct)
if independent([w4, z]) != 2:
    raise SystemExit("full-V4 quotient block collapsed")

image_basis = [w4]
pairs = []
for v in allv:
    if delta(v, Bct) != 0:
        continue
    w = delta(v, Bcc)
    if w and independent(image_basis + [w]) > len(image_basis):
        image_basis.append(w)
        pairs.append((w, v))
        if len(pairs) == 3:
            break
if len(pairs) != 3 or independent(image_basis) != 4:
    raise SystemExit("three Q(i) permutation blocks not found")

radical = [w for w, _ in pairs] + [w4, z]
if independent(radical) != 5:
    raise SystemExit("radical basis regression")
span = []
for v in radical:
    add_to_basis(span, v)
trivials = []
for v in common_fixed:
    trial = list(span)
    if add_to_basis(trial, v):
        span = trial
        trivials.append(v)
        if len(trivials) == 5:
            break
if len(trivials) != 5 or len(span) != 10:
    raise SystemExit("five trivial direct summands not found")

basis_masks = list(trivials)
for w, x in pairs:
    basis_masks.extend([w, x])
basis_masks.extend([w4, z, x4])
if independent(basis_masks) != N:
    raise SystemExit("normal-form basis is not invertible")
P = [mask_to_row(v) for v in basis_masks]
Tcc, Tct = target_actions()
if mm(P, Bcc) != mm(Tcc, P) or mm(P, Bct) != mm(Tct, P):
    raise SystemExit("module conjugacy to target normal form failed")

# Direct finite-H1 replay.
eq = []
for j in range(N):
    eq.append([Ncc[i][j] for i in range(N)] + [0] * N)
for j in range(N):
    eq.append([0] * N + [Nct[i][j] for i in range(N)])
for j in range(N):
    eq.append([Nct[i][j] for i in range(N)] + [Ncc[i][j] for i in range(N)])
cocycle_dim = 2 * N - rank2(eq)
coboundary_dim = rank2([Ncc[i] + Nct[i] for i in range(N)])
finite_h1_dim = cocycle_dim - coboundary_dim
if (cocycle_dim, coboundary_dim, finite_h1_dim) != (20, 4, 16):
    raise SystemExit("finite H1 direct regression")

module_decomposition = {
    "field_K": "Q(i,sqrt(2))",
    "named_generators": {"cc": "i -> -i, sqrt(2) fixed", "ct": "sqrt(2) -> -sqrt(2), i fixed"},
    "exact_v4_module": "F2^5_trivial direct_sum Ind_{G_Q(i)}^{G_Q}(F2)^3 direct_sum J_K",
    "J_K": "Ind_{G_K}^{G_Q}(F2) / F2*Norm_V4",
    "dimensions": {"trivial": 5, "three_Qi_induced": 6, "J_K": 3, "total": 14},
    "normal_form_basis_rows_in_proper_Br2_coordinates": P,
    "basis_labels": ["t1", "t2", "t3", "t4", "t5", "w1", "x1", "w2", "x2", "w3", "x3", "w4", "z", "x4"],
    "normal_form_cc_action_f2": Tcc,
    "normal_form_ct_action_f2": Tct,
    "radical_image_dimension_f2": 5,
    "joint_fixed_dimension_f2": 10,
}
absolute = {
    "H1_GQ_proper_Br2": "(Q^*/Q^{*2})^5 direct_sum (Q(i)^*/Q(i)^{*2})^3 direct_sum H1(G_Q,J_K)",
    "J_K_short_exact_sequence": "0 -> coker[Q^*/Q^{*2} -> K^*/K^{*2}] -> H1(G_Q,J_K) -> ker[Br(Q)[2] -> Br(K)[2]] -> 0",
    "K": "Q(i,sqrt(2))",
    "derivation": [
        "direct V4-module decomposition above",
        "Shapiro: H1(G_Q,Ind_{G_F}^{G_Q} F2)=H1(G_F,F2)",
        "Kummer: H1(G_F,F2)=F^*/F^{*2}",
        "0 -> F2 -> Ind_{G_K}^{G_Q}F2 -> J_K -> 0",
        "Shapiro + long exact sequence, with H2(G_F,F2)=Br(F)[2]",
    ],
    "all_absolute_classes_accounted": True,
    "finite_dimensional_claim_for_absolute_H1": False,
}
cert = {
    "schema": "STAGE33_10_ABSOLUTE_H1_GALOIS_DESCENT_ADAPTER_V1",
    "stage": "33-10",
    "name": "ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER",
    "source_locks": {
        "proper_brauer2_from_discriminant_sha256": proper_sha,
        "stage33_09_handoff_sha256": handoff09_sha,
        "stage33_09_closure_sha256": handoff09["source_locks"]["stage33_09_closure_sha256"],
        "stage33_03_galois_extractor_git_blob_sha1": extractor_blob,
        "upstream_git_blob_sha1": handoff09["source_locks"]["upstream_git_blob_sha1"],
    },
    "finite_v4_receiver": {
        "H1_dimension_f2": finite_h1_dim,
        "cocycle_dimension_f2": cocycle_dim,
        "coboundary_dimension_f2": coboundary_dim,
        "inflation_into_absolute_H1_injective": True,
        "equals_absolute_H1": False,
        "shortcut_status": "PROVED_INVALID_EXPLICITLY_REPLACED",
        "reason": "absolute H1 contains five direct copies of Q^*/Q^{*2}, hence is not the finite 16-dimensional V4 H1",
    },
    "module_decomposition": module_decomposition,
    "absolute_receiver": absolute,
    "inflation_restriction_consistency": {
        "splitting_field": "K=Q(i,sqrt(2))",
        "kernel": "G_K",
        "kernel_action_on_proper_Br2": "trivial",
        "five_term_sequence": "0 -> H1(V4,M) -> H1(G_Q,M) -> H1(G_K,M)^V4 -> H2(V4,M)",
        "kernel_galois_relevant_contribution_accounted": True,
        "accounting_method": "direct module decomposition plus Shapiro/Kummer/relative-Brauer long exact sequence",
    },
    "stage33_11_interface": {
        "source_directions": 26,
        "domain": "(Z/2)^23 direct_sum (Z/4)^3 minimal invariant-factor directions",
        "order2_localization_codom": "H1(G_Q, proper geometric Br[2]) as absolute_receiver above",
        "domain_and_codomain_well_defined": True,
        "connecting_columns_materialized": "0/26",
        "stage33_11_released": True,
    },
    "branches": {
        "33-10a_finite_shortcut": "CLOSED_NEGATIVE_PROVED_INVALID",
        "33-10b_inflation_restriction": "ACCOUNTED_BY_DIRECT_DECOMPOSITION",
        "33-10c_kernel_galois": "ACCOUNTED_BY_SHAPIRO_KUMMER_RELATIVE_BRAUER_PACKAGE",
        "33-10d_direct_absolute_h1": "CLOSED_EXACT",
        "33-10e_absolute_receiver_certification": "CLOSED_EXACT",
    },
    "exit_condition": {
        "absolute_h1_receiver_exact": True,
        "finite_v4_shortcut_status_proved_valid_or_explicitly_replaced": True,
        "kernel_galois_relevant_contribution_accounted": True,
        "stage33_11_domain_and_codomain_well_defined": True,
    },
    "status": "CLOSED_EXACT",
    "parent_big_task": "33-07",
    "stage33_progress": "6/11",
    "stage33_07_closed": False,
    "stage33_08_released": False,
    "arithmetic_localization_connecting_map_computed": False,
    "connecting_matrix_columns_materialized": "0/26",
    "arithmetic_hs_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_hash(cert)
(HERE / "absolute-h1-galois-descent-adapter.json").write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

closure = {
    "schema": "STAGE33_10_CLOSURE_V1", "stage": "33-10", "status": "CLOSED_EXACT", "parent_big_task": "33-07",
    "source_locks": {"absolute_h1_adapter_sha256": cert["canonical_sha256"]}, "exit_condition": cert["exit_condition"],
    "finite_v4_shortcut_status": "PROVED_INVALID_EXPLICITLY_REPLACED", "absolute_h1_receiver_exact": True,
    "kernel_galois_relevant_contribution_accounted": True, "stage33_11_domain_and_codomain_well_defined": True,
    "stage33_11_released": True, "stage33_progress": "6/11", "stage33_07_closed": False, "stage33_08_released": False,
    "connecting_matrix_columns_materialized": "0/26", "arithmetic_localization_connecting_map_computed": False,
    "arithmetic_hs_closed": False, "theorem_credit": False, "endpoint_credit": False, "perfect_cuboid_nonexistence_claim": False,
}
closure["canonical_sha256"] = canonical_hash(closure)
(HERE / "stage33-10-closure.json").write_text(json.dumps(closure, indent=2, sort_keys=True) + "\n", encoding="utf-8")

handoff = {
    "schema": "STAGE33_10_HANDOFF_V1", "stage": "33-10", "name": "ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER",
    "status": "CLOSED_EXACT", "parent_big_task": "33-07",
    "source_locks": {"absolute_h1_adapter_sha256": cert["canonical_sha256"], "stage33_10_closure_sha256": closure["canonical_sha256"]},
    "exit_condition": cert["exit_condition"],
    "firewalls": {"stage33_progress": "6/11", "stage33_07_closed": False, "stage33_08_released": False,
                  "connecting_matrix_columns_materialized": "0/26", "arithmetic_localization_connecting_map_computed": False,
                  "arithmetic_hs_closed": False, "theorem_credit": False, "endpoint_credit": False},
    "next_item": "Stage33-11_ARITHMETIC_LOCALIZATION_CONNECTING_MAP", "next_expected_command": "Stage33-main-batch",
}
handoff["canonical_sha256"] = canonical_hash(handoff)
(HERE / "handoff.json").write_text(json.dumps(handoff, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(json.dumps({
    "success": True, "finite_v4_H1_dimension_f2": finite_h1_dim,
    "finite_v4_shortcut": "PROVED_INVALID_EXPLICITLY_REPLACED", "module": module_decomposition["exact_v4_module"],
    "absolute_H1": absolute["H1_GQ_proper_Br2"], "ABSOLUTE_H1_RECEIVER_EXACT": True,
    "KERNEL_GALOIS_RELEVANT_CONTRIBUTION_ACCOUNTED": True, "STAGE33_11_DOMAIN_AND_CODOMAIN_WELL_DEFINED": True,
    "adapter_sha256": cert["canonical_sha256"], "closure_sha256": closure["canonical_sha256"], "handoff_sha256": handoff["canonical_sha256"],
}, indent=2, sort_keys=True))
