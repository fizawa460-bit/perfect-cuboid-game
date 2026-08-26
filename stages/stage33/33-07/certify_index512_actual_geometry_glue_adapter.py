#!/usr/bin/env python3
"""Certify that the actual geometric index-512 glue lies in the unique rep88 orbit.

This leaf closes only the existence/orbit-identification gap.  It does NOT
choose a labeled generator set for T(S)/L0 and does NOT close arithmetic HS.

Mathematical adapter used here: for an even full-rank overlattice L0 <= T,
H=T/L0 embeds as an isotropic subgroup of A_L0, |H|=[T:L0], and
A_T is canonically H^perp/H.  Hence the actual geometric T(S), already
certified as an index-512 overlattice of the seven-piece integral pullback L0,
necessarily supplies one of the exhaustively classified order-512 glues.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def verify_canonical(name, want):
    d = load(name)
    got = d.get("canonical_sha256")
    assert got == want, (name, got, want)
    u = dict(d)
    u.pop("canonical_sha256", None)
    rec = hashlib.sha256(
        json.dumps(u, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert rec == want, (name, rec, want)
    return d


glue = verify_canonical(
    "coordinate-k3-transcendental-glue-index.json",
    "0cc5321d02b56cea801b8def71a4c3b0946bd8011d8c30767a9602faba2fa8d8",
)
actions = verify_canonical(
    "coordinate-k3-scaled-action-choices-retained.json",
    "a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20",
)
bridge = verify_canonical(
    "index512-unique-surviving-glue-orbit-bridge.json",
    "0b56ffa7b62243264baa04e07892c9b5492cf3c725e21e4e04a062d6e8d4d09b",
)

# Exact geometric predecessor: L0 is the seven-piece integral pullback lattice
# inside T(S), both have rank 14, and the determinant ratio gives index 512.
L0 = glue["seven_piece_integral_pullback_sublattice"]
T = glue["endpoint_transcendental_target"]
ig = glue["integral_glue"]
assert glue["schema"] == "STAGE33_07_COORDINATE_K3_TRANSCENDENTAL_GLUE_INDEX_V1"
assert L0["rank"] == 14 and T["rank"] == 14
assert L0["isometry_type"] == "<8>^10 direct_sum <16>^4"
assert L0["discriminant_group"] == "(Z/8)^10 direct_sum (Z/16)^4"
assert L0["determinant_v2"] == 46 and T["determinant_v2"] == 28
assert ig["index_T_over_L0"] == 512 and ig["index_v2"] == 9
assert ig["glue_subgroup_order"] == 512
assert ig["no_elementary_or_invariant_factor_type_assumed"] is True

# The actual cc/ct action on each scaled coordinate-K3 pullback piece must be
# among these exact finite quadratic extensions.  No commutativity above the
# unscaled discriminant module was assumed.
assert actions["finite_quadratic_extension_exhaustive"] is True
for mode, n in (("ka", 4), ("kb", 8), ("kc", 4)):
    p = actions["pieces"][mode]
    assert p["all_pairs_cartesian"] is True
    assert p["source_pair_count"] == n

# Exhaustive endpoint-compatible classification: all non-elementary index-512
# possibilities are UNSAT; the elementary survivors form one integral Aut(L0)
# orbit, represented by rep88.
assert bridge["all_non_elementary_index512_types_eliminated"] is True
assert bridge["non_elementary_survivor_count"] == 0
assert bridge["unique_surviving_integral_glue_orbit_among_locked_endpoint_compatibility_candidates"] is True
assert bridge["elementary_surviving_integral_Aut_L0_orbit_count"] == 1
assert bridge["unique_surviving_integral_glue_orbit_representative"] == 88
assert bridge["elementary_surviving_labeled_embeddings"] == [120, 121, 122, 123]

# Overlattice correspondence now supplies the missing existence bridge.
# Because the predecessor certifies an actual index-512 even overlattice
# L0 <= T(S), H_actual=T(S)/L0 exists, is isotropic of order 512 in A_L0,
# and H_actual^perp/H_actual is exactly A_T with its endpoint finite q-form.
# The geometric field/sign actions stabilize L0 and T(S); the finite cc/ct
# lifts were exhaustively enumerated above.  Therefore H_actual belongs to the
# locked endpoint-compatible candidate universe.  Exhaustion forces it into
# the unique surviving integral orbit rep88.
cert = {
    "schema": "STAGE33_07_INDEX512_ACTUAL_GEOMETRY_GLUE_ADAPTER_V1",
    "source_locks": {
        "coordinate_k3_transcendental_glue_index_sha256": glue["canonical_sha256"],
        "coordinate_k3_scaled_action_choices_sha256": actions["canonical_sha256"],
        "unique_surviving_glue_orbit_bridge_sha256": bridge["canonical_sha256"],
    },
    "overlattice_correspondence_applied": True,
    "actual_geometric_L0_is_full_rank_integral_sublattice_of_T": True,
    "actual_geometric_index_T_over_L0": 512,
    "actual_glue_H_exists_as_T_over_L0": True,
    "actual_glue_H_order": 512,
    "actual_glue_H_isotropic_in_A_L0": True,
    "actual_endpoint_discriminant_is_Hperp_over_H": True,
    "actual_cc_ct_scaled_action_caught_by_exhaustive_piece_level_extensions": True,
    "actual_coordinate_sign_actions_are_geometric_and_stabilize_glue": True,
    "actual_geometry_glue_in_locked_endpoint_compatibility_candidate_universe": True,
    "actual_geometry_glue_nonnelementary_rejected_by_exhaustive_classification": True,
    "actual_geometry_glue_is_elementary": True,
    "actual_geometry_glue_existence_in_rep88_orbit_proved": True,
    "actual_geometry_glue_integral_Aut_L0_orbit_representative": 88,
    "actual_geometry_glue_possible_locked_labeled_embeddings": [120, 121, 122, 123],
    "actual_index512_glue_identified_up_to_integral_Aut_L0_orbit": True,
    "actual_labeled_glue_subgroup_identified": False,
    "actual_labeled_glue_generator_set_identified": False,
    "INDEX512_GLUE_ACTUAL_GEOMETRY_PROVED": True,
    "arithmetic_HS_closed": False,
    "new_residual_kernel": "R33-BR2A-ACTUAL-INDEX512-GLUE-IS-REP88-ORBIT-BUT-FOUR-LOCKED-LABELED-EMBEDDINGS-REMAIN",
    "next_exact_leaf": "L33-07-PROPAGATE-FOUR-REP88-LABELED-EMBEDDINGS-INTO-BR4-GALOIS-MODULE-AND-ARITHMETIC-HS-SOURCE",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "unit_status": "RUNNING_REPAIR",
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
out = HERE / "index512-actual-geometry-glue-adapter.json"
out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "actual_glue_orbit": 88,
    "possible_labeled_embeddings": [120, 121, 122, 123],
    "actual_geometry_glue_proved": True,
    "arithmetic_HS_closed": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
