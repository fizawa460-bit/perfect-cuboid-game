#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter
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


def rhs_bmask(kernel, exceptional, boundary_normal) -> int:
    bmask = 0
    for eq, h in enumerate(kernel):
        rhs = 0
        for label, value in exceptional.items():
            rhs ^= (h[label - 1] & 1) & (int(value) & 1)
        for label, value in boundary_normal.items():
            rhs ^= (h[label - 1] & 1) & (int(value) & 1)
        if rhs:
            bmask |= 1 << eq
    if sum(int(v) for v in boundary_normal.values()) & 1:
        bmask |= 1 << len(kernel)
    return bmask


def projected_row_coefficients(kernel, mask: int) -> list[int]:
    coeff = [0] * 140
    for eq, h in enumerate(kernel):
        if (mask >> eq) & 1:
            coeff = [a ^ (int(b) & 1) for a, b in zip(coeff, h)]
    if (mask >> len(kernel)) & 1:
        for label in range(1, base.NORMAL_COUNT + 1):
            coeff[label - 1] ^= 1
    return coeff


def exact_cover(cover_bits: list[int], universe: int, max_size: int = 6):
    useful = [i for i, bits in enumerate(cover_bits) if bits]
    for size in range(1, min(max_size, len(useful)) + 1):
        for combo in itertools.combinations(useful, size):
            union = 0
            for i in combo:
                union |= cover_bits[i]
            if union == universe:
                return list(combo)
    return None


def greedy_cover(cover_bits: list[int], universe: int) -> list[int]:
    uncovered = universe
    chosen: list[int] = []
    while uncovered:
        best = None
        best_gain = 0
        for i, bits in enumerate(cover_bits):
            if i in chosen:
                continue
            gain = (bits & uncovered).bit_count()
            if gain > best_gain:
                best = i
                best_gain = gain
        req(best is not None and best_gain > 0, "GF2 row family failed to cover contradiction universe")
        chosen.append(best)
        uncovered &= ~cover_bits[best]
    return chosen


