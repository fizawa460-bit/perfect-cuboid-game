#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mass7_mod2_obstruction as base


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def run() -> dict:
    P, blocks = base.load_picard_interface()
    kernel = base.left_kernel_mod2(P)
    boundary_labels = sorted({b for pack in base.PACKS for b in pack})
    unknown_normal_labels = [
        label for label in range(1, base.NORMAL_COUNT + 1) if label not in boundary_labels
    ]
    masks = base.consistency_masks(kernel, unknown_normal_labels)
    idx = base.e8.indexer()
    current_main = set(map(int, base.e8.current_main_survivor_block_indices()))

    targeted = 0
    obstructed = 0
    current_main_targeted = 0
    current_main_obstructed = 0
    attempts = 0
    survivors = []
    targeted_h = hashlib.sha256()
    obstructed_h = hashlib.sha256()
    by_mass = {"7": {"targeted": 0, "obstructed": 0}, "8": {"targeted": 0, "obstructed": 0}}

    for block_index in range(base.e8.UNFILTERED_BLOCK_COUNT):
        sig = base.e8.block_signature(block_index, idx)
        mass = int(sig["fixed_exceptional_mass"])
        groups = [int(v) for v in sig["n355_known_group_sums"]]
        if mass < 7 or groups[2] != 3:
            continue
        targeted += 1
        by_mass[str(mass)]["targeted"] += 1
        targeted_h.update(f"{block_index}\n".encode())
        if block_index in current_main:
            current_main_targeted += 1
        blocked, witness, count = base.block_mod2_obstructed(
            block_index, idx, blocks, kernel, masks
        )
        attempts += count
        if blocked:
            obstructed += 1
            by_mass[str(mass)]["obstructed"] += 1
            obstructed_h.update(f"{block_index}\n".encode())
            if block_index in current_main:
                current_main_obstructed += 1
        elif len(survivors) < 64:
            survivors.append({
                "block_index": block_index,
                "fixed_exceptional_mass": mass,
                "n355_group_sums": groups,
                "current_main_prefix_survivor": block_index in current_main,
                "known_exceptional_support": int(sig["known_exceptional_support"]),
                "residual_exceptional_label": None if witness is None else witness.get("residual_exceptional_label"),
                "fibre_degrees": None if witness is None else witness.get("fibre_degrees"),
                "incidence_sums": None if witness is None else witness.get("incidence_sums"),
            })

    survivor_count = targeted - obstructed
    status = (
        "PASS_G3_EQ_3_FULL_COMPRESSED_E8_MOD2_OBSTRUCTION"
        if targeted > 0 and survivor_count == 0
        else "COUNTEREXAMPLE_G3_EQ_3_FULL_E8_CHALLENGE"
    )
    req(current_main_targeted == 1677, "current-MAIN g3==3 target-count drift")
    req(current_main_obstructed == 1677, "current-MAIN g3==3 obstruction-count drift")

    out = {
        "schema": "STAGE32_CERTLIFT_G3_EQ_3_EXACT_CANDIDATE_V1",
        "stage": "32",
        "node": "CERTLIFT-03",
        "status": status,
        "hypothesis": {
            "e": 8,
            "d": 8,
            "predicate": "fixed_exceptional_mass>=7 and sum(y93,y94,y95,y96)==3",
            "g3_definition": "N355 group3 = [93,94,95,96]",
            "scope": "entire 11,318-block compressed e8 terminal-signature universe, before N220/N355 current-MAIN filtering",
        },
        "method": {
            "solver_used": False,
            "finite_ring": 2,
            "exceptional_completion_exact": True,
            "fibre_equations_exact": True,
            "remaining_normal_parities_projected_by_exact_gaussian_elimination": True,
            "projection_contradiction_is_sound_unsat_certificate": True,
        },
        "matrix": {
            "picard_pairing_shape": [P.rows, P.cols],
            "left_kernel_dimension_mod2": len(kernel),
            "unknown_nonboundary_normal_count": len(unknown_normal_labels),
            "projected_consistency_mask_count": len(masks),
            "projected_consistency_masks_sha256": csha(masks),
        },
        "result": {
            "unfiltered_block_count": base.e8.UNFILTERED_BLOCK_COUNT,
            "targeted_blocks": targeted,
            "mod2_obstructed_blocks": obstructed,
            "projection_survivor_blocks": survivor_count,
            "current_main_targeted_blocks": current_main_targeted,
            "current_main_mod2_obstructed_blocks": current_main_obstructed,
            "by_fixed_exceptional_mass": by_mass,
            "attempted_exact_exceptional_fibre_completions": attempts,
            "targeted_block_stream_sha256": targeted_h.hexdigest(),
            "obstructed_block_stream_sha256": obstructed_h.hexdigest(),
            "first_projection_survivors": survivors,
        },
        "interpretation": {
            "finite_exhaustive_e8_family_lemma_candidate": status.startswith("PASS_"),
            "algebraic_row_certificate_still_required_for_symbolic_promotion": True,
            "cross_e_claim": False,
        },
        "credit": {
            "certlift_03_candidate": status.startswith("PASS_"),
            "stage32_main_pruning_credit": False,
            "theorem_credit": False,
            "stage32_closure_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()
    out = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    if args.self_check:
        r = out["result"]
        print(json.dumps({
            "status": out["status"],
            "targeted": r["targeted_blocks"],
            "obstructed": r["mod2_obstructed_blocks"],
            "survivors": r["projection_survivor_blocks"],
            "by_mass": r["by_fixed_exceptional_mass"],
            "first_survivor_blocks": [x["block_index"] for x in r["first_projection_survivors"][:16]],
            "canonical": out["canonical_sha256_without_this_field"],
        }, sort_keys=True))
    elif not args.output:
        print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
