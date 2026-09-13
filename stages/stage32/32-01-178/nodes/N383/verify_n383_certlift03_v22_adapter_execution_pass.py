#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent

EXPECTED_N382_BLOB = "0b5c43009e19606a306bc71a55bf9acfba078c2f"
EXPECTED_N382_CANONICAL = "f5b6b08264c1743df1d633bad47c9cb435ba569da3eff2ce808053cfb36eec1d"
EXPECTED_N383_CANONICAL = "f12b8a4696d2e82f8541f89fcb80ee47243443dacc2c26df072a4831ac4b7182"
EXPECTED_ADAPTER_BLOB = "327aa601acad47bc1e486cccbbac3d3dee7c2681"
EXPECTED_V22_SOURCE_RECEIPT_BLOB = "2ca912e9aafeebfc8962a127887947f5c9ec0b90"
EXPECTED_V22_SOURCE_RECEIPT_CANONICAL = "16bba90759c021552a80950d7d0feef00323cd8c6ac47767678b0a65bc2381ce"
EXPECTED_RESULT_CANONICAL = "597fe83b10c7a23f1da9748423ea3f70a78d448991a253777b64cab554c7ffaf"


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def check_blob(path: Path, expected: str, label: str) -> None:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob(path) == expected, f"{label} blob drift")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--producer-root", required=True)
    ap.add_argument("--audited-adapter-root", required=True)
    ap.add_argument("--v22-main-root", required=True)
    for n in range(193, 199):
        ap.add_argument(f"--cut{n}-root", required=True)
    args = ap.parse_args()

    n382_path = HERE.parent / "N382" / "STATE.json"
    n383_path = HERE / "STATE.json"
    check_blob(n382_path, EXPECTED_N382_BLOB, "N382 state")
    n382 = load(n382_path)
    req(canonical(n382) == EXPECTED_N382_CANONICAL, "N382 canonical drift")

    n383 = load(n383_path)
    req(canonical(n383) == EXPECTED_N383_CANONICAL, "N383 canonical drift")
    req(n383["canonical_sha256_without_this_field"] == EXPECTED_N383_CANONICAL, "N383 retained canonical drift")
    req(n383["status"] == "CERTLIFT03_V22_ADAPTER_EXACT_EXECUTION_PASS_PENDING_RECEIPT_AND_HOSTILE_AUDIT_NO_CREDIT", "N383 status drift")

    producer = Path(args.producer_root).resolve()
    script = producer / "stages/stage32/cert-lift/certlift03_v22_consumption_adapter.py"
    receipt = producer / "stages/stage32/cert-lift/CERTLIFT-03-V22-AUTHORITY-SOURCE-RECEIPT.json"
    check_blob(script, EXPECTED_ADAPTER_BLOB, "V22 adapter")
    check_blob(receipt, EXPECTED_V22_SOURCE_RECEIPT_BLOB, "V22 source receipt")
    receipt_obj = load(receipt)
    req(receipt_obj["canonical_sha256_without_this_field"] == EXPECTED_V22_SOURCE_RECEIPT_CANONICAL, "V22 source receipt stored canonical drift")
    req(canonical(receipt_obj) == EXPECTED_V22_SOURCE_RECEIPT_CANONICAL, "V22 source receipt canonical replay drift")

    env = dict(os.environ)
    env.update({
        "CERTLIFT_V22_MAIN_ROOT": str(Path(args.v22_main_root).resolve()),
        "CERTLIFT_ADAPTER_AUDITED_ROOT": str(Path(args.audited_adapter_root).resolve()),
    })
    for n in range(193, 199):
        env[f"CERTLIFT_CUT{n}_ROOT"] = str(Path(getattr(args, f"cut{n}_root")).resolve())

    p = subprocess.run(
        ["python", str(script), "--self-check"],
        env=env,
        text=True,
        capture_output=True,
        check=True,
    )
    lines = [line.strip() for line in p.stdout.splitlines() if line.strip()]
    req(lines, "V22 adapter produced no output")
    live = json.loads(lines[-1])

    req(live["status"] == "PASS_EXACT_HOSTILE_AUDITED_V22_CONSUMPTION_ADAPTER_CANDIDATE", "V22 live status drift")
    req(live["canonical"] == EXPECTED_RESULT_CANONICAL, "V22 live canonical drift")
    inc = live["candidate_increment"]
    overlap = live["prior_authority_overlap"]
    req(inc["incremental_blocks"] == 1369, "V22 incremental block drift")
    req(inc["incremental_terminals"] == 154697, "V22 incremental terminal drift")
    req(inc["candidate_remaining_terminals_if_later_consumed"] == 47589703313957134649501, "V22 candidate remainder drift")
    req(inc["incremental_block_stream_sha256"] == "e1bf3732f8ad64b882cfc6cbca1296211088df2b106633e8c85eae5c9e2b0abd", "V22 incremental stream drift")
    req(overlap == {
        "cut191_blocks": 0,
        "cut193_blocks": 40,
        "cut194_blocks": 33,
        "cut195_blocks": 29,
        "cut196_blocks": 59,
        "cut197_blocks": 72,
        "cut198_blocks": 75,
        "double_charge": False,
        "n357_blocks": 0,
        "n358_blocks": 0,
        "n358_overlap_reason": "audited empty incremental domain on g1-d008/e8",
        "union_blocks": 308,
    }, "V22 prior-overlap accounting drift")
    req(live["firewall"]["hostile_audit_required_before_consumption"] is True, "V22 hostile-audit gate lost")
    req(live["firewall"]["main_authority_mutated"] is False, "V22 adapter mutated MAIN")
    req(live["firewall"]["main_pruning_credit"] is False, "V22 adapter granted MAIN credit")

    req(n383["producer"]["retained_result_receipt_present"] is False, "N383 receipt boundary drift")
    req(n383["producer"]["v22_adapter_hostile_audited"] is False, "N383 audit boundary drift")
    req(n383["promotion_boundary"]["v22_increment_consumable_now"] is False, "V22 increment consumed early")
    req(n383["n101_contract"]["remains_stopped"] is True, "N101 stop lost")
    req(not any(n383["credit"].values()), "N383 credit firewall regression")
    req(not any(n383["anti_loop"].values()), "N383 anti-loop regression")

    print(json.dumps({
        "canonical": EXPECTED_RESULT_CANONICAL,
        "incremental_blocks": 1369,
        "incremental_terminals": 154697,
        "main_pruning_credit": False,
        "n101_reopened_credit": False,
        "next_gate": n383["next_gate"],
        "prior_overlap_union_blocks": 308,
        "v22_increment_consumable_now": False,
        "verdict": "PASS_N383_CERTLIFT03_V22_ADAPTER_EXECUTION_PASS_AUDIT_WAIT_BOUNDARY"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
