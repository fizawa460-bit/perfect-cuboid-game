#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SUPPORT = HERE / "run_hpadj22_support_qbc_local_row_b.py"
SUPPORT_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
PREFLIGHT = HERE / "SUPPORT-QBC-EXACT-TSET-PREFLIGHT.json"
PREFLIGHT_BLOB = "5826f70e36ebd922a3b08f217067de62d6f33f9e"
V47_HELPER = ROOT / "stages/stage32/management/grf04-hpadj22-joint/benchmark_grf04_hpadj22_highd_bchunk.py"
V47_HELPER_BLOB = "99eef03657b07eb5cf86be8d880050fd8aa2d13b"
V47_EXACT_HEAD = "620b90d1ca1f5316d55b88b2620f78eeba1949c7"
HPADJ22_SOURCE_HEAD = "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
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


def exact_relaxed_tset(support, *, b: int, c: int, support_count: int, qbc: int) -> tuple[int, ...]:
    parity = int(c) & 1
    return tuple(
        t
        for t in range(parity, int(b) + int(c) + 1, 2)
        if support.aggregate_q_lower(int(b), int(c), t, int(support_count)) <= int(qbc)
    )


def nearest_set_distance(y: int, values: tuple[int, ...]) -> int:
    req(bool(values), "empty exact relaxed t-set")
    pos = bisect.bisect_left(values, int(y))
    best = 10**30
    if pos < len(values):
        best = min(best, abs(values[pos] - int(y)))
    if pos:
        best = min(best, abs(values[pos - 1] - int(y)))
    return best


