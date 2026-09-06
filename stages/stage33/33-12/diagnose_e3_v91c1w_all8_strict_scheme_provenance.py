#!/usr/bin/env python3
"""V91C1W scratch: source-bind all eight V91C1S strict divisor schemes as far as exact data allow.

No Stage33 credit. Replays V91C1V, reconstructs exact 33-11d/e carrier refinements,
and uses the retained known140 Picard64 marking to certify the six direct-support
multi-match schemes by divisor decomposition/exhaustivity/multiplicity.  The two
remaining exact reduced primes stay unresolved unless an independent Picard64
relation is available.  No complete Pic/2 reduction is inferred here.
"""
from __future__ import annotations

import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
V_PATH = HERE / "diagnose_e3_v91c1v_actual_prime_known140_locator.py"

vns = runpy.run_path(str(V_PATH))
sns = vns["sns"]
kns = vns["kns"]

needed = sorted(sns["strict_package_difference"])
assert len(needed) == 8
matches = vns["matches"]
contained_known_classes = vns["contained_known_classes"]

old_to_canonical = sns["old_to_canonical"]
canonical_generators = sns["canonical_generators"]
prime_records = sns["prime_records"]
prime_action = sns["prime_action"]
carrier_refinements = sns["e11"]["prime_inventory"]["carrier_refinements"]

known = kns["known"]
hyperplane = kns["hyperplane"]
gram = kns["gram"]
pairing = kns["pairing"]
row_times_matrix = kns["row_times_matrix"]
actions = kns["actions"]
assert len(known) == 140 and len(hyperplane) == 64 and len(actions) == 2
assert pairing(hyperplane, hyperplane, gram) == 16


def vadd(a, b):
    return [x + y for x, y in zip(a, b)]


def vscale(n, a):
    return [n * x for x in a]


def vsum(rows):
    out = [0] * 64
    for row in rows:
        out = vadd(out, row)
    return out


def act_swap23(row):
    # V91C1Q word swap12 * swap13 * swap12.  The retained Picard actions are
    # involutions in the same row-vector convention used by the 33-07 verifier.
    out = row
    for matrix in (actions[0], actions[1], actions[0]):
        out = row_times_matrix(out, matrix)
    return out


canonical_to_old = {}
for old_id, canonical_id in old_to_canonical.items():
    canonical_to_old.setdefault(canonical_id, []).append(old_id)
for ids in canonical_to_old.values():
    ids.sort()

image_to_sources = {}
for source_id, image_id in prime_action.items():
    image_to_sources.setdefault(image_id, []).append(source_id)
for ids in image_to_sources.values():
    ids.sort()


def compact_record(old_id):
    row = prime_records[old_id]
    out = {"old_prime_id": old_id, "kind": row["kind"]}
    if row["kind"] == "AUDITED_33_11D_DIRECT_PRIME_SUPPORT":
        out.update({
            "carrier_id": row["carrier_id"],
            "reduced_support": row["reduced_support"],
            "scheme_multiplicity_in_carrier": int(row["scheme_multiplicity_in_carrier"]),
        })
    else:
        out.update({
            "source_representative": row["source_representative"],
            "transport_provenance": row["transport_provenance"],
        })
    return out


def carriers_for_old(old_id):
    row = prime_records[old_id]
    if row["kind"] == "AUDITED_33_11D_DIRECT_PRIME_SUPPORT":
        return [row["carrier_id"]]
    return sorted({x["carrier_id"] for x in row["transport_provenance"]})


def picard_sum_for_matches(class_indices):
    return vsum([known[j - 1] for j in class_indices])


# Certify every direct-support carrier needed by the eight targets.  For each
# carrier, the audited 33-11d multiplicities give its complete refinement as a
# hyperplane section.  Every matched known curve is an exact contained curve.
# If the weighted sum of those known-curve classes is exactly H, then any
# additional component or extra multiplicity would give a nonzero effective
# residual divisor of positive H-degree.  Hence the displayed decomposition is
# exhaustive with the displayed component multiplicities.
relevant_direct_carriers = set()
for target_id in needed:
    source_ids = set(canonical_to_old.get(target_id, []))
    source_ids.update(image_to_sources.get(target_id, []))
    # source_ids currently mixes old IDs for retained targets and canonical IDs
    # for acted preimages; normalize below.
    canonical_sources = set()
    if canonical_to_old.get(target_id):
        canonical_sources.add(target_id)
    canonical_sources.update(image_to_sources.get(target_id, []))
    for source_id in canonical_sources:
        for old_id in canonical_to_old.get(source_id, []):
            row = prime_records[old_id]
            if row["kind"] == "AUDITED_33_11D_DIRECT_PRIME_SUPPORT":
                relevant_direct_carriers.add(row["carrier_id"])

