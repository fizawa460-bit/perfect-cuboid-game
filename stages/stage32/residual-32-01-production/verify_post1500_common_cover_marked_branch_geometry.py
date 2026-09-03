#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = HERE / "post1500-common-cover-marked-branch-geometry-certificate.json"
SOURCE_NOTE_PATH = HERE / "post1500-hostile-audit-rosati-trace-repair-source-note.md"
CONTROLLER_PATH = ROOT / "stages/stage32/controller.json"
WORKFLOW_PATH = ROOT / ".github/workflows/stage32-post1500-common-cover-marked-branch-geometry.yml"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    controller = json.loads(CONTROLLER_PATH.read_text(encoding="utf-8"))
    source_bytes = SOURCE_NOTE_PATH.read_bytes()
    source = source_bytes.decode("utf-8")

    require(cert["schema_version"] == 2, "schema_version")
    require(cert["stage"] == 32, "stage")
    require(cert["base_pr"] == 1500, "base_pr")
    require(cert["repair_pr"] == 1501, "repair_pr")
    require(cert["status"] == "AUDITED_NEGATIVE", "certificate status")
    require(WORKFLOW_PATH.is_file(), "dedicated workflow missing")

    source_lock = cert["admitted_inputs"]["repair_source_note"]
    require(source_lock["path"] == str(SOURCE_NOTE_PATH.relative_to(ROOT)), "source-note path lock")
    require(
        git_blob_sha1(source_bytes) == source_lock["git_blob_sha1"] == "b0ea281eae453929c292059a919bc1f68b3080b3",
        "repair source-note blob lock",
    )

    require(controller["stage"] == 32, "controller stage")
    require(controller["fixed_target"]["O"] == 210, "controller fixed target must remain O210")
    require(controller["active_pr"]["number"] == 1501, "controller active PR")
    require(
        controller["active_pr"]["branch"] == "stage32-post1500-o210-rosati-geometry",
        "controller active branch",
    )
    require(controller["merge_allowed"] is False, "merge must remain blocked before hostile re-audit PASS")
    require(controller["checkpoint_merge_ready"] is False, "checkpoint must not be merge-ready")
    require(controller["audit_required_before_promotion"] is True, "hostile re-audit must be required")
    require(controller["current_leaf"]["status"] == "AUDITED_NEGATIVE", "controller negative-lane status")
    require(controller["current_leaf"]["O212_and_later_blocked"] is True, "O212+ firewall")

    repair = controller["repair_boundary"]
    require(repair["source_note_path"] == str(SOURCE_NOTE_PATH.relative_to(ROOT)), "controller source-note path")
    require(repair["source_note_blob_sha1"] == source_lock["git_blob_sha1"], "controller/source certificate blob agreement")
    require(repair["corrected"]["Gamma_square"] == 15806, "Gamma^2 authority")
    require(repair["corrected"]["sigma_Gamma"] == 1204, "sigma authority")
    require(repair["corrected"]["Q_T"] == 602, "Q authority")
    require(repair["corrected"]["O210_Gamma_normalization_defect"] == 7984, "corrected delta")
    bounded = repair["bounded_existing_asset_result"]
    require(bounded["D4_direct_sum_D4_represents_Q602"] is True, "D4 representation")
    require(bounded["one_D4_norm602_shell_count"] == 8448, "D4 shell count")
    require(bounded["operator_bound_8505_excludes_Q602"] is False, "operator nonexclusion")
    require(bounded["weierstrass_delta_min"] == 1924, "Weierstrass delta lower bound")
    require(bounded["corrected_delta_7984_satisfies_weierstrass_bound"] is True, "Weierstrass nonexclusion")

    for exact_text in (
        "`Gamma^2 = 3874+11932 = 15806`",
        "`sigma(Gamma)=2*105*81-15806=1204`",
        "`Q(T)=602`",
        "`T^dagger*T <= 8505`",
        "`delta_Gamma >= 1924`",
        "O=210 carrier is OPEN again",
        "O=212 and all later overlaps remain blocked behind O=210",
    ):
        require(exact_text in source, f"source-note content lock missing: {exact_text}")

    before = cert["authority_before"]
    after = cert["authority_after"]
    expected_authority = {
        "checkpoint": "O210",
        "fixed_overlap": 210,
        "sigma_gamma": 1204,
        "q_total": 602,
        "o210_closed": False,
        "o212_plus_authorized": False,
    }
    require(before == after, "negative audit must not promote authority")
    require(after == expected_authority, "unexpected authority state")

    facts = cert["source_locked_nonexclusion_facts"]
    require(facts["gamma_square"] == repair["corrected"]["Gamma_square"], "cert/controller Gamma^2")
    require(facts["sigma_gamma"] == repair["corrected"]["sigma_Gamma"], "cert/controller sigma")
    require(facts["q_total"] == repair["corrected"]["Q_T"], "cert/controller Q")
    require(facts["d4_direct_sum_d4_represents_q602"] == bounded["D4_direct_sum_D4_represents_Q602"], "cert/controller D4")
    require(facts["one_d4_norm602_shell_count"] == bounded["one_D4_norm602_shell_count"], "cert/controller shell")
    require(facts["operator_constraint"] == {
        "statement": "T^dagger*T <= 8505",
        "bound": 8505,
        "excludes_q602": False,
    }, "operator source-lock record")
    require(facts["weierstrass"] == {
        "delta_gamma_lower_bound": 1924,
        "corrected_delta_gamma": 7984,
        "excludes_corrected_delta": False,
    }, "Weierstrass source-lock record")

    result = cert["result"]
    require(result["new_geometric_exclusion_certified"] is False, "unexpected geometric exclusion")
    require(result["strict_rosati_loss_certified"] is False, "unexpected Rosati strictness")
    require(len(cert["required_new_evidence"]) == 3, "re-entry evidence count")
    require(len(cert["anti_loop"]) >= 3, "anti-loop rules")

    required = controller["required_lightweight_verifier"]
    require(required["path"] == str(Path(__file__).resolve().relative_to(ROOT)), "controller verifier path")
    require(required["certificate_path"] == str(CERT_PATH.relative_to(ROOT)), "controller certificate path")
    require(required["workflow"] == str(WORKFLOW_PATH.relative_to(ROOT)), "controller workflow path")

    print(
        "PASS: post1500 common-cover/marked-branch lane is AUDITED_NEGATIVE; "
        "O210 authority remains open at sigma=1204 / Q=602 and O212+ remains blocked"
    )


if __name__ == "__main__":
    main()
