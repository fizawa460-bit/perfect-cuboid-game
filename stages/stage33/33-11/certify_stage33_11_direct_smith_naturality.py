#!/usr/bin/env python3
"""Stage33-11 direct Smith-quotient naturality scout.

This replaces the historical ambiguous intrinsic->retained discriminant
transport by using the Stage33-09 certified *actual* 64x64 coordinate swaps in
the historical q256 Picard basis itself.  A fresh exact Smith decomposition of
the historical Picard Gram is allowed to choose a new discriminant basis: all
cc/ct, seven coordinate signs, and both actual swaps are induced into that same
basis simultaneously.  Basis-independent regression invariants then certify
that the resulting K=Br(Sbar)[2] V4 module is the Stage33-10 receiver module.

The absolute-H1 argument is deliberately two-step and never identifies
H^1(G_Q,K) with H^1(V4,K):

  * if Hom_H(A,K)=0, restriction of delta to H^1(G_L,K)^V4 vanishes because
    H acts trivially on the character factor Hom_cont(G_L,F2);
  * if also Hom_H(A,H^1(V4,K))=0, the remaining inflated factor vanishes.

Here A is the 26-dimensional order-two localization source and H is generated
by the seven Q-defined coordinate signs and two Q-defined coordinate swaps.
"""
from __future__ import annotations

import hashlib
import json
import runpy
import sys
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

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
OUT = HERE / "stage33-11-direct-smith-naturality.json"

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


def zmat(raw, label: str) -> sp.Matrix:
    if not isinstance(raw, list) or len(raw) != PICRANK or any(not isinstance(r, list) or len(r) != PICRANK for r in raw):
        raise SystemExit(f"{label}: expected 64x64 matrix")
    if any(type(x) is not int for r in raw for x in r):
        raise SystemExit(f"{label}: nonintegral entry")
    return sp.Matrix(raw)


def to_int_lists(M: sp.Matrix, label: str) -> list[list[int]]:
    out = []
    for i in range(M.rows):
        row = []
        for j in range(M.cols):
            x = sp.Rational(M[i, j])
            if x.q != 1:
                raise SystemExit(f"{label}: nonintegral entry at {i},{j}: {x}")
            row.append(int(x))
        out.append(row)
    return out


def mixed_well_defined(M: list[list[int]], mods: list[int]) -> bool:
    return all((mods[i] * int(M[i][j])) % mods[j] == 0 for i in range(len(mods)) for j in range(len(mods)))


def mixed_mul(A: list[list[int]], B: list[list[int]], mods: list[int]) -> list[list[int]]:
    n = len(mods)
    return [[sum(int(A[i][k]) * int(B[k][j]) for k in range(n)) % mods[j] for j in range(n)] for i in range(n)]


def mixed_eye(mods: list[int]) -> list[list[int]]:
    return [[int(i == j) % mods[j] for j in range(len(mods))] for i in range(len(mods))]


