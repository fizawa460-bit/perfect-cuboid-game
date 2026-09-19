#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "MB104-000707-FIBRATION-ISOTROPIC-SHELLS-PREFLIGHT-CERTIFICATE.json"
RUNKEY = HERE / "runkeys" / "000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"

LOCKS = {
    "runner_git_blob": HERE / "run_mb104_000707_fibration_isotropic_shells.py",
    "parent_verifier_git_blob": HERE / "verify_mb104_000707_fibration_isotropic_shells.py",
    "workunit_runner_git_blob": HERE / "run_mb104_000707_fibration_isotropic_shell_workunit.py",
    "workunit_verifier_git_blob": HERE / "verify_mb104_000707_fibration_isotropic_shell_workunit.py",
}


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


d = json.loads(CERT.read_text(encoding="utf-8"))
k = json.loads(RUNKEY.read_text(encoding="utf-8"))
assert d["schema"] == "STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_PREFLIGHT_V1"
assert d["status"] == "PRE_AUDIT_EXECUTION_PREFLIGHT_COLD_NO_NUMERICAL_RESULT_NO_CREDIT"
assert d["support"]["mask"] == "000707000f0f"
assert d["support"]["P2"] == 336
assert d["support"]["H_dot_P"] == 112
assert len(d["shells"]) == 4
expected = [
    (0,10,30,10,400,-320),
    (1,10,34,9,400,-288),
    (2,10,38,8,400,-256),
    (3,12,36,12,144,-192),
]
got = [
    (x["shell_index"],x["H_dot_F"],x["P_dot_F"],x["support_mass"],x["minus_transform_square"],x["transform_dot_P"])
    for x in d["shells"]
]
assert got == expected
for x in d["shells"]:
    a,b = (8,5) if x["H_dot_F"] == 10 else (4,3)
    assert x["transform_dot_P"] == a*x["P_dot_F"] - b*112
    assert 7*x["H_dot_F"] - 4*x["support_mass"] == x["P_dot_F"]

assert k["schema"] == "STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_RUNKEY_V1"
assert k["generation"] == 0
assert k["mode"] == "COLD"
assert k["armed"] is False
assert k["support_mask"] == "000707000f0f"
assert [x["shell_index"] for x in k["workunits"]] == [0,1,2,3]
assert k["pilot"]["required_before_scaleout"] is True
assert k["pilot"]["shell_index"] == 0
assert k["pilot"]["measured"] is False
assert k["resume"]["partition_key"] == "shell_index"
assert k["resume"]["expected_workunit_count"] == 4
assert k["concurrency"]["planned_effective_heavy_concurrency"] == 1
assert k["concurrency"]["stage_heavy_cap"] == 18
assert k["storage"]["repository_operating_budget_mb"] == 500
assert k["execution_gate"]["automatic_execution_authorized"] is False
assert k["execution_gate"]["state_transition_recorded"] is False

for key,path in LOCKS.items():
    got_blob = blob(path)
    assert d["source_locks"][key] == got_blob, (key, d["source_locks"][key], got_blob)
    assert k["source_locks"][key] == got_blob, (key, k["source_locks"][key], got_blob)

assert all(v is False for v in d["firewalls"].values())
assert all(v is False for v in k["credit"].values())
print("PASS: 000707 degree10/12 isotropic-shell execution preflight is exact, cold, partitioned, and zero-credit")
