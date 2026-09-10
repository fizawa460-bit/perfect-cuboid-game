#!/usr/bin/env python3
"""Compact the verbose lane-e ambiguity audit into a context-safe certificate."""
import hashlib
import json
import sys

x = json.load(sys.stdin)
out = {
    "success": x["success"],
    "schema": "STAGE33_KUMMER_E_75X10_ABSTRACT_V4_AMBIGUITY_COMPACT_V1",
    "scope": x["scope"],
    "source_result_canonical_sha256": x["canonical_sha256"],
    "source_locks": x["source_locks"],
    "revoked_relation_firewall": x["revoked_relation_firewall"],
    "extension_solution_space": x["extension_solution_space"],
    "matrix": {
        "rows_h1": x["matrix"]["rows_h1"],
        "columns_retained_sources": x["matrix"]["columns_retained_sources"],
        "scalar_entries": x["matrix"]["scalar_entries"],
        "residual_ambiguity_dimension_f2": x["matrix"]["residual_ambiguity_dimension_f2"],
        "independent_linear_constraints_on_750_entries": x["matrix"]["scalar_entries"] - x["matrix"]["residual_ambiguity_dimension_f2"],
        "column_ambiguity_dimensions_f2": x["matrix"]["column_ambiguity_dimensions_f2"],
        "forced_columns_one_based": x["matrix"]["forced_columns_one_based"],
        "forced_entry_count": x["matrix"]["forced_entry_count"],
        "forced_entries_all_zero": x["matrix"]["forced_entries_all_zero"],
        "forced_entry_global_indices_zero_based": [e["global_zero_based"] for e in x["matrix"]["forced_entries"]],
        "coordinate_index_convention": "global=75*(source_one_based-1)+(h1_one_based-1)",
    },
    "minimal_coordinate_measurement_plan": {
        "minimum_scalar_entry_measurements": x["minimal_coordinate_measurement_plan"]["minimum_scalar_entry_measurements"],
        "measurement_global_indices_zero_based": [e["global_zero_based"] for e in x["minimal_coordinate_measurement_plan"]["entries"]],
        "coordinate_index_convention": "global=75*(source_one_based-1)+(h1_one_based-1)",
        "reason": x["minimal_coordinate_measurement_plan"]["reason"],
    },
    "firewall": x["firewall"],
}
body = json.dumps(out, sort_keys=True, separators=(",", ":"))
out["canonical_sha256"] = hashlib.sha256(body.encode()).hexdigest()
print(json.dumps(out, indent=2, sort_keys=True))
