#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
N377 = HERE / "STATE.json"
N376 = HERE.parent / "N376/STATE.json"

N377_BLOB = "ecbba41447f089ebd5100859b62d5d5ab75a16ca"
N377_CANON = "0086b11b55f77ee8cd852ff0557d1a2b1f952f50fb312f72faa747d5423874a4"
N376_BLOB = "ecfc6d5c35339305f11a5de6e95c3a644cc9910e"
N376_CANON = "81f59725176ad89d0cd32cce65967a8e45bc81849081342002ad4cd551f4d7e5"
CERTLIFT_HEAD = "3d4b16e7da3e2f4f1a078fb2e150ab6fd939bfda"
CERTLIFT_STATE_REL = Path("stages/stage32/cut-cert-lift/STATE.json")
CERTLIFT_STATE_BLOB = "c99c9b564568ba5a839b7a54dc395e758e0c3eb1"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected_blob: str, expected_canon: str | None = None) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
        req(canonical(obj) == expected_canon, f"canonical replay drift: {path}")
    return obj


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certlift-root", type=Path, required=True)
    args = ap.parse_args()

    n376 = checked(N376, N376_BLOB, N376_CANON)
    n377 = checked(N377, N377_BLOB, N377_CANON)

    root = args.certlift_root.resolve()
    req(exact_head(root) == CERTLIFT_HEAD, "CERT-LIFT exact head drift")
    producer_state_path = root / CERTLIFT_STATE_REL
    producer = checked(producer_state_path, CERTLIFT_STATE_BLOB)

    req(n376["status"] == "STOPPED_IDENTITY_ONLY_S3_NEEDS_NEW_SIGNATURE_INPUT_NO_CREDIT", "N376 stop boundary drift")
    req(n377["parent"]["n376_state_blob_sha1"] == N376_BLOB, "N377 parent blob drift")
    req(n377["parent"]["n376_state_canonical_sha256"] == N376_CANON, "N377 parent canonical drift")
    req(n377["status"] == "WAITING_ON_CERTLIFT_EXACT_SIGNATURE_NO_CREDIT", "N377 status drift")
    req(n377["producer"]["exact_head"] == CERTLIFT_HEAD, "N377 producer head drift")
    req(n377["producer"]["state_blob_sha1"] == CERTLIFT_STATE_BLOB, "N377 producer state blob drift")
    req(n377["producer"]["producer_result_consumable_now"] is False, "N377 prematurely consumes producer")

    req(producer["schema"] == "STAGE32_CUT_CERT_LIFT_STATE_V1", "CERT-LIFT state schema drift")
    req(producer["status"] == "ACTIVE", "CERT-LIFT state status drift")
    req(producer["active_node"] == "CERTLIFT-01_CERTIFICATE_SIGNATURE_EXTRACTION", "CERT-LIFT active node drift")
    req(producer["credit"]["main_pruning"] is False, "CERT-LIFT unexpectedly grants MAIN pruning")
    req(producer["credit"]["full178"] is False, "CERT-LIFT unexpectedly grants FULL178")
    req(producer["credit"]["merge_authorized"] is False, "CERT-LIFT unexpectedly grants merge authorization")

    obs = n377["current_observation"]
    req(obs["certlift_is_only_extracting_candidate_signatures"] is True, "N377 producer observation drift")
    req(obs["certlift_has_not_yet_proved_s1"] is True, "N377 S1 observation drift")
    req(obs["certlift_has_not_yet_proved_s2"] is True, "N377 S2 observation drift")
    req(obs["certlift_has_not_yet_published_integral_picard_action"] is True, "N377 Picard-action observation drift")
    req(obs["n376_stop_condition_remains_in_force"] is True, "N377 stop observation drift")

    kinds = [entry["kind"] for entry in n377["requested_interface"]["either"]]
    req(kinds == ["FINITE_SIGNATURE", "INTEGRAL_PICARD_ACTION"], "N377 acceptance alternatives drift")
    req(n377["requested_interface"]["negative_controls_required"] is True, "N377 negative-control firewall drift")
    req(n377["requested_interface"]["unknown_must_not_be_promoted"] is True, "N377 UNKNOWN firewall drift")

    for key, value in n377["credit"].items():
        req(value is False, f"N377 credit firewall drift: {key}")
    anti = n377["anti_loop"]
    req(all(value is False for value in anti.values()), "N377 anti-loop/heavy firewall drift")

    print(json.dumps({
        "verdict": "PASS_N377_CERTLIFT_PRODUCER_HANDOFF_WAIT_BOUNDARY",
        "producer_pr": 1803,
        "producer_exact_head": CERTLIFT_HEAD,
        "producer_active_node": producer["active_node"],
        "producer_result_consumable_now": False,
        "n376_stop_remains": True,
        "next_gate": n377["next_gate"],
        "main_pruning_credit": False,
        "full178_complete": False,
        "n101_reopened_credit": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
