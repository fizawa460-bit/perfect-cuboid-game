#!/usr/bin/env python3
"""Stage33-11 global/all-at-once arithmetic-localization naturality test.

Goal
====
The Stage33-10 handoff deliberately replaced the false shortcut

    H^1(G_Q,K) = H^1(V4,K)

by the exact absolute receiver for K=Br(Sbar)[2], split by
L=Q(i,sqrt(2)).  Stage33-11 must therefore not prove only that the finite-V4
connecting matrix vanishes and silently promote that to an absolute statement.

Instead let Gamma=G_Q, N=G_L, Q=Gamma/N=V4, let A be the 26-dimensional
order-two localization source, and let H be the Q-defined geometric
automorphism group generated here by the seven coordinate signs and the two
actual coordinate swaps.  H commutes with Gamma and acts only on coefficient
modules/cohomology, not on Gamma itself.

For the genuine arithmetic connecting map

    delta : A -> H^1(Gamma,K),

naturality makes delta H-equivariant. Inflation-restriction gives

  0 -> H^1(Q,K) -> H^1(Gamma,K) -> H^1(N,K)^Q.

Because N acts trivially on K,

    H^1(N,K) = Hom_cont(N,F2) tensor K,

and H is trivial on the character factor. Therefore:

  (I)  Hom_H(A,K)=0
       => every H-map A -> H^1(N,K)^Q is zero
       => delta factors through inflation H^1(Q,K).

  (II) Hom_H(A,H^1(Q,K))=0
       => that factor is zero
       => delta=0 in the exact absolute Stage33-10 receiver.

This verifier computes both Hom spaces exactly over F2 from source-locked
geometric actions.  It does NOT materialize an arbitrary endpoint-compatible
middle Gersten extension and it does NOT identify finite H1 with absolute H1.
If either Hom space is nonzero, the all-at-once zero route remains open and
Stage33-11 must continue with the residual symmetry block or genuine middle
Gersten data.
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
SWAP_TRANSPORT_SCRIPT = LEGACY / "certify_intrinsic_to_retained_at2_swap_transport_named_v4.py"
OUT = HERE / "stage33-11-global-naturality-scout.json"

EXPECTED_09 = "9d385fd8ccddbf2d6f5289d944c4e80523ba39310d165c0741d9b5c33698e573"
EXPECTED_09_CLOSURE = "6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7"
EXPECTED_09_BRIDGE = "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92"
EXPECTED_10 = "4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f"
EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
QDIM = 26
KDIM = 14
H1DIM = 16


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str, label: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"{label} source lock moved: claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def hom_dimension(source_actions, target_actions, sdim: int, tdim: int, rank_bitmasks) -> tuple[int, int]:
    """Dimension of D with S_g D = D T_g for all supplied generators."""
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


# Local legacy helpers import retained sibling modules by bare module name.
sys.path.insert(0, str(LEGACY))

prev09 = load_locked(PREV09, EXPECTED_09, "Stage33-09 handoff")
bridge09 = load_locked(BRIDGE09, EXPECTED_09_BRIDGE, "Stage33-09 marked Picard bridge")
prev10 = load_locked(PREV10, EXPECTED_10, "Stage33-10 handoff")
br2 = load_locked(BR2_PATH, EXPECTED_BR2, "proper geometric Br2")

if prev09.get("status") != "CLOSED_EXACT":
    raise SystemExit("Stage33-09 is not exact-closed")
if prev09.get("source_locks", {}).get("stage33_09_closure_sha256") != EXPECTED_09_CLOSURE:
    raise SystemExit("Stage33-09 closure lock moved")
if not bridge09.get("exact_consequence", {}).get(
    "actual_integral_swaps_now_available_in_historical_q256_picard_basis"
):
    raise SystemExit("Stage33-09 no longer certifies actual historical-q256 swaps")
if prev10.get("status") != "CLOSED_EXACT":
    raise SystemExit("Stage33-10 is not exact-closed")
if prev10.get("next_item") != "Stage33-11_ARITHMETIC_LOCALIZATION_CONNECTING_MAP":
    raise SystemExit("Stage33-10 no longer releases Stage33-11")
if not prev10.get("exit_condition", {}).get("absolute_h1_receiver_exact"):
    raise SystemExit("Stage33-10 absolute receiver is not exact")
if prev10.get("exact_receiver", {}).get("finite_v4_shortcut_status") != "EXPLICITLY_REPLACED":
    raise SystemExit("finite-V4 shortcut firewall moved")

# Rebuild the retained source actions, proper K actions, and finite H1 quotient
# from the exact Stage33-07 local machinery.  This also independently checks
# every source-side sign boundary permutation against exact Q(i) node data.
sign = runpy.run_path(str(SIGN_SCRIPT))
rank2 = sign["rank2"]
rank_bitmasks = sign["rank_bitmasks"]
matmul2 = sign["matmul2"]
eye = sign["eye"]
transpose = sign["transpose"]
rowmul2 = sign["rowmul2"]
rowmul_z = sign["rowmul_z"]
permute_vector = sign["permute_vector"]

B_cc = sign["B_cc"]
B_ct = sign["B_ct"]
if B_cc != [[int(x) & 1 for x in row] for row in br2["proper_Br2_cc_action_f2"]]:
    raise SystemExit("retained sign endpoint cc action differs from Stage33-10 K")
if B_ct != [[int(x) & 1 for x in row] for row in br2["proper_Br2_ct_action_f2"]]:
    raise SystemExit("retained sign endpoint ct action differs from Stage33-10 K")
if br2["finite_v4_H1_proper_Br2"]["H1_dimension_f2"] != H1DIM:
    raise SystemExit("Stage33-10 finite H1 dimension regression")

source_sign_actions = sign["source_sign_actions"]
proper_sign_actions = sign["B_signs"]
h1_sign_actions = sign["h1_sign_actions"]
if (len(source_sign_actions), len(proper_sign_actions), len(h1_sign_actions)) != (7, 7, 7):
    raise SystemExit("seven-sign action coverage regression")

# Stage33-09 supplies the missing semantic marking: the historical q256 Picard
# basis is now certified to be the same marked geometric Picard lattice as the
# retained 140-class model.  The named-V4 transport solver then asks whether
# the actual swap pair on K is independent of every remaining basis isometry
# compatible with the seven signs, cc/ct, and the discriminant quadratic form.
transport = runpy.run_path(str(SWAP_TRANSPORT_SCRIPT))
unique_swap_pair = bool(transport["unique_pair"])
X12 = transport["X120"]
X13 = transport["X130"]
if not unique_swap_pair:
    scout = {
        "schema": "STAGE33_11_GLOBAL_NATURALITY_SCOUT_V1",
        "route_status": "BLOCKED_RETAINED_K_SWAP_PAIR_NOT_UNIQUE",
        "source_locks": {
            "stage33_09_handoff_sha256": EXPECTED_09,
            "stage33_09_marked_picard_bridge_sha256": EXPECTED_09_BRIDGE,
            "stage33_10_handoff_sha256": EXPECTED_10,
            "proper_brauer2_sha256": EXPECTED_BR2,
        },
        "connecting_source_directions_exact": "0/26",
        "arithmetic_localization_connecting_map_computed": False,
        "finite_v4_shortcut_used": False,
        "next_exact_leaf": "derive the actual historical-q256 discriminant swap action directly from the certified Stage33-09 marked Picard bridge/Smith quotient before imposing global naturality",
        "theorem_credit": False,
        "endpoint_credit": False,
    }
    scout["canonical_sha256"] = csha(scout)
    OUT.write_text(json.dumps(scout, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(scout, indent=2, sort_keys=True))
    raise SystemExit("actual retained-K swap pair is not unique; fail closed")

proper_swap_actions = [transpose(X12), transpose(X13)]
I14 = eye(KDIM)
for name, P in zip(("swap12", "swap13"), proper_swap_actions):
    if matmul2(P, P) != I14:
        raise SystemExit(f"{name}: proper K action lost involutivity")
    if matmul2(P, B_cc) != matmul2(B_cc, P) or matmul2(P, B_ct) != matmul2(B_ct, P):
        raise SystemExit(f"{name}: Q-defined swap does not commute with V4 on K")
if matmul2(matmul2(proper_swap_actions[0], proper_swap_actions[1]), proper_swap_actions[0]) != matmul2(
    matmul2(proper_swap_actions[1], proper_swap_actions[0]), proper_swap_actions[1]
):
    raise SystemExit("actual retained-K swaps lost the S3 braid relation")

# Reconstruct the two source-side boundary actions directly from the retained
# 140-class geometric swap permutations; do not infer them from K.
pic = runpy.run_path(str(SWAP_PICARD_SCRIPT))
boundaries = pic["boundaries"]
if [r["action"] for r in boundaries] != ["swap12", "swap13"]:
    raise SystemExit("coordinate-swap boundary ordering regression")

edges = sign["edges"]
edge_index = sign["edge_index"]
U44 = sign["U44"]
R17 = sign["R17"]
O4 = sign["O4"]
solve61 = sign["solve61"]
Tsmith = sign["T"]
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
        smith_rel = rowmul_z(rowmul_z(rel, A29), Tsmith)
        if any(smith_rel[j] % diag29[j] for j in range(29)):
            raise SystemExit(f"{name}: exact relation lattice not preserved")

    out_rows = []
    for rec in source_basis:
        original = [int(x) for x in rec["original_R17_O12_coordinates_Z29"]]
        smith = rowmul_z(rowmul_z(original, A29), Tsmith)
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
        raise SystemExit(f"{name}: source A2 action is not an involutive automorphism")
    return out_rows


source_swap_actions = [
    source_action_from_boundary(
        rec["action"], rec["side_permutation_1based"], rec["exceptional_permutation_1based"]
    )
    for rec in boundaries
]
if matmul2(matmul2(source_swap_actions[0], source_swap_actions[1]), source_swap_actions[0]) != matmul2(
    matmul2(source_swap_actions[1], source_swap_actions[0]), source_swap_actions[1]
):
    raise SystemExit("source swap actions lost S3 braid relation")

# Induce each actual coefficient automorphism on the exact finite H1 quotient.
h1 = sign["h1"]
solve_h1 = sign["solve_h1"]


def induce_h1(name: str, proper: list[list[int]]) -> list[list[int]]:
    action = []
    for z in h1:
        transformed = rowmul2(z[:KDIM], proper) + rowmul2(z[KDIM:], proper)
        coeff = solve_h1(transformed)
        action.append(coeff[4:])
    if rank2(action, H1DIM) != H1DIM or matmul2(action, action) != eye(H1DIM):
        raise SystemExit(f"{name}: induced finite-H1 action regression")
    return action


h1_swap_actions = [
    induce_h1(name, proper)
    for name, proper in zip(("swap12", "swap13"), proper_swap_actions)
]
if matmul2(matmul2(h1_swap_actions[0], h1_swap_actions[1]), h1_swap_actions[0]) != matmul2(
    matmul2(h1_swap_actions[1], h1_swap_actions[0]), h1_swap_actions[1]
):
    raise SystemExit("finite-H1 swap actions lost S3 braid relation")

# The seven signs have one projective product relation; retaining all seven as
# generator constraints is harmless.  Add the two actual coordinate swaps.
generator_names = list(sign["SIGN_NAMES"]) + ["swap12", "swap13"]
source_actions = source_sign_actions + source_swap_actions
proper_actions = proper_sign_actions + proper_swap_actions
h1_actions = h1_sign_actions + h1_swap_actions

hom_A_K_dim, hom_A_K_rank = hom_dimension(source_actions, proper_actions, QDIM, KDIM, rank_bitmasks)
hom_A_H1_dim, hom_A_H1_rank = hom_dimension(source_actions, h1_actions, QDIM, H1DIM, rank_bitmasks)

absolute_zero = hom_A_K_dim == 0 and hom_A_H1_dim == 0
scout = {
    "schema": "STAGE33_11_GLOBAL_NATURALITY_SCOUT_V1",
    "stage": "33-11",
    "name": "ARITHMETIC-LOCALIZATION-CONNECTING-MAP",
    "branch": "33-11a_GLOBAL_ALL_AT_ONCE_26_COLUMN_CLOSURE",
    "source_locks": {
        "stage33_09_handoff_sha256": EXPECTED_09,
        "stage33_09_closure_sha256": EXPECTED_09_CLOSURE,
        "stage33_09_marked_picard_bridge_sha256": EXPECTED_09_BRIDGE,
        "stage33_10_handoff_sha256": EXPECTED_10,
        "proper_brauer2_sha256": EXPECTED_BR2,
        "testa_stoll_upstream_git_blob_sha1": prev10["source_locks"]["testa_stoll_upstream_git_blob_sha1"],
    },
    "exact_geometry": {
        "q_defined_generator_names": generator_names,
        "generator_count_including_redundant_seventh_sign": len(generator_names),
        "actual_coordinate_swaps_semantically_marked_by_stage33_09": True,
        "actual_retained_K_swap_pair_unique_after_named_v4_sign_quadratic_transport": True,
        "source_and_coefficient_swap_s3_relations_exact": True,
        "all_generators_commute_with_galois_v4_on_K": True,
    },
    "absolute_cohomology_argument": {
        "group_extension": "1 -> G_L -> G_Q -> V4 -> 1, L=Q(i,sqrt(2))",
        "finite_v4_shortcut_used": False,
        "inflation_restriction_segment": "0 -> H1(V4,K) -> H1(G_Q,K) -> H1(G_L,K)^V4",
        "kernel_action": "G_L acts trivially on K",
        "kernel_h1": "H1(G_L,K)=X_L tensor_F2 K, X_L=Hom_cont(G_L,F2)",
        "q_defined_geometric_H_action_on_X_L": "trivial",
        "step_1": "Hom_H(A,K)=0 forces the restriction of delta to H1(G_L,K)^V4 to vanish, hence delta factors through inflation",
        "step_2": "Hom_H(A,H1(V4,K))=0 forces the inflated factor to vanish",
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
    "exact_consequence": {
        "absolute_arithmetic_localization_connecting_map_forced_zero_by_global_naturality": absolute_zero,
        "all_26_source_directions_treated_uniformly": True,
        "connecting_source_directions_exact": "26/26" if absolute_zero else "0/26",
        "arithmetic_localization_connecting_map_computed": absolute_zero,
        "connecting_map_value_if_closed": "ZERO_MAP" if absolute_zero else None,
        "individual_middle_gersten_lift_choices_required_for_closure": False if absolute_zero else True,
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
        "promote exact 26/26 zero connecting map to Stage33-11 closure, then release Stage33-12 arithmetic-HS closure"
        if absolute_zero
        else "decompose the residual H-equivariant Hom block and materialize only the surviving symmetry orbit/block before any per-column fallback"
    ),
}
scout["canonical_sha256"] = csha(scout)
OUT.write_text(json.dumps(scout, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "generator_names": generator_names,
    "Hom_H_A_to_K_dimension_f2": hom_A_K_dim,
    "Hom_H_A_to_finite_H1_dimension_f2": hom_A_H1_dim,
    "absolute_connecting_map_forced_zero": absolute_zero,
    "connecting_source_directions_exact": scout["exact_consequence"]["connecting_source_directions_exact"],
    "route_status": scout["route_status"],
    "certificate_sha256": scout["canonical_sha256"],
    "next": scout["next_exact_leaf"],
}, indent=2, sort_keys=True))
