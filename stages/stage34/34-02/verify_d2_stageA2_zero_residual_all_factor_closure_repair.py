#!/usr/bin/env python3
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_VERIFIER = HERE / "verify_d2_stageA2_zero_residual_all_factor_closure.py"
CERT = HERE / "d2-stageA2-zero-residual-all-factor-closure-assembly-certificate.json"

NEW_LOCKS = {
    "full_support_survivor_commitment": (
        "d2-stageA2-full-support-d1-survivor-id-commitment.json",
        "8528dd5b3767f3980827590e22f15e015529ad7c",
    ),
    "genus2_rankle1_audit_receipt": (
        "d2-stageA2-genus2-rankle1-14-hostile-audit-promotion-receipt.json",
        "79f635a01452e4ac41ba7b18c40f94c2ef9be62a",
    ),
}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_pinned(name):
    path, expected = NEW_LOCKS[name]
    data = (HERE / path).read_bytes()
    assert git_blob_sha(data) == expected
    return json.loads(data)


def load(name):
    return json.loads((HERE / name).read_text())


def digest_ids(ids):
    return hashlib.sha256(("\n".join(sorted(ids)) + "\n").encode()).hexdigest()


def main():
    subprocess.run([sys.executable, str(BASE_VERIFIER)], check=True)

    commitment = load_pinned("full_support_survivor_commitment")
    receipt = load_pinned("genus2_rankle1_audit_receipt")

    assert commitment["source"]["run"] == 33512504700
    assert commitment["source"]["job"] == 99871456739
    assert commitment["source"]["artifact_id"] == 9802225387
    assert commitment["source"]["artifact_zip_digest"] == "sha256:eee10b6d11542422a1f8fbda84a091ebd1208353a31841bc969f812827cbe18b"
    assert commitment["source"]["payload_sha256"] == "sha256:849058b6ab53f5efad68ef1394472af808f66588d2b7bd13aca197759a1fd36d"
    assert commitment["d1_survivor_count"] == 92
    assert commitment["d2_survivor_count"] == 0
    assert commitment["d1_survivor_counts_by_q"] == {
        "20/21": 24,
        "80/39": 12,
        "24/7": 8,
        "84/13": 8,
        "48/55": 8,
        "20/99": 16,
        "60/11": 16,
    }

    audit = receipt["hostile_audit"]
    assert audit["review_node"] == "PRR_kwDOTr52Y88AAAABLwVwQw"
    assert audit["review_id"] == 5083852867
    assert audit["audited_head"] == "35d250ea96271c924b205383a8486fdcdcddd08f"
    assert audit["result"] == "PASS"
    auth = receipt["authorized_promotion"]
    assert (auth["before_remaining_branches"], auth["closed_branches"], auth["after_remaining_branches"]) == (44, 14, 30)

    ids = []
    rz = load("d2-stageA2-rankzero-AB-complete-pullback.json")
    ids += [r["branch_id"] for r in rz["branches"]]

    r1 = load("d2-stageA2-rank1-mw-congruence-sieve-certificate.json")
    ids += [r[1] for r in r1["closed"]]

    g0 = load("d2-stageA2-genus2-rankzero-closure-certificate.json")
    ids += [r["branch_id"] for r in g0["closed"]]

    g1 = load("d2-stageA2-genus2-rankle1-14-closure-certificate.json")
    assert (g1["input_remaining_branches"], g1["closed_branches"], g1["remaining_branches"]) == (44, 14, 30)
    assert auth["closed_by_q"] == g1["closed_by_q"]
    assert auth["after_by_q"] == g1["remaining_by_q"]
    ids += [r["branch_id"] for r in g1["closed_records"]]

    two = load("d2-stageA2-two-orbit-audit-promotion-certificate.json")
    ids += list(two["promoted_closures"]["all"])

    alt = load("d2-stageA2-two-rankzero-alternate-audit-promotion-certificate.json")
    ids += list(alt["promoted_closures"]["all"])

    cab = load("d2-stageA2-candidateAB-hostile-reaudit-promotion-certificate.json")
    ids += list(cab["candidate_A"]["direct_representatives"])
    ids += list(cab["candidate_A"]["sign_partners"])
    ids += list(cab["candidate_B"]["closed_branch_ids"])

    q80 = load("d2-stageA2-pr1486-q8039-hostile-audit-promotion-certificate.json")
    ids += list(q80["promotion"]["closed_branch_ids"])

    q84 = load("d2-stageA2-pr1489-q8413-hostile-audit-promotion-certificate.json")
    ids += list(q84["promotion"]["closed_branch_ids"])

    assert len(ids) == 92
    assert len(set(ids)) == 92
    closure_digest = digest_ids(ids)
    assert closure_digest == "7d43cd93f9329b48fa981857c10b03ad7a9df985af057ff1845001ca4fcefa6f"
    assert closure_digest == commitment["d1_survivor_ids_sha256"]

    cert = json.loads(CERT.read_text())
    assert cert["repair_of_hostile_audit_review_id"] == 5087093035
    assert cert["source_locks"]["full_support_survivor_commitment"] == list(NEW_LOCKS["full_support_survivor_commitment"])
    assert cert["source_locks"]["genus2_rankle1_audit_receipt"] == list(NEW_LOCKS["genus2_rankle1_audit_receipt"])
    assert cert["audit_lineage"]["pr1482_genus2_rankle1_14_review_id"] == 5083852867
    assert cert["audit_lineage"]["pr1482_genus2_rankle1_14_audited_head"] == "35d250ea96271c924b205383a8486fdcdcddd08f"
    assert cert["audit_lineage"]["pr1482_genus2_rankle1_14_authorized_transition"] == "44 -> 30"
    assert cert["full_support_survivor_set_commitment"]["d1_survivor_ids_sha256"] == closure_digest
    assert cert["assembly_result"]["full_support_survivor_commitment_equals_closure_commitment"] is True

    assert cert["firewalls"]["hostile_audit_passed"] is False
    assert cert["firewalls"]["D2_all_factor_branches_closed_authoritative"] is False
    assert cert["firewalls"]["direct_cover_rational_points_complete"] is False
    assert cert["firewalls"]["all_multiples_closed"] is False
    assert cert["firewalls"]["R29_EXT_CHANG_C_closed"] is False
    print("PASS_EXACT_CUMULATIVE_ALL_FACTOR_CLOSURE_AUDIT_REPAIR_PREAUDIT")


if __name__ == "__main__":
    main()
