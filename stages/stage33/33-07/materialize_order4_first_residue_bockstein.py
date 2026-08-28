#!/usr/bin/env python3
"""Resolve the nine quotient-only A[2] directions as exact order-four residues.

The preceding exact leaf proves that A[2] has dimension 26, with a 17-dimensional
kernel of the quotient-to-raw doubling obstruction and a rank-9 image in the
known U44 unit-symbol residue space.  This leaf does not pretend those nine
classes have raw order-two lifts.  Instead it:

* reconstructs the exact U44 basis together with its generating unit-symbol pair;
* materializes the obstruction/Bockstein map beta : A[2] -> U44;
* proves ker(beta) has dimension 17 and im(beta) has dimension 9;
* proves the nine quotient-only basis elements map independently to im(beta);
* materializes deterministic order-four P1 residue functions for all 26 sources;
* verifies that doubling each order-four function gives exactly beta(source).

Thus all 26 source directions acquire explicit first-residue functions, but nine
of them live genuinely at order four.  No connecting-map column, 14x26
squareclass tensor, absolute delta_loc, or arithmetic HS closure is claimed.
"""
import json
import runpy
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "materialize_order2_first_residue_functions.py"
OUT = HERE / "order4-first-residue-bockstein.json"

ns = runpy.run_path(str(BASE))
canonical_sha256 = ns["canonical_sha256"]
rank2 = ns["rank2"]
ib = ns["ib"]
edges = ns["edges"]
edges_data = ns["edges_data"]
Uvertex = ns["Uvertex"]
U44 = ns["U44"]
R17 = ns["R17"]
O4 = ns["O4"]
Odoubles = ns["Odoubles"]
solve61 = ns["solve61"]
negate_element = ns["negate_element"]
source_records_order2 = ns["source_records"]

if len(U44) != 44 or len(R17) != 17 or len(O4) != 12 or len(edges) != 144:
    raise SystemExit("upstream raw residue basis shape regression")
if len(ib["invariant_factor_generators"]) != 26:
    raise SystemExit("A[2] basis dimension regression")

# Recover provenance of the exact greedy U44 basis.  The old construction uses
# the 91 pairwise wedges of the 14 unit valuation vectors, retaining a row iff
# it raises the F2 rank.  Record the corresponding unit pair for each retained
# basis row and verify bit-for-bit equality with the upstream U44 basis.
unit_symbol_basis = []
rebuilt_U44 = []
rank_now = 0
for i, j in combinations(range(14), 2):
    vi, vj = Uvertex[i], Uvertex[j]
    row = [
        (vi[a] * vj[b] - vi[b] * vj[a]) & 1
        for a, b in edges
    ]
    new_rank = rank2(rebuilt_U44 + [row], 144)
    if new_rank > rank_now:
        rebuilt_U44.append(row)
        unit_symbol_basis.append({
            "u44_basis_index_1based": len(rebuilt_U44),
            "unit_pair_1based": [i + 1, j + 1],
            "symbol_name": f"{{UNIT_{i+1:02d},UNIT_{j+1:02d}}}",
        })
        rank_now = new_rank
if rebuilt_U44 != U44 or len(unit_symbol_basis) != 44:
    raise SystemExit("U44 unit-symbol provenance reconstruction moved")


def obstruction_and_mod4(generator):
    multiplier = 1 if int(generator["order"]) == 2 else 2
    original = [multiplier * int(x) for x in generator["original_R17_O12_coordinates"]]
    mod4 = [0] * 144
    for coefficient, row in zip(original[:17], R17):
        for e, bit in enumerate(row):
            mod4[e] = (mod4[e] + 2 * coefficient * bit) % 4
    for coefficient, row in zip(original[17:], O4):
        for e, value in enumerate(row):
            mod4[e] = (mod4[e] + coefficient * value) % 4

    # 2*x in Z/4, divided by 2, is x mod 2.  R17 terms therefore disappear
    # and the odd O4 coefficients give the exact U44-valued Bockstein.
    double_vector = [x & 1 for x in mod4]
    coords = solve61(double_vector)
    if any(coords[44:]):
        raise SystemExit("order-four double escaped U44")
    return multiplier, original, mod4, coords[:44]


