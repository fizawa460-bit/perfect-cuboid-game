#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_fibration_nef_selective_picard_workunit.py"
WORKER_BLOB = "3bbc4ba84f7ba5bf7188929d56c4a273ca0532f5"
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
TARGET_X4 = 0


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


def stream_hash_update(h, row) -> None:
    h.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode())
    h.update(b"\n")


def floor_fraction(v: Fraction) -> int:
    return v.numerator // v.denominator


def exact_threshold(*, g: int, d: int, t: int, x4: int, p0: int, p1: int) -> tuple[Fraction,int]:
    genus_budget = Fraction(d*d,16) + d + 2 - 2*g
    static_rho = Fraction((d//2 - 2*x4 - t)**2,12)
    minimum = Fraction(p0,2) + Fraction(p1,10)
    cut = 2*(genus_budget-static_rho-minimum)
    return minimum, floor_fraction(cut)


def main() -> None:
    req(WORKER.is_file() and git_blob(WORKER) == WORKER_BLOB, "worker drift")
    req(FAST.is_file() and git_blob(FAST) == FAST_BLOB, "closed-form verifier drift")

    worker = load_module(WORKER, "stage32_178_lowmass_slice_worker")
    fast = load_module(FAST, "stage32_178_lowmass_slice_closed")
    rt = worker.load_runtime()

    req(TARGET_X4 in worker.SELECTED_X4, "target x4 left retained selected slices")
    req(rt["g"] == 1 and rt["d"] == 192 and rt["e"] == 32 and rt["qcap"] == 4992,
        "lowmass target drift")
    req(rt["kernel"].center.rows == 5 and rt["kernel"].center.cols == 11, "kernel center shape drift")
    req(all(v == 0 for v in rt["kernel"].center), "conditional center is no longer zero")
    req(tuple(rt["kernel"].r_degrees) == (0,0,0,0,0), "residual aggregate degrees drift")
    req(rt["kernel"].penalty == fast.EXPECTED_PENALTY, "residual penalty drift")

    # No depth2 and no signature_problem calls below.  For d=192,e=32 the
    # residual feasible set is exactly the simplex 0<=sum(r)<=R with R=e-a-b-c.
    # The exact Picard lattice fixes the residual parity uniquely, while mu=0
    # makes that minimal parity vector the exact quadratic minimizer.
    a_cache = {}
    h_cache = {}
    evidence_hash = hashlib.sha256()
    static_total = len(rt["static_keys"])
    static_picard_unsat = 0
    parity_mass_unsat = 0
    exact_threshold_pruned = 0
    exact_threshold_survivors = 0
    exact_total = 0
    zero_mass = 0
    exact_threshold_min = None
    exact_threshold_max = None
    a_materialized = set()
    h_materialized = set()

    for a,b,c,t,min_q in rt["static_keys"]:
        R = rt["e"] - a - b - c
        req(R >= 0, "static key exceeds e mass")
        static_values = (a,b,c,t,TARGET_X4,rt["e"],rt["d"])
        p = fast.parity_witness(static_values)
        if p is None:
            static_picard_unsat += 1
            exact_threshold_pruned += 1
            continue
        p0,p1,p2,p3,p4 = p
        req((p2,p3,p4) == (0,0,0), "closed-form tail parity drift")
        if p0+p1 > R:
            parity_mass_unsat += 1
            exact_threshold_pruned += 1
            continue

        minimum, threshold = exact_threshold(
            g=rt["g"],d=rt["d"],t=t,x4=TARGET_X4,p0=p0,p1=p1
        )
        req(str(minimum) == str(Fraction(p0,2)+Fraction(p1,10)), "minimum formula drift")
        exact_threshold_min = threshold if exact_threshold_min is None else min(exact_threshold_min,threshold)
        exact_threshold_max = threshold if exact_threshold_max is None else max(exact_threshold_max,threshold)
        if int(min_q) > threshold:
            exact_threshold_pruned += 1
            continue

        exact_threshold_survivors += 1
        if a not in a_cache:
            a_cache[a] = rt["sel"].a_poly_for_key(a,rt["qcap"])
            a_materialized.add(a)
        hk=(b,c,t)
        if hk not in h_cache:
            h_cache[hk] = rt["sel"].h_poly_for_key(b,c,t,rt["qcap"])
            h_materialized.add(hk)
        aq,hq=a_cache[a],h_cache[hk]
        req(aq and hq, "selective polynomial missing exact-threshold survivor")

        exact_mass=rt["sel"].cumulative_product(aq,hq,min(rt["qcap"],threshold))
        if exact_mass==0:
            zero_mass+=1
        exact_total+=exact_mass
        stream_hash_update(evidence_hash,{
            "static_key":[a,b,c,t],
            "static_min_q":int(min_q),
            "residual_parity":[p0,p1,0,0,0],
            "exact_picard_minimum":str(minimum),
            "exact_picard_threshold":threshold,
            "exact_picard_weighted_mass":str(exact_mass),
        })

    req(exact_threshold_pruned+exact_threshold_survivors==static_total,
        "static-key accounting mismatch")
    out={
        "schema":"STAGE32_32_01_178_ZERO_CENTER_CLOSED_FORM_X4_0000_V3",
        "role":"EXACT_SELECTED_SLICE_NUMERICAL_RESEARCH__ZERO_MAIN_CREDIT",
        "source_locks":{
            "worker_blob_sha1":WORKER_BLOB,
            "zero_center_closed_form_blob_sha1":FAST_BLOB,
            "selective_weighted_survivor_blob_sha1":rt["wu"].SELECTIVE_BLOB,
        },
        "target":{
            "row_id":"g1-d192","g":rt["g"],"d":rt["d"],"e":rt["e"],
            "absolute_qcap":rt["qcap"],"x4":TARGET_X4,
            "scope":"ONE_COMPLETE_SELECTED_X4_SLICE_NOT_FULL_ROW_NOT_FULL178",
        },
        "exact_algorithm":{
            "entry_population":"all retained static support/min-q keys before depth2",
            "old_depth2_survivor_pass_used":False,
            "signature_problem_called_per_key":False,
            "five_dimensional_branch_and_bound_used":False,
            "separable_marginal_allocation_used":False,
            "conditional_center":"identically zero",
            "residual_parity":"(b+t mod2, a mod2, 0,0,0)",
            "minimum_formula":"r0/2+r1/10",
            "A_H_polynomials_materialized_only_after_exact_threshold":True,
            "runkey_used":False,"heavy_execution_armed":False,
            "artifact_production_armed":False,
        },
        "result":{
            "static_keys_before_exact_picard":static_total,
            "static_picard_congruence_unsat_keys":static_picard_unsat,
            "minimum_parity_mass_unsat_keys":parity_mass_unsat,
            "exact_threshold_pruned_static_keys":exact_threshold_pruned,
            "exact_threshold_surviving_static_keys":exact_threshold_survivors,
            "exact_picard_weighted_mass":str(exact_total),
            "zero_exact_weighted_mass_static_keys":zero_mass,
            "A_keys_materialized":len(a_materialized),
            "H_keys_materialized":len(h_materialized),
            "exact_threshold_min":exact_threshold_min,
            "exact_threshold_max":exact_threshold_max,
            "survivor_evidence_stream_sha256":evidence_hash.hexdigest(),
        },
        "next_exact_step":"generalize the same zero-center closed-form consumer to x4=24,48,72,96, freeze a five-slice exact checkpoint, then test whether complete e=32 x4 coverage is cheap enough to replace the old workunit route entirely",
        "firewalls":{
            "full_row_census_claimed":False,"full178_census_claimed":False,
            "main_credit_changed":False,"theorem_credit_changed":False,
            "endpoint_credit_changed":False,"merge":False,
        },
    }
    print("ZERO_CENTER_CLOSED_FORM_X4_0000_SUMMARY="+json.dumps({
        "static_keys":static_total,
        "static_picard_unsat":static_picard_unsat,
        "parity_mass_unsat":parity_mass_unsat,
        "threshold_pruned":exact_threshold_pruned,
        "threshold_survivors":exact_threshold_survivors,
        "exact_mass":str(exact_total),
        "zero_mass":zero_mass,
        "A_keys":len(a_materialized),
        "H_keys":len(h_materialized),
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
