#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
BUNDLE_FILE = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING_FILE = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
HPERP_ADAPTER_FILE = HERE / "hperp_integral_adapter.py"
WITNESS_FILE = HERE / "post1588-hperp-nonexceptional-mod2-witness.json"
POST1563_FILE = HERE / "post1563-ambient-symmetry-exhaustion-batch.json"

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_HPERP_TEXT_SHA256 = "af373f16d6ab2bb8aed6ca09e0a15c8b28d565cbec6f242a8b76c590df81bb4f"
EXPECTED_ALL140_RETAINED_COORDS_SHA256 = "ba5aa10e67f1237c5fe6e79d7db5168d2041353ffa60b2801c7cde09222d7f9a"
EXPECTED_WITNESS_CANONICAL = "6adc55114e29720f2a89649d71381228711a58b80677d3cc6b753f54daa4b8c8"
EXPECTED_POST1563_CANONICAL = "9dbf0bcb144824a14497b663da2200f94d7250bfc755a37d1d65ca0b565fbb2e"
EXPECTED_AUT_GROUP_ORDER = 1536
KNOWN_CURVE_COUNT = 140
PICARD_RANK = 64
NORMAL_COUNT = 92


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def canonical_sha(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if claimed != calc:
        raise SystemExit(f"canonical mismatch: {claimed} != {calc}")
    return calc


def compose(p: list[int], q: list[int]) -> list[int]:
    return [q[p[j] - 1] for j in range(len(p))]


def power(p: list[int], n: int) -> list[int]:
    out = list(range(1, len(p) + 1))
    for _ in range(n):
        out = compose(out, p)
    return out


def close_group(generators: list[tuple[str, list[int]]]) -> dict[tuple[int, ...], str]:
    identity = tuple(range(1, KNOWN_CURVE_COUNT + 1))
    seen: dict[tuple[int, ...], str] = {identity: "1"}
    queue: deque[tuple[int, ...]] = deque([identity])
    while queue:
        p = queue.popleft()
        prefix = seen[p]
        for name, gp in generators:
            q = tuple(compose(list(p), gp))
            if q in seen:
                continue
            seen[q] = name if prefix == "1" else prefix + "*" + name
            queue.append(q)
    return seen


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
    sys.path.insert(0, str(HERE))
    hperp = load_module(HPERP_ADAPTER_FILE, "stage32_hperp_order3_adapter")
    bundle_mod = load_module(BUNDLE_FILE, "stage32_hperp_order3_bundle")
    marking_mod = load_module(MARKING_FILE, "stage32_hperp_order3_marking")
    bundle = bundle_mod.load()
    marking = marking_mod.load()

    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise SystemExit("retained Picard bundle canonical moved")
    if bundle.get("upstream_git_blob_sha1") != EXPECTED_UPSTREAM_BLOB:
        raise SystemExit("retained Picard upstream blob moved")

    adapter = hperp.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    cert = adapter.certificate
    if cert["hperp"]["hperp_text_sha256"] != EXPECTED_HPERP_TEXT_SHA256:
        raise SystemExit("retained Hperp text hash moved")
    if cert["all140_retained_coordinates_sha256"] != EXPECTED_ALL140_RETAINED_COORDS_SHA256:
        raise SystemExit("retained all140 Picard coordinates moved")
    if cert["known_curve_count"] != KNOWN_CURVE_COUNT or cert["picard_rank"] != PICARD_RANK:
        raise SystemExit("retained Hperp/Picard dimensions moved")

    witness = json.loads(WITNESS_FILE.read_text())
    if canonical_sha(witness) != EXPECTED_WITNESS_CANONICAL:
        raise SystemExit("post1588 repaired witness authority moved")
    deterministic = witness["deterministic_witness"]
    ranks = witness["mod2_rank_test"]
    if deterministic["normal_curve_label_1based"] != 1:
        raise SystemExit("post1588 deterministic witness moved")
    if deterministic["separator_support_retained_picard_coordinates_1based"] != [1]:
        raise SystemExit("post1588 separator support moved")
    if ranks["exceptional_rank_F2"] != 38 or not ranks["all_normal_known_curves_escape_exceptional_span"]:
        raise SystemExit("post1588 mod2 authority moved")
    if witness["fixed_target"]["surviving_residues_decimal"] != [73, 97, 235]:
        raise SystemExit("post1588 repaired Q602 survivor authority moved")

    post1563 = json.loads(POST1563_FILE.read_text())
    if canonical_sha(post1563) != EXPECTED_POST1563_CANONICAL:
        raise SystemExit("post1563 ambient symmetry authority moved")
    route_c = post1563["routes"]["C_principal_b3_membership"]
    if not post1563["decision"]["retained_stoll_full_aut_equality_proved"]:
        raise SystemExit("full retained Stoll=Aut(box) authority moved")
    if not route_c["beta_B_in_retained_stoll_group"] or route_c["beta_B_in_H"]:
        raise SystemExit("principal beta_B membership/outside-H authority moved")
    if route_c["principal_b3_order"] != 3:
        raise SystemExit("principal b3 order moved")
    if post1563["firewalls"]["explicit_beta_B_stoll_word_claimed"]:
        raise SystemExit("explicit beta_B Stoll word unexpectedly claimed")

    coords_matrix = adapter.class_coordinates_in_retained_basis
    if coords_matrix.shape != (KNOWN_CURVE_COUNT, PICARD_RANK):
        raise SystemExit(f"all140 retained coordinate shape moved: {coords_matrix.shape}")
    coords = [
        [int(coords_matrix[i, j]) for j in range(PICARD_RANK)]
        for i in range(KNOWN_CURVE_COUNT)
    ]

    # Replay post1588 in the exact coordinate convention that produced it.
    if coords[0][0] % 2 != 1:
        raise SystemExit("retained coordinate 1 no longer detects label1")
    if any(coords[j][0] % 2 for j in range(NORMAL_COUNT, KNOWN_CURVE_COUNT)):
        raise SystemExit("retained coordinate 1 no longer annihilates all exceptionals")
    exceptional_basis = f2_basis(
        [f2_mask(coords[j]) for j in range(NORMAL_COUNT, KNOWN_CURVE_COUNT)]
    )
    if len(exceptional_basis) != 38:
        raise SystemExit("exceptional F2 rank moved")

    aut = marking["aut_action"]
    if aut["schema"] != "STAGE32_AUT_PERM_SOURCELOCK_V1":
        raise SystemExit("retained Aut action schema moved")
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != KNOWN_CURVE_COUNT for p in perms):
        raise SystemExit("retained Stoll generator permutation shape moved")

    group = close_group([(f"g{i}", perms[i - 1]) for i in range(1, 10)])
    if len(group) != EXPECTED_AUT_GROUP_ORDER:
        raise SystemExit(f"retained Stoll group order moved: {len(group)}")

    identity = list(range(1, KNOWN_CURVE_COUNT + 1))
    order3: list[tuple[tuple[int, ...], str]] = []
    for p_tuple, word in group.items():
        p = list(p_tuple)
        if p != identity and power(p, 3) == identity:
            order3.append((p_tuple, word))

    witness_mask = f2_mask(coords[0])
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
        moved_mask = f2_mask(coords[image - 1])
        if in_f2_span(moved_mask ^ witness_mask, exceptional_basis):
            fixed_quotient.append(word)
        if coords[image - 1][0] % 2 == 1:
            separator_same.append(word)
        else:
            separator_flipped.append(word)

    image_list = sorted(images)
    normal_images = [x for x in image_list if 1 <= x <= NORMAL_COUNT]
    exceptional_images = [x for x in image_list if NORMAL_COUNT < x <= KNOWN_CURVE_COUNT]
    all_order3_move_label = not fixed_label
    all_order3_move_quotient = not fixed_quotient
    all_order3_flip_separator = not separator_same

    result = {
        "schema": "STAGE32_HPERP_ORDER3_LABEL1_ACTION_DIAGNOSTIC_V3_EXACT_RETAINED_BASIS",
        "source_lock": {
            "post1588_canonical_sha256": EXPECTED_WITNESS_CANONICAL,
            "post1563_canonical_sha256": EXPECTED_POST1563_CANONICAL,
            "hperp_adapter_canonical_sha256": cert["canonical_sha256_without_this_field"],
            "all140_retained_coordinates_sha256": cert["all140_retained_coordinates_sha256"],
        },
        "retained_stoll_group_order": len(group),
        "retained_stoll_generator_count": len(perms),
        "principal_b3_retained_input": {
            "membership_in_full_stoll_group": True,
            "outside_H": True,
            "order": 3,
            "explicit_stoll_word_source_locked": False,
            "candidate_superset": "all_nonidentity_order3_elements_of_retained_full_Stoll1536",
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
            "surviving_residues_decimal": [73, 97, 235],
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
