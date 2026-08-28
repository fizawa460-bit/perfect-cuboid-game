#!/usr/bin/env python3
"""Stage33-11 exact global naturality on Picard discriminant 2-torsion.

For an integral lattice L with Gram G (row convention),

    A_L[2] = (L^*/L)[2]  ~=  { z mod 2 : z G = 0 mod 2 },

via z -> z/2 mod L.  Thus no integral Smith transform is needed for the
2-primary order-two receiver: the proper geometric Br[2] module is computed
as the exact F2 left kernel of the source-locked 64x64 Picard Gram.  Every
Q-defined Picard automorphism acts directly on this kernel by z -> z A.

The rest is the same two-step absolute-H1 naturality argument as the direct
Smith scout.  It never identifies absolute H1 with finite V4 H1.
"""
from __future__ import annotations

import hashlib
import json
import runpy
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
LEGACY = STAGE33 / "33-07"
PREV09 = STAGE33 / "33-09" / "handoff.json"
BRIDGE09 = STAGE33 / "33-09" / "marked-picard-basis-bridge-certified.json"
PREV10 = STAGE33 / "33-10" / "handoff.json"
BR2_PATH = LEGACY / "proper-brauer2-from-discriminant.json"
SIGN_SCRIPT = LEGACY / "certify_retained_geometric_sign_intertwiner_space.py"
SWAP_PICARD_SCRIPT = LEGACY / "certify_two_coordinate_swap_picard_rows.py"
OLD_BASE_SCRIPT = LEGACY / "picard_base_rows_retained.py"
OLD_SIGN_SCRIPT = LEGACY / "picard_coordinate_sign_rows_retained.py"
OUT = HERE / "stage33-11-kernel-mod2-naturality.json"

EXPECTED_09 = "9d385fd8ccddbf2d6f5289d944c4e80523ba39310d165c0741d9b5c33698e573"
EXPECTED_09_CLOSURE = "6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7"
EXPECTED_09_BRIDGE = "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92"
EXPECTED_10 = "4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f"
EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_SEVEN_SIGN_H1_HOM_DIM = 146
QDIM = 26
KDIM = 14
H1DIM = 16
PICRANK = 64


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str, label: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"{label} source lock moved: claimed={claimed} actual={actual} expected={expected}")
    return obj


def zmat(raw, label: str) -> list[list[int]]:
    if not isinstance(raw, list) or len(raw) != PICRANK or any(not isinstance(r, list) or len(r) != PICRANK for r in raw):
        raise SystemExit(f"{label}: expected 64x64 matrix")
    if any(type(x) is not int for r in raw for x in r):
        raise SystemExit(f"{label}: nonintegral entry")
    return [[int(x) for x in r] for r in raw]


