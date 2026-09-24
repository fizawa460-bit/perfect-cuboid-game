#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "run_v48_support_qbc_exact_tset_cell_probe.py"
BASE_BLOB = "f8347770ee64e09873a47c3418fef7b68538617b"
JOINT = HERE / "verify_support_qbc_joint_min_preflight.py"
JOINT_BLOB = "490db30dc7e4bfc42da0e6dd9947a644dea14275"
V48_UPPER_BOUND = 128470212118313474449


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


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


def main() -> None:
    started = time.perf_counter()
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--row-index", type=int, default=22)
    ap.add_argument("--b", type=int, default=36)
    ap.add_argument("--c", type=int, required=True)
    args = ap.parse_args()

    req(BASE.is_file() and blob(BASE) == BASE_BLOB, "exact-tset base probe drift")
    req(JOINT.is_file() and blob(JOINT) == JOINT_BLOB, "joint-min preflight drift")
    base = load(BASE, "v48_joint_tset_base")
    joint_min = load(JOINT, "v48_joint_tset_min")

    req(base.SUPPORT.is_file() and blob(base.SUPPORT) == base.SUPPORT_BLOB, "support worker drift")
    req(base.V47_HELPER.is_file() and blob(base.V47_HELPER) == base.V47_HELPER_BLOB, "V47 helper drift")
    support = base.load(base.SUPPORT, "v48_joint_tset_support")
    hd = base.load(base.V47_HELPER, "v48_joint_tset_v47")
    direct = hd.load(hd.DIRECT, hd.DIRECT_BLOB, "v48_joint_tset_direct")
    proj = hd.load(hd.PROJECTION, hd.PROJECTION_BLOB, "v48_joint_tset_projection")

    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx

    req(0 <= args.row_index < len(rows), "row index outside source manifest")
    row_id, g0, d0 = rows[args.row_index]
    g, d = int(g0), int(d0)
    h = d // 2
    req((args.row_index, row_id, g, d, args.b) == (22, "g1-d192", 1, 192, 36), "probe target drift")
    req(0 <= args.c <= h, "c outside target row")

    bc_joint = bc.build_joint_bc_shard(old.HMAX, args.b, args.b)
    ca = [counter.component_a(d, aa) for aa in range(h + 1)]
    aprof: dict[tuple[int, int], tuple[tuple[int, int], ...]] = {}
    qa_values: set[int] = set()
    for aa in range(h + 1):
        if ca[aa] < 0:
            continue
        for sa in range(4):
            tiers = profiles[aa][sa]
            if tiers:
                tt = tuple((int(q), int(w)) for q, w in tiers)
                aprof[(aa, sa)] = tt
                qa_values.update(q for q, _ in tt if int(q) >= 0)
    qa_values = set(qa_values)

    K = counter.ceil_div(d - 16 * g + 16, 4)
    tq = (d * d + 16 * d + (32 if g == 0 else 0)) // 8
    c = args.c
    jbc = bc_joint[args.b][c]
    active = []
    qkeys: set[int] = set()
    for sbc in range(8):
        for r in (0, 1):
            hist = {
                int(q): int(w)
                for q, w in jbc[sbc][r].items()
                if int(w) and int(q) <= tq
            }
            if hist:
                active.append((sbc, r, hist))
                qkeys.update(hist)
    req(bool(active), "probe cell has no active qBC histogram")

    c3 = counter.component3(d, args.b, c)
    req(c3 >= 0, "probe cell has negative component3")
    old_intervals = hd.interval_table(proj, args.b, c, qkeys)
    points = hd.x4_points(h16, h, g, args.b, c)

    prepared = []
    joint_strict_tset_states = 0
    joint_strict_count_states = 0
    max_removed_t = 0
    max_exact_minus_joint_x4 = 0
    fast_counter_regression_cases = 0

    for sbc, r, hist in active:
        hull_weight: dict[int, int] = {}
        exact_weight: dict[int, int] = {}
        joint_weight: dict[int, int] = {}

        parity = c & 1
        t_domain = tuple(range(parity, args.b + c + 1, 2))
        separate_floor = {
            t: support.aggregate_q_lower(args.b, c, t, sbc)
            for t in t_domain
        }
        joint_floor = {
            t: joint_min.joint_q_lower(args.b, c, t, sbc)
            for t in t_domain
        }
        req(
            all(joint_floor[t] >= separate_floor[t] for t in t_domain),
            f"joint floor weakened separate floor {(c,sbc,r)}",
        )

        separate_tsets = {}
        joint_tsets = {}
        hulls = {}
        for qbc in hist:
            separate = tuple(t for t in t_domain if separate_floor[t] <= qbc)
            joined = tuple(t for t in t_domain if joint_floor[t] <= qbc)
            req(bool(separate), f"nonempty histogram lost separate t-set {(c,sbc,r,qbc)}")
            req(set(joined).issubset(separate), f"joint t-set escaped separate t-set {(c,sbc,r,qbc)}")
            hull = support.support_t_interval(b=args.b, c=c, support=sbc, qbc=qbc)
            req((separate[0], separate[-1]) == hull, f"separate t-set hull drift {(c,sbc,r,qbc)}")
            separate_tsets[qbc] = separate
            joint_tsets[qbc] = joined
            hulls[qbc] = hull
            if len(joined) < len(separate):
                joint_strict_tset_states += 1
                max_removed_t = max(max_removed_t, len(separate) - len(joined))

        for qa in sorted(qa_values):
            if qa > tq:
                hull_weight[qa] = exact_weight[qa] = joint_weight[qa] = 0
                continue
            xs = [x4 for x4, cap in points[r] if cap >= qa]
            hw = ew = jw = 0
            for qbc, mult in hist.items():
                if qa + qbc > tq:
                    continue
                hull = hulls[qbc]
                old_interval = old_intervals.get(qbc)
                req(old_interval is not None, "support state outside V47 interval")
                hc = hd.count_intersection(counter, xs, d=d, g=g, tint=hull, q=qa + qbc)
                ec = base.exact_set_intersection_count(
                    counter, xs, d=d, g=g, tset=separate_tsets[qbc], q=qa + qbc
                )
                jc = base.exact_set_intersection_count(
                    counter, xs, d=d, g=g, tset=joint_tsets[qbc], q=qa + qbc
                )
                if fast_counter_regression_cases < 256:
                    eb = base.exact_set_intersection_count_bruteforce(
                        xs, d=d, g=g, tset=separate_tsets[qbc], q=qa + qbc
                    )
                    jb = base.exact_set_intersection_count_bruteforce(
                        xs, d=d, g=g, tset=joint_tsets[qbc], q=qa + qbc
                    )
                    req((ec, jc) == (eb, jb), f"fast exact counter drift {(c,sbc,r,qbc,qa,ec,jc,eb,jb)}")
                    fast_counter_regression_cases += 1
                req(jc <= ec <= hc, f"joint refinement order drift {(c,sbc,r,qbc,qa,jc,ec,hc)}")
                if jc < ec:
                    joint_strict_count_states += 1
                    max_exact_minus_joint_x4 = max(max_exact_minus_joint_x4, ec - jc)
                hw += int(mult) * hc
                ew += int(mult) * ec
                jw += int(mult) * jc
            hull_weight[qa] = hw
            exact_weight[qa] = ew
            joint_weight[qa] = jw
        prepared.append((sbc, r, hull_weight, exact_weight, joint_weight))

    v48 = exact = joined = 0
    strict_weighted_terms = 0
    visited_weighted_terms = 0

    for aa in range(h + 1):
        if ca[aa] < 0:
            continue
        srem = min(16, d) + ca[aa] + c3
        ec_by_support: dict[int, int] = {}
        for support_count in range(11):
            es = bnd.eligible_e(counter, d, g, h, aa, args.b, c, support_count, srem, K)
            if es:
                ec_by_support[support_count] = len(es)

        for sbc, r, hw, ew, jw in prepared:
            for sa in range(4):
                tiers = aprof.get((aa, sa))
                ne = ec_by_support.get(sbc + sa)
                if tiers is None or ne is None:
                    continue
                for qa, va in tiers:
                    x = hw[qa] * int(va) * int(ne)
                    y = ew[qa] * int(va) * int(ne)
                    z = jw[qa] * int(va) * int(ne)
                    req(z <= y <= x, f"weighted joint refinement order drift {(aa,sbc,r,sa,qa,z,y,x)}")
                    v48 += x
                    exact += y
                    joined += z
                    strict_weighted_terms += int(z < y)
                    visited_weighted_terms += 1

    req(joined <= exact <= v48, "cell aggregate joint refinement order drift")
    exact_incremental = v48 - exact
    joint_incremental_vs_exact = exact - joined
    joint_incremental_vs_v48 = v48 - joined

    out = {
        "schema": "STAGE32_32_01_178_V48_SUPPORT_QBC_JOINT_TSET_CELL_PROBE_V1",
        "status": "EXACT_BOUNDED_CELL_JOINT_MIN_REFINEMENT__ZERO_MAIN_CREDIT",
        "target": {
            "row_index": args.row_index,
            "row_id": row_id,
            "g": g,
            "d": d,
            "b": args.b,
            "c": c,
        },
        "source_locks": {
            "exact_tset_base_probe_blob_sha1": BASE_BLOB,
            "joint_min_preflight_blob_sha1": JOINT_BLOB,
            "support_qbc_worker_blob_sha1": base.SUPPORT_BLOB,
            "v47_helper_blob_sha1": base.V47_HELPER_BLOB,
            "v47_exact_head": base.V47_EXACT_HEAD,
            "hpadj22_source_head": base.HPADJ22_SOURCE_HEAD,
            "v48_certified_upper_bound": str(V48_UPPER_BOUND),
        },
        "result": {
            "cell_v48_hull_survivors": str(v48),
            "cell_exact_tset_survivors": str(exact),
            "cell_joint_tset_survivors": str(joined),
            "exact_tset_incremental_vs_v48": str(exact_incremental),
            "joint_min_incremental_vs_exact_tset": str(joint_incremental_vs_exact),
            "joint_min_incremental_vs_v48": str(joint_incremental_vs_v48),
            "strict_weighted_terms_vs_exact_tset": strict_weighted_terms,
            "visited_weighted_terms": visited_weighted_terms,
        },
        "diagnostics": {
            "joint_strict_tset_states": joint_strict_tset_states,
            "joint_strict_count_states": joint_strict_count_states,
            "max_removed_t_values_per_state": max_removed_t,
            "max_exact_minus_joint_x4_count": max_exact_minus_joint_x4,
            "fast_counter_bruteforce_regression_cases": fast_counter_regression_cases,
        },
        "semantics": {
            "same_population_as_v48_covered_cell": True,
            "joint_min_exact_for_fixed_b_c_t_support_with_canonical_order_relaxed": True,
            "actual_geometric_H_tuple_exactness_claimed": False,
            "additive_subtraction": False,
            "statistical_independence": False,
            "uncomputed_v48_population_unchanged": True,
            "main_consumption_performed": False,
        },
        "timing": {"wall_seconds": time.perf_counter() - started},
        "firewalls": {
            "main_credit_changed": False,
            "full178_numerical_census_changed": False,
            "effectivity_credit": False,
            "theorem_credit_changed": False,
            "endpoint_credit_changed": False,
            "merge": False,
        },
    }
    print("V48_SUPPORT_QBC_JOINT_TSET_CELL_PROBE=" + json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
