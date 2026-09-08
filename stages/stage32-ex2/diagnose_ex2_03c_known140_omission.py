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

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "stages" / "stage32" / "residual-32-01-production"
STAGE33_07 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
AG_PATH = HERE / "post1648ag-v6-known140-basis-elimination.json"
EX2_02 = ROOT / "stages" / "stage32-ex2" / "EX2-02" / "exact-fixed-component-extraction.json"
ZERO_LABELS = [17, 21, 24, 25, 30, 31, 98]

sys.path.insert(0, str(HERE))
from hperp_integral_adapter import (  # noqa: E402
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)

EXPECTED_BLOBS = {
    V6_PATH: "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    AG_PATH: "e0bbe443919d1ec5424bffa84c1c5a79befbdf1e",
    EX2_02: "b07fd12a40acbfc478cdab472157cb4a34efe39c",
}


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob(path: Path) -> str:
    import subprocess
    return subprocess.check_output(
        ["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True
    ).strip()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def int_row(m: Matrix) -> list[int]:
    assert m.rows == 1
    out: list[int] = []
    for x in m:
        if getattr(x, "q", 1) != 1:
            raise ValueError(f"nonintegral coordinate {x}")
        out.append(int(x))
    return out


def complete_exact(
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
        raise ValueError("negative basis residual")
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
        raise ValueError("exact V6 reconstruction failed")
    return coeffs


def solve_one(
    zero_label: int,
    coords: Matrix,
    gram: Matrix,
    vcoords: list[int],
    pairings: list[int],
    basis_indices: list[int],
    nonbasis_indices: list[int],
) -> dict:
    zidx = zero_label - 1
    non_pos = {i: k for k, i in enumerate(nonbasis_indices)}
    basis_pos = {i: j for j, i in enumerate(basis_indices)}

    A = np.array(
        [[int(coords[i, j]) for i in nonbasis_indices] for j in range(64)],
        dtype=float,
    )
    lower = np.full(64, -np.inf)
    upper = np.array(vcoords, dtype=float)
    lb = np.zeros(len(nonbasis_indices))
    ub = np.full(len(nonbasis_indices), np.inf)
    constraint_mode: str
    if zidx in non_pos:
        ub[non_pos[zidx]] = 0.0
        constraint_mode = "NONBASIS_VARIABLE_FIXED_ZERO"
    elif zidx in basis_pos:
        j = basis_pos[zidx]
        lower[j] = float(vcoords[j])
        upper[j] = float(vcoords[j])
        constraint_mode = "BASIS_RESIDUAL_FIXED_ZERO_EXACT_EQUALITY"
    else:
        raise AssertionError("zero label is neither basis nor nonbasis")

    scipy_result = milp(
        c=np.ones(len(nonbasis_indices), dtype=float),
        integrality=np.ones(len(nonbasis_indices), dtype=int),
        bounds=Bounds(lb, ub),
        constraints=LinearConstraint(A, lower, upper),
        options={"time_limit": 30.0, "mip_rel_gap": 0.0, "presolve": True},
    )
    scipy_meta = {
        "success": bool(scipy_result.success),
        "status": int(scipy_result.status),
        "message": str(scipy_result.message),
        "fun": None if scipy_result.fun is None else float(scipy_result.fun),
    }

    candidate: list[int] | None = None
    candidate_source: str | None = None
    if scipy_result.x is not None:
        trial = [int(round(float(x))) for x in scipy_result.x]
        try:
            coeffs = complete_exact(coords, vcoords, basis_indices, nonbasis_indices, trial)
            if coeffs[zidx] != 0:
                raise ValueError("omitted coefficient is nonzero")
            candidate = coeffs
            candidate_source = "SCIPY_HIGHS_MILP_CANDIDATE_EXACTLY_REVERIFIED"
        except ValueError:
            pass

    z3_meta: dict = {"attempted": False}
    if candidate is None:
        xs = [Int(f"z{zero_label}_x{k+1}") for k in range(len(nonbasis_indices))]
        solver = Solver()
        solver.set(timeout=30000, random_seed=0)
        for x in xs:
            solver.add(x >= 0)
        if zidx in non_pos:
            solver.add(xs[non_pos[zidx]] == 0)
        for j in range(64):
            expr = Sum([xs[k] * int(coords[i, j]) for k, i in enumerate(nonbasis_indices)])
            if zidx in basis_pos and basis_pos[zidx] == j:
                solver.add(expr == vcoords[j])
            else:
                solver.add(expr <= vcoords[j])
        check = solver.check()
        z3_meta = {
            "attempted": True,
            "result": str(check),
            "reason_unknown": None if check == sat else solver.reason_unknown(),
            "timeout_ms": 30000,
        }
        if check == sat:
            model = solver.model()
            trial = [int(model.eval(x, model_completion=True).as_long()) for x in xs]
            coeffs = complete_exact(coords, vcoords, basis_indices, nonbasis_indices, trial)
            if coeffs[zidx] != 0:
                raise ValueError("z3 omitted coefficient is nonzero")
            candidate = coeffs
            candidate_source = "Z3_REDUCED_76VAR_EXACT_SAT"

    out = {
        "zero_label_1based": zero_label,
        "constraint_mode": constraint_mode,
        "scipy_highs": scipy_meta,
        "z3_fallback": z3_meta,
        "exact_feasible_witness_materialized": candidate is not None,
        "candidate_source": candidate_source,
    }
    if candidate is None:
        out["bounded_result"] = "NO_EXACT_WITNESS_MATERIALIZED_NO_UNSAT_CREDIT"
        return out

    reconstructed = [
        sum(candidate[i] * int(coords[i, j]) for i in range(140))
        for j in range(64)
    ]
    replay_pairings = [int(x) for x in (coords * gram * Matrix(reconstructed))]
    if replay_pairings != pairings:
        raise ValueError("all140 pairing replay failed")
    sparse = [
        {"known140_label_1based": i + 1, "multiplicity": candidate[i]}
        for i in range(140) if candidate[i]
    ]
    if any(row["known140_label_1based"] == zero_label for row in sparse):
        raise ValueError("omitted label appears in sparse witness")
    out.update({
        "bounded_result": "EXACT_EFFECTIVE_V6_DIVISOR_OMITTING_TARGET_CURVE",
        "omitted_curve_coefficient": 0,
        "picard64_reconstruction_exact": True,
        "all140_pairing_reconstruction_exact": True,
        "nonzero_term_count": len(sparse),
        "total_multiplicity": sum(candidate),
        "normal_curve_multiplicity": sum(candidate[:92]),
        "exceptional_curve_multiplicity": sum(candidate[92:]),
        "decomposition": sparse,
        "decomposition_sha256": csha(candidate),
        "certifies_target_curve_nonfixed_within_complete_linear_system": True,
    })
    return out


def main() -> None:
    for path, expected in EXPECTED_BLOBS.items():
        actual = git_blob(path)
        if actual != expected:
            raise ValueError(f"source lock regression {path}: {actual} != {expected}")

    ex2 = json.loads(EX2_02.read_text())
    if ex2["exact_scan"]["zero_pairing_labels_1based"] != ZERO_LABELS:
        raise ValueError("EX2-02 zero-label regression")

    bundle = load_retained(STAGE33_07 / "picard_base_rows_retained.py", "ex203c_picard")
    marking = load_retained(STAGE33_07 / "stage32_picard_marking_retained.py", "ex203c_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    coords = adapter.class_coordinates_in_retained_basis
    if coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("retained matrix shape regression")

    basis_indices = [j - 1 for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    if coords.extract(basis_indices, list(range(64))) != eye(64):
        raise ValueError("retained basis identity regression")
    basis_set = set(basis_indices)
    nonbasis_indices = [i for i in range(140) if i not in basis_set]
    if len(nonbasis_indices) != 76:
        raise ValueError("nonbasis count regression")

    v6 = json.loads(V6_PATH.read_text())
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    basis_pairings = Matrix([[pairings[j - 1] for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]])
    vcoords = int_row(basis_pairings * gram.inv())
    if vcoords != [int(x) for x in v6["witness"]["picard_coordinates"]]:
        raise ValueError("V6 coordinate regression")

    original = json.loads(AG_PATH.read_text())
    original_support = {
        int(row["known140_label_1based"])
        for row in original["known140_monoid"]["decomposition"]
    }
    if not set(ZERO_LABELS).issubset(original_support):
        raise ValueError("original AG decomposition does not contain all seven target zero curves")

    results = [
        solve_one(z, coords, gram, vcoords, pairings, basis_indices, nonbasis_indices)
        for z in ZERO_LABELS
    ]
    nonfixed = [r["zero_label_1based"] for r in results if r["exact_feasible_witness_materialized"]]
    unresolved = [z for z in ZERO_LABELS if z not in nonfixed]

    out = {
        "schema": "STAGE32EX2_EX2_03C_KNOWN140_ZERO_CURVE_OMISSION_DIAGNOSTIC_V1",
        "stage": "32EX2",
        "unit": "EX2-03C",
        "status": "EXACT_BOUNDED_DIAGNOSTIC_COMPLETE",
        "source_locks": {
            "v6_blob_sha1": EXPECTED_BLOBS[V6_PATH],
            "v6_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "ag_blob_sha1": EXPECTED_BLOBS[AG_PATH],
            "ag_canonical_sha256": original["canonical_sha256_without_this_field"],
            "ex2_02_blob_sha1": EXPECTED_BLOBS[EX2_02],
            "hperp_adapter_canonical_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "all140_retained_coordinates_sha256": adapter.certificate["all140_retained_coordinates_sha256"],
        },
        "exact_reduction": {
            "known140_variable_count": 140,
            "retained_basis_variable_count": 64,
            "nonbasis_variable_count": 76,
            "basis_omission_semantics": "If target z is one of the retained identity-basis curves, impose equality A_nonbasis^T*x at that basis coordinate = V6_coordinate so the completed basis residual n_z is exactly zero.",
            "nonbasis_omission_semantics": "If target z is nonbasis, fix its reduced variable x_z=0.",
            "candidate_acceptance": "Every solver candidate is completed and replayed with exact integer Picard64 coordinates and all140 pairings before any nonfixedness credit.",
        },
        "target_zero_labels_1based": ZERO_LABELS,
        "results": results,
        "summary": {
            "exact_omission_witness_count": len(nonfixed),
            "certified_nonfixed_zero_labels_1based": nonfixed,
            "unresolved_zero_labels_1based": unresolved,
            "all_seven_certified_nonfixed": len(nonfixed) == len(ZERO_LABELS),
        },
        "firewalls": {
            "known140_omission_search_is_complete_H0": False,
            "solver_miss_is_unsat": False,
            "unresolved_target_is_fixed_component": False,
            "all_possible_fixed_curves_classified": False,
            "integral_irreducible_genus1_member_constructed": False,
            "population_wide_no_genus1_member_proved": False,
            "stage32_main_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
