#!/usr/bin/env python3
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ARTIFACT = HERE / "ex4-10s-retained-bounded-terminal-candidate.json"


def csha(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def git_blob_sha(path):
    return subprocess.check_output(
        ["git", "-C", str(ROOT), "hash-object", str(path)], text=True
    ).strip()


def check_lock(lock):
    path = ROOT / lock["path"]
    assert path.is_file(), lock["path"]
    if "blob_sha1" in lock:
        assert git_blob_sha(path) == lock["blob_sha1"], lock["path"]
    if "canonical_sha256" in lock:
        obj = json.loads(path.read_text())
        expected = lock["canonical_sha256"]
        assert obj.get("canonical_sha256_without_this_field") == expected
        stripped = dict(obj)
        stripped.pop("canonical_sha256_without_this_field", None)
        assert csha(stripped) == expected


def main():
    data = json.loads(ARTIFACT.read_text())
    expected = data.pop("canonical_sha256_without_this_field")
    assert csha(data) == expected

    for lock in data["source_locks"].values():
        check_lock(lock)

    subprocess.check_call([
        "python",
        str(HERE / "verify_ex4_10_bounded_terminal_decision_certificate_assembly_scratch.py"),
    ])

    terminal = data["terminal_candidate"]
    assert terminal["outcome"] == "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"
    assert terminal["bounded_obstruction_only"] is True
    assert terminal["projective_pair_classes"] == 24
    assert terminal["W_action_image"] == "S3"
    assert terminal["W_action_transitive"] is True
    assert terminal["delta0inf_line_counts"] == {"L1": 8, "L2": 8, "L3": 8}
    assert terminal["line_to_residue"] == {"L1": 73, "L2": 97, "L3": 235}
    assert terminal["absolute_W_line_identified"] is False
    assert terminal["absolute_Q602_residue_identified"] is False

    sync = data["claim_sync"]
    assert sync["registered_claim_id"] == "S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V1"
    assert sync["target_authority_status"] == "PROVISIONAL"
    assert sync["claim_sync_complete_after_registry_and_state_update"] is True
    assert sync["active_frontier_semantics_changed"] is False
    assert sync["stage32_main_promotion"] is False

    ceiling = data["credit_ceiling"]
    assert ceiling["audit_ready_full_target_closure"] is True
    assert ceiling["hostile_audit_pass"] is False
    assert ceiling["full_target_closure"] is False
    assert ceiling["Q602_excluded"] is False
    assert ceiling["O210_excluded"] is False
    assert ceiling["stage32_main_credit"] is False

    print(json.dumps({
        "result": "PASS_EX4_10S_RETAINED_TERMINAL_CANDIDATE",
        "canonical_sha256": expected,
        "terminal_outcome": terminal["outcome"],
        "authority_status": "PROVISIONAL",
        "hostile_audit_pass": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
