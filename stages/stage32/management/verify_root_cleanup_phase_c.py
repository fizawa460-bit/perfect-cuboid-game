#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STAGE = ROOT / "stages" / "stage32"
MANIFEST = STAGE / "archive" / "legacy-root" / "manifest-phase-c.json"
STATE = STAGE / "MAIN-STATE.json"
EXPECTED_MANIFEST_CANONICAL = "6b84a64a6dc228a8ffddd16cbe941219ab69f6089fd60d9388d52a1b7a3eae51"
EXPECTED_RELOCATIONS = {
    "stages/stage32/HEAVY_WORKFLOW_POLICY.md": ("stages/stage32/archive/legacy-root/HEAVY_WORKFLOW_POLICY.md", "2e6ec123f7b3dd5320f79e59d57f3b0335aad66d"),
    "stages/stage32/HISTORY.md": ("stages/stage32/archive/legacy-root/HISTORY.md", "982a5eb1ceebccc114285bfe3a2429766a7e93bf"),
    "stages/stage32/ROADMAP-32-01-RESIDUAL-CLOSURE.md": ("stages/stage32/archive/legacy-root/ROADMAP-32-01-RESIDUAL-CLOSURE.md", "2acdb26b4cef3c4bf0caf4fe017ed34958eb762e"),
    "stages/stage32/ROADMAP-32-19-21-REANCHOR.md": ("stages/stage32/archive/legacy-root/ROADMAP-32-19-21-REANCHOR.md", "88340fd2f5190a1cc1c8c3e6487ce757103899ba"),
    "stages/stage32/post1728-remap-audit-handoff.md": ("stages/stage32/archive/legacy-root/post1728-remap-audit-handoff.md", "c6bddb89f537f3d570fce25263f2222495c7e267"),
    "stages/stage32/verify_root_cleanup_phase_b.py": ("stages/stage32/archive/legacy-root/verify_root_cleanup_phase_b.py", "8203e6afb26777bd924f96c31c584877a49b7fd9"),
    "stages/stage32/mainbatch-final-chain-reentry-20260909.json": ("stages/stage32/management/mainbatch-final-chain-reentry-20260909.json", "52dd699c1dc6a43de0db1bce79a619e4544371fa"),
}
CANONICAL_EX_ROOTS = ["stages/stage32-ex1", "stages/stage32-ex2", "stages/stage32-ex3", "stages/stage32-ex4"]


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
    if manifest["canonical_sha256_without_this_field"] != EXPECTED_MANIFEST_CANONICAL or canonical_sha(manifest) != EXPECTED_MANIFEST_CANONICAL:
        fail("phase-C manifest canonical mismatch")
    if manifest["relocation_only"] is not True or manifest["deletion_of_content"] is not False:
        fail("phase-C relocation semantics changed")

    got = {x["old_path"]: (x["new_path"], x["blob_sha1"]) for x in manifest["relocated"]}
    if got != EXPECTED_RELOCATIONS:
        fail("phase-C relocation inventory changed")
    for old, (new, blob) in EXPECTED_RELOCATIONS.items():
        if (ROOT / old).exists():
            fail(f"relocated loose root path still exists: {old}")
        p = ROOT / new
        if not p.is_file() or git_blob_sha(p) != blob:
            fail(f"relocated file missing or changed: {new}")

    for rel in CANONICAL_EX_ROOTS:
        if not (ROOT / rel).is_dir():
            fail(f"canonical audited EX evidence root missing: {rel}")
    if not (ROOT / "stages/stage32-ex5").is_dir():
        fail("retained EX5 evidence root missing")
    if not (STAGE / "integrated-ex" / "README.md").is_file():
        fail("integrated EX1-EX4 view missing")
    if not (STAGE / "README.md").is_file():
        fail("Stage32 root landing README missing")

    skip = {
        ".github/workflows/stage32-root-cleanup-phase-b.yml",
        "stages/stage32/archive/legacy-root/manifest-phase-c.json",
        "stages/stage32/management/verify_root_cleanup_phase_c.py",
    }
    preserved_historical_prefixes = ("stages/stage32/archive/", "stages/stage32/proof/historical-routing-blobs/")
    for rel in tracked_files():
        if rel in skip or rel.startswith(preserved_historical_prefixes):
            continue
        path = ROOT / rel
        try:
            data = path.read_bytes()
        except OSError:
            continue
        for old in EXPECTED_RELOCATIONS:
            if old.encode() in data:
                fail(f"stale relocated full-path reference remains: {old} in {rel}")

    state = json.loads(STATE.read_text(encoding="utf-8"))
    cleanup = state["cleanup_gate"]
    if cleanup["root_cleanup_phase"] != "PHASE_C_USER_FACING_EX1_EX4_INTEGRATION_AND_LOOSE_ROOT_RELOCATION":
        fail("MAIN-STATE phase-C cleanup routing missing")
    if cleanup["archive_manifest"] != "stages/stage32/archive/legacy-root/manifest-phase-c.json":
        fail("MAIN-STATE phase-C manifest path mismatch")
    if cleanup["proof_or_source_locked_assets_may_be_deleted_without_reference_audit"] is not False:
        fail("unsafe proof/source-lock cleanup permission")
    if cleanup["legacy_numbered_directories_physically_relocated"] is not False:
        fail("path-locked numbered legacy directories were falsely marked relocated")

    org = state["organizational_integration"]
    if org["former_ex1_ex4_user_facing_view"] != "stages/stage32/integrated-ex/README.md":
        fail("integrated EX view routing mismatch")
    if any(org["ordinary_separate_lane_startup"].values()):
        fail("EX1-EX4 still marked ordinary separate startup lanes")
    if org["EX5_separate_pr_active"] is not False:
        fail("merged EX5 is still marked as a separate active PR")
    if org["EX5_retained_evidence_merged_to_main"] is not True:
        fail("EX5 merged evidence routing missing")
    if org["integration_changes_mathematical_credit"] is not False:
        fail("organizational integration changed mathematical credit")

    expected_checkpoint = "stages/stage32/management/post-ex5-merge-final-chain-sync-20260910.json"
    if expected_checkpoint not in state["current_leaf_working_set"]:
        fail("post-EX5-merge current MAIN checkpoint not in working set")

    fire = manifest["firewalls"]
    for key in ["mathematical_credit_changed", "claim_core_changed", "hostile_audit_credit_self_assigned", "heavy_compute_authorized", "receiver_credit_changed", "stage32_closed", "merge_authorized"]:
        if fire[key] is not False:
            fail(f"phase-C firewall changed: {key}")

    print("PASS Stage32 root cleanup phase C")
    print(f"manifest_canonical={EXPECTED_MANIFEST_CANONICAL}")
    print(f"relocated_loose_root_file_count={len(EXPECTED_RELOCATIONS)}")
    print("integrated_ex1_ex4_view=true")
    print("canonical_audited_ex1_ex5_paths_preserved=true")
    print("historical_routing_blobs_preserved_immutable=true")
    print("ex5_separate_pr_active=false")
    print("ex5_retained_evidence_merged_to_main=true")
    print("legacy_numbered_paths_relocated=false")
    print("mathematical_credit_changed=false")


if __name__ == "__main__":
    main()
