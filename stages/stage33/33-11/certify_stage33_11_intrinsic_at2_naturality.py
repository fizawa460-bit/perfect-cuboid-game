#!/usr/bin/env python3
"""Stage33-11 exact naturality on the canonical intrinsic discriminant A[2].

This is the local-only replacement for the historical retained-Smith replay.
For the Picard lattice (L,G), A_L[2] is canonically ker(G mod 2), represented
by y/2 mod L.  Stage33-07 already reconstructs cc, ct, the two actual
coordinate swaps and all seven coordinate signs on this 14-dimensional model
from source-locked Picard geometry.  No Smith form or remote CAS is needed.
"""
from __future__ import annotations

import hashlib
import json
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
LEGACY = STAGE33 / "33-07"
PREV09 = STAGE33 / "33-09" / "handoff.json"
BRIDGE09 = STAGE33 / "33-09" / "marked-picard-basis-bridge-certified.json"
PREV10 = STAGE33 / "33-10" / "handoff.json"
BR2_PATH = LEGACY / "proper-brauer2-from-discriminant.json"
SIGN_SCRIPT = LEGACY / "certify_retained_geometric_sign_intertwiner_space.py"
SWAP_PICARD_SCRIPT = LEGACY / "certify_two_coordinate_swap_picard_rows.py"
INTRINSIC_SCRIPT = LEGACY / "certify_actual_galois_at2_actions.py"
OUT = HERE / "stage33-11-intrinsic-at2-naturality.json"

EXPECTED_09 = "9d385fd8ccddbf2d6f5289d944c4e80523ba39310d165c0741d9b5c33698e573"
EXPECTED_09_CLOSURE = "6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7"
EXPECTED_09_BRIDGE = "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92"
EXPECTED_10 = "4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f"
EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_SEVEN_SIGN_H1_HOM_DIM = 146
QDIM, KDIM, H1DIM = 26, 14, 16
ORDER = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path, expected, label):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"{label} source lock moved: claimed={claimed} actual={actual} expected={expected}")
    return obj


def hom_dimension(source_actions, target_actions, sdim, tdim, rank_bitmasks):
    if len(source_actions) != len(target_actions):
        raise SystemExit("source/target generator count mismatch")
    equations = []
    for S, T in zip(source_actions, target_actions):
        if len(S) != sdim or any(len(r) != sdim for r in S):
            raise SystemExit("source action shape regression")
        if len(T) != tdim or any(len(r) != tdim for r in T):
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
    raise SystemExit("finite diagnostic H1 dimension moved")

# Reconstruct the canonical intrinsic A[2] actions entirely locally.
intrinsic = runpy.run_path(str(INTRINSIC_SCRIPT))
intrinsic_cert = intrinsic["out"]
expected_intrinsic = bridge09.get("source_locks", {}).get("actual_galois_at2_certificate_sha256")
if expected_intrinsic and intrinsic_cert.get("canonical_sha256") != expected_intrinsic:
    raise SystemExit(
        "Stage33-09 actual Galois A2 source lock moved: "
        f"got={intrinsic_cert.get('canonical_sha256')} expected={expected_intrinsic}"
    )
B_cc = intrinsic["A_cc"]
B_ct = intrinsic["A_ct"]
B_signs = intrinsic["signs7"]
B_swaps = [intrinsic["A12"], intrinsic["A13"]]

sign = runpy.run_path(str(SIGN_SCRIPT))
rank2 = sign["rank2"]; row_basis = sign["row_basis"]; nullspace2 = sign["nullspace2"]
build_solver = sign["build_solver"]; rank_bitmasks = sign["rank_bitmasks"]
matmul2 = sign["matmul2"]; rowmul2 = sign["rowmul2"]; rowmul_z = sign["rowmul_z"]
permute_vector = sign["permute_vector"]; sub2 = sign["sub2"]; eye = sign["eye"]
source_sign_actions = sign["source_sign_actions"]
if len(source_sign_actions) != 7:
    raise SystemExit("source seven-sign coverage moved")

I14 = eye(KDIM)
if matmul2(B_cc, B_cc) != I14 or matmul2(B_ct, B_ct) != I14 or matmul2(B_cc, B_ct) != matmul2(B_ct, B_cc):
    raise SystemExit("intrinsic K V4 relations failed")
for name, B in [(f"sign_{n}", M) for n, M in zip(ORDER, B_signs)] + [("swap12", B_swaps[0]), ("swap13", B_swaps[1])]:
    if matmul2(B, B) != I14 or matmul2(B, B_cc) != matmul2(B_cc, B) or matmul2(B, B_ct) != matmul2(B_ct, B):
        raise SystemExit(f"{name}: intrinsic K action regression")
