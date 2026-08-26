#!/usr/bin/env python3
"""Certify the exact geometric existence data for the index-512 glue.

This adapter deliberately stops before arithmetic cc/ct compatibility.
The finite discriminant-module cc/ct lift census does not by itself promote
those actions to the actual integral Betti lattice T(S).  Therefore it cannot
be used to place the actual glue into the later q+V4 candidate universe or to
identify the actual glue with rep88.

For an even full-rank overlattice L0 <= T, H=T/L0 embeds as an isotropic
subgroup of A_L0, |H|=[T:L0], and A_T = H^perp/H as finite quadratic forms.
That geometric statement is the exact credit taken here.
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

cert = {
    "schema": "STAGE33_07_INDEX512_ACTUAL_GEOMETRY_GLUE_ADAPTER_V2_FIREWALLED",
    "source_locks": {
        "coordinate_k3_transcendental_glue_index_sha256": glue["canonical_sha256"],
    },
    "overlattice_correspondence_applied": True,
    "actual_geometric_L0_is_full_rank_integral_sublattice_of_T": True,
    "actual_geometric_index_T_over_L0": 512,
    "actual_glue_H_exists_as_T_over_L0": True,
    "actual_glue_H_order": 512,
    "actual_glue_H_isotropic_in_A_L0": True,
    "actual_endpoint_discriminant_is_Hperp_over_H": True,
    "actual_endpoint_finite_q_form_must_match_locked_endpoint": True,
    "finite_discriminant_cc_ct_extension_census_is_not_integral_betti_promotion": True,
    "arithmetic_cc_ct_action_on_integral_T_proved": False,
    "actual_geometry_glue_in_q_plus_V4_candidate_universe_proved": False,
    "actual_geometry_glue_nonnelementary_rejected_by_V4_classification": False,
    "actual_geometry_glue_is_elementary": False,
    "actual_geometry_glue_existence_in_rep88_orbit_proved": False,
    "actual_index512_glue_identified_up_to_integral_Aut_L0_orbit": False,
    "actual_labeled_glue_subgroup_identified": False,
    "actual_labeled_glue_generator_set_identified": False,
    "INDEX512_GLUE_ACTUAL_GEOMETRY_PROVED": False,
    "arithmetic_HS_closed": False,
    "safe_geometric_next_route": "classify order-512 glues using endpoint finite q plus the seven geometric coordinate-sign involutions, without arithmetic cc/ct V4",
    "new_residual_kernel": "R33-BR2A-ACTUAL-INDEX512-GLUE-EXISTS-BUT-ARITHMETIC-V4-ON-INTEGRAL-T-NOT-PROMOTED",
    "next_exact_leaf": "L33-07-FULL-Q-PLUS-SEVEN-GEOMETRIC-SIGNS-WITHOUT-ARITHMETIC-V4",
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
    "actual_glue_exists": True,
    "actual_glue_order": 512,
    "rep88_proved": False,
    "arithmetic_integral_T_action_proved": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
