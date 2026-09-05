#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_FILE = HERE / "diagnose_stage32_hperp_order3_label1_action.py"
POST1550_FILE = HERE / "post1550-b3-v4-torsor-normalizer.json"
H_ASSET_FILE = HERE / "post1532-full-stoll-h-orbit-symmetry-negative.json"

EXPECTED_POST1550_CANONICAL = "1225ca34034f1f1dacb2f3e1f46e7f3d15a6008a5e6b03960109f7bc992b5e95"
EXPECTED_H_ASSET_CANONICAL = "6067bf47c856561917de355c0bb734580846f06fd3beaa81f43297721ca241aa"
EXPECTED_H_WORDS = {"id": "1", "u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def inverse(p: list[int]) -> list[int]:
    out = [0] * len(p)
    for i, image in enumerate(p, start=1):
        out[image - 1] = i
    return out


def main() -> None:
    base = load_module(BASE_FILE, "stage32_hperp_order3_base")
    post1550 = json.loads(POST1550_FILE.read_text())
    h_asset = json.loads(H_ASSET_FILE.read_text())
    if base.canonical_sha(post1550) != EXPECTED_POST1550_CANONICAL:
        raise SystemExit("post1550 canonical moved")
    if base.canonical_sha(h_asset) != EXPECTED_H_ASSET_CANONICAL:
        raise SystemExit("retained H asset canonical moved")

    principal = post1550["principal_b3"]
    if principal["restriction_order"] != 3 or not principal["W_invariant"]:
        raise SystemExit("principal b3 W action contract moved")
    if principal["restriction_to_W"] != [[1, 1], [1, 0]]:
        raise SystemExit("principal b3 W matrix moved")
    if h_asset["finite_result"]["h_deck_words"] != EXPECTED_H_WORDS:
        raise SystemExit("retained H words moved")
    if h_asset["finite_result"]["h_deck_group_order"] != 4:
        raise SystemExit("retained H order moved")

    marking_mod = base.load_module(base.MARKING_FILE, "stage32_hnormalizer_marking")
    bundle_mod = base.load_module(base.BUNDLE_FILE, "stage32_hnormalizer_bundle")
    hperp_mod = base.load_module(base.HPERP_ADAPTER_FILE, "stage32_hnormalizer_hperp")
    marking = marking_mod.load()
    bundle = bundle_mod.load()
    adapter = hperp_mod.HperpIntegralPairingAdapter.from_retained(marking, bundle)

    perms = [[int(x) for x in p] for p in marking["aut_action"]["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != base.KNOWN_CURVE_COUNT for p in perms):
        raise SystemExit("retained Stoll generators moved")
    group = base.close_group([(f"g{i}", perms[i - 1]) for i in range(1, 10)])
    if len(group) != base.EXPECTED_AUT_GROUP_ORDER:
        raise SystemExit("retained Stoll group order moved")

    identity = list(range(1, base.KNOWN_CURVE_COUNT + 1))

    def word(indices: tuple[int, ...]) -> list[int]:
        out = identity
        for i in indices:
            out = base.compose(out, perms[i - 1])
        return out

    h_perms = {
        "id": identity,
        "u": word((7, 9)),
        "v": word((7, 8)),
        "uv": word((8, 9)),
    }
    h_lookup = {tuple(p): name for name, p in h_perms.items()}
    if len(h_lookup) != 4:
        raise SystemExit("retained H permutations are not four distinct elements")
    for a in h_perms.values():
        for b in h_perms.values():
            if tuple(base.compose(a, b)) not in h_lookup:
                raise SystemExit("retained H words do not close as a subgroup")

    coords_matrix = adapter.class_coordinates_in_retained_basis
    coords = [
        [int(coords_matrix[i, j]) for j in range(base.PICARD_RANK)]
        for i in range(base.KNOWN_CURVE_COUNT)
    ]
    exceptional_basis = base.f2_basis(
        [base.f2_mask(coords[j]) for j in range(base.NORMAL_COUNT, base.KNOWN_CURVE_COUNT)]
    )
    witness_mask = base.f2_mask(coords[0])

    candidates: list[dict] = []
    order3_count = 0
    h_normalizing_order3_count = 0
    for p_tuple, word_name in group.items():
        p = list(p_tuple)
        if p == identity or base.power(p, 3) != identity:
            continue
        order3_count += 1
        pinv = inverse(p)
        induced: dict[str, str] = {}
        normalizes = True
        for hname, h in h_perms.items():
            # p h p^-1 in the concrete retained permutation action.
            conj = base.compose(base.compose(pinv, h), p)
            cname = h_lookup.get(tuple(conj))
            if cname is None:
                normalizes = False
                break
            induced[hname] = cname
        if not normalizes:
            continue
        h_normalizing_order3_count += 1
        cycles_nonidentity = all(induced[name] != name for name in ("u", "v", "uv"))
        if not cycles_nonidentity:
            continue

        image = p[0]
        moved_mask = base.f2_mask(coords[image - 1])
        candidates.append({
            "word": word_name,
            "label1_image": image,
            "fixes_label1": image == 1,
            "fixes_label1_mod_exceptional_span": base.in_f2_span(moved_mask ^ witness_mask, exceptional_basis),
            "separator_same": bool(coords[image - 1][0] % 2),
            "H_conjugation": induced,
        })

    label_images = sorted({c["label1_image"] for c in candidates})
    fixed_label = [c for c in candidates if c["fixes_label1"]]
    fixed_quotient = [c for c in candidates if c["fixes_label1_mod_exceptional_span"]]
    separator_same = [c for c in candidates if c["separator_same"]]

    result = {
        "schema": "STAGE32_HPERP_B3_H_NORMALIZER_ACTION_DIAGNOSTIC_V1",
        "source_lock": {
            "post1550_canonical_sha256": EXPECTED_POST1550_CANONICAL,
            "retained_H_asset_canonical_sha256": EXPECTED_H_ASSET_CANONICAL,
            "post1588_canonical_sha256": base.EXPECTED_WITNESS_CANONICAL,
            "retained_all140_coordinates_sha256": adapter.certificate["all140_retained_coordinates_sha256"],
        },
        "semantic_constraint": {
            "principal_b3_preserves_W_equal_H_dual": True,
            "principal_b3_action_on_W_has_order": 3,
            "basis_free_deck_consequence": "conjugation normalizes H and cycles its three nonidentity elements",
            "H_words": EXPECTED_H_WORDS,
        },
        "finite_filter": {
            "retained_stoll_group_order": len(group),
            "order3_element_count": order3_count,
            "H_normalizing_order3_count": h_normalizing_order3_count,
            "H_cycling_order3_candidate_count": len(candidates),
            "label1_image_set": label_images,
            "label1_image_cardinality": len(label_images),
            "fix_label1_count": len(fixed_label),
            "move_label1_count": len(candidates) - len(fixed_label),
            "fix_label1_mod_exceptional_span_count": len(fixed_quotient),
            "move_label1_mod_exceptional_span_count": len(candidates) - len(fixed_quotient),
            "separator_same_count": len(separator_same),
            "separator_flip_count": len(candidates) - len(separator_same),
            "sample_candidates": candidates[:16],
        },
        "decision_boundary": {
            "exact_principal_b3_member_identified": len(candidates) == 1,
            "exact_principal_b3_label1_image_identified": len(label_images) == 1,
            "principal_b3_label1_noninvariance_forced": bool(candidates) and not fixed_label,
            "principal_b3_quotient_noninvariance_forced": bool(candidates) and not fixed_quotient,
            "principal_b3_separator_flip_forced": bool(candidates) and not separator_same,
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
