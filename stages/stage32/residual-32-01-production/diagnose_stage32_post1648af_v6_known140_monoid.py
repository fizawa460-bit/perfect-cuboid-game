#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix
from z3 import Int, Solver, Sum, sat, unsat, unknown, get_version_string

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
STAGE33_07 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
OUT = HERE / "post1648af-v6-known140-monoid-preflight.json"

sys.path.insert(0, str(HERE))
from hperp_integral_adapter import (  # noqa: E402
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def row_list(m: Matrix) -> list[int]:
    assert m.rows == 1
    out = []
    for value in m:
        if getattr(value, "q", 1) != 1:
            raise ValueError(f"nonintegral coordinate: {value}")
        out.append(int(value))
    return out


def main() -> None:
    bundle = load_retained(STAGE33_07 / "picard_base_rows_retained.py", "s32_af_picard")
    marking = load_retained(STAGE33_07 / "stage32_picard_marking_retained.py", "s32_af_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    coords = adapter.class_coordinates_in_retained_basis
    if coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("retained all140/Picard64 shape regression")

    v6 = json.loads(V6_PATH.read_text())
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(pairings) != 140:
        raise ValueError("V6 all140 pairing count regression")
    basis_pairings = Matrix([[pairings[j - 1] for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]])
    vcoords_q = basis_pairings * gram.inv()
    vcoords = row_list(vcoords_q)

    # Independent exact replay: the reconstructed class must reproduce all 140
    # V6 pairings, not merely the 64 basis pairings used to recover it.
    replay = coords * gram * Matrix(vcoords)
    replay_pairings = [int(replay[i, 0]) for i in range(140)]
    if replay_pairings != pairings:
        raise ValueError("V6 retained Picard64 recovery does not reproduce all140 pairings")

    ns = [Int(f"n{i+1}") for i in range(140)]
    solver = Solver()
    solver.set(timeout=180000, random_seed=0)
    for n in ns:
        solver.add(n >= 0)
    for j in range(64):
        solver.add(Sum([ns[i] * int(coords[i, j]) for i in range(140)]) == vcoords[j])

    check = solver.check()
    base = {
        "schema": "STAGE32_POST1648AF_V6_KNOWN140_MONOID_PREFLIGHT_V1",
        "stage": 32,
        "leaf": "POST1648AF_V6_KNOWN140_MONOID_PREFLIGHT",
        "source_locks": {
            "v6_witness_path": str(V6_PATH.relative_to(ROOT)),
            "v6_witness_blob_sha1_expected": "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
            "v6_witness_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "hperp_integral_adapter_certificate_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "retained_picard_basis_known_labels_1based": list(RETAINED_BASIS_KNOWN_LABELS_1BASED),
            "retained_picard_gram_sha256": adapter.certificate["retained_basis_gram_sha256"],
            "all140_retained_coordinates_sha256": adapter.certificate["all140_retained_coordinates_sha256"],
        },
        "v6_recovery": {
            "all140_pairings_sha256": v6["witness"]["all140_pairings_sha256"],
            "retained_picard64_coordinates": vcoords,
            "retained_picard64_coordinates_sha256": csha(vcoords),
            "all140_pairing_replay_exact": True,
            "stored_post1473_picard_coordinates_match_this_retained_basis": vcoords == [int(x) for x in v6["witness"]["picard_coordinates"]],
        },
        "solver": {
            "engine": "z3 QF_LIA",
            "z3_version": get_version_string(),
            "timeout_ms": 180000,
            "random_seed": 0,
            "result": str(check),
        },
        "firewalls": {
            "known140_monoid_membership_is_not_integral_irreducible_genus1_member": True,
            "effective_divisor_decomposition_is_not_distinguished_member": True,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_credit": False,
        },
    }

    if check == sat:
        model = solver.model()
        coeffs = [int(model.eval(n, model_completion=True).as_long()) for n in ns]
        if any(n < 0 for n in coeffs):
            raise ValueError("negative coefficient in SAT model")
        reconstructed = [
            sum(coeffs[i] * int(coords[i, j]) for i in range(140))
            for j in range(64)
        ]
        if reconstructed != vcoords:
            raise ValueError("SAT decomposition fails exact Picard64 reconstruction")
        sparse = [
            {"known140_label_1based": i + 1, "multiplicity": coeffs[i]}
            for i in range(140) if coeffs[i]
        ]
        recon_pairings = [
            sum(coeffs[i] * int((coords * gram)[i, j]) for i in range(140))
            for j in range(64)
        ]
        if recon_pairings != [pairings[j - 1] for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]:
            raise ValueError("SAT decomposition fails retained-basis pairing replay")
        base["status"] = "EXACT_SAT_KNOWN140_MONOID_DECOMPOSITION"
        base["verdict"] = "PASS_STAGE32_POST1648AF_EXACT_KNOWN140_MONOID_SAT"
        base["known140_monoid"] = {
            "membership": True,
            "nonzero_term_count": len(sparse),
            "total_multiplicity": sum(coeffs),
            "normal_curve_multiplicity": sum(coeffs[:92]),
            "exceptional_curve_multiplicity": sum(coeffs[92:]),
            "decomposition": sparse,
            "picard64_reconstruction_exact": True,
            "retained_basis_pairing_reconstruction_exact": True,
            "effective_divisor_explicitly_constructed_as_known140_sum": True,
            "integral_irreducible_genus1_member_constructed": False,
        }
        base["decision"] = {
            "bounded_positive": "V6_CLASS_HAS_AN_EXPLICIT_EFFECTIVE_DIVISOR_REPRESENTATIVE_AS_A_NONNEGATIVE_INTEGER_SUM_OF_KNOWN140_CURVES",
            "member_level_gap_closed": False,
            "next_exact_route": "ANALYZE_THE_EXPLICIT_REDUCIBLE_KNOWN140_DIVISOR_AND_OR_USE_IT_TO_BUILD_A_DISTINGUISHED_SECTION_OR_DEFORM_TO_AN_INTEGRAL_GENUS1_MEMBER",
        }
    elif check == unsat:
        base["status"] = "Z3_EXACT_UNSAT_WITHOUT_INDEPENDENT_STANDALONE_INTEGER_CERTIFICATE"
        base["verdict"] = "BOUNDED_DIAGNOSTIC_ONLY_KNOWN140_MONOID_UNSAT_NOT_PROMOTED"
        base["known140_monoid"] = {
            "membership": False,
            "solver_unsat": True,
            "standalone_exact_unsat_certificate_materialized": False,
            "effectivity_outside_known140_not_excluded": True,
        }
        base["decision"] = {
            "bounded_negative": "NO_Z3_INTEGER_SOLUTION_IN_KNOWN140_MONOID_UNDER_EXACT_RETAINED_PICARD64_EQUATIONS",
            "promotable_credit": False,
            "next_exact_route": "MATERIALIZE_A_STANDALONE_MODULAR_OR_SEPARATING_UNSAT_CERTIFICATE_BEFORE_ANY_BOUNDED_NEGATIVE_PROMOTION",
        }
    else:
        base["status"] = "SOLVER_UNKNOWN_OR_TIMEOUT"
        base["verdict"] = "NO_RESULT"
        base["decision"] = {
            "reason_unknown": solver.reason_unknown(),
            "promotable_credit": False,
            "next_exact_route": "COMPRESS_OR_DECOMPOSE_THE_MONOID_FEASIBILITY_PROBLEM",
        }

    base["canonical_sha256_without_this_field"] = csha(base)
    OUT.write_text(json.dumps(base, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": base["status"],
        "verdict": base["verdict"],
        "canonical_sha256": base["canonical_sha256_without_this_field"],
        "output": str(OUT.relative_to(ROOT)),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
