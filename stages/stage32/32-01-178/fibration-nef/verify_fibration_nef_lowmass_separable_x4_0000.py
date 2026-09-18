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
FAST_BLOB = "2a51a7b12500a87133af95b9f69004a4a8bf84a7"
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


def main() -> None:
    req(WORKER.is_file() and git_blob(WORKER) == WORKER_BLOB, "worker drift")
    req(FAST.is_file() and git_blob(FAST) == FAST_BLOB, "fast minimizer drift")

    worker = load_module(WORKER, "stage32_178_lowmass_slice_worker")
    fast = load_module(FAST, "stage32_178_lowmass_slice_fast")
    rt = worker.load_runtime()

    req(TARGET_X4 in worker.SELECTED_X4, "target x4 left retained selected slices")
    req(rt["g"] == 1 and rt["d"] == 192 and rt["e"] == 32 and rt["qcap"] == 4992,
        "lowmass target drift")
    req(rt["kernel"].penalty == fast.EXPECTED_PENALTY, "separable penalty drift")
    req(int(rt["cert"]["membership_modulus"]) == 2, "Picard modulus drift")

    rows, _ = rt["sel"].survivor_rows(
        sf=rt["sf"], depth2=rt["depth2"], depth1=rt["depth1"],
        sigmod=rt["sigmod"], prefix=rt["prefix"], bnb=rt["bnb"],
        kernel=rt["kernel"], cert=rt["cert"], static_keys=rt["static_keys"],
        g=rt["g"], d=rt["d"], e=rt["e"], x4_values=(TARGET_X4,),
    )
    req(len(rows) == 1 and rows[0][0] == TARGET_X4, "single-slice reconstruction drift")
    _, survivors, thresholds = rows[0]
    ordered = tuple(sorted(survivors))
    req(len(ordered) == len(set(ordered)), "duplicate survivor key")

    a_cache = {}
    h_cache = {}
    evidence_hash = hashlib.sha256()
    envelope_total = 0
    exact_total = 0
    no_picard = 0
    zero_mass = 0
    total_marginal_steps = 0
    max_marginal_steps = 0
    unique_parity_class_counts = set()
    exact_threshold_min = None
    exact_threshold_max = None

    for a, b, c, t in ordered:
        envelope_threshold = int(thresholds[(a, b, c, t)])
        problem = rt["sigmod"].signature_problem(
            rt["bnb"], rt["kernel"], g=rt["g"], d=rt["d"], e=rt["e"],
            sig=(a, b, c, t, TARGET_X4, 0),
        )
        req(not problem.get("structurally_infeasible"),
            "depth2 survivor became structurally infeasible")
        static_values = (a, b, c, t, TARGET_X4, rt["e"], rt["d"])

        minimum, witness, meta = fast.fast_simplex_minimum(
            problem, rt["cert"], static_values, rt["kernel"].penalty
        )
        unique_parity_class_counts.add(int(meta.get("parity_classes", 0)))
        steps = int(meta.get("marginal_steps", 0))
        total_marginal_steps += steps
        max_marginal_steps = max(max_marginal_steps, steps)

        _cut, exact_threshold = rt["qthr"].qexc_threshold(
            g=rt["g"], d=rt["d"], t=t, x4=TARGET_X4, min_penalty=minimum
        )
        aq = a_cache.setdefault(a, rt["sel"].a_poly_for_key(a, rt["qcap"]))
        hk = (b, c, t)
        hq = h_cache.setdefault(hk, rt["sel"].h_poly_for_key(b, c, t, rt["qcap"]))
        req(aq and hq, "selective polynomial missing key")
        envelope_mass = rt["sel"].cumulative_product(
            aq, hq, min(rt["qcap"], envelope_threshold)
        )

        if exact_threshold is None:
            exact_mass = 0
            no_picard += 1
        else:
            exact_threshold = int(exact_threshold)
            req(exact_threshold <= envelope_threshold,
                "exact threshold exceeds depth2 envelope")
            exact_threshold_min = exact_threshold if exact_threshold_min is None else min(exact_threshold_min, exact_threshold)
            exact_threshold_max = exact_threshold if exact_threshold_max is None else max(exact_threshold_max, exact_threshold)
            exact_mass = rt["sel"].cumulative_product(
                aq, hq, min(rt["qcap"], exact_threshold)
            )

        req(exact_mass <= envelope_mass, "exact mass enlarged envelope")
        if exact_mass == 0:
            zero_mass += 1
        envelope_total += envelope_mass
        exact_total += exact_mass

        evidence = {
            "static_key": [a, b, c, t],
            "depth2_envelope_threshold": envelope_threshold,
            "exact_picard_threshold": exact_threshold,
            "exact_picard_minimum": None if minimum is None else str(minimum),
            "exact_picard_witness": None if witness is None else list(witness),
            "marginal_steps": steps,
            "depth2_envelope_weighted_mass": str(envelope_mass),
            "exact_picard_weighted_mass": str(exact_mass),
        }
        stream_hash_update(evidence_hash, evidence)

    req(exact_total <= envelope_total, "aggregate exact mass enlarged envelope")
    out = {
        "schema": "STAGE32_32_01_178_LOWMASS_SEPARABLE_X4_0000_V1",
        "role": "EXACT_SELECTED_SLICE_NUMERICAL_RESEARCH__ZERO_MAIN_CREDIT",
        "source_locks": {
            "worker_blob_sha1": WORKER_BLOB,
            "fast_minimizer_blob_sha1": FAST_BLOB,
            "selective_weighted_survivor_blob_sha1": rt["wu"].SELECTIVE_BLOB,
        },
        "target": {
            "row_id": "g1-d192",
            "g": rt["g"],
            "d": rt["d"],
            "e": rt["e"],
            "absolute_qcap": rt["qcap"],
            "x4": TARGET_X4,
            "scope": "ONE_COMPLETE_SELECTED_X4_SLICE_NOT_FULL_ROW_NOT_FULL178",
        },
        "exact_algorithm": {
            "picard_residual_minimum": "fixed-parity separable-convex marginal allocation",
            "five_dimensional_branch_and_bound_used": False,
            "runkey_used": False,
            "heavy_execution_armed": False,
            "artifact_production_armed": False,
        },
        "result": {
            "depth2_survivor_static_keys": len(ordered),
            "depth2_envelope_weighted_mass": str(envelope_total),
            "exact_picard_weighted_mass": str(exact_total),
            "exact_picard_tightening": str(envelope_total - exact_total),
            "no_picard_feasible_residual_static_keys": no_picard,
            "zero_exact_weighted_mass_static_keys": zero_mass,
            "total_marginal_steps": total_marginal_steps,
            "max_marginal_steps_per_key": max_marginal_steps,
            "observed_parity_class_counts": sorted(unique_parity_class_counts),
            "exact_threshold_min": exact_threshold_min,
            "exact_threshold_max": exact_threshold_max,
            "key_evidence_stream_sha256": evidence_hash.hexdigest(),
        },
        "next_exact_step": "if this complete slice replay is successful and runtime remains lightweight, extend the identical exact consumer to x4=24,48,72,96 and freeze a five-slice checkpoint before considering wider low-mass row coverage",
        "firewalls": {
            "full_row_census_claimed": False,
            "full178_census_claimed": False,
            "main_credit_changed": False,
            "theorem_credit_changed": False,
            "endpoint_credit_changed": False,
            "merge": False,
        },
    }
    print("LOWMASS_SEPARABLE_X4_0000_SUMMARY=" + json.dumps({
        "keys": len(ordered),
        "envelope_mass": str(envelope_total),
        "exact_mass": str(exact_total),
        "tightening": str(envelope_total - exact_total),
        "no_picard": no_picard,
        "zero_mass": zero_mass,
        "marginal_steps": total_marginal_steps,
        "max_steps": max_marginal_steps,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
