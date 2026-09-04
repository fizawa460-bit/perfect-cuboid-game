#!/usr/bin/env python3
"""Certify Stage32 post1563 ambient-symmetry exhaustion batch."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

CERT = HERE / "post1563-ambient-symmetry-exhaustion-batch.json"
SOURCE_NOTE = HERE / "post1563-ambient-symmetry-exhaustion-batch-source-note.md"

EXPECTED_CERT_CANONICAL = "9dbf0bcb144824a14497b663da2200f94d7250bfc755a37d1d65ca0b565fbb2e"
EXPECTED_SOURCE_NOTE_BLOB = "4884ff210577a2d83e2c1aba9c778334ef166bb9"

LOCKS = {
    "stages/stage32/residual-32-01-production/post1561-b3-picard-action-adapter-gap.json":
        ("861d0eab190b66b5a6511b7d1c467f23978cbb17",
         "72945b0cd9d5a7e9e7e40e35bb6bd0cea79b7fafcfda8ea8d31af527c1e04b38"),
    "stages/stage32/residual-32-01-production/post1555-b3-full-g-box-quotient-normalizer.json":
        ("5b93e49f1114a0cc1423eaff70b29e96af1c489d",
         "4d2eacaca1ccb8db9bf0143e57fd39c9d8bb47a7180db8b9cd37533e5d5f7c38"),
    "stages/stage32/residual-32-01-production/post1532-full-stoll-h-orbit-symmetry-negative.json":
        ("809e1186b2da2ece267b1418a51289bbb174c55c",
         "6067bf47c856561917de355c0bb734580846f06fd3beaa81f43297721ca241aa"),
    "stages/stage32/residual-32-01-production/post1532-q602-single-b3-commutator.json":
        ("8699cdf52bff82304485a0544131e461b78c1fa6",
         "a374defb3a888c131ce92db9416702f34a03eb780b76d1dd6c26ab019f3c5064"),
    "stages/stage32/residual-32-01-production/post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json":
        ("9cd6d7122b8a3149b8ab79396946d72b986649df",
         "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"),
}

BLOB_ONLY_LOCKS = {
    "stages/stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-source-note.md":
        "deeecac5599f3b542b445cd87c2070dae488bc85",
    "docs/arsenal/index.json":
        "aa45d19c2f1d8970c7f142bf744c5c17e75abe5a",
    "docs/arsenal/cards/formal/S30-W01.md":
        "0b0d8871ce873896e62e841deb698f3c505abda5",
    "docs/arsenal/cards/formal/S30-W02.md":
        "9960136fee2f5a7f884e12f7ac17bcb229f97442",
    "docs/arsenal/cards/provisional/S32-PW05.md":
        "18988010867b5bd6278e4431b9f0efe81186c381",
}


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canonical_sha256(obj: dict) -> str:
    x = dict(obj)
    claimed = x.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert claimed == got
    return got


def matmul2(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def main() -> None:
    cert = json.loads(CERT.read_text())
    assert cert["schema"] == "STAGE32_POST1563_AMBIENT_SYMMETRY_EXHAUSTION_BATCH_V1"
    expected_base = os.environ.get("STAGE32_EXPECTED_BASE_SHA")
    assert expected_base, "STAGE32_EXPECTED_BASE_SHA is required for freshness fail-close"
    assert cert["base_main_sha"] == expected_base, (
        f"certificate base_main_sha {cert['base_main_sha']} != authoritative base {expected_base}"
    )
    assert canonical_sha256(cert) == EXPECTED_CERT_CANONICAL
    assert blob_sha1(SOURCE_NOTE) == EXPECTED_SOURCE_NOTE_BLOB

    for rel, (expected_blob, expected_canon) in LOCKS.items():
        p = ROOT / rel
        assert blob_sha1(p) == expected_blob, rel
        obj = json.loads(p.read_text())
        assert canonical_sha256(obj) == expected_canon, rel

    for rel, expected_blob in BLOB_ONLY_LOCKS.items():
        assert blob_sha1(ROOT / rel) == expected_blob, rel

    b3 = [[-1, -1], [1, 0]]
    b3_2 = matmul2(b3, b3)
    b3_3 = matmul2(b3_2, b3)
    assert b3 != [[1, 0], [0, 1]]
    assert b3_3 == [[1, 0], [0, 1]]

    parent = json.loads((ROOT / "stages/stage32/residual-32-01-production/post1561-b3-picard-action-adapter-gap.json").read_text())
    box = json.loads((ROOT / "stages/stage32/residual-32-01-production/post1555-b3-full-g-box-quotient-normalizer.json").read_text())
    stoll = json.loads((ROOT / "stages/stage32/residual-32-01-production/post1532-full-stoll-h-orbit-symmetry-negative.json").read_text())
    relh = json.loads((ROOT / "stages/stage32/residual-32-01-production/post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json").read_text())

    assert parent["missing_action_adapter"]["retained_stoll_group_exhausts_new_semilinear_lifts_proved"] is False
    assert box["full_G_normalizer"]["beta_B_exists"] is True
    assert box["quotient_chain"]["H_normal_index_in_G"] == 2
    assert box["quotient_chain"]["C0_to_X4_degree"] == 2
    assert box["hyperelliptic_centrality"]["b3_is_automorphism_of_C0"] is True
    assert box["hyperelliptic_centrality"]["b3_commutes_with_tau"] is True

    fr = stoll["finite_result"]
    assert fr["retained_stoll_group_order"] == 1536
    assert fr["h_deck_group_order"] == 4
    assert fr["base_class_to_h_orbit_count"] == 4
    assert fr["base_class_to_h_orbit_outside_h_count"] == 0
    assert fr["setwise_h_orbit_stabilizer_count"] == 4
    assert fr["setwise_h_orbit_stabilizer_outside_h_count"] == 0
    assert {x["word"] for x in fr["base_class_to_h_orbit_elements"]} == {
        "1", "g7*g8", "g7*g9", "g8*g9"
    }
    assert relh["equivariant_adapter"]["modular_to_stoll"] == {
        "u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"
    }

    r = cert["routes"]
    assert r["A_arsenal"]["S30_W01_applicable"] is True
    assert r["A_arsenal"]["S32_PW05_does_not_supply_semantic_identification"] is True

    b = r["B_full_automorphism_exhaustion"]
    assert b["retained_stoll_group_order"] == 1536
    assert b["external_full_box_automorphism_group_order"] == 1536
    assert b["common_geometric_anchor_is_same_box_surface"] is True
    assert b["retained_stoll_group_equals_full_box_automorphism_group"] is True
    assert b["exact_replacement_proof_not_abstract_group_match"] is True

    c = r["C_principal_b3_membership"]
    assert c["beta_B_exists_as_box_automorphism"] is True
    assert c["principal_b3_order"] == 3
    assert c["C0_to_X4_deck_kernel_order"] == 2
    assert c["principal_b3_descends_nontrivially_to_X4"] is True
    assert c["relative_H_actions_trivial_on_X4_after_quotient_by_G"] is True
    assert c["beta_B_in_retained_stoll_group"] is True
    assert c["beta_B_in_H"] is False

    d = r["D_H_orbit_consumption"]
    assert d["base_class_to_H_orbit_elements_are_exactly_H"] is True
    assert d["setwise_H_orbit_stabilizer_is_exactly_H"] is True
    assert d["beta_B_C_in_H_orbit"] is False
    assert d["beta_B_preserves_H_orbit_setwise"] is False
    assert d["any_H_deck_adjusted_beta_B_C_in_H_orbit"] is False
    assert d["hypothetical_exact_V6_carrier_beta_B_invariant"] is False
    assert d["statement_is_conditional_on_carrier_existence"] is True

    e = r["E_direct_Gamma_valence_source_check"]
    assert e["direct_Gamma_invariance_identity_found"] is False
    assert e["integral_valence_or_scalarity_theorem_found"] is False
    assert e["bounded_source_statement_only"] is True

    lane = cert["lane_closure"]
    assert lane["old_reentry_SYMMETRY_OUTSIDE_RETAINED_STOLL_FINITE_ACTION_closed"] is True
    assert lane["ambient_box_automorphism_lane_exhausted"] is True
    assert lane["no_further_ambient_symmetry_gap_localization_only"] is True

    dec = cert["decision"]
    assert dec["result"] == "PASS_EXACT_AMBIENT_SYMMETRY_LANE_EXHAUSTION_BATCH"
    assert dec["retained_stoll_full_aut_equality_proved"] is True
    assert dec["beta_B_stoll_membership_proved"] is True
    assert dec["beta_B_outside_H_proved"] is True
    assert dec["beta_B_V6_H_orbit_noninvariance_proved"] is True
    assert dec["hypothetical_carrier_beta_B_invariance_refuted"] is True
    assert dec["correspondence_invariance_proved"] is False
    assert dec["correspondence_noninvariance_proved"] is False
    assert dec["actual_T_b3_commutation_proved"] is False
    assert dec["actual_T_b3_noncommutation_proved"] is False
    assert dec["Q602_excluded"] is False
    assert dec["O210_excluded"] is False
    assert dec["O212_plus_advance_allowed"] is False
    assert dec["controller_change_authorized"] is False

    fw = cert["firewalls"]
    assert fw["abstract_group_isomorphism_used_as_semantic_adapter"] is False
    assert fw["explicit_beta_B_stoll_word_claimed"] is False
    assert fw["class_noninvariance_promoted_to_carrier_nonexistence"] is False
    assert fw["class_noninvariance_promoted_to_T_noncommutation"] is False
    assert fw["bounded_source_search_promoted_to_literature_nonexistence"] is False

    ext = cert["source_locks"]["external_stoll_verification"]
    assert ext["commit_sha"] == "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
    assert ext["blob_sha1"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
    fsm = cert["source_locks"]["external_freitag_salvati_manni"]
    assert fsm["arxiv"] == "1303.6495v1"
    assert "full automorphism group of box variety has order 1536" in fsm["exact_used_facts"]

    print(json.dumps({
        "success": True,
        "schema": cert["schema"],
        "canonical_sha256": EXPECTED_CERT_CANONICAL,
        "base_main_sha": cert["base_main_sha"],
        "result": dec["result"],
        "retained_stoll_group_order": fr["retained_stoll_group_order"],
        "H_order": fr["h_deck_group_order"],
        "beta_B_in_full_stoll": c["beta_B_in_retained_stoll_group"],
        "beta_B_in_H": c["beta_B_in_H"],
        "ambient_symmetry_lane_exhausted": lane["ambient_box_automorphism_lane_exhausted"],
        "Q602_excluded": dec["Q602_excluded"],
        "O210_excluded": dec["O210_excluded"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()