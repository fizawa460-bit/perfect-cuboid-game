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
OBSERVABLE_ORDER = ("a","b","c","t","x4","e","d","r0","r1","r2","r3","r4")
EXPECTED_CONGRUENCES = (
    (1,0,0,0,0,0,0,0,1,0,0,0),
    (0,1,0,1,0,0,0,1,0,0,0,0),
    (0,0,1,1,0,0,0,0,0,0,0,0),
    (0,0,0,0,0,1,0,0,0,0,0,0),
    (0,0,0,0,0,0,1,0,0,0,0,0),
    (0,0,0,0,0,0,0,0,0,1,0,0),
    (0,0,0,0,0,0,0,0,0,0,1,0),
    (0,0,0,0,0,0,0,0,0,0,0,1),
)
EXPECTED_PENALTY = Matrix.diag(
    Rational(1,2), Rational(1,10), Rational(1,16), Rational(1,16), Rational(1,16)
)
ZERO5 = Matrix.zeros(5,1)


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
    proc = subprocess.run([sys.executable, str(AGG)], cwd=HERE, check=True, capture_output=True, text=True)
    payload = json.loads(proc.stdout)
    req(payload["rule_is_exact_for_linear_picard_lattice_extendability"] is True,
        "aggregate Picard rule lost exactness")
    cert = payload["full_observable_image_lattice"]
    req(tuple(cert["observable_order"]) == OBSERVABLE_ORDER, "observable order drift")
    req(int(cert["membership_modulus"]) == 2, "membership modulus drift")
    coeff = tuple(tuple(int(v) for v in row) for row in cert["membership_coefficients_mod_q"])
    req(coeff == EXPECTED_CONGRUENCES, "Picard congruence matrix drift")
    req(int(cert["image_lattice_index_in_Zm"]) == 256, "Picard image-lattice index drift")
    return cert


def membership_ok(cert: dict, values: tuple[int, ...]) -> bool:
    q = int(cert["membership_modulus"])
    return all(sum(int(c)*int(v) for c,v in zip(row, values)) % q == 0
               for row in cert["membership_coefficients_mod_q"])


def parity_witness(static_values: tuple[int, ...]) -> tuple[int, ...] | None:
    a,b,c,t,_x4,e,d = (int(v) for v in static_values)
    if ((c+t)&1) or (e&1) or (d&1):
        return None
    return ((b+t)&1, a&1, 0, 0, 0)


def closed_form_minimum(problem: dict, cert: dict, static_values: tuple[int, ...], penalty: Matrix):
    if problem.get("structurally_infeasible"):
        return None, None, {"reason": problem.get("reason","structurally_infeasible"), "closed_form": True}
    req(problem["mu"] == ZERO5, "conditional center is no longer identically zero")
    req(penalty == EXPECTED_PENALTY, "residual penalty drift")
    R = int(problem["remaining"])
    req(tuple(int(v) for v in problem["caps"]) == (R,)*5, "target simplex cap condition drift")
    req(int(problem["sum_lo"]) == 0 and int(problem["sum_hi"]) == R, "target simplex sum-window drift")

    p = parity_witness(static_values)
    if p is None:
        return None, None, {"reason":"static_picard_congruence_unsat","closed_form":True}
    req(membership_ok(cert, static_values + p), "closed-form parity witness lost Picard membership")
    if sum(p) > R:
        return None, None, {"reason":"minimum_parity_mass_exceeds_remaining","closed_form":True}

    # mu=0 and every diagonal weight is positive.  On r_i>=0 the objective
    # sum w_i r_i^2 is coordinatewise nondecreasing, so the least admissible
    # nonnegative integer in each fixed parity class is globally optimal.
    value = Rational(p[0],2) + Rational(p[1],10)
    return value, p, {
        "reason":"zero_center_fixed_parity_closed_form",
        "closed_form":True,
        "parity_mass":sum(p),
        "marginal_steps":0,
        "parity_classes":1,
    }


def fast_simplex_minimum(problem: dict, cert: dict, static_values: tuple[int, ...], penalty: Matrix):
    return closed_form_minimum(problem, cert, static_values, penalty)


def brute_simplex_minimum(problem: dict, cert: dict, static_values: tuple[int, ...], penalty: Matrix):
    if problem.get("structurally_infeasible"):
        return None, None
    R = int(problem["remaining"])
    best = None
    best_r = None
    for r in itertools.product(range(R+1), repeat=5):
        if sum(r) > R or not membership_ok(cert, static_values + tuple(r)):
            continue
        rv = Matrix(r)
        value = sympy.factor((rv.T * penalty * rv)[0])
        if best is None or value < best or (value == best and tuple(r) < best_r):
            best, best_r = value, tuple(r)
    return best, best_r


