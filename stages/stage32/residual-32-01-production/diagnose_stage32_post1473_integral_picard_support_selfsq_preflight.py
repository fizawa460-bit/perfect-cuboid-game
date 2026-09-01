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
PRIOR_V7_ARTIFACT_CANONICAL_SHA256 = "027d524953ce645b058c812a42e84986c2af03f489318c83e15922251e6602f0"
PRIOR_DIVISOR_EFFECTIVITY_AUDIT_CANONICAL_SHA256 = "570034738f8f7de6238a42888e3d54a1ebd7e5a477e75f3aecb0e27986906489"
PICARD_RANK = 64
K_SQUARE = 16
P_G = 7
Q = 0
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


def load_locked_json(path: Path, expected: str, label: str) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.get("canonical_sha256_without_this_field")
    body = dict(raw)
    body.pop("canonical_sha256_without_this_field", None)
    if claimed != expected or v5.csha(body) != claimed:
        raise ValueError(f"{label} canonical regression")
    return raw


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

    stages_dir = Path(__file__).resolve().parents[2]
    source_lock_path = stages_dir / "stage29" / "29-02a" / "source-lock.md"
    source_lock = source_lock_path.read_text()
    required_source_strings = (
        "K^2=16",
        "p_g=7",
        "q=0",
        "canonical divisor big and nef",
        "SOURCE_AUDIT=PASS",
    )
    missing = [value for value in required_source_strings if value not in source_lock]
    if missing:
        raise ValueError(f"Testa-Stoll surface-invariant source-lock regression: {missing}")

    prior_audit_path = Path(__file__).resolve().parents[1] / "32-21" / "post-21bl-divisor-effectivity-audit.json"
    prior_audit = load_locked_json(
        prior_audit_path,
        PRIOR_DIVISOR_EFFECTIVITY_AUDIT_CANONICAL_SHA256,
        "prior divisor-effectivity audit",
    )
    prior = prior_audit["independent_recomputation"]
    if (prior.get("K_square"), prior.get("p_g"), prior.get("q"), prior.get("chi_O")) != (16, 7, 0, 8):
        raise ValueError("audited surface-invariant tuple regression")

    # Reuse the exact V6 candidate search/replay unchanged; enrich only the
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
        divisor_effective = False
        chi_C = None
        h0_lower = None
        arithmetic_genus = None
        genus_defect = None
    else:
        selfsq = int(witness["self_intersection"])
        lower = int(witness["project_native_self_intersection_lower_bound"])
        combined_sat = bool(witness["passes_project_native_self_intersection_lower_bound"])
        probe_status = (
            "SAT_SAME_EXACT_WITNESS_SUPPORT_AND_SELF_INTERSECTION"
            if combined_sat
            else "SUPPORT_WITNESS_FAILS_SELF_INTERSECTION_FIXED_Z_COMBINED_FEASIBILITY_OPEN"
        )

        degree = int(EXPECTED_TARGET["degree"])
        genus = int(EXPECTED_TARGET["genus"])
        chi_O = 1 - Q + P_G
        if (selfsq - degree) % 2:
            raise ValueError("Riemann-Roch parity regression on V8 witness")
        chi_C = chi_O + (selfsq - degree) // 2
        K_dot_K_minus_C = K_SQUARE - degree
        if K_dot_K_minus_C >= 0:
            raise ValueError("expected K.(K-C)<0 on V8 witness")
        # K is nef by the audited Stage29 source lock. If K-C were effective,
        # nefness would give K.(K-C)>=0, contradicting -170. Hence h2(C)=0.
        h0_lower = chi_C
        divisor_effective = h0_lower > 0
        if not divisor_effective:
            raise ValueError("Riemann-Roch lower bound failed to prove divisor effectivity")
        if (selfsq + degree) % 2:
            raise ValueError("adjunction parity regression on V8 witness")
        arithmetic_genus = (selfsq + degree) // 2 + 1
        genus_defect = arithmetic_genus - genus

    payload["schema"] = "STAGE32_POST1473_INTEGRAL_PICARD_SUPPORT_SELFSQ_DIVISOR_EFFECTIVITY_PREFLIGHT_V8"
    payload["leaf"] = "POST1473_FIXED_Z_SUPPORT_SELFSQ_AND_DIVISOR_EFFECTIVITY"
    payload["mode"] = (
        "V6_NUMERICAL_CANDIDATE_PLUS_EXACT_Z3_PICARD_REPLAY_EXACT_RETAINED_GRAM_SELF_INTERSECTION_AND_AUDITED_RIEMANN_ROCH_DIVISOR_EFFECTIVITY"
    )
    payload["source_locks"]["prior_v6_artifact_canonical_sha256"] = PRIOR_V6_ARTIFACT_CANONICAL_SHA256
    payload["source_locks"]["prior_v7_artifact_canonical_sha256"] = PRIOR_V7_ARTIFACT_CANONICAL_SHA256
    payload["source_locks"]["v6_intermediate_replay_canonical_sha256"] = v6_intermediate_canonical
    payload["source_locks"]["prior_divisor_effectivity_audit_canonical_sha256"] = PRIOR_DIVISOR_EFFECTIVITY_AUDIT_CANONICAL_SHA256
    payload["source_locks"]["surface_invariant_source_lock"] = "stages/stage29/29-02a/source-lock.md"
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
    payload["divisor_effectivity_probe"] = {
        "status": "PASS_EXACT_RIEMANN_ROCH_EFFECTIVE_DIVISOR" if divisor_effective else "NOT_REACHED",
        "surface_invariants": {"K_square": K_SQUARE, "p_g": P_G, "q": Q, "chi_O": 1 - Q + P_G, "K_nef": True},
        "K_dot_C": int(EXPECTED_TARGET["degree"]),
        "C_square": selfsq,
        "chi_O_C": chi_C,
        "K_dot_K_minus_C": K_SQUARE - int(EXPECTED_TARGET["degree"]),
        "K_nef_excludes_effective_K_minus_C": bool(divisor_effective),
        "h2_O_C": 0 if divisor_effective else None,
        "h0_lower_bound": h0_lower,
        "effective_divisor_exists_in_class_C": divisor_effective,
        "arithmetic_genus": arithmetic_genus,
        "target_normalization_genus": int(EXPECTED_TARGET["genus"]),
        "required_total_normalization_genus_defect_if_integral": genus_defect,
        "effective_divisor_is_not_integral_irreducible_curve": True,
        "effective_divisor_is_not_normalization_genus1": True,
    }
    payload["firewalls"]["fixed_z_support_plus_self_intersection_sat"] = combined_sat
    payload["firewalls"]["fixed_z_support_plus_self_intersection_unsat"] = False
    payload["firewalls"]["effective_divisor_exists_for_exact_witness"] = divisor_effective
    payload["firewalls"]["integral_picard_class_is_not_effective_curve"] = True
    payload["firewalls"]["effective_divisor_is_not_integral_irreducible_low_genus_curve"] = True
    payload["canonical_sha256_without_this_field"] = v5.csha(payload)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print(
        json.dumps(
            {
                "verdict": "PASS_STAGE32_POST1473_SUPPORT_SELFSQ_DIVISOR_EFFECTIVITY_PREFLIGHT",
                "probe_status": probe_status,
                "witness_self_intersection": selfsq,
                "project_native_lower_bound": lower,
                "combined_sat": combined_sat,
                "effective_divisor_exists": divisor_effective,
                "h0_lower_bound": h0_lower,
                "arithmetic_genus": arithmetic_genus,
                "required_genus_defect": genus_defect,
                "canonical_sha256": payload["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
