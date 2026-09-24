#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import math
from functools import lru_cache
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SUPPORT = HERE / "run_hpadj22_support_qbc_local_row_b.py"
SUPPORT_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
JOINT = HERE / "verify_support_qbc_joint_min_preflight.py"
JOINT_BLOB = "490db30dc7e4bfc42da0e6dd9947a644dea14275"
V47_HELPER = ROOT / "stages/stage32/management/grf04-hpadj22-joint/benchmark_grf04_hpadj22_highd_bchunk.py"
V47_HELPER_BLOB = "99eef03657b07eb5cf86be8d880050fd8aa2d13b"
INF = 10**30


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


def dist(y: int, vals: tuple[int, ...]) -> int:
    req(bool(vals), "distance from empty t-set")
    p = bisect.bisect_left(vals, y)
    best = 10**30
    if p < len(vals):
        best = min(best, abs(vals[p] - y))
    if p:
        best = min(best, abs(vals[p - 1] - y))
    return best


def exact_count(xs: list[int], *, d: int, g: int, vals: tuple[int, ...], q: int) -> int:
    if not xs or not vals:
        return 0
    rem = 3 * d * d + 48 * d + 96 - 96 * g - 24 * int(q)
    if rem < 0:
        return 0
    rad = math.isqrt(rem // 4)
    return sum(dist(d // 2 - 2 * x4, vals) <= rad for x4 in xs)


def main() -> None:
    started = time.perf_counter()
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--top", type=int, default=6)
    args = ap.parse_args()

    req(blob(SUPPORT) == SUPPORT_BLOB, "support worker drift")
    req(blob(JOINT) == JOINT_BLOB, "joint-min verifier drift")
    req(blob(V47_HELPER) == V47_HELPER_BLOB, "V47 helper drift")
    support = load(SUPPORT, "joint_tset_selector_support")
    joint = load(JOINT, "joint_tset_selector_min")
    separate_floor_fn = lru_cache(maxsize=None)(support.aggregate_q_lower)
    joint_floor_fn = lru_cache(maxsize=None)(joint.joint_q_lower)
    hd = load(V47_HELPER, "joint_tset_selector_v47")
    direct = hd.load(hd.DIRECT, hd.DIRECT_BLOB, "joint_tset_selector_direct")
    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc, bnd, h21, h18, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx

    row_index = 22
    row_id, g0, d0 = rows[row_index]
    g, d = int(g0), int(d0)
    req((row_id, g, d) == ("g1-d192", 1, 192), "row22 identity drift")
    h = d // 2
    b = 36
    tq = (d * d + 16 * d + (32 if g == 0 else 0)) // 8
    shard = bc.build_joint_bc_shard(old.HMAX, b, b)

    qa_values = set()
    for aa in range(h + 1):
        if counter.component_a(d, aa) < 0:
            continue
        for sa in range(4):
            tiers = profiles[aa][sa]
            if tiers:
                qa_values.update(int(q) for q, _ in tiers if 0 <= int(q) <= tq)
    qa_values = sorted(qa_values)[-8:]
    req(bool(qa_values), "empty selector qA frontier")

    retained_exact_panel = {83, 85, 89}
    rows_out = []
    for c in range(h + 1):
        c3 = counter.component3(d, b, c)
        if c3 < 0:
            continue
        jbc = shard[b][c]
        active = []
        for sbc in range(8):
            for r in (0, 1):
                hist = {
                    int(q): int(w)
                    for q, w in jbc[sbc][r].items()
                    if int(w) and int(q) <= tq
                }
                if hist:
                    active.append((sbc, r, hist))
        if not active:
            continue

        points = hd.x4_points(h16, h, g, b, c)
        score = 0
        strict_count_states = 0
        strict_tset_states = 0
        max_removed_t = 0
        max_count_delta = 0
        qbc_states = 0

        for sbc, r, hist in active:
            parity = c & 1
            t_domain = tuple(range(parity, b + c + 1, 2))
            separate_floor = {
                t: separate_floor_fn(b, c, t, sbc)
                for t in t_domain
            }
            joint_floor = {
                t: joint_floor_fn(b, c, t, sbc)
                for t in t_domain
            }
            req(
                all(joint_floor[t] >= separate_floor[t] for t in t_domain),
                f"joint floor weakened separate floor {(c,sbc,r)}",
            )
            cache = {}
            for qbc in hist:
                separate = tuple(t for t in t_domain if separate_floor[t] <= qbc)
                joined = tuple(t for t in t_domain if joint_floor[t] <= qbc)
                req(bool(separate), f"histogram state lost separate t-set {(c,sbc,r,qbc)}")
                req(set(joined).issubset(separate), f"joint t-set escaped separate {(c,sbc,r,qbc)}")
                cache[qbc] = (separate, joined)
                qbc_states += 1
                if len(joined) < len(separate):
                    strict_tset_states += 1
                    max_removed_t = max(max_removed_t, len(separate) - len(joined))

            for qa in qa_values:
                xs = [x4 for x4, cap in points[r] if cap >= qa]
                if not xs:
                    continue
                for qbc, mult in hist.items():
                    if qa + qbc > tq:
                        continue
                    separate, joined = cache[qbc]
                    ec = exact_count(xs, d=d, g=g, vals=separate, q=qa + qbc)
                    jc = exact_count(xs, d=d, g=g, vals=joined, q=qa + qbc)
                    req(jc <= ec, f"joint selector weakened exact-set {(c,sbc,r,qbc,qa,jc,ec)}")
                    delta = ec - jc
                    if delta:
                        strict_count_states += 1
                        max_count_delta = max(max_count_delta, delta)
                        score += int(mult) * delta

        rows_out.append({
            "c": c,
            "already_in_retained_exact_panel": c in retained_exact_panel,
            "heuristic_joint_hist_x4_saving_score": str(score),
            "strict_joint_count_states": strict_count_states,
            "strict_joint_tset_states": strict_tset_states,
            "qbc_states": qbc_states,
            "max_removed_t_values": max_removed_t,
            "max_exact_minus_joint_x4_count": max_count_delta,
        })

    ranked = sorted(
        rows_out,
        key=lambda x: (
            int(x["heuristic_joint_hist_x4_saving_score"]),
            x["strict_joint_count_states"],
            x["strict_joint_tset_states"],
        ),
        reverse=True,
    )
    selected = [
        x["c"]
        for x in ranked
        if int(x["heuristic_joint_hist_x4_saving_score"]) > 0
        and not x["already_in_retained_exact_panel"]
    ][: args.top]
    req(bool(selected), "joint selector found no new c with positive heuristic tightening")

    out = {
        "schema": "STAGE32_32_01_178_V48_JOINT_TSET_C_PANEL_SELECTOR_V1",
        "status": "HEURISTIC_JOINT_MIN_SELECTOR_ONLY__ZERO_MAIN_CREDIT",
        "target": {"row_index": row_index, "row_id": row_id, "g": g, "d": d, "b": b},
        "selected_new_c": selected,
        "retained_exact_panel_c": sorted(retained_exact_panel),
        "top_rows": ranked[:16],
        "coverage": {
            "eligible_c_rows": len(rows_out),
            "selector_qa_values": len(qa_values),
            "selector_uses_highest_qA_tiers": True,
        },
        "semantics": {
            "selector_score_is_not_terminal_credit": True,
            "selector_omits_a_e_profile_weights": True,
            "exact_weighted_joint_cell_replay_required": True,
            "no_scaleout_authorization": True,
        },
        "timing": {"wall_seconds": time.perf_counter() - started},
        "firewalls": {
            "main_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge": False,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print("V48_JOINT_TSET_C_PANEL_SELECTOR=" + json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