source_rows = []
obstruction_rows = []
quotient_only_rows = []
all_order4_models = []

for source_index, generator in enumerate(ib["invariant_factor_generators"], 1):
    multiplier, original, mod4, obstruction = obstruction_and_mod4(generator)
    obstruction_rows.append(obstruction)
    raw_order2 = not any(obstruction)
    old = source_records_order2[source_index - 1]
    if bool(old["raw_order2_first_residue_function_liftable"]) != raw_order2:
        raise SystemExit(f"A2_{source_index:02d} liftability moved")
    if old["double_obstruction_U44_f2_hex_le"] != f"{sum(bit << j for j, bit in enumerate(obstruction)):011x}":
        raise SystemExit(f"A2_{source_index:02d} obstruction lock moved")

    if not raw_order2:
        quotient_only_rows.append(obstruction)

    # The mod-4 crossing vector is a cycle.  Since every edge is oriented from
    # a side component to an exceptional component, all incident signs at a
    # fixed component agree.  Hence the unsigned sum of local exponents is 0
    # mod 4.  This makes the homogeneous denominator v^D a fourth power in the
    # Kummer class and yields a deterministic function on every P1 component.
    component_models = []
    nontrivial_components = 0
    for component in range(72):
        factors = []
        D = 0
        for e, (a, b) in enumerate(edges):
            exponent = int(mod4[e]) % 4
            if not exponent or component not in (a, b):
                continue
            point = (
                edges_data[e]["side_point"]
                if component < 24
                else edges_data[e]["exceptional_point"]
            )
            pa, pb = point
            factors.append({
                "edge_id": f"X_{e+1:04d}",
                "exponent_mod4": exponent,
                "point_P1_L_basis": point,
                "linear_factor_bu_minus_av_L_basis": [pb, negate_element(pa)],
            })
            D += exponent
        if D % 4:
            raise SystemExit(
                f"A2_{source_index:02d} component {component+1}: mod4 degree {D} is not divisible by 4"
            )
        if factors:
            nontrivial_components += 1
        component_models.append({
            "component_id": (
                f"SIDE_{component+1:03d}" if component < 24
                else f"EXC_{component-23:03d}"
            ),
            "numerator_factors": factors,
            "denominator": "v^D",
            "denominator_exponent_D": D,
            "denominator_exponent_divisible_by_4": True,
        })

    # Doubling the explicit order-four residue vector must reproduce the exact
    # U44 obstruction crossing vector, not just its abstract coordinates.
    doubled_f2 = [x & 1 for x in mod4]
    reconstructed_double = [0] * 144
    for coeff, row in zip(obstruction, U44):
        if coeff:
            reconstructed_double = [x ^ y for x, y in zip(reconstructed_double, row)]
    if doubled_f2 != reconstructed_double:
        raise SystemExit(f"A2_{source_index:02d}: explicit function double != U44 Bockstein")

    symbols = [
        unit_symbol_basis[j]["symbol_name"]
        for j, bit in enumerate(obstruction) if bit
    ]
    obstruction_hex = f"{sum(bit << j for j, bit in enumerate(obstruction)):011x}"
    mod4_hex = "".join(format(sum((mod4[4*k+t] & 3) << (2*t) for t in range(4)), "02x") for k in range(36))
    model_body = {
        "source_basis_name": f"A2_{source_index:02d}",
        "components": component_models,
        "trivial_component_function": "1",
        "function_convention": "product (b*u-a*v)^e / v^D, e in {0,1,2,3}, D=sum e divisible by 4",
    }
    model_sha = canonical_sha256(model_body)
    all_order4_models.append(model_body)
    source_rows.append({
        "source_basis_name": f"A2_{source_index:02d}",
        "from_invariant_factor": generator["name"],
        "parent_order": int(generator["order"]),
        "parent_multiplier": multiplier,
        "raw_order2_liftable": raw_order2,
        "genuine_order4_required": not raw_order2,
        "raw_crossing_residue_mod4_packed_hex": mod4_hex,
        "u44_bockstein_coordinates_f2_hex_le": obstruction_hex,
        "u44_bockstein_symbol_support": symbols,
        "u44_bockstein_symbol_weight": len(symbols),
        "nontrivial_component_function_count": nontrivial_components,
        "all_72_component_order4_function_model_sha256": model_sha,
    })

