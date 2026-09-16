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
PARENT = ROOT / "stages/stage32-ex5/hpadj-18_ex5/derive_q_quadratic_exact_predomain_picard_parity_lp_bound.py"
PARENT_BLOB = "09c3a97ca47f2602b547efc572a3ddfee1d3437f"
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
    req(PARENT.is_file() and git_blob(PARENT) == PARENT_BLOB, "HPADJ18 parent blob drift")
    spec = importlib.util.spec_from_file_location("hpadj18_locked_for_hpadj19", PARENT)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ18 parent")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def qa_min_for_mass_support(a: int, support: int) -> int:
    """Exact min x2^2+x3^2+x7^2 at fixed sum a and exact support."""
    if support == 0:
        req(a == 0, "support-0 A mass must be zero")
        return 0
    req(1 <= support <= 3 and a >= support, "invalid A mass/support")
    q, r = divmod(a, support)
    return (support - r) * q * q + r * (q + 1) * (q + 1)


def support_q_survivors(h16, h: int, g: int, b: int, c: int) -> list[list[tuple[int, int]]]:
    """Exact-support A-square lower bound + actual Picard x4 parity; BC relaxation stays unchanged."""
    out = [[(0, 0) for _ in range(4)] for __ in range(h + 1)]
    xr = h16.a0_interval(h, g, b, c)
    if xr is None:
        return out
    left, right = xr

    qvals = [[] for _ in range(4)]
    qvals[0] = [0]
    for s in range(1, 4):
        qvals[s] = [qa_min_for_mass_support(a, s) for a in range(s, h + 1)]

    # diffs[s][parity][a].  The exact scaled condition is
    #   138*qA_min(a,s) + f0(h,g,b,c,x4) <= 0,
    # since f0 is the 23/4-scaled BC-relaxation minus the GRF04 RHS.
    diffs = [[[0] * (h + 2) for _ in range(2)] for __ in range(4)]
    for x4 in range(left, right + 1):
        room = -h16.f0(h, g, b, c, x4)
        req(room >= 0, "support-q interval construction regression")
        p = x4 & 1

        # a=0, support=0.
        diffs[0][p][0] += 1
        diffs[0][p][1] -= 1

        qcap = room // 138
        for s in range(1, 4):
            vals = qvals[s]
            k = bisect.bisect_right(vals, qcap)
            if k:
                amax = s + k - 1
                diffs[s][p][s] += 1
                diffs[s][p][amax + 1] -= 1

    runs = [[0, 0] for _ in range(4)]
    for a in range(h + 1):
        for s in range(4):
            runs[s][0] += diffs[s][0][a]
            runs[s][1] += diffs[s][1][a]
            out[a][s] = (runs[s][0], runs[s][1])
    return out


