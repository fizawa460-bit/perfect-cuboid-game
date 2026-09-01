#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy
from sympy import Matrix

import diagnose_stage32_post1473_integral_picard_support_milp_candidate_preflight as v6
import diagnose_stage32_post1473_integral_picard_support_reduced_lia_preflight as v5
from diagnose_stage32_post1473_integral_picard_support_preflight import EXPECTED_TARGET

PRIOR_V6_ARTIFACT_CANONICAL_SHA256 = "76730cd865b4e63791c185636e49202e6e8a4a7e33cf4686d2ac038a3c036417"
PICARD_RANK = 64
_ORIGINAL_RECONSTRUCT_WITNESS = v5.reconstruct_witness
_GRAM: Matrix | None = None
_GRAM_SHA256: str | None = None


def matrix_payload(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def arg_path(flag: str) -> Path:
    try:
        i = sys.argv.index(flag)
        value = sys.argv[i + 1]
    except (ValueError, IndexError) as exc:
        raise ValueError(f"missing required wrapper argument {flag}") from exc
    return Path(value)


def reconstruct_witness_with_self_intersection(**kwargs) -> dict:
    if _GRAM is None or _GRAM_SHA256 is None:
        raise RuntimeError("retained Picard Gram not initialized")
    witness = _ORIGINAL_RECONSTRUCT_WITNESS(**kwargs)

    data = kwargs["data"]
    z = tuple(int(v) for v in kwargs["z"])
    U = kwargs["U"]
    rvars = kwargs["rvars"]
    model = kwargs["model"]

    rv = Matrix([int(model.eval(v, model_completion=True).as_long()) for v in rvars])
    original_t = U * rv
    picard = data["x0_map"] * Matrix(z) + data["K"] * original_t
    picard_coordinates = [int(v) for v in picard]
    if v5.csha(picard_coordinates) != witness["picard_coordinates_sha256"]:
        raise ValueError("self-intersection Picard reconstruction hash regression")

    raw_selfsq = (picard.T * _GRAM * picard)[0, 0]
    if sympy.denom(raw_selfsq) != 1:
        raise ValueError("Picard self-intersection became nonintegral")
    selfsq = int(raw_selfsq)
    lower = -int(EXPECTED_TARGET["degree"]) - 2 + 2 * int(EXPECTED_TARGET["genus"])

    witness["retained_picard_gram_sha256"] = _GRAM_SHA256
    witness["self_intersection"] = selfsq
    witness["project_native_self_intersection_lower_bound"] = lower
    witness["passes_project_native_self_intersection_lower_bound"] = selfsq >= lower
    return witness


def main() -> None:
    global _GRAM, _GRAM_SHA256

    retained_path = arg_path("--retained")
    output_path = arg_path("--output")
    bundle = v5.load_module_payload(retained_path, "stage32_post1473_support_selfsq_picard")
    gram = Matrix(bundle["picard_gram_64x64"])
    if gram.shape != (PICARD_RANK, PICARD_RANK) or gram != gram.T:
        raise ValueError("retained Picard Gram shape/symmetry regression")
    _GRAM = gram
    _GRAM_SHA256 = v5.csha(matrix_payload(gram))

    # Reuse the exact V6 candidate search/replay unchanged; only enrich the
    # exact reconstructed witness before V6 serializes it.
    v5.reconstruct_witness = reconstruct_witness_with_self_intersection
    v6.main()

    payload = json.loads(output_path.read_text())
    v6_intermediate_canonical = payload.pop("canonical_sha256_without_this_field")
    witness = payload.get("exact_replay", {}).get("witness")
    if payload.get("exact_replay", {}).get("status") != "SAT" or not isinstance(witness, dict):
        probe_status = "UNKNOWN_NO_EXACT_SUPPORT_WITNESS"
        combined_sat = False
        selfsq = None
        lower = -int(EXPECTED_TARGET["degree"]) - 2 + 2 * int(EXPECTED_TARGET["genus"])
    else:
        selfsq = int(witness["self_intersection"])
        lower = int(witness["project_native_self_intersection_lower_bound"])
        combined_sat = bool(witness["passes_project_native_self_intersection_lower_bound"])
        probe_status = (
            "SAT_SAME_EXACT_WITNESS_SUPPORT_AND_SELF_INTERSECTION"
            if combined_sat
            else "SUPPORT_WITNESS_FAILS_SELF_INTERSECTION_FIXED_Z_COMBINED_FEASIBILITY_OPEN"
        )

    payload["schema"] = "STAGE32_POST1473_INTEGRAL_PICARD_SUPPORT_SELFSQ_PREFLIGHT_V7"
    payload["leaf"] = "POST1473_FIXED_Z_SUPPORT_PLUS_PROJECT_NATIVE_SELF_INTERSECTION"
    payload["mode"] = (
        "V6_NUMERICAL_CANDIDATE_PLUS_EXACT_Z3_PICARD_REPLAY_AND_EXACT_RETAINED_GRAM_SELF_INTERSECTION"
    )
    payload["source_locks"]["prior_v6_artifact_canonical_sha256"] = PRIOR_V6_ARTIFACT_CANONICAL_SHA256
    payload["source_locks"]["v6_intermediate_replay_canonical_sha256"] = v6_intermediate_canonical
    payload["self_intersection_probe"] = {
        "status": probe_status,
        "formula": "x^2 = x^T * picard_gram_64x64 * x",
        "arithmetic": "exact integer SymPy Matrix arithmetic",
        "project_native_lower_formula": "-d-2+2g",
        "project_native_lower_bound": lower,
        "witness_self_intersection": selfsq,
        "same_exact_witness_satisfies_support_ge_47_and_self_intersection": combined_sat,
        "failure_of_this_one_witness_would_not_authorize_unsat": True,
    }
    payload["firewalls"]["fixed_z_support_plus_self_intersection_sat"] = combined_sat
    payload["firewalls"]["fixed_z_support_plus_self_intersection_unsat"] = False
    payload["firewalls"]["integral_picard_class_is_not_effective_curve"] = True
    payload["canonical_sha256_without_this_field"] = v5.csha(payload)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print(
        json.dumps(
            {
                "verdict": "PASS_STAGE32_POST1473_SUPPORT_SELFSQ_PREFLIGHT",
                "probe_status": probe_status,
                "witness_self_intersection": selfsq,
                "project_native_lower_bound": lower,
                "combined_sat": combined_sat,
                "canonical_sha256": payload["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
