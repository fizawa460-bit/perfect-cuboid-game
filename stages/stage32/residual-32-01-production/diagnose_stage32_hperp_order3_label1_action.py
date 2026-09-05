#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "diagnose_stage32_post1566_orbit_sum_commutator.py"


def load_source():
    spec = importlib.util.spec_from_file_location("stage32_post1566_diag", SOURCE)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load retained post1566 diagnostic")
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def power(mod, p: list[int], n: int) -> list[int]:
    out = list(range(1, len(p) + 1))
    for _ in range(n):
        out = mod.compose(out, p)
    return out


def f2_mask(row: list[int]) -> int:
    out = 0
    for i, value in enumerate(row):
        if int(value) & 1:
            out |= 1 << i
    return out


def f2_basis(masks: list[int]) -> dict[int, int]:
    basis: dict[int, int] = {}
    for value in masks:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return basis


def in_f2_span(value: int, basis: dict[int, int]) -> bool:
    x = value
    while x:
        pivot = x.bit_length() - 1
        if pivot not in basis:
            return False
        x ^= basis[pivot]
    return True


def main() -> None:
    d = load_source()
    h = d.load_picard_helper()
    aut = h.marking["aut_action"]
    if aut["schema"] != "STAGE32_AUT_PERM_SOURCELOCK_V1":
        raise SystemExit("retained Aut action schema moved")
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != 140 for p in perms):
        raise SystemExit("retained Stoll generator permutation shape moved")
    known = [[int(x) for x in row] for row in h.known]
    if len(known) != 140 or any(len(row) != 64 for row in known):
        raise SystemExit("retained all140 Picard coordinate shape moved")

    # Replay the post1588 separator support [1] directly in the retained basis.
    if known[0][0] % 2 != 1:
        raise SystemExit("label1 is no longer detected by separator coordinate 1")
    if any(known[j][0] % 2 for j in range(92, 140)):
        raise SystemExit("separator coordinate 1 no longer annihilates all exceptionals")
    exceptional_basis = f2_basis([f2_mask(known[j]) for j in range(92, 140)])
    if len(exceptional_basis) != 38:
        raise SystemExit("exceptional F2 rank moved")

    group = d.close_group([(f"g{i}", perms[i - 1]) for i in range(1, 10)])
    if len(group) != d.EXPECTED_AUT_GROUP_ORDER:
        raise SystemExit("retained Stoll group order moved")

    identity = list(range(1, 141))
    order3: list[tuple[tuple[int, ...], str]] = []
    for p_tuple, word in group.items():
        p = list(p_tuple)
        if p == identity:
            continue
        if power(d, p, 3) == identity:
            order3.append((p_tuple, word))

    witness_mask = f2_mask(known[0])
    fixed_label: list[str] = []
    fixed_quotient: list[str] = []
    separator_same: list[str] = []
    separator_flipped: list[str] = []
    images: set[int] = set()
    for p_tuple, word in order3:
        image = p_tuple[0]
        images.add(image)
        if image == 1:
            fixed_label.append(word)
        moved_mask = f2_mask(known[image - 1])
        if in_f2_span(moved_mask ^ witness_mask, exceptional_basis):
            fixed_quotient.append(word)
        if known[image - 1][0] % 2 == 1:
            separator_same.append(word)
        else:
            separator_flipped.append(word)

    image_list = sorted(images)
    normal_images = [x for x in image_list if 1 <= x <= 92]
    exceptional_images = [x for x in image_list if 93 <= x <= 140]
    all_order3_move_label = not fixed_label
    all_order3_move_quotient = not fixed_quotient
    all_order3_flip_separator = not separator_same

    result = {
        "schema": "STAGE32_HPERP_ORDER3_LABEL1_ACTION_DIAGNOSTIC_V2",
        "retained_stoll_group_order": len(group),
        "retained_stoll_generator_count": len(perms),
        "principal_b3_retained_input": {
            "membership_in_full_stoll_group": True,
            "order": 3,
            "explicit_stoll_word_source_locked": False,
        },
        "hperp_witness": {
            "normal_curve_label_1based": 1,
            "separator_support_retained_picard_coordinates_1based": [1],
            "exceptional_rank_F2": len(exceptional_basis),
        },
        "order3_sweep": {
            "order3_element_count": len(order3),
            "fix_label1_count": len(fixed_label),
            "move_label1_count": len(order3) - len(fixed_label),
            "fix_label1_mod_exceptional_span_count": len(fixed_quotient),
            "move_label1_mod_exceptional_span_count": len(order3) - len(fixed_quotient),
            "separator_same_count": len(separator_same),
            "separator_flip_count": len(separator_flipped),
            "label1_image_set": image_list,
            "normal_image_set": normal_images,
            "exceptional_image_set": exceptional_images,
            "all_order3_move_label1": all_order3_move_label,
            "all_order3_move_label1_mod_exceptional_span": all_order3_move_quotient,
            "all_order3_flip_post1588_separator": all_order3_flip_separator,
            "sample_label_fixing_words": fixed_label[:12],
            "sample_quotient_fixing_words": fixed_quotient[:12],
            "sample_separator_same_words": separator_same[:12],
        },
        "decision_boundary": {
            "exact_principal_b3_label1_image_identified": len(image_list) == 1,
            "principal_b3_label1_noninvariance_forced_by_membership_order": all_order3_move_label,
            "principal_b3_quotient_noninvariance_forced_by_membership_order": all_order3_move_quotient,
            "principal_b3_separator_flip_forced_by_membership_order": all_order3_flip_separator,
            "residue_specific_commutator_obtained": False,
            "q602_residue_elimination_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
