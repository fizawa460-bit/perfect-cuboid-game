#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

import mass7_mod2_obstruction as base

SOURCE_MANIFEST = ROOT / "stages/stage32/cut-cert-lift/SOURCE-LOCKS.json"
LEDGER = HERE / "CERTIFICATE-LEDGER.json"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def locked_audited_scope(survivors: list[int]) -> tuple[list[int], dict]:
    manifest = json.loads(SOURCE_MANIFEST.read_text())
    req(manifest.get("schema") == "STAGE32_CUT_CERT_LIFT_SOURCE_LOCKS_V1", "manifest schema drift")
    waves = manifest.get("waves", [])
    req(len(waves) == 6, "audited wave-count drift")
    out: list[int] = []
    expected = 1
    for wave in waves:
        start = int(wave["offset_start"])
        end = int(wave["offset_end"])
        req(start == expected and end - start + 1 == 255, f"offset drift at {wave['id']}")
        part = list(map(int, survivors[start : end + 1]))
        req(len(part) == 255, f"scope reconstruction drift at {wave['id']}")
        out.extend(part)
        expected = end + 1
    req(expected == 1531 and len(out) == 1530 and len(set(out)) == 1530, "six-wave scope drift")
    return out, manifest


def analyze(
    name: str,
    block_indices: list[int],
    idx,
    blocks,
    kernel,
    masks,
    offset_by_block: dict[int, int],
) -> dict:
    targeted = 0
    obstructed = 0
    attempts = 0
    survivor_rows: list[dict] = []
    targeted_by_mass = Counter()
    obstructed_by_mass = Counter()
    survivor_by_mass = Counter()
    survivor_group_sums = Counter()
    survivor_support = Counter()
    obstructed_h = hashlib.sha256()
    survivor_h = hashlib.sha256()

    for block_index in block_indices:
        sig = base.e8.block_signature(block_index, idx)
        mass = int(sig["fixed_exceptional_mass"])
        if mass < 7:
            continue
        targeted += 1
        targeted_by_mass[mass] += 1
        blocked, witness, count = base.block_mod2_obstructed(
            block_index, idx, blocks, kernel, masks
        )
        attempts += count
        if blocked:
            obstructed += 1
            obstructed_by_mass[mass] += 1
            obstructed_h.update(f"{block_index}\n".encode())
            continue

        survivor_by_mass[mass] += 1
        groups = tuple(int(v) for v in sig["n355_known_group_sums"])
        survivor_group_sums[groups] += 1
        support = int(sig["known_exceptional_support"])
        survivor_support[support] += 1
        survivor_h.update(f"{block_index}\n".encode())
        row = {
            "block_index": int(block_index),
            "current_main_survivor_offset": int(offset_by_block[block_index]),
            "fixed_exceptional_mass": mass,
            "known_exceptional_support": support,
            "n355_group_sums": list(groups),
            "n356_lhs_b_minus_c": int(groups[1] - groups[2]),
        }
        if witness is not None:
            row["residual_exceptional_label"] = witness.get("residual_exceptional_label")
            row["fibre_degrees"] = witness.get("fibre_degrees")
            row["incidence_sums"] = witness.get("incidence_sums")
        survivor_rows.append(row)

    survivor_count = targeted - obstructed
    req(survivor_count == len(survivor_rows), f"survivor accounting drift in {name}")
    offsets = [r["current_main_survivor_offset"] for r in survivor_rows]
    return {
        "scope": name,
        "input_blocks": len(block_indices),
        "targeted_mass_ge_7_blocks": targeted,
        "mod2_obstructed_blocks": obstructed,
        "projection_survivor_blocks": survivor_count,
        "targeted_by_mass": {str(k): v for k, v in sorted(targeted_by_mass.items())},
        "obstructed_by_mass": {str(k): v for k, v in sorted(obstructed_by_mass.items())},
        "survivor_by_mass": {str(k): v for k, v in sorted(survivor_by_mass.items())},
        "survivor_known_support_histogram": {str(k): v for k, v in sorted(survivor_support.items())},
        "survivor_n355_group_sums_histogram": {
            ",".join(map(str, k)): v for k, v in sorted(survivor_group_sums.items())
        },
        "survivor_offset_minmax": [min(offsets), max(offsets)] if offsets else None,
        "attempted_exact_exceptional_fibre_completions": attempts,
        "obstructed_block_stream_sha256": obstructed_h.hexdigest(),
        "survivor_block_stream_sha256": survivor_h.hexdigest(),
        "first_projection_survivors": survivor_rows[:32],
    }


