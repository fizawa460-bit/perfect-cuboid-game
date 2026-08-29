#!/usr/bin/env python3
"""Certify the abstract full-surface J2 zero Kummer-defect direction.

This leaf deliberately does not assign J2 to one of the retained ten
coordinate basis vectors.  The retained interface certifies the Q-defined
full-surface J2 direction, but not its original proper-Br2 coordinates.
"""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ADJUST = HERE / "full-surface-hs-adjustment-contract.json"
OUT = HERE / "j2-full-surface-mu2-zero-defect-contract.json"

EXPECTED_ADJUST = "f1b34a61119da7bbf2ee47ccf457a962e1e127ab5464082426f1948ce7321c43"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


adjust = json.loads(ADJUST.read_text(encoding="utf-8"))
body = dict(adjust)
claimed = body.pop("canonical_sha256", None)
if claimed != EXPECTED_ADJUST or csha(body) != EXPECTED_ADJUST:
    raise SystemExit("full-surface HS adjustment source lock moved")

module = adjust["full_surface_proper_adjustment_module"]
firewall = adjust["k3_to_full_surface_firewall"]
if module["module"] != "P=Br(Sbar)[2]^{G_Q}":
    raise SystemExit("proper adjustment module regression")
if not module["kernel_contains_q_defined_J2"]:
    raise SystemExit("Q-defined J2 kernel contract regressed")
if not firewall["J2_full_surface_q_defined_pullback_certified_elsewhere"]:
    raise SystemExit("full-surface Q-defined J2 pullback contract regressed")

certificate = {
    "schema": "STAGE33_12_J2_FULL_SURFACE_MU2_ZERO_DEFECT_CONTRACT_V1",
    "source_locks": {
        "full_surface_hs_adjustment_contract_sha256": EXPECTED_ADJUST,
    },
    "exact_input": {
        "class": "J2",
        "full_surface_q_defined_pullback_certified": True,
        "j2_certified_inside_P_equals_BrSbar2_GQ": True,
    },
    "kummer_exact_sequence": {
        "sequence": "Pic(S)/2 -> H^2_et(S,mu_2) -> Br(S)[2] -> 0",
        "arithmetic_mu2_lift_exists": True,
        "reason": (
            "The retained full-surface contract certifies a Q-defined J2 direction "
            "in the 2-torsion proper adjustment module; exactness of the arithmetic "
            "Kummer sequence supplies a mu_2 lift of its Q-defined Brauer representative."
        ),
    },
    "finite_v4_consequence": {
        "geometric_mu2_lift_is_v4_invariant": True,
        "delta_Kum_V4_of_J2": "EXACT_ZERO",
        "integral_bockstein_of_this_zero_defect": "EXACT_ZERO",
        "known_zero_defect_direction_dimension_lower_bound_f2": 1,
    },
    "coordinate_firewall": {
        "j2_vector_in_original_proper_br2_coordinates_materialized": False,
        "j2_coordinates_in_retained_10_vector_P_basis_materialized": False,
        "existing_75x10_matrix_column_index_identified": False,
        "columns_materialized": 0,
        "matrix_entries_materialized": 0,
        "reason": (
            "The retained interfaces certify the full-surface Q-defined J2 direction "
            "but do not identify its vector in the source-locked 14-dimensional "
            "proper-Br2 coordinate system. A zero abstract direction is not silently "
            "assigned to an existing basis column."
        ),
    },
    "absolute_firewall": {
        "finite_V4_zero_implies_absolute_zero": False,
        "absolute_H1_identified_with_finite_V4_H1": False,
    },
    "next_exact_leaf": (
        "MATERIALIZE_J2_TO_PROPER14_COORDINATE_ADAPTER_OR_ONE_EQUIVALENT_NON_J2_"
        "FULL_SURFACE_MU2_GLUE_COLUMN"
    ),
    "promotion_firewall": {
        "proper_d2_map_computed": False,
        "finite_obstruction_cosets_materialized": 0,
        "arithmetic_hs_d2_computed": False,
        "global_q_residue_lifts_complete": False,
        "stage33_12_closed": False,
        "stage33_07_closed": False,
        "stage33_progress": "6/11",
        "theorem_credit": False,
        "endpoint_credit": False,
    },
}
certificate["canonical_sha256"] = csha(certificate)
OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "delta_Kum_V4_of_J2": "EXACT_ZERO",
    "coordinate_column_materialized": False,
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
