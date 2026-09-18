#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_fibration_nef_selective_picard_workunit.py"
WORKER_BLOB = "3bbc4ba84f7ba5bf7188929d56c4a273ca0532f5"
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
X4ONE = HERE / "verify_fibration_nef_lowmass_separable_x4_0000.py"
X4ONE_BLOB = "e2125399170e95a9ae5d09569b2b9d9e666ef7cf"


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


def stream_sha(rows) -> str:
    h = hashlib.sha256()
    for row in rows:
        h.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode())
        h.update(b"\n")
    return h.hexdigest()


def main() -> None:
    req(WORKER.is_file() and git_blob(WORKER) == WORKER_BLOB, "worker drift")
    req(FAST.is_file() and git_blob(FAST) == FAST_BLOB, "closed-form verifier drift")
    req(X4ONE.is_file() and git_blob(X4ONE) == X4ONE_BLOB, "x4=0 consumer drift")

    worker = load_module(WORKER, "stage32_178_selected5_worker")
    fast = load_module(FAST, "stage32_178_selected5_closed")
    one = load_module(X4ONE, "stage32_178_selected5_one")
    rt = worker.load_runtime()

    x4_values = tuple(int(v) for v in worker.SELECTED_X4)
    req(x4_values == (0,24,48,72,96), "selected x4 contract drift")
    req(rt["g"] == 1 and rt["d"] == 192 and rt["e"] == 32 and rt["qcap"] == 4992,
        "target drift")
    req(all(v == 0 for v in rt["kernel"].center), "conditional center drift")
    req(tuple(rt["kernel"].r_degrees) == (0,0,0,0,0), "residual degree drift")
    req(rt["kernel"].penalty == fast.EXPECTED_PENALTY, "penalty drift")

    # Static Picard/parity feasibility is x4-independent.
    base = []
    static_picard_unsat = 0
    parity_mass_unsat = 0
    for a,b,c,t,min_q in rt["static_keys"]:
        R = rt["e"] - a - b - c
        req(R >= 0, "static key exceeds e")
        p = fast.parity_witness((a,b,c,t,0,rt["e"],rt["d"]))
        if p is None:
            static_picard_unsat += 1
            continue
        p0,p1,p2,p3,p4 = p
        req((p2,p3,p4) == (0,0,0), "tail parity drift")
        if p0+p1 > R:
            parity_mass_unsat += 1
            continue
        base.append((a,b,c,t,int(min_q),p0,p1))

    req(len(base) + static_picard_unsat + parity_mass_unsat == len(rt["static_keys"]),
        "base accounting mismatch")

    # A/H polynomials are independent of x4; retain one cache across all slices.
    a_cache = {}
    h_cache = {}
    rows = []
    all_evidence = []

    for x4 in x4_values:
        pruned = 0
        survivors = 0
        exact_mass = 0
        zero_mass = 0
        threshold_min = None
        threshold_max = None
        slice_evidence = []

        for a,b,c,t,min_q,p0,p1 in base:
            minimum, threshold = one.exact_threshold(
                g=rt["g"], d=rt["d"], t=t, x4=x4, p0=p0, p1=p1
            )
            threshold_min = threshold if threshold_min is None else min(threshold_min, threshold)
            threshold_max = threshold if threshold_max is None else max(threshold_max, threshold)
            if min_q > threshold:
                pruned += 1
                continue

            survivors += 1
            if a not in a_cache:
                a_cache[a] = rt["sel"].a_poly_for_key(a, rt["qcap"])
            hk = (b,c,t)
            if hk not in h_cache:
                h_cache[hk] = rt["sel"].h_poly_for_key(b,c,t,rt["qcap"])
            aq, hq = a_cache[a], h_cache[hk]
            req(aq and hq, "missing selective polynomial")
            mass = rt["sel"].cumulative_product(aq,hq,min(rt["qcap"],threshold))
            if mass == 0:
                zero_mass += 1
            exact_mass += mass
            slice_evidence.append({
                "static_key":[a,b,c,t],
                "residual_parity":[p0,p1,0,0,0],
                "minimum":str(minimum),
                "threshold":threshold,
                "mass":str(mass),
            })

        req(pruned + survivors == len(base), f"slice accounting mismatch x4={x4}")
        row = {
            "x4":x4,
            "base_picard_feasible_static_keys":len(base),
            "exact_threshold_pruned_static_keys":pruned,
            "exact_threshold_surviving_static_keys":survivors,
            "zero_exact_weighted_mass_static_keys":zero_mass,
            "exact_picard_weighted_mass":str(exact_mass),
            "exact_threshold_min":threshold_min,
            "exact_threshold_max":threshold_max,
            "survivor_evidence_stream_sha256":stream_sha(slice_evidence),
        }
        rows.append(row)
        all_evidence.extend({"x4":x4, **r} for r in slice_evidence)

    selected_total = sum(int(r["exact_picard_weighted_mass"]) for r in rows)
    out = {
        "schema":"STAGE32_32_01_178_ZERO_CENTER_SELECTED5_V1",
        "role":"EXACT_SELECTED_FIVE_SLICE_NUMERICAL_RESEARCH__ZERO_MAIN_CREDIT",
        "source_locks":{
            "worker_blob_sha1":WORKER_BLOB,
            "zero_center_closed_form_blob_sha1":FAST_BLOB,
            "x4_0000_consumer_blob_sha1":X4ONE_BLOB,
            "selective_weighted_survivor_blob_sha1":rt["wu"].SELECTIVE_BLOB,
        },
        "target":{
            "row_id":"g1-d192","g":rt["g"],"d":rt["d"],"e":rt["e"],
            "absolute_qcap":rt["qcap"],"x4_slices":list(x4_values),
            "scope":"FIVE_COMPLETE_SELECTED_X4_SLICES_NOT_FULL_ROW_NOT_FULL178",
        },
        "static_reduction":{
            "static_keys_before_picard":len(rt["static_keys"]),
            "static_picard_congruence_unsat_keys":static_picard_unsat,
            "minimum_parity_mass_unsat_keys":parity_mass_unsat,
            "x4_independent_picard_feasible_static_keys":len(base),
        },
        "exact_algorithm":{
            "old_depth2_survivor_pass_used":False,
            "signature_problem_called_per_key":False,
            "five_dimensional_branch_and_bound_used":False,
            "separable_marginal_allocation_used":False,
            "A_H_polynomial_cache_shared_across_x4":True,
            "runkey_used":False,
            "heavy_execution_armed":False,
            "artifact_production_armed":False,
        },
        "result":{
            "rows":rows,
            "selected_five_slice_exact_weighted_mass":str(selected_total),
            "A_keys_materialized":len(a_cache),
            "H_keys_materialized":len(h_cache),
            "all_survivor_evidence_stream_sha256":stream_sha(all_evidence),
        },
        "next_exact_step":"derive the exact GRF04 x4 support bound for g1-d192/e32 and extend the same cached closed-form consumer from the selected five slices to every admissible x4 value; if that replay stays lightweight, freeze a complete e32 row certificate",
        "firewalls":{
            "full_row_census_claimed":False,"full178_census_claimed":False,
            "main_credit_changed":False,"theorem_credit_changed":False,
            "endpoint_credit_changed":False,"merge":False,
        },
    }
    print("ZERO_CENTER_SELECTED5_SUMMARY="+json.dumps({
        "static_keys":len(rt["static_keys"]),
        "base_picard_feasible":len(base),
        "A_keys":len(a_cache),
        "H_keys":len(h_cache),
        "selected_total":str(selected_total),
        "rows":[{"x4":r["x4"],"survivors":r["exact_threshold_surviving_static_keys"],
                 "mass":r["exact_picard_weighted_mass"]} for r in rows],
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
