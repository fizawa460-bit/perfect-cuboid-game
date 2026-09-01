#!/usr/bin/env python3
import json
import pathlib
import subprocess
import sys

KEY = "stages/stage34/runkeys/stage34-01-mw-full-group.json"
EXPECTED_FIBERS = ["20/21", "80/39", "24/7", "84/13", "48/55", "20/99", "60/11"]
EXPECTED_EXTERNAL_COMMIT = "bd3018b896c8ac15b56cadc382af1477dca9e97a"


def emit(ok: bool, reason: str) -> None:
    safe = reason.replace("\n", " ").replace("\r", " ")
    print(f"authorized={'true' if ok else 'false'}")
    print(f"reason={safe}")


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], text=True, capture_output=True)


if len(sys.argv) != 3:
    emit(False, "usage requires BEFORE HEAD")
    raise SystemExit(0)

before, head = sys.argv[1], sys.argv[2]
if not before or not head:
    emit(False, "missing before/head")
    raise SystemExit(0)

if git("cat-file", "-e", f"{before}^{{commit}}").returncode != 0:
    emit(False, "before commit unavailable")
    raise SystemExit(0)

changed = git("diff", "--name-only", before, head)
if changed.returncode != 0 or KEY not in changed.stdout.splitlines():
    emit(False, "dedicated run-key not changed in actual commit range")
    raise SystemExit(0)

new_path = pathlib.Path(KEY)
try:
    new = json.loads(new_path.read_text(encoding="utf-8"))
except Exception as exc:
    emit(False, f"new key parse failure: {exc}")
    raise SystemExit(0)

old_show = git("show", f"{before}:{KEY}")
if old_show.returncode == 0:
    try:
        old = json.loads(old_show.stdout)
    except Exception as exc:
        emit(False, f"old key parse failure: {exc}")
        raise SystemExit(0)
else:
    old = {"generation": 0, "armed": False}

checks = [
    (new.get("schema") == "STAGE34_01_MW_FULL_GROUP_RUNKEY_V1", "schema"),
    (new.get("armed") is True, "armed"),
    (isinstance(new.get("generation"), int) and new["generation"] > int(old.get("generation", 0)), "generation"),
    (new.get("paper_c_external_commit") == EXPECTED_EXTERNAL_COMMIT, "external_commit"),
    (new.get("fibers") == EXPECTED_FIBERS, "fibers"),
    (new.get("planned_heavy_jobs") == 1, "job_count"),
    (new.get("effective_heavy_concurrency") == 1, "concurrency"),
    (new.get("artifact_max_bytes") == 1048576, "artifact_cap"),
    (new.get("retention_days") == 1, "retention"),
]
failed = [name for ok, name in checks if not ok]
if failed:
    emit(False, "semantic gate failed: " + ",".join(failed))
    raise SystemExit(0)

emit(True, f"generation {new['generation']} explicitly armed")
