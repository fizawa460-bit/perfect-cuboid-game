#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ARTIFACT = HERE / "ex4-10s-mutable-routing-source-lock-policy-repair-scratch.json"
WRAPPER = ROOT / "stages/stage32/proof/verify_stage32_claim_dag.py"
IMPL = ROOT / "stages/stage32/proof/verify_stage32_claim_dag_impl.py"
ACTIVE = ROOT / "stages/stage32/proof/verify_stage32_active_frontier.py"
EX4_STATE = HERE / "MAIN-STATE.json"


def git_blob_sha(path):
    return subprocess.check_output(
        ["git", "-C", str(ROOT), "hash-object", str(path)], text=True
    ).strip()


def canonical_sha256(data):
    d = dict(data)
    expected = d.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(
        json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    assert got == expected, (got, expected)
    return got


def main():
    data = json.loads(ARTIFACT.read_text())
    canonical_sha256(data)

    repair = data["repair"]
    assert git_blob_sha(WRAPPER) == repair["wrapper_blob_sha1"]
    assert git_blob_sha(IMPL) == repair["frozen_impl_blob_sha1"]

    snapshot = ROOT / repair["historical_snapshot_path"]
    assert snapshot.is_file()
    assert git_blob_sha(snapshot) == repair["historical_snapshot_blob_sha1"]
    assert repair["historical_snapshot_blob_sha1"] == data["problem"]["current_blob_before_transition"]

    # The live state is now expected to have advanced; the old routing bytes are
    # retained under the hash-named immutable snapshot instead of requiring the
    # working tree to remain frozen forever.
    assert git_blob_sha(EX4_STATE) != data["problem"]["current_blob_before_transition"]

    spec = importlib.util.spec_from_file_location("stage32_claim_wrapper", WRAPPER)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert mod._HISTORICAL_ROUTING_STATUSES == {"DECLARED_GOAL", "SUPERSEDED", "REVOKED"}
    locked = mod._historical_blob_bytes(data["problem"]["current_blob_before_transition"])
    assert mod.git_blob_sha1(locked) == data["problem"]["current_blob_before_transition"]

    subprocess.check_call(["python", str(WRAPPER), "--integrity"])
    subprocess.check_call(["python", str(ACTIVE)])

    final = subprocess.run(
        ["python", str(WRAPPER), "--final"],
        text=True,
        capture_output=True,
        check=False,
    )
    assert final.returncode == 2, (final.returncode, final.stdout, final.stderr)
    assert "NOT_READY_STAGE32_FINAL_CHECK" in final.stdout

    old_ceiling = data["claim_ceiling_at_policy_repair_subleaf"]
    assert old_ceiling["claim_sync_complete"] is False
    assert old_ceiling["ex4_main_state_updated"] is False
    assert old_ceiling["terminal_candidate_registered_provisional"] is False

    later = data["later_transition"]
    assert later["state_transition_completed_after_this_subleaf"] is True
    assert later["registered_claim_id"] == "S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V1"
    assert later["authority_status"] == "PROVISIONAL"
    assert later["hostile_audit_still_required"] is True

    print(json.dumps({
        "artifact": ARTIFACT.name,
        "canonical_sha256": data["canonical_sha256_without_this_field"],
        "wrapper_blob_sha1": repair["wrapper_blob_sha1"],
        "impl_blob_sha1": repair["frozen_impl_blob_sha1"],
        "historical_snapshot_blob_sha1": repair["historical_snapshot_blob_sha1"],
        "claim_dag_integrity": "PASS",
        "active_frontier_integrity": "PASS",
        "final_check": "NOT_READY_STAGE32_FINAL_CHECK",
        "result": "PASS_EX4_10S_ROUTING_SOURCE_LOCK_POLICY_REPAIR"
    }, indent=2))


if __name__ == "__main__":
    main()
