#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "stages/stage32-ex5/hpadj-15_ex5/derive_b_shard_row_exact_grf04_picard_capacity_bound.py"

PARENT_BLOB = "99ac15d18c83da050107ac7e8b113ae795ff0629"
Q_EXACT_HEAD = "6489e1fb9f35b8ecdc19c982301a816d956711e9"
Q_VERIFIER_BLOB = "373ed6768f22f94b2e0d82c1af514c7ce1833a0a"
Q_CANDIDATE_BLOB = "1d669114e930951b9d5f9f82a6abb2b59cd43884"
Q_CANDIDATE_CANON = "3fca63c0d678eb2de2147848a1aa29839618cfd9cb65bdd27d671b28c6e44b01"
Q_BENCHMARK = 195603649074545538415
HPADJ15_BENCHMARK = 426398981823116026011
PLANNED = ((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))
HMAX = 96


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


def load_module(path: Path, blob: str, name: str):
    req(path.is_file(), f"missing {name}")
    req(git_blob(path) == blob, f"{name} blob drift")
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {name}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def count_parity_upto(limit: int, parity: int) -> int:
    if limit < parity:
        return 0
    return (limit - parity) // 2 + 1


def build_bc_counts() -> list[list[int]]:
    """Independent replay of #1808 q-verifier relaxed canonical/parity counts keyed by (b,c)."""
    B = [[0, 0] for _ in range(HMAX + 1)]
    C = [[0, 0] for _ in range(HMAX + 1)]
    for m in range(HMAX + 1):
        for x9 in range(m + 1):
            B[m][x9 & 1] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                C[m][(x8 + x10) & 1] += 1

    pb = [[0] * (HMAX + 1) for _ in range(2)]
    for p in (0, 1):
        total = 0
        for m in range(HMAX + 1):
            total += B[m][p]
            pb[p][m] = total

    def sum_b(p: int, lo: int, hi: int) -> int:
        if lo > hi:
            return 0
        return pb[p][hi] - (pb[p][lo - 1] if lo else 0)

    eq_first = [[[0] * (HMAX + 1) for _ in range(HMAX + 1)] for __ in range(2)]
    eq_second = [[[0] * (HMAX + 1) for _ in range(HMAX + 1)] for __ in range(2)]
    for tp in (0, 1):
        for rb in range(HMAX + 1):
            for rc in range(HMAX + 1):
                total = 0
                for delta in range(1, rc + 1):
                    last_x5 = min(rb, rc - delta)
                    p = (tp + rb + delta) & 1
                    top = rc - delta
                    total += sum_b(p, top - last_x5, top)
                eq_first[tp][rb][rc] = total

                need_x10 = (tp + rb) & 1
                total = 0
                for u in range(min(rb, rc) + 1):
                    x9 = rb - u
                    rem = rc - u
                    limit_x6 = min(x9, rem)
                    need_x6 = (rem - need_x10) & 1
                    total += count_parity_upto(limit_x6, need_x6)
                eq_second[tp][rb][rc] = total

    bc = [[0] * (HMAX + 1) for _ in range(HMAX + 1)]
    for x0 in range(HMAX + 1):
        for x1 in range(x0 + 1, HMAX + 1):
            px1 = x1 & 1
            for b in range(x1, HMAX + 1):
                g2 = b - x1
                b0, b1 = B[g2]
                for c in range(x0, HMAX + 1):
                    c0, c1 = C[c - x0]
                    bc[b][c] += b0 * (c1 if px1 else c0) + b1 * (c0 if px1 else c1)

    for t in range(HMAX + 1):
        tp = t & 1
        for b in range(t, HMAX + 1):
            rb = b - t
            for c in range(t, HMAX + 1):
                rc = c - t
                bc[b][c] += eq_first[tp][rb][rc] + eq_second[tp][rb][rc]
    return bc


