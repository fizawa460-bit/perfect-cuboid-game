#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "stages/stage32-ex5/hpadj-15_ex5/derive_b_shard_row_exact_grf04_picard_capacity_bound.py"

PARENT_BLOB = "99ac15d18c83da050107ac7e8b113ae795ff0629"
Q_EXACT_HEAD = "6489e1fb9f35b8ecdc19c982301a816d956711e9"
Q_REL = Path("stages/stage32/management/grf04-quadratic-capacity")
Q_VERIFIER = "verify_grf04_main_independent_quadratic_capacity_candidate.py"
Q_CANDIDATE = "GRF04-MAIN-INDEPENDENT-QUADRATIC-CAPACITY-LP-CANDIDATE.json"
Q_VERIFIER_BLOB = "373ed6768f22f94b2e0d82c1af514c7ce1833a0a"
Q_CANDIDATE_BLOB = "1d669114e930951b9d5f9f82a6abb2b59cd43884"
Q_CANDIDATE_CANON = "3fca63c0d678eb2de2147848a1aa29839618cfd9cb65bdd27d671b28c6e44b01"
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


def load_module(path: Path, blob: str, name: str):
    req(path.is_file(), f"missing {name}")
    req(git_blob(path) == blob, f"{name} blob drift")
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {name}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_q(q_root: Path):
    base = q_root / Q_REL
    verifier = base / Q_VERIFIER
    candidate_path = base / Q_CANDIDATE
    q = load_module(verifier, Q_VERIFIER_BLOB, "stage32_q_quadratic_locked_for_hpadj16")
    req(candidate_path.is_file() and git_blob(candidate_path) == Q_CANDIDATE_BLOB,
        "q-quadratic candidate blob drift")
    candidate = json.loads(candidate_path.read_text())
    req(candidate.get("canonical_sha256_without_this_field") == Q_CANDIDATE_CANON,
        "q-quadratic candidate stored canonical drift")
    req(canonical(candidate) == Q_CANDIDATE_CANON, "q-quadratic candidate canonical drift")
    req(candidate["candidate_bound"]["candidate_upper_bound"] == Q_BENCHMARK,
        "q-quadratic benchmark drift")
    req(candidate["candidate_bound"]["composition_if_audited"] ==
        "MIN_OF_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING",
        "q-quadratic composition drift")
    req(candidate["exact_input_envelope"]["x4_complete_after_hpadj08"] is True,
        "q-quadratic x4-complete envelope drift")
    req(candidate["exact_input_envelope"]["hpadj08_survivor_x4_complete_envelope_terminals"] ==
        6703403803993209250491, "q-quadratic envelope mass drift")
    req(candidate["group_sum_relaxation"]["b"] == "x1+x5+x9", "q-quadratic b semantics drift")
    req(candidate["promotion_gate"]["main_credit_granted"] is False,
        "q-quadratic source unexpectedly carries MAIN credit")
    return q, candidate


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
    # Maximize a unit-mass LP with bounded bins: fill in descending survivor ratio.
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--q-root", required=True)
    ns = ap.parse_args()

    parent15 = load_module(PARENT, PARENT_BLOB, "hpadj15_locked_for_hpadj16")
    q, q_candidate = load_q(Path(ns.q_root))
    masses, parent14 = exact_cell_masses(parent15)
    req(parent15.HPADJ14_BENCHMARK == 463577241806597722598, "HPADJ15 parent benchmark drift")

    bc = q.build_bc_counts()
    # Preserve q-verifier's two load-bearing canonical-prefix fixtures.
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
    strict_vs_global_ratio_cells = 0
    diagnostic = hashlib.sha256()
    seen = set()

    for g, hmax in ((0, 88), (1, 96)):
        for h in range(4, hmax + 1):
            d = 2 * h
            legacy = 8 if g == 0 else 4
            K = q.ceil_div(d - 16 * g + 16, 4)
            e_lower = max(legacy, K, d - 4 * g + 4)
            if e_lower & 1:
                e_lower += 1
            e_upper = 3 * d

            # q's relaxed histogram, now kept separately for each historical b-shard.
            hists = {
                interval: [[0] * (3 * h + 1) for _ in range(h + 2)]
                for interval in PLANNED
            }
            for b in range(h + 1):
                interval = shard_for_b(b)
                hist = hists[interval]
                for c in range(h + 1):
                    bc_count = bc[b][c]
                    if not bc_count:
                        continue
                    x4_interval = q.a0_interval(h, g, b, c)
                    if x4_interval is None:
                        continue
                    left, right = x4_interval
                    diff = [0] * (h + 2)
                    for x4 in range(left, right + 1):
                        room = -q.f0(h, g, b, c, x4)
                        req(room >= 0, "q interval construction regression")
                        amax = min(h, int((room // 46) ** 0.5))
                        # Correct possible float-rounding at large integer values fail-closed.
                        while (amax + 1) <= h and 46 * (amax + 1) * (amax + 1) <= room:
                            amax += 1
                        while 46 * amax * amax > room:
                            amax -= 1
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
                if M and obj < Fraction(Q_BENCHMARK * M, parent14.EXPECTED_SURVIVOR_ENVELOPE):
                    strict_vs_global_ratio_cells += 1
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
            "q_group_b_semantics": q_candidate["group_sum_relaxation"]["b"],
            "hpadj15_b_shard_and_q_group_b_are_same_coordinate": True,
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
            "cells_strictly_below_global_q_average_ratio": strict_vs_global_ratio_cells,
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
            "same_b_coordinate_adapter_proved_by_source_locked_formula": True,
            "q_quadratic_capacity_replayed_not_inherited_as_main_credit": True,
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
