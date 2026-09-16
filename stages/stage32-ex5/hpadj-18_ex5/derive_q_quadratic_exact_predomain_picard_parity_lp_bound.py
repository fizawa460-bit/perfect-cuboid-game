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
PARENT = ROOT / "stages/stage32-ex5/hpadj-17_ex5/derive_q_quadratic_b_shard_e_capacity_lp_bound.py"
PARENT_BLOB = "10c1a836136f66b716ad39f6ca74250e32f386a9"
Q_BENCHMARK = 195603649074545538415
HPADJ15_BENCHMARK = 426398981823116026011
PLANNED = ((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))
Q_AUDITED_HEAD = "6489e1fb9f35b8ecdc19c982301a816d956711e9"
Q_AUDIT_REVIEW_NODE = "PRR_kwDOTr52Y88AAAABNv6cog"


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
    req(PARENT.is_file() and git_blob(PARENT) == PARENT_BLOB, "HPADJ17 parent blob drift")
    spec = importlib.util.spec_from_file_location("hpadj17_locked_for_hpadj18", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ17 parent")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def parity_q_survivors(h16, h: int, g: int, b: int, c: int) -> list[tuple[int, int]]:
    """For every exact a, count q-feasible x4 in the required parity classes r=0,1."""
    out = [(0, 0) for _ in range(h + 1)]
    xr = h16.a0_interval(h, g, b, c)
    if xr is None:
        return out
    left, right = xr
    diffs = [[0] * (h + 2), [0] * (h + 2)]
    for x4 in range(left, right + 1):
        room = -h16.f0(h, g, b, c, x4)
        req(room >= 0, "q interval construction regression")
        amax = min(h, math.isqrt(room // 46))
        p = x4 & 1
        diffs[p][0] += 1
        diffs[p][amax + 1] -= 1
    run = [0, 0]
    vals = []
    for a in range(h + 1):
        run[0] += diffs[0][a]
        run[1] += diffs[1][a]
        vals.append((run[0], run[1]))
    return vals


def optimize_cell_exact_predomain(cap_by_ratio: dict[tuple[int, int], int], mass: int) -> tuple[Fraction, int, int, int]:
    total_capacity = sum(int(v) for v in cap_by_ratio.values())
    req(0 <= mass <= total_capacity, f"post mass outside exact pre capacity: mass={mass} cap={total_capacity}")
    rem = int(mass)
    obj = Fraction(0, 1)
    used = 0
    positive_capacity = 0
    for (s, B), cap in sorted(
        cap_by_ratio.items(),
        key=lambda kv: Fraction(kv[0][0], kv[0][1]),
        reverse=True,
    ):
        if s:
            positive_capacity += int(cap)
        if rem == 0:
            continue
        take = min(rem, int(cap))
        if take:
            obj += Fraction(int(s) * take, int(B))
            rem -= take
            used += 1
    req(rem == 0, "exact-predomain LP failed to cover post mass")
    return obj, total_capacity, positive_capacity, used


def main() -> None:
    h17 = load_parent()
    h16 = h17.load_parent()
    cells, p14 = h17.exact_cells(h16)
    counter = p14.load_counter()

    req(h16.Q_EXACT_HEAD == Q_AUDITED_HEAD, "q audited-head identity drift")
    req(h16.Q_BENCHMARK == Q_BENCHMARK, "q benchmark drift")
    req(p14.EXPECTED_SURVIVOR_ENVELOPE == 6703403803993209250491, "survivor envelope drift")

    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178, "FULL178 row coverage")
    H = max(d // 2 for _, _, d in rows)
    req(H == 96, "FULL178 hmax drift")
    BC = counter.build_bc_exact_parity(H)

    total_obj = Fraction(0, 1)
    cell_floor_sum = 0
    total_pre_terms = 0
    total_pre_blocks = 0
    positive_q_capacity = 0
    nonzero_post_cells = 0
    strict_parity_split_states = 0
    diagnostic = hashlib.sha256()
    seen = set()

    for row_id, g, d in rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = counter.ceil_div(d - 16 * g + 16, 4)
        A = [[counter.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
        cell_caps = {interval: defaultdict(int) for interval in PLANNED}
        cell_blocks = {interval: 0 for interval in PLANNED}

        for b in range(h + 1):
            interval = h16.shard_for_b(b)
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv):
                    continue
                c3 = counter.component3(d, b, c)
                if c3 < 0:
                    continue
                qsurv = parity_q_survivors(h16, h, g, b, c)

                for a in range(h + 1):
                    avec = A[a]
                    if not any(avec):
                        continue
                    M = a + b + c
                    ca = counter.component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3
                    s0, s1 = qsurv[a]
                    if s0 != s1:
                        strict_parity_split_states += 1

                    for sbc, pair in enumerate(bcv):
                        for r in (0, 1):
                            left_count = int(pair[r])
                            if not left_count:
                                continue
                            q_s = s0 if r == 0 else s1
                            for sa, right_count in enumerate(avec):
                                if not right_count:
                                    continue
                                support = sbc + sa
                                count = left_count * int(right_count)
                                qneed = K - support
                                if qneed > 0 and srem < qneed:
                                    continue

                                lower = max(legacy, K, d - 4 * g + 4, M, M + max(0, qneed))
                                upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
                                if lower > upper:
                                    continue
                                excluded = set()
                                e_n358 = 3 * d - (b - c)
                                if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                                    excluded.add(e_n358)
                                if g == 1 and d == 8:
                                    excluded.add(8)

                                lo = lower if lower % 2 == 0 else lower + 1
                                hi = upper if upper % 2 == 0 else upper - 1
                                if lo > hi:
                                    continue
                                for e in range(lo, hi + 1, 2):
                                    if e in excluded:
                                        continue
                                    B = 19 * d - 5 * e + 1
                                    req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,e,B)}")
                                    req(B - 1 >= 8 * h, f"q interval domain too short {(g,d,e,B)}")
                                    cell_blocks[interval] += count
                                    cell_caps[interval][(int(q_s), int(B))] += count * B

        for interval in PLANNED:
            key = (interval, int(g), int(d))
            req(key in cells, f"missing exact post-mass cell {key}")
            seen.add(key)
            info = cells[key]
            Mpost = int(info["post_mass"])
            Pexact = int(info["pre_mass"])
            pre_cap_here = sum(cell_caps[interval].values())
            req(pre_cap_here == Pexact, f"exact pre-domain terminal mass mismatch {key}: {pre_cap_here} != {Pexact}")

            blocks_here = int(cell_blocks[interval])
            recovered_blocks = 0
            for e, term_cap in info["pre_e_term_caps"].items():
                B = 19 * d - 5 * int(e) + 1
                req(int(term_cap) % B == 0, f"pre-e term cap not block-divisible {key,e}")
                recovered_blocks += int(term_cap) // B
            req(blocks_here == recovered_blocks, f"exact pre-domain block mass mismatch {key}")

            obj, cap, poscap, used = optimize_cell_exact_predomain(cell_caps[interval], Mpost)
            if Mpost:
                nonzero_post_cells += 1
            total_obj += obj
            cell_floor = obj.numerator // obj.denominator
            cell_floor_sum += cell_floor
            total_pre_terms += cap
            total_pre_blocks += blocks_here
            positive_q_capacity += poscap

            compact = {
                "row_id": row_id,
                "b_interval": list(interval),
                "g": int(g),
                "d": int(d),
                "exact_pre_mass": Pexact,
                "exact_pre_blocks": blocks_here,
                "exact_post_mass": Mpost,
                "ratio_bin_count": len(cell_caps[interval]),
                "positive_q_terminal_capacity": poscap,
                "used_ratio_bins": used,
                "cell_objective_numerator": obj.numerator,
                "cell_objective_denominator": obj.denominator,
                "cell_integer_upper": cell_floor,
            }
            diagnostic.update(json.dumps(compact, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(seen == set(cells), "exact cell key-set mismatch")
    req(total_pre_terms == p14.EXPECTED_PRE_TERMS, "exact pre terminal aggregate")
    req(total_pre_blocks == p14.EXPECTED_PRE_BLOCKS, "exact pre block aggregate")
    global_floor = total_obj.numerator // total_obj.denominator
    req(cell_floor_sum <= global_floor, "cellwise floor direction")
    req(global_floor <= Q_BENCHMARK, "exact-predomain parity LP weakened q benchmark")
    req(cell_floor_sum <= Q_BENCHMARK, "exact-predomain parity cellwise bound weakened q benchmark")

    out = {
        "schema": "STAGE32EX5_HPADJ18_Q_QUADRATIC_EXACT_PREDOMAIN_PICARD_PARITY_LP_BOUND_V1",
        "status": "Q_QUADRATIC_EXACT_PREDOMAIN_PICARD_PARITY_LP_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "route_id": "HPADJ-18_ex5",
        "source_locks": {
            "hpadj17_parent_blob_sha1": PARENT_BLOB,
            "main_q_quadratic_exact_source_head": Q_AUDITED_HEAD,
            "main_q_quadratic_candidate_blob_sha1": h16.Q_CANDIDATE_BLOB,
            "main_q_quadratic_verifier_blob_sha1": h16.Q_VERIFIER_BLOB,
            "main_q_quadratic_candidate_hostile_audit_status": "PASS",
            "main_q_quadratic_hostile_audit_review_node": Q_AUDIT_REVIEW_NODE,
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
        },
        "exact_population_adapter": {
            "full178_rows": 178,
            "historical_b_shards": len(PLANNED),
            "row_shard_cells": 178 * len(PLANNED),
            "nonzero_post_mass_cells": nonzero_post_cells,
            "pre_hpadj08_exact_terminal_mass": total_pre_terms,
            "pre_hpadj08_exact_block_mass": total_pre_blocks,
            "post_hpadj08_x4_complete_survivor_mass": p14.EXPECTED_SURVIVOR_ENVELOPE,
            "exact_pre_domain_replayed_by_a_b_c_support_e_picard_parity": True,
            "picard_character": "x4 == x0+x8+x10 (mod 2)",
            "bc_exact_parity_coordinate": "r=(x0+x8+x10) mod 2",
            "q_group_b_semantics": "x1+x5+x9",
            "unknown_hpadj08_removed_block_identity_assumed": False,
        },
        "quadratic_refinement": {
            "necessary_integer_inequality": "46*a^2 + 3*(6*D^2-8*D*b-6*D*c+18*b^2+4*b*c+13*c^2) <= 23*(R_g(d)/4)",
            "D": "d/2-2*x4",
            "q_survivors_counted_in_the_actual_required_picard_parity_class": True,
            "relaxed_global_prefix_capacity_replaced_by_exact_pre_domain_prefix_capacity": True,
            "parity_split_observed_state_count": strict_parity_split_states,
            "q_interval_closes_before_universal_actual_block_minimum": True,
        },
        "optimization": {
            "problem": "For every exact (g,d,b-shard) cell, maximize q-and-Picard survivors over the exact pre-HPADJ08 block capacity while fixing only the certified post-HPADJ08 terminal mass; deleted-block identity is left adversarial.",
            "relaxation": "Whole-block survival is relaxed to fractional terminal mass within each exact block-ratio bin, so the optimum remains an upper bound.",
            "cell_solution": "Sort exact pre-domain block capacities by s/B descending and fill the certified post mass greedily.",
            "integer_strengthening": "Floor each disjoint cell rational optimum before summing.",
            "aggregate_positive_q_terminal_capacity": positive_q_capacity,
            "aggregate_rational_objective_numerator": total_obj.numerator,
            "aggregate_rational_objective_denominator": total_obj.denominator,
            "aggregate_rational_floor": global_floor,
            "cellwise_integer_floor_sum": cell_floor_sum,
            "diagnostic_stream_sha256": diagnostic.hexdigest(),
        },
        "candidate_bound": {
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
            "hpadj15_candidate_upper_bound": HPADJ15_BENCHMARK,
            "hpadj18_candidate_upper_bound": cell_floor_sum,
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
