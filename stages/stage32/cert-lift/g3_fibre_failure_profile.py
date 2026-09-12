#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mass7_mod2_obstruction as base

G3_LABELS = [93, 94, 95, 96]


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parity_word(values: list[int]) -> str:
    return "".join(str(int(v) & 1) for v in values)


def classify_sums(sums: list[list[int]]) -> dict:
    pwords = [parity_word(pack) for pack in sums]
    uniform = [len({v & 1 for v in pack}) == 1 for pack in sums]
    maxs = [max(pack) for pack in sums]
    pack_parities = [None if not uniform[i] else (sums[i][0] & 1) for i in range(2)]
    if not uniform[0] or not uniform[1]:
        feasible_pre_cross = False
        reason = (
            "BOTH_PACKS_MIXED_PARITY" if not uniform[0] and not uniform[1]
            else "PACK1_MIXED_PARITY" if not uniform[0]
            else "PACK2_MIXED_PARITY"
        )
    elif pack_parities[0] != pack_parities[1]:
        feasible_pre_cross = False
        reason = "PACK_PARITY_SUM_MISMATCH_WITH_D_EVEN"
    elif maxs[0] + maxs[1] > base.TARGET_D:
        feasible_pre_cross = False
        reason = "MINIMUM_FIBRE_DEGREES_EXCEED_D"
    else:
        feasible_pre_cross = True
        reason = "PRE_CROSS_FIBRE_FEASIBLE"

    cross_ok = all(a + b <= base.TARGET_D for a in sums[0] for b in sums[1])
    # When both packs have uniform parity, max1+max2<=d is equivalent to the
    # exact degree-floor feasibility and also to the CUT cross-pack inequality.
    exact_fibre_feasible = bool(feasible_pre_cross and cross_ok)
    return {
        "parity_words": pwords,
        "uniform_pack_parity": uniform,
        "pack_parities": pack_parities,
        "max_cell_sums": maxs,
        "max_sum_total": sum(maxs),
        "cross_ok": cross_ok,
        "reason": reason if not exact_fibre_feasible else "EXACT_FIBRE_FEASIBLE",
        "exact_fibre_feasible": exact_fibre_feasible,
    }


