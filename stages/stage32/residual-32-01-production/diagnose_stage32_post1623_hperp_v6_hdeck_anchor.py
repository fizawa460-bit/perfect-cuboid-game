#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OLD = HERE / "diagnose_stage32_post1566_orbit_sum_commutator.py"
HPERP = HERE / "post1588-hperp-nonexceptional-mod2-witness.json"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
H_DECK = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json"

EXPECTED_OLD_BLOB = "53e9f81813af13637ce62d4bd8770b81b4b23fb2"
EXPECTED_HPERP = "6adc55114e29720f2a89649d71381228711a58b80677d3cc6b753f54daa4b8c8"
EXPECTED_V6 = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_H_DECK = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"
EXPECTED_SURVIVORS = [73, 97, 235]
EXPECTED_HWORDS = {"u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"}
H_ORDER = ("id", "u", "v", "uv")
AFFINE_CHARACTER_PROFILES = {
    "chi_u": [0, 1, 0, 1],
    "1+chi_u": [1, 0, 1, 0],
    "chi_v": [0, 0, 1, 1],
    "1+chi_v": [1, 1, 0, 0],
    "chi_uv": [0, 1, 1, 0],
    "1+chi_uv": [1, 0, 0, 1],
}


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_old():
    if blob_sha1(OLD) != EXPECTED_OLD_BLOB:
        raise SystemExit("retained Stoll/Picard diagnostic blob moved")
    spec = importlib.util.spec_from_file_location("stage32_post1623_old", OLD)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot import retained Stoll/Picard diagnostic")
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def f2_mask(row) -> int:
    out = 0
    for j, x in enumerate(row):
        if int(x) & 1:
            out |= 1 << j
    return out


def triangular_basis(rows: list[int]) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for value in rows:
        x = value
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return pivots


def reduce_by_basis(value: int, pivots: dict[int, int]) -> int:
    x = value
    while x:
        p = x.bit_length() - 1
        if p not in pivots:
            return x
        x ^= pivots[p]
    return 0