def matmul_z(A, B):
    return [[sum(int(A[i][k]) * int(B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(M):
    return [list(x) for x in zip(*M)]


def gf2_rref(rows: list[list[int]], n: int):
    a = [[int(x) & 1 for x in row[:n]] for row in rows if any(int(x) & 1 for x in row[:n])]
    pivots = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a[:r], pivots


def gf2_nullspace_rows(M: list[list[int]], n: int) -> list[list[int]]:
    # Right nullspace of M; for symmetric G these are also the left-kernel rows.
    rref, pivots = gf2_rref(M, n)
    free = [j for j in range(n) if j not in pivots]
    out = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, p in enumerate(pivots):
            v[p] = rref[i][f]
        out.append(v)
    return out


def solve_in_row_basis(v: list[int], basis: list[list[int]]) -> list[int]:
    # Solve c*basis=v by pivoting the augmented row system on basis coordinates.
    d = len(basis)
    n = len(v)
    cols = [[basis[i][j] & 1 for i in range(d)] for j in range(n)]
    eq = [cols[j] + [v[j] & 1] for j in range(n)]
    r = 0
    pivot_cols = []
    for c in range(d):
        p = next((i for i in range(r, len(eq)) if eq[i][c]), None)
        if p is None:
            continue
        eq[r], eq[p] = eq[p], eq[r]
        for i in range(len(eq)):
            if i != r and eq[i][c]:
                eq[i] = [x ^ y for x, y in zip(eq[i], eq[r])]
        pivot_cols.append(c)
        r += 1
    if len(pivot_cols) != d:
        raise SystemExit("kernel basis solver lost full rank")
    if any(not any(row[:d]) and row[d] for row in eq):
        raise SystemExit("vector escaped kernel basis")
    x = [0] * d
    for row in eq:
        p = next((j for j in range(d) if row[j]), None)
        if p is not None:
            x[p] = row[d]
    return x


def rowmul2(v, M):
    return [sum((int(v[k]) & 1) * (int(M[k][j]) & 1) for k in range(len(v))) & 1 for j in range(len(M[0]))]


def matmul2(A, B):
    return [rowmul2(r, B) for r in A]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def sub2(A, B):
    return [[(int(x) ^ int(y)) & 1 for x, y in zip(ar, br)] for ar, br in zip(A, B)]


def hom_dimension(source_actions, target_actions, sdim: int, tdim: int, rank_bitmasks) -> tuple[int, int]:
    if len(source_actions) != len(target_actions):
        raise SystemExit("source/target generator count mismatch")
    equations = []
    for S, T in zip(source_actions, target_actions):
        for i in range(sdim):
            for j in range(tdim):
                mask = 0
                for k in range(sdim):
                    if int(S[i][k]) & 1:
                        mask ^= 1 << (k * tdim + j)
                for ell in range(tdim):
                    if int(T[ell][j]) & 1:
                        mask ^= 1 << (i * tdim + ell)
                if mask:
                    equations.append(mask)
    rk = rank_bitmasks(equations)
    return sdim * tdim - rk, rk


sys.path.insert(0, str(LEGACY))
prev09 = load_locked(PREV09, EXPECTED_09, "Stage33-09 handoff")
bridge09 = load_locked(BRIDGE09, EXPECTED_09_BRIDGE, "Stage33-09 marked Picard bridge")
prev10 = load_locked(PREV10, EXPECTED_10, "Stage33-10 handoff")
br2 = load_locked(BR2_PATH, EXPECTED_BR2, "proper geometric Br2")
if prev09.get("status") != "CLOSED_EXACT" or prev09.get("source_locks", {}).get("stage33_09_closure_sha256") != EXPECTED_09_CLOSURE:
    raise SystemExit("Stage33-09 exact closure lock moved")
if prev10.get("status") != "CLOSED_EXACT" or not prev10.get("exit_condition", {}).get("absolute_h1_receiver_exact"):
    raise SystemExit("Stage33-10 exact absolute receiver lock moved")
if prev10.get("exact_receiver", {}).get("finite_v4_shortcut_status") != "EXPLICITLY_REPLACED":
    raise SystemExit("Stage33-10 finite-V4 firewall moved")
if br2["finite_v4_H1_proper_Br2"]["H1_dimension_f2"] != H1DIM:
    raise SystemExit("Stage33-10 finite diagnostic H1 dimension moved")

sign = runpy.run_path(str(SIGN_SCRIPT))
rank2 = sign["rank2"]
row_basis = sign["row_basis"]
nullspace2 = sign["nullspace2"]
build_solver = sign["build_solver"]
rank_bitmasks = sign["rank_bitmasks"]
rowmul_z = sign["rowmul_z"]
permute_vector = sign["permute_vector"]
source_sign_actions = sign["source_sign_actions"]
if len(source_sign_actions) != 7:
    raise SystemExit("source seven-sign coverage moved")

old = runpy.run_path(str(OLD_BASE_SCRIPT))["load"]()
old_sign = runpy.run_path(str(OLD_SIGN_SCRIPT))["load"]()
locks09 = bridge09["source_locks"]
if old["canonical_sha256"] != locks09["retained_old_picard_base_sha256"]:
    raise SystemExit("historical Picard base lock differs from Stage33-09")
if old_sign["canonical_sha256"] != locks09["retained_old_picard_signs_sha256"]:
    raise SystemExit("historical Picard sign lock differs from Stage33-09")
order = list(old_sign["coordinate_order"])
if order != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
    raise SystemExit("historical sign order moved")

Gz = zmat(old["picard_gram_64x64"], "historical Picard Gram")
A_cc_z = zmat(old["picard_action_cc_64x64"], "historical cc")
A_ct_z = zmat(old["picard_action_ct_64x64"], "historical ct")
A_signs_z = [zmat(old_sign["picard_actions_64x64"][name], f"historical sign {name}") for name in order]
swaps09 = bridge09["actual_coordinate_swaps_in_historical_magma_picard_basis"]
A_swap12_z = zmat(swaps09["swap12_action_64x64"], "Stage33-09 actual swap12")
A_swap13_z = zmat(swaps09["swap13_action_64x64"], "Stage33-09 actual swap13")

# Integral isometry regressions before reduction mod 2.
Gsp = sp.Matrix(Gz)
I64 = sp.eye(PICRANK)
for name, raw in [("cc", A_cc_z), ("ct", A_ct_z)] + [(f"sign_{n}", A) for n, A in zip(order, A_signs_z)] + [("swap12", A_swap12_z), ("swap13", A_swap13_z)]:
    A = sp.Matrix(raw)
    if A * A != I64 or A * Gsp * A.T != Gsp:
        raise SystemExit(f"{name}: historical Picard involution/isometry regression")
if sp.Matrix(A_swap12_z) * sp.Matrix(A_swap13_z) * sp.Matrix(A_swap12_z) != sp.Matrix(A_swap13_z) * sp.Matrix(A_swap12_z) * sp.Matrix(A_swap13_z):
    raise SystemExit("historical actual swaps lost S3 braid")

G2 = [[x & 1 for x in row] for row in Gz]
kernel_basis = gf2_nullspace_rows(G2, PICRANK)
if len(kernel_basis) != KDIM:
    raise SystemExit(f"Picard mod-2 kernel dimension moved: {len(kernel_basis)}")
if any(any(rowmul2(b, G2)) for b in kernel_basis):
    raise SystemExit("Picard mod-2 kernel basis verification failed")


def induce_kernel(name: str, rawA: list[list[int]]) -> list[list[int]]:
    A2 = [[x & 1 for x in row] for row in rawA]
    rows = []
    for b in kernel_basis:
        image = rowmul2(b, A2)
        if any(rowmul2(image, G2)):
            raise SystemExit(f"{name}: Picard action escaped discriminant 2-torsion kernel")
        rows.append(solve_in_row_basis(image, kernel_basis))
    if rank2(rows, KDIM) != KDIM or matmul2(rows, rows) != eye(KDIM):
        raise SystemExit(f"{name}: induced kernel action is not an involutive automorphism")
    return rows


B_cc = induce_kernel("cc", A_cc_z)
B_ct = induce_kernel("ct", A_ct_z)
B_signs = [induce_kernel(f"sign_{n}", A) for n, A in zip(order, A_signs_z)]
B_swaps = [induce_kernel("swap12", A_swap12_z), induce_kernel("swap13", A_swap13_z)]
I14 = eye(KDIM)
if matmul2(B_cc, B_ct) != matmul2(B_ct, B_cc):
    raise SystemExit("kernel V4 actions ceased commuting")
for name, B in [(f"sign_{n}", B) for n, B in zip(order, B_signs)] + [("swap12", B_swaps[0]), ("swap13", B_swaps[1])]:
    if matmul2(B, B_cc) != matmul2(B_cc, B) or matmul2(B, B_ct) != matmul2(B_ct, B):
        raise SystemExit(f"{name}: Q-defined kernel action fails V4 commutation")
if matmul2(matmul2(B_swaps[0], B_swaps[1]), B_swaps[0]) != matmul2(matmul2(B_swaps[1], B_swaps[0]), B_swaps[1]):
    raise SystemExit("kernel actual swaps lost S3 braid")

# Independent V4 cohomology regression against the retained proper-Br2 receiver.
Ng = sub2(B_cc, I14)
Nh = sub2(B_ct, I14)
fixed_eq = []
for j in range(KDIM):
    fixed_eq.append([Ng[i][j] for i in range(KDIM)])
for j in range(KDIM):
    fixed_eq.append([Nh[i][j] for i in range(KDIM)])
joint_fixed_dim = KDIM - rank2(fixed_eq, KDIM)
if joint_fixed_dim != int(br2["proper_Br2_joint_V4_fixed_dimension_f2"]):
    raise SystemExit(f"kernel K joint fixed dimension mismatch: {joint_fixed_dim}")
eq = []
for j in range(KDIM):
    eq.append([Ng[i][j] for i in range(KDIM)] + [0] * KDIM)
for j in range(KDIM):
    eq.append([0] * KDIM + [Nh[i][j] for i in range(KDIM)])
for j in range(KDIM):
    eq.append([Nh[i][j] for i in range(KDIM)] + [Ng[i][j] for i in range(KDIM)])
z1 = nullspace2(eq, 2 * KDIM)
b1, _ = row_basis([Ng[i] + Nh[i] for i in range(KDIM)], 2 * KDIM)
if (len(z1), len(b1)) != (20, 4):
    raise SystemExit(f"kernel finite V4 receiver mismatch: Z1={len(z1)} B1={len(b1)}")
frame = list(b1)
h1 = []
for z in z1:
    if rank2(frame + [z], 2 * KDIM) > len(frame):
        frame.append(z)
        h1.append(z)
if len(h1) != H1DIM or rank2(frame, 2 * KDIM) != 20:
    raise SystemExit("kernel finite H1 quotient complement regression")
solve_h1 = build_solver(frame)


def induce_h1(name: str, proper: list[list[int]]) -> list[list[int]]:
    action = []
    for z in h1:
        transformed = rowmul2(z[:KDIM], proper) + rowmul2(z[KDIM:], proper)
        coeff = solve_h1(transformed)
        action.append(coeff[len(b1):])
    if rank2(action, H1DIM) != H1DIM or matmul2(action, action) != eye(H1DIM):
        raise SystemExit(f"{name}: induced finite-H1 action regression")
    return action


H1_signs = [induce_h1(f"sign_{n}", B) for n, B in zip(order, B_signs)]
H1_swaps = [induce_h1("swap12", B_swaps[0]), induce_h1("swap13", B_swaps[1])]
if matmul2(matmul2(H1_swaps[0], H1_swaps[1]), H1_swaps[0]) != matmul2(matmul2(H1_swaps[1], H1_swaps[0]), H1_swaps[1]):
    raise SystemExit("finite H1 actual swaps lost S3 braid")

seven_hom_dim, seven_hom_rank = hom_dimension(source_sign_actions, H1_signs, QDIM, H1DIM, rank_bitmasks)
if seven_hom_dim != EXPECTED_SEVEN_SIGN_H1_HOM_DIM:
    raise SystemExit(f"kernel-mod2 seven-sign Hom regression: got {seven_hom_dim}, expected 146")

# Reconstruct source-side coordinate-swap actions from the exact boundary
# permutations, exactly as in the direct Smith scout.
pic = runpy.run_path(str(SWAP_PICARD_SCRIPT))
boundaries = pic["boundaries"]
if [r["action"] for r in boundaries] != ["swap12", "swap13"]:
    raise SystemExit("source coordinate-swap boundary ordering regression")
edges = sign["edges"]
edge_index = sign["edge_index"]
U44 = sign["U44"]
R17 = sign["R17"]
O4 = sign["O4"]
solve61 = sign["solve61"]
Tsource = sign["T"]
diag29 = sign["diag29"]
relation29 = sign["relation29"]
source_basis = sign["source_basis"]
support_to_source = sign["support_to_source"]


def source_action_from_boundary(name: str, side1: list[int], point1: list[int]) -> list[list[int]]:
    sidep = [int(x) - 1 for x in side1]
    pointp = [int(x) - 1 for x in point1]
    if sorted(sidep) != list(range(24)) or sorted(pointp) != list(range(48)):
        raise SystemExit(f"{name}: boundary permutation shape regression")
    vertex_perm = sidep + [24 + x for x in pointp]
    edge_perm = [edge_index[(vertex_perm[a], vertex_perm[b])] for a, b in edges]
    if sorted(edge_perm) != list(range(144)):
        raise SystemExit(f"{name}: crossing permutation regression")
    for u in U44:
        coords = solve61(permute_vector(u, edge_perm, 2))
        if any(coords[44:]):
            raise SystemExit(f"{name}: U44 escaped itself")
    r_action = []
    for row in R17:
        coords = solve61(permute_vector(row, edge_perm, 2))
        r_action.append([int(x) & 1 for x in coords[44:]])
    o_action = []
    for j, row in enumerate(O4):
        image = permute_vector(row, edge_perm, 4)
        matches = []
        for k, target in enumerate(O4):
            if image == target:
                matches.append((k, 1))
            if image == [(-int(x)) % 4 for x in target]:
                matches.append((k, -1))
        if len(matches) != 1:
            raise SystemExit(f"{name}: O4_{j+1} not a unique signed generator: {matches}")
        o_action.append(matches[0])
    A29 = []
    for i in range(17):
        A29.append(r_action[i] + [0] * 12)
    for j in range(12):
        row = [0] * 29
        target, sgn = o_action[j]
        row[17 + target] = sgn
        A29.append(row)
    for rel in relation29:
        smith_rel = rowmul_z(rowmul_z(rel, A29), Tsource)
        if any(smith_rel[j] % diag29[j] for j in range(29)):
            raise SystemExit(f"{name}: exact source relation lattice not preserved")
    out_rows = []
    for rec in source_basis:
        original_coords = [int(x) for x in rec["original_R17_O12_coordinates_Z29"]]
        smith = rowmul_z(rowmul_z(original_coords, A29), Tsource)
        out = [0] * QDIM
        for j, d in enumerate(diag29):
            value = smith[j] % d
            if not value:
                continue
            if j not in support_to_source:
                raise SystemExit(f"{name}: source image hit trivial Smith coordinate {j}")
            source_index, basis_value = support_to_source[j]
            if value != basis_value % d:
                raise SystemExit(f"{name}: source image not A2 basis-valued at Smith {j}")
            out[source_index] ^= 1
        out_rows.append(out)
    if rank2(out_rows, QDIM) != QDIM or matmul2(out_rows, out_rows) != eye(QDIM):
        raise SystemExit(f"{name}: source A2 action not involutive automorphism")
    return out_rows


source_swaps = [source_action_from_boundary(rec["action"], rec["side_permutation_1based"], rec["exceptional_permutation_1based"]) for rec in boundaries]
if matmul2(matmul2(source_swaps[0], source_swaps[1]), source_swaps[0]) != matmul2(matmul2(source_swaps[1], source_swaps[0]), source_swaps[1]):
    raise SystemExit("source A2 actual swaps lost S3 braid")

source_actions = source_sign_actions + source_swaps
K_actions = B_signs + B_swaps
H1_actions = H1_signs + H1_swaps
generator_names = ["sign_" + n for n in order] + ["swap12", "swap13"]
hom_A_K_dim, hom_A_K_rank = hom_dimension(source_actions, K_actions, QDIM, KDIM, rank_bitmasks)
hom_A_H1_dim, hom_A_H1_rank = hom_dimension(source_actions, H1_actions, QDIM, H1DIM, rank_bitmasks)
absolute_zero = hom_A_K_dim == 0 and hom_A_H1_dim == 0

cert = {
    "schema": "STAGE33_11_KERNEL_MOD2_GLOBAL_NATURALITY_V1",
    "stage": "33-11",
    "branch": "33-11a_GLOBAL_ALL_AT_ONCE_26_COLUMN_CLOSURE",
    "source_locks": {
        "stage33_09_handoff_sha256": EXPECTED_09,
        "stage33_09_closure_sha256": EXPECTED_09_CLOSURE,
        "stage33_09_marked_picard_bridge_sha256": EXPECTED_09_BRIDGE,
        "stage33_10_handoff_sha256": EXPECTED_10,
        "proper_brauer2_sha256": EXPECTED_BR2,
        "historical_picard_base_sha256": old["canonical_sha256"],
        "historical_picard_signs_sha256": old_sign["canonical_sha256"],
    },
    "discriminant_two_torsion_model": {
        "model": "A_Pic[2] ~= ker(Picard_Gram mod 2), z mod 2 maps to z/2 mod Pic",
        "row_action_convention": "z -> z*A for Picard action matrix A with A*G*A^T=G",
        "historical_picard_rank": PICRANK,
        "kernel_dimension_f2": len(kernel_basis),
        "integral_smith_decomposition_used": False,
        "remote_cas_used": False,
        "actual_swaps_consumed_directly_from_stage33_09_historical_picard_basis": True,
        "old_ambiguous_intrinsic_to_retained_discriminant_transport_used": False,
        "K_joint_V4_fixed_dimension_f2": joint_fixed_dim,
        "finite_Z1_dimension_f2": len(z1),
        "finite_B1_dimension_f2": len(b1),
        "finite_H1_dimension_f2": len(h1),
        "seven_sign_Hom_A_to_finite_H1_dimension_regression": seven_hom_dim,
        "seven_sign_regression_expected": EXPECTED_SEVEN_SIGN_H1_HOM_DIM,
    },
    "q_defined_naturality_group": {
        "generator_names": generator_names,
        "generator_count_including_redundant_seventh_sign": len(generator_names),
        "coordinate_swap_s3_exact_on_source_K_and_finite_H1": True,
        "all_target_generators_commute_with_V4": True,
    },
    "exact_hom_spaces": {
        "A_dimension_f2": QDIM,
        "K_dimension_f2": KDIM,
        "finite_H1_V4_K_dimension_f2": H1DIM,
        "Hom_H_A_to_K_ambient_dimension_f2": QDIM * KDIM,
        "Hom_H_A_to_K_constraint_rank_f2": hom_A_K_rank,
        "Hom_H_A_to_K_dimension_f2": hom_A_K_dim,
        "Hom_H_A_to_finite_H1_ambient_dimension_f2": QDIM * H1DIM,
        "Hom_H_A_to_finite_H1_constraint_rank_f2": hom_A_H1_rank,
        "Hom_H_A_to_finite_H1_dimension_f2": hom_A_H1_dim,
    },
    "absolute_cohomology_argument": {
        "finite_v4_shortcut_used": False,
        "group_extension": "1 -> G_L -> G_Q -> V4 -> 1, L=Q(i,sqrt(2))",
        "inflation_restriction_segment": "0 -> H1(V4,K) -> H1(G_Q,K) -> H1(G_L,K)^V4",
        "kernel_action": "G_L acts trivially on K",
        "kernel_h1": "H1(G_L,K)=Hom_cont(G_L,F2) tensor_F2 K",
        "geometric_H_action_on_character_factor": "trivial",
        "step_1_valid_if": "Hom_H(A,K)=0",
        "step_2_valid_if": "Hom_H(A,H1(V4,K))=0",
    },
    "exact_consequence": {
        "absolute_arithmetic_localization_connecting_map_forced_zero_by_global_naturality": absolute_zero,
        "all_26_source_directions_treated_uniformly": True,
        "connecting_source_directions_exact": "26/26" if absolute_zero else "0/26",
        "arithmetic_localization_connecting_map_computed": absolute_zero,
        "connecting_map_value_if_closed": "ZERO_MAP" if absolute_zero else None,
        "arithmetic_hs_closed": False,
        "stage33_07_closed": False,
        "stage33_08_released": False,
        "stage33_progress": "6/11",
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
    "route_status": "PASS_EXACT_GLOBAL_ABSOLUTE_ZERO" if absolute_zero else "OPEN_RESIDUAL_H_EQUIVARIANT_BLOCK",
    "next_exact_leaf": (
        "write Stage33-11 26/26 zero-map closure and request hostile audit; do not release Stage33-12 before audit"
        if absolute_zero else
        "decompose the surviving H-equivariant Hom block and materialize only that symmetry block before any per-column fallback"
    ),
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "kernel_dimension_f2": len(kernel_basis),
    "joint_fixed_dimension_f2": joint_fixed_dim,
    "finite_H1_dimension_f2": len(h1),
    "seven_sign_Hom_A_to_finite_H1_dimension_f2": seven_hom_dim,
    "Hom_H_A_to_K_dimension_f2": hom_A_K_dim,
    "Hom_H_A_to_finite_H1_dimension_f2": hom_A_H1_dim,
    "absolute_connecting_map_forced_zero": absolute_zero,
    "connecting_source_directions_exact": cert["exact_consequence"]["connecting_source_directions_exact"],
    "route_status": cert["route_status"],
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
