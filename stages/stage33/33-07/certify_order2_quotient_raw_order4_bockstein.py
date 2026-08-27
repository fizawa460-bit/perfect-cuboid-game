#!/usr/bin/env python3
"""Materialize the nine quotient-order2/raw-order4 first-residue lifts.

PR #1414 proved that A[2] has dimension 26, with 17 sources admitting raw
order-two crossing residues and 9 sources whose raw representatives have exact
order four.  For each of the nine exceptional sources this leaf:

* reconstructs the exact raw Z/4 crossing vector;
* expands its nonzero double in the canonical 44-dimensional U44 unit-symbol
  basis selected by the retained greedy construction;
* proves that complex conjugation changes the chosen raw lift by exactly that
  doubled U44 class (the concrete quotient-to-raw Bockstein defect);
* checks the signed divisor condition modulo 4 on every boundary P1; and
* materializes deterministic order-four first-residue function models on all
  nontrivial boundary components.

This does NOT identify these order-four models with squareclasses.  In
particular it does not compute the project 14x26 L*/L*2 tensor or absolute
localization map.
"""

import hashlib
import json
import runpy
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE_SCRIPT = HERE / "materialize_order2_first_residue_functions.py"
BASE_CERT = HERE / "order2-first-residue-function-liftability.json"
OUT = HERE / "order2-quotient-raw-order4-bockstein.json"
EXPECTED_BASE_CERT_SHA256 = "85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312"


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def component_id(index):
    return f"SIDE_{index + 1:03d}" if index < 24 else f"EXC_{index - 23:03d}"


# Re-run the source-locked #1414 producer and reuse its exact reconstructed
# U44/R17/O12 boundary data.  runpy returns the producer globals without
# weakening any of its internal assertions.
ns = runpy.run_path(str(BASE_SCRIPT))
base_cert = json.loads(BASE_CERT.read_text(encoding="utf-8"))
if base_cert.get("canonical_sha256") != EXPECTED_BASE_CERT_SHA256:
    raise SystemExit("#1414 first-residue certificate moved")
body = dict(base_cert)
claimed = body.pop("canonical_sha256")
if canonical_sha256(body) != claimed:
    raise SystemExit("#1414 first-residue certificate canonical hash mismatch")

rank2 = ns["rank2"]
rowmul2 = ns["rowmul2"]
negate_element = ns["negate_element"]
Uvertex = ns["Uvertex"]
edges = ns["edges"]
edges_data = ns["edges_data"]
cc_edges = ns["cc_edges"]
U44 = ns["U44"]
R17 = ns["R17"]
O4 = ns["O4"]
ib = ns["ib"]
double_obstructions = ns["double_obstructions"]

if len(U44) != 44 or len(R17) != 17 or len(O4) != 12:
    raise SystemExit("retained U44/R17/O12 dimensions moved")
if len(double_obstructions) != 26 or rank2(double_obstructions, 44) != 9:
    raise SystemExit("#1414 obstruction matrix moved")

# Reconstruct exactly which pair of the 14 retained units generated each row
# of the greedy U44 basis.  These labels turn the 44-bit obstruction from
# #1414 into an explicit unit-symbol support list.
selected_u44_pairs = []
selected_u44_rows = []
rank_now = 0
for i, j in combinations(range(14), 2):
    vi, vj = Uvertex[i], Uvertex[j]
    row = [
        (vi[a] * vj[b] - vi[b] * vj[a]) & 1
        for a, b in edges
    ]
    new_rank = rank2(selected_u44_rows + [row], 144)
    if new_rank > rank_now:
        selected_u44_rows.append(row)
        selected_u44_pairs.append([i + 1, j + 1])
        rank_now = new_rank
if selected_u44_rows != U44 or len(selected_u44_pairs) != 44:
    raise SystemExit("greedy U44 unit-pair basis reconstruction moved")

records = []
all_raw_order4 = []
all_obstructions = []
all_cc_defects = []
all_signed_degree_residues = []

