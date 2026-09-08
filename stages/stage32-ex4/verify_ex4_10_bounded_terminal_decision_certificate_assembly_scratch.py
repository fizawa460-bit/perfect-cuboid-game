#!/usr/bin/env python3
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ARTIFACT = HERE / "ex4-10-bounded-terminal-decision-certificate-assembly-scratch.json"

def canonical_sha256(data):
    d = dict(data)
    expected = d.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(
        json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    assert got == expected, (got, expected)
    return got

def git_blob_sha(path):
    return subprocess.check_output(
        ["git", "-C", str(ROOT), "hash-object", str(path)], text=True
    ).strip()

def check_json_lock(lock):
    path = ROOT / lock["path"]
    assert path.exists(), lock["path"]
    if "blob_sha1" in lock:
        assert git_blob_sha(path) == lock["blob_sha1"], lock["path"]
    if "canonical_sha256" in lock:
        obj = json.loads(path.read_text())
        assert obj.get("canonical_sha256_without_this_field") == lock["canonical_sha256"], lock["path"]

def main():
    data = json.loads(ARTIFACT.read_text())
    canonical_sha256(data)

    for lock in data["source_locks"].values():
        check_json_lock(lock)

    subprocess.check_call(["python", str(HERE / "verify_ex4_08_frozen_package_ambiguity_scratch.py")])
    subprocess.check_call(["python", str(HERE / "verify_ex4_09_independent_crosscheck_circularity_scratch.py")])

    outcome = data["terminal_outcome"]
    assert outcome["name"] == "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"
    assert outcome["absolute_W_line_identified"] is False
    assert outcome["absolute_Q602_residue_identified"] is False

    fam = data["replayable_obstruction_chain"]["strongest_projective_identification_family"]
    assert fam["retained_group_order"] == 48
    assert fam["center_order"] == 2
    assert fam["projective_pair_classes"] == 24
    assert fam["W_action_image"] == "S3"
    assert fam["W_action_transitive"] is True
    assert fam["source_to_W_bijections"] == 6
    assert fam["bijection_multiplicity"] == 4
    assert fam["delta0inf_line_counts"] == {"L1": 8, "L2": 8, "L3": 8}

    target = data["replayable_obstruction_chain"]["retained_target"]
    assert target["line_to_residue"] == {"L1": 73, "L2": 97, "L3": 235}

    indep = data["independence_and_circularity"]
    assert indep["ex4_09_result"] == "PASS_CANDIDATE"
    for key in [
        "seed_line_invariant",
        "residue_numbers_not_used_to_construct_marking_family",
        "literal_STinverse_not_promoted",
        "canonical_gauge_not_promoted",
        "stage33_marking_not_imported_without_adapter",
        "post1648j_not_promoted_to_audited",
    ]:
        assert indep[key] is True, key

    reentry = data["minimal_reentry_interface"]["sufficient_new_data"]
    assert reentry == [
        "DIRECT_DELTA0INF_RETAINED_J2_COORDINATE",
        "EXACT_PRODUCT_ELEMENT_BINDING",
        "BRANCH_LABELLED_SYMPLECTIC_HOMOLOGY_OR_LEVEL_MARKING",
    ]

    ceiling = data["claim_ceiling"]
    assert ceiling["full_target_closure_candidate_for_EX4_marking_decision"] is True
    assert ceiling["audit_ready_full_target_closure"] is False
    assert ceiling["hostile_audit_pass"] is False
    for key in [
        "fixed_source_package_cannot_select_absolute_W_line_audited_credit",
        "absolute_W_line_and_Q602_residue_identified",
        "Q602_residue_contraction_credit",
        "Q602_excluded",
        "O210_excluded",
        "stage32_main_credit",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ]:
        assert ceiling[key] is False, key

    management = data["management_transition"]
    assert management["claim_sync_contract_opened"] is True
    assert management["claim_sync_complete"] is False
    assert management["current_EX4_MAIN_STATE_intentionally_unchanged_in_this_commit"] is True
    assert management["final_stage32_check_expected"] == "NOT_READY_STAGE32_FINAL_CHECK"
    assert management["next_management_leaf"] == "EX4-10S_CLAIM_SYNC_AND_ROUTING_STATE_CONSISTENCY"

    assert data["status"].endswith("CLAIM_SYNC_PENDING_NOT_AUDITED")

    print(json.dumps({
        "artifact": ARTIFACT.name,
        "canonical_sha256": data["canonical_sha256_without_this_field"],
        "terminal_outcome_candidate": outcome["name"],
        "projective_pair_classes": fam["projective_pair_classes"],
        "delta0inf_line_counts": fam["delta0inf_line_counts"],
        "claim_sync_complete": management["claim_sync_complete"],
        "audit_ready_full_target_closure": ceiling["audit_ready_full_target_closure"],
        "result": "PASS_EX4_10_ASSEMBLY_SYNC_PENDING"
    }, indent=2))

if __name__ == "__main__":
    main()