def exact_set_intersection_count(counter, xs: list[int], *, d: int, g: int, tset: tuple[int, ...], q: int) -> int:
    if not xs or not tset:
        return 0
    rem = 3 * d * d + 48 * d + 96 - 96 * g - 24 * int(q)
    if rem < 0:
        return 0
    rad = math.isqrt(rem // 4)
    return sum(
        1
        for x4 in xs
        if nearest_set_distance(d // 2 - 2 * int(x4), tset) <= rad
    )


def hull_intersection_count_explicit(xs: list[int], *, d: int, g: int, interval: tuple[int, int], q: int) -> int:
    if not xs:
        return 0
    rem = 3 * d * d + 48 * d + 96 - 96 * g - 24 * int(q)
    if rem < 0:
        return 0
    rad = math.isqrt(rem // 4)
    lo, hi = map(int, interval)
    total = 0
    for x4 in xs:
        y = d // 2 - 2 * int(x4)
        dist = lo - y if y < lo else y - hi if y > hi else 0
        total += int(dist <= rad)
    return total


def main() -> None:
    started = time.perf_counter()
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--row-index", type=int, default=22)
    ap.add_argument("--b", type=int, default=36)
    ap.add_argument("--c", type=int, default=0)
    args = ap.parse_args()

    req(SUPPORT.is_file() and blob(SUPPORT) == SUPPORT_BLOB, "support-qBC worker drift")
    req(PREFLIGHT.is_file() and blob(PREFLIGHT) == PREFLIGHT_BLOB, "exact-tset preflight drift")
    req(V47_HELPER.is_file() and blob(V47_HELPER) == V47_HELPER_BLOB, "V47 helper drift")

    support = load(SUPPORT, "v48_exact_tset_support")
    hd = load(V47_HELPER, "v48_exact_tset_v47_helper")
    req(hd.DIRECT_BLOB == "e965ab0a6ea51938006882ca2110016f48b3768e", "V47 direct source drift")
    req(hd.PROJECTION_BLOB == "6b85abcd693586191eb83a7f275b8dd5d9c69b18", "V47 projection source drift")
    direct = hd.load(hd.DIRECT, hd.DIRECT_BLOB, "v48_exact_tset_direct")
    proj = hd.load(hd.PROJECTION, hd.PROJECTION_BLOB, "v48_exact_tset_projection")

    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx

    req(0 <= args.row_index < len(rows), "row index outside source manifest")
    row_id, g0, d0 = rows[args.row_index]
    g, d = int(g0), int(d0)
    h = d // 2
    req(0 <= args.b <= h and 0 <= args.c <= h, "b/c outside target row")
    req((args.row_index, g, d, args.b) == (22, 1, 192, 36), "probe target drift")

    joint = bc.build_joint_bc_shard(old.HMAX, args.b, args.b)
    ca = [counter.component_a(d, x) for x in range(h + 1)]
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
                qa_values.update(q for q, _ in tt)
    qa_values = {q for q in qa_values if q >= 0}

    K = counter.ceil_div(d - 16 * g + 16, 4)
    tq = (d * d + 16 * d + (32 if g == 0 else 0)) // 8

    c = args.c
    jbc = joint[args.b][c]
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
    tset_states = strict_hole_states = strict_count_states = 0
    max_hole_count = max_hull_minus_exact = 0
    witness_seen = False

    for sbc, r, hist in active:
        old_weight: dict[int, int] = {}
        hull_weight: dict[int, int] = {}
        exact_weight: dict[int, int] = {}

        tsets = {}
        hulls = {}
        for qbc in hist:
            tset = exact_relaxed_tset(
                support, b=args.b, c=c, support_count=sbc, qbc=qbc
            )
            req(bool(tset), f"nonempty histogram lost exact relaxed t-set {(sbc,r,qbc)}")
            hull = support.support_t_interval(
                b=args.b, c=c, support=sbc, qbc=qbc
            )
            req((tset[0], tset[-1]) == hull, f"hull endpoints drift {(sbc,r,qbc,tset,hull)}")
            tsets[qbc] = tset
            hulls[qbc] = hull
            tset_states += 1
            parity_hull_count = ((hull[1] - hull[0]) // 2) + 1
            holes = parity_hull_count - len(tset)
            req(holes >= 0, "negative hole count")
            strict_hole_states += int(holes > 0)
            max_hole_count = max(max_hole_count, holes)
            if (sbc, qbc) == (1, 1296):
                req(tset == (0, 36), f"strict witness t-set drift {tset}")
                witness_seen = True

        for qa in sorted(qa_values):
            if qa > tq:
                old_weight[qa] = hull_weight[qa] = exact_weight[qa] = 0
                continue
            xs = [x4 for x4, cap in points[r] if cap >= qa]
            ow = hw = ew = 0
            for qbc, mult in hist.items():
                if qa + qbc > tq:
                    continue
                old_interval = old_intervals.get(qbc)
                req(old_interval is not None, "support state outside V47 interval")
                hull = hulls[qbc]
                req(
                    old_interval[0] <= hull[0] <= hull[1] <= old_interval[1],
                    f"support hull escaped V47 interval {(sbc,r,qbc,old_interval,hull)}",
                )
                oc = hd.count_intersection(
                    counter, xs, d=d, g=g, tint=old_interval, q=qa + qbc
                )
                hc = hd.count_intersection(
                    counter, xs, d=d, g=g, tint=hull, q=qa + qbc
                )
                hc_explicit = hull_intersection_count_explicit(
                    xs, d=d, g=g, interval=hull, q=qa + qbc
                )
                req(hc == hc_explicit, f"hull count formula drift {(sbc,r,qbc,qa,hc,hc_explicit)}")
                ec = exact_set_intersection_count(
                    counter, xs, d=d, g=g, tset=tsets[qbc], q=qa + qbc
                )
                req(ec <= hc <= oc, f"exact-set refinement order drift {(sbc,r,qbc,qa,ec,hc,oc)}")
                strict_count_states += int(ec < hc)
                max_hull_minus_exact = max(max_hull_minus_exact, hc - ec)
                ow += int(mult) * oc
                hw += int(mult) * hc
                ew += int(mult) * ec
            old_weight[qa] = ow
            hull_weight[qa] = hw
            exact_weight[qa] = ew
        prepared.append((sbc, r, old_weight, hull_weight, exact_weight))

    if c == 0:
        req(witness_seen, "strict witness histogram state absent from c=0 bounded cell")

    v47 = v48 = exact = 0
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

        for sbc, r, ow, hw, ew in prepared:
            for sa in range(4):
                tiers = aprof.get((aa, sa))
                ne = ec_by_support.get(sbc + sa)
                if tiers is None or ne is None:
                    continue
                for qa, va in tiers:
                    x = ow[qa] * int(va) * int(ne)
                    y = hw[qa] * int(va) * int(ne)
                    z = ew[qa] * int(va) * int(ne)
                    req(z <= y <= x, f"weighted refinement order drift {(aa,sbc,r,sa,qa,z,y,x)}")
                    v47 += x
                    v48 += y
                    exact += z
                    strict_weighted_terms += int(z < y)
                    visited_weighted_terms += 1

    req(exact <= v48 <= v47, "cell aggregate refinement order drift")
    incremental = v48 - exact
    # Zero is a valid bounded measurement: structural strictness need not intersect
    # the current weighted survivor population in every c-cell.

    out = {
        "schema": "STAGE32_32_01_178_V48_SUPPORT_QBC_EXACT_TSET_CELL_PROBE_V1",
        "status": "EXACT_BOUNDED_CELL_STRICT_V48_REFINEMENT__ZERO_MAIN_CREDIT",
        "target": {
            "row_index": args.row_index,
            "row_id": row_id,
            "g": g,
            "d": d,
            "b": args.b,
            "c": c,
        },
        "source_locks": {
            "support_qbc_worker_blob_sha1": SUPPORT_BLOB,
            "exact_tset_preflight_blob_sha1": PREFLIGHT_BLOB,
            "v47_helper_blob_sha1": V47_HELPER_BLOB,
            "v47_exact_head": V47_EXACT_HEAD,
            "hpadj22_source_head": HPADJ22_SOURCE_HEAD,
            "v48_certified_upper_bound": str(V48_UPPER_BOUND),
        },
        "result": {
            "cell_v47_joint_survivors": str(v47),
            "cell_v48_support_qbc_hull_survivors": str(v48),
            "cell_exact_tset_survivors": str(exact),
            "cell_v48_incremental_tightening": str(incremental),
            "strict_weighted_terms": strict_weighted_terms,
            "visited_weighted_terms": visited_weighted_terms,
        },
        "tset_diagnostics": {
            "active_tset_states": tset_states,
            "strict_hole_states": strict_hole_states,
            "strict_count_states": strict_count_states,
            "max_parity_hull_hole_count": max_hole_count,
            "max_per_state_hull_minus_exact_x4_count": max_hull_minus_exact,
            "strict_witness_present": witness_seen,
        },
        "semantics": {
            "same_population_as_v48_covered_cell": True,
            "exact_only_for_retained_support_qbc_lower_bound_relaxation": True,
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
    print("V48_SUPPORT_QBC_EXACT_TSET_CELL_PROBE=" + json.dumps(out, sort_keys=True))
    if incremental == 0:
        print("V48_SUPPORT_QBC_EXACT_TSET_CELL_ZERO=1")


if __name__ == "__main__":
    main()