def main() -> None:
    h18 = load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    cells, p14 = h17.exact_cells(h16)
    counter = p14.load_counter()

    req(h18.Q_BENCHMARK == Q_BENCHMARK, "HPADJ18 q benchmark drift")
    req(h18.PARENT_BLOB == "10c1a836136f66b716ad39f6ca74250e32f386a9", "HPADJ18 parent identity drift")
    req(p14.EXPECTED_SURVIVOR_ENVELOPE == 6703403803993209250491, "survivor envelope drift")

    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178, "FULL178 row coverage")
    H = max(d // 2 for _, _, d in rows)
    req(H == 96, "FULL178 hmax drift")
    BC = counter.build_bc_exact_parity(H)
    valid_support_classes = [
        (a, s) for a in range(H + 1) for s in range(4)
        if counter.triple_free_count(a, s)
    ]
    req(all(138 * qa_min_for_mass_support(a, s) >= 46 * a * a for a, s in valid_support_classes),
        "support-aware qA lower bound does not dominate parent continuous qA relaxation")
    strict_support_classes = sum(
        138 * qa_min_for_mass_support(a, s) > 46 * a * a for a, s in valid_support_classes
    )
    req(strict_support_classes > 0, "support-aware qA formula gives no strict class")

    total_obj = Fraction(0, 1)
    cell_floor_sum = 0
    total_pre_terms = 0
    total_pre_blocks = 0
    positive_q_capacity = 0
    nonzero_post_cells = 0
    diagnostic = hashlib.sha256()
    seen = set()

    for row_id, g, d in rows:
        h = d // 2
        legacy = 8 if g == 0 else 4
        K = counter.ceil_div(d - 16 * g + 16, 4)
        A = [[counter.triple_free_count(a, sa) for sa in range(4)] for a in range(h + 1)]
        cell_caps = {interval: defaultdict(int) for interval in h18.PLANNED}
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
                qsurv = support_q_survivors(h16, h, g, b, c)

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
                            for sa, right_count in enumerate(avec):
                                if not right_count:
                                    continue
                                q_s = int(qsurv[a][sa][r])
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
                                    cell_caps[interval][(q_s, B)] += count * B

        for interval in h18.PLANNED:
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

            obj, cap, poscap, used = h18.optimize_cell_exact_predomain(cell_caps[interval], Mpost)
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
    req(cell_floor_sum <= Q_BENCHMARK, "support-exact qA LP weakened q benchmark")
    req(cell_floor_sum <= HPADJ15_BENCHMARK, "support-exact qA LP weakened HPADJ15 benchmark")

    out = {
        "schema": "STAGE32EX5_HPADJ19_EXACT_QA_SUPPORT_PREDOMAIN_PICARD_LP_V1",
        "route_id": "HPADJ-19_ex5",
        "status": "Q_QUADRATIC_EXACT_QA_SUPPORT_PREDOMAIN_PICARD_PARITY_LP_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "sources": {
            "hpadj18_parent_blob_sha1": PARENT_BLOB,
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
            "picard_character": "x4 == x0+x8+x10 (mod 2)",
            "unknown_hpadj08_removed_block_identity_assumed": False,
        },
        "qA_refinement": {
            "group": "x2+x3+x7=a",
            "exact_support_preserved": True,
            "exact_minimum_rule": "If a=s*q+r with exact support s in {1,2,3}, min qA=(s-r)q^2+r(q+1)^2; (a,s)=(0,0) gives 0.",
            "scaled_joint_condition": "138*qA_min(a,supportA)+f0(h,g,b,c,x4)<=0",
            "parent_relaxation_replaced": "46*a^2+f0<=0",
            "strict_support_class_count": strict_support_classes,
            "wolfram_check": "Exact enumeration for a<=15 and supports 0..3 matched the balanced positive-part formula; symbolic scaling follows 23/4*24=138.",
        },
        "optimization": {
            "problem": "For every exact (g,d,b-shard) cell, maximize q/Picard survivors over exact pre-HPADJ08 capacities while fixing only certified post mass.",
            "relaxation": "Whole-block survival remains fractionally relaxed inside each exact survivor-ratio bin; HPADJ08 deleted identities remain adversarial.",
            "cell_solution": "Sort exact pre-domain capacities by q-survivor ratio q_s/B descending and greedily fill certified post mass.",
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
            "hpadj19_candidate_upper_bound": cell_floor_sum,
            "improvement_vs_main_q_quadratic_global": Q_BENCHMARK - cell_floor_sum,
            "improvement_vs_hpadj15": HPADJ15_BENCHMARK - cell_floor_sum,
            "structurally_no_weaker_than_hpadj18": True,
            "composition_if_consumed": "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        },
        "semantics": {
            "same_q_quadratic_and_picard_character_as_parent": True,
            "per_exact_pre_block_q_survivor_capacity_no_larger_than_hpadj18": True,
            "statistical_independence_assumed": False,
            "hpadj08_deleted_block_identity_inferred": False,
            "hpadj18_parent_credit_inherited": False,
            "q_quadratic_source_credit_inherited": False,
            "new_heavy_run_used": False,
            "hostile_audit_required_before_any_consumption": True,
            "main_consumption_performed": False,
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
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
