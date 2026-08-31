#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from sympy import Matrix

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_21BL_EVIDENCE_CANONICAL = "ac88fb355252750e6afdc10cbb54abec24babbad57c25090c017f9a55ac93a44"
EXPECTED_WITNESS_SHA256 = "1a131595c87cf9c5d54ef97dba62261eeb3dda7bb92a5a9fa62c280f46bc4137"
EXPECTED_ANTI_RANK = 59
EXPECTED_PICARD_RANK = 64
EXPECTED_PAIRINGS = 140
SCHEMA = "STAGE32_POST21BL_EXACT_PICARD_WITNESS_ADAPTER_V1"


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def vector_list(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
    return [int(v[i, 0]) for i in range(v.rows)]


def sha256_json(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_21bl_evidence(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_21BL_EVIDENCE_CANONICAL or csha(raw) != claimed:
        raise ValueError("21bl evidence canonical regression")
    raw["canonical_sha256_without_this_field"] = claimed
    if raw.get("result", {}).get("status") != "SAT":
        raise ValueError("21bl evidence is not SAT")
    witness = raw["result"].get("witness_r_reduced")
    if not isinstance(witness, list) or len(witness) != EXPECTED_ANTI_RANK:
        raise ValueError("21bl witness rank regression")
    if raw["result"].get("witness_sha256") != EXPECTED_WITNESS_SHA256:
        raise ValueError("21bl witness SHA regression")
    return raw


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    evidence = load_21bl_evidence(args.evidence)
    bundle = load_retained(args.retained, "s32_post21bl_picard")
    marking = load_retained(args.marking, "s32_post21bl_marking")
    data = reconstruct_translation_data(marking, bundle)

    target = evidence["target"]
    genus, degree = parse_row_id(str(target["row_id"]))
    exceptional_total = int(target["e"])
    first_normal_half_total = int(target["a"])
    z = Matrix([int(v) for v in target["z"]])
    r = Matrix([int(v) for v in evidence["result"]["witness_r_reduced"]])

    if z.shape != (5, 1):
        raise ValueError(f"fixed projection z shape regression: {z.shape}")
    if r.shape != (EXPECTED_ANTI_RANK, 1):
        raise ValueError(f"reduced witness shape regression: {r.shape}")

    # Rebuild exactly the same unimodular reduced anti-fixed basis used by 21bl.
    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    selected_M = M.extract(list(pivots), list(range(EXPECTED_ANTI_RANK)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform reconstruction regression")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("21bl reduced-coordinate transform is not unimodular")
    Mred = M * U

    x0 = data["x0_map"] * z
    q = data["K"] * U * r
    x = x0 + q
    if x.shape != (EXPECTED_PICARD_RANK, 1):
        raise ValueError("Picard reconstruction rank regression")

    # Exact fixed-projection replay.  C*x=z is the affine-fiber identity and
    # N*x=B*z is the Reynolds-numerator identity behind the representative leaf.
    fixed_coords = data["C"] * x
    fixed_projection_exact = fixed_coords == z
    reynolds_exact = data["N"] * x == data["B"] * z
    anti_fixed_exact = data["C"] * q == Matrix.zeros(5, 1)

    adapter = data["adapter"]
    bridge = data["bridge"]
    gram = Matrix(bundle["picard_gram_64x64"])
    pairings = adapter.pairing_matrix * x
    if pairings.shape != (EXPECTED_PAIRINGS, 1):
        raise ValueError("all140 pairing shape regression")

    # Independent replay of the linear form used by the 21bl solver.
    y0 = data["pairing_x0_map"] * z
    pairings_from_reduced = y0 + Mred * r
    pairing_model_replay_exact = pairings == pairings_from_reduced

    pairing_values = vector_list(pairings)
    all_pairings_integral = all(isinstance(v, int) for v in pairing_values)
    all_pairings_nonnegative = min(pairing_values) >= 0

    orbit_sums = []
    orbit_nonnegative = []
    for orbit in data["orbits"]:
        vals = [pairing_values[int(i)] for i in orbit]
        orbit_sums.append(sum(vals))
        orbit_nonnegative.append(min(vals) >= 0)
    expected_orbit_sums = [sum(int(y0[int(i), 0]) for i in orbit) for orbit in data["orbits"]]
    orbit_sums_exact = orbit_sums == expected_orbit_sums

    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])
    slice_values = vector_list(phi * x)
    expected_slice = [degree, exceptional_total, first_normal_half_total]
    slice_exact = slice_values == expected_slice
    target_image_exact = bridge.target_in_image(*expected_slice)

    self_square = int((x.T * gram * x)[0])
    fixed_square = int((x0.T * gram * x0)[0])
    anti_fixed_square = int((q.T * gram * q)[0])
    orthogonal_split_exact = int((x0.T * gram * q)[0]) == 0 and self_square == fixed_square + anti_fixed_square
    required_lower = -degree - 2 + 2 * genus
    self_square_pass = self_square >= required_lower

    exact_reconstruction_pass = all([
        fixed_projection_exact,
        reynolds_exact,
        anti_fixed_exact,
        pairing_model_replay_exact,
        all_pairings_integral,
        all_pairings_nonnegative,
        orbit_sums_exact,
        slice_exact,
        target_image_exact,
        orthogonal_split_exact,
    ])

    if not exact_reconstruction_pass:
        status = "FAIL_POST21BL_EXACT_PICARD_RECONSTRUCTION"
    elif self_square_pass:
        status = "PASS_POST21BL_EXACT_PICARD64_SLICE_WITNESS"
    else:
        status = "PASS_RECONSTRUCTION_BUT_WITNESS_FAILS_ORIGINAL_SELF_INTERSECTION_THRESHOLD"

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "mode": "EXACT_21BL_REDUCED_INTEGER_WITNESS_TO_ORIGINAL_RETAINED_PICARD64_ADAPTER",
        "status": status,
        "source": {
            "21bl_evidence_canonical_sha256": EXPECTED_21BL_EVIDENCE_CANONICAL,
            "21bl_witness_sha256": EXPECTED_WITNESS_SHA256,
            "retained_bundle_sha256": bundle["canonical_sha256"],
            "adapter_certificate_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "bridge_certificate_sha256": bridge.certificate["canonical_sha256_without_this_field"],
        },
        "target": {
            "row_id": target["row_id"],
            "genus": genus,
            "degree": degree,
            "e": exceptional_total,
            "a": first_normal_half_total,
            "u": int(target["u"]),
            "v": int(target["v"]),
            "z": vector_list(z),
            "ordinal": int(evidence["ordinal"]),
            "triple": [int(v) for v in evidence["triple"]],
        },
        "reconstruction": {
            "picard_rank": EXPECTED_PICARD_RANK,
            "anti_fixed_rank": EXPECTED_ANTI_RANK,
            "reduced_transform_unimodular": True,
            "picard_coordinates": vector_list(x),
            "picard_coordinates_sha256": sha256_json(vector_list(x)),
            "anti_fixed_coordinates_in_picard_basis": vector_list(q),
            "fixed_projection_coordinates_replayed": vector_list(fixed_coords),
            "fixed_projection_exact": fixed_projection_exact,
            "reynolds_numerator_exact": reynolds_exact,
            "anti_fixed_kernel_exact": anti_fixed_exact,
        },
        "all140": {
            "pairing_count": len(pairing_values),
            "pairings": pairing_values,
            "pairings_sha256": sha256_json(pairing_values),
            "pairing_model_replay_exact": pairing_model_replay_exact,
            "all_pairings_integral": all_pairings_integral,
            "all_pairings_nonnegative": all_pairings_nonnegative,
            "minimum_pairing": min(pairing_values),
            "maximum_pairing": max(pairing_values),
            "zero_pairing_count": sum(1 for v in pairing_values if v == 0),
            "orbit_sums": orbit_sums,
            "expected_orbit_sums": expected_orbit_sums,
            "orbit_sums_exact": orbit_sums_exact,
            "all_orbits_nonnegative": all(orbit_nonnegative),
        },
        "slice": {
            "actual_d_e_a": slice_values,
            "expected_d_e_a": expected_slice,
            "slice_exact": slice_exact,
            "target_image_exact": target_image_exact,
        },
        "quadratic": {
            "picard_self_square": self_square,
            "fixed_part_self_square": fixed_square,
            "anti_fixed_part_self_square": anti_fixed_square,
            "fixed_antifixed_orthogonal_split_exact": orthogonal_split_exact,
            "required_lower_formula": "-d-2+2g",
            "required_lower": required_lower,
            "self_square_meets_original_threshold": self_square_pass,
            "slack": self_square - required_lower,
        },
        "interpretation": {
            "exact_reconstruction_pass": exact_reconstruction_pass,
            "if_status_pass_exact_picard64_slice_witness_then_this_is_one_exact_integral_picard_class_for_the_representative_slice": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
            "picard_class_is_not_effective_curve_existence": True,
            "receiver_credit": False,
            "theorem_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": status,
        "self_square": self_square,
        "required_lower": required_lower,
        "slack": self_square - required_lower,
        "minimum_pairing": min(pairing_values),
        "zero_pairing_count": payload["all140"]["zero_pairing_count"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))

    if status == "FAIL_POST21BL_EXACT_PICARD_RECONSTRUCTION":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
