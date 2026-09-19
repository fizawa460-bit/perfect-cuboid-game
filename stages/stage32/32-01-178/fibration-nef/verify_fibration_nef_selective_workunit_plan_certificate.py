#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKUNIT = HERE / "verify_fibration_nef_selective_picard_workunit_preflight.py"
WORKUNIT_BLOB = "0ee1c21df1b765e91937587903e873f83ec06729"


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


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    # Fail closed on the exact producer contract before importing it.
    req(WORKUNIT.is_file(), "missing selective Picard workunit producer")
    req(git_blob(WORKUNIT) == WORKUNIT_BLOB,
        "selective Picard workunit producer drift")
    wu = load_module(WORKUNIT, "stage32_178_workunit_plan_source")

    req(wu.SELECTIVE.is_file(), "missing selective weighted survivor carrier")
    req(wu.git_blob(wu.SELECTIVE) == wu.SELECTIVE_BLOB,
        "selective weighted survivor carrier drift")
    sel = wu.load_module(wu.SELECTIVE, "stage32_178_plan_selective")

    req(sel.STATIC_FIRST.is_file(), "missing static-first carrier")
    req(sel.git_blob(sel.STATIC_FIRST) == sel.STATIC_FIRST_BLOB,
        "static-first carrier drift")
    sf = sel.load_module(sel.STATIC_FIRST, "stage32_178_plan_static_first")
    for name, (path, expected) in sf.LOCKS.items():
        req(path.is_file(), f"missing static-first source lock {name}")
        req(sf.git_blob(path) == expected, f"static-first source drift {name}")

    depth2 = sf.load_module(sf.DEPTH2, "stage32_178_plan_depth2")
    complete = sf.load_module(sf.COMPLETE, "stage32_178_plan_complete")
    req(depth2.DEPTH1.is_file(), "missing depth1 carrier")
    req(depth2.git_blob(depth2.DEPTH1) == depth2.DEPTH1_BLOB,
        "depth1 carrier drift")
    depth1 = depth2.load_module(depth2.DEPTH1, "stage32_178_plan_depth1")
    for name, (path, expected) in depth1.LOCKS.items():
        req(path.is_file(), f"missing depth1 source lock {name}")
        req(depth1.git_blob(path) == expected, f"depth1 source drift {name}")

    weighted = depth1.load_module(depth1.WEIGHTED, "stage32_178_plan_weighted")
    qthr = depth1.load_module(depth1.QTHRESH, "stage32_178_plan_qthreshold")
    weighted.lock_sources_before_import()
    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file(), f"missing qthreshold source lock {name}")
        req(qthr.git_blob(path) == expected, f"qthreshold source drift {name}")

    sigmod = qthr.load_module(qthr.SIGNATURE, "stage32_178_plan_signature")
    existential = qthr.load_module(qthr.EXISTENTIAL, "stage32_178_plan_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_plan_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB,
        "Picard leaf carrier drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_plan_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_plan_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_plan_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    req(complete.UNEQUAL.is_file(), "missing unequal static min-q producer")
    req(complete.git_blob(complete.UNEQUAL) == complete.UNEQUAL_BLOB,
        "unequal static min-q producer drift")
    unequal = complete.load_module(complete.UNEQUAL, "stage32_178_plan_unequal")

    g, d, e = 1, 192, 32
    qcap = (d * d) // 8 + 2 * d + 4 - 4 * g
    req(qcap == 4992, "g1-d192 qcap drift")
    limit = weighted.effective_mass_cap(e, qcap)
    req(limit == e, "unexpected e32 effective mass cap")

    unequal_h, _ = unequal.unequal_static_minq(limit, qcap)
    equal_h = complete.equal_static_minq(limit, qcap)
    hmin = complete.merge_static_minq(unequal_h, equal_h)

    static_keys = []
    for a in range(limit + 1):
        qa = unequal.a_min_q_closed(a)
        if qa > qcap:
            continue
        for (b, c, t), qh in hmin.items():
            if a + b + c > e:
                continue
            min_q = qa + qh
            if min_q <= qcap:
                static_keys.append((a, b, c, t, min_q))

    x4_values = (0, 24, 48, 72, 96)
    rows, _survivor_union = sel.survivor_rows(
        sf=sf, depth2=depth2, depth1=depth1, sigmod=sigmod,
        prefix=prefix, bnb=bnb, kernel=kernel, cert=cert,
        static_keys=static_keys, g=g, d=d, e=e, x4_values=x4_values,
    )

    slice_summaries = []
    unit_identities = []
    total_survivors = 0
    for x4, survivors, _thresholds in rows:
        ordered = tuple(sorted(survivors))
        req(len(ordered) == len(set(ordered)), "duplicate static survivor key")
        records = [
            {"row_id": "g1-d192", "e": e, "x4": x4,
             "a": a, "b": b, "c": c, "t": t}
            for a, b, c, t in ordered
        ]
        total_survivors += len(records)
        start_unit = len(unit_identities)
        for ordinal, start in enumerate(range(0, len(records), wu.WORKUNIT_SIZE)):
            chunk = records[start:start + wu.WORKUNIT_SIZE]
            unit_identities.append({
                "workunit_id": f"g1-d192-e032-x4-{x4:04d}-u{ordinal:04d}",
                "x4": x4,
                "start_index": start,
                "stop_index_exclusive": start + len(chunk),
                "static_key_count": len(chunk),
                "static_key_stream_sha256": wu.stream_sha256(chunk),
            })
        stop_unit = len(unit_identities)
        slice_summaries.append({
            "x4": x4,
            "survivor_static_key_count": len(records),
            "survivor_static_key_stream_sha256": wu.stream_sha256(records),
            "workunit_index_range": [start_unit, stop_unit],
            "workunit_count": stop_unit - start_unit,
        })

    req(all(1 <= u["static_key_count"] <= wu.WORKUNIT_SIZE for u in unit_identities),
        "invalid workunit size")
    identity_stream_sha = wu.stream_sha256(unit_identities)

    body = {
        "schema": "STAGE32_32_01_178_SELECTIVE_WORKUNIT_PLAN_CERTIFICATE_V1",
        "role": "REGENERABLE_PLAN_IDENTITY_NOT_A_NUMERICAL_RESULT_CERTIFICATE",
        "source": {
            "producer_path": str(WORKUNIT.relative_to(HERE.parents[3])),
            "producer_blob_sha1": WORKUNIT_BLOB,
            "selective_weighted_survivor_blob_sha1": wu.SELECTIVE_BLOB,
        },
        "production_target": {
            "row_id": "g1-d192",
            "g": g,
            "d": d,
            "e": e,
            "absolute_qcap": qcap,
            "x4_slices": list(x4_values),
            "static_keys_before_depth2": len(static_keys),
            "depth2_survivor_static_keys_across_slices": total_survivors,
        },
        "partition_contract": {
            "canonical_key_order": ["x4", "a", "b", "c", "t"],
            "workunit_size_ceiling": wu.WORKUNIT_SIZE,
            "workunit_count": len(unit_identities),
            "workunit_identity_stream_sha256": identity_stream_sha,
            "slice_summaries": slice_summaries,
            "unit_identities_included": False,
            "unit_identities_regenerable_from_locked_producer": True,
            "completed_unit_reexecution_required": False,
        },
        "execution_state": {
            "workunits_executed_by_this_certificate": 0,
            "production_heavy_run_armed": False,
            "numerical_result_claimed": False,
            "full_row_census_claimed": False,
            "full178_census_claimed": False,
        },
        "firewalls": {
            "main_credit_changed": False,
            "theorem_credit_changed": False,
            "endpoint_credit_changed": False,
            "merge": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    print("SELECTIVE_WORKUNIT_PLAN_CERTIFICATE_SUMMARY=" + json.dumps({
        "static_keys_before_depth2": len(static_keys),
        "depth2_survivors": total_survivors,
        "workunits": len(unit_identities),
        "identity_stream_sha256": identity_stream_sha,
        "certificate_sha256": body["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    print(json.dumps(body, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
