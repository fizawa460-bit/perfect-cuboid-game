#!/usr/bin/env python3
"""Network-free structural, provenance, blob, and authority-snapshot verifier."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
INDEX = HERE / "index.json"
SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()


def current_blob(path: Path) -> str:
    return git("hash-object", "--", str(path))


def committed_blob(commit: str, path: str) -> str:
    return git("rev-parse", "--verify", f"{commit}:{path}")


def nested(data: dict, dotted_key: str):
    value = data
    for part in dotted_key.split("."):
        value = value[part]
    return value


def nonempty_string_list(value) -> bool:
    return isinstance(value, list) and bool(value) and all(isinstance(item, str) and item.strip() for item in value)


def main() -> int:
    data = json.loads(INDEX.read_text())
    errors = []
    required = set(data["required_asset_fields"])
    allowed_authority = set(data["authority_statuses"])
    ids = [asset.get("asset_id") for asset in data["assets"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate asset_id")

    authority_source = data["current_authority_source"]
    controller_path = ROOT / authority_source["path"]
    try:
        controller_commit_blob = committed_blob(authority_source["commit_sha"], authority_source["path"])
    except subprocess.CalledProcessError:
        controller_commit_blob = ""
        errors.append("authority controller commit:path is unavailable")
    if controller_commit_blob != authority_source["blob_sha1"]:
        errors.append("authority controller commit:path blob mismatch")
    if not controller_path.is_file():
        errors.append("authority controller path missing")
        controller = {}
    else:
        if current_blob(controller_path) != authority_source["blob_sha1"]:
            errors.append("working-tree authority controller differs from locked snapshot")
        controller = json.loads(controller_path.read_text())

    for asset in data["assets"]:
        asset_id = asset.get("asset_id", "<missing-id>")
        missing = sorted(required - set(asset))
        if missing:
            errors.append(f"{asset_id}: missing required fields {missing}")
            continue
        for field in ("objects", "aliases", "relations", "outputs", "candidate_queries", "limitations"):
            if not nonempty_string_list(asset[field]):
                errors.append(f"{asset_id}: {field} must be a nonempty string list")
        if not isinstance(asset["stage"], int) or asset["stage"] <= 0:
            errors.append(f"{asset_id}: invalid stage")

        artifact = asset["artifact"]
        if not isinstance(artifact.get("status"), str) or not artifact["status"]:
            errors.append(f"{asset_id}: artifact status required")
        if not SHA256.fullmatch(artifact.get("canonical_sha256", "")):
            errors.append(f"{asset_id}: invalid artifact canonical SHA256")

        authority = asset["current_authority_snapshot"]
        if authority.get("status") not in allowed_authority:
            errors.append(f"{asset_id}: invalid current authority status")
        if not SHA256.fullmatch(authority.get("canonical_sha256", "")):
            errors.append(f"{asset_id}: invalid authority canonical SHA256")
        try:
            controller_entry = nested(controller, authority["controller_key"])
        except (KeyError, TypeError):
            errors.append(f"{asset_id}: controller key not found")
            controller_entry = {}
        if controller_entry.get("status") != authority.get("status"):
            errors.append(f"{asset_id}: controller authority status mismatch")
        if controller_entry.get("canonical_sha256") != authority.get("canonical_sha256"):
            errors.append(f"{asset_id}: controller authority canonical mismatch")
        if artifact.get("canonical_sha256") != authority.get("canonical_sha256"):
            errors.append(f"{asset_id}: artifact/authority canonical mismatch")
        if "audit_pass_head_sha" in authority:
            if not SHA1.fullmatch(authority["audit_pass_head_sha"]):
                errors.append(f"{asset_id}: invalid audit PASS head")
            else:
                try:
                    git("cat-file", "-e", f"{authority['audit_pass_head_sha']}^{{commit}}")
                except subprocess.CalledProcessError:
                    errors.append(f"{asset_id}: audit PASS commit unavailable")
            if not isinstance(authority.get("audit_pass_review_id"), int) or authority["audit_pass_review_id"] <= 0:
                errors.append(f"{asset_id}: audit PASS review required")

        evidence_commit = asset["evidence_commit_sha"]
        if not SHA1.fullmatch(evidence_commit):
            errors.append(f"{asset_id}: invalid evidence commit")
        if not isinstance(asset["files"], list) or not asset["files"]:
            errors.append(f"{asset_id}: files must be nonempty")
            continue
        primary = None
        for file in asset["files"]:
            if not all(isinstance(file.get(key), str) and file[key] for key in ("role", "path", "blob_sha1")):
                errors.append(f"{asset_id}: incomplete file record")
                continue
            path = ROOT / file["path"]
            if not path.is_file():
                errors.append(f"{asset_id}: missing {file['path']}")
                continue
            if current_blob(path) != file["blob_sha1"]:
                errors.append(f"{asset_id}: working-tree blob mismatch {file['path']}")
            try:
                evidence_blob = committed_blob(evidence_commit, file["path"])
            except subprocess.CalledProcessError:
                evidence_blob = ""
                errors.append(f"{asset_id}: evidence commit:path unavailable {file['path']}")
            if evidence_blob != file["blob_sha1"]:
                errors.append(f"{asset_id}: evidence commit:path blob mismatch {file['path']}")
            if file["role"] == "primary":
                if primary is not None:
                    errors.append(f"{asset_id}: multiple primary files")
                primary = path
        if primary is None:
            errors.append(f"{asset_id}: primary file required")
        elif primary.suffix == ".json":
            primary_data = json.loads(primary.read_text())
            if primary_data.get("status") != artifact.get("status"):
                errors.append(f"{asset_id}: artifact-local primary status mismatch")
            primary_canonical = primary_data.get("canonical_sha256_without_this_field", primary_data.get("canonical_sha256"))
            if primary_canonical != artifact.get("canonical_sha256"):
                errors.append(f"{asset_id}: artifact-local primary canonical mismatch")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "PROOF_REPLAY_COMPLETE: "
        f"{len(data['assets'])} positive assets; mandatory query metadata, current authority controller snapshot, "
        "artifact/current-authority separation, evidence commit:path blobs, working-tree blobs, and primary statuses verified"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
