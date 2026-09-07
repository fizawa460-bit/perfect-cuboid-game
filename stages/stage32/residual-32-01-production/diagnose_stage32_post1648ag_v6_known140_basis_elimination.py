#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from sympy import Matrix, eye
from z3 import Int, Solver, Sum, sat

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
STAGE33_07 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
OUT = HERE / "post1648ag-v6-known140-basis-elimination.json"

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


def int_row(m: Matrix) -> list[int]:
    assert m.rows == 1
    out = []
    for x in m:
        if getattr(x, "q", 1) != 1:
            raise ValueError(f"nonintegral coordinate {x}")
        out.append(int(x))
    return out


def exact_complete_solution(
    coords: Matrix,
    vcoords: list[int],
    basis_indices: list[int],
    nonbasis_indices: list[int],
    nonbasis_coeffs: list[int],
) -> list[int]:
    if len(nonbasis_coeffs) != len(nonbasis_indices) or any(x < 0 for x in nonbasis_coeffs):
        raise ValueError("invalid nonbasis coefficient vector")
    contribution = [
        sum(nonbasis_coeffs[k] * int(coords[i, j]) for k, i in enumerate(nonbasis_indices))
        for j in range(64)
    ]
    residual = [vcoords[j] - contribution[j] for j in range(64)]
    if any(x < 0 for x in residual):
        raise ValueError("basis-elimination residual is negative")
    coeffs = [0] * 140
    for k, i in enumerate(nonbasis_indices):
        coeffs[i] = nonbasis_coeffs[k]
    for j, i in enumerate(basis_indices):
        coeffs[i] = residual[j]
    reconstructed = [
        sum(coeffs[i] * int(coords[i, j]) for i in range(140))
        for j in range(64)
    ]
    if reconstructed != vcoords:
        raise ValueError("completed known140 decomposition does not reconstruct V6")
    return coeffs


