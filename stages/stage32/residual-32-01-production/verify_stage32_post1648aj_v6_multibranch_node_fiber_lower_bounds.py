#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

AI = HERE / "post1648ai-fsm-nodewise-unibranch-v6-exclusion.json"
NOTE = HERE / "post1648aj-v6-multibranch-node-fiber-lower-bounds-source-note.md"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
OUT = HERE / "post1648aj-v6-multibranch-node-fiber-lower-bounds.json"

AI_CANON = "8506d88f630e5d097de5355491e91f072f7728bac484490e3ab3067db7b9db97"
NOTE_SHA = "373badcda792eae3058c532a4cc9ef3e6f0ec4aa2c7c41fbfdd9c19c2c2a5839"
V6_CANON = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
ALL140_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"


def csha(value: dict) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def min_total_branches(masses: list[int], needed_minimal: int) -> tuple[int, int]:
    inf = 10**9
    dp = {0: 0}
    for m in masses:
        if m == 0:
            opts = [(0, 0)]
        else:
            opts = []
            for t in range(m + 1):
                if t == m:
                    b = m
                elif t == 0:
                    b = 1
                else:
                    b = t + 1
                opts.append((t, b))
        nxt: dict[int, int] = {}
        for total_t, total_b in dp.items():
            for t, b in opts:
                nt = total_t + t
                nb = total_b + b
                if nb < nxt.get(nt, inf):
                    nxt[nt] = nb
        dp = nxt
    return min((b, t) for t, b in dp.items() if t >= needed_minimal)


