#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1561-b3-picard-action-adapter-gap.json"
EXPECTED_CANONICAL = "72945b0cd9d5a7e9e7e40e35bb6bd0cea79b7fafcfda8ea8d31af527c1e04b38"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_lock(lock: dict):
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    if path.suffix == ".json":
        doc = json.loads(path.read_text())
        if "canonical_sha256" in lock:
            assert canonical_sha256(doc) == lock["canonical_sha256"], path
        return doc
    return path.read_text()


def main() -> None:
    cert = json.loads(CERT.read_text())
    assert cert["schema"] == "STAGE32_POST1561_B3_PICARD_ACTION_ADAPTER_GAP_V1"
    assert cert["status"] == "EXACT_RETAINED_ACTION_ADAPTER_GAP_PENDING_HOSTILE_AUDIT"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert cert["fixed_target"] == {"row_id": "g1-d186", "O": 210, "qprime": 4, "Q": 602}

    locks = cert["source_locks"]
    parent = load_lock(locks["parent_source_gap"])
    normalizer = load_lock(locks["b3_box_normalizer"])
    stoll = load_lock(locks["full_stoll_h_orbit_negative"])
    arsenal_index = load_lock(locks["arsenal_router"])
    arsenal_card = load_lock(locks["arsenal_S32_PW05"])
    note = load_lock(locks["source_note"])

    # #1561: member-level bridge still absent.
    missing = parent["missing_member_level_data"]
    assert missing["defining_equation_or_ideal_for_N"] is False
    assert missing["distinguished_defining_section_for_N"] is False
    assert missing["uniqueness_of_integral_carrier_in_fixed_V6_class"] is False
    assert missing["source_locked_beta_B_action_on_defining_carrier_member_or_section"] is False
    assert parent["decision"]["retained_input_does_not_yet_prove_carrier_or_Gamma_invariance"] is True

    # #1556: the ambient quotient lift exists, but its certificate contains no marked-Picard adapter.
    fg = normalizer["full_G_normalizer"]
    assert fg["beta_X_exists"] is True and fg["beta_B_exists"] is True and fg["X_to_B_equivariant"] is True
    assert normalizer["carrier_boundary"]["beta_X_Y_invariance_proved"] is False
    assert normalizer["carrier_boundary"]["Gamma_invariance_proved"] is False

    # Older retained finite Stoll result: exact only in that finite action.
    fin = stoll["finite_result"]
    assert fin["retained_stoll_group_order"] == 1536
    assert fin["h_deck_group_order"] == 4
    assert fin["base_class_to_h_orbit_count"] == 4
    assert fin["base_class_to_h_orbit_outside_h_count"] == 0
    assert fin["setwise_h_orbit_stabilizer_count"] == 4
    assert fin["setwise_h_orbit_stabilizer_outside_h_count"] == 0
    assert "SYMMETRY_OUTSIDE_RETAINED_STOLL_FINITE_ACTION" in stoll["reentry_requires"]
    assert stoll["decision"]["actual_T_commutation_proved"] is False
    assert stoll["decision"]["Q602_excluded"] is False

    # Research OS routing / Arsenal firewall.
    assert arsenal_index["registry_contract"]["canonical_machine_registry"] is True
    assert "FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION" in arsenal_card
    assert "semantic/geometric identification merely from reconstructed algebra" in arsenal_card

    pos = cert["retained_positive_input"]
    assert pos["beta_X_exists"] is True and pos["beta_B_exists"] is True
    assert pos["retained_stoll_group_order"] == 1536
    assert pos["retained_stoll_generator_count"] == 9
    assert pos["H_deck_group_order"] == 4
    assert pos["base_class_to_H_orbit_elements_are_exactly_H"] is True
    assert pos["setwise_H_orbit_stabilizer_is_exactly_H"] is True

    gap = cert["missing_action_adapter"]
    assert all(gap[k] is False for k in [
        "beta_X_retained_stoll_word_source_locked",
        "beta_X_140_class_permutation_source_locked",
        "beta_X_action_on_recovered_V6_class_source_locked",
        "retained_stoll_group_exhausts_new_semilinear_lifts_proved",
        "beta_X_proved_outside_retained_stoll_action",
    ])

    boundary = cert["logical_boundary"]
    assert all(boundary.values())
    assert cert["arsenal_check"]["card"] == "S32-PW05"
    assert cert["arsenal_check"]["card_supplies_missing_action_identification"] is False

    decision = cert["decision"]
    assert decision["result"] == "PASS_EXACT_B3_PICARD_ACTION_ADAPTER_GAP_LOCALIZATION"
    assert decision["missing_object"] == "BETA_X_ACTION_ON_RECOVERED_V6_PICARD_CLASS"
    for key in [
        "carrier_invariance_proved", "carrier_noninvariance_proved",
        "correspondence_invariance_proved", "correspondence_noninvariance_proved",
        "actual_T_b3_commutation_proved", "actual_T_b3_noncommutation_proved",
        "Q602_excluded", "O210_excluded", "O212_plus_advance_allowed",
        "controller_change_authorized",
    ]:
        assert decision[key] is False, key
    assert decision["next_exact_leaf"] == "SOURCE_LOCK_BETA_X_MARKED_PICARD_ACTION_OR_DIRECT_DIVISOR_CORRESPONDENCE_IDENTITY"

    for key, value in cert["firewalls"].items():
        assert value is False, key

    for phrase in [
        "BETA_X_ACTION_ON_RECOVERED_V6_PICARD_CLASS",
        "cannot be applied to `beta_X` merely because both are ambient symmetries",
        "No search over the 1536 Stoll elements may substitute for this adapter",
        "O212+ remains BLOCKED",
    ]:
        assert phrase in note, phrase

    controller = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert controller["stage"] == 32
    assert controller["stage32_closed"] is False
    target = controller["fixed_target"]
    assert target["row_id"] == "g1-d186" and target["O"] == 210 and target["qprime"] == 4 and target["Q"] == 602

    print("PASS: post1561 b3 Picard-action adapter gap is exact; beta_X exists, retained Stoll H-orbit stabilizer is exactly H, but no source-locked adapter identifies the new lift with that marked Picard action. Q602/O210 remain open; O212+ blocked.")


if __name__ == "__main__":
    main()