def main() -> None:
    bundle = load_retained(STAGE33_07 / "picard_base_rows_retained.py", "s32_ag_picard")
    marking = load_retained(STAGE33_07 / "stage32_picard_marking_retained.py", "s32_ag_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    coords = adapter.class_coordinates_in_retained_basis
    if coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("retained all140/Picard64 shape regression")

    basis_indices = [j - 1 for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    if coords.extract(basis_indices, list(range(64))) != eye(64):
        raise ValueError("retained basis known curves are not the identity coordinate rows")
    basis_set = set(basis_indices)
    nonbasis_indices = [i for i in range(140) if i not in basis_set]
    if len(nonbasis_indices) != 76:
        raise ValueError("nonbasis known140 count regression")

    v6 = json.loads(V6_PATH.read_text())
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    basis_pairings = Matrix([[pairings[j - 1] for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]])
    vcoords = int_row(basis_pairings * gram.inv())
    if vcoords != [int(x) for x in v6["witness"]["picard_coordinates"]]:
        raise ValueError("V6 stored coordinates do not match retained Picard64 recovery")
    if [int(x) for x in (coords * gram * Matrix(vcoords))] != pairings:
        raise ValueError("V6 all140 pairing replay regression")

    # Exact equivalence:
    # basis rows are e_j, so n_basis_j = v_j - sum_i x_i a_ij.
    # Therefore the 140-variable equality problem with all n>=0 is equivalent
    # to 76 nonbasis integer variables x>=0 satisfying A_non^T x <= v.
    A = np.array(
        [[int(coords[i, j]) for k, i in enumerate(nonbasis_indices)] for j in range(64)],
        dtype=float,
    )
    upper = np.array(vcoords, dtype=float)
    candidate_source = None
    nonbasis_coeffs = None
    scipy_meta = {}

    scipy_result = milp(
        c=np.ones(76, dtype=float),
        integrality=np.ones(76, dtype=int),
        bounds=Bounds(np.zeros(76), np.full(76, np.inf)),
        constraints=LinearConstraint(A, np.full(64, -np.inf), upper),
        options={"time_limit": 60.0, "mip_rel_gap": 0.0, "presolve": True},
    )
    scipy_meta = {
        "success": bool(scipy_result.success),
        "status": int(scipy_result.status),
        "message": str(scipy_result.message),
        "fun": None if scipy_result.fun is None else float(scipy_result.fun),
    }
    if scipy_result.x is not None:
        trial = [int(round(float(x))) for x in scipy_result.x]
        try:
            exact_complete_solution(coords, vcoords, basis_indices, nonbasis_indices, trial)
            nonbasis_coeffs = trial
            candidate_source = "SCIPY_HIGHS_MILP_CANDIDATE_EXACTLY_REVERIFIED"
        except ValueError:
            pass

    z3_meta = {"attempted": False}
    if nonbasis_coeffs is None:
        xs = [Int(f"x{k+1}") for k in range(76)]
        solver = Solver()
        solver.set(timeout=120000, random_seed=0)
        for x in xs:
            solver.add(x >= 0)
        for j in range(64):
            solver.add(
                Sum([xs[k] * int(coords[i, j]) for k, i in enumerate(nonbasis_indices)])
                <= vcoords[j]
            )
        check = solver.check()
        z3_meta = {
            "attempted": True,
            "result": str(check),
            "reason_unknown": None if check == sat else solver.reason_unknown(),
            "timeout_ms": 120000,
        }
        if check == sat:
            model = solver.model()
            trial = [int(model.eval(x, model_completion=True).as_long()) for x in xs]
            exact_complete_solution(coords, vcoords, basis_indices, nonbasis_indices, trial)
            nonbasis_coeffs = trial
            candidate_source = "Z3_REDUCED_76VAR_EXACT_SAT"

    base = {
        "schema": "STAGE32_POST1648AG_V6_KNOWN140_BASIS_ELIMINATION_V1",
        "stage": 32,
        "leaf": "POST1648AG_V6_KNOWN140_BASIS_ELIMINATION",
        "source_locks": {
            "v6_witness_path": str(V6_PATH.relative_to(ROOT)),
            "v6_witness_blob_sha1_expected": "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
            "v6_witness_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "hperp_integral_adapter_certificate_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "all140_retained_coordinates_sha256": adapter.certificate["all140_retained_coordinates_sha256"],
            "retained_picard_gram_sha256": adapter.certificate["retained_basis_gram_sha256"],
        },
        "exact_reduction": {
            "known140_variable_count": 140,
            "retained_basis_variable_count": 64,
            "nonbasis_variable_count": 76,
            "retained_basis_rows_are_identity": True,
            "equivalence": "sum_140 n_i*C_i=V6 with n_i>=0 iff x_nonbasis>=0 and A_nonbasis^T*x<=V6_coordinates; basis coefficients are the coordinatewise residual",
            "v6_retained_picard64_coordinates": vcoords,
            "v6_all140_pairing_replay_exact": True,
        },
        "candidate_search": {
            "scipy_highs": scipy_meta,
            "z3_fallback": z3_meta,
        },
        "firewalls": {
            "floating_milp_candidate_without_exact_replay_gets_no_credit": True,
            "known140_monoid_membership_is_not_integral_irreducible_genus1_member": True,
            "effective_divisor_decomposition_is_not_distinguished_member": True,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_credit": False,
        },
    }

    if nonbasis_coeffs is None:
        base["status"] = "NO_EXACT_SAT_WITNESS_MATERIALIZED"
        base["verdict"] = "NO_RESULT"
        base["decision"] = {
            "promotable_credit": False,
            "next_exact_route": "FURTHER_CONE_COMPRESSION_OR_STANDALONE_UNSAT_CERTIFICATE",
        }
    else:
        coeffs = exact_complete_solution(
            coords, vcoords, basis_indices, nonbasis_indices, nonbasis_coeffs
        )
        reconstructed = [
            sum(coeffs[i] * int(coords[i, j]) for i in range(140))
            for j in range(64)
        ]
        if reconstructed != vcoords:
            raise ValueError("final decomposition reconstruction regression")
        replay_pairings = [int(x) for x in (coords * gram * Matrix(reconstructed))]
        if replay_pairings != pairings:
            raise ValueError("final decomposition all140 pairing replay regression")
        sparse = [
            {"known140_label_1based": i + 1, "multiplicity": coeffs[i]}
            for i in range(140) if coeffs[i]
        ]
        base["status"] = "EXACT_SAT_KNOWN140_MONOID_DECOMPOSITION"
        base["verdict"] = "PASS_STAGE32_POST1648AG_EXACT_KNOWN140_MONOID_SAT"
        base["known140_monoid"] = {
            "membership": True,
            "candidate_source": candidate_source,
            "nonzero_term_count": len(sparse),
            "total_multiplicity": sum(coeffs),
            "normal_curve_multiplicity": sum(coeffs[:92]),
            "exceptional_curve_multiplicity": sum(coeffs[92:]),
            "decomposition": sparse,
            "picard64_reconstruction_exact": True,
            "all140_pairing_reconstruction_exact": True,
            "effective_divisor_explicitly_constructed_as_known140_sum": True,
            "integral_irreducible_genus1_member_constructed": False,
        }
        base["decision"] = {
            "bounded_positive": "V6_CLASS_HAS_AN_EXPLICIT_EFFECTIVE_DIVISOR_REPRESENTATIVE_AS_A_NONNEGATIVE_INTEGER_SUM_OF_KNOWN140_CURVES",
            "member_level_gap_closed": False,
            "next_exact_route": "EXPLOIT_THE_EXPLICIT_KNOWN140_DIVISOR_TO_BUILD_A_DISTINGUISHED_SECTION_OR_ANALYZE_LINEAR_SYSTEM_COMPONENTS/DEFORMATION_TOWARD_AN_INTEGRAL_GENUS1_MEMBER",
        }

    base["canonical_sha256_without_this_field"] = csha(base)
    OUT.write_text(json.dumps(base, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": base["status"],
        "verdict": base["verdict"],
        "canonical_sha256": base["canonical_sha256_without_this_field"],
        "candidate_source": candidate_source,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
