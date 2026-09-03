#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECTED_CANONICAL = "28b3b51f1fc2f129a467bc93d87014d80eeefd083cc5f79846ad3dc69122323b"
EXPECTED_16 = [65,67,73,75,97,99,105,107,193,195,201,203,225,227,233,235]


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_locked_json(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
    return doc


def load_locked_text(lock: dict) -> str:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    return path.read_text()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()

    cert_path = ROOT / args.check
    cert = json.loads(cert_path.read_text())
    assert cert["schema"] == "STAGE32_POST1505_O210_Q602_16_RESIDUE_RETAINED_ASSET_SEARCH_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    # Current-head controller wiring is part of the replay contract.
    controller = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert controller["schema"] == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V236_POST1505_Q602_16_RETAINED_ASSET_SEARCH_PROVISIONAL"
    assert controller["status"] == "STAGE32_O210_Q602_AUDITED_16_RETAINED_ASSET_SEARCH_PENDING_HOSTILE_AUDIT"
    assert controller["current_item"] == "O210_Q602_AUDITED_16_RETAINED_ASSET_SEARCH_PENDING_HOSTILE_AUDIT"
    ctl_leaf = controller["current_leaf"]
    assert ctl_leaf["status"] == "PROVISIONAL_EXACT_BOUNDED_NEGATIVE_RETAINED_ASSET_SEARCH_PENDING_HOSTILE_AUDIT"
    assert ctl_leaf["O212_and_later_blocked"] is True
    ctl_bundle = controller["post1505_q602_16_residue_retained_asset_search_provisional"]
    assert ctl_bundle["certificate_path"] == args.check
    assert ctl_bundle["canonical_sha256"] == EXPECTED_CANONICAL
    assert ctl_bundle["q602_residue_pruning"] == "16 -> 16"
    assert ctl_bundle["surviving_residues_decimal"] == EXPECTED_16
    required = controller["required_lightweight_verifier"]
    assert required["path"] == "stages/stage32/residual-32-01-production/certify_stage32_post1505_o210_q602_16_residue_retained_asset_search.py"
    assert required["certificate_path"] == args.check
    assert required["workflow"] == ".github/workflows/stage32-post1505-o210-q602-16-residue-retained-asset-search.yml"
    assert controller["audit_required_before_promotion"] is True
    assert controller["merge_allowed"] is False
    assert controller["operations"]["heavy_compute_authorized"] is False
    assert controller["operations"]["retained_asset_research_authorized"] is False

    locks = cert["source_locks"]
    adapter = load_locked_json(locks["audited_16_adapter"])
    arsenal = load_locked_json(locks["arsenal_index"])
    pw03 = load_locked_text(locks["arsenal_pw03"])
    pw04 = load_locked_text(locks["arsenal_pw04"])
    locator = load_locked_json(locks["evidence_locator"])
    rosati = load_locked_json(locks["principal_rosati"])
    repair = load_locked_json(locks["post1500_q602_nonexclusion"])
    note = load_locked_text(locks["source_note"])

    # Exact hostile-audited input boundary: preserve all 16, no hidden pruning.
    assert locks["audited_16_adapter"]["hostile_reaudit_review"] == 5100346603
    audited = adapter["q602_pointwise_exact_W_test"]
    assert audited["surviving_residue_count"] == 16
    assert audited["surviving_residues_decimal"] == EXPECTED_16
    assert cert["audited_input"]["residue_count"] == 16
    assert cert["audited_input"]["residues_decimal"] == EXPECTED_16
    assert cert["audited_input"]["ordered_basis"] == ["e1","e2","r*e1","r*e2"]
    assert cert["audited_input"]["condition"] == "T|W=id and T^dagger|W=id"

    # Arsenal cards are lattice/Picard-side contracts, not direct End(J) residue predicates.
    assert arsenal["registry_contract"]["authority_order"][0] == "active stage controller and current source locks"
    assert "LATTICE_IMAGE_HNF_GATE" in pw03
    assert "picard_rank=64" in pw03
    assert "changed marking without an adapter" in pw03
    assert "FINITE_LATTICE_QUOTIENT_BOUND" in pw04
    assert "same exact quadratic kernel" in pw04
    s = cert["searched_asset_classes"]
    assert s["arsenal_pw03"]["direct_operator_mod2_predicate"] is False
    assert s["arsenal_pw03"]["adapter_to_current_operator_residue_found"] is False
    assert s["arsenal_pw04"]["direct_operator_mod2_predicate"] is False
    assert s["arsenal_pw04"]["adapter_to_current_operator_residue_found"] is False

    # Locator is explicitly positive-only and not an absence oracle. Check exact manifest only.
    assert locator["purpose"] == "machine-only positive-asset locator; not a claim authority and not an absence oracle"
    assert locator["policies"]["positive_assets_only"] is True
    assert locator["policies"]["query_miss_proves_repo_absence"] is False
    assert len(locator["assets"]) == 5
    manifest_text = json.dumps(locator["assets"], sort_keys=True)
    assert "End(J)" not in manifest_text
    assert "operator residue" not in manifest_text
    assert s["evidence_locator"]["registered_asset_count"] == 5
    assert s["evidence_locator"]["direct_current_operator_mod2_predicate_registered"] is False
    assert s["evidence_locator"]["query_miss_proves_repo_absence"] is False

    # The principal Rosati structure is already consumed in the audited dagger condition.
    assert rosati["rosati"]["formula"] == "T^dagger=H^{-1}*bar(T)^t*H"
    assert adapter["q602_pointwise_exact_W_test"]["condition"] == "T|W=id and T^dagger|W=id"
    assert s["principal_rosati"]["already_consumed_by_audited_16_predicate"] is True
    assert s["principal_rosati"]["new_independent_residue_predicate_from_lock_alone"] is False
    assert s["principal_rosati"]["g12_commutation_or_equivariance_assumed"] is False

    # Historical retained Q602 assets are an exact nonexclusion boundary, not a new predicate.
    assert repair["corrected_rosati_arithmetic"]["Q"] == 602
    assert repair["bounded_retained_rosati_search"]["existing_assets_exclude_Q602"] is False
    assert s["post1500_retained_q602_assets"]["Q"] == 602
    assert s["post1500_retained_q602_assets"]["existing_assets_exclude_Q602"] is False
    assert s["post1500_retained_q602_assets"]["new_residue_predicate_promoted"] is False

    for needle in [
        "provenance/search boundary only",
        "does **not** prove that no stronger theorem or repository asset exists",
        "locator miss is not repository-wide absence evidence",
        "does **not** authorize assuming that the current correspondence operator `T` commutes with G12",
        "input residues: 16",
        "output residues: the same 16",
    ]:
        assert needle in note, needle

    out = cert["bounded_search_result"]
    assert out["claim"] == "NO_NEW_SOURCE_LOCKED_DIRECT_PREDICATE_FOUND_WITHIN_EXACT_INSPECTED_ASSET_CLASSES"
    assert out["global_repository_absence_claim"] is False
    assert out["theorem_absence_claim"] is False
    assert out["input_residue_count"] == 16
    assert out["output_residue_count"] == 16
    assert out["output_residues_decimal"] == EXPECTED_16
    assert out["new_pruning"] is False
    assert out["Q602_excluded"] is False
    assert out["O210_excluded"] is False
    assert out["O212_plus_authorized"] is False

    fire = cert["firewalls"]
    assert fire["locator_miss_used_as_absence_proof"] is False
    assert fire["cross_object_constraint_reused_without_adapter"] is False
    assert fire["g12_equivariance_inferred"] is False
    assert fire["heavy_compute_authorized"] is False

    print(json.dumps({
        "schema": cert["schema"],
        "canonical": EXPECTED_CANONICAL,
        "controller": controller["schema"],
        "bounded_search": "inspected retained asset classes only",
        "Q602_residues": {"input": 16, "output": 16, "values": EXPECTED_16},
        "new_pruning": False,
        "Q602_excluded": False,
        "O210_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
