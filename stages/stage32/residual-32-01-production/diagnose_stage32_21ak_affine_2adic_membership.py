#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

from diagnose_stage32_21aj_2adic_pairing_saturation import (
    EXPECTED_21AI_CANONICAL_SHA256,
    EXPECTED_ANTI_RANK,
    gf2_basis_and_expressions,
    gf2_rank,
    integer_coordinate_matrix,
    matrix_int_list,
)
from direct_picard_reynolds_lattice_diagnostic import (
    EXPECTED_FIXED_RANK,
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    exact_column_lattice_basis_lowrank,
    load_retained,
)
from direct_picard_reynolds_rank2_integral_projection_bound import (
    build_reynolds_numerator,
)
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_21AJ_CANONICAL_SHA256 = (
    "e360d4277135c5191c23e7f422ab669eb20d3363f0ff054073796c12e65598d0"
)
EXPECTED_SMITH_FACTORS = (1,) * 45 + (2,) * 4 + (4,) * 8 + (8,) * 2
MODULUS = 8


def saturation_step_with_transition(a: Matrix) -> tuple[Matrix, Matrix, dict]:
    """One deterministic exact 2-saturation step plus old->new coordinates."""
    basis_indices, expressions = gf2_basis_and_expressions(a)
    basis_set = set(basis_indices)
    dependent_indices = tuple(j for j in range(a.cols) if j not in basis_set)
    defect = len(dependent_indices)
    if defect == 0:
        return a, Matrix.eye(a.cols), {
            "mod2_rank": a.cols,
            "defect": 0,
            "input_basis_sha256": csha(matrix_int_list(a)),
            "output_basis_sha256": csha(matrix_int_list(a)),
        }

    basis_columns = [a[:, j] for j in basis_indices]
    new_columns = list(basis_columns)
    qmap = Matrix.zeros(a.cols, a.cols)

    for k, old_j in enumerate(basis_indices):
        qmap[k, old_j] = 1

    dependency_payload = []
    for q, old_j in enumerate(dependent_indices):
        mask = expressions[old_j]
        even = a[:, old_j]
        support = []
        for k, bcol in enumerate(basis_columns):
            if (mask >> k) & 1:
                even = even - bcol
                qmap[k, old_j] = 1
                support.append(k)
        if any(int(v) % 2 for v in even):
            raise ValueError(f"dependent column {old_j} did not become even")
        new_columns.append(even.applyfunc(lambda v: int(v) // 2))
        qmap[len(basis_indices) + q, old_j] = 2
        dependency_payload.append(
            {
                "old_column_0based": old_j,
                "basis_positions_0based": support,
            }
        )

    enlarged = Matrix.hstack(*new_columns)
    if enlarged * qmap != a:
        raise ValueError("2-saturation transition reconstruction regression")

    return enlarged, qmap, {
        "mod2_rank": len(basis_indices),
        "defect": defect,
        "input_basis_sha256": csha(matrix_int_list(a)),
        "output_basis_sha256": csha(matrix_int_list(enlarged)),
        "old_to_new_coordinate_map_sha256": csha(matrix_int_list(qmap)),
        "dependency_payload_sha256": csha(dependency_payload),
    }


def reconstruct_translation_data(marking: dict, bundle: dict) -> dict:
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    phi = Matrix(
        [
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ]
    )

    N, subgroup, action_hashes_sha = build_reynolds_numerator(
        marking, adapter, gram, phi
    )
    B, module_stats = exact_column_lattice_basis_lowrank(N, EXPECTED_FIXED_RANK)
    C = integer_coordinate_matrix(N, B)
    if B * C != N:
        raise ValueError("N=B*C regression")

    C_dm = DomainMatrix.from_Matrix(C).convert_to(ZZ)
    Dc_dm, Sc_dm, Tc_dm = smith_normal_decomp(C_dm)
    if Sc_dm * C_dm * Tc_dm != Dc_dm:
        raise ValueError("fixed-coordinate Smith reconstruction regression")
    Dc = Dc_dm.to_Matrix()
    Sc = Sc_dm.to_Matrix()
    Tc = Tc_dm.to_Matrix()
    cdiag_signed = tuple(int(Dc[i, i]) for i in range(EXPECTED_FIXED_RANK))
    if tuple(abs(v) for v in cdiag_signed) != (1,) * EXPECTED_FIXED_RANK:
        raise ValueError(f"fixed-coordinate Smith diagonal regression: {cdiag_signed}")

    K = Tc[:, EXPECTED_FIXED_RANK:]
    if K.shape != (PICARD_RANK, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed kernel shape regression")
    if C * K != Matrix.zeros(EXPECTED_FIXED_RANK, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed kernel C-regression")

    pairing = adapter.pairing_matrix
    M = pairing * K
    current = M
    original_coordinate_map = Matrix.eye(EXPECTED_ANTI_RANK)
    steps = []
    defects = []

    for layer in range(29):
        rank2 = gf2_rank(current)
        defect = EXPECTED_ANTI_RANK - rank2
        defects.append(defect)
        if defect == 0:
            break
        enlarged, qmap, step = saturation_step_with_transition(current)
        original_coordinate_map = qmap * original_coordinate_map
        current = enlarged
        if current * original_coordinate_map != M:
            raise ValueError(f"translation coordinate map regression at layer {layer + 1}")
        step["layer_1based"] = layer + 1
        steps.append(step)
    else:
        raise ValueError("2-saturation did not terminate")

    if defects != [14, 10, 2, 0]:
        raise ValueError(f"21aj defect-sequence regression: {defects}")

    F = original_coordinate_map
    F_dm = DomainMatrix.from_Matrix(F).convert_to(ZZ)
    Df_dm, Uf_dm, Vf_dm = smith_normal_decomp(F_dm)
    if Uf_dm * F_dm * Vf_dm != Df_dm:
        raise ValueError("small quotient Smith reconstruction regression")
    Df = Df_dm.to_Matrix()
    Uf = Uf_dm.to_Matrix()
    Vf = Vf_dm.to_Matrix()
    factors = tuple(abs(int(Df[i, i])) for i in range(EXPECTED_ANTI_RANK))
    if factors != EXPECTED_SMITH_FACTORS:
        raise ValueError(f"21aj exact Smith factor regression: {factors}")

    pivot_rows, _ = gf2_basis_and_expressions(current.T)
    if len(pivot_rows) != EXPECTED_ANTI_RANK:
        raise ValueError("final saturated pairing basis lacks 59 mod2-independent rows")
    square = current.extract(list(pivot_rows), list(range(EXPECTED_ANTI_RANK)))
    if int(square.det()) % 2 == 0:
        raise ValueError("selected saturated square minor is not odd")
    square_inv_mod8 = square.inv_mod(MODULUS)
    if (square_inv_mod8 * square).applyfunc(lambda v: int(v) % MODULUS) != Matrix.eye(
        EXPECTED_ANTI_RANK
    ):
        raise ValueError("mod8 inverse regression")

    quotient_from_selected = (Uf * square_inv_mod8).applyfunc(
        lambda v: int(v) % MODULUS
    )

    locked = Matrix.zeros(PICARD_RANK, EXPECTED_FIXED_RANK)
    for i in range(EXPECTED_FIXED_RANK):
        for j in range(EXPECTED_FIXED_RANK):
            value = int(Sc[i, j])
            diag = cdiag_signed[i]
            if value % diag:
                raise ValueError("fixed Smith affine map divisibility regression")
            locked[i, j] = value // diag
    x0_map = Tc * locked
    if C * x0_map != Matrix.eye(EXPECTED_FIXED_RANK):
        raise ValueError("canonical affine representative map regression")
    pairing_x0_map = pairing * x0_map

    selected_x0_map = pairing_x0_map.extract(
        list(pivot_rows), list(range(EXPECTED_FIXED_RANK))
    )
    affine_offset_map = (quotient_from_selected * selected_x0_map).applyfunc(
        lambda v: int(v) % MODULUS
    )

    constraint_rows = []
    for i, factor in enumerate(factors):
        if factor == 1:
            continue
        coeff = tuple(
            int(quotient_from_selected[i, j]) % factor
            for j in range(EXPECTED_ANTI_RANK)
        )
        offset = tuple(
            int(affine_offset_map[i, j]) % factor
            for j in range(EXPECTED_FIXED_RANK)
        )
        support = tuple(j for j, v in enumerate(coeff) if v % factor)
        constraint_rows.append(
            {
                "smith_index_0based": i,
                "modulus": factor,
                "selected_pairing_coefficients": list(coeff),
                "projection_z_offset_coefficients": list(offset),
                "selected_support_positions_0based": list(support),
                "selected_support_curve_indices_0based": [
                    int(pivot_rows[j]) for j in support
                ],
            }
        )

    if len(constraint_rows) != 14:
        raise ValueError(
            f"expected 14 nontrivial affine torsion constraints, got {len(constraint_rows)}"
        )

    selected_M = M.extract(list(pivot_rows), list(range(EXPECTED_ANTI_RANK)))
    for j in range(EXPECTED_ANTI_RANK):
        cmod = (square_inv_mod8 * selected_M[:, j]).applyfunc(
            lambda v: int(v) % MODULUS
        )
        qmod = (Uf * cmod).applyfunc(lambda v: int(v) % MODULUS)
        for i, factor in enumerate(factors):
            if int(qmod[i, 0]) % factor:
                raise ValueError(
                    f"published quotient constraint failed on translation generator {j}, row {i}"
                )

    unvisited = set(range(pairing.rows))
    orbits = []
    curve_to_orbit = {}
    while unvisited:
        seed = min(unvisited)
        orbit = tuple(sorted({g[seed] for g in subgroup}))
        oid = len(orbits)
        orbits.append(orbit)
        for idx in orbit:
            curve_to_orbit[idx] = oid
        unvisited.difference_update(orbit)
    if len(orbits) != 14:
        raise ValueError("stabilizer orbit count regression")
    selected_orbit_ids = [curve_to_orbit[int(i)] for i in pivot_rows]

    orbit_support_counts = []
    for row in constraint_rows:
        orbit_ids = sorted(
            set(selected_orbit_ids[j] for j in row["selected_support_positions_0based"])
        )
        orbit_support_counts.append(
            {
                "smith_index_0based": row["smith_index_0based"],
                "modulus": row["modulus"],
                "support_coordinate_count": len(row["selected_support_positions_0based"]),
                "support_orbit_ids_0based": orbit_ids,
                "support_orbit_count": len(orbit_ids),
            }
        )

    return {
        "adapter": adapter,
        "bridge": bridge,
        "N": N,
        "B": B,
        "C": C,
        "K": K,
        "M": M,
        "Sfinal": current,
        "F": F,
        "Df": Df,
        "Uf": Uf,
        "Vf": Vf,
        "factors": factors,
        "defects": defects,
        "steps": steps,
        "pivot_rows": pivot_rows,
        "square": square,
        "square_inv_mod8": square_inv_mod8,
        "quotient_from_selected": quotient_from_selected,
        "x0_map": x0_map,
        "pairing_x0_map": pairing_x0_map,
        "affine_offset_map": affine_offset_map,
        "constraint_rows": constraint_rows,
        "orbit_support_counts": orbit_support_counts,
        "orbits": orbits,
        "selected_orbit_ids": selected_orbit_ids,
        "module_stats": module_stats,
        "action_hashes_sha": action_hashes_sha,
    }


def build_certificate(marking: dict, bundle: dict) -> dict:
    data = reconstruct_translation_data(marking, bundle)
    factors = data["factors"]
    moduli = [int(v) for v in factors if int(v) != 1]
    cert = {
        "schema": "STAGE32_21AK_EXACT_AFFINE_2ADIC_PAIRING_MEMBERSHIP_INTERFACE_V1",
        "mode": "EXACT_14_CONGRUENCE_AFFINE_FILTER_FROM_SATURATED_PAIRING_BASIS",
        "upstream_21ai_certificate_sha256": EXPECTED_21AI_CANONICAL_SHA256,
        "upstream_21aj_certificate_sha256": EXPECTED_21AJ_CANONICAL_SHA256,
        "anti_fixed_integer_rank": EXPECTED_ANTI_RANK,
        "projection_coordinate_rank": EXPECTED_FIXED_RANK,
        "translation_pairing_shape": [data["M"].rows, data["M"].cols],
        "translation_pairing_sha256": csha(matrix_int_list(data["M"])),
        "two_saturation_defect_sequence": data["defects"],
        "final_saturated_pairing_basis_sha256": csha(matrix_int_list(data["Sfinal"])),
        "original_in_saturated_coordinate_map_sha256": csha(matrix_int_list(data["F"])),
        "small_coordinate_smith": {
            "shape": [data["F"].rows, data["F"].cols],
            "nonzero_diagonal": list(factors),
            "nonunit_factor_count": len(moduli),
            "modulus_multiplicities": {
                "2": moduli.count(2),
                "4": moduli.count(4),
                "8": moduli.count(8),
            },
            "maximum_modulus": max(moduli),
            "left_transform_sha256": csha(matrix_int_list(data["Uf"])),
            "right_transform_sha256": csha(matrix_int_list(data["Vf"])),
            "reconstruction_exact": True,
        },
        "selected_pairing_coordinates": {
            "count": len(data["pivot_rows"]),
            "curve_indices_0based": list(data["pivot_rows"]),
            "stabilizer_orbit_ids_0based": data["selected_orbit_ids"],
            "saturated_square_minor_sha256": csha(matrix_int_list(data["square"])),
            "saturated_square_minor_determinant_is_odd": True,
            "inverse_mod8_sha256": csha(matrix_int_list(data["square_inv_mod8"])),
        },
        "canonical_projection_representative": {
            "formula": "x0(z)=Tc*(Sc*z/Dc_diag,0^59)",
            "x0_map_shape": [data["x0_map"].rows, data["x0_map"].cols],
            "x0_map_sha256": csha(matrix_int_list(data["x0_map"])),
            "C_times_x0_map_is_identity": True,
            "all_integral_classes_with_projection_z": "x0(z)+K*t, t in Z^59",
            "pairing_x0_map_sha256": csha(matrix_int_list(data["pairing_x0_map"])),
        },
        "affine_membership_filter": {
            "constraint_count": len(data["constraint_rows"]),
            "ambient_modulus": MODULUS,
            "constraint_moduli": moduli,
            "constraint_rows": data["constraint_rows"],
            "constraint_rows_sha256": csha(data["constraint_rows"]),
            "orbit_support_summary": data["orbit_support_counts"],
            "orbit_support_summary_sha256": csha(data["orbit_support_counts"]),
            "criterion": (
                "for projection coordinate z and candidate integral pairing vector y, "
                "let s be y restricted to selected 59 curve rows; every genuine lift "
                "must satisfy row_i(s)-offset_i(z) == 0 mod smith_factor_i "
                "for all 14 nonunit rows"
            ),
            "verified_on_all_59_translation_generators": True,
            "failure_is_safe_nonmembership_certificate": True,
            "passing_does_not_enforce_81_rational_relations": True,
            "passing_is_necessary_not_sufficient_for_nonnegative_fiber_feasibility": True,
        },
        "next_leaf": (
            "32-21al: combine these 14 affine mod-2/4/8 constraints with the "
            "14 fixed stabilizer-orbit totals and test exact nonnegative "
            "composition feasibility on the deterministic representative FULL178 shard"
        ),
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "unknown_is_not_unsat": True,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_21ak_picard")
    marking = load_retained(args.marking, "s32_21ak_marking")
    cert = build_certificate(marking, bundle)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    interface = cert["affine_membership_filter"]
    support = interface["orbit_support_summary"]
    print(
        json.dumps(
            {
                "verdict": "PASS_STAGE32_21AK_EXACT_AFFINE_2ADIC_MEMBERSHIP_INTERFACE",
                "constraint_count": interface["constraint_count"],
                "modulus_multiplicities": cert["small_coordinate_smith"][
                    "modulus_multiplicities"
                ],
                "maximum_modulus": cert["small_coordinate_smith"]["maximum_modulus"],
                "selected_pairing_coordinate_count": cert[
                    "selected_pairing_coordinates"
                ]["count"],
                "min_constraint_orbit_support": min(
                    row["support_orbit_count"] for row in support
                ),
                "max_constraint_orbit_support": max(
                    row["support_orbit_count"] for row in support
                ),
                "canonical_sha256": cert["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