def main() -> None:
    old = load_old()
    hperp = json.loads(HPERP.read_text(encoding="utf-8"))
    v6 = json.loads(V6.read_text(encoding="utf-8"))
    hdeck = json.loads(H_DECK.read_text(encoding="utf-8"))
    for obj, expected, name in [
        (hperp, EXPECTED_HPERP, "Hperp witness"),
        (v6, EXPECTED_V6, "V6 witness"),
        (hdeck, EXPECTED_H_DECK, "H-deck adapter"),
    ]:
        if old.canonical_sha(obj) != expected:
            raise SystemExit(f"{name} canonical moved")

    if hperp["fixed_target"]["surviving_residues_decimal"] != EXPECTED_SURVIVORS:
        raise SystemExit("audited survivor set moved")
    witness = hperp["deterministic_witness"]
    if witness["normal_curve_label_1based"] != 1:
        raise SystemExit("deterministic Hperp witness label moved")
    if witness["separator_support_retained_picard_coordinates_1based"] != [1]:
        raise SystemExit("Hperp separator support moved")
    if not witness["separator_annihilates_all_48_exceptional_classes"]:
        raise SystemExit("Hperp separator no longer annihilates exceptionals")

    h = old.load_picard_helper()
    aut = h.marking["aut_action"]
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != 140 for p in perms):
        raise SystemExit("retained Stoll action shape moved")
    group = old.close_group([(f"g{i}", perms[i - 1]) for i in range(1, 10)])
    if len(group) != 1536:
        raise SystemExit("retained Stoll group order moved")

    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    if hwords != EXPECTED_HWORDS:
        raise SystemExit("retained H-deck words moved")
    identity = list(range(1, 141))
    hperms = {"id": identity}
    for name in ("u", "v", "uv"):
        hperms[name] = old.perm_for_word(hwords[name], perms)
    if len(old.close_group([(name, hperms[name]) for name in ("u", "v")])) != 4:
        raise SystemExit("retained H-deck group order moved")

    exceptional_labels = set(range(93, 141))
    for name, p in hperms.items():
        if {p[j - 1] for j in exceptional_labels} != exceptional_labels:
            raise SystemExit(f"H element {name} moved exceptional block")

    b = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(b) != 140 or b[0] != 13:
        raise SystemExit("V6 all140 pairing source moved")
    gram_inv = h.invert_matrix(h.gram)
    exceptional_rows = [f2_mask(h.known[j - 1]) for j in range(93, 141)]
    exceptional_basis = triangular_basis(exceptional_rows)
    if len(exceptional_basis) != 38:
        raise SystemExit("exceptional F2 rank moved")

    records = []
    moved_masks = []
    moved_pairings_by_h = {}
    for name in H_ORDER:
        p = hperms[name]
        moved_pairings = old.transform(b, p)
        moved_pairings_by_h[name] = moved_pairings
        moved_coords = h.integral_row(
            h.row_times_fraction_matrix([moved_pairings[j - 1] for j in h.INDLIST], gram_inv),
            f"V6 {name} translate",
        )
        mask = f2_mask(moved_coords)
        moved_masks.append(mask)
        pinv = old.inverse(p)
        records.append({
            "h_element": name,
            "stoll_word": "1" if name == "id" else hwords[name],
            "pullback_of_normal_label_1_1based": int(pinv[0]),
            "v6_translate_intersection_with_normal_label_1": int(moved_pairings[0]),
            "v6_translate_intersection_with_normal_label_1_mod2": int(moved_pairings[0]) & 1,
            "hperp_separator_coordinate_1_value_mod2": int(moved_coords[0]) & 1,
            "translate_outside_exceptional_span_mod2": reduce_by_basis(mask, exceptional_basis) != 0,
        })

    profile_to_labels = {}
    normal_profiles = []
    for label in range(1, 93):
        profile = [int(moved_pairings_by_h[name][label - 1]) & 1 for name in H_ORDER]
        key = "".join(str(x) for x in profile)
        profile_to_labels.setdefault(key, []).append(label)
        normal_profiles.append((label, profile))
    profile_distribution = {key: len(labels) for key, labels in sorted(profile_to_labels.items())}
    nonconstant = [(label, profile) for label, profile in normal_profiles if len(set(profile)) > 1]
    character_hits = {}
    for cname, target in AFFINE_CHARACTER_PROFILES.items():
        character_hits[cname] = [label for label, profile in normal_profiles if profile == target]
    first_character_hit = next(
        (
            {"normal_label_1based": label, "character": cname, "profile_id_u_v_uv": profile}
            for label, profile in normal_profiles
            for cname, target in AFFINE_CHARACTER_PROFILES.items()
            if profile == target
        ),
        None,
    )

    orbit_sum_mask = 0
    for mask in moved_masks:
        orbit_sum_mask ^= mask
    result = {
        "schema": "STAGE32_POST1623_HPERP_V6_HDECK_COMMON_ANCHOR_DIAGNOSTIC_V2",
        "fixed_target": {"Q": 602, "surviving_residues_decimal": EXPECTED_SURVIVORS},
        "hperp_witness": {"normal_curve_label_1based": 1, "separator_support_1based": [1]},
        "v6_hdeck_translate_records": records,
        "all_92_normal_curve_intersection_parity_profiles": {
            "coordinate_order": list(H_ORDER),
            "distinct_profile_count": len(profile_to_labels),
            "profile_distribution": profile_distribution,
            "nonconstant_profile_label_count": len(nonconstant),
            "first_nonconstant_profile": (
                {"normal_label_1based": nonconstant[0][0], "profile_id_u_v_uv": nonconstant[0][1]}
                if nonconstant else None
            ),
            "nontrivial_affine_H_character_label_sets": character_hits,
            "first_nontrivial_affine_H_character_hit": first_character_hit,
        },
        "h_orbit_sum": {
            "separator_coordinate_1_value_mod2": (orbit_sum_mask >> 0) & 1,
            "outside_exceptional_span_mod2": reduce_by_basis(orbit_sum_mask, exceptional_basis) != 0,
        },
        "type_firewall": {
            "picard_quotient_dimension_from_retained_all140": 26,
            "q602_operator_module_dimension": 4,
            "direct_residue_matrix_action_on_picard_witness_defined": False,
            "picard_to_q602_operator_adapter_materialized": False,
            "q602_residue_specific_commutator_obtained": False,
            "Q602_excluded": False,
            "O210_excluded": False,
        },
        "next_exact_route": "SOURCE_BIND_A_NONTRIVIAL_NORMAL_CURVE_H_CHARACTER_PROFILE_TO_THE_RETAINED_W_LINE_OR_CORRESPONDENCE_J2_OPERATOR_MODULE_OR_STOP_AT_TYPED_ADAPTER_GAP",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
