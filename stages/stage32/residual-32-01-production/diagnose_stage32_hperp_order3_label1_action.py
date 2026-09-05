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


def main() -> None:
    d = load_source()
    h = d.load_picard_helper()
    aut = h.marking["aut_action"]
    if aut["schema"] != "STAGE32_AUT_PERM_SOURCELOCK_V1":
        raise SystemExit("retained Aut action schema moved")
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != 140 for p in perms):
        raise SystemExit("retained Stoll generator permutation shape moved")

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

    fixed = [(word, list(p_tuple)) for p_tuple, word in order3 if p_tuple[0] == 1]
    moved = [(word, list(p_tuple)) for p_tuple, word in order3 if p_tuple[0] != 1]
    images = sorted({p_tuple[0] for p_tuple, _ in order3})
    normal_images = [x for x in images if 1 <= x <= 92]
    exceptional_images = [x for x in images if 93 <= x <= 140]

    result = {
        "schema": "STAGE32_HPERP_ORDER3_LABEL1_ACTION_DIAGNOSTIC_V1",
        "retained_stoll_group_order": len(group),
        "retained_stoll_generator_count": len(perms),
        "principal_b3_retained_input": {
            "membership_in_full_stoll_group": True,
            "order": 3,
            "explicit_stoll_word_source_locked": False,
        },
        "hperp_witness": {
            "normal_curve_label_1based": 1,
        },
        "order3_sweep": {
            "order3_element_count": len(order3),
            "fix_label1_count": len(fixed),
            "move_label1_count": len(moved),
            "label1_image_set": images,
            "normal_image_set": normal_images,
            "exceptional_image_set": exceptional_images,
            "all_order3_move_label1": len(fixed) == 0,
            "all_order3_preserve_normal_block_at_label1": len(exceptional_images) == 0,
            "sample_fixing_words": [word for word, _ in fixed[:12]],
            "sample_moving_words": [word for word, _ in moved[:12]],
        },
        "decision_boundary": {
            "principal_b3_label1_action_identified": len(fixed) == 0,
            "reason_if_not_identified": (
                "ORDER3_MEMBERSHIP_DOES_NOT_DETERMINE_LABEL1_ACTION"
                if fixed
                else "ALL_ORDER3_ELEMENTS_MOVE_LABEL1"
            ),
            "q602_residue_elimination_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