def f0(h: int, g: int, b: int, c: int, x4: int) -> int:
    D = h - 2 * x4
    d = 2 * h
    r4 = (3 * d * d + 48 * d + 96 - 96 * g) // 4
    return 3 * (
        6 * D * D - 8 * D * b - 6 * D * c + 18 * b * b + 4 * b * c + 13 * c * c
    ) - 23 * r4


def a0_interval(h: int, g: int, b: int, c: int) -> tuple[int, int] | None:
    n_min = 8 * h
    linear = -72 * h + 48 * b + 36 * c
    vertex = max(0, min(n_min, (-linear) // 144))
    best = vertex
    for z in (vertex - 1, vertex + 1):
        if 0 <= z <= n_min and f0(h, g, b, c, z) < f0(h, g, b, c, best):
            best = z
    if f0(h, g, b, c, best) > 0:
        return None

    if f0(h, g, b, c, 0) <= 0:
        left = 0
    else:
        lo, hi = 0, best
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if f0(h, g, b, c, mid) <= 0:
                hi = mid
            else:
                lo = mid
        left = hi

    req(f0(h, g, b, c, n_min) > 0, f"quadratic interval reaches N_min {(g,2*h,b,c)}")
    lo, hi = best, n_min
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if f0(h, g, b, c, mid) <= 0:
            lo = mid
        else:
            hi = mid
    return left, lo


def shard_for_b(b: int) -> tuple[int,int]:
    if b <= 83:
        lo = (b // 12) * 12
        return (lo, lo + 11)
    return (84, 96)


def exact_cell_masses(parent15):
    parent14 = parent15.load_parent()
    rejected = parent15.load_certificate(parent14)
    counter = parent14.load_counter()
    pre = parent15.exact_pre_shard_caps(parent14, counter)
    masses = {}
    pre_total = rejected_total = survivor_total = 0
    for rec in pre:
        interval = tuple(rec["b_interval"])
        g, d = int(rec["g"]), int(rec["d"])
        key = (interval, g, d)
        req(key in rejected, f"missing rejected cell {key}")
        P = int(rec["pre_terms"])
        R = int(rejected[key])
        req(0 <= R <= P, f"invalid rejected mass {key}")
        M = P - R
        req(key not in masses, f"duplicate mass cell {key}")
        masses[key] = M
        pre_total += P
        rejected_total += R
        survivor_total += M
    req(len(masses) == 178 * len(PLANNED), "cell mass coverage")
    req(pre_total == parent14.EXPECTED_PRE_TERMS, "pre-mass aggregate")
    req(rejected_total == parent14.EXPECTED_HPADJ08_REJECTED, "rejected-mass aggregate")
    req(survivor_total == parent14.EXPECTED_SURVIVOR_ENVELOPE, "survivor-mass aggregate")
    return masses, parent14


def optimize_cell(cap_by_ratio: dict[tuple[int,int], int], mass: int) -> tuple[Fraction, int, int]:
    total_capacity = sum(int(v) for v in cap_by_ratio.values())
    req(total_capacity >= mass, f"relaxed q capacity below exact cell mass: cap={total_capacity} mass={mass}")
    rem = mass
    obj = Fraction(0, 1)
    used_bins = 0
    items = sorted(cap_by_ratio.items(), key=lambda kv: Fraction(kv[0][0], kv[0][1]), reverse=True)
    for (s, B), cap in items:
        if rem == 0:
            break
        take = min(rem, int(cap))
        if take:
            obj += Fraction(int(s) * take, int(B))
            rem -= take
            used_bins += 1
    req(rem == 0, "q shard-mass LP did not cover exact cell mass")
    return obj, total_capacity, used_bins


def main() -> None:
    parent15 = load_module(PARENT, PARENT_BLOB, "hpadj15_locked_for_hpadj16")
    masses, parent14 = exact_cell_masses(parent15)
    req(parent15.HPADJ14_BENCHMARK == 463577241806597722598, "HPADJ15 parent benchmark drift")
    req(parent14.EXPECTED_SURVIVOR_ENVELOPE == 6703403803993209250491, "q/HPADJ envelope drift")

    bc = build_bc_counts()
    def prefix_total(h: int) -> int:
        acount = sum((a + 1) * (a + 2) // 2 for a in range(h + 1))
        bccount = sum(bc[b][c] for b in range(h + 1) for c in range(h + 1))
        return acount * bccount
    req(prefix_total(4) == 24010, "q h=4 canonical-prefix fixture")
    req(prefix_total(96) == 27398914615401945, "q h=96 canonical-prefix fixture")

    total_obj = Fraction(0, 1)
    cell_floor_sum = 0
    total_relaxed_capacity = 0
    nonzero_mass_cells = 0
    diagnostic = hashlib.sha256()
    seen = set()

    for g, hmax in ((0, 88), (1, 96)):
        for h in range(4, hmax + 1):
            d = 2 * h
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16 * g + 16, 4)
            e_lower = max(legacy, K, d - 4 * g + 4)
            if e_lower & 1:
                e_lower += 1
            e_upper = 3 * d

            hists = {interval: [[0] * (3 * h + 1) for _ in range(h + 2)] for interval in PLANNED}
            for b in range(h + 1):
                interval = shard_for_b(b)
                hist = hists[interval]
                for c in range(h + 1):
                    bc_count = bc[b][c]
                    if not bc_count:
                        continue
                    x4_interval = a0_interval(h, g, b, c)
                    if x4_interval is None:
                        continue
                    left, right = x4_interval
                    diff = [0] * (h + 2)
                    for x4 in range(left, right + 1):
                        room = -f0(h, g, b, c, x4)
                        req(room >= 0, "q interval construction regression")
                        amax = min(h, math.isqrt(room // 46))
                        diff[0] += 1
                        diff[amax + 1] -= 1
                    raw = 0
                    for a in range(h + 1):
                        raw += diff[a]
                        if raw <= 0:
                            break
                        s = (raw + 1) // 2
                        req(s < len(hist), "q survivor histogram overflow")
                        a_count = (a + 1) * (a + 2) // 2
                        hist[s][a + b + c] += a_count * bc_count

            for interval in PLANNED:
                key = (interval, g, d)
                req(key in masses, f"missing exact mass cell {key}")
                seen.add(key)
                M = int(masses[key])
                cap_by_ratio: dict[tuple[int,int], int] = defaultdict(int)
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
                        weight = prefix[min(e, 3 * h)]
                        if not weight:
                            continue
                        B = 19 * d - 5 * e + 1
                        req(B > 0, f"q normal block {(g,d,e)}")
                        cap_by_ratio[(s, B)] += int(weight) * B

                if M == 0:
                    obj = Fraction(0, 1)
                    relaxed_cap = sum(cap_by_ratio.values())
                    used_bins = 0
                else:
                    nonzero_mass_cells += 1
                    obj, relaxed_cap, used_bins = optimize_cell(cap_by_ratio, M)
                total_obj += obj
                cell_floor = obj.numerator // obj.denominator
                cell_floor_sum += cell_floor
                total_relaxed_capacity += relaxed_cap
                compact = {
                    "b_interval": list(interval), "g": g, "d": d,
                    "exact_post_hpadj08_mass": M,
                    "relaxed_q_capacity": relaxed_cap,
                    "used_ratio_bins": used_bins,
                    "cell_objective_numerator": obj.numerator,
                    "cell_objective_denominator": obj.denominator,
                    "cell_integer_upper": cell_floor,
                }
                diagnostic.update(json.dumps(compact, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(seen == set(masses), "q/certificate cell key-set mismatch")
    global_floor = total_obj.numerator // total_obj.denominator
    req(cell_floor_sum <= global_floor, "cellwise flooring direction regression")
    req(global_floor <= Q_BENCHMARK, "shard-mass LP weakened q benchmark")
    req(cell_floor_sum <= Q_BENCHMARK, "cellwise q bound weakened q benchmark")

    out = {
        "schema": "STAGE32EX5_HPADJ16_Q_QUADRATIC_B_SHARD_MASS_LP_BOUND_V1",
        "status": "Q_QUADRATIC_B_SHARD_EXACT_MASS_LP_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "route_id": "HPADJ-16_ex5",
        "source_locks": {
            "hpadj15_parent_blob_sha1": PARENT_BLOB,
            "main_q_quadratic_exact_source_head": Q_EXACT_HEAD,
            "main_q_quadratic_verifier_blob_sha1": Q_VERIFIER_BLOB,
            "main_q_quadratic_candidate_blob_sha1": Q_CANDIDATE_BLOB,
            "main_q_quadratic_candidate_canonical_sha256": Q_CANDIDATE_CANON,
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
            "main_q_quadratic_candidate_hostile_audited": False,
        },
        "exact_population_adapter": {
            "full178_rows": 178,
            "historical_b_shards": len(PLANNED),
            "row_shard_cells": 178 * len(PLANNED),
            "nonzero_exact_mass_cells": nonzero_mass_cells,
            "pre_hpadj08_replay_domain_terminals": parent14.EXPECTED_PRE_TERMS,
            "hpadj08_exact_square_rejected_terminals": parent14.EXPECTED_HPADJ08_REJECTED,
            "post_hpadj08_x4_complete_survivor_mass": parent14.EXPECTED_SURVIVOR_ENVELOPE,
            "exact_mass_fixed_separately_in_every_g_d_bshard_cell": True,
            "q_group_b_semantics": "x1+x5+x9",
            "hpadj15_b_shard_and_q_group_b_are_same_coordinate": True,
        },
        "quadratic_replay": {
            "D": "d/2-2*x4",
            "necessary_integer_inequality": "46*a^2 + 3*(6*D^2-8*D*b-6*D*c+18*b^2+4*b*c+13*c^2) <= 23*(R_g(d)/4)",
            "q_source_formula_reimplemented_independently_in_ex5": True,
            "q_source_bytes_imported_at_runtime": False,
            "canonical_prefix_fixtures_replayed": True,
        },
        "optimization": {
            "problem": "Maximize the q-quadratic survivor objective independently in every exact (g,d,b-shard) cell, with q relaxed-bin capacities and the exact post-HPADJ08 cell mass fixed.",
            "cell_solution": "Sort bounded relaxed bins by exact ratio s/B descending and fill exact integer terminal mass greedily; this is the exact bounded unit-mass LP optimum in each cell.",
            "integer_strengthening": "Actual survivor count is integral in every disjoint cell, so floor each cell rational optimum before summing.",
            "aggregate_relaxed_q_capacity": total_relaxed_capacity,
            "aggregate_rational_objective_numerator": total_obj.numerator,
            "aggregate_rational_objective_denominator": total_obj.denominator,
            "aggregate_rational_floor": global_floor,
            "cellwise_integer_floor_sum": cell_floor_sum,
            "diagnostic_stream_sha256": diagnostic.hexdigest(),
        },
        "candidate_bound": {
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
            "hpadj15_candidate_upper_bound": HPADJ15_BENCHMARK,
            "hpadj16_candidate_upper_bound": cell_floor_sum,
            "improvement_vs_main_q_quadratic_global": Q_BENCHMARK - cell_floor_sum,
            "improvement_vs_hpadj15": HPADJ15_BENCHMARK - cell_floor_sum,
            "strict_improvement_vs_main_q_quadratic_global": cell_floor_sum < Q_BENCHMARK,
            "composition_if_consumed": "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        },
        "semantics": {
            "same_hpadj08_td01_x4_complete_population": True,
            "same_b_coordinate_adapter_proved_by_formula_identity": True,
            "q_quadratic_candidate_credit_inherited": False,
            "statistical_independence_assumed": False,
            "additive_subtraction_used": False,
            "exact_incremental_rejected_identity_set_claimed": False,
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