carrier_certificates = {}
direct_piece_classes = {}
for carrier_id in sorted(relevant_direct_carriers):
    pieces_out = []
    weighted_class = [0] * 64
    weighted_degree = 0
    for piece in carrier_refinements[carrier_id]:
        old_id = piece["prime_id"]
        row = prime_records[old_id]
        if row["kind"] != "AUDITED_33_11D_DIRECT_PRIME_SUPPORT":
            raise SystemExit(f"mixed direct carrier refinement: {carrier_id}")
        canonical_id = old_to_canonical[old_id]
        component_matches = contained_known_classes(canonical_generators[canonical_id])
        if not component_matches:
            raise SystemExit(f"direct support has no known component: {canonical_id}")
        component_class = picard_sum_for_matches(component_matches)
        multiplicity = int(piece["multiplicity"])
        direct_piece_classes[canonical_id] = component_class
        component_degree = pairing(component_class, hyperplane, gram)
        weighted_class = vadd(weighted_class, vscale(multiplicity, component_class))
        weighted_degree += multiplicity * component_degree
        pieces_out.append({
            "canonical_id": canonical_id,
            "old_prime_id": old_id,
            "support": row["reduced_support"],
            "scheme_multiplicity_in_carrier": multiplicity,
            "known92_irreducible_components": component_matches,
            "component_count": len(component_matches),
            "picard64_class": component_class,
            "hyperplane_degree": component_degree,
            "component_multiplicity_inside_reduced_support": 1,
        })
    if weighted_class != hyperplane:
        raise SystemExit(f"direct carrier Picard64 exhaustion failed: {carrier_id}")
    if weighted_degree != 16:
        raise SystemExit(f"direct carrier H-degree exhaustion failed: {carrier_id}")
    carrier_certificates[carrier_id] = {
        "pieces": pieces_out,
        "weighted_piece_class_equals_hyperplane": True,
        "weighted_hyperplane_degree": weighted_degree,
        "hyperplane_square": 16,
        "exact_decomposition_exhaustive": True,
        "scheme_multiplicities_source_bound": True,
        "residual_effective_divisor_excluded_by_positive_hyperplane_degree": True,
    }

rows = []
resolved_target_classes = {}
unresolved_targets = []
for target_id in needed:
    retained_old = canonical_to_old.get(target_id, [])
    acted_sources = image_to_sources.get(target_id, [])
    if not retained_old and len(acted_sources) != 1:
        raise SystemExit(f"unresolved target provenance: {target_id}")
    canonical_sources = sorted(set(([target_id] if retained_old else []) + acted_sources))
    source_rows = []
    parent_carriers = set()
    candidate_classes = []
    exact_prime_provenance = False
    for source_id in canonical_sources:
        olds = canonical_to_old.get(source_id, [])
        for old_id in olds:
            parent_carriers.update(carriers_for_old(old_id))
            if prime_records[old_id]["kind"] == "EXACT_REDUCED_PRIME_IDEAL":
                exact_prime_provenance = True
        source_class = direct_piece_classes.get(source_id)
        target_class_from_source = None
        if source_class is not None:
            target_class_from_source = (
                source_class if source_id == target_id
                else act_swap23(source_class)
            )
            candidate_classes.append(target_class_from_source)
        source_rows.append({
            "canonical_id": source_id,
            "is_target_itself_retained": source_id == target_id and bool(retained_old),
            "maps_to_target_under_swap23": prime_action.get(source_id) == target_id,
            "known92_matches": contained_known_classes(canonical_generators[source_id]),
            "old_records": [compact_record(x) for x in olds],
            "picard64_class_if_direct_support": source_class,
            "target_picard64_class_via_swap23_if_direct_support": target_class_from_source,
        })
    if candidate_classes:
        if any(row != candidate_classes[0] for row in candidate_classes[1:]):
            raise SystemExit(f"inconsistent direct-support target class: {target_id}")
        target_class = candidate_classes[0]
        # The target-side known-component sum is an independent check whenever
        # V91C1V found components there.
        if matches[target_id] and picard_sum_for_matches(matches[target_id]) != target_class:
            raise SystemExit(f"target known-component class mismatch: {target_id}")
        resolved_target_classes[target_id] = target_class
        resolution = "RESOLVED_DIRECT_SUPPORT_EXACT_DECOMPOSITION"
    else:
        target_class = None
        unresolved_targets.append(target_id)
        resolution = "UNRESOLVED_EXACT_REDUCED_PRIME" if exact_prime_provenance else "UNRESOLVED"
    rows.append({
        "target_id": target_id,
        "difference_coefficient": int(sns["strict_package_difference"][target_id]),
        "target_known92_matches": matches[target_id],
        "target_retained": bool(retained_old),
        "target_old_records": [compact_record(x) for x in retained_old],
        "retained_sources_or_preimages": source_rows,
        "parent_carriers": sorted(parent_carriers),
        "picard64_resolution": resolution,
        "target_picard64_class": target_class,
    })

assert len(resolved_target_classes) == 6
assert len(unresolved_targets) == 2
assert sorted(unresolved_targets) == sorted(p for p in needed if not matches[p])

partial_strict_difference_class = [0] * 64
for prime_id, cls in resolved_target_classes.items():
    partial_strict_difference_class = vadd(
        partial_strict_difference_class,
        vscale(int(sns["strict_package_difference"][prime_id]), cls),
    )

result = {
    "success": True,
    "credit": False,
    "marker": "V91C1W_ALL8_STRICT_SCHEME_PICARD64_SOURCE_BINDING_SCRATCH",
    "strict_scheme_count": len(rows),
    "rows": rows,
    "relevant_direct_carrier_count": len(carrier_certificates),
    "direct_carrier_decomposition_certificates": carrier_certificates,
    "picard64_classes_assigned": len(resolved_target_classes),
    "picard64_classes_unresolved": len(unresolved_targets),
    "resolved_target_ids": sorted(resolved_target_classes),
    "unresolved_target_ids": sorted(unresolved_targets),
    "six_multi_match_schemes_exactly_decomposed": True,
    "direct_support_decomposition_exhaustivity_verified": True,
    "direct_support_scheme_multiplicity_verified": True,
    "two_zero_match_exact_primes_still_unresolved": True,
    "partial_strict_difference_picard64_class": partial_strict_difference_class,
    "complete_strict_difference_picard64_class_computed": False,
    "pic2_cech_difference_class_computed": False,
    "a2_02_swap23_seed_fixed_mod_pic2": False,
    "a2_02_marked_brauer_image_excluded_from_mask20": False,
}
print(json.dumps(result, sort_keys=True))