def run() -> dict:
    _P, blocks = base.load_picard_interface()
    idx = base.e8.indexer()

    target_blocks = 0
    completions = 0
    feasible = 0
    reason_hist = Counter()
    reason_by_mass = defaultdict(Counter)
    parity_pair_hist = Counter()
    residual_cell_pair_hist = Counter()
    residual_cell_pair_reason = defaultdict(Counter)
    maxsum_hist = Counter()
    target_stream = hashlib.sha256()
    completion_stream = hashlib.sha256()
    first_examples: dict[str, dict] = {}

    # Cell pair of every exceptional label; this is the natural finite case
    # space for the residual unit when fixed mass=7.
    label_cell_pair = {}
    for label in range(93, 141):
        loc = []
        for p, pack in enumerate(blocks):
            hits = [k for k, cell in enumerate(pack) if label in cell]
            req(len(hits) == 1, f"label {label} incidence drift in pack {p}")
            loc.append(hits[0])
        label_cell_pair[label] = tuple(loc)

    for block_index in range(base.e8.UNFILTERED_BLOCK_COUNT):
        sig = base.e8.block_signature(block_index, idx)
        mass = int(sig["fixed_exceptional_mass"])
        groups = [int(v) for v in sig["n355_known_group_sums"]]
        if mass < 7 or groups[2] != 3:
            continue
        target_blocks += 1
        target_stream.update(f"{block_index}\n".encode())
        fixed = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
        req(sum(fixed.values()) == mass, "fixed mass drift")
        req(sum(fixed[label] for label in G3_LABELS) == 3, "g3 target drift")

        for residual_label, exceptional in base.exceptional_completions(fixed):
            completions += 1
            req(sum(exceptional.values()) == base.TARGET_E, "exceptional total mass drift")
            sums = [[sum(exceptional[j] for j in cell) for cell in pack] for pack in blocks]
            profile = classify_sums(sums)
            reason = profile["reason"]
            if profile["exact_fibre_feasible"]:
                feasible += 1
            reason_hist[reason] += 1
            reason_by_mass[mass][reason] += 1
            parity_pair_hist[tuple(profile["parity_words"])] += 1
            maxsum_hist[profile["max_sum_total"]] += 1

            cell_key = "NONE" if residual_label is None else f"{label_cell_pair[int(residual_label)][0]},{label_cell_pair[int(residual_label)][1]}"
            residual_cell_pair_hist[cell_key] += 1
            residual_cell_pair_reason[cell_key][reason] += 1
            first_examples.setdefault(reason, {
                "block_index": block_index,
                "mass": mass,
                "groups": groups,
                "fixed": {str(k): v for k, v in sorted(fixed.items())},
                "residual_label": residual_label,
                "residual_cell_pair": cell_key,
                "sums": sums,
                "profile": profile,
            })
            completion_stream.update(json.dumps({
                "block": block_index,
                "residual": residual_label,
                "sums": sums,
                "reason": reason,
            }, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(target_blocks == 1852, "g3 target-count drift")
    req(feasible == 0, "g3 fibre-feasible completion regression")
    req(reason_hist["EXACT_FIBRE_FEASIBLE"] == 0, "unexpected feasible reason")

    out = {
        "schema": "STAGE32_CERTLIFT_G3_FIBRE_FAILURE_PROFILE_V1",
        "stage": "32",
        "node": "CERTLIFT-03",
        "status": "PASS_G3_ALL_EXACT_EXCEPTIONAL_COMPLETIONS_FIBRE_EMPTY",
        "hypothesis": "d=e=8, fixed_exceptional_mass>=7, g3=sum(y93,y94,y95,y96)=3",
        "scope": {
            "unfiltered_blocks": base.e8.UNFILTERED_BLOCK_COUNT,
            "target_blocks": target_blocks,
            "exact_exceptional_completions": completions,
            "fibre_feasible_completions": feasible,
            "target_block_stream_sha256": target_stream.hexdigest(),
            "completion_stream_sha256": completion_stream.hexdigest(),
        },
        "failure_profile": {
            "reason_histogram": dict(sorted(reason_hist.items())),
            "reason_by_fixed_mass": {str(m): dict(sorted(h.items())) for m, h in sorted(reason_by_mass.items())},
            "pack_parity_word_pair_histogram": {f"{a}|{b}": n for (a,b), n in sorted(parity_pair_hist.items())},
            "max_cell_sum_total_histogram": {str(k): v for k, v in sorted(maxsum_hist.items())},
            "first_examples": first_examples,
        },
        "residual_unit_cases": {
            "exceptional_label_cell_pair": {str(k): list(v) for k, v in sorted(label_cell_pair.items())},
            "cell_pair_histogram": dict(sorted(residual_cell_pair_hist.items())),
            "cell_pair_reason_histogram": {k: dict(sorted(v.items())) for k, v in sorted(residual_cell_pair_reason.items())},
        },
        "interpretation": {
            "pure_fibre_parity_alone_sufficient": False,
            "mass7_and_g3_finite_case_data_used": True,
            "next_gate": "Compress the observed failure profile to a symbolic case split on fixed exceptional mass 7/8 and, for mass7, the residual unit cell-pair. A valid lemma must derive fibre infeasibility from nonnegative integral fibre equations and d=e=8, not from block index enumeration."
        },
        "credit": {
            "symbolic_lemma": False,
            "stage32_main_pruning_credit": False,
            "theorem_credit": False,
            "stage32_closure_credit": False,
            "merge_authorized": False
        }
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    return out


def main() -> None:
    out = run()
    print(json.dumps({
        "status": out["status"],
        "target_blocks": out["scope"]["target_blocks"],
        "completions": out["scope"]["exact_exceptional_completions"],
        "feasible": out["scope"]["fibre_feasible_completions"],
        "reasons": out["failure_profile"]["reason_histogram"],
        "reason_by_mass": out["failure_profile"]["reason_by_fixed_mass"],
        "parity_patterns": len(out["failure_profile"]["pack_parity_word_pair_histogram"]),
        "residual_cell_pairs": len(out["residual_unit_cases"]["cell_pair_histogram"]),
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