def run() -> dict:
    P, blocks = base.load_picard_interface()
    kernel = base.left_kernel_mod2(P)
    boundary_labels = sorted({b for pack in base.PACKS for b in pack})
    unknown_normal_labels = [
        label for label in range(1, base.NORMAL_COUNT + 1) if label not in boundary_labels
    ]
    masks = base.consistency_masks(kernel, unknown_normal_labels)
    idx = base.e8.indexer()
    current_main = list(map(int, base.e8.current_main_survivor_block_indices()))
    req(len(current_main) == base.e8.CURRENT_MAIN_BLOCK_COUNT == 7596, "current-MAIN e8 population drift")
    offset_by_block = {block: offset for offset, block in enumerate(current_main)}
    audited_blocks, manifest = locked_audited_scope(current_main)

    audited = analyze(
        "audited-cut193-cut198",
        audited_blocks,
        idx,
        blocks,
        kernel,
        masks,
        offset_by_block,
    )
    current = analyze(
        "current-main-e8",
        current_main,
        idx,
        blocks,
        kernel,
        masks,
        offset_by_block,
    )

    ledger = json.loads(LEDGER.read_text())
    expected_audited_mass7 = int(ledger["candidate_rule"]["selected_closed_blocks"])
    req(expected_audited_mass7 == 1049, "MASS7 ledger drift")
    req(
        audited["targeted_mass_ge_7_blocks"] == expected_audited_mass7,
        "audited MASS7 target-count drift",
    )

    audited_pass = audited["projection_survivor_blocks"] == 0
    current_extension_pass = current["projection_survivor_blocks"] == 0
    if audited_pass and not current_extension_pass:
        status = "PASS_AUDITED_MASS7_MOD2__CURRENT_MAIN_EXTENSION_COUNTEREXAMPLES"
    elif audited_pass and current_extension_pass:
        status = "PASS_MASS7_MOD2_THROUGH_CURRENT_MAIN"
    else:
        status = "COUNTEREXAMPLE_INSIDE_AUDITED_MASS7_SCOPE"

    out = {
        "schema": "STAGE32_CERTLIFT_MASS7_SCOPE_SPLIT_V1",
        "stage": "32",
        "node": "CERTLIFT-02",
        "status": status,
        "source": {
            "manifest": str(SOURCE_MANIFEST.relative_to(ROOT)),
            "ex5_producer_exact_head": manifest["shared_inputs"]["ex5_e8_terminal_producer_exact_head"],
            "audited_wave_ids": [w["id"] for w in manifest["waves"]],
            "audited_survivor_offsets": [1, 1530],
        },
        "matrix": {
            "picard_pairing_shape": [P.rows, P.cols],
            "left_kernel_dimension_mod2": len(kernel),
            "unknown_nonboundary_normal_count": len(unknown_normal_labels),
            "projected_consistency_mask_count": len(masks),
            "projected_consistency_masks_sha256": csha(masks),
        },
        "audited_scope": audited,
        "current_main_scope": current,
        "interpretation": {
            "audited_mass7_exact_mod2_replay_pass": audited_pass,
            "current_main_mass7_extension_pass": current_extension_pass,
            "projection_survivor_is_integral_completion_witness": False,
            "next_receiver": "compress current-MAIN projection survivors by prefix/HNF invariants; do not promote MASS7 globally",
        },
        "credit": {
            "certlift_l2_audited_candidate": audited_pass,
            "stage32_main_pruning_credit": False,
            "theorem_credit": False,
            "stage32_closure_credit": False,
            "merge_authorized": False,
        },
        "firewalls": {
            "no_cross_e_extrapolation": True,
            "no_current_main_promotion_from_audited_scope": True,
            "no_projection_survivor_relabel_as_sat_integral_completion": True,
            "no_timeout_semantics": True,
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
        a = out["audited_scope"]
        c = out["current_main_scope"]
        print(json.dumps({
            "status": out["status"],
            "audited_targeted": a["targeted_mass_ge_7_blocks"],
            "audited_obstructed": a["mod2_obstructed_blocks"],
            "audited_survivors": a["projection_survivor_blocks"],
            "current_targeted": c["targeted_mass_ge_7_blocks"],
            "current_obstructed": c["mod2_obstructed_blocks"],
            "current_survivors": c["projection_survivor_blocks"],
            "current_survivor_by_mass": c["survivor_by_mass"],
            "current_survivor_offset_minmax": c["survivor_offset_minmax"],
            "first_current_survivor_blocks": [r["block_index"] for r in c["first_projection_survivors"][:16]],
            "canonical": out["canonical_sha256_without_this_field"],
        }, sort_keys=True))
    elif not args.output:
        print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
