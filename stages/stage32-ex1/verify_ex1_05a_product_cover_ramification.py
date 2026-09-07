#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "ex1-05a-product-cover-ramification.json"

data = json.loads(CERT.read_text(encoding="utf-8"))

# Canonical digest with the digest field omitted.
claimed = data["canonical_sha256_without_this_field"]
payload = dict(data)
payload.pop("canonical_sha256_without_this_field")
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
actual = hashlib.sha256(canonical).hexdigest()
assert actual == claimed, (actual, claimed)

T = data["target"]
pairings = T["exceptional_pairings"]
assert len(pairings) == 48
assert sum(pairings) == 266
assert sum(m > 0 for m in pairings) == 47
unit_labels = [i + 1 for i, m in enumerate(pairings) if m == 1]
assert unit_labels == [1, 2, 3, 7, 15, 20, 22, 24, 36]
assert len(unit_labels) == 9
nonunit = [m for m in pairings if m >= 2]
assert len(nonunit) == 38

# Stoll-Testa product quotient adapter arithmetic.
assert 2 * 5 - 2 == 4 * (2 * 2 - 2) == 8
assert data["derived_cover_adapter"]["X_to_C2_degree"] == 4
assert data["derived_cover_adapter"]["Y_to_C2xC2_degree"] == 4

C = data["curve_pullback_argument"]
assert T["canonical_degree"] == 186
assert C["canonical_degree_on_D_from_Sbar"] == 372 == 2 * 186
assert C["projection_degree_sum"] == 186
assert C["projection_degree_max_lower_bound"] == 93
assert C["ramification_degree_lower_bound"] == 186 == 2 * 93

N = data["node_branch_consequences"]
assert N["normalization_node_branch_count_lower_bound"] == 186
assert N["node_fiber_excess_lower_bound"] == 186 - 47 == 139
assert N["node_fiber_excess_upper_bound"] == 266 - 47 == 219
assert N["contact_order_excess_upper_bound"] == 266 - 186 == 80
assert N["nonunit_normalization_branch_count_lower_bound"] == 186 - 9 == 177

capacities = sorted((m - 1 for m in nonunit), reverse=True)
assert sum(capacities[:13]) == 138
assert sum(capacities[:14]) == 145
assert N["minimum_number_of_multibranch_nonunit_nodes"] == 14
assert N["no_node_multibranch_branch_excluded_candidate"] is True

assert data["exit"]["residual_configurations_all_disposed"] is False
assert data["exit"]["positive_witness_established"] is False
assert data["exit"]["full_target_closure"] is False

F = data["firewalls"]
for key in [
    "ramification_degree_identified_with_total_delta_472",
    "normalization_node_branch_count_identified_with_exceptional_mass_266",
    "node_fiber_excess_identified_with_delta",
    "product_cover_argument_promoted_to_full_v6_exclusion",
    "smooth_locus_singularities_discarded",
    "arsenal_nonmatch_treated_as_repository_absence",
    "stage32_main_credit",
    "receiver_credit",
    "theorem_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert F[key] is False, key

print("PASS EX1-05A product-cover ramification replay")
print("canonical_sha256", actual)
print("R_node_lower", 186)
print("B_node_range", [139, 219])
print("contact_order_excess_upper", 80)
print("minimum_multibranch_nonunit_nodes", 14)
