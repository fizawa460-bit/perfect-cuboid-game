#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import heapq
import importlib.util
import itertools
import json
import sys
from pathlib import Path

import sympy
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
BNB = HERE / "verify_fibration_nef_branch_and_bound_preflight.py"
BNB_BLOB = "6d4c79db4246b8b54cdc45bc6423f00d622740e6"
SIG = HERE / "verify_fibration_nef_signature_factorization.py"
SIG_BLOB = "eaa1351f3da2d18cbc4ee9525e3447b665e753dd"
WEIGHTS80 = (40, 8, 5, 5, 5)


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


def objective80(r: tuple[int, ...]) -> int:
    return sum(WEIGHTS80[i] * int(r[i]) * int(r[i]) for i in range(5))


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def general_zero_center_minimum(problem: dict, cert: dict, static_values: tuple[int, ...], fast):
    if problem.get("structurally_infeasible"):
        return None, None, {"reason": problem.get("reason", "structurally_infeasible")}

    req(problem["mu"] == Matrix.zeros(5, 1), "conditional center is not zero")
    caps = tuple(int(v) for v in problem["caps"])
    lo = int(problem["sum_lo"])
    hi = min(int(problem["sum_hi"]), sum(caps))
    req(len(caps) == 5 and all(v >= 0 for v in caps), "invalid residual caps")
    req(0 <= lo <= int(problem["sum_hi"]), "invalid residual sum window")

    p = fast.parity_witness(static_values)
    if p is None:
        return None, None, {"reason": "static_picard_congruence_unsat"}
    p = tuple(int(v) for v in p)
    req(fast.membership_ok(cert, static_values + p), "minimal parity vector lost Picard membership")

    for i in range(5):
        if p[i] > caps[i]:
            return None, None, {"reason": "minimal_parity_exceeds_coordinate_cap", "coordinate": i}

    base = sum(p)
    if base > hi:
        return None, None, {"reason": "minimal_parity_exceeds_sum_hi"}

    # All feasible sums have parity base mod 2. Because every +2 increment is
    # nonnegative-cost at mu=0, the optimum uses the least feasible total sum.
    increments_needed = max(0, ceil_div(lo - base, 2))
    target_sum = base + 2 * increments_needed
    if target_sum > hi:
        return None, None, {"reason": "sum_window_parity_gap"}

    zmax = tuple((caps[i] - p[i]) // 2 for i in range(5))
    if increments_needed > sum(zmax):
        return None, None, {"reason": "coordinate_caps_cannot_reach_sum_lo"}

    # Marginal objective in scale 80:
    # Delta_i(z)=w_i[(p_i+2z+2)^2-(p_i+2z)^2]
    #           =4*w_i*(p_i+2z+1), with w_i in WEIGHTS80.
    # Each sequence is strictly increasing, so choosing the globally smallest
    # available increments gives the exact separable-convex optimum.
    z = [0] * 5
    heap = []
    for i in range(5):
        if zmax[i] > 0:
            delta = 4 * WEIGHTS80[i] * (p[i] + 1)
            heapq.heappush(heap, (delta, i, 0))

    chosen = []
    for _ in range(increments_needed):
        req(heap, "marginal heap exhausted before required lower sum")
        delta, i, zi = heapq.heappop(heap)
        req(zi == z[i], "marginal heap state drift")
        z[i] += 1
        chosen.append((delta, i))
        if z[i] < zmax[i]:
            next_delta = 4 * WEIGHTS80[i] * (p[i] + 2 * z[i] + 1)
            heapq.heappush(heap, (next_delta, i, z[i]))

    r = tuple(p[i] + 2 * z[i] for i in range(5))
    req(all(0 <= r[i] <= caps[i] for i in range(5)), "general witness violates caps")
    req(lo <= sum(r) <= hi, "general witness violates sum window")
    req(fast.membership_ok(cert, static_values + r), "general witness lost Picard membership")
    value80 = objective80(r)
    return Rational(value80, 80), r, {
        "reason": "exact_zero_center_fixed_parity_capacitated_allocation",
        "base_parity_mass": base,
        "increments_of_two": increments_needed,
        "target_sum": target_sum,
        "zmax": list(zmax),
        "chosen_marginal_count": len(chosen),
        "objective80": value80,
    }


def brute(problem: dict, cert: dict, static_values: tuple[int, ...], fast):
    if problem.get("structurally_infeasible"):
        return None, None
    caps = tuple(int(v) for v in problem["caps"])
    best = None
    witness = None
    for r in itertools.product(*(range(v + 1) for v in caps)):
        s = sum(r)
        if not (int(problem["sum_lo"]) <= s <= int(problem["sum_hi"])):
            continue
        if not fast.membership_ok(cert, static_values + tuple(r)):
            continue
        q = objective80(tuple(r))
        if best is None or q < best or (q == best and tuple(r) < witness):
            best, witness = q, tuple(r)
    return (None, None) if best is None else (Rational(best, 80), witness)


def main() -> None:
    for name, path, expected in (
        ("zero-center closed form", FAST, FAST_BLOB),
        ("branch-and-bound kernel", BNB, BNB_BLOB),
        ("signature factorization", SIG, SIG_BLOB),
    ):
        req(path.is_file() and git_blob(path) == expected, f"{name} source drift")

    fast = load_module(FAST, "stage32_178_general_fast")
    bnb = load_module(BNB, "stage32_178_general_bnb")
    sig = load_module(SIG, "stage32_178_general_sig")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_general_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)
    cert = fast.load_certificate()

    req(kernel.center == Matrix.zeros(5, 11), "kernel center drift")
    req(tuple(kernel.r_degrees) == (0, 0, 0, 0, 0), "residual aggregate degree drift")
    req(kernel.penalty == fast.EXPECTED_PENALTY, "penalty drift")

    # Abstract exhaustive regression over small cap/sum windows. Static values
    # are chosen so the only Picard restrictions on r are the fixed parities.
    abstract_cases = 0
    for caps in (
        (0,0,0,0,0),(1,1,1,1,1),(2,2,2,2,2),(3,2,1,3,2),
        (4,1,4,2,3),(2,4,3,1,4),(5,3,2,4,1)
    ):
        capsum = sum(caps)
        for a in range(2):
            for b in range(2):
                for t in range(2):
                    c = t  # c+t even
                    static = (a,b,c,t,0,8,8)
                    for lo in range(capsum + 1):
                        for hi in sorted({lo, capsum, min(capsum, lo + 2)}):
                            if hi < lo:
                                continue
                            problem = {
                                "structurally_infeasible": False,
                                "caps": caps,
                                "sum_lo": lo,
                                "sum_hi": hi,
                                "mu": Matrix.zeros(5,1),
                            }
                            gv, gr, _ = general_zero_center_minimum(problem, cert, static, fast)
                            bv, br = brute(problem, cert, static, fast)
                            req(gv == bv, f"abstract minimum mismatch caps={caps} static={static} window={(lo,hi)}")
                            req((gr is None) == (br is None), "abstract feasibility mismatch")
                            abstract_cases += 1

    # Real signature problems with active lower-sum/cap behavior. These include
    # e>=d examples, unlike the historical e32 low-mass slice.
    real_cases = []
    saw_positive_sum_lo = False
    saw_nontrivial_cap = False
    saw_feasible = False
    saw_infeasible = False
    for g in (0,1):
        d = 8
        for e in (8,10,12,14,16):
            for a,b,c,t,x4 in (
                (0,0,0,0,0),(1,0,1,1,0),(0,1,1,1,0),
                (1,1,0,0,1),(2,1,1,1,2),(1,2,2,0,3),
            ):
                if a+b+c > e:
                    continue
                problem = sig.signature_problem(bnb, kernel, g=g, d=d, e=e, sig=(a,b,c,t,x4,0))
                static = (a,b,c,t,x4,e,d)
                gv, gr, meta = general_zero_center_minimum(problem, cert, static, fast)
                bv, br = brute(problem, cert, static, fast)
                req(gv == bv, f"real minimum mismatch {(g,d,e,a,b,c,t,x4)}")
                req((gr is None) == (br is None), "real feasibility mismatch")
                if not problem.get("structurally_infeasible"):
                    saw_positive_sum_lo |= int(problem["sum_lo"]) > 0
                    saw_nontrivial_cap |= any(int(v) < int(problem["remaining"]) for v in problem["caps"])
                saw_feasible |= gr is not None
                saw_infeasible |= gr is None
                real_cases.append({
                    "g":g,"d":d,"e":e,"signature":[a,b,c,t,x4],
                    "structurally_infeasible":bool(problem.get("structurally_infeasible")),
                    "sum_lo":None if problem.get("structurally_infeasible") else int(problem["sum_lo"]),
                    "sum_hi":None if problem.get("structurally_infeasible") else int(problem["sum_hi"]),
                    "caps":None if problem.get("structurally_infeasible") else [int(v) for v in problem["caps"]],
                    "minimum":None if gv is None else str(gv),
                    "witness":None if gr is None else list(gr),
                    "reason":meta.get("reason"),
                })

    req(saw_positive_sum_lo, "real regression lacks positive sum_lo case")
    req(saw_nontrivial_cap, "real regression lacks active coordinate cap case")
    req(saw_feasible and saw_infeasible, "real regression lacks feasibility diversity")

    out = {
        "schema":"STAGE32_32_01_178_ZERO_CENTER_GENERAL_CAPS_V1",
        "status":"EXACT_GENERAL_RESIDUAL_MINIMIZER_PASS__ZERO_MAIN_CREDIT",
        "purpose":"Generalize the zero-center Picard residual minimum from the obsolete low-mass e32 simplex to arbitrary active coordinate caps and positive residual sum lower bounds.",
        "exact_theorem":{
            "conditional_center_zero":True,
            "penalty_diagonal":["1/2","1/10","1/16","1/16","1/16"],
            "fixed_picard_parity":["(b+t) mod 2","a mod 2",0,0,0],
            "substitution":"r_i=p_i+2*z_i, z_i>=0",
            "coordinate_cap":"0 <= z_i <= floor((cap_i-p_i)/2)",
            "least_feasible_total":"base=sum(p); k=max(0,ceil((sum_lo-base)/2)); target=base+2k, subject to target<=sum_hi and k<=sum zmax",
            "marginal_scaled80":"Delta_i(z)=4*w80_i*(p_i+2z+1)",
            "marginal_sequences_strictly_increasing":True,
            "exact_algorithm":"Take exactly k globally smallest available marginal +2 increments, respecting zmax.",
            "why_exact":"At mu=0 every marginal cost is positive, so an optimum uses the least feasible total residual mass. For fixed total increment count the objective is separable discrete convex, hence the globally sorted marginal prefix is optimal."
        },
        "regression":{
            "abstract_exhaustive_cases":abstract_cases,
            "real_signature_cases":len(real_cases),
            "positive_sum_lo_exercised":saw_positive_sum_lo,
            "active_coordinate_cap_exercised":saw_nontrivial_cap,
            "feasible_and_infeasible_cases_exercised":saw_feasible and saw_infeasible,
            "all_general_minima_match_independent_bruteforce":True,
            "real_cases":real_cases,
        },
        "current_authority_pivot":{
            "g1_d192_current_e_lower":192,
            "historical_e32_lowmass_route_current_credit":0,
            "general_minimizer_applicable_when_e_exceeds_d":True,
            "next_exact_step":"Build a current-domain g1-d192 bounded panel for active even e>=192 using the general minimizer, then determine whether a same-population full-row replacement can beat HPADJ21."
        },
        "firewalls":{
            "main_credit_changed":False,"full178_complete":False,
            "theorem_credit_changed":False,"endpoint_credit_changed":False,
            "heavy_execution_armed":False,"merge":False
        }
    }
    print("ZERO_CENTER_GENERAL_CAPS_SUMMARY=" + json.dumps({
        "abstract_cases":abstract_cases,
        "real_cases":len(real_cases),
        "positive_sum_lo":saw_positive_sum_lo,
        "active_caps":saw_nontrivial_cap,
        "bruteforce_match":True,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