if matmul2(matmul2(B_swaps[0], B_swaps[1]), B_swaps[0]) != matmul2(matmul2(B_swaps[1], B_swaps[0]), B_swaps[1]):
    raise SystemExit("intrinsic K swap S3 relation failed")

Ng = sub2(B_cc, I14); Nh = sub2(B_ct, I14)
fixed_eq = [[Ng[i][j] for i in range(KDIM)] for j in range(KDIM)] + [[Nh[i][j] for i in range(KDIM)] for j in range(KDIM)]
joint_fixed_dim = KDIM - rank2(fixed_eq, KDIM)
if joint_fixed_dim != int(br2["proper_Br2_joint_V4_fixed_dimension_f2"]):
    raise SystemExit(f"intrinsic K joint-fixed mismatch: {joint_fixed_dim}")
eq = []
for j in range(KDIM): eq.append([Ng[i][j] for i in range(KDIM)] + [0] * KDIM)
for j in range(KDIM): eq.append([0] * KDIM + [Nh[i][j] for i in range(KDIM)])
for j in range(KDIM): eq.append([Nh[i][j] for i in range(KDIM)] + [Ng[i][j] for i in range(KDIM)])
z1 = nullspace2(eq, 2 * KDIM)
b1, _ = row_basis([Ng[i] + Nh[i] for i in range(KDIM)], 2 * KDIM)
if (len(z1), len(b1)) != (20, 4):
    raise SystemExit(f"intrinsic finite V4 receiver mismatch: Z1={len(z1)} B1={len(b1)}")
frame = list(b1); h1 = []
for z in z1:
    if rank2(frame + [z], 2 * KDIM) > len(frame):
        frame.append(z); h1.append(z)
if len(h1) != H1DIM:
    raise SystemExit("intrinsic finite H1 quotient complement regression")
solve_h1 = build_solver(frame)


def induce_h1(name, proper):
    action = []
    for z in h1:
        transformed = rowmul2(z[:KDIM], proper) + rowmul2(z[KDIM:], proper)
        coeff = solve_h1(transformed)
        action.append(coeff[len(b1):])
    if rank2(action, H1DIM) != H1DIM or matmul2(action, action) != eye(H1DIM):
        raise SystemExit(f"{name}: induced finite-H1 action regression")
    return action


H1_signs = [induce_h1(f"sign_{n}", B) for n, B in zip(ORDER, B_signs)]
H1_swaps = [induce_h1("swap12", B_swaps[0]), induce_h1("swap13", B_swaps[1])]
seven_hom_dim, seven_hom_rank = hom_dimension(source_sign_actions, H1_signs, QDIM, H1DIM, rank_bitmasks)
if seven_hom_dim != EXPECTED_SEVEN_SIGN_H1_HOM_DIM:
    raise SystemExit(f"intrinsic seven-sign Hom regression: got {seven_hom_dim}, expected {EXPECTED_SEVEN_SIGN_H1_HOM_DIM}")

# Reconstruct the source A[2] actual swaps exactly from the 72 boundary action.
pic = runpy.run_path(str(SWAP_PICARD_SCRIPT))
boundaries = pic["boundaries"]
if [r["action"] for r in boundaries] != ["swap12", "swap13"]:
    raise SystemExit("source coordinate-swap boundary ordering regression")
edges = sign["edges"]; edge_index = sign["edge_index"]; U44 = sign["U44"]; R17 = sign["R17"]; O4 = sign["O4"]
solve61 = sign["solve61"]; Tsource = sign["T"]; diag29 = sign["diag29"]; relation29 = sign["relation29"]
source_basis = sign["source_basis"]; support_to_source = sign["support_to_source"]


def source_action_from_boundary(name, side1, point1):
    sidep = [int(x) - 1 for x in side1]; pointp = [int(x) - 1 for x in point1]
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
        image = permute_vector(row, edge_perm, 4); matches = []
        for k, target in enumerate(O4):
            if image == target: matches.append((k, 1))
            if image == [(-int(x)) % 4 for x in target]: matches.append((k, -1))
        if len(matches) != 1:
            raise SystemExit(f"{name}: O4_{j+1} not a unique signed generator: {matches}")
        o_action.append(matches[0])
    A29 = [r_action[i] + [0] * 12 for i in range(17)]
    for target, sgn in o_action:
        row = [0] * 29; row[17 + target] = sgn; A29.append(row)
    for rel in relation29:
        smith_rel = rowmul_z(rowmul_z(rel, A29), Tsource)
        if any(smith_rel[j] % diag29[j] for j in range(29)):
            raise SystemExit(f"{name}: source relation lattice not preserved")
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


