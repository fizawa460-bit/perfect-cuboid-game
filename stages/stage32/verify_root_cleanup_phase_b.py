#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
H = Path(__file__).resolve().parent
MANIFEST = H / "archive" / "legacy-root" / "manifest.json"
STATE = H / "MAIN-STATE.json"
EXPECTED_MANIFEST_CANONICAL = "8bbc6435cace28874ed46d21b2b4dd80773bef04f003cac6eb92e093439d436d"
EXPECTED_RELOCATIONS = {
    "stages/stage32/POST_B16_LITERATURE_RECEIVER_ROADMAP.md": ("stages/stage32/archive/legacy-root/POST_B16_LITERATURE_RECEIVER_ROADMAP.md", "d852e82372f45df920530bded3c426a017578734"),
    "stages/stage32/POST_B16_RELEASE_CONTRACT.md": ("stages/stage32/archive/legacy-root/POST_B16_RELEASE_CONTRACT.md", "7d5de7d8870b9722cb28e4eddcd4960434eec0d6"),
    "stages/stage32/controller-history-through-32-21ad.json": ("stages/stage32/archive/legacy-root/controller-history-through-32-21ad.json", "1f89f1722fb4c34c932128f6d2cc2286b4918a65"),
    "stages/stage32/controller-v243-post1505-gauge-merge-released.json": ("stages/stage32/archive/legacy-root/controller-v243-post1505-gauge-merge-released.json", "a9c468260d86b90ca7ea9ff73a5293a17babc7a8"),
    "stages/stage32/controller-v246-post1520-retained-geometry-18-to-18-provisional.json": ("stages/stage32/archive/legacy-root/controller-v246-post1520-retained-geometry-18-to-18-provisional.json", "e0ed6329d654583a5aa63f7e93ed7a2300ea358a"),
    "stages/stage32/goal-and-stop-contract.json": ("stages/stage32/archive/legacy-root/goal-and-stop-contract.json", "430e37f9e002aa3d975f0ecb970e2d60932e145f"),
    "stages/stage32/post-b16-literature-receiver-contract.json": ("stages/stage32/archive/legacy-root/post-b16-literature-receiver-contract.json", "46acc2d3f11c855f7652625effe6e102d3730f8a"),
    "stages/stage32/post1504-antiloop-removal-policy.md": ("stages/stage32/archive/legacy-root/post1504-antiloop-removal-policy.md", "e2946c7c4d8d26ef4eedf70d1a9ce07e818f15b1"),
    "stages/stage32/post1505-trace-parity-bridge.md": ("stages/stage32/archive/legacy-root/post1505-trace-parity-bridge.md", "0b34468dda2d37608667653dbf0dcb5c6a33ec02"),
}


def fail(msg: str) -> None:
    raise SystemExit(msg)


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def tracked_files() -> list[str]:
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [p.decode() for p in raw.split(b"\0") if p]


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if canonical_sha(manifest) != EXPECTED_MANIFEST_CANONICAL:
        fail("cleanup manifest canonical mismatch")
    if manifest.get("canonical_sha256_without_this_field") != EXPECTED_MANIFEST_CANONICAL:
        fail("recorded cleanup manifest canonical mismatch")
    if manifest.get("relocation_only") is not True or manifest.get("deletion_of_content") is not False:
        fail("cleanup semantics moved")

    got = {x["old_path"]: (x["new_path"], x["blob_sha1"]) for x in manifest["relocated"]}
    if got != EXPECTED_RELOCATIONS:
        fail("relocation inventory moved")

    for old, (new, blob) in EXPECTED_RELOCATIONS.items():
        if (ROOT / old).exists():
            fail(f"legacy root path still exists: {old}")
        new_path = ROOT / new
        if not new_path.is_file():
            fail(f"archived path missing: {new}")
        if git_blob_sha(new_path) != blob:
            fail(f"archived blob changed: {new}")

    # These three files are the audit/control layer for this relocation and are
    # intentionally allowed to name the old paths. All other tracked files must not.
    skip = {
        ".github/workflows/stage32-root-cleanup-phase-b.yml",
        "stages/stage32/verify_root_cleanup_phase_b.py",
        "stages/stage32/archive/legacy-root/manifest.json",
    }
    for rel in tracked_files():
        if rel in skip or rel.startswith("stages/stage32/archive/legacy-root/"):
            continue
        path = ROOT / rel
        try:
            data = path.read_bytes()
        except OSError:
            continue
        for old in EXPECTED_RELOCATIONS:
            if old.encode() in data:
                fail(f"old full-path reference remains outside archive: {old} in {rel}")

    state = json.loads(STATE.read_text(encoding="utf-8"))
    cleanup = state["cleanup_gate"]
    if cleanup["stage32_root_cleanup_started"] is not True:
        fail("MAIN-STATE cleanup start not recorded")
    if cleanup["root_cleanup_phase"] != "PHASE_B_LOOSE_LEGACY_ROOT_RELOCATION_PENDING_HOSTILE_AUDIT":
        fail("MAIN-STATE cleanup phase moved")
    if cleanup["archive_manifest"] != "stages/stage32/archive/legacy-root/manifest.json":
        fail("MAIN-STATE archive manifest path moved")
    if cleanup["proof_or_source_locked_assets_may_be_deleted_without_reference_audit"] is not False:
        fail("unsafe cleanup permission detected")

    for rel in manifest["preserved_root_authority_files"]:
        if not (ROOT / rel).is_file():
            fail(f"preserved root authority file missing: {rel}")
    fire = manifest["firewalls"]
    if fire != {
        "proof_or_source_locked_asset_deleted": False,
        "current_leaf_working_set_changed": False,
        "mathematical_credit_changed": False,
        "heavy_compute_authorized": False,
    }:
        fail("cleanup firewalls moved")

    print("PASS Stage32 root cleanup phase B")
    print(f"manifest_canonical={EXPECTED_MANIFEST_CANONICAL}")
    print(f"relocated_file_count={len(EXPECTED_RELOCATIONS)}")
    print("byte_identical_relocation=true")
    print("old_full_path_reference_outside_archive=false")
    print("mathematical_credit_changed=false")


if __name__ == "__main__":
    main()
