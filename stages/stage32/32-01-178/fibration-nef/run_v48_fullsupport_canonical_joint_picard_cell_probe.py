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
BASE = HERE / "run_v48_support_qbc_exact_tset_cell_probe.py"
BASE_BLOB = "f8347770ee64e09873a47c3418fef7b68538617b"
JOINT = HERE / "verify_support_qbc_joint_min_preflight.py"
JOINT_BLOB = "490db30dc7e4bfc42da0e6dd9947a644dea14275"
CANON = HERE / "verify_support_qbc_canonical_joint_min_preflight.py"
CANON_BLOB = "4296a18f9fb1b59f963206ff28af73a4e9cf7ef0"
V48_UPPER_BOUND = 128470212118313474449
CURRENT_384_CANDIDATE = 128443221087959579960


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(p: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, p)
    req(spec is not None and spec.loader is not None, "cannot load " + str(p))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def count_with_rad(xs: list[int], *, d: int, tset: tuple[int, ...], rad: int) -> int:
    if not xs or not tset or rad < 0:
        return 0
    merged: list[list[int]] = []
    for t in reversed(tset):
        lo = (d // 2 - int(t) - rad + 1) // 2
        hi = (d // 2 - int(t) + rad) // 2
        if lo > hi:
            continue
        if merged and lo <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    return sum(
        bisect.bisect_right(xs, hi) - bisect.bisect_left(xs, lo)
        for lo, hi in merged
    )


def count_with_rad_bruteforce(xs: list[int], *, d: int, tset: tuple[int, ...], rad: int) -> int:
    if not xs or not tset or rad < 0:
        return 0
    return sum(
        min(abs(d // 2 - 2 * int(x4) - int(t)) for t in tset) <= rad
        for x4 in xs
    )


def picard_rad(*, d: int, g: int, q: int, p0: int, p1: int) -> int:
    rhs120 = (15 * d * d) // 2 + 120 * d + 240 - 240 * g
    budget = rhs120 - 60 * int(q) - 60 * (int(p0) & 1) - 12 * (int(p1) & 1)
    if budget < 0:
        return -1
    return math.isqrt(budget // 10)


def main() -> None:
    started = time.perf_counter()
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--row-index", type=int, default=22)
    ap.add_argument("--b", type=int, default=36)
    ap.add_argument("--c", type=int, required=True)
    args = ap.parse_args()

    req(BASE.is_file() and blob(BASE) == BASE_BLOB, "base exact-tset probe drift")
    req(JOINT.is_file() and blob(JOINT) == JOINT_BLOB, "joint-min preflight drift")
    req(CANON.is_file() and blob(CANON) == CANON_BLOB, "canonical joint-min preflight drift")
    base = load(BASE, "v48_picard_base")
    joint_min = load(JOINT, "v48_picard_joint")
    canonical_min = load(CANON, "v48_picard_canonical_joint")

    req(base.SUPPORT.is_file() and blob(base.SUPPORT) == base.SUPPORT_BLOB, "support worker drift")
    req(base.V47_HELPER.is_file() and blob(base.V47_HELPER) == base.V47_HELPER_BLOB, "V47 helper drift")
    support = base.load(base.SUPPORT, "v48_picard_support")
    qparent = support.load(support.FAST_PARENT, "v48_fullsupport_qparent")
    req(support.blob(support.FAST_PARENT) == support.FAST_PARENT_BLOB, "full-support qparent drift")
    hd = base.load(base.V47_HELPER, "v48_picard_v47")
    direct = hd.load(hd.DIRECT, hd.DIRECT_BLOB, "v48_picard_direct")
    proj = hd.load(hd.PROJECTION, hd.PROJECTION_BLOB, "v48_picard_projection")

    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx
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
    K = counter.ceil_div(d - 16 * g + 16, 4)
    tq = (d * d + 16 * d + (32 if g == 0 else 0)) // 8

    c = args.c
    jbc = bc_joint[args.b][c]
    active = []
    qkeys: set[int] = set()
    for sbc in range(8):
        for r in (0, 1):
            hist = {int(q): int(w) for q, w in jbc[sbc][r].items() if int(w) and int(q) <= tq}
            if hist:
                active.append((sbc, r, hist))
                qkeys.update(hist)
    req(bool(active), "probe cell has no active qBC histogram")

    c3 = counter.component3(d, args.b, c)
    req(c3 >= 0, "negative component3")
    old_intervals = hd.interval_table(proj, args.b, c, qkeys)
    points = hd.x4_points(h16, h, g, args.b, c)
    p0 = (args.b + c) & 1

    prepared = []
    joint_strict_tset_states = picard_strict_count_states = 0
    canonical_strict_tset_states = canonical_empty_vs_relaxed_states = 0
    canonical_picard_strict_vs_relaxed_states = 0
    fullsupport_strict_count_states = 0
    fast_regression_cases = 0
    fullsupport_qcut_regression_cases = 0
    for sbc, r, hist in active:
        parity = c & 1
        t_domain = tuple(range(parity, args.b + c + 1, 2))
        separate_floor = {t: support.aggregate_q_lower(args.b, c, t, sbc) for t in t_domain}
        joint_floor = {t: joint_min.joint_q_lower(args.b, c, t, sbc) for t in t_domain}
        canonical_floor = {t: canonical_min.canonical_joint_q_lower(args.b, c, t, sbc) for t in t_domain}
        req(all(joint_floor[t] >= separate_floor[t] for t in t_domain), "joint floor weakening")
        req(all(canonical_floor[t] >= joint_floor[t] for t in t_domain), "canonical joint floor weakening")

        hulls = {}
        separate_tsets = {}
        joint_tsets = {}
        canonical_tsets = {}
        for qbc in hist:
            separate = tuple(t for t in t_domain if separate_floor[t] <= qbc)
            joined = tuple(t for t in t_domain if joint_floor[t] <= qbc)
            canonical = tuple(t for t in t_domain if canonical_floor[t] <= qbc)
            req(bool(separate) and set(joined).issubset(separate), f"t-set relation {(c,sbc,r,qbc)}")
            req(set(canonical).issubset(joined), f"canonical t-set escaped relaxed joint {(c,sbc,r,qbc)}")
            hull = support.support_t_interval(b=args.b, c=c, support=sbc, qbc=qbc)
            req((separate[0], separate[-1]) == hull, f"hull endpoint drift {(c,sbc,r,qbc)}")
            hulls[qbc] = hull
            separate_tsets[qbc] = separate
            joint_tsets[qbc] = joined
            canonical_tsets[qbc] = canonical
            joint_strict_tset_states += int(len(joined) < len(separate))
            canonical_strict_tset_states += int(len(canonical) < len(joined))
            canonical_empty_vs_relaxed_states += int(bool(joined) and not canonical)

        hull_weight: dict[int, int] = {}
        exact_weight: dict[int, int] = {}
        joint_weight: dict[int, int] = {}
        fullsupport_picard_weight = {0: {}, 1: {}}
        picard_weight = {0: {}, 1: {}}
        canonical_picard_weight = {0: {}, 1: {}}

        for qa in sorted(qa_values):
            if qa > tq:
                hull_weight[qa] = exact_weight[qa] = joint_weight[qa] = 0
                fullsupport_picard_weight[0][qa] = fullsupport_picard_weight[1][qa] = 0
                picard_weight[0][qa] = picard_weight[1][qa] = 0
                canonical_picard_weight[0][qa] = canonical_picard_weight[1][qa] = 0
                continue
            xs = [x4 for x4, cap in points[r] if cap >= qa]
            hw = ew = jw = 0
            fw = [0, 0]
            pw = [0, 0]
            cw = [0, 0]
            for qbc, mult in hist.items():
                if qa + qbc > tq:
                    continue
                old_interval = old_intervals.get(qbc)
                req(old_interval is not None, "support state outside V47 interval")
                hc = hd.count_intersection(counter, xs, d=d, g=g, tint=hulls[qbc], q=qa + qbc)
                ec = base.exact_set_intersection_count(counter, xs, d=d, g=g, tset=separate_tsets[qbc], q=qa + qbc)
                jc = base.exact_set_intersection_count(counter, xs, d=d, g=g, tset=joint_tsets[qbc], q=qa + qbc)
                req(jc <= ec <= hc, f"t-set count order {(c,sbc,r,qbc,qa,jc,ec,hc)}")
                for ap in (0, 1):
                    rad = picard_rad(d=d, g=g, q=qa + qbc, p0=p0, p1=ap)
                    hull_tset = tuple(range(hulls[qbc][0], hulls[qbc][1] + 1, 2))
                    fc = count_with_rad(xs, d=d, tset=hull_tset, rad=rad)
                    pc = count_with_rad(xs, d=d, tset=joint_tsets[qbc], rad=rad)
                    cc = count_with_rad(xs, d=d, tset=canonical_tsets[qbc], rad=rad)
                    if fast_regression_cases < 256:
                        fbrute = count_with_rad_bruteforce(xs, d=d, tset=hull_tset, rad=rad)
                        brute = count_with_rad_bruteforce(xs, d=d, tset=joint_tsets[qbc], rad=rad)
                        cbrute = count_with_rad_bruteforce(xs, d=d, tset=canonical_tsets[qbc], rad=rad)
                        req((fc, pc, cc) == (fbrute, brute, cbrute), f"Picard union counter drift {(c,sbc,r,qbc,qa,ap,fc,pc,cc,fbrute,brute,cbrute)}")
                        fast_regression_cases += 1
                    if fullsupport_qcut_regression_cases < 256:
                        direct_fc = sum(
                            int(qa + qbc <= support.qcut_support(
                                qparent, g=g, d=d, b=args.b, c=c, support=sbc,
                                qbc=qbc, x4=x4, a_parity=ap,
                            ))
                            for x4 in xs
                        )
                        req(fc == direct_fc, f"full-support qcut/count equivalence drift {(c,sbc,r,qbc,qa,ap,fc,direct_fc)}")
                        fullsupport_qcut_regression_cases += 1
                    req(cc <= pc <= fc <= jc <= ec <= hc, f"canonical/full-support/joint-Picard order drift {(c,sbc,r,qbc,qa,ap,cc,pc,fc,jc,ec,hc)}")
                    fullsupport_strict_count_states += int(fc < jc)
                    picard_strict_count_states += int(pc < fc)
                    canonical_picard_strict_vs_relaxed_states += int(cc < pc)
                    fw[ap] += int(mult) * fc
                    pw[ap] += int(mult) * pc
                    cw[ap] += int(mult) * cc
                hw += int(mult) * hc
                ew += int(mult) * ec
                jw += int(mult) * jc
            hull_weight[qa] = hw
            exact_weight[qa] = ew
            joint_weight[qa] = jw
            fullsupport_picard_weight[0][qa], fullsupport_picard_weight[1][qa] = fw
            picard_weight[0][qa], picard_weight[1][qa] = pw
            canonical_picard_weight[0][qa], canonical_picard_weight[1][qa] = cw
        prepared.append((sbc, r, hull_weight, exact_weight, joint_weight, fullsupport_picard_weight, picard_weight, canonical_picard_weight))

    v48 = exact = joined = fullsupport_picard = picard = canonical_picard = 0
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
        ap = aa & 1

        for sbc, r, hw, ew, jw, fw, pw, cw in prepared:
            for sa in range(4):
                tiers = aprof.get((aa, sa))
                ne = ec_by_support.get(sbc + sa)
                if tiers is None or ne is None:
                    continue
                for qa, va in tiers:
                    mult = int(va) * int(ne)
                    x = hw[qa] * mult
                    y = ew[qa] * mult
                    z = jw[qa] * mult
                    f = fw[ap][qa] * mult
                    p = pw[ap][qa] * mult
                    q = cw[ap][qa] * mult
                    req(q <= p <= f <= z <= y <= x, f"weighted canonical/full-support/joint-Picard refinement order {(aa,sbc,r,sa,qa,q,p,f,z,y,x)}")
                    v48 += x
                    exact += y
                    joined += z
                    fullsupport_picard += f
                    picard += p
                    canonical_picard += q
                    strict_weighted_terms += int(q < f)
                    visited_weighted_terms += 1

    req(canonical_picard <= picard <= fullsupport_picard <= joined <= exact <= v48, "cell aggregate canonical successor refinement order drift")

    out = {
        "schema": "STAGE32_32_01_178_V48_FULLSUPPORT_CANONICAL_JOINT_PICARD_CELL_PROBE_V1",
        "status": "EXACT_BOUNDED_CELL_CANONICAL_JOINT_INCREMENTAL_OVER_CURRENT_FULLSUPPORT__ZERO_MAIN_CREDIT",
        "target": {"row_index": args.row_index, "row_id": row_id, "g": g, "d": d, "b": args.b, "c": c},
        "source_locks": {
            "exact_tset_base_probe_blob_sha1": BASE_BLOB,
            "joint_min_preflight_blob_sha1": JOINT_BLOB,
            "canonical_joint_min_preflight_verifier_blob_sha1": CANON_BLOB,
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
            "cell_current_fullsupport_picard_survivors": str(fullsupport_picard),
            "cell_joint_picard_survivors": str(picard),
            "cell_canonical_joint_picard_survivors": str(canonical_picard),
            "exact_tset_incremental_vs_v48": str(v48 - exact),
            "joint_min_incremental_vs_exact_tset": str(exact - joined),
            "current_fullsupport_picard_incremental_vs_v48": str(v48 - fullsupport_picard),
            "joint_picard_incremental_vs_current_fullsupport": str(fullsupport_picard - picard),
            "canonical_joint_incremental_vs_relaxed_joint_picard": str(picard - canonical_picard),
            "canonical_joint_picard_incremental_vs_current_fullsupport": str(fullsupport_picard - canonical_picard),
            "canonical_joint_picard_incremental_vs_v48": str(v48 - canonical_picard),
            "strict_weighted_terms_vs_current_fullsupport": strict_weighted_terms,
            "visited_weighted_terms": visited_weighted_terms,
        },
        "diagnostics": {
            "joint_strict_tset_states": joint_strict_tset_states,
            "canonical_strict_tset_states_vs_relaxed_joint": canonical_strict_tset_states,
            "canonical_empty_tset_states_vs_nonempty_relaxed_joint": canonical_empty_vs_relaxed_states,
            "fullsupport_picard_strict_vs_joint_tset_states": fullsupport_strict_count_states,
            "joint_picard_strict_vs_current_fullsupport_states": picard_strict_count_states,
            "canonical_picard_strict_vs_relaxed_joint_states": canonical_picard_strict_vs_relaxed_states,
            "fast_picard_counter_bruteforce_regression_cases": fast_regression_cases,
            "fullsupport_qcut_equivalence_regression_cases": fullsupport_qcut_regression_cases,
            "picard_p0": p0,
        },
        "semantics": {
            "same_population_as_v48_covered_cell": True,
            "same_population_as_current_384_fullsupport_coordinate_bound": True,
            "current_384_candidate_context": str(CURRENT_384_CANDIDATE),
            "current_fullsupport_semantics_replayed_exactly": True,
            "picard_penalty_formula": "q/2+z^2/12+p0/2+p1/10 <= d^2/16+d+2-2g",
            "joint_min_exact_with_canonical_order_relaxed": True,
            "canonical_joint_min_exact_for_retained_H_terminal_constraints": True,
            "canonical_order_and_retained_parity_enforced": True,
            "actual_weighted_gain_requires_this_exact_replay": True,
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
    print("V48_FULLSUPPORT_CANONICAL_JOINT_PICARD_CELL_PROBE=" + json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