def run() -> dict:
    P, blocks = base.load_picard_interface()
    kernel = base.left_kernel_mod2(P)
    boundary_labels = sorted({b for pack in base.PACKS for b in pack})
    unknown_normal_labels = [
        label for label in range(1, base.NORMAL_COUNT + 1) if label not in boundary_labels
    ]
    masks = base.consistency_masks(kernel, unknown_normal_labels)
    idx = base.e8.indexer()

    row_coeffs = [projected_row_coefficients(kernel, mask) for mask in masks]
    for i, coeff in enumerate(row_coeffs):
        req(
            all(coeff[label - 1] == 0 for label in unknown_normal_labels),
            f"projected row {i} retained an eliminated normal coefficient",
        )

    cover_bits = [0] * len(masks)
    violation_pattern_hist = Counter()
    configuration_count = 0
    targeted_blocks = 0
    fibre_empty_blocks = 0
    targeted_by_mass = Counter()
    configs_by_mass = Counter()
    configs_by_fibre = Counter()
    target_h = hashlib.sha256()
    config_h = hashlib.sha256()

    for block_index in range(base.e8.UNFILTERED_BLOCK_COUNT):
        sig = base.e8.block_signature(block_index, idx)
        mass = int(sig["fixed_exceptional_mass"])
        groups = [int(v) for v in sig["n355_known_group_sums"]]
        if mass < 7 or groups[2] != 3:
            continue
        targeted_blocks += 1
        targeted_by_mass[mass] += 1
        target_h.update(f"{block_index}\n".encode())
        fixed = {int(k): int(v) for k, v in sig["fixed_exceptional_pairings"].items()}
        had_configuration = False
        for residual_label, exceptional in base.exceptional_completions(fixed):
            for n1, n2, boundary, sums in base.boundary_candidates(exceptional, blocks):
                had_configuration = True
                ordinal = configuration_count
                configuration_count += 1
                configs_by_mass[mass] += 1
                configs_by_fibre[(n1, n2)] += 1
                bmask = rhs_bmask(kernel, exceptional, boundary)
                violated = tuple(
                    i for i, mask in enumerate(masks)
                    if ((mask & bmask).bit_count() & 1)
                )
                req(violated, f"g3 target projection survivor at block {block_index}")
                violation_pattern_hist[violated] += 1
                for i in violated:
                    cover_bits[i] |= 1 << ordinal
                config_h.update(
                    json.dumps({
                        "block": block_index,
                        "mass": mass,
                        "residual_label": residual_label,
                        "fibre": [n1, n2],
                        "incidence_sums": sums,
                        "violated_rows": list(violated),
                    }, sort_keys=True, separators=(",", ":")).encode() + b"\n"
                )
        if not had_configuration:
            fibre_empty_blocks += 1
            config_h.update(f"EMPTY:{block_index}\n".encode())

    req(targeted_blocks == 1852, "g3 full-e8 target-count drift")
    req(targeted_by_mass == Counter({8: 1264, 7: 588}), "g3 mass split drift")

    universal_rows = []
    exact = None
    greedy = []
    chosen = []
    if configuration_count:
        universe = (1 << configuration_count) - 1
        req(
            all(any((bits >> ordinal) & 1 for bits in cover_bits) for ordinal in range(configuration_count)),
            "at least one exact g3 configuration lacks a GF2 contradiction row",
        )
        universal_rows = [i for i, bits in enumerate(cover_bits) if bits == universe]
        exact = exact_cover(cover_bits, universe, max_size=6)
        greedy = greedy_cover(cover_bits, universe)
        chosen = exact if exact is not None else greedy
        status = "PASS_SINGLE_UNIVERSAL_GF2_ROW" if universal_rows else "PASS_FINITE_GF2_ROW_COVER"
    else:
        req(fibre_empty_blocks == targeted_blocks, "mixed fibre-empty accounting drift")
        status = "PASS_G3_PRE_GF2_FIBRE_EMPTY"

    row_records = []
    for i, (mask, coeff, coverage) in enumerate(zip(masks, row_coeffs, cover_bits)):
        labels = [j + 1 for j, bit in enumerate(coeff) if bit]
        row_records.append({
            "row_index": i,
            "transform_mask_hex": hex(mask),
            "covered_configurations": coverage.bit_count(),
            "coverage_fraction": f"{coverage.bit_count()}/{configuration_count}",
            "normal_labels": [label for label in labels if label <= base.NORMAL_COUNT],
            "exceptional_labels": [label for label in labels if label > base.NORMAL_COUNT],
            "coefficient_support": len(labels),
            "coefficient_stream_sha256": csha(labels),
        })

    out = {
        "schema": "STAGE32_CERTLIFT_G3_GF2_ROW_CERTIFICATE_V2",
        "stage": "32",
        "node": "CERTLIFT-03",
        "status": status,
        "hypothesis": "e=8,d=8,fixed_exceptional_mass>=7,g3=sum(y93,y94,y95,y96)=3",
        "scope": {
            "unfiltered_e8_blocks": base.e8.UNFILTERED_BLOCK_COUNT,
            "targeted_blocks": targeted_blocks,
            "targeted_by_mass": {str(k): v for k, v in sorted(targeted_by_mass.items())},
            "fibre_empty_blocks": fibre_empty_blocks,
            "post_fibre_projected_configurations": configuration_count,
            "configurations_by_mass": {str(k): v for k, v in sorted(configs_by_mass.items())},
            "configurations_by_fibre_degrees": {
                f"{k[0]},{k[1]}": v for k, v in sorted(configs_by_fibre.items())
            },
            "target_block_stream_sha256": target_h.hexdigest(),
            "configuration_stream_sha256": config_h.hexdigest(),
        },
        "projection": {
            "left_kernel_dimension_mod2": len(kernel),
            "eliminated_nonboundary_normal_count": len(unknown_normal_labels),
            "consistency_row_count": len(masks),
            "consistency_masks_sha256": csha(masks),
            "universal_row_indices": universal_rows,
            "exact_cover_size_up_to_6": None if exact is None else len(exact),
            "exact_cover_row_indices": exact,
            "greedy_cover_size": len(greedy),
            "greedy_cover_row_indices": greedy,
            "chosen_row_indices": chosen,
            "violation_pattern_count": len(violation_pattern_hist),
            "rows": row_records,
        },
        "interpretation": {
            "pre_gf2_fibre_obstruction": configuration_count == 0,
            "meaning": "If post_fibre_projected_configurations=0, the exact exceptional mass and fibre equalities already contradict the hypothesis before any Picard64 column-image parity row is used.",
            "next_gate": "Derive the fibre contradiction directly from incidence-sum parity/degree equations under fixed_mass>=7 and g3=3.",
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()
    out = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    if args.self_check:
        p = out["projection"]
        rows = {r["row_index"]: r for r in p["rows"]}
        print(json.dumps({
            "status": out["status"],
            "targeted_blocks": out["scope"]["targeted_blocks"],
            "fibre_empty_blocks": out["scope"]["fibre_empty_blocks"],
            "post_fibre_configurations": out["scope"]["post_fibre_projected_configurations"],
            "consistency_rows": p["consistency_row_count"],
            "universal_rows": p["universal_row_indices"],
            "chosen_rows": [rows[i] for i in p["chosen_row_indices"]],
            "canonical": out["canonical_sha256_without_this_field"],
        }, sort_keys=True))
    elif not args.output:
        print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
