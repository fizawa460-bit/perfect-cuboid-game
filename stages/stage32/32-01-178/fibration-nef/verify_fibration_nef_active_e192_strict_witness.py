#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy
from sympy import Matrix

HERE = Path(__file__).resolve().parent
GENERAL = HERE / "verify_fibration_nef_zero_center_general_caps.py"
GENERAL_BLOB = "cc6e6aabace3bbe0d92a9cb32e659b3a7df76650"
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
ROW_WORKER_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
HPADJ16_BLOB = "61805f8b6d661c29805b6966e2453ed411d73189"
HPADJ10_BLOB = "eebeb47f91df22461c33e9974d63aceca4da3b52"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--row-worker", type=Path, required=True)
    ap.add_argument("--hpadj16", type=Path, required=True)
    ap.add_argument("--hpadj10", type=Path, required=True)
    args = ap.parse_args()

    req(GENERAL.is_file() and blob(GENERAL) == GENERAL_BLOB, "general-cap verifier drift")
    req(FAST.is_file() and blob(FAST) == FAST_BLOB, "zero-center verifier drift")
    req(args.row_worker.is_file() and blob(args.row_worker) == ROW_WORKER_BLOB, "HPADJ21 row worker drift")
    req(args.hpadj16.is_file() and blob(args.hpadj16) == HPADJ16_BLOB, "HPADJ16 source drift")
    req(args.hpadj10.is_file() and blob(args.hpadj10) == HPADJ10_BLOB, "HPADJ10 counter drift")

    row_text = re.sub(r"\s+", "", args.row_worker.read_text())
    h10_text = re.sub(r"\s+", "", args.hpadj10.read_text())
    req("lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))" in row_text, "current e-lower formula drift")
    req("B=19*d-5*e+1" in row_text, "current normal-block formula drift")
    req("r=(x0&1)^x1par^x9par" in h10_text, "unequal HPADJ parity formula drift")

    h16 = load_module(args.hpadj16, "stage32_178_active_witness_hpadj16")
    general = load_module(GENERAL, "stage32_178_active_witness_general")
    fast = load_module(FAST, "stage32_178_active_witness_fast")
    cert = fast.load_certificate()

    g, d, e, h = 1, 192, 192, 96
    # Canonical exceptional tuple, assignment order excluding normal x4:
    # x0,x1,x2,x3,x5,x6,x7,x8,x9,x10.
    x0,x1,x2,x3,x5,x6,x7,x8,x9,x10 = (15,16,15,15,15,15,15,15,14,15)
    req(x0 < x1, "witness not in canonical unequal branch")
    req(all(v > 0 for v in (x0,x1,x2,x3,x5,x6,x7,x8,x9,x10)), "witness support drift")

    a = x2+x3+x7
    b = x1+x5+x9
    c = x0+x6+x8+x10
    t = x0+x1+x6+x9
    qA = x2*x2+x3*x3+x7*x7
    qH = x0*x0+x1*x1+x5*x5+x6*x6+x8*x8+x9*x9+x10*x10
    qexc = qA+qH
    support = 10
    r = (x0+x8+x10) & 1

    req((a,b,c,t,qA,qH,qexc,support,r) == (45,45,60,60,675,1577,2252,10,1),
        "witness aggregate drift")
    req(((c-t)&1) == 0, "terminal-family parity relation drift")

    legacy = 4
    K = (d-16*g+16 + 3)//4
    ca = min(13,d-a,d-2*a+4,d//2+5)
    c3 = min(9,d-b-c,d-2*b,d-2*c+1)
    req((K,ca,c3) == (48,13,9), "HPADJ support-capacity drift")
    srem = min(16,d)+ca+c3
    qneed = K-support
    lower = max(legacy,K,d-4*g+4,a+b+c,a+b+c+max(0,qneed))
    upper = min((19*d)//5,3*d,3*d-(b-c))
    excluded = set()
    e_n358 = 3*d-(b-c)
    if b <= h-5 and support+srem == K and e_n358-(a+b+c) >= srem:
        excluded.add(e_n358)
    req((srem,qneed,lower,upper) == (38,38,192,576), "HPADJ source-window drift")
    req(e == lower and e <= upper and e not in excluded, "e192 not in current HPADJ source domain")
    B = 19*d-5*e+1
    req(B == 2689, "e192 normal-block size drift")

    # e=d and M=150 imply R=42 and every residual cap is R; nevertheless use
    # the general-cap minimizer, not the old low-mass special-case proof.
    R = e-a-b-c
    problem = {
        "structurally_infeasible":False,
        "remaining":R,
        "caps":(R,R,R,R,R),
        "sum_lo":0,
        "sum_hi":R,
        "mu":Matrix.zeros(5,1),
    }
    static_values = (a,b,c,t,0,e,d)
    minpen, residual, meta = general.general_zero_center_minimum(problem, cert, static_values, fast)
    req(minpen == Fraction(3,5) and residual == (1,1,0,0,0), "general residual minimum drift")

    genus_budget = Fraction(d*d,16)+d+2-2*g
    strict = []
    boundary = []
    for x4 in (79,81,83,85,87,89,91):
        req(0 <= x4 < B, "x4 outside canonical normal block")
        hp_parity = (x4 & 1) == r
        room = -int(h16.f0(h,g,b,c,x4))
        hp_q_threshold = room // 138
        hp_q_pass = hp_parity and qA <= hp_q_threshold
        static_rho = Fraction((d//2-2*x4-t)**2,12)
        exact_cut = 2*(genus_budget-static_rho-minpen)
        fib_threshold = exact_cut.numerator // exact_cut.denominator
        fib_pass = qexc <= fib_threshold
        rec = {
            "x4":x4,
            "current_hpadj21_parity_pass":hp_parity,
            "current_hpadj21_qA_threshold":hp_q_threshold,
            "current_hpadj21_qA_pass":hp_q_pass,
            "zero_center_exact_qexc_threshold":fib_threshold,
            "qA":qA,
            "qH":qH,
            "qexc":qexc,
            "zero_center_pass":fib_pass,
        }
        boundary.append(rec)
        if hp_q_pass and not fib_pass:
            strict.append(x4)

    req(strict == [83,85,87,89], "active strict x4 witness set drift")
    req(boundary[1]["x4"] == 81 and boundary[1]["current_hpadj21_qA_pass"] and boundary[1]["zero_center_pass"],
        "lower boundary witness drift")
    req(boundary[-1]["x4"] == 91 and not boundary[-1]["current_hpadj21_qA_pass"],
        "upper HPADJ boundary witness drift")

    out = {
        "schema":"STAGE32_32_01_178_ACTIVE_E192_ZERO_CENTER_STRICT_WITNESS_V1",
        "status":"CURRENT_HPADJ21_SOURCE_POPULATION_STRICT_WITNESS_PASS__ZERO_MAIN_CREDIT",
        "source_locks":{
            "current_hpadj21_audited_head":"265fbef0a67014494fcf773af6c3a9f1b095ef95",
            "row_worker_blob_sha1":ROW_WORKER_BLOB,
            "hpadj16_q_source_blob_sha1":HPADJ16_BLOB,
            "hpadj10_counter_blob_sha1":HPADJ10_BLOB,
            "general_zero_center_blob_sha1":GENERAL_BLOB,
        },
        "current_source_key":{
            "row_id":"g1-d192","g":g,"d":d,"e":e,
            "hpadj21_e_window":[lower,upper],
            "normal_block_size":B,
            "b_interval":[36,47],
        },
        "exceptional_witness":{
            "coordinates":{"x0":x0,"x1":x1,"x2":x2,"x3":x3,"x5":x5,"x6":x6,"x7":x7,"x8":x8,"x9":x9,"x10":x10},
            "aggregate":{"a":a,"b":b,"c":c,"t":t,"qA":qA,"qH":qH,"qexc":qexc,"support":support,"required_x4_parity":r},
            "canonical_unequal_branch":True,
            "current_hpadj21_source_key_member":True,
        },
        "zero_center_residual":{
            "remaining_mass":R,
            "exact_minimum":str(minpen),
            "exact_witness":list(residual),
            "general_cap_algorithm_reason":meta["reason"],
        },
        "boundary_replay":boundary,
        "strict_current_source_terminals":{
            "x4_values":strict,
            "count":len(strict),
            "meaning":"These four concrete e192 terminals are admitted by the current HPADJ21 qA/parity necessary condition but rejected by the exact zero-center qexc+residual necessary condition.",
        },
        "next_exact_step":"Enrich the HPADJ21 H-side census by (t,qH,support,required_x4_parity) so the zero-center condition can replace qA-only survivor counts inside the same current b-interval LP population, preserving post-mass adversarial accounting.",
        "firewalls":{
            "bounded_witness_only":True,
            "main_credit_changed":False,
            "main_numeric_bound_replacement_authorized":False,
            "full178_complete":False,
            "theorem_credit_changed":False,
            "endpoint_credit_changed":False,
            "merge":False,
        },
    }
    print("ACTIVE_E192_STRICT_WITNESS_SUMMARY="+json.dumps({
        "row_id":"g1-d192","e":192,
        "aggregate":[a,b,c,t],
        "qA":qA,"qH":qH,"qexc":qexc,
        "strict_x4":strict,
        "strict_count":len(strict),
        "current_source_member":True,
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