source_swaps = [
    source_action_from_boundary(rec["action"], rec["side_permutation_1based"], rec["exceptional_permutation_1based"])
    for rec in boundaries
]
if matmul2(matmul2(source_swaps[0], source_swaps[1]), source_swaps[0]) != matmul2(matmul2(source_swaps[1], source_swaps[0]), source_swaps[1]):
    raise SystemExit("source A2 actual swaps lost S3 braid")

source_actions = source_sign_actions + source_swaps
K_actions = B_signs + B_swaps
H1_actions = H1_signs + H1_swaps
hom_A_K_dim, hom_A_K_rank = hom_dimension(source_actions, K_actions, QDIM, KDIM, rank_bitmasks)
hom_A_H1_dim, hom_A_H1_rank = hom_dimension(source_actions, H1_actions, QDIM, H1DIM, rank_bitmasks)
absolute_zero = hom_A_K_dim == 0 and hom_A_H1_dim == 0

cert = {
    "schema": "STAGE33_11_INTRINSIC_AT2_GLOBAL_NATURALITY_V1",
    "stage": "33-11",
    "branch": "33-11_INTRINSIC_AT2_LOCAL_ONLY",
    "source_locks": {
        "stage33_09_handoff_sha256": EXPECTED_09,
        "stage33_09_closure_sha256": EXPECTED_09_CLOSURE,
        "stage33_09_marked_picard_bridge_sha256": EXPECTED_09_BRIDGE,
        "stage33_10_handoff_sha256": EXPECTED_10,
        "proper_brauer2_sha256": EXPECTED_BR2,
        "actual_galois_at2_certificate_sha256": intrinsic_cert["canonical_sha256"],
    },
    "transport": {
        "model": "canonical ker(Picard_Gram mod 2) = discriminant A_L[2]",
        "remote_cas_used": False,
        "smith_form_used": False,
        "target_dimension": KDIM,
        "actual_swaps_integral_picard_source_locked": True,
        "named_cc_ct_and_seven_signs_source_locked": True,
        "finite_K_joint_V4_fixed_dimension_f2": joint_fixed_dim,
        "finite_Z1_dimension_f2": len(z1),
        "finite_B1_dimension_f2": len(b1),
        "finite_H1_dimension_f2": len(h1),
        "seven_sign_Hom_A_to_finite_H1_dimension_regression": seven_hom_dim,
    },
    "exact_hom_spaces": {
        "A_dimension_f2": QDIM,
        "K_dimension_f2": KDIM,
        "finite_H1_V4_K_dimension_f2": H1DIM,
        "Hom_H_A_to_K_constraint_rank_f2": hom_A_K_rank,
        "Hom_H_A_to_K_dimension_f2": hom_A_K_dim,
        "Hom_H_A_to_finite_H1_constraint_rank_f2": hom_A_H1_rank,
        "Hom_H_A_to_finite_H1_dimension_f2": hom_A_H1_dim,
    },
    "absolute_cohomology_argument": {
        "finite_v4_shortcut_used": False,
        "inflation_restriction_segment": "0 -> H1(V4,K) -> H1(G_Q,K) -> H1(G_L,K)^V4",
        "Hom_H_A_to_K_zero_kills_restriction_factor": hom_A_K_dim == 0,
        "Hom_H_A_to_finite_H1_zero_kills_inflated_factor": hom_A_H1_dim == 0,
        "absolute_connecting_map_forced_zero": absolute_zero,
    },
    "exit_condition": {
        "stage33_11_closed_exact": absolute_zero,
        "arithmetic_localization_connecting_map_zero": absolute_zero,
        "stage33_07_arithmetic_HS_closed": False,
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"HOM_A_K_DIM={hom_A_K_dim}")
print(f"HOM_A_FINITE_H1_DIM={hom_A_H1_dim}")
print(f"ABSOLUTE_CONNECTING_MAP_ZERO={str(absolute_zero).lower()}")
print(f"CERTIFICATE_SHA256={cert['canonical_sha256']}")
if not absolute_zero:
    raise SystemExit("Stage33-11 intrinsic-A2 naturality does not close both absolute factors")
print("STAGE33_11_INTRINSIC_AT2_NATURALITY=PASS_EXACT")