def main() -> None:
    if sha256_bytes(NOTE.read_bytes()) != NOTE_SHA:
        raise ValueError("AJ source note moved")
    text = NOTE.read_text(encoding="utf-8")
    for fragment in [
        "m_i = sum_j ord_{P_{i,j}}(nu^* E_i)",
        "T >= 47",
        "9 + 16 + 15 = 40 < 47",
        "sum_i b_i >= 72",
        "Smooth-ambient-locus singularities may coexist",
    ]:
        if fragment not in text:
            raise ValueError(f"AJ semantic lock moved: {fragment}")

    ai = json.loads(AI.read_text(encoding="utf-8"))
    if ai.get("canonical_sha256_without_this_field") != AI_CANON or csha(ai) != AI_CANON:
        raise ValueError("AI parent canonical moved")
    if ai["decision"]["remaining_open_case"] != (
        "ANY_INTEGRAL_GEOMETRIC_GENUS1_V6_CARRIER_MUST_BE_MULTIBRANCH_OVER_AT_LEAST_ONE_MET_BOX_SURFACE_NODE"
    ):
        raise ValueError("AI remaining-case boundary moved")
    if not ai["decision"]["smooth_ambient_locus_singularities_may_coexist"]:
        raise ValueError("AI coexistence firewall moved")

    v6 = json.loads(V6.read_text(encoding="utf-8"))
    if v6["canonical_sha256_without_this_field"] != V6_CANON:
        raise ValueError("V6 canonical moved")
    if v6["witness"]["all140_pairings_sha256"] != ALL140_SHA:
        raise ValueError("V6 all140 source moved")
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    masses = pairings[92:]
    if len(masses) != 48 or sum(masses) != 266:
        raise ValueError("V6 exceptional vector moved")

    unit_labels = [i + 1 for i, m in enumerate(masses) if m == 1]
    positive = [m for m in masses if m > 0]
    nonunit_desc = sorted((m for m in masses if m > 1), reverse=True)
    if unit_labels != [1, 2, 3, 7, 15, 20, 22, 24, 36]:
        raise ValueError("V6 unit exceptional labels moved")
    if len(positive) != 47 or nonunit_desc[:2] != [16, 15]:
        raise ValueError("V6 support/top masses moved")

    zeros_lower = 2 * 186
    pole_per_minimal = 8
    minimal_required = (zeros_lower + pole_per_minimal - 1) // pole_per_minimal
    if (zeros_lower, minimal_required) != (372, 47):
        raise ValueError("FSM minimal branch requirement moved")

    max_with_two_multibranch = len(unit_labels) + nonunit_desc[0] + nonunit_desc[1]
    if max_with_two_multibranch != 40 or not max_with_two_multibranch < minimal_required:
        raise ValueError("three-node lower-bound arithmetic moved")

    minimum_total, optimum_t = min_total_branches(masses, minimal_required)
    if (minimum_total, optimum_t) != (72, 47):
        raise ValueError("normalization fiber DP lower bound moved")
    excess = minimum_total - len(positive)
    if excess != 25:
        raise ValueError("branch excess moved")

    cert = {
        "schema": "STAGE32_POST1648AJ_V6_MULTIBRANCH_NODE_FIBER_LOWER_BOUNDS_V1",
        "stage": 32,
        "leaf": "POST1648AJ_V6_MULTIBRANCH_NODE_FIBER_LOWER_BOUNDS",
        "status": "EXACT_COMBINATORIAL_LOWER_BOUNDS_CONDITIONAL_ON_EXISTENCE_OF_INTEGRAL_GEOMETRIC_GENUS1_V6_CARRIER",
        "parent": {
            "path": str(AI.relative_to(ROOT)),
            "canonical_sha256": AI_CANON,
            "scratch_head": "31ad1e33a569ae3f753bff002ef8c4fc980aad93",
            "ci": {"run_id": 34076480820, "job_id": 101603494707, "result": "SUCCESS"},
        },
        "source_locks": {
            "source_note_path": str(NOTE.relative_to(ROOT)),
            "source_note_sha256": NOTE_SHA,
            "v6_witness_path": str(V6.relative_to(ROOT)),
            "v6_witness_canonical_sha256": V6_CANON,
            "v6_all140_pairings_sha256": ALL140_SHA,
        },
        "v6_exact_data": {
            "row_id": "g1-d186",
            "geometric_genus": 1,
            "degree_d": 186,
            "exceptional_mass_e": 266,
            "exceptional_pairings": masses,
            "positive_support": len(positive),
            "unit_pairing_labels_1based": unit_labels,
            "unit_pairing_count": len(unit_labels),
            "largest_nonunit_pairings_desc": nonunit_desc[:2],
        },
        "fsm_minimal_branch_budget": {
            "zeros_lower_per_k": zeros_lower,
            "positive_pole_upper_per_minimal_branch_per_k": pole_per_minimal,
            "minimal_branch_count_required": minimal_required,
            "reason": "372k <= poles <= 8k*T",
        },
        "distinct_multibranch_node_lower_bound": {
            "if_at_most_two_multibranch_max_minimal_branches": max_with_two_multibranch,
            "required_minimal_branches": minimal_required,
            "contradiction": True,
            "minimum_distinct_multibranch_nodes": 3,
        },
        "normalization_fiber_dp": {
            "local_lower_bound_rule": {
                "m_zero": "b=0",
                "t_zero_m_positive": "b>=1",
                "zero_lt_t_lt_m": "b>=t+1",
                "t_eq_m": "b>=m",
            },
            "constraint": "sum_i t_i >= 47, 0 <= t_i <= m_i integers",
            "minimum_total_normalization_preimages_over_48_exceptional_nodes": minimum_total,
            "minimal_branch_total_at_optimum": optimum_t,
            "met_node_count": len(positive),
            "minimum_branch_excess_over_one_per_met_node": excess,
        },
        "decision": {
            "conditional_on_carrier_existence": True,
            "minimum_distinct_multibranch_surface_nodes": 3,
            "minimum_total_normalization_preimages_over_met_surface_nodes": minimum_total,
            "minimum_normalization_branch_excess": excess,
            "smooth_ambient_locus_singularities_may_coexist": True,
            "next_exact_route": "ENUMERATE_MULTIBRANCH_NODE_LOCAL_CAPACITY_PATTERNS_AGAINST_EXACT_EXCEPTIONAL_PAIRINGS_AND_FSM_CUSP_TYPES",
        },
        "firewalls": {
            "integral_genus1_member_materialized": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
            "controller_promotion_granted": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1648AJ_V6_MULTIBRANCH_NODE_FIBER_LOWER_BOUNDS",
        "minimum_distinct_multibranch_nodes": 3,
        "minimum_total_normalization_preimages": minimum_total,
        "minimum_branch_excess": excess,
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
