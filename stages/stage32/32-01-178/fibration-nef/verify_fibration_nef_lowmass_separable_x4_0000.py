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

    # Important: do NOT reconstruct the old depth2-survivor set.  The new exact
    # minimum is cheaper than the old two-coordinate lower-envelope pass, so
    # apply it directly to every retained static key and materialize A/H
    # q-polynomials only when the exact threshold can admit min_q.
    a_cache = {}
    h_cache = {}
    evidence_hash = hashlib.sha256()
    static_total = len(rt["static_keys"])
    structural = 0
    exact_threshold_pruned = 0
    exact_threshold_survivors = 0
    exact_total = 0
    no_picard = 0
    zero_mass = 0
    total_marginal_steps = 0
    max_marginal_steps = 0
    unique_parity_class_counts = set()
    exact_threshold_min = None
    exact_threshold_max = None
    a_materialized = set()
    h_materialized = set()

    for a, b, c, t, min_q in rt["static_keys"]:
        problem = rt["sigmod"].signature_problem(
            rt["bnb"], rt["kernel"], g=rt["g"], d=rt["d"], e=rt["e"],
            sig=(a, b, c, t, TARGET_X4, 0),
        )
        if problem.get("structurally_infeasible"):
            structural += 1
            continue

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
        if exact_threshold is None:
            no_picard += 1
            exact_threshold_pruned += 1
            continue

        exact_threshold = int(exact_threshold)
        exact_threshold_min = exact_threshold if exact_threshold_min is None else min(exact_threshold_min, exact_threshold)
        exact_threshold_max = exact_threshold if exact_threshold_max is None else max(exact_threshold_max, exact_threshold)
        if int(min_q) > exact_threshold:
            exact_threshold_pruned += 1
            continue

        exact_threshold_survivors += 1
        if a not in a_cache:
            a_cache[a] = rt["sel"].a_poly_for_key(a, rt["qcap"])
            a_materialized.add(a)
        hk = (b, c, t)
        if hk not in h_cache:
            h_cache[hk] = rt["sel"].h_poly_for_key(b, c, t, rt["qcap"])
            h_materialized.add(hk)
        aq = a_cache[a]
        hq = h_cache[hk]
        req(aq and hq, "selective polynomial missing exact-threshold survivor key")

        exact_mass = rt["sel"].cumulative_product(
            aq, hq, min(rt["qcap"], exact_threshold)
        )
        if exact_mass == 0:
            zero_mass += 1
        exact_total += exact_mass

        evidence = {
            "static_key": [a, b, c, t],
            "static_min_q": int(min_q),
            "exact_picard_threshold": exact_threshold,
            "exact_picard_minimum": str(minimum),
            "exact_picard_witness": None if witness is None else list(witness),
            "marginal_steps": steps,
            "exact_picard_weighted_mass": str(exact_mass),
        }
        stream_hash_update(evidence_hash, evidence)

    req(structural + exact_threshold_pruned + exact_threshold_survivors == static_total,
        "static-key accounting mismatch")
    out = {
        "schema": "STAGE32_32_01_178_LOWMASS_SEPARABLE_X4_0000_V2",
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
            "entry_population": "all retained static support/min-q keys before depth2",
            "old_depth2_survivor_pass_used": False,
            "picard_residual_minimum": "fixed-parity separable-convex marginal allocation",
            "five_dimensional_branch_and_bound_used": False,
            "A_H_polynomials_materialized_only_after_exact_threshold": True,
            "runkey_used": False,
            "heavy_execution_armed": False,
            "artifact_production_armed": False,
        },
        "result": {
            "static_keys_before_exact_picard": static_total,
            "structurally_infeasible_static_keys": structural,
            "exact_threshold_pruned_static_keys": exact_threshold_pruned,
            "exact_threshold_surviving_static_keys": exact_threshold_survivors,
            "exact_picard_weighted_mass": str(exact_total),
            "no_picard_feasible_residual_static_keys": no_picard,
            "zero_exact_weighted_mass_static_keys": zero_mass,
            "A_keys_materialized": len(a_materialized),
            "H_keys_materialized": len(h_materialized),
            "total_marginal_steps": total_marginal_steps,
            "max_marginal_steps_per_key": max_marginal_steps,
            "observed_parity_class_counts": sorted(unique_parity_class_counts),
            "exact_threshold_min": exact_threshold_min,
            "exact_threshold_max": exact_threshold_max,
            "survivor_evidence_stream_sha256": evidence_hash.hexdigest(),
        },
        "next_exact_step": "if this direct all-static-key replay succeeds, generalize the same exact consumer over x4=24,48,72,96 and freeze a five-slice exact checkpoint; only then assess extension from selected slices to the complete e=32 x4 range",
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
        "static_keys": static_total,
        "structural": structural,
        "threshold_pruned": exact_threshold_pruned,
        "threshold_survivors": exact_threshold_survivors,
        "exact_mass": str(exact_total),
        "no_picard": no_picard,
        "zero_mass": zero_mass,
        "A_keys": len(a_materialized),
        "H_keys": len(h_materialized),
        "marginal_steps": total_marginal_steps,
        "max_steps": max_marginal_steps,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
