#!/usr/bin/env python3
from __future__ import annotations

import bisect
import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "stages/stage32-ex5/hpadj-19_ex5/derive_exact_support_qa_predomain_picard_lp_bound.py"
PARENT_BLOB = "fdf5c721121d549361b08a92694373f3df7d02c8"
Q_BENCHMARK = 195603649074545538415
HPADJ15_BENCHMARK = 426398981823116026011


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
    req(PARENT.is_file() and git_blob(PARENT) == PARENT_BLOB, "HPADJ19 parent blob drift")
    spec = importlib.util.spec_from_file_location("hpadj19_locked_for_hpadj20", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ19 parent")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_two_tier_profiles(H: int, counter, h19):
    """For each exact (a,support), retain min-qA tuples and a certified second tier.

    Tier 1 is the exact minimum qA with its exact multiplicity.  Tier 2 contains
    every remaining ordered triple and uses the exact second-smallest qA as a
    common lower bound.  This preserves population exactly while strictly
    refining the HPADJ19 rule that gives every tuple the minimum qA.
    """
    profiles = [[[] for _ in range(4)] for __ in range(H + 1)]
    exact_hist_class_count = 0
    strict_two_tier_class_count = 0
    nonminimum_tuple_count = 0

    for a in range(H + 1):
        hist = [defaultdict(int) for _ in range(4)]
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                s = int(x2 > 0) + int(x3 > 0) + int(x7 > 0)
                qA = x2 * x2 + x3 * x3 + x7 * x7
                hist[s][qA] += 1

        for s in range(4):
            expected = int(counter.triple_free_count(a, s))
            got = sum(hist[s].values())
            req(got == expected, f"A histogram multiplicity drift {(a,s)}: {got} != {expected}")
            if not expected:
                continue
            exact_hist_class_count += 1
            keys = sorted(hist[s])
            q0 = int(keys[0])
            req(q0 == int(h19.qa_min_for_mass_support(a, s)), f"A minimum drift {(a,s)}")
            m0 = int(hist[s][q0])
            req(0 < m0 <= expected, f"A minimum multiplicity drift {(a,s)}")
            if len(keys) == 1:
                profiles[a][s] = [(q0, expected)]
                continue
            q1 = int(keys[1])
            rest = expected - m0
            req(q1 > q0 and rest > 0, f"A second-tier drift {(a,s)}")
            profiles[a][s] = [(q0, m0), (q1, rest)]
            strict_two_tier_class_count += 1
            nonminimum_tuple_count += rest

    req(strict_two_tier_class_count > 0 and nonminimum_tuple_count > 0,
        "two-tier A profile has no strict refinement classes")
    return profiles, exact_hist_class_count, strict_two_tier_class_count, nonminimum_tuple_count


def survivor_profiles(h16, h19, profiles, h: int, g: int, b: int, c: int):
    """Return HPADJ19 parent survivor counts and HPADJ20 two-tier multiplicities."""
    caps = [[], []]
    xr = h16.a0_interval(h, g, b, c)
    if xr is not None:
        left, right = xr
        for x4 in range(left, right + 1):
            room = -h16.f0(h, g, b, c, x4)
            req(room >= 0, "two-tier q interval construction regression")
            caps[x4 & 1].append(room // 138)
    caps[0].sort()
    caps[1].sort()

    out = [[None for _ in range(4)] for __ in range(h + 1)]
    strict_survivor_tiers = 0
    for a in range(h + 1):
        for s in range(4):
            tiers = profiles[a][s]
            if not tiers:
                continue
            qmin = int(h19.qa_min_for_mass_support(a, s))
            parent = tuple(len(caps[r]) - bisect.bisect_left(caps[r], qmin) for r in (0, 1))
            grouped = defaultdict(int)
            for qlower, mult in tiers:
                surv = tuple(len(caps[r]) - bisect.bisect_left(caps[r], int(qlower)) for r in (0, 1))
                req(surv[0] <= parent[0] and surv[1] <= parent[1],
                    f"two-tier survivor dominance drift {(h,g,b,c,a,s,qlower)}")
                if surv[0] < parent[0] or surv[1] < parent[1]:
                    strict_survivor_tiers += 1
                grouped[surv] += int(mult)
            req(sum(grouped.values()) == sum(mult for _, mult in tiers),
                f"two-tier grouped multiplicity drift {(a,s)}")
            out[a][s] = {
                "parent": parent,
                "tiers": [(int(k[0]), int(k[1]), int(v)) for k, v in sorted(grouped.items())],
            }
    return out, strict_survivor_tiers


def main() -> None:
    h19 = load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    cells, p14 = h17.exact_cells(h16)
    counter = p14.load_counter()

    req(h19.Q_BENCHMARK == Q_BENCHMARK, "HPADJ19 q benchmark drift")
    req(h19.HPADJ15_BENCHMARK == HPADJ15_BENCHMARK, "HPADJ19 HPADJ15 benchmark drift")
    req(p14.EXPECTED_SURVIVOR_ENVELOPE == 6703403803993209250491, "survivor envelope drift")

    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178, "FULL178 row coverage")
    H = max(d // 2 for _, _, d in rows)
    req(H == 96, "FULL178 hmax drift")
    BC = counter.build_bc_exact_parity(H)
    profiles, hist_classes, strict_profile_classes, nonminimum_tuples = build_two_tier_profiles(H, counter, h19)

    total_obj = Fraction(0, 1)
    parent_total_obj = Fraction(0, 1)
    cell_floor_sum = 0
    parent_cell_floor_sum = 0
    total_pre_terms = 0
    total_pre_blocks = 0
    positive_q_capacity = 0
    parent_positive_q_capacity = 0
    nonzero_post_cells = 0
    strict_survivor_tiers = 0
    strict_cell_count = 0
    diagnostic = hashlib.sha256()
    seen = set()

    for row_id, g, d in rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = counter.ceil_div(d - 16 * g + 16, 4)
        A = [[sum(mult for _, mult in profiles[a][sa]) for sa in range(4)] for a in range(h + 1)]
        req(all(A[a][sa] == counter.triple_free_count(a, sa) for a in range(h + 1) for sa in range(4)),
            f"A profile population mismatch row {row_id}")
        cell_caps = {interval: defaultdict(int) for interval in h18.PLANNED}
        parent_caps = {interval: defaultdict(int) for interval in h18.PLANNED}
        cell_blocks = {interval: 0 for interval in h18.PLANNED}

        for b in range(h + 1):
            interval = h16.shard_for_b(b)
            for c in range(h + 1):
                bcv = BC[b][c]
                if not any(any(pair) for pair in bcv):
                    continue
                c3 = counter.component3(d, b, c)
                if c3 < 0:
                    continue
                qsurv, strict_here = survivor_profiles(h16, h19, profiles, h, g, b, c)
                strict_survivor_tiers += strict_here

                for a in range(h + 1):
                    avec = A[a]
                    if not any(avec):
                        continue
                    M = a + b + c
                    ca = counter.component_a(d, a)
                    if ca < 0:
                        continue
                    srem = min(16, d) + ca + c3

                    for sbc, pair in enumerate(bcv):
                        for r in (0, 1):
                            left_count = int(pair[r])
                            if not left_count:
                                continue
                            for sa, right_total in enumerate(avec):
                                if not right_total:
                                    continue
                                qinfo = qsurv[a][sa]
                                req(qinfo is not None, f"missing q profile {(a,sa)}")
                                req(sum(v[2] for v in qinfo["tiers"]) == int(right_total),
                                    f"q tier population mismatch {(a,sa)}")
                                parent_q = int(qinfo["parent"][r])
                                support = sbc + sa
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
                                    parent_count = left_count * int(right_total)
                                    cell_blocks[interval] += parent_count
                                    parent_caps[interval][(parent_q, B)] += parent_count * B
                                    tier_count = 0
                                    for s0, s1, mult in qinfo["tiers"]:
                                        q_s = s0 if r == 0 else s1
                                        count = left_count * int(mult)
                                        tier_count += count
                                        cell_caps[interval][(int(q_s), B)] += count * B
                                    req(tier_count == parent_count, "two-tier block population drift")

        for interval in h18.PLANNED:
            key = (interval, int(g), int(d))
            req(key in cells, f"missing exact post-mass cell {key}")
            seen.add(key)
            info = cells[key]
            Mpost = int(info["post_mass"])
            Pexact = int(info["pre_mass"])
            pre_cap_here = sum(cell_caps[interval].values())
            parent_cap_here = sum(parent_caps[interval].values())
            req(pre_cap_here == Pexact, f"HPADJ20 exact pre-domain terminal mass mismatch {key}: {pre_cap_here} != {Pexact}")
            req(parent_cap_here == Pexact, f"HPADJ19 replay pre-domain terminal mass mismatch {key}: {parent_cap_here} != {Pexact}")

            blocks_here = int(cell_blocks[interval])
            recovered_blocks = 0
            for e, term_cap in info["pre_e_term_caps"].items():
                B = 19 * d - 5 * int(e) + 1
                req(int(term_cap) % B == 0, f"pre-e term cap not block-divisible {key,e}")
                recovered_blocks += int(term_cap) // B
            req(blocks_here == recovered_blocks, f"exact pre-domain block mass mismatch {key}")

            obj, cap, poscap, used = h18.optimize_cell_exact_predomain(cell_caps[interval], Mpost)
            pobj, pcap, pposcap, pused = h18.optimize_cell_exact_predomain(parent_caps[interval], Mpost)
            req(cap == pcap == Pexact, f"LP capacity mismatch {key}")
            req(obj <= pobj, f"two-tier LP weakened HPADJ19 replay {key}")
            if obj < pobj:
                strict_cell_count += 1
            if Mpost:
                nonzero_post_cells += 1
            total_obj += obj
            parent_total_obj += pobj
            cell_floor = obj.numerator // obj.denominator
            parent_cell_floor = pobj.numerator // pobj.denominator
            req(cell_floor <= parent_cell_floor, f"cell floor weakened HPADJ19 replay {key}")
            cell_floor_sum += cell_floor
            parent_cell_floor_sum += parent_cell_floor
            total_pre_terms += cap
            total_pre_blocks += blocks_here
            positive_q_capacity += poscap
            parent_positive_q_capacity += pposcap

            compact = {
                "row_id": row_id,
                "b_interval": list(interval),
                "g": int(g),
                "d": int(d),
                "exact_pre_mass": Pexact,
                "exact_pre_blocks": blocks_here,
                "exact_post_mass": Mpost,
                "hpadj19_replay_ratio_bin_count": len(parent_caps[interval]),
                "hpadj20_ratio_bin_count": len(cell_caps[interval]),
                "hpadj19_replay_used_ratio_bins": pused,
                "hpadj20_used_ratio_bins": used,
                "hpadj19_replay_cell_integer_upper": parent_cell_floor,
                "hpadj20_cell_integer_upper": cell_floor,
            }
            diagnostic.update(json.dumps(compact, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(seen == set(cells), "exact cell key-set mismatch")
    req(total_pre_terms == p14.EXPECTED_PRE_TERMS, "exact pre terminal aggregate")
    req(total_pre_blocks == p14.EXPECTED_PRE_BLOCKS, "exact pre block aggregate")
    global_floor = total_obj.numerator // total_obj.denominator
    parent_global_floor = parent_total_obj.numerator // parent_total_obj.denominator
    req(cell_floor_sum <= global_floor, "HPADJ20 cellwise floor direction")
    req(parent_cell_floor_sum <= parent_global_floor, "HPADJ19 replay cellwise floor direction")
    req(cell_floor_sum <= parent_cell_floor_sum, "HPADJ20 aggregate weakened HPADJ19 replay")
    req(cell_floor_sum <= Q_BENCHMARK, "HPADJ20 weakened MAIN q benchmark")
    req(cell_floor_sum <= HPADJ15_BENCHMARK, "HPADJ20 weakened HPADJ15 benchmark")
    req(strict_survivor_tiers > 0 and strict_cell_count > 0,
        "two-tier profile produced no strict survivor/cell refinement")

    out = {
        "schema": "STAGE32EX5_HPADJ20_QA_TWO_TIER_EXACT_MULTIPLICITY_PREDOMAIN_PICARD_LP_V1",
        "route_id": "HPADJ-20_ex5",
        "status": "Q_QUADRATIC_QA_TWO_TIER_EXACT_MULTIPLICITY_PREDOMAIN_PICARD_LP_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "sources": {
            "hpadj19_parent_blob_sha1": PARENT_BLOB,
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
            "hpadj15_candidate_upper_bound": HPADJ15_BENCHMARK,
            "full178_manifest_blob_sha1": p14.LOCKS["manifest_blob"],
            "hpadj10_counter_blob_sha1": p14.LOCKS["hpadj10_counter_blob"],
        },
        "exact_population_adapter": {
            "full178_rows": 178,
            "historical_b_shards": len(h18.PLANNED),
            "row_shard_cells": 178 * len(h18.PLANNED),
            "nonzero_post_mass_cells": nonzero_post_cells,
            "pre_hpadj08_exact_terminal_mass": total_pre_terms,
            "pre_hpadj08_exact_block_mass": total_pre_blocks,
            "post_hpadj08_x4_complete_survivor_mass": p14.EXPECTED_SURVIVOR_ENVELOPE,
            "exact_pre_domain_replayed_by_a_b_c_support_e_picard_parity": True,
            "A_ordered_triple_population_preserved_exactly": True,
            "picard_character": "x4 == x0+x8+x10 (mod 2)",
            "unknown_hpadj08_removed_block_identity_assumed": False,
        },
        "qA_refinement": {
            "group": "x2+x3+x7=a",
            "exact_support_preserved": True,
            "exact_histogram_class_count": hist_classes,
            "strict_two_tier_class_count": strict_profile_classes,
            "nonminimum_tuple_count_in_full_H96_profile": nonminimum_tuples,
            "tier_rule": "For each exact (a,s), keep exact multiplicity at qA_min; all remaining tuples form a second population-preserving tier with lower bound equal to the exact second-smallest qA.",
            "scaled_joint_condition": "138*qA_lower_tier+f0(h,g,b,c,x4)<=0",
            "parent_rule_replayed": "HPADJ19 assigns qA_min(a,s) to every ordered A triple in the support class.",
            "strict_survivor_tier_instances": strict_survivor_tiers,
            "strict_lp_cell_count": strict_cell_count,
            "wolfram_independent_check": "For a<=20 and supports 0..3, exact ordered-triple enumeration matched C(3,s)C(a-1,s-1) and the balanced qA minimum in every nonempty class; 33 classes already had more than one qA value, first at (a,s)=(4,2).",
        },
        "optimization": {
            "problem": "For every exact (g,d,b-shard) cell, maximize q/Picard survivors over exact pre-HPADJ08 capacities while fixing only certified post mass.",
            "relaxation": "Whole-block survival remains fractionally relaxed inside each survivor-ratio bin; HPADJ08 deleted identities remain adversarial. The nonminimum A tier uses only its certified second-smallest qA lower bound, not the full qA histogram.",
            "cell_solution": "Sort exact pre-domain capacities by q-survivor ratio q_s/B descending and greedily fill certified post mass.",
            "hpadj19_replay_positive_q_terminal_capacity": parent_positive_q_capacity,
            "hpadj20_positive_q_terminal_capacity": positive_q_capacity,
            "hpadj19_replay_rational_objective_numerator": parent_total_obj.numerator,
            "hpadj19_replay_rational_objective_denominator": parent_total_obj.denominator,
            "hpadj20_rational_objective_numerator": total_obj.numerator,
            "hpadj20_rational_objective_denominator": total_obj.denominator,
            "hpadj19_replay_aggregate_rational_floor": parent_global_floor,
            "hpadj20_aggregate_rational_floor": global_floor,
            "hpadj19_replay_cellwise_integer_floor_sum": parent_cell_floor_sum,
            "hpadj20_cellwise_integer_floor_sum": cell_floor_sum,
            "diagnostic_stream_sha256": diagnostic.hexdigest(),
        },
        "candidate_bound": {
            "main_q_quadratic_global_candidate_upper_bound": Q_BENCHMARK,
            "hpadj15_candidate_upper_bound": HPADJ15_BENCHMARK,
            "replayed_hpadj19_candidate_upper_bound": parent_cell_floor_sum,
            "hpadj20_candidate_upper_bound": cell_floor_sum,
            "improvement_vs_hpadj19_replay": parent_cell_floor_sum - cell_floor_sum,
            "improvement_vs_main_q_quadratic_global": Q_BENCHMARK - cell_floor_sum,
            "improvement_vs_hpadj15": HPADJ15_BENCHMARK - cell_floor_sum,
            "strict_improvement_vs_hpadj19_replay": cell_floor_sum < parent_cell_floor_sum,
            "structurally_no_weaker_than_hpadj19": True,
            "composition_if_consumed": "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        },
        "semantics": {
            "same_hpadj08_td01_x4_complete_population": True,
            "hpadj19_source_credit_inherited": False,
            "per_exact_pre_block_q_survivor_capacity_no_larger_than_hpadj19": True,
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