def restrict_two(M: list[list[int]], mods: list[int]) -> list[list[int]]:
    scales = [m // 2 for m in mods]
    out = []
    for i in range(len(mods)):
        row = []
        for j in range(len(mods)):
            num = scales[i] * int(M[i][j])
            if num % scales[j]:
                raise SystemExit("A_T[2] restriction integrality failed")
            row.append((num // scales[j]) & 1)
        out.append(row)
    return out


def hom_dimension(source_actions, target_actions, sdim: int, tdim: int, rank_bitmasks) -> tuple[int, int]:
    if len(source_actions) != len(target_actions):
        raise SystemExit("source/target generator count mismatch")
    equations = []
    for S, T in zip(source_actions, target_actions):
        if len(S) != sdim or any(len(row) != sdim for row in S):
            raise SystemExit("source action shape regression")
        if len(T) != tdim or any(len(row) != tdim for row in T):
            raise SystemExit("target action shape regression")
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

# Rebuild the exact source-side sign actions and all source quotient helpers.
# The retained target actions produced by this legacy script are used only as a
# basis-independent seven-sign Hom-dimension regression, not as swap transport.
sign = runpy.run_path(str(SIGN_SCRIPT))
rank2 = sign["rank2"]
row_basis = sign["row_basis"]
nullspace2 = sign["nullspace2"]
build_solver = sign["build_solver"]
rank_bitmasks = sign["rank_bitmasks"]
matmul2 = sign["matmul2"]
rowmul2 = sign["rowmul2"]
rowmul_z = sign["rowmul_z"]
permute_vector = sign["permute_vector"]
sub2 = sign["sub2"]
transpose = sign["transpose"]
eye = sign["eye"]
source_sign_actions = sign["source_sign_actions"]
if len(source_sign_actions) != 7:
    raise SystemExit("source seven-sign coverage moved")

# Historical q256 Picard lattice and all Q-defined automorphisms in the same
# certified basis. Stage33-09 provides the formerly missing actual swaps here.
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

G = zmat(old["picard_gram_64x64"], "historical Picard Gram")
A_cc_z = zmat(old["picard_action_cc_64x64"], "historical cc")
A_ct_z = zmat(old["picard_action_ct_64x64"], "historical ct")
A_signs_z = [zmat(old_sign["picard_actions_64x64"][name], f"historical sign {name}") for name in order]
swaps09 = bridge09["actual_coordinate_swaps_in_historical_magma_picard_basis"]
A_swap12_z = zmat(swaps09["swap12_action_64x64"], "Stage33-09 actual swap12")
A_swap13_z = zmat(swaps09["swap13_action_64x64"], "Stage33-09 actual swap13")
I64 = sp.eye(PICRANK)
for name, A in [("cc", A_cc_z), ("ct", A_ct_z)] + [(f"sign_{n}", A) for n, A in zip(order, A_signs_z)] + [("swap12", A_swap12_z), ("swap13", A_swap13_z)]:
    if A * A != I64:
        raise SystemExit(f"{name}: historical action lost involutivity")
    if A * G * A.T != G:
        raise SystemExit(f"{name}: historical action lost Picard Gram isometry")
for name, A in [("swap12", A_swap12_z), ("swap13", A_swap13_z)]:
    if A * A_cc_z != A_cc_z * A or A * A_ct_z != A_ct_z * A:
        raise SystemExit(f"{name}: Q-defined swap no longer commutes with cc/ct")
if A_swap12_z * A_swap13_z * A_swap12_z != A_swap13_z * A_swap12_z * A_swap13_z:
    raise SystemExit("historical actual swaps lost S3 braid")

# Fresh exact Smith coordinates. They need not equal the old compact Smith
# coordinates: every action below is transported simultaneously into this one
# basis, and the receiver invariants are checked independently.
D, S, T = smith_normal_decomp(G, domain=ZZ)
if D != S * G * T:
    raise SystemExit("historical Picard Smith decomposition failed")
diag = [abs(int(D[i, i])) for i in range(PICRANK)]
if any(D[i, j] != 0 for i in range(PICRANK) for j in range(PICRANK) if i != j):
    raise SystemExit("Picard Smith output not diagonal")
pos = [i for i, d in enumerate(diag) if d > 1]
mods = [diag[i] for i in pos]
if sorted(mods) != [2] * 4 + [4] * 6 + [8] * 4 or len(pos) != KDIM:
    raise SystemExit(f"Picard discriminant invariant factors moved: {mods}")
Tin = T.inv()
if any(sp.Rational(Tin[i, j]).q != 1 for i in range(PICRANK) for j in range(PICRANK)):
    raise SystemExit("Smith right transform is not unimodular")


def induce_mixed(name: str, A: sp.Matrix) -> list[list[int]]:
    # Same contragredient convention as the retained Magma extractor:
    # V^-1 * Transpose(A^-1) * V. All named actions are involutions.
    C = Tin * A.T * T
    Ci = to_int_lists(C, name + " discriminant transport")
    M = [[Ci[i][j] % mods[b] for b, j in enumerate(pos)] for i in pos]
    if not mixed_well_defined(M, mods):
        raise SystemExit(f"{name}: action not well-defined on Smith discriminant quotient")
    return M


M_cc = induce_mixed("cc", A_cc_z)
M_ct = induce_mixed("ct", A_ct_z)
M_signs = [induce_mixed(f"sign_{n}", A) for n, A in zip(order, A_signs_z)]
M_swaps = [induce_mixed("swap12", A_swap12_z), induce_mixed("swap13", A_swap13_z)]
Imix = mixed_eye(mods)
if mixed_mul(M_cc, M_cc, mods) != Imix or mixed_mul(M_ct, M_ct, mods) != Imix or mixed_mul(M_cc, M_ct, mods) != mixed_mul(M_ct, M_cc, mods):
    raise SystemExit("fresh Smith cc/ct relations failed")
for name, M in [(f"sign_{n}", M) for n, M in zip(order, M_signs)] + [("swap12", M_swaps[0]), ("swap13", M_swaps[1])]:
    if mixed_mul(M, M, mods) != Imix:
        raise SystemExit(f"{name}: fresh Smith involution failed")
    if mixed_mul(M, M_cc, mods) != mixed_mul(M_cc, M, mods) or mixed_mul(M, M_ct, mods) != mixed_mul(M_ct, M, mods):
        raise SystemExit(f"{name}: fresh Smith action fails Q-defined cc/ct commutation")
if mixed_mul(mixed_mul(M_swaps[0], M_swaps[1], mods), M_swaps[0], mods) != mixed_mul(mixed_mul(M_swaps[1], M_swaps[0], mods), M_swaps[1], mods):
    raise SystemExit("fresh Smith actual swaps lost S3 braid")

# K=proper geometric Br[2] row-action convention matches the historical exact
# code: restrict the Picard discriminant action to 2-torsion, then transpose.
B_cc = transpose(restrict_two(M_cc, mods))
B_ct = transpose(restrict_two(M_ct, mods))
B_signs = [transpose(restrict_two(M, mods)) for M in M_signs]
B_swaps = [transpose(restrict_two(M, mods)) for M in M_swaps]
I14 = eye(KDIM)
if matmul2(B_cc, B_cc) != I14 or matmul2(B_ct, B_ct) != I14 or matmul2(B_cc, B_ct) != matmul2(B_ct, B_cc):
    raise SystemExit("fresh K V4 relations failed")
for name, B in [(f"sign_{n}", B) for n, B in zip(order, B_signs)] + [("swap12", B_swaps[0]), ("swap13", B_swaps[1])]:
    if matmul2(B, B) != I14 or matmul2(B, B_cc) != matmul2(B_cc, B) or matmul2(B, B_ct) != matmul2(B_ct, B):
        raise SystemExit(f"{name}: fresh K action regression")
if matmul2(matmul2(B_swaps[0], B_swaps[1]), B_swaps[0]) != matmul2(matmul2(B_swaps[1], B_swaps[0]), B_swaps[1]):
    raise SystemExit("fresh K swap S3 relation failed")

# Basis-independent V4 receiver regressions against Stage33-10.
Ng = sub2(B_cc, I14)
Nh = sub2(B_ct, I14)
fixed_eq = []
for j in range(KDIM):
    fixed_eq.append([Ng[i][j] for i in range(KDIM)])
for j in range(KDIM):
    fixed_eq.append([Nh[i][j] for i in range(KDIM)])
joint_fixed_dim = KDIM - rank2(fixed_eq, KDIM)
if joint_fixed_dim != int(br2["proper_Br2_joint_V4_fixed_dimension_f2"]):
    raise SystemExit(f"fresh K joint fixed dimension mismatch: {joint_fixed_dim}")
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
    raise SystemExit(f"fresh finite V4 receiver mismatch: Z1={len(z1)} B1={len(b1)}")
frame = list(b1)
h1 = []
for z in z1:
    if rank2(frame + [z], 2 * KDIM) > len(frame):
        frame.append(z)
        h1.append(z)
if len(h1) != H1DIM or rank2(frame, 2 * KDIM) != 20:
    raise SystemExit("fresh finite H1 quotient complement regression")
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

# Strong coordinate-convention regression: before the newly usable actual
# swaps, the independently rebuilt seven-sign receiver must reproduce the
# historical exact 146-dimensional naturality ambiguity.
seven_hom_dim, seven_hom_rank = hom_dimension(source_sign_actions, H1_signs, QDIM, H1DIM, rank_bitmasks)
if seven_hom_dim != EXPECTED_SEVEN_SIGN_H1_HOM_DIM:
    raise SystemExit(f"fresh Smith seven-sign Hom regression: got {seven_hom_dim}, expected 146")

# Reconstruct source-side swap actions from exact boundary permutations.
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
        original = [int(x) for x in rec["original_R17_O12_coordinates_Z29"]]
        smith = rowmul_z(rowmul_z(original, A29), Tsource)
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
    "schema": "STAGE33_11_DIRECT_SMITH_GLOBAL_NATURALITY_V1",
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
    "direct_smith_transport": {
        "historical_picard_rank": PICRANK,
        "picard_determinant": int(G.det()),
        "fresh_smith_discriminant_moduli": mods,
        "actual_swaps_consumed_directly_from_stage33_09_historical_picard_basis": True,
        "old_ambiguous_intrinsic_to_retained_discriminant_transport_used": False,
        "all_11_named_actions_induced_in_one_fresh_smith_basis": True,
        "fresh_K_joint_V4_fixed_dimension_f2": joint_fixed_dim,
        "fresh_finite_Z1_dimension_f2": len(z1),
        "fresh_finite_B1_dimension_f2": len(b1),
        "fresh_finite_H1_dimension_f2": len(h1),
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
    "seven_sign_Hom_A_to_finite_H1_dimension_f2": seven_hom_dim,
    "Hom_H_A_to_K_dimension_f2": hom_A_K_dim,
    "Hom_H_A_to_finite_H1_dimension_f2": hom_A_H1_dim,
    "absolute_connecting_map_forced_zero": absolute_zero,
    "connecting_source_directions_exact": cert["exact_consequence"]["connecting_source_directions_exact"],
    "route_status": cert["route_status"],
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
