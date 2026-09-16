#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "stages/stage32-ex5/hpadj-16_ex5/derive_q_quadratic_b_shard_mass_lp_bound.py"
PARENT_BLOB = "61805f8b6d661c29805b6966e2453ed411d73189"
Q_BENCHMARK = 195603649074545538415
HPADJ15_BENCHMARK = 426398981823116026011
PLANNED = ((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_parent():
    req(PARENT.is_file() and git_blob(PARENT) == PARENT_BLOB, "HPADJ16 parent blob drift")
    spec = importlib.util.spec_from_file_location("hpadj16_locked_for_hpadj17", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ16 parent")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def exact_cells(h16):
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_hpadj17")
    p14 = p15.load_parent()
    rejected = p15.load_certificate(p14)
    counter = p14.load_counter()
    pre = p15.exact_pre_shard_caps(p14, counter)
    cells = {}
    pre_total = rejected_total = post_total = 0
    for rec in pre:
        interval = tuple(rec["b_interval"])
        g, d = int(rec["g"]), int(rec["d"])
        key = (interval, g, d)
        req(key in rejected, f"missing rejection cell {key}")
        P = int(rec["pre_terms"])
        R = int(rejected[key])
        req(0 <= R <= P, f"invalid rejected mass {key}")
        e_caps = {int(e): int(n) * (19*d - 5*int(e) + 1) for e, n in rec["caps"].items()}
        req(sum(e_caps.values()) == P, f"exact pre-e capacity sum drift {key}")
        req(key not in cells, f"duplicate exact cell {key}")
        cells[key] = {"post_mass": P-R, "pre_mass": P, "rejected_mass": R, "pre_e_term_caps": e_caps}
        pre_total += P
        rejected_total += R
        post_total += P-R
    req(len(cells) == 178 * len(PLANNED), "exact cell coverage")
    req(pre_total == p14.EXPECTED_PRE_TERMS, "pre aggregate")
    req(rejected_total == p14.EXPECTED_HPADJ08_REJECTED, "rejected aggregate")
    req(post_total == p14.EXPECTED_SURVIVOR_ENVELOPE, "post aggregate")
    return cells, p14


def optimize_cell_with_e_caps(raw_by_e: dict[int, dict[tuple[int,int], int]], info: dict) -> tuple[Fraction,int,int,int]:
    effective: dict[tuple[int,int], int] = defaultdict(int)
    positive_effective = 0
    exact_pre_mass = int(info["pre_mass"])
    exact_post_mass = int(info["post_mass"])
    e_caps = info["pre_e_term_caps"]

    # For each e, actual pre-HPADJ08 terminal mass cannot exceed its exact pre-domain mass.
    # To maximize q survivors under that cap, retain the highest s/B relaxed bins first.
    for e, pre_cap in e_caps.items():
        rem = int(pre_cap)
        bins = raw_by_e.get(int(e), {})
        for (s, B), cap in sorted(bins.items(), key=lambda kv: Fraction(kv[0][0], kv[0][1]), reverse=True):
            if rem == 0:
                break
            take = min(rem, int(cap))
            if take:
                effective[(int(s), int(B))] += take
                positive_effective += take
                rem -= take
        # Any exact pre mass not coverable by positive q bins has survivor ratio zero.
        if rem:
            effective[(0, 1)] += rem

    # If an e is absent from the exact pre-domain, its relaxed q bins carry zero actual mass.
    req(sum(effective.values()) == exact_pre_mass, "effective exact-pre capacity conservation")
    req(exact_post_mass <= exact_pre_mass, "post mass exceeds exact pre mass")

    rem = exact_post_mass
    obj = Fraction(0, 1)
    used = 0
    for (s, B), cap in sorted(effective.items(), key=lambda kv: Fraction(kv[0][0], kv[0][1]), reverse=True):
        if rem == 0:
            break
        take = min(rem, int(cap))
        if take:
            obj += Fraction(int(s) * take, int(B))
            rem -= take
            used += 1
    req(rem == 0, "effective e-capped bins do not cover exact post mass")
    return obj, exact_pre_mass, positive_effective, used


def main() -> None:
    h16 = load_parent()
    cells, p14 = exact_cells(h16)
    bc = h16.build_bc_counts()

    def prefix_total(h: int) -> int:
        acount = sum((a + 1) * (a + 2) // 2 for a in range(h + 1))
        bccount = sum(bc[b][c] for b in range(h + 1) for c in range(h + 1))
        return acount * bccount
    req(prefix_total(4) == 24010, "q h=4 canonical-prefix fixture")
    req(prefix_total(96) == 27398914615401945, "q h=96 canonical-prefix fixture")

    total_obj = Fraction(0, 1)
    cell_floor_sum = 0
    exact_pre_capacity_total = 0
    positive_effective_total = 0
    nonzero_post_cells = 0
    diagnostic = hashlib.sha256()
    seen = set()

    for g, hmax in ((0, 88), (1, 96)):
        for h in range(4, hmax + 1):
            d = 2 * h
            legacy = 8 if g == 0 else 4
            K = h16.ceil_div(d - 16*g + 16, 4)
            e_lower = max(legacy, K, d - 4*g + 4)
            if e_lower & 1:
                e_lower += 1
            e_upper = 3*d

            hists = {interval: [[0] * (3*h + 1) for _ in range(h + 2)] for interval in PLANNED}
            for b in range(h + 1):
                interval = h16.shard_for_b(b)
                hist = hists[interval]
                for c in range(h + 1):
                    bc_count = bc[b][c]
                    if not bc_count:
                        continue
                    xr = h16.a0_interval(h, g, b, c)
                    if xr is None:
                        continue
                    left, right = xr
                    diff = [0] * (h + 2)
                    for x4 in range(left, right + 1):
                        room = -h16.f0(h, g, b, c, x4)
                        req(room >= 0, "q interval construction regression")
                        amax = min(h, __import__('math').isqrt(room // 46))
                        diff[0] += 1
                        diff[amax + 1] -= 1
                    raw = 0
                    for a in range(h + 1):
                        raw += diff[a]
                        if raw <= 0:
                            break
                        s = (raw + 1) // 2
                        req(s < len(hist), "q survivor histogram overflow")
                        hist[s][a+b+c] += ((a+1)*(a+2)//2) * bc_count

            for interval in PLANNED:
                key = (interval, g, d)
                req(key in cells, f"missing exact cell {key}")
                seen.add(key)
                info = cells[key]
                raw_by_e: dict[int, dict[tuple[int,int], int]] = defaultdict(lambda: defaultdict(int))
                hist = hists[interval]
                for s in range(1, len(hist)):
                    row = hist[s]
                    if not any(row):
                        continue
                    prefix = []
                    acc = 0
                    for value in row:
                        acc += value
                        prefix.append(acc)
                    for e in range(e_lower, e_upper + 1, 2):
                        if g == 1 and d == 8 and e == 8:
                            continue
                        weight = prefix[min(e, 3*h)]
                        if not weight:
                            continue
                        B = 19*d - 5*e + 1
                        req(B > 0, f"q normal block {(g,d,e)}")
                        raw_by_e[e][(s,B)] += int(weight) * B

                obj, pre_cap, pos_cap, used = optimize_cell_with_e_caps(raw_by_e, info)
                if int(info["post_mass"]):
                    nonzero_post_cells += 1
                total_obj += obj
                cell_floor = obj.numerator // obj.denominator
                cell_floor_sum += cell_floor
                exact_pre_capacity_total += pre_cap
                positive_effective_total += pos_cap
                compact = {
                    "b_interval": list(interval), "g": g, "d": d,
                    "exact_pre_mass": int(info["pre_mass"]),
                    "exact_post_mass": int(info["post_mass"]),
                    "exact_e_bins": len(info["pre_e_term_caps"]),
                    "positive_q_effective_capacity_after_e_caps": pos_cap,
                    "used_ratio_bins": used,
                    "cell_objective_numerator": obj.numerator,
                    "cell_objective_denominator": obj.denominator,
                    "cell_integer_upper": cell_floor,
                }
                diagnostic.update(json.dumps(compact, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(seen == set(cells), "cell key-set mismatch")
    req(exact_pre_capacity_total == p14.EXPECTED_PRE_TERMS, "effective pre capacity aggregate")
    global_floor = total_obj.numerator // total_obj.denominator
    req(cell_floor_sum <= global_floor, "cellwise floor direction")
    req(global_floor <= Q_BENCHMARK, "e-capped LP weakened global q candidate")
    req(cell_floor_sum <= Q_BENCHMARK, "e-capped cellwise bound weakened global q candidate")

    out = {
        "schema": "STAGE32EX5_HPADJ17_Q_QUADRATIC_B_SHARD_E_CAPACITY_LP_BOUND_V1",
        "status": "Q_QUADRATIC_B_SHARD_EXACT_MASS_AND_E_CAPACITY_LP_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "route_id": "HPADJ-17_ex5",
        "source_locks": {
            "hpadj16_parent_blob_sha1": PARENT_BLOB,
            "main_q_quadratic_exact_source_head": h16.Q_EXACT_HEAD,
            "main_q_quadratic_verifier_blob_sha1": h16.Q_VERIFIER_BLOB,
            "main_q_quadratic_candidate_blob_sha1": h16.Q_CANDIDATE_BLOB,
            "main_q_quadratic_candidate_canonical_sha256": h16.Q_CANDIDATE_CANON,
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
            "main_q_quadratic_candidate_hostile_audited": False,
        },
        "exact_population_adapter": {
            "row_shard_cells": 178 * len(PLANNED),
            "nonzero_post_mass_cells": nonzero_post_cells,
            "post_hpadj08_x4_complete_survivor_mass": p14.EXPECTED_SURVIVOR_ENVELOPE,
            "pre_hpadj08_exact_terminal_mass": p14.EXPECTED_PRE_TERMS,
            "exact_post_mass_fixed_by_g_d_bshard": True,
            "exact_pre_mass_cap_fixed_by_g_d_bshard_e": True,
            "q_group_b_semantics": "x1+x5+x9",
            "hpadj_b_shard_and_q_group_b_same_coordinate": True,
        },
        "optimization": {
            "first_stage": "Within each exact e cap, keep highest q survivor-ratio capacity first; unused exact pre mass is assigned ratio zero.",
            "second_stage": "Within each (g,d,b-shard) cell, fill the exact post-HPADJ08 mass from the resulting bounded ratios in descending order.",
            "integer_strengthening": "Floor each disjoint cell rational survivor optimum before summing.",
            "aggregate_exact_pre_capacity": exact_pre_capacity_total,
            "aggregate_positive_q_effective_capacity_after_e_caps": positive_effective_total,
            "aggregate_rational_objective_numerator": total_obj.numerator,
            "aggregate_rational_objective_denominator": total_obj.denominator,
            "aggregate_rational_floor": global_floor,
            "cellwise_integer_floor_sum": cell_floor_sum,
            "diagnostic_stream_sha256": diagnostic.hexdigest(),
        },
        "candidate_bound": {
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
            "hpadj15_candidate_upper_bound": HPADJ15_BENCHMARK,
            "hpadj17_candidate_upper_bound": cell_floor_sum,
            "improvement_vs_main_q_quadratic_global": Q_BENCHMARK - cell_floor_sum,
            "improvement_vs_hpadj15": HPADJ15_BENCHMARK - cell_floor_sum,
            "strict_improvement_vs_main_q_quadratic_global": cell_floor_sum < Q_BENCHMARK,
            "composition_if_consumed": "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        },
        "semantics": {
            "same_hpadj08_td01_x4_complete_population": True,
            "q_quadratic_source_credit_inherited": False,
            "statistical_independence_assumed": False,
            "additive_subtraction_used": False,
            "main_consumption_performed": False,
            "hostile_audit_required_before_main_handoff_or_consumption": True,
            "new_heavy_run_used": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


if __name__ == "__main__":
    main()
