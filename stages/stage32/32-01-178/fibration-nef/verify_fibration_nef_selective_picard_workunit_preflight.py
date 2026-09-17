#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SELECTIVE = HERE / "verify_fibration_nef_selective_weighted_survivor_preflight.py"
SELECTIVE_BLOB = "9e5b662d1e26a20afdf8621b131ffbac60b31b07"
WORKUNIT_SIZE = 256


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


def stream_sha256(records) -> str:
    h = hashlib.sha256()
    for record in records:
        h.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode())
        h.update(b"\n")
    return h.hexdigest()


def panel_indices(n: int) -> tuple[int, ...]:
    if n <= 0:
        return ()
    return tuple(sorted({0, n // 4, n // 2, (3 * n) // 4, n - 1}))


def main() -> None:
    req(SELECTIVE.is_file(), "missing selective weighted survivor carrier")
    req(git_blob(SELECTIVE) == SELECTIVE_BLOB,
        "selective weighted survivor carrier drift")
    sel = load_module(SELECTIVE, "stage32_178_workunit_selective")

    req(sel.STATIC_FIRST.is_file(), "missing static-first carrier")
    req(sel.git_blob(sel.STATIC_FIRST) == sel.STATIC_FIRST_BLOB,
        "static-first carrier drift")
    sf = sel.load_module(sel.STATIC_FIRST, "stage32_178_workunit_static_first")
    for name, (path, expected) in sf.LOCKS.items():
        req(path.is_file(), f"missing static-first source lock {name}")
        req(sf.git_blob(path) == expected, f"static-first source drift {name}")

    depth2 = sf.load_module(sf.DEPTH2, "stage32_178_workunit_depth2")
    complete = sf.load_module(sf.COMPLETE, "stage32_178_workunit_complete")
    req(depth2.DEPTH1.is_file(), "missing depth1 carrier")
    req(depth2.git_blob(depth2.DEPTH1) == depth2.DEPTH1_BLOB,
        "depth1 carrier drift")
    depth1 = depth2.load_module(depth2.DEPTH1, "stage32_178_workunit_depth1")
    for name, (path, expected) in depth1.LOCKS.items():
        req(path.is_file(), f"missing depth1 source lock {name}")
        req(depth1.git_blob(path) == expected, f"depth1 source drift {name}")

    weighted = depth1.load_module(depth1.WEIGHTED, "stage32_178_workunit_weighted")
    qthr = depth1.load_module(depth1.QTHRESH, "stage32_178_workunit_qthreshold")
    weighted.lock_sources_before_import()
    for name, (path, expected) in qthr.SOURCE_LOCKS.items():
        req(path.is_file(), f"missing qthreshold source lock {name}")
        req(qthr.git_blob(path) == expected, f"qthreshold source drift {name}")

    sigmod = qthr.load_module(qthr.SIGNATURE, "stage32_178_workunit_signature")
    existential = qthr.load_module(qthr.EXISTENTIAL, "stage32_178_workunit_existential")
    req(existential.PREFIX.is_file(), "missing Picard-prefix carrier")
    req(existential.git_blob(existential.PREFIX) == existential.PREFIX_BLOB,
        "Picard-prefix carrier drift")
    prefix = existential.load_module(existential.PREFIX, "stage32_178_workunit_prefix")
    req(prefix.LEAF.is_file(), "missing Picard leaf carrier")
    req(prefix.git_blob(prefix.LEAF) == prefix.LEAF_BLOB,
        "Picard leaf carrier drift")
    leaf = prefix.load_module(prefix.LEAF, "stage32_178_workunit_leaf")
    prefix.lock_leaf_and_dependencies(leaf)
    cert = leaf.load_picard_certificate()
    bnb = leaf.load_module(leaf.BNB, "stage32_178_workunit_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_workunit_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)

    req(complete.UNEQUAL.is_file(), "missing unequal static min-q producer")
    req(complete.git_blob(complete.UNEQUAL) == complete.UNEQUAL_BLOB,
        "unequal static min-q producer drift")
    unequal = complete.load_module(complete.UNEQUAL, "stage32_178_workunit_unequal")

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

    workunits = []
    bounded_panel = []
    total_survivors = 0
    total_panel_nodes = 0
    total_panel_exact_mass = 0
    total_panel_envelope_mass = 0

    for x4, survivors, thresholds in rows:
        ordered = tuple(sorted(survivors))
        req(len(ordered) == len(set(ordered)), "duplicate static survivor key")
        total_survivors += len(ordered)

        records = [
            {"row_id": "g1-d192", "e": e, "x4": x4,
             "a": a, "b": b, "c": c, "t": t}
            for a, b, c, t in ordered
        ]
        for ordinal, start in enumerate(range(0, len(records), WORKUNIT_SIZE)):
            chunk = records[start:start + WORKUNIT_SIZE]
            workunits.append({
                "workunit_id": f"g1-d192-e032-x4-{x4:04d}-u{ordinal:04d}",
                "x4": x4,
                "start_index": start,
                "stop_index_exclusive": start + len(chunk),
                "static_key_count": len(chunk),
                "static_key_stream_sha256": stream_sha256(chunk),
            })

        # Bounded real-production exact Picard panel: five canonical quantiles
        # per x4 slice.  This is not the production workunit execution.
        for idx in panel_indices(len(ordered)):
            a, b, c, t = ordered[idx]
            envelope_threshold = int(thresholds[(a, b, c, t)])
            problem = sigmod.signature_problem(
                bnb, kernel, g=g, d=d, e=e,
                sig=(a, b, c, t, x4, 0),
            )
            req(not problem.get("structurally_infeasible"),
                "depth2 survivor became structurally infeasible")
            static_values = (a, b, c, t, x4, e, d)
            minimum, witness, stats = qthr.picard_min_penalty(
                prefix, leaf, bnb, kernel, problem, cert,
                static_values=static_values,
            )
            _cut, exact_threshold = qthr.qexc_threshold(
                g=g, d=d, t=t, x4=x4, min_penalty=minimum
            )
            req(exact_threshold is not None,
                "depth2 survivor has no exact Picard minimum threshold")
            req(int(exact_threshold) <= envelope_threshold,
                "exact Picard threshold exceeds safe depth2 envelope threshold")

            aq = sel.a_poly_for_key(a, qcap)
            hq = sel.h_poly_for_key(b, c, t, qcap)
            req(aq and hq, "selective polynomial missing bounded panel key")
            envelope_mass = sel.cumulative_product(
                aq, hq, min(qcap, envelope_threshold)
            )
            exact_mass = sel.cumulative_product(
                aq, hq, min(qcap, int(exact_threshold))
            )
            req(exact_mass <= envelope_mass,
                "exact Picard minimum enlarged depth2-envelope weighted mass")
            total_panel_nodes += stats.visited_nodes
            total_panel_exact_mass += exact_mass
            total_panel_envelope_mass += envelope_mass
            bounded_panel.append({
                "x4": x4,
                "canonical_survivor_index": idx,
                "static_key": [a, b, c, t],
                "depth2_envelope_threshold": envelope_threshold,
                "exact_picard_threshold": int(exact_threshold),
                "depth2_envelope_weighted_mass": str(envelope_mass),
                "exact_picard_weighted_mass": str(exact_mass),
                "exact_picard_minimum_nodes": stats.visited_nodes,
                "exact_picard_witness": list(witness) if witness is not None else None,
            })

    req(all(1 <= u["static_key_count"] <= WORKUNIT_SIZE for u in workunits),
        "invalid workunit size")
    unit_identity = [
        {k: u[k] for k in (
            "workunit_id", "x4", "start_index", "stop_index_exclusive",
            "static_key_count", "static_key_stream_sha256"
        )}
        for u in workunits
    ]

    out = {
        "schema": "STAGE32_32_01_178_SELECTIVE_PICARD_WORKUNIT_PREFLIGHT_V1",
        "purpose": "connect selective depth2-survivor q-polynomials to bounded exact Picard minima and freeze a deterministic resumable static-key workunit partition before any wider production execution",
        "production_target": {
            "row_id": "g1-d192",
            "e": e,
            "absolute_qcap": qcap,
            "x4_slices": list(x4_values),
            "static_keys_before_depth2": len(static_keys),
            "depth2_survivor_static_keys_across_slices": total_survivors,
        },
        "resumable_workunit_contract": {
            "canonical_key_order": ["x4", "a", "b", "c", "t"],
            "workunit_size_ceiling": WORKUNIT_SIZE,
            "workunit_count": len(workunits),
            "workunit_identity_stream_sha256": stream_sha256(unit_identity),
            "units": workunits,
            "resume_granularity": "one deterministic static-key chunk at one exact x4 slice",
            "completed_unit_reexecution_required": False,
            "artifact_production_armed": False,
        },
        "bounded_real_exact_picard_panel": {
            "selection": "canonical survivor quantiles {first, quarter, middle, three-quarter, last} per selected x4 slice",
            "cases": len(bounded_panel),
            "all_exact_thresholds_no_larger_than_depth2_envelope": True,
            "all_exact_weighted_masses_no_larger_than_depth2_envelope": True,
            "aggregate_exact_picard_minimum_nodes": total_panel_nodes,
            "aggregate_depth2_envelope_weighted_mass": str(total_panel_envelope_mass),
            "aggregate_exact_picard_weighted_mass": str(total_panel_exact_mass),
            "rows": bounded_panel,
            "full_workunit_execution_claimed": False,
        },
        "next_exact_step": "retain a compact certificate for this workunit plan, then execute only unfinished units under the repository heavy/resume authorization gate; investigate x4 translation reuse separately and do not assume it",
        "production_heavy_run_armed": False,
        "full_row_census_claimed": False,
        "full178_census_claimed": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "merge": False,
    }
    print("SELECTIVE_PICARD_WORKUNIT_SUMMARY=" + json.dumps({
        "static_keys_before_depth2": len(static_keys),
        "depth2_survivors": total_survivors,
        "workunits": len(workunits),
        "bounded_panel_cases": len(bounded_panel),
        "bounded_panel_nodes": total_panel_nodes,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
