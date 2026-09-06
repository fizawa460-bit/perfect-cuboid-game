#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
AB = HERE / "post1648ab-galois-v4-orbit-intersections.json"
GAP = HERE / "post1556-carrier-invariance-source-gap.json"
CERT = HERE / "post1648ac-galois-v4-common-support-interface-wall.json"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def canonical(obj, field):
    x = dict(obj)
    x.pop(field, None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

ab = load(AB)
gap = load(GAP)
cert = load(CERT)

assert canonical(ab, "canonical_sha256_without_this_field") == "7b36625f61fd1c2d7868f2f5b5a7deaeb6dc50835cba77b0189e2b676e0cbcf1"
assert canonical(gap, "canonical_sha256_without_this_field") == "256cbd7d1a3f3667d1558e530293392a3068f52cd8dfa1495f14cb3015caa308"
assert canonical(cert, "canonical_sha256_without_this_field") == "9f3e922a48b8131c6f86f81dc3e203fe05cc8fae01f86073edf66cbc93095158"

cg = ab["conditional_geometric_consequence"]
orbit = ab["exact_galois_v4_orbit"]
assert cg["Q_rational_points_fixed_by_cc_and_ct"] is True
assert cg["Q_rational_points_lie_in_all_four_conjugate_curves"] is True
assert cg["smallest_pair"] == "C_intersection_ctC"
assert cg["smallest_pairwise_intersection_length"] == 1026
assert orbit["all_four_classes_pairwise_distinct"] is True
assert orbit["pairwise_intersections"]["D.ctD"] == 1026

missing = gap["missing_member_level_data"]
assert missing["defining_equation_or_ideal_for_N"] is False
assert missing["distinguished_defining_section_for_N"] is False
assert missing["uniqueness_of_integral_carrier_in_fixed_V6_class"] is False
assert missing["picard_class_invariance_sufficient_for_member_invariance"] is False

red = cert["exact_conditional_common_support_reduction"]
assert red["Q_rational_points_lie_in_all_four_conjugate_curves"] is True
assert red["four_way_common_support_is_subscheme_of_smallest_pair"] is True
assert red["conditional_four_way_common_support_length_upper_bound"] == 1026
assert red["actual_four_way_common_support_materialized"] is False
assert red["rational_support_identified"] is False

iface = cert["retained_member_level_interface"]
assert iface["defining_equation_or_ideal_for_carrier_member"] is False
assert iface["distinguished_defining_section_for_carrier_member"] is False
assert iface["uniqueness_of_integral_carrier_in_fixed_V6_class"] is False
assert iface["class_level_data_sufficient_to_materialize_member_intersection_support"] is False

app = cert["current_main_asset_applicability"]
assert app["stage33_v91c1v_locator_checked"] is True
assert app["locator_starts_from_explicit_strict_prime_ideal_generators"] is True
assert app["locator_inverts_positive_picard_class_to_distinguished_prime"] is False
assert app["applicable_to_unknown_positive_square_V6_member_without_ideal"] is False
assert app["category_mismatch"] is True

dec = cert["decision"]
assert dec["simultaneous_survivor_exclusion_achieved"] is False
assert dec["Q602_excluded"] is False
assert dec["O210_excluded"] is False
assert dec["O212_plus_advance_allowed"] is False
assert cert["fixed_target"]["surviving_residues_decimal"] == [73, 97, 235]

print(json.dumps({
    "certificate_canonical_sha256": "9f3e922a48b8131c6f86f81dc3e203fe05cc8fae01f86073edf66cbc93095158",
    "four_way_common_support_length_upper_bound": 1026,
    "actual_common_support_materialized": False,
    "member_level_ideal_materialized": False,
    "stage33_locator_category_mismatch": True,
    "survivors_current_credit": [73, 97, 235],
    "Q602_excluded": False,
    "O210_excluded": False,
    "verdict": "PASS_STAGE32_POST1648AC_COMMON_SUPPORT_INTERFACE_WALL_NONEXCLUSION"
}, sort_keys=True))
