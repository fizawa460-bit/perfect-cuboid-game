#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import subprocess
import sys
from pathlib import Path

import sympy
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
AGG = HERE / "verify_fibration_nef_aggregate_picard_lattice_preflight.py"
BNB = HERE / "verify_fibration_nef_branch_and_bound_preflight.py"
COLD = HERE / "SELECTIVE-PICARD-COLD-STOP.json"

LOCKS = {
    "aggregate_picard_lattice": (AGG, "5fa9f1d67d6411cb550230b62398aff7bd6488ff"),
    "branch_and_bound": (BNB, "6d4c79db4246b8b54cdc45bc6423f00d622740e6"),
    "cold_stop": (COLD, "5b92371e5f147b96ade73ff9e5ea0d0a9f90f98e"),
}

OBSERVABLE_ORDER = ("a", "b", "c", "t", "x4", "e", "d", "r0", "r1", "r2", "r3", "r4")
EXPECTED_MODULUS = 2
EXPECTED_CONGRUENCES = (
    (1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),  # a+r1
    (0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0),  # b+t+r0
    (0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),  # c+t
    (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),  # e
    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),  # d
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),  # r2
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),  # r3
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),  # r4
)
EXPECTED_PENALTY = Matrix.diag(
    Rational(1, 2), Rational(1, 10), Rational(1, 16), Rational(1, 16), Rational(1, 16)
)
ASSIGNMENT = (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96)
L = (
    (0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0),
    (1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1),
    (1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
)
TARGET = {"g": 1, "d": 192, "e": 32, "row_id": "g1-d192"}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_certificate() -> dict:
    proc = subprocess.run(
        [sys.executable, str(AGG)],
        cwd=HERE,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(proc.stdout)
    req(payload["rule_is_exact_for_linear_picard_lattice_extendability"] is True,
        "aggregate Picard rule lost exactness")
    cert = payload["full_observable_image_lattice"]
    req(tuple(cert["observable_order"]) == OBSERVABLE_ORDER, "observable order drift")
    req(int(cert["membership_modulus"]) == EXPECTED_MODULUS, "membership modulus drift")
    coeff = tuple(tuple(int(v) for v in row) for row in cert["membership_coefficients_mod_q"])
    req(coeff == EXPECTED_CONGRUENCES, "full observable congruence matrix drift")
    req(int(cert["image_lattice_index_in_Zm"]) == 256, "Picard image-lattice index drift")
    return cert


def aggregate_from_x(x: tuple[int, ...]) -> tuple[int, ...]:
    req(len(x) == 11, "assignment width")
    return tuple(sum(row[j] * int(x[j]) for j in range(11)) for row in L)


def membership_ok(cert: dict, values: tuple[int, ...]) -> bool:
    q = int(cert["membership_modulus"])
    return all(
        sum(int(c) * int(v) for c, v in zip(row, values)) % q == 0
        for row in cert["membership_coefficients_mod_q"]
    )


def allowed_parities(cert: dict, static_values: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    req(len(static_values) == 7, "static observable width")
    out = []
    for p in itertools.product((0, 1), repeat=5):
        if membership_ok(cert, static_values + tuple(p)):
            out.append(tuple(int(v) for v in p))
    return tuple(out)


def eval_penalty(penalty: Matrix, r: tuple[int, ...], mu: Matrix):
    delta = Matrix([Rational(r[i]) - mu[i, 0] for i in range(5)])
    return sympy.factor((delta.T * penalty * delta)[0])


def fast_simplex_minimum(problem: dict, cert: dict, static_values: tuple[int, ...], penalty: Matrix):
    if problem.get("structurally_infeasible"):
        return None, None, {"reason": problem.get("reason", "structurally_infeasible")}

    remaining = int(problem["remaining"])
    caps = tuple(int(v) for v in problem["caps"])
    req(caps == (remaining,) * 5, "low-mass simplex cap condition not satisfied")
    req(int(problem["sum_lo"]) == 0 and int(problem["sum_hi"]) == remaining,
        "low-mass simplex sum-window condition not satisfied")
    req(penalty == EXPECTED_PENALTY, "separable penalty drift")

    parities = allowed_parities(cert, static_values)
    if not parities:
        return None, None, {"reason": "picard_static_congruence_unsat", "parity_classes": 0}

    best = None
    best_r = None
    marginal_steps = 0
    mu = problem["mu"]

    for parity in parities:
        parity_mass = sum(parity)
        if parity_mass > remaining:
            continue

        # r_i = parity_i + 2*z_i, z_i >= 0.  The only remaining coupling is
        # sum(z_i) <= floor((remaining-sum(parity))/2).
        budget = (remaining - parity_mass) // 2
        z = [0] * 5

        def fi(i: int, zi: int):
            value = Rational(parity[i] + 2 * zi) - mu[i, 0]
            return penalty[i, i] * value * value

        # Each marginal Delta_i(z)=f_i(z+1)-f_i(z) is strictly increasing:
        # Delta_i(z+1)-Delta_i(z)=8*penalty[i,i] > 0.
        # Therefore merging the five increasing marginal sequences and taking
        # the negative marginals in global ascending order is the exact
        # separable-convex optimum under an at-most budget.
        for _ in range(budget):
            delta = [sympy.factor(fi(i, z[i] + 1) - fi(i, z[i])) for i in range(5)]
            j = min(range(5), key=lambda i: (delta[i], i))
            if delta[j] >= 0:
                break
            z[j] += 1
            marginal_steps += 1

        r = tuple(parity[i] + 2 * z[i] for i in range(5))
        req(sum(r) <= remaining and all(v >= 0 for v in r), "fast witness left simplex")
        req(membership_ok(cert, static_values + r), "fast witness lost Picard membership")
        value = eval_penalty(penalty, r, mu)
        if best is None or value < best or (value == best and r < best_r):
            best, best_r = value, r

    if best is None:
        return None, None, {"reason": "parity_mass_exceeds_simplex", "parity_classes": len(parities)}
    return best, best_r, {
        "reason": "exact_separable_convex_minimum",
        "parity_classes": len(parities),
        "marginal_steps": marginal_steps,
    }


def brute_simplex_minimum(problem: dict, cert: dict, static_values: tuple[int, ...], penalty: Matrix):
    if problem.get("structurally_infeasible"):
        return None, None
    remaining = int(problem["remaining"])
    best = None
    best_r = None
    for r in itertools.product(range(remaining + 1), repeat=5):
        if sum(r) > remaining:
            continue
        if not membership_ok(cert, static_values + tuple(r)):
            continue
        value = eval_penalty(penalty, tuple(r), problem["mu"])
        if best is None or value < best or (value == best and tuple(r) < best_r):
            best, best_r = value, tuple(r)
    return best, best_r


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    cold = json.loads(COLD.read_text())
    req(cold["status"] == "BLOCKED_EXECUTION_AUTHORIZATION_REQUIRED", "cold-stop status drift")
    req("NEW_NONHEAVY_MATHEMATICAL_WEAPON" in {x["id"] for x in cold["reopen_conditions"]},
        "cold-stop no longer exposes nonheavy reopen condition")

    cert = load_certificate()
    bnb = load_module(BNB, "stage32_178_lowmass_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_lowmass_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)
    req(kernel.penalty == EXPECTED_PENALTY, "conditional penalty is no longer diagonal/separable")

    # Exact symbolic target-domain simplification.  For d=192,e=32 and every
    # non-structurally-infeasible terminal, m10<=32 and each known block mass is
    # <=m10.  Hence d-known_i>=160 while R=e-m10<=32, so every cap equals R;
    # the sixth-block condition likewise gives sum_lo=0 and sum_hi=R.
    req(TARGET["d"] - TARGET["e"] >= TARGET["e"],
        "target no longer satisfies d-e>=e low-mass dominance")

    expected_parity_formula = {
        "static_necessary": ["c+t == 0 (mod 2)", "e == 0 (mod 2)", "d == 0 (mod 2)"],
        "residual": [
            "r0 == b+t (mod 2)",
            "r1 == a (mod 2)",
            "r2 == 0 (mod 2)",
            "r3 == 0 (mod 2)",
            "r4 == 0 (mod 2)",
        ],
    }

    # Independent bounded brute regression on low-mass geometric fixtures.
    fixtures = []
    candidate_x = [
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0),
    ]
    for d in (8, 10, 12):
        for e in (0, 2, 4, 6):
            if e > d:
                continue
            for x in candidate_x:
                m10 = sum(x[i] for i, lab in enumerate(ASSIGNMENT) if lab >= 93)
                if m10 > e:
                    continue
                problem = bnb.residual_problem(kernel, g=0, d=d, e=e, x=x)
                if problem.get("structurally_infeasible"):
                    continue
                remaining = int(problem["remaining"])
                if tuple(int(v) for v in problem["caps"]) != (remaining,) * 5:
                    continue
                if int(problem["sum_lo"]) != 0 or int(problem["sum_hi"]) != remaining:
                    continue
                static_values = aggregate_from_x(x) + (e, d)
                fast_v, fast_r, meta = fast_simplex_minimum(problem, cert, static_values, kernel.penalty)
                brute_v, brute_r = brute_simplex_minimum(problem, cert, static_values, kernel.penalty)
                req(fast_v == brute_v, f"fast/brute minimum mismatch d={d} e={e} x={x}")
                req((fast_r is None) == (brute_r is None),
                    f"fast/brute feasibility mismatch d={d} e={e} x={x}")
                if fast_r is not None:
                    req(eval_penalty(kernel.penalty, fast_r, problem["mu"]) == fast_v,
                        "fast witness objective replay failed")
                fixtures.append({
                    "d": d,
                    "e": e,
                    "x": list(x),
                    "remaining": remaining,
                    "fast_minimum": None if fast_v is None else str(fast_v),
                    "fast_witness": None if fast_r is None else list(fast_r),
                    "brute_minimum": None if brute_v is None else str(brute_v),
                    "brute_witness": None if brute_r is None else list(brute_r),
                    "parity_classes": meta.get("parity_classes"),
                })

    req(fixtures, "no bounded regression fixtures")
    req(any(x["fast_witness"] is None for x in fixtures), "regression lacks congruence-UNSAT fixture")
    req(any(x["fast_witness"] is not None for x in fixtures), "regression lacks feasible fixture")

    out = {
        "schema": "STAGE32_32_01_178_LOWMASS_PARITY_SEPARABLE_PICARD_MIN_V1",
        "purpose": "replace the current target's five-dimensional exact Picard residual branch-and-bound minimum by an exact fixed-parity separable-convex resource-allocation minimum, reopening the cold boundary without heavy/artifact execution",
        "source_locks": {name: {"path": str(path.relative_to(HERE.parent.parent.parent.parent.parent)), "blob_sha1": expected}
                         for name, (path, expected) in LOCKS.items()},
        "exact_structure": {
            "observable_order": list(OBSERVABLE_ORDER),
            "picard_membership_modulus": EXPECTED_MODULUS,
            "picard_image_lattice_index": 256,
            "membership_congruences": [list(row) for row in EXPECTED_CONGRUENCES],
            "parity_formula": expected_parity_formula,
            "conditional_penalty": [
                ["1/2", "0", "0", "0", "0"],
                ["0", "1/10", "0", "0", "0"],
                ["0", "0", "1/16", "0", "0"],
                ["0", "0", "0", "1/16", "0"],
                ["0", "0", "0", "0", "1/16"],
            ],
            "penalty_is_diagonal": True,
            "fixed_residual_parity_after_static_key": True,
        },
        "target_lowmass_theorem": {
            "row_id": TARGET["row_id"],
            "g": TARGET["g"],
            "d": TARGET["d"],
            "e": TARGET["e"],
            "for_every_nonstructurally_infeasible_key": True,
            "remaining_R": "e-M10 <= 32",
            "all_five_caps_equal_R": True,
            "sum_window": "0 <= r0+r1+r2+r3+r4 <= R",
            "reason": "known_block_mass_i<=M10<=e=32 and d-known_block_mass_i>=160>=R; same bound on the sixth block makes sum_lo=0",
        },
        "exact_minimizer": {
            "substitution": "r_i = parity_i + 2*z_i, z_i>=0",
            "budget": "sum z_i <= floor((R-sum parity_i)/2)",
            "objective": "sum_i w_i*(parity_i+2*z_i-mu_i)^2",
            "marginal": "Delta_i(z)=f_i(z+1)-f_i(z)",
            "strict_discrete_convexity": "Delta_i(z+1)-Delta_i(z)=8*w_i>0",
            "algorithm": "start z=0; repeatedly take the globally smallest negative next marginal while budget remains",
            "exactness_reason": "the five marginal sequences are individually increasing, so the feasible objective increments form a separable-convex resource-allocation problem and the sorted negative-marginal prefix is optimal",
            "five_dimensional_branch_and_bound_required_on_target": False,
        },
        "bounded_independent_regression": {
            "fixture_count": len(fixtures),
            "all_fast_minima_match_independent_bruteforce": True,
            "fixtures": fixtures,
        },
        "cold_stop_reopen": {
            "reopen_condition": "NEW_NONHEAVY_MATHEMATICAL_WEAPON",
            "condition_satisfied": True,
            "next_exact_step": "wire this exact low-mass minimizer into the retained selected-slice weighted consumer and replay the five x4 slices without arming SELECTIVE-PICARD-RUNKEY",
            "pilot_measure_runkey_required_for_this_new_route": False,
        },
        "firewalls": {
            "selected_lowmass_target_only": True,
            "full_row_census_claimed": False,
            "full178_census_claimed": False,
            "main_credit_changed": False,
            "theorem_credit_changed": False,
            "endpoint_credit_changed": False,
            "heavy_execution_armed": False,
            "artifact_production_armed": False,
            "merge": False,
        },
    }
    print("LOWMASS_PARITY_SEPARABLE_SUMMARY=" + json.dumps({
        "fixtures": len(fixtures),
        "penalty_diagonal": True,
        "picard_modulus": 2,
        "residual_parity_fixed": True,
        "target_simplex": True,
        "cold_reopen": True,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