obstruction_rank = rank2(obstruction_rows, 44)
quotient_only_rank = rank2(quotient_only_rows, 44)
zero_count = sum(not any(row) for row in obstruction_rows)
nonzero_count = 26 - zero_count
if (obstruction_rank, quotient_only_rank, zero_count, nonzero_count) != (9, 9, 17, 9):
    raise SystemExit(
        "Bockstein profile regression "
        f"rank={obstruction_rank} qrank={quotient_only_rank} zero={zero_count} nonzero={nonzero_count}"
    )

# Since the nine nonzero basis images are independent, their span maps
# isomorphically onto im(beta); no change of basis can enlarge ker(beta) beyond
# the exact 17-dimensional raw-order-two subspace.
cert = {
    "schema": "STAGE33_07_ORDER4_FIRST_RESIDUE_BOCKSTEIN_V1",
    "source": "exact reconstruction from materialize_order2_first_residue_functions.py locked inputs",
    "boundary_component_count": 72,
    "crossing_count": 144,
    "unit_rank": 14,
    "u44_unit_symbol_rank_f2": 44,
    "u44_basis_with_unit_pair_provenance": unit_symbol_basis,
    "a2_dimension_f2": 26,
    "bockstein_map": {
        "domain": "A[2] quotient source",
        "codomain": "U44 known unit-symbol residue space",
        "matrix_shape_f2": [26, 44],
        "matrix_rows_f2": obstruction_rows,
        "rank_f2": obstruction_rank,
        "kernel_dimension_f2": 26 - obstruction_rank,
        "image_dimension_f2": obstruction_rank,
        "zero_basis_image_count": zero_count,
        "nonzero_basis_image_count": nonzero_count,
        "nine_nonzero_basis_images_independent": quotient_only_rank == 9,
        "quotient_only_span_maps_isomorphically_to_image": True,
        "raw_order2_liftable_subspace_is_maximal_dimension_17": True,
    },
    "source_basis": source_rows,
    "order4_function_materialization": {
        "all_26_sources_materialized": True,
        "raw_order2_sources_also_recovered_as_even_exponent_order4_models": True,
        "genuine_order4_source_count": 9,
        "every_component_denominator_exponent_divisible_by_4": True,
        "doubling_every_model_matches_exact_u44_bockstein": True,
        "full_models_sha256": canonical_sha256(all_order4_models),
    },
    "exact_consequence": {
        "nine_obstructions_are_intrinsic_not_a_bad_basis_artifact": True,
        "cannot_replace_the_9_by_additional_raw_order2_lifts": True,
        "all_26_first_residue_directions_now_have_explicit_order4_function_models": True,
        "remaining_issue_is_to_propagate_the_rank9_u44_bockstein_through_the_middle_gersten_extension": True,
    },
    "constructive_progress": {
        "raw_order2_first_residue_functions_materialized": 17,
        "genuine_order4_first_residue_functions_materialized": 9,
        "all_26_first_residue_functions_materialized_at_order_dividing_4": True,
        "nine_u44_bocksteins_materialized_with_unit_symbol_support": True,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
    },
    "new_smallest_exact_kernel": "R33-BR2A-RANK9-U44-BOCKSTEIN-PROPAGATION-THROUGH-MIDDLE-GERSTEN",
    "next_exact_leaf": "L33-07-PUSH-RANK9-U44-BOCKSTEIN-THROUGH-MIDDLE-GERSTEN-BEFORE-ANY-14x26-SQUARECLASS-TENSOR",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(json.dumps({
    "success": True,
    "a2_dimension_f2": 26,
    "raw_order2_kernel_dimension_f2": 17,
    "u44_bockstein_rank_f2": 9,
    "genuine_order4_source_count": 9,
    "all_26_order4_function_models_materialized": True,
    "certificate_sha256": cert["canonical_sha256"],
    "next_exact_leaf": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
