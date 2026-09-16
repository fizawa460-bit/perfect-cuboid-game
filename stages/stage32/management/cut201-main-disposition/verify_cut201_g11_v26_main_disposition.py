#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
DISP = HERE / "CUT201-G11-V26-MAIN-DISPOSITION.json"
RECEIPT = HERE / "CUT201-V27-MAIN-CONSUMPTION.json"
DISP_CANON = "946ec777f824eaae75aa14d9c3ab5f348bfea38da020e72ede9750c914f86381"
RECEIPT_BLOB = "cdd766cae064430bb1aa901f1d023fcb48b39877"
RECEIPT_CANON = "aa9a40c0514412444a15db8a59d54de4866de39345ff4a0dbd531c14eaced9f6"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def locked_json(path: Path, expected_blob: str | None = None, expected_canon: str | None = None) -> dict:
    req(path.is_file(), f"missing {path}")
    if expected_blob is not None:
        req(blob(path) == expected_blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift {path}")
        req(canon(obj) == expected_canon, f"canonical drift {path}")
    return obj

def main() -> None:
    d = locked_json(DISP, expected_canon=DISP_CANON)
    r = locked_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON)
    req(d["schema"] == "STAGE32_MAIN_CUT201_G11_V26_DISPOSITION_V1", "historical disposition schema")
    req(d["producer"]["pr"] == 1806, "historical producer PR")
    req(d["producer"]["audited_exact_head"] == "8eed1449b325c3b990f90b61471bf7ecec0d89bc", "historical bounded head")
    req(d["producer"]["hostile_audit_review_id"] == 5204865930, "historical bounded audit")
    req(d["candidate"]["candidate_pruned_terminals"] == 25538, "historical candidate count")
    md = d["main_disposition"]
    req(md["credited_current_v26_incremental_rejected_terminal_count"] == 0, "historical disposition must remain zero-credit")
    req(md["main_subtraction_performed"] is False and md["main_authority_mutated"] is False, "historical disposition mutated")
    req(r["producer_audit"]["audited_exact_head"] == "9b485b4e643b7ed041629547fdb4a867e31c00cd", "adapter audited head")
    req(r["producer_audit"]["hostile_audit_review_id"] == 5206283218, "adapter audit review")
    req(r["accounting"]["credited_incremental_rejected_terminals"] == 18758, "consumed increment")
    req(r["accounting"]["double_charge"] is False, "double charge")
    req(r["accounting"]["main_consumer_authority_subtraction_performed"] is True, "MAIN subtraction missing")
    print("PASS: historical CUT201 G11 zero-credit disposition preserved; audited V26 adapter is consumed separately by MAIN V27")
if __name__ == "__main__":
    main()
