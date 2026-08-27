#!/usr/bin/env python3
"""Compact the detailed raw-order4 Bockstein certificate for source control."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "order2-quotient-raw-order4-bockstein.json"
OUT = HERE / "order2-quotient-raw-order4-bockstein-compact.json"


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


x = json.loads(SRC.read_text(encoding="utf-8"))
body = dict(x)
claimed = body.pop("canonical_sha256")
if canonical_sha256(body) != claimed:
    raise SystemExit("detailed Bockstein certificate hash mismatch")

compact = {
    "schema": "STAGE33_07_QUOTIENT_ORDER2_RAW_ORDER4_BOCKSTEIN_COMPACT_V1",
    "full_certificate_sha256": claimed,
    "source_locks": x["source_locks"],
    "u44_unit_symbol_basis": {
        "dimension_f2": x["u44_unit_symbol_basis"]["dimension_f2"],
        "ambient_pair_candidates": x["u44_unit_symbol_basis"]["ambient_pair_candidates"],
        "selected_unit_pair_indices_1based": x["u44_unit_symbol_basis"]["selected_unit_pair_indices_1based"],
    },
    "quotient_to_raw_bockstein": {
        key: value
        for key, value in x["quotient_to_raw_bockstein"].items()
        if key != "nine_source_records"
    },
    "nine_source_records": [],
    "exact_checks": x["exact_checks"],
    "constructive_progress": x["constructive_progress"],
    "new_smallest_exact_kernel": x["new_smallest_exact_kernel"],
    "next_exact_leaf": x["next_exact_leaf"],
    "stage33_progress": x["stage33_progress"],
    "stage33_08_released": x["stage33_08_released"],
    "theorem_credit": x["theorem_credit"],
    "endpoint_credit": x["endpoint_credit"],
}

for r in x["quotient_to_raw_bockstein"]["nine_source_records"]:
    compact["nine_source_records"].append({
        "source_basis_name": r["source_basis_name"],
        "from_invariant_factor": r["from_invariant_factor"],
        "parent_order": r["parent_order"],
        "parent_multiplier": r["parent_multiplier"],
        "raw_residue_exact_order": r["raw_residue_exact_order"],
        "raw_z4_crossing_vector_2bit_hex_le": r["raw_z4_crossing_vector_2bit_hex_le"],
        "raw_odd_crossing_entry_count": r["raw_odd_crossing_entry_count"],
        "double_obstruction_U44_f2_hex_le": r["double_obstruction_U44_f2_hex_le"],
        "double_obstruction_crossing_vector_f2_144_hex_le": r["double_obstruction_crossing_vector_f2_144_hex_le"],
        "double_obstruction_u44_basis_support": r["double_obstruction_u44_basis_support"],
        "complex_conjugation_defect_equals_double_obstruction": r["complex_conjugation_defect_equals_double_obstruction"],
        "all_signed_component_divisor_degrees_zero_mod4": r["all_signed_component_divisor_degrees_zero_mod4"],
        "nontrivial_component_order4_function_count": r["nontrivial_component_order4_function_count"],
        "full_order4_function_package_sha256": r["full_order4_function_package_sha256"],
    })

compact["canonical_sha256"] = canonical_sha256(compact)
OUT.write_text(json.dumps(compact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "full_certificate_sha256": claimed,
    "compact_certificate_sha256": compact["canonical_sha256"],
    "nine_source_count": len(compact["nine_source_records"]),
}, indent=2, sort_keys=True))
