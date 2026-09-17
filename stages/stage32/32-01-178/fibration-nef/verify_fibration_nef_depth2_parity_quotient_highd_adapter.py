#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEPTH2 = HERE / "verify_fibration_nef_static_lower_envelope_depth2_highd_preflight.py"
PARITY = HERE / "verify_fibration_nef_parity_quotient_weighted_counter_preflight.py"
LOCKS = {
    "depth2_envelope": (DEPTH2, "c60e7dbde8b60a1d0edefd407c4a745373a02b01"),
    "parity_quotient_counter": (PARITY, "051dd67a3317194f743314340722eb15efd44a40"),
}


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


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


def main() -> None:
    for name, (path, expected) in LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    depth2 = load_module(DEPTH2, "stage32_178_pq_depth2")
    parity = load_module(PARITY, "stage32_178_pq_counter")

    req(depth2.DEPTH1.is_file(), "missing depth1 carrier")
    req(depth2.git_blob(depth2.DEPTH1) == depth2.DEPTH1_BLOB,
        "depth1 carrier drift")
    depth1 = depth2.load_module(depth2.DEPTH1, "stage32_178_pq_depth1")
    for name, (path, expected) in depth1.LOCKS.items():
        req(path.is_file(), f"missing depth1 source lock {name}")
        req(depth1.git_blob(path) == expected, f"depth1 source drift {name}")

    weighted = depth1.load_module(depth1.WEIGHTED, "stage32_178_pq_weighted")
    qthr = depth1.load_module(depth1.QTHRESH, "stage32_178_pq_qthreshold")
    weighted.lock_sources_before_import()
    req(parity.WEIGHTED_BLOB == git_blob(depth1.WEIGHTED),
        "parity quotient does not bind the retained weighted producer")

    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file(), f"missing qthreshold source lock {name}")
        req(qthr.git_blob(path) == expected, f"qthreshold source drift {name}")

    sigmod = qthr.load_module(qthr.SIGNATURE, "stage32_178_pq_signature")
    existential = qthr.load_module(qthr.EXISTENTIAL, "stage32_178_pq_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_pq_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB, "Picard leaf source drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_pq_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_pq_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_pq_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    checkpoint = json.loads(depth1.CHECKPOINT.read_text())
    max_stratum = checkpoint["symbolic_full178_prefix_census"]["max_single_stratum"]
    req(max_stratum["row_id"] == "g1-d192", "retained high-d row drift")
    req(int(max_stratum["e"]) == 663, "retained maximum-stratum e drift")

    highd_g, highd_d, highd_e = 1, 192, 32
    qcap = (highd_d * highd_d) // 8 + 2 * highd_d + 4 - 4 * highd_g
    req(qcap == 4992, "g1-d192 qcap drift")

    old_counter = weighted.build_factorized_counter(highd_e, qcap)
    new_counter = parity.build_factorized_counter(weighted, highd_e, qcap)
    req(old_counter == new_counter,
        "parity quotient changed exact factorized counter consumed by depth2")

    normal_budget = 19 * highd_d - 5 * highd_e
    highd_x4 = (0, 24, 48, 72, 96)
    req(all(0 <= x4 <= normal_budget for x4 in highd_x4),
        "high-d x4 outside production range")

    rows = [
        depth2.evaluate_highd_envelope_only(
            depth1=depth1,
            weighted=weighted,
            sigmod=sigmod,
            prefix=prefix,
            bnb=bnb,
            kernel=kernel,
            cert=cert,
            g=highd_g,
            d=highd_d,
            e=highd_e,
            x4=x4,
            factorized_counter=new_counter,
        )
        for x4 in highd_x4
    ]

    out = {
        "schema": "STAGE32_32_01_178_DEPTH2_PARITY_QUOTIENT_HIGHD_ADAPTER_V1",
        "purpose": "wire the exact parity-quotiented weighted counter into the retained depth-2 high-d static lower-envelope consumer without changing the counted population",
        "adapter": {
            "producer": "PARITY_QUOTIENT_WEIGHTED_COUNTER_PREFLIGHT_V1",
            "consumer": "STATIC_LOWER_ENVELOPE_DEPTH2_HIGHD_PREFLIGHT_V1",
            "row_id": "g1-d192",
            "e": highd_e,
            "absolute_qcap": qcap,
            "old_and_new_factorized_counter_exact_match": True,
            "population_change": False,
            "semantic_change": False,
        },
        "bounded_real_high_d_envelope_telemetry": {
            "x4_slices": list(highd_x4),
            "rows": rows,
            "exact_picard_minimum_executed": False,
            "full_row_census_claimed": False,
            "full178_census_claimed": False,
        },
        "next_exact_step": "separate static support/min-q generation from q-polynomial materialization so depth-2 can reject static keys before constructing their full qexc distributions at larger e",
        "production_heavy_run_armed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("DEPTH2_PARITY_QUOTIENT_ADAPTER_SUMMARY=" + json.dumps({
        "highd_slices": len(rows),
        "static_keys": sum(r["static_keys"] for r in rows),
        "depth2_pruned_keys": sum(r["structural_or_envelope_depth2_pruned_keys"] for r in rows),
        "remaining_exact_minimization_keys": sum(r["keys_requiring_exact_picard_minimum_after_depth2"] for r in rows),
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
