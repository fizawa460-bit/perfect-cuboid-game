#!/usr/bin/env python3
"""Verify post-#1498 Stage32 evidence-locator additions against immutable source locks."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REGISTRY = HERE / "stage32-post1498.json"
SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()


def nested(data: dict, dotted_key: str):
    value = data
    for part in dotted_key.split("."):
        value = value[part]
    return value


def committed_text(commit: str, path: str) -> str:
    return git("show", f"{commit}:{path}")


def committed_blob(commit: str, path: str) -> str:
    return git("rev-parse", "--verify", f"{commit}:{path}")


def main() -> int:
    data = json.loads(REGISTRY.read_text())
    errors = []

    source = data["current_authority_source"]
    if not SHA1.fullmatch(source.get("commit_sha", "")) or not SHA1.fullmatch(source.get("blob_sha1", "")):
        errors.append("invalid Stage32 authority source SHA")
        controller = {}
    else:
        try:
            blob = committed_blob(source["commit_sha"], source["path"])
            if blob != source["blob_sha1"]:
                errors.append("Stage32 authority source commit:path blob mismatch")
            controller = json.loads(committed_text(source["commit_sha"], source["path"]))
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            errors.append("Stage32 authority source unavailable")
            controller = {}

    # This extension is only a locator registration. It must preserve the live
    # post-#1501 STOP boundary rather than manufacture re-entry credit.
    if controller.get("fixed_target", {}).get("O") != 210:
        errors.append("Stage32 fixed target is not O210")
    if controller.get("current_leaf", {}).get("status") != "AUDITED_NEGATIVE":
        errors.append("post-#1501 geometry lane is not AUDITED_NEGATIVE")
    if controller.get("current_leaf", {}).get("O212_and_later_blocked") is not True:
        errors.append("O212+ firewall is not active")
    if controller.get("post1501_geometry_negative_lane", {}).get("reentry_requires_new_source_locked_evidence") is not True:
        errors.append("post-#1501 re-entry gate is not active")

    ids = [asset.get("asset_id") for asset in data["assets"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate Stage32 post1498 asset_id")

    for asset in data["assets"]:
        aid = asset.get("asset_id", "<missing>")
        if asset.get("stage") != 32:
            errors.append(f"{aid}: wrong stage")

        authority = asset["current_authority_snapshot"]
        try:
            row = nested(controller, authority["controller_key"])
            actual_status = nested(row, authority["controller_status_key"])
        except (KeyError, TypeError):
            errors.append(f"{aid}: controller authority status key missing")
            actual_status = None
        if actual_status != authority.get("status"):
            errors.append(f"{aid}: controller authority status mismatch")

        try:
            canonical_row = nested(controller, authority["canonical_controller_key"])
        except (KeyError, TypeError):
            errors.append(f"{aid}: controller canonical key missing")
            canonical_row = {}
        if canonical_row.get("canonical_sha256") != authority.get("canonical_sha256"):
            errors.append(f"{aid}: controller authority canonical mismatch")

        pass_row = controller.get("post1500_repair_hostile_audit_pass", {})
        if pass_row.get("review_id") != authority.get("audit_pass_review_id"):
            errors.append(f"{aid}: hostile-audit PASS review mismatch")
        if pass_row.get("audited_exact_head") != authority.get("audit_pass_head_sha"):
            errors.append(f"{aid}: hostile-audit PASS head mismatch")
        ci = pass_row.get("audited_exact_head_ci", {})
        if ci.get("run_id") != authority.get("exact_head_ci_run_id") or ci.get("job_id") != authority.get("exact_head_ci_job_id") or ci.get("success") is not True:
            errors.append(f"{aid}: exact-head CI authority mismatch")

        artifact = asset["artifact"]
        if not SHA256.fullmatch(artifact.get("canonical_sha256", "")):
            errors.append(f"{aid}: invalid artifact canonical")
        if artifact.get("canonical_sha256") != authority.get("canonical_sha256"):
            errors.append(f"{aid}: artifact/current-authority canonical mismatch")

        evidence_commit = asset["evidence_commit_sha"]
        if not SHA1.fullmatch(evidence_commit):
            errors.append(f"{aid}: invalid evidence commit")
            continue
        if evidence_commit != authority.get("audit_pass_head_sha"):
            errors.append(f"{aid}: evidence commit is not the hostile-audited head")

        primary = None
        for record in asset["files"]:
            path = ROOT / record["path"]
            if not path.is_file():
                errors.append(f"{aid}: missing working-tree file {record['path']}")
                continue
            current_blob = git("hash-object", "--", str(path))
            if current_blob != record["blob_sha1"]:
                errors.append(f"{aid}: working-tree blob mismatch {record['path']}")
            try:
                evidence_blob = committed_blob(evidence_commit, record["path"])
            except subprocess.CalledProcessError:
                evidence_blob = ""
            if evidence_blob != record["blob_sha1"]:
                errors.append(f"{aid}: evidence commit:path blob mismatch {record['path']}")
            if record["role"] == "primary":
                if primary is not None:
                    errors.append(f"{aid}: multiple primary files")
                primary = path

        if primary is None:
            errors.append(f"{aid}: primary file missing")
            continue
        primary_data = json.loads(primary.read_text())
        primary_canonical = primary_data.get("canonical_sha256_without_this_field", primary_data.get("canonical_sha256"))
        if primary_canonical != artifact.get("canonical_sha256"):
            errors.append(f"{aid}: primary canonical mismatch")
        try:
            primary_status = nested(primary_data, artifact["status_key"])
        except (KeyError, TypeError):
            primary_status = None
        if primary_status != artifact.get("status"):
            errors.append(f"{aid}: primary artifact-local status mismatch")

        for field in ("objects", "aliases", "relations", "outputs", "candidate_queries", "limitations", "files"):
            if not asset.get(field):
                errors.append(f"{aid}: empty {field}")
        if not any("does not by itself reopen" in item for item in asset.get("limitations", [])):
            errors.append(f"{aid}: missing explicit no-reopen firewall")

    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1

    print(
        "PROOF_REPLAY_COMPLETE: "
        f"{len(data['assets'])} post-#1498 Stage32 positive assets verified; "
        "registration grants no O210/O212 re-entry credit"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
