#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

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


def replay_evidence_query(script_path: Path) -> dict:
    proc = subprocess.run(
        [sys.executable, str(script_path), "Q602", "--stage", "32", "--limit", "20"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(proc.stdout)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()

    cert_path = ROOT / args.check
    cert = json.loads(cert_path.read_text())
    assert cert["schema"] == "STAGE32_POST1505_O210_Q602_16_RESIDUE_RETAINED_ASSET_SEARCH_V2"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    failure = cert["audit_failure"]
    assert failure["review_id"] == 5100795695
    assert failure["exact_head"] == "62978828a88978b362ed51eeaa1a150b6d914a0b"
    assert failure["scope"] == "LOCATOR_SEARCH_PROVENANCE_ONLY"
    assert failure["mathematical_16_to_16_rejected"] is False

    # Historical-bundle lifecycle contract: this verifier replays the audited
    # 16->16 bundle under successor controllers.  It must not pin the active
    # controller schema/current leaf/required verifier or checkpoint merge-release
    # state, because later controller promotions are allowed to advance while
    # retaining this bundle.
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
    query_script = load_locked_text(locks["evidence_query_script"])
    locator_index = load_locked_json(locks["evidence_locator_index"])
    locator_stage32 = load_locked_json(locks["evidence_locator_stage32_extension"])
    locator_stage33 = load_locked_json(locks["evidence_locator_stage33"])
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

    # Hostile-audit repair: source-lock and execute the actual multi-registry query route.
    assert 'REGISTRY_PATHS = [HERE / "index.json", HERE / "stage32-post1498.json", HERE / "stage33.json"]' in query_script
    assert locator_index["policies"]["positive_assets_only"] is True
    assert locator_index["policies"]["query_miss_proves_repo_absence"] is False
    assert locator_stage32["policies"]["positive_assets_only"] is True
    assert locator_stage32["policies"]["query_miss_proves_repo_absence"] is False
    assert len(locator_stage32["assets"]) == 1
    assert locator_stage32["assets"][0]["asset_id"] == EXPECTED_EXTENSION_ASSET
    assert locator_stage32["assets"][0]["artifact"]["canonical_sha256"] == repair["canonical_sha256_without_this_field"]
    assert locator_stage33["policies"]["query_miss_proves_repo_absence"] is False

    query_result = replay_evidence_query(ROOT / locks["evidence_query_script"]["path"])
    assert query_result["schema"] == "PERFECT_CUBOID_EVIDENCE_QUERY_RESULT_V3_MULTI_STAGE"
    assert query_result["query"] == ["Q602"]
    assert query_result["filters"]["stage"] == 32
    assert [x["file"] for x in query_result["registry_sources"]] == EXPECTED_REGISTRIES
    matches = {m["asset_id"]: m for m in query_result["matches"]}
    assert EXPECTED_EXTENSION_ASSET in matches
    ext_match = matches[EXPECTED_EXTENSION_ASSET]
    assert ext_match["registry_file"] == "stage32-post1498.json"
    assert ext_match["stage"] == 32
    assert any("do not exclude" in x for x in ext_match["relations"])
    assert any("does not exclude" in x for x in ext_match["limitations"])
    assert query_result["firewalls"]["query_miss_proves_repo_absence"] is False
    assert query_result["firewalls"]["locator_match_grants_mathematical_credit"] is False

    loc = s["evidence_locator"]
    assert loc["query_contract"] == "python docs/evidence-locator/query_evidence.py Q602 --stage 32 --limit 20"
    assert loc["registry_files"] == EXPECTED_REGISTRIES
    assert loc["stage32_extension_asset_id"] == EXPECTED_EXTENSION_ASSET
    assert loc["stage32_extension_asset_found_by_replay"] is True
    assert loc["stage32_extension_is_same_post1500_q602_nonexclusion"] is True
    assert loc["direct_current_operator_mod2_predicate_found"] is False
    assert loc["query_miss_proves_repo_absence"] is False

    # The principal Rosati structure is already consumed in the audited dagger condition.
    assert rosati["rosati"]["formula"] == "T^dagger=H^{-1}*bar(T)^t*H"
    assert adapter["q602_pointwise_exact_W_test"]["condition"] == "T|W=id and T^dagger|W=id"
    assert s["principal_rosati"]["already_consumed_by_audited_16_predicate"] is True
    assert s["principal_rosati"]["new_independent_residue_predicate_from_lock_alone"] is False
    assert s["principal_rosati"]["g12_commutation_or_equivariance_assumed"] is False

    # The extension asset and the direct authority lock are the same Q602 nonexclusion boundary.
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
        "does **not** authorize assuming that the current correspondence operator `T` commutes with G12",
        "input residues: 16",
        "output residues: the same 16",
    ]:
        assert needle in note, needle

    out = cert["bounded_search_result"]
    assert out["claim"] == "NO_NEW_SOURCE_LOCKED_DIRECT_PREDICATE_FOUND_WITHIN_EXACT_INSPECTED_ASSET_CLASSES_INCLUDING_MULTI_REGISTRY_LOCATOR"
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
    assert fire["index_only_locator_surrogate_used"] is False
    assert fire["cross_object_constraint_reused_without_adapter"] is False
    assert fire["g12_equivariance_inferred"] is False
    assert fire["heavy_compute_authorized"] is False

    print(json.dumps({
        "schema": cert["schema"],
        "canonical": EXPECTED_CANONICAL,
        "controller": controller["schema"],
        "lifecycle": "historical audited bundle replay under successor controller",
        "locator_registries": EXPECTED_REGISTRIES,
        "extension_asset": EXPECTED_EXTENSION_ASSET,
        "bounded_search": "multi-registry route replayed and hostile-re-audit promotion retained",
        "Q602_residues": {"input": 16, "output": 16, "values": EXPECTED_16},
        "new_pruning": False,
        "Q602_excluded": False,
        "O210_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