for index, generator in enumerate(ib["invariant_factor_generators"], 1):
    multiplier = 1 if int(generator["order"]) == 2 else 2
    original = [
        multiplier * int(x)
        for x in generator["original_R17_O12_coordinates"]
    ]

    raw_mod4 = [0] * 144
    for coefficient, row in zip(original[:17], R17):
        for e, bit in enumerate(row):
            raw_mod4[e] = (raw_mod4[e] + 2 * coefficient * bit) % 4
    for coefficient, row in zip(original[17:], O4):
        for e, value in enumerate(row):
            raw_mod4[e] = (raw_mod4[e] + coefficient * value) % 4

    obstruction = [int(x) & 1 for x in double_obstructions[index - 1]]
    if not any(obstruction):
        if any(x & 1 for x in raw_mod4):
            raise SystemExit(f"A2_{index:02d} should be raw order two but has odd Z4 entries")
        continue

    if not any(x & 1 for x in raw_mod4):
        raise SystemExit(f"A2_{index:02d} obstruction is nonzero without raw order-four entries")

    obstruction_edge = rowmul2(obstruction, U44)
    double_from_raw = [((2 * int(x)) % 4) // 2 for x in raw_mod4]
    if double_from_raw != obstruction_edge:
        raise SystemExit(f"A2_{index:02d} raw double != U44 obstruction")

    cc_raw = [raw_mod4[cc_edges[e]] for e in range(144)]
    if [cc_raw[cc_edges[e]] for e in range(144)] != raw_mod4:
        raise SystemExit(f"A2_{index:02d} raw Z4 conjugation is not involutive")
    defect_mod4 = [(cc_raw[e] - raw_mod4[e]) % 4 for e in range(144)]
    if any(x not in (0, 2) for x in defect_mod4):
        raise SystemExit(f"A2_{index:02d} conjugation defect is not two-torsion")
    cc_defect = [x // 2 for x in defect_mod4]
    if cc_defect != obstruction_edge:
        raise SystemExit(f"A2_{index:02d} conjugation defect != doubled U44 obstruction")

    component_functions = []
    signed_degree_residues = []
    for component in range(72):
        factors = []
        degree = 0
        for e, (a_vertex, b_vertex) in enumerate(edges):
            if component == a_vertex:
                coefficient = (-raw_mod4[e]) % 4
            elif component == b_vertex:
                coefficient = raw_mod4[e] % 4
            else:
                continue
            if coefficient == 0:
                continue

            point = (
                edges_data[e]["side_point"]
                if component < 24
                else edges_data[e]["exceptional_point"]
            )
            a, b = point
            factors.append({
                "edge_id": f"X_{e + 1:04d}",
                "z4_divisor_coefficient": coefficient,
                "point_P1_L_basis": point,
                "linear_factor_bu_minus_av_L_basis": [b, negate_element(a)],
            })
            degree += coefficient

        residue = degree % 4
        signed_degree_residues.append(residue)
        if residue:
            raise SystemExit(
                f"A2_{index:02d} {component_id(component)} signed divisor degree is {residue} mod 4"
            )
        if not factors:
            continue

        full_model = {
            "component_id": component_id(component),
            "coefficient_field": "L=Q(i,sqrt(2))",
            "crossing_factor_convention": "for oriented edge side->exceptional use -r on side and +r on exceptional",
            "selected_crossing_factors": factors,
            "denominator": "v^d",
            "denominator_exponent_d": degree,
            "denominator_exponent_divisible_by_4": True,
            "order4_function_model": "product (b*u-a*v)^c / v^d",
        }
        component_functions.append({
            **full_model,
            "function_model_sha256": canonical_sha256(full_model),
        })

    obstruction_support = []
    for basis_index, bit in enumerate(obstruction):
        if not bit:
            continue
        i, j = selected_u44_pairs[basis_index]
        obstruction_support.append({
            "u44_basis_index_1based": basis_index + 1,
            "unit_pair_indices_1based": [i, j],
            "symbol_label": f"UNIT_{i:02d}_WEDGE_UNIT_{j:02d}",
        })

    packed_raw = sum((int(value) & 3) << (2 * e) for e, value in enumerate(raw_mod4))
    packed_double = sum((int(bit) & 1) << e for e, bit in enumerate(obstruction_edge))
    packed_obstruction = sum((int(bit) & 1) << j for j, bit in enumerate(obstruction))

    record = {
        "source_basis_name": f"A2_{index:02d}",
        "from_invariant_factor": generator["name"],
        "parent_order": int(generator["order"]),
        "parent_multiplier": multiplier,
        "raw_residue_exact_order": 4,
        "raw_z4_crossing_vector_2bit_hex_le": f"{packed_raw:072x}",
        "raw_odd_crossing_entry_count": sum(int(x) & 1 for x in raw_mod4),
        "double_obstruction_U44_f2_hex_le": f"{packed_obstruction:011x}",
        "double_obstruction_crossing_vector_f2_144_hex_le": f"{packed_double:036x}",
        "double_obstruction_u44_basis_support": obstruction_support,
        "complex_conjugation_defect_equals_double_obstruction": True,
        "signed_component_divisor_degrees_mod4": signed_degree_residues,
        "all_signed_component_divisor_degrees_zero_mod4": True,
        "nontrivial_component_order4_function_count": len(component_functions),
        "component_order4_first_residue_functions": component_functions,
        "full_order4_function_package_sha256": canonical_sha256({
            "source_basis_name": f"A2_{index:02d}",
            "component_functions": component_functions,
            "trivial_components_have_function": "1",
        }),
    }
    records.append(record)
    all_raw_order4.append(raw_mod4)
    all_obstructions.append(obstruction)
    all_cc_defects.append(cc_defect)
    all_signed_degree_residues.extend(signed_degree_residues)

if len(records) != 9:
    raise SystemExit(f"expected 9 raw-order4 sources, found {len(records)}")
if rank2(all_obstructions, 44) != 9:
    raise SystemExit("the nine explicit U44 Bockstein defects lost rank 9")
if all_cc_defects != [rowmul2(row, U44) for row in all_obstructions]:
    raise SystemExit("conjugation defect matrix moved")
if any(all_signed_degree_residues):
    raise SystemExit("some order-four component divisor degree is nonzero mod 4")

cert = {
    "schema": "STAGE33_07_QUOTIENT_ORDER2_RAW_ORDER4_BOCKSTEIN_V1",
    "source_locks": {
        "order2_first_residue_liftability_sha256": EXPECTED_BASE_CERT_SHA256,
        "producer": "materialize_order2_first_residue_functions.py",
    },
    "u44_unit_symbol_basis": {
        "dimension_f2": 44,
        "ambient_pair_candidates": 91,
        "selection_rule": "same greedy rank-increase order over pairs (UNIT_i,UNIT_j), i<j, used by #1414 producer",
        "selected_unit_pair_indices_1based": selected_u44_pairs,
    },
    "quotient_to_raw_bockstein": {
        "quotient_A2_dimension_f2": 26,
        "raw_order2_kernel_dimension_f2": 17,
        "raw_order4_quotient_dimension_f2": 9,
        "double_obstruction_rank_f2": 9,
        "nine_source_records": records,
    },
    "order4_function_convention": {
        "oriented_crossing_edge": "side -> exceptional",
        "raw_edge_coefficient": "r in Z/4",
        "side_component_divisor_coefficient": "-r mod 4",
        "exceptional_component_divisor_coefficient": "+r mod 4",
        "crossing_point": "p=[a:b]",
        "homogeneous_boundary_coordinate": "[u:v]",
        "linear_factor": "b*u-a*v",
        "component_function": "product (b*u-a*v)^c / v^d",
        "d": "sum of canonical coefficients c in {1,2,3}",
        "d_divisible_by_4_for_all_materialized_components": True,
        "coefficient_field": "L=Q(i,sqrt(2))",
    },
    "exact_checks": {
        "base_1414_certificate_reproduced_and_locked": True,
        "greedy_U44_basis_recovered_with_44_explicit_unit_pairs": True,
        "exactly_9_sources_have_nonzero_raw_order4_part": True,
        "each_raw_double_equals_its_nonzero_U44_obstruction": True,
        "nine_U44_obstructions_have_rank_9": True,
        "each_complex_conjugation_defect_equals_the_same_doubled_U44_obstruction": True,
        "all_9_raw_order4_vectors_satisfy_signed_component_divisor_degree_zero_mod4": True,
        "all_9_order4_component_first_residue_function_models_materialized": True,
    },
    "constructive_progress": {
        "raw_order2_first_residue_function_models_retained": 17,
        "raw_order4_first_residue_function_models_materialized": 9,
        "all_26_boundary_first_residue_models_materialized_in_mixed_order2_order4_form": True,
        "all_26_are_order2_squareclass_models": False,
        "nine_bockstein_defects_materialized_in_explicit_U44_unit_symbol_basis": True,
        "nine_bockstein_defects_killed": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_HS_closed": False,
    },
    "new_smallest_exact_kernel": "R33-BR2A-9-ORDER4-FIRST-RESIDUE-GALOIS-BOCKSTEIN-COCYCLE",
    "next_exact_leaf": "L33-07-COMPUTE-GALOIS-DIFFERENCE-COCYCLES-FOR-9-ORDER4-FIRST-RESIDUE-LIFTS",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_existence_claim": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(json.dumps({
    "success": True,
    "raw_order2_models_retained": 17,
    "raw_order4_models_materialized": 9,
    "double_obstruction_rank_f2": 9,
    "all_26_boundary_first_residue_models_materialized_mixed_order": True,
    "all_26_order2_squareclass_models": False,
    "certificate_sha256": cert["canonical_sha256"],
    "new_smallest_exact_kernel": cert["new_smallest_exact_kernel"],
    "next_exact_leaf": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
