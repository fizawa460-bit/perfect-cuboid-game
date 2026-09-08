#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
B3B1 = HERE / "e3-v91c1x-r5b3b1-a2-02-317-1757-boundary-uniformizers.json"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
C4B1A = HERE / "e3-v91c1x-r5b3b3c4b1a-exceptional-nonsquare-obstruction-census-and-correction-preflight.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1b-uniformizer-scalar-gauge-obstruction-reduction.json"

B3B1_SHA = "8a5dcb751b312a846a06fac88298166efe8c1fd91ed0988b3cb04a408cfc2654"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
C4B1A_SHA = "2bdd01db7b77de5e1587bb0a1c367da5039610b1266c8d5e77b10a63742e3a6f"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved: {path.name}: "
            f"claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def qi_decode(z):
    return Fraction(int(z[0]), int(z[1])), Fraction(int(z[2]), int(z[3]))


def qi_encode(z):
    return [
        z[0].numerator,
        z[0].denominator,
        z[1].numerator,
        z[1].denominator,
    ]


def qi_mul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def rational_sqrt(q: Fraction):
    if q < 0:
        return None
    sn = math.isqrt(q.numerator)
    sd = math.isqrt(q.denominator)
    if sn * sn != q.numerator or sd * sd != q.denominator:
        return None
    return Fraction(sn, sd)


def qi_is_square(z) -> bool:
    a, b = z
    if a == 0 and b == 0:
        return True
    norm = a * a + b * b
    r = rational_sqrt(norm)
    if r is None:
        return False
    sx = rational_sqrt((r + a) / 2)
    sy = rational_sqrt((r - a) / 2)
    if sx is None or sy is None:
        return False
    for x in {sx, -sx}:
        for y in {sy, -sy}:
            if qi_mul((x, y), (x, y)) == z:
                return True
    return False


