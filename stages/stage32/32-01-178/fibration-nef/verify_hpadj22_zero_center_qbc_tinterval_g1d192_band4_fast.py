#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE / "verify_hpadj22_zero_center_qbc_tinterval_g1d192_band4.py"
PARENT_BLOB = "3e21729cf39783e96aeff82a8cf734ef53a51f9e"
EXPECTED_CURRENT = 2397821920794178000


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "cannot load " + str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def suffix_index(counter: Counter[int]):
    keys = sorted(counter)
    suffix = [0] * (len(keys) + 1)
    for i in range(len(keys) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + int(counter[keys[i]])
    return keys, suffix


def suffix_ge(index, threshold: int) -> int:
    keys, suffix = index
    return suffix[bisect.bisect_left(keys, int(threshold))]


def prefix_index(hist: dict[int, int]):
    keys = sorted(hist)
    prefix = []
    running = 0
    for key in keys:
        running += int(hist[key])
        prefix.append(running)
    return keys, prefix


def prefix_leq(index, threshold: int) -> int:
    keys, prefix = index
    pos = bisect.bisect_right(keys, int(threshold)) - 1
    return 0 if pos < 0 else prefix[pos]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    args = ap.parse_args()

    req(PARENT.is_file() and blob(PARENT) == PARENT_BLOB, "qBC parent verifier drift")
    q = load(PARENT, "stage32_178_qbc_fast_parent")

    direct_path = args.repo_root / q.DIRECT_REL
    req(direct_path.is_file() and blob(direct_path) == q.DIRECT_BLOB, "direct-count source drift")
    req(q.FAST.is_file() and blob(q.FAST) == q.FAST_BLOB, "zero-center parity source drift")
    direct = load(direct_path, "stage32_178_qbc_fast_direct")
    fast = load(q.FAST, "stage32_178_qbc_fast_picard")
    cert = fast.load_certificate()
    req(int(cert["membership_modulus"]) == 2, "Picard modulus drift")

    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx
    row_id, g0, d0 = rows[q.ROW_INDEX]
    g, d = int(g0), int(d0)
    req((row_id, g, d) == (q.ROW_ID, 1, 192), "target row drift")
    h = d // 2
    K = counter.ceil_div(d - 16 * g + 16, 4)
    tq = (d * d + 16 * d + (32 if g == 0 else 0)) // 8
    req(tq == 4992, "target q threshold drift")

    b0, b1 = old.PLANNED[q.BAND]
    joint = bc.build_joint_bc_shard(old.HMAX, b0, b1)

    ca = [counter.component_a(d, a) for a in range(h + 1)]
    row_aprof = {}
    row_qas = set()
    for a in range(h + 1):
        if ca[a] < 0:
            continue
        for sa in range(4):
            tiers = profiles[a][sa]
            if tiers:
                tt = tuple((int(qv), int(mult)) for qv, mult in tiers)
                row_aprof[(a, sa)] = tt
                row_qas.update(qv for qv, _ in tt)
    row_qas = tuple(sorted(qv for qv in row_qas if qv <= tq))

    current = refined = 0
    strict_bc = 0
    bc_records = []
    qbc_bins_seen = x4_qbc_pairs = 0
    current_limit_states = refined_limit_states = 0
    lookup_count = current_regression_queries = 0

    for b in range(b0, min(b1, h) + 1):
        for c in range(h + 1):
            jbc = joint[b][c]
            active = []
            for sbc in range(8):
                for r in (0, 1):
                    hist0 = jbc[sbc][r]
                    if not hist0:
                        continue
                    hist = {
                        int(qv): int(mult)
                        for qv, mult in hist0.items()
                        if int(mult) and int(qv) <= tq
                    }
                    if hist:
                        active.append((sbc, r, hist))
            if not active:
                continue

            c3 = counter.component3(d, b, c)
            if c3 < 0:
                continue
            caps = bnd.x4_caps(h16, h, g, b, c)
            xr = h16.a0_interval(h, g, b, c)
            if xr is None:
                continue

            x4_by_r = {0: [], 1: []}
            for x4 in range(int(xr[0]), int(xr[1]) + 1):
                room = -int(h16.f0(h, g, b, c, x4))
                req(room >= 0, f"negative current x4 room {(b,c,x4)}")
                x4_by_r[x4 & 1].append((x4, room // 138))

            prepared = []
            for sbc, r, hist in active:
                qbc_bins_seen += len(hist)
                hist_prefix = prefix_index(hist)
                cur_limits = Counter()
                ref_limits = {0: Counter(), 1: Counter()}

                for qbc, mult in hist.items():
                    for x4, cap in x4_by_r[r]:
                        x4_qbc_pairs += 1
                        cur_limit = min(cap, tq - qbc)
                        if cur_limit >= 0:
                            cur_limits[cur_limit] += mult
                        for ap in (0, 1):
                            cut = q.qcut(
                                g=g, d=d, b=b, c=c, qbc=qbc,
                                x4=x4, a_parity=ap,
                            )
                            req(
                                cut <= tq,
                                f"new qcut weakened current threshold {(b,c,qbc,x4,ap,cut)}",
                            )
                            limit = min(cap, cut - qbc)
                            if limit >= 0:
                                ref_limits[ap][limit] += mult

                cur_index = suffix_index(cur_limits)
                ref_index = {
                    0: suffix_index(ref_limits[0]),
                    1: suffix_index(ref_limits[1]),
                }
                current_limit_states += len(cur_limits)
                refined_limit_states += len(ref_limits[0]) + len(ref_limits[1])

                # Independent exact identity for the aggregation rewrite:
                # current HPADJ22 acceptance factors into its x4 capacity count
                # and qBC threshold before the new qBC-conditioned gate.
                for qa in row_qas:
                    expected = (
                        int(bnd.survivor_count(caps, r, qa))
                        * prefix_leq(hist_prefix, tq - qa)
                    )
                    observed = suffix_ge(cur_index, qa)
                    req(
                        observed == expected,
                        f"current limit aggregation drift {(b,c,sbc,r,qa,observed,expected)}",
                    )
                    current_regression_queries += 1

                prepared.append((sbc, r, cur_index, ref_index))

            bc_cur = bc_ref = 0
            for a in range(h + 1):
                if ca[a] < 0:
                    continue
                srem = min(16, d) + ca[a] + c3
                ec = {}
                for support in range(11):
                    es = bnd.eligible_e(counter, d, g, h, a, b, c, support, srem, K)
                    if es:
                        req(
                            all((int(e) & 1) == 0 for e in es),
                            f"odd eligible e {(a,b,c,support)}",
                        )
                        ec[support] = len(es)
                if not ec:
                    continue

                ap = a & 1
                for sbc, r, cur_index, ref_index in prepared:
                    for sa in range(4):
                        tiers = row_aprof.get((a, sa))
                        ne = ec.get(sbc + sa)
                        if tiers is None or ne is None:
                            continue
                        for qa, va in tiers:
                            cur = suffix_ge(cur_index, qa)
                            if not cur:
                                continue
                            ref = suffix_ge(ref_index[ap], qa)
                            req(
                                ref <= cur,
                                f"fast refinement weakened {(a,b,c,sbc,r,sa,qa)}",
                            )
                            w = int(va) * int(ne)
                            bc_cur += cur * w
                            bc_ref += ref * w
                            lookup_count += 1

            current += bc_cur
            refined += bc_ref
            if bc_ref < bc_cur:
                strict_bc += 1
                bc_records.append({
                    "b": b,
                    "c": c,
                    "current": str(bc_cur),
                    "refined": str(bc_ref),
                    "reduction": str(bc_cur - bc_ref),
                })

    req(
        current == EXPECTED_CURRENT,
        f"same-population row-band identity drift {current}!={EXPECTED_CURRENT}",
    )
    reduction = current - refined
    req(reduction >= 0, "negative reduction")
    candidate = q.CURRENT_GLOBAL - reduction

    out = {
        "schema": "STAGE32_32_01_178_HPADJ22_ZERO_CENTER_QBC_TINTERVAL_G1D192_BAND4_FAST_V1",
        "status": "EXACT_CURRENT_HPADJ22_ROW_BAND_REFINEMENT_FAST_AGGREGATION__ZERO_MAIN_CREDIT",
        "target": {
            "row_index": q.ROW_INDEX,
            "row_id": q.ROW_ID,
            "g": g,
            "d": d,
            "band_position": q.BAND,
            "b_interval": [b0, b1],
        },
        "source_locks": {
            "parent_qbc_verifier_blob_sha1": PARENT_BLOB,
            "direct_count_blob_sha1": q.DIRECT_BLOB,
            "zero_center_picard_blob_sha1": q.FAST_BLOB,
            "hpadj22_source_head": "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2",
        },
        "result": {
            "current_row_band_survivors": str(current),
            "refined_row_band_survivors": str(refined),
            "exact_reduction": str(reduction),
            "current_global_upper_bound": str(q.CURRENT_GLOBAL),
            "candidate_global_upper_bound_if_promoted": str(candidate),
            "global_reduction_fraction": reduction / q.CURRENT_GLOBAL,
            "one_percent_threshold": str(q.ONE_PERCENT),
            "one_percent_reached_by_this_single_row_band": reduction >= q.ONE_PERCENT,
            "strict_bc_cells": strict_bc,
        },
        "optimization": {
            "mathematics_changed": False,
            "parent_qcut_reused_exactly": True,
            "aggregation_identity": "For fixed (sbc,r,a-parity), accumulate H multiplicity over every (qBC,x4) pair by its exact maximum accepted qA; answer each qA tier by a suffix count.",
            "current_limit_hist_replayed_against_separated_current_rule_for_every_realized_qA": True,
            "qbc_bins_seen": qbc_bins_seen,
            "x4_qbc_pairs": x4_qbc_pairs,
            "current_limit_states": current_limit_states,
            "refined_limit_states": refined_limit_states,
            "current_regression_queries": current_regression_queries,
            "weighted_lookup_count": lookup_count,
        },
        "mathematics": {
            "identity_t": "t=x0+x1+x6+x9",
            "identity_complement": "b+c-t=x5+x8+x10",
            "cauchy_upper": "t^2<=4*qBC",
            "cauchy_lower": "(b+c-t)^2<=3*qBC",
            "parity": "t==c (mod2)",
            "safe_qbc_conditioned_t_interval": "b+c-floor(sqrt(3qBC)) <= t <= floor(sqrt(4qBC)), intersect parity c",
            "picard_minimum_lower_bound": "((b+c) mod2)/2+(a mod2)/10",
            "necessary_inequality": "qexc/2+z_min(qBC)^2/12+parity_min<=d^2/16+d+2-2g",
            "exact_t_and_general_caps_deliberately_ignored": True,
            "zero_loss": True,
        },
        "strict_cells": bc_records,
        "semantics": {
            "same_population_as_current_hpadj22": True,
            "direct_replacement_not_additive_subtraction": True,
            "all_non_target_current_hpadj22_survivors_unchanged": True,
            "main_consumption_performed": False,
        },
        "firewalls": {
            "main_credit_changed": False,
            "full178_complete": False,
            "hostile_audit_required_before_promotion": True,
            "theorem_credit_changed": False,
            "endpoint_credit_changed": False,
            "merge": False,
        },
    }

    print("HPADJ22_ZERO_CENTER_QBC_TINTERVAL_FAST_G1D192_BAND4=" + json.dumps({
        "current": str(current),
        "refined": str(refined),
        "reduction": str(reduction),
        "global_fraction": reduction / q.CURRENT_GLOBAL,
        "one_percent": reduction >= q.ONE_PERCENT,
        "candidate_global": str(candidate),
        "strict_bc": strict_bc,
        "qbc_bins_seen": qbc_bins_seen,
        "limit_states": current_limit_states + refined_limit_states,
        "weighted_lookups": lookup_count,
    }, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
