#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECTED_CANONICAL = "27a8863324aeb651ff741950b2ee20df8489c4321f66bb949b630d4f365c0b22"
EXPECTED_16 = [65,67,73,75,97,99,105,107,193,195,201,203,225,227,233,235]
EXPECTED_REGISTRIES = ["index.json", "stage32-post1498.json", "stage33.json"]
EXPECTED_EXTENSION_ASSET = "EVID-S32-O210-ROSATI-TRACE-REPAIR-AUDITED"


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


def assert_historical_locator_lock(lock: dict) -> None:
    # The locator was intentionally retired by Research OS.  Its historical
    # provenance remains hash-recorded in this immutable certificate, but the
    # retired file is no longer required to exist or execute on successor heads.
    assert lock["path"].startswith("docs/evidence-locator/")
    assert len(lock["blob_sha1"]) == 40


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()

    cert_path = ROOT / args.check
    cert = json.loads(cert_path.read_text())
    assert cert["schema"] == "STAGE32_POST1505_O210_Q602_16_RESIDUE_RETAINED_ASSET_SEARCH_V2"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    failure = cert["audit_failure"]
    assert failure["review_id"] == 5100795695
    assert failure["exact_head"] == "62978828a88978b362ed51eeaa1a150b6d914a0b"
    assert failure["scope"] == "LOCATOR_SEARCH_PROVENANCE_ONLY"
    assert failure["mathematical_16_to_16_rejected"] is False

    controller = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert controller["stage"] == 32
    assert controller["operations"]["heavy_compute_authorized"] is False
    assert controller["current_leaf"]["O212_and_later_blocked"] is True
    assert controller["firewalls"]["O210_closed"] is False

    ctl_bundle = controller["post1505_q602_16_residue_retained_asset_search_provisional"]
    assert ctl_bundle["status"] == "AUDITED_EXACT_BOUNDED_NEGATIVE_SEARCH_AFTER_HOSTILE_REAUDIT"
    assert ctl_bundle["certificate_path"] == args.check
    assert ctl_bundle["canonical_sha256"] == EXPECTED_CANONICAL
    assert ctl_bundle["q602_residue_pruning"] == "16 -> 16"
    assert ctl_bundle["surviving_residues_decimal"] == EXPECTED_16
    assert ctl_bundle["audit_failure_review_id"] == 5100795695
    assert ctl_bundle["multi_registry_locator_repaired"] is True

    audit_pass = controller["post1505_q602_16_residue_retained_asset_search_hostile_reaudit_pass"]
    assert audit_pass["review_id"] == 5101885156
    assert audit_pass["audited_exact_head"] == "b1d71cbae3f3d5bf3e7d2bf36c5a739acf475789"
    assert audit_pass["exact_head_ci"] == {"run_id":33754122329,"job_id":100644300234,"result":"SUCCESS"}
    assert audit_pass["verdict"] == "PASS"
    assert audit_pass["authority_promotion"] == "AUDITED_BOUNDED_NEGATIVE_MULTI_REGISTRY_16_TO_16_NONEXCLUSION"

    locks = cert["source_locks"]
    adapter = load_locked_json(locks["audited_16_adapter"])
    arsenal = load_locked_json(locks["arsenal_index"])
    pw03 = load_locked_text(locks["arsenal_pw03"])
    pw04 = load_locked_text(locks["arsenal_pw04"])
    rosati = load_locked_json(locks["principal_rosati"])
    repair = load_locked_json(locks["post1500_q602_nonexclusion"])
    note = load_locked_text(locks["source_note"])

    for key in [
        "evidence_query_script",
        "evidence_locator_index",
        "evidence_locator_stage32_extension",
        "evidence_locator_stage33",
    ]:
        assert_historical_locator_lock(locks[key])
    assert not (ROOT / "docs/evidence-locator").exists(), "retired locator must stay absent on successor heads"

    # Current discovery authority replaces the retired locator without changing
    # the historical mathematical/nonexclusion result of this bundle.
    policy = (ROOT / "docs/research-os/policies/repository-asset-discovery.md").read_text()
    agents = (ROOT / "AGENTS.md").read_text()
    assert "canonical final handoff" in policy
    assert "## Arsenal" in policy
    assert "not a mathematical claim that the repository lacks the object" in policy
    assert "search-first, not tree-first" in agents
    assert "Do not acquire a recursive repository tree by default" in agents
    assert "search miss never proves repository-wide absence" in agents.lower()

    audited = adapter["q602_pointwise_exact_W_test"]
    assert audited["surviving_residue_count"] == 16
    assert audited["surviving_residues_decimal"] == EXPECTED_16
    assert cert["audited_input"]["residue_count"] == 16
    assert cert["audited_input"]["residues_decimal"] == EXPECTED_16
    assert cert["audited_input"]["ordered_basis"] == ["e1","e2","r*e1","r*e2"]
    assert cert["audited_input"]["condition"] == "T|W=id and T^dagger|W=id"

    assert arsenal["registry_contract"]["authority_order"][0] == "active stage controller and current source locks"
    assert "LATTICE_IMAGE_HNF_GATE" in pw03 and "FINITE_LATTICE_QUOTIENT_BOUND" in pw04
    s = cert["searched_asset_classes"]
    assert s["arsenal_pw03"]["direct_operator_mod2_predicate"] is False
    assert s["arsenal_pw04"]["direct_operator_mod2_predicate"] is False

    # Preserve the audited historical locator receipt as data, not as a live tool.
    loc = s["evidence_locator"]
    assert loc["query_contract"] == "python docs/evidence-locator/query_evidence.py Q602 --stage 32 --limit 20"
    assert loc["registry_files"] == EXPECTED_REGISTRIES
    assert loc["stage32_extension_asset_id"] == EXPECTED_EXTENSION_ASSET
    assert loc["stage32_extension_asset_found_by_replay"] is True
    assert loc["stage32_extension_is_same_post1500_q602_nonexclusion"] is True
    assert loc["direct_current_operator_mod2_predicate_found"] is False
    assert loc["query_miss_proves_repo_absence"] is False

    assert rosati["rosati"]["formula"] == "T^dagger=H^{-1}*bar(T)^t*H"
    assert adapter["q602_pointwise_exact_W_test"]["condition"] == "T|W=id and T^dagger|W=id"
    assert s["principal_rosati"]["already_consumed_by_audited_16_predicate"] is True
    assert s["principal_rosati"]["new_independent_residue_predicate_from_lock_alone"] is False
    assert s["principal_rosati"]["g12_commutation_or_equivariance_assumed"] is False

    assert repair["corrected_rosati_arithmetic"]["Q"] == 602
    assert repair["bounded_retained_rosati_search"]["existing_assets_exclude_Q602"] is False
    assert s["post1500_retained_q602_assets"]["Q"] == 602
    assert s["post1500_retained_q602_assets"]["existing_assets_exclude_Q602"] is False
    assert s["post1500_retained_q602_assets"]["new_residue_predicate_promoted"] is False

    for needle in [
        "provenance/search boundary only",
        "does **not** prove that no stronger theorem or repository asset exists",
        "query_evidence.py",
        "stage32-post1498.json",
        EXPECTED_EXTENSION_ASSET,
        "locator miss is not repository-wide absence evidence",
        "input residues: 16",
        "output residues: the same 16",
    ]:
        assert needle in note, needle

    out = cert["bounded_search_result"]
    assert out["global_repository_absence_claim"] is False
    assert out["theorem_absence_claim"] is False
    assert out["input_residue_count"] == out["output_residue_count"] == 16
    assert out["output_residues_decimal"] == EXPECTED_16
    assert out["new_pruning"] is False
    assert out["Q602_excluded"] is False
    assert out["O210_excluded"] is False
    assert out["O212_plus_authorized"] is False

    fire = cert["firewalls"]
    assert fire["locator_miss_used_as_absence_proof"] is False
    assert fire["index_only_locator_surrogate_used"] is False
    assert fire["cross_object_constraint_reused_without_adapter"] is False
    assert fire["g12_equivariance_inferred"] is False
    assert fire["heavy_compute_authorized"] is False

    print(json.dumps({
        "schema": cert["schema"],
        "canonical": EXPECTED_CANONICAL,
        "controller": controller["schema"],
        "lifecycle": "historical audited locator receipt replay under retired-locator Research OS",
        "retired_locator_live_execution_required": False,
        "historical_locator_hashes_retained": True,
        "Q602_residues": {"input": 16, "output": 16, "values": EXPECTED_16},
        "new_pruning": False,
        "Q602_excluded": False,
        "O210_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
