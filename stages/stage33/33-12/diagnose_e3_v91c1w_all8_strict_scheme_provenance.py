#!/usr/bin/env python3
"""V91C1W scratch: classify all eight V91C1S strict divisor schemes.

No Stage33 credit. Replays V91C1V and records, for every strict scheme in the
swap23 package difference, whether it is retained or an acted image, its
33-11d/e source record, parent-carrier refinement provenance, and known92
containment both before and after swap23. This is a diagnostic for the
all-eight Picard64 source-binding leaf; it does not assign Picard classes.
"""
from __future__ import annotations

import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
V_PATH = HERE / "diagnose_e3_v91c1v_actual_prime_known140_locator.py"

vns = runpy.run_path(str(V_PATH))
sns = vns["sns"]

needed = sorted(sns["strict_package_difference"])
assert len(needed) == 8
matches = vns["matches"]
contained_known_classes = vns["contained_known_classes"]

old_to_canonical = sns["old_to_canonical"]
canonical_generators = sns["canonical_generators"]
prime_records = sns["prime_records"]
prime_action = sns["prime_action"]
carrier_refinements = sns["e11"]["prime_inventory"]["carrier_refinements"]

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


def carrier_summary(carrier_id):
    pieces = []
    for piece in carrier_refinements[carrier_id]:
        old_id = piece["prime_id"]
        canonical_id = old_to_canonical[old_id]
        generators = canonical_generators[canonical_id]
        pieces.append({
            "old_prime_id": old_id,
            "canonical_id": canonical_id,
            "multiplicity": int(piece["multiplicity"]),
            "known92_matches": contained_known_classes(generators),
            "kind": prime_records[old_id]["kind"],
        })
    return pieces

rows = []
for target_id in needed:
    retained_old = canonical_to_old.get(target_id, [])
    acted_sources = image_to_sources.get(target_id, [])
    # Every outside-inventory target must have a unique retained source under
    # the involutive swap23 action. Retained targets may also be action images.
    if not retained_old and len(acted_sources) != 1:
        raise SystemExit(f"unresolved target provenance: {target_id}")
    source_ids = sorted(set(([target_id] if retained_old else []) + acted_sources))
    source_rows = []
    parent_carriers = set()
    for source_id in source_ids:
        olds = canonical_to_old.get(source_id, [])
        for old_id in olds:
            parent_carriers.update(carriers_for_old(old_id))
        source_rows.append({
            "canonical_id": source_id,
            "is_target_itself_retained": source_id == target_id and bool(retained_old),
            "maps_to_target_under_swap23": prime_action.get(source_id) == target_id,
            "known92_matches": contained_known_classes(canonical_generators[source_id]),
            "old_records": [compact_record(x) for x in olds],
        })
    rows.append({
        "target_id": target_id,
        "difference_coefficient": int(sns["strict_package_difference"][target_id]),
        "target_known92_matches": matches[target_id],
        "target_retained": bool(retained_old),
        "target_old_records": [compact_record(x) for x in retained_old],
        "retained_sources_or_preimages": source_rows,
        "parent_carriers": {
            carrier_id: carrier_summary(carrier_id)
            for carrier_id in sorted(parent_carriers)
        },
    })

result = {
    "success": True,
    "credit": False,
    "marker": "V91C1W_ALL8_STRICT_SCHEME_PROVENANCE_SCRATCH",
    "strict_scheme_count": len(rows),
    "rows": rows,
    "picard64_classes_assigned": 0,
    "pic2_cech_difference_class_computed": False,
}
print(json.dumps(result, sort_keys=True))