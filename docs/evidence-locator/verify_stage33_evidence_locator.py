#!/usr/bin/env python3
"""Verify the Stage33 evidence-locator extension against immutable source locks."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REGISTRY = HERE / "stage33.json"
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
        errors.append("invalid authority source SHA")
        controller = {}
    else:
        try:
            blob = committed_blob(source["commit_sha"], source["path"])
            if blob != source["blob_sha1"]:
                errors.append("authority source commit:path blob mismatch")
            controller = json.loads(committed_text(source["commit_sha"], source["path"]))
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            errors.append("authority source unavailable")
            controller = {}

    ids = [asset.get("asset_id") for asset in data["assets"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate Stage33 asset_id")

    for asset in data["assets"]:
        aid = asset.get("asset_id", "<missing>")
        authority = asset["current_authority_snapshot"]
        try:
            row = nested(controller, authority["controller_key"])
        except (KeyError, TypeError):
            errors.append(f"{aid}: controller key missing")
            row = {}
        if row.get("status") != authority.get("status"):
            errors.append(f"{aid}: current-authority status mismatch")
        if row.get("canonical_sha256") != authority.get("canonical_sha256"):
            errors.append(f"{aid}: current-authority canonical mismatch")

        artifact = asset["artifact"]
        if not SHA256.fullmatch(artifact.get("canonical_sha256", "")):
            errors.append(f"{aid}: invalid artifact canonical")
        if artifact.get("canonical_sha256") != authority.get("canonical_sha256"):
            errors.append(f"{aid}: artifact/current-authority canonical mismatch")

        evidence_commit = asset["evidence_commit_sha"]
        if not SHA1.fullmatch(evidence_commit):
            errors.append(f"{aid}: invalid evidence commit")
            continue
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
                primary = path
        if primary is None:
            errors.append(f"{aid}: primary file missing")
            continue
        primary_data = json.loads(primary.read_text())
        if primary_data.get("canonical_sha256") != artifact.get("canonical_sha256"):
            errors.append(f"{aid}: primary canonical mismatch")
        try:
            primary_status = nested(primary_data, artifact["status_key"])
        except (KeyError, TypeError):
            primary_status = None
        if primary_status != artifact.get("status"):
            errors.append(f"{aid}: primary status mismatch")

        for field in ("objects", "aliases", "relations", "outputs", "candidate_queries", "limitations", "files"):
            if not asset.get(field):
                errors.append(f"{aid}: empty {field}")

    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1
    print(f"PROOF_REPLAY_COMPLETE: {len(data['assets'])} Stage33 positive assets verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