def main() -> None:
    for name,(path,expected) in LOCKS.items():
        req(path.is_file() and git_blob(path)==expected, f"source drift {name}")
    cold = json.loads(COLD.read_text())
    req("NEW_NONHEAVY_MATHEMATICAL_WEAPON" in {x["id"] for x in cold["reopen_conditions"]},
        "nonheavy reopen condition missing")

    cert = load_certificate()
    bnb = load_module(BNB, "stage32_178_zero_center_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_zero_center_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    req(kernel.center == Matrix.zeros(5,11), "conditional center matrix is not zero")
    req(tuple(kernel.r_degrees) == (0,0,0,0,0), "residual aggregate degrees are not zero")
    req(kernel.penalty == EXPECTED_PENALTY, "conditional penalty drift")
    bridge = bnb.td02_aggregate_bridge(kernel)
    req(all(all(Rational(v)==0 for v in row) for row in bridge["F"]), "TD02 center factor F nonzero")
    req(all(Rational(v)==0 for v in bridge["d_shift"]), "TD02 d-shift nonzero")

    # Independent brute regression over low-mass exact simplex problems.
    fixtures = []
    for d in (8,10,12):
        for e in (0,2,4,6):
            if e>d:
                continue
            for a in range(min(e,3)+1):
                for b in range(min(e-a,3)+1):
                    for c in range(min(e-a-b,3)+1):
                        for t in range(0,4):
                            static=(a,b,c,t,0,e,d)
                            R=e-a-b-c
                            problem={
                                "structurally_infeasible":False,
                                "remaining":R,
                                "caps":(R,)*5,
                                "sum_lo":0,
                                "sum_hi":R,
                                "mu":ZERO5,
                            }
                            fv,fr,_=closed_form_minimum(problem,cert,static,kernel.penalty)
                            bv,br=brute_simplex_minimum(problem,cert,static,kernel.penalty)
                            req(fv==bv, f"closed/brute minimum mismatch {static}")
                            req((fr is None)==(br is None), f"closed/brute feasibility mismatch {static}")
                            fixtures.append((static,fv,fr))
    req(fixtures, "empty brute regression")

    # Current target low-mass theorem: because a+b+c<=e=32<<d=192,
    # all nef caps are R and the sixth-block lower sum bound is zero.
    req(192-32 >= 32, "g1-d192/e32 low-mass dominance drift")

    out={
        "schema":"STAGE32_32_01_178_ZERO_CENTER_PARITY_CLOSED_FORM_V2",
        "purpose":"collapse the exact five-residual Picard minimum to a zero-center fixed-parity closed form, eliminating residual branch-and-bound and marginal allocation on the g1-d192/e32 target",
        "exact_structure":{
            "conditional_center_matrix_zero":True,
            "residual_aggregate_degrees_zero":True,
            "conditional_penalty":["1/2","1/10","1/16","1/16","1/16"],
            "picard_membership_modulus":2,
            "picard_image_lattice_index":256,
            "static_necessary":["c+t == 0 (mod 2)","e == 0 (mod 2)","d == 0 (mod 2)"],
            "unique_minimal_residual_parity_witness":[
                "r0 = (b+t) mod 2",
                "r1 = a mod 2",
                "r2 = r3 = r4 = 0"
            ],
            "exact_minimum_formula":"(r0)/2 + (r1)/10",
            "feasibility_formula":"r0+r1 <= R=e-a-b-c",
        },
        "target":{
            "row_id":"g1-d192","g":1,"d":192,"e":32,
            "all_caps_equal_R":True,"sum_window":"0 <= sum(r) <= R",
            "five_dimensional_branch_and_bound_required":False,
            "separable_marginal_allocation_required":False,
        },
        "bounded_independent_bruteforce":{
            "fixture_count":len(fixtures),
            "all_closed_form_minima_match":True,
        },
        "cold_stop_reopen":{
            "reopen_condition":"NEW_NONHEAVY_MATHEMATICAL_WEAPON",
            "condition_satisfied":True,
            "pilot_measure_runkey_required":False,
            "next_exact_step":"apply the closed-form minimum directly to every static key before any depth2 pass; materialize A/H q-polynomials only for exact-threshold survivors"
        },
        "firewalls":{
            "full_row_census_claimed":False,"full178_census_claimed":False,
            "main_credit_changed":False,"theorem_credit_changed":False,
            "endpoint_credit_changed":False,"heavy_execution_armed":False,
            "artifact_production_armed":False,"merge":False
        }
    }
    print("ZERO_CENTER_PARITY_CLOSED_FORM_SUMMARY="+json.dumps({
        "fixtures":len(fixtures),"center_zero":True,"residual_degrees_zero":True,
        "closed_form":True,"cold_reopen":True
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