def rref_squareclass_system(rows: list[dict], nvars: int):
    work = [
        {
            "bits": list(row["bits"]),
            "rhs": row["rhs"],
            "source_ids": [row["exceptional_id"]],
        }
        for row in rows
    ]
    pivot_cols = []
    rank = 0
    for col in range(nvars):
        pivot = next((r for r in range(rank, len(work)) if work[r]["bits"][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for r in range(len(work)):
            if r == rank or not work[r]["bits"][col]:
                continue
            work[r]["bits"] = [a ^ b for a, b in zip(work[r]["bits"], work[rank]["bits"])]
            work[r]["rhs"] = qi_mul(work[r]["rhs"], work[rank]["rhs"])
            work[r]["source_ids"] = sorted(set(work[r]["source_ids"] + work[rank]["source_ids"]))
        pivot_cols.append(col)
        rank += 1
        if rank == len(work):
            break

    contradictions = []
    for row in work:
        if not any(row["bits"]) and not qi_is_square(row["rhs"]):
            contradictions.append({
                "source_exceptional_ids": row["source_ids"],
                "rhs_Qi": qi_encode(row["rhs"]),
                "rhs_is_square_in_Qi": False,
            })

    solution = [(Fraction(1), Fraction(0)) for _ in range(nvars)]
    if not contradictions:
        for r, col in enumerate(pivot_cols):
            solution[col] = work[r]["rhs"]
    return rank, pivot_cols, contradictions, solution


def build_certificate() -> dict:
    b3b1 = load_locked(B3B1, B3B1_SHA)
    b3b2 = load_locked(B3B2, B3B2_SHA)
    c4a = load_locked(C4A, C4A_SHA)
    c4b1a = load_locked(C4B1A, C4B1A_SHA)

    if not b3b1["construction_status"]["eight_residue_function_uniformizer_pairs_materialized"]:
        raise SystemExit("B3B1 eight formal pairs moved")
    if not b3b2["formal_tame_symbol_sum"]["formal_symbol_sum_materialized"]:
        raise SystemExit("B3B2 formal symbol sum moved")

    components = list(b3b2["formal_tame_symbol_sum"]["component_ids_in_source_order"])
    if len(components) != 8 or len(set(components)) != 8:
        raise SystemExit("formal symbol component inventory moved")

    c4a_by_eid = {
        row["exceptional_id"]: row
        for row in c4a["exceptional_prime_preflight"]["rows"]
    }
    obstruction_rows = list(
        c4b1a["exceptional_obstruction_census"]["nonsquare_obstruction_rows"]
    )
    if len(obstruction_rows) != 31:
        raise SystemExit("C4B1A obstruction count moved")

    constant_rows = []
    nonconstant_rows = []
    for row in obstruction_rows:
        factors = list(row["combined_residue_squareclass"]["odd_irreducible_factors"])
        if factors:
            nonconstant_rows.append(row)
            continue
        eid = row["exceptional_id"]
        arow = c4a_by_eid[eid]
        bits = [int(arow["v_f_by_symbol_component"][component]) & 1 for component in components]
        rhs = qi_decode(row["combined_residue_squareclass"]["factorization_coefficient_Qi"])
        if qi_is_square(rhs):
            raise SystemExit(f"constant-only obstruction coefficient became square: {eid}")
        constant_rows.append({
            "exceptional_id": eid,
            "bits": bits,
            "rhs": rhs,
            "incidence_support_components": [
                component for component, bit in zip(components, bits) if bit
            ],
        })

    if len(constant_rows) != 27 or len(nonconstant_rows) != 4:
        raise SystemExit(
            f"constant/nonconstant obstruction partition moved: {len(constant_rows)}/{len(nonconstant_rows)}"
        )

    nonconstant_ids = sorted(row["exceptional_id"] for row in nonconstant_rows)
    expected_nonconstant = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]
    if nonconstant_ids != expected_nonconstant:
        raise SystemExit(f"nonconstant exceptional support moved: {nonconstant_ids}")

    rank, pivots, contradictions, solution = rref_squareclass_system(constant_rows, len(components))
    consistent = not contradictions

    adjusted_rows = []
    all_adjusted_constant_square = False
    if consistent:
        for row in constant_rows:
            factor = (Fraction(1), Fraction(0))
            for bit, scalar in zip(row["bits"], solution):
                if bit:
                    factor = qi_mul(factor, scalar)
            adjusted = qi_mul(row["rhs"], factor)
            adjusted_rows.append({
                "exceptional_id": row["exceptional_id"],
                "adjusted_constant_Qi": qi_encode(adjusted),
                "adjusted_constant_is_square_in_Qi": qi_is_square(adjusted),
            })
        all_adjusted_constant_square = all(
            row["adjusted_constant_is_square_in_Qi"] for row in adjusted_rows
        )
        if not all_adjusted_constant_square:
            raise SystemExit("constructed scalar-gauge solution failed exact square replay")

    scalar_rows = [
        {
            "component_id": component,
            "uniformizer_scalar_Qi": qi_encode(scalar),
            "uniformizer_scalar_squareclass_trivial": qi_is_square(scalar),
        }
        for component, scalar in zip(components, solution)
    ] if consistent else []

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1b.uniformizer_scalar_gauge_obstruction_reduction.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1B_BOUNDARY_PRESERVING_UNIFORMIZER_SCALAR_GAUGE_OBSTRUCTION_REDUCTION",
        "role": "EXACT_NONCREDIT_DIAGNOSTIC_OF_CONSTANT_UNIFORMIZER_GAUGE_ON_C4B1_EXCEPTIONAL_RESIDUES",
        "entry": {
            "pr": 1695,
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
        },
        "source_locks": {
            "r5b3b1_boundary_uniformizers_sha256": B3B1_SHA,
            "r5b3b2_formal_symbol_sum_sha256": B3B2_SHA,
            "r5b3b3c4a_tame_residue_parity_preflight_sha256": C4A_SHA,
            "r5b3b3c4b1a_obstruction_census_sha256": C4B1A_SHA,
        },
        "gauge_model": {
            "transformation": "pi_D -> c_D * pi_D for one nonzero constant c_D in Q(i)^* per each of the eight formal symbol components",
            "constant_scaling_preserves_uniformizer_valuations": True,
            "designated_boundary_residue_function_f_D_is_not_modified": True,
            "exceptional_residue_effect_mod_squares": "multiply the residue at E by product_D c_D^(v_E(f_D) mod 2)",
            "field": "Q(i)",
            "unknown_scalar_count": 8,
            "component_ids_in_source_order": components,
            "important_firewall": "This is a boundary-data-preserving Gersten/formal-symbol gauge diagnostic. It is not certified to preserve a particular named global H2(mu2) or Brauer representative without the missing source-bound Cech/Kummer comparison.",
        },
        "obstruction_partition": {
            "c4b1_total_nonsquare_exceptional_count": 31,
            "constant_only_nonsquare_count": 27,
            "nonconstant_function_field_factor_nonsquare_count": 4,
            "nonconstant_function_field_factor_exceptional_ids": nonconstant_ids,
            "constant_only_exceptional_ids": sorted(row["exceptional_id"] for row in constant_rows),
            "nonconstant_rows_cannot_be_made_square_by_multiplying_by_Qi_constants": True,
        },
        "constant_scalar_squareclass_system": {
            "equation_count": len(constant_rows),
            "unknown_count": len(components),
            "incidence_matrix_rank_f2": rank,
            "pivot_component_ids": [components[j] for j in pivots],
            "consistent_in_Qi_squareclass_group": consistent,
            "contradiction_rows": contradictions,
            "one_exact_scalar_representative_solution": scalar_rows,
            "all_27_adjusted_constant_residues_square_trivial": all_adjusted_constant_square,
            "adjusted_constant_rows": adjusted_rows,
        },
        "exact_consequence": {
            "uniformizer_constant_gauge_can_kill_all_27_constant_only_exceptional_obstructions": consistent and all_adjusted_constant_square,
            "uniformizer_constant_gauge_cannot_kill_the_four_nonconstant_function_field_obstructions": True,
            "uniformizer_constant_gauge_cannot_make_the_current_formal_symbol_unramified_on_all_48_exceptional_primes": True,
            "a_nonconstant_cover_or_cech_level_correction_is_required_before_exceptional_unramifiedness_can_hold": True,
            "no_named_h2_or_brauer_source_equivalence_credit_follows_from_this_gauge_diagnostic": True,
        },
        "construction_status": {
            "boundary_preserving_uniformizer_scalar_gauge_space_materialized": True,
            "constant_only_exceptional_squareclass_linear_system_solved": True,
            "nonconstant_exceptional_obstruction_support_isolated": True,
            "source_bound_nonconstant_cech_correction_space_materialized": False,
            "corrected_global_representative_materialized": False,
            "exceptional_residue_cancellation_verified": False,
            "all_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "next_missing_object": "SOURCE_BOUND_NONCONSTANT_COVER_OR_CECH_CORRECTION_CAPABLE_OF_CHANGING_THE_EXCEPTIONAL_P1_FUNCTION_FIELD_FACTOR_CLASSES_AT_EXC_003_EXC_004_EXC_011_EXC_012_WITHOUT_BREAKING_THE_EIGHT_A2_02_BOUNDARY_RESIDUES",
        "next_exact_leaf": "V91C1X_R5B3B3C4B1C_NONCONSTANT_EXCEPTIONAL_CORRECTION_SPACE_PREFLIGHT",
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "credit_firewall": {
            "authority_promotion": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "hostile_audit_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        if not OUT.exists():
            raise SystemExit("materialized C4B1B artifact is missing")
        current = json.loads(OUT.read_text(encoding="utf-8"))
        if current != cert:
            raise SystemExit("materialized C4B1B artifact is stale")
    system = cert["constant_scalar_squareclass_system"]
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B3C4B1B_UNIFORMIZER_SCALAR_GAUGE_EXACT",
        "canonical_sha256": cert["canonical_sha256"],
        "constant_only_obstruction_count": 27,
        "nonconstant_obstruction_count": 4,
        "incidence_rank_f2": system["incidence_matrix_rank_f2"],
        "constant_system_consistent": system["consistent_in_Qi_squareclass_group"],
        "all_27_adjusted_constant_residues_square_trivial": system["all_27_adjusted_constant_residues_square_trivial"],
        "next_exact_leaf": cert["next_exact_leaf"],
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
