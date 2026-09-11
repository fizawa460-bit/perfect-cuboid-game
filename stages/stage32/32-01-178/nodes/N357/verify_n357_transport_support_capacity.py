#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = HERE.parent / "N357-engine" / "verify_n357_transport_support_capacity.py"
N356_RECEIPT = HERE.parent / "N356" / "HOSTILE-AUDIT-PASS.json"

EXPECTED_ENGINE_BLOB = "479c783cb42d0952cc310708106787147b499240"
EXPECTED_N356_RECEIPT_BLOB = "4966d57f61624c1cfd313ae5d1fe5e33bb25e569"
EXPECTED_N356_RECEIPT_CANONICAL = "fdeedf56ba9dca97dc06175f892efeae09fd7ef0d3bb8670bfea438106227b74"
EXPECTED_N356_REVIEW = 5176607630
EXPECTED_N356_HEAD = "0cd222d4824e65ea122bc90ac0d48686ddae38f2"
EXPECTED_REMAIN_STRATA = 17128
EXPECTED_REMAIN_TERMINALS = 65396964990500233636214


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha_without(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_engine():
    actual = git_blob_sha1(ENGINE)
    if actual != EXPECTED_ENGINE_BLOB:
        raise ValueError(f"N357 frozen-engine source-lock regression: {actual}!={EXPECTED_ENGINE_BLOB}")
    spec = importlib.util.spec_from_file_location("s32_n357_frozen_engine", ENGINE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {ENGINE}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def validate_n356_receipt() -> dict:
    actual = git_blob_sha1(N356_RECEIPT)
    if actual != EXPECTED_N356_RECEIPT_BLOB:
        raise ValueError(f"N356 audit receipt blob regression: {actual}!={EXPECTED_N356_RECEIPT_BLOB}")
    receipt = json.loads(N356_RECEIPT.read_text())
    if receipt.get("canonical_sha256_without_this_field") != EXPECTED_N356_RECEIPT_CANONICAL:
        raise ValueError("N356 audit receipt stored canonical regression")
    if csha_without(receipt) != EXPECTED_N356_RECEIPT_CANONICAL:
        raise ValueError("N356 audit receipt recomputed canonical regression")
    if receipt.get("status") != "PASS":
        raise ValueError("N356 hostile audit is not PASS")
    if receipt.get("review_id") != EXPECTED_N356_REVIEW:
        raise ValueError("N356 hostile-audit review regression")
    if receipt.get("audited_exact_head") != EXPECTED_N356_HEAD:
        raise ValueError("N356 hostile-audit exact-head regression")
    counts = receipt.get("consumed_counts", {})
    if counts.get("remaining_strata") != EXPECTED_REMAIN_STRATA:
        raise ValueError("N356 audited remaining-strata regression")
    if counts.get("remaining_terminals") != EXPECTED_REMAIN_TERMINALS:
        raise ValueError("N356 audited remaining-terminal regression")
    return receipt


def main() -> None:
    receipt = validate_n356_receipt()
    engine = load_engine()

    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        engine.main()
    lines = [line.strip() for line in captured.getvalue().splitlines() if line.strip()]
    if not lines:
        raise ValueError("N357 frozen engine produced no checkpoint output")
    checkpoint = json.loads(lines[-1])
    if checkpoint.get("verdict") != "PASS_N357_TRANSPORT_SUPPORT_CAPACITY_RESEARCH_CHECKPOINT":
        raise ValueError("N357 frozen-engine checkpoint verdict regression")
    if checkpoint.get("main_pruning_credit") is not False:
        raise ValueError("N357 checkpoint must not self-promote MAIN pruning credit")

    out = {
        "verdict": "PASS_N357_RETAINED_POST_N356_AUDIT_RESEARCH_CHECKPOINT",
        "n356_hostile_audit_status": "PASS",
        "n356_review_id": receipt["review_id"],
        "n356_audited_exact_head": receipt["audited_exact_head"],
        "n356_authoritative_remaining_strata": EXPECTED_REMAIN_STRATA,
        "n356_authoritative_remaining_terminals": EXPECTED_REMAIN_TERMINALS,
        "n357_main_pruning_credit": False,
        "n357_all178_srem_census_complete": False,
        "witness_stratum": checkpoint["witness_stratum"],
        "n356_exceptional": checkpoint["n356_exceptional"],
        "n357_exceptional": checkpoint["n357_exceptional"],
        "incremental_exceptional_reject": checkpoint["incremental_exceptional_reject"],
        "incremental_terminal_reject": checkpoint["incremental_terminal_reject"],
        "next_route": "BUILD_ALL178_SREM_SYMBOLIC_CENSUS",
    }
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
