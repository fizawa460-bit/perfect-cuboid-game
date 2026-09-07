#!/usr/bin/env python3
"""Compact R4 inventory of retained A2_02 local chart/function data.

This diagnostic intentionally reads the retained Stage33-07 payloads repo-side
and emits only the selected A2_02 rows and field inventories needed to decide
whether a literal cover-indexed H2(mu2) representative can be constructed.
It grants no H2/Brauer/fixedness credit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
SIDE = S07 / "mixed-order-side-ambient-function-lifts.json"
EXC = S07 / "mixed-order-exceptional-ambient-tangent-function-lifts.json"
OUT = HERE / "e3-v91c1x-r4-a2-02-local-chart-inventory.json"
SOURCE = "A2_02"
EXPECTED = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def compact_factor(f: dict) -> dict:
    out = {
        "keys": sorted(f),
        "edge_id": f.get("edge_id"),
        "exponent": int(f.get("exponent", 1)),
    }
    for key in (
        "ambient_linear_factor_coefficients_L_basis",
        "ambient_tangent_linear_factor_coefficients_L_basis",
        "coefficients_Qi",
    ):
        if key in f:
            out[key] = f[key]
    return out


side = load(SIDE)
exc = load(EXC)
srow = next(r for r in side["source_ambient_side_lifts"] if r["source_basis_name"] == SOURCE)
erow = next(r for r in exc["source_ambient_exceptional_lifts"] if r["source_basis_name"] == SOURCE)

side_rows = []
for r in srow["side_ambient_function_lifts"]:
    side_rows.append({
        "component_id": r["component_id"],
        "row_keys": sorted(r),
        "denominator_keys": sorted(r.get("denominator", {})),
        "denominator_exponent": int(r.get("denominator", {}).get("exponent", 0)),
        "D_coefficients_L_basis": r.get("D_coefficients_L_basis"),
        "numerator_factors": [compact_factor(f) for f in r.get("numerator_factors", [])],
    })

exc_rows = []
for r in erow["exceptional_ambient_tangent_function_lifts"]:
    exc_rows.append({
        "component_id": r["component_id"],
        "row_keys": sorted(r),
        "denominator_keys": sorted(r.get("denominator", {})),
        "denominator_exponent": int(r.get("denominator", {}).get("exponent", 0)),
        "ambient_projection_R0_R1_coefficients_L_basis": r.get(
            "ambient_projection_R0_R1_coefficients_L_basis"
        ),
        "numerator_factors": [compact_factor(f) for f in r.get("numerator_factors", [])],
    })

components = [r["component_id"] for r in exc_rows] + [r["component_id"] for r in side_rows]
cert = {
    "schema": "stage33.e3.v91c1x_r4.a2_02_local_chart_inventory.v1",
    "stage": "33-12",
    "role": "EXACT_NONCREDIT_R4_SOURCE_INVENTORY",
    "source_direction": SOURCE,
    "source_paths": {
        "side": str(SIDE.relative_to(HERE.parents[2])),
        "exceptional": str(EXC.relative_to(HERE.parents[2])),
    },
    "raw_order": {
        "side": int(srow["raw_order"]),
        "exceptional": int(erow["raw_order"]),
    },
    "components": components,
    "expected_components_exact": components == EXPECTED,
    "side_rows": side_rows,
    "exceptional_rows": exc_rows,
    "construction_questions": {
        "side_rows_expose_component_local_equation_beyond_D": any(
            any(k in r["row_keys"] for k in ("local_equation", "uniformizer", "chart", "patch"))
            for r in side_rows
        ),
        "exceptional_rows_expose_component_local_equation_beyond_R0_R1": any(
            any(k in r["row_keys"] for k in ("local_equation", "uniformizer", "chart", "patch"))
            for r in exc_rows
        ),
        "rows_expose_cover_or_overlap_indices": any(
            any("overlap" in k.lower() or "cover" in k.lower() for k in r["row_keys"])
            for r in side_rows + exc_rows
        ),
        "rows_expose_edge_ids": any(
            any(f.get("edge_id") is not None for f in r["numerator_factors"])
            for r in side_rows + exc_rows
        ),
    },
    "credit_firewall": {
        "accepted_source_representative_materialized": False,
        "literal_mu2_2_cocycle_materialized": False,
        "equivalent_unimodular_cech_glue_materialized": False,
        "swap23_common_refinement_materialized": False,
        "h2_fixedness_credit": False,
        "mask20_credit": False,
        "theorem_credit": False,
        "merge_allowed": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "marker": "V91C1X_R4_A2_02_LOCAL_CHART_INVENTORY",
    "component_count": len(components),
    "expected_components_exact": cert["expected_components_exact"],
    "construction_questions": cert["construction_questions"],
    "certificate_sha256": cert["canonical_sha256"],
}, sort_keys=True))
