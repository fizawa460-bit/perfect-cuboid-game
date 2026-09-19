#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ADAPTER = HERE / "V43-SOURCE-KEY-ACCOUNTING-E32.json"
ADAPTER_BLOB = "dd44cd15b01237bbf89de134e3195f7a69f0191d"
CHECKPOINT = HERE / "ZERO-CENTER-E32-FULL-X4-ROW-CHECKPOINT.json"
CHECKPOINT_BLOB = "18ddff73af80d750f4087008dd1e3941b2bee989"

MAIN_HEAD = "83ae3f66cfcbdfaaaebf149bea078d1b0ff11c49"
V42_RECEIPT_BLOB = "3072d84981eaec239ba55a5e5e25a3481d37406b"
ROW_WORKER_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
ROW_CERT_CANON = "ba356db05dfb3699c7a13b59698d30cad9599a32e3bf409f6e6d5de45c42ddca"
CURRENT_AUTH = 157570677819451133507
ROW_FLOOR = 10295799819832396278


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main-state", type=Path, required=True)
    ap.add_argument("--v42-receipt", type=Path, required=True)
    ap.add_argument("--row-worker", type=Path, required=True)
    ap.add_argument("--row-cert", type=Path, required=True)
    args = ap.parse_args()

    req(ADAPTER.is_file() and blob(ADAPTER) == ADAPTER_BLOB, "accounting adapter drift")
    req(CHECKPOINT.is_file() and blob(CHECKPOINT) == CHECKPOINT_BLOB, "e32 checkpoint drift")
    req(args.v42_receipt.is_file() and blob(args.v42_receipt) == V42_RECEIPT_BLOB, "V42 receipt drift")
    req(args.row_worker.is_file() and blob(args.row_worker) == ROW_WORKER_BLOB, "HPADJ21 row worker drift")

    a = json.loads(ADAPTER.read_text())
    cp = json.loads(CHECKPOINT.read_text())
    state = json.loads(args.main_state.read_text())
    v42 = json.loads(args.v42_receipt.read_text())
    row = json.loads(args.row_cert.read_text())

    req(a["schema"] == "STAGE32_32_01_178_V43_SOURCE_KEY_ACCOUNTING_E32_V1", "adapter schema")
    req(a["status"] == "EXACT_NO_OVERLAP__ZERO_CURRENT_MAIN_CREDIT__PIVOT_REQUIRED", "adapter status")
    req(a["producer"]["audited_exact_head"] == "8a8efc48866f8008d253c21ebd272e698d18dc44", "producer audited head")
    req(a["producer"]["hostile_audit_status"] == "PASS", "producer audit status")
    req(a["producer"]["route_row_id"] == "g1-d192" and int(a["producer"]["route_e"]) == 32, "producer source key")
    req(a["producer"]["route_exact_weighted_mass"] == "41498727425", "producer route mass")

    req(cp["target"]["row_id"] == "g1-d192" and int(cp["target"]["e"]) == 32, "checkpoint source key")
    req(cp["result"]["complete_e32_x4_exact_weighted_mass"] == "41498727425", "checkpoint mass")
    req(cp["firewalls"]["main_credit_changed"] is False, "checkpoint MAIN credit firewall")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V43_HPADJ21_FULL178_BOUND_AUDIT_SYNCED", "current MAIN schema")
    req(state["current_exact_frontier"]["authoritative_remaining_terminals"] == CURRENT_AUTH, "current MAIN authority")
    req(state["current_exact_frontier"]["live_ex5_hpadj21_main_credit_consumed"] is True, "HPADJ21 not current authority")
    req(state["current_exact_frontier"]["full178_numerical_census_complete"] is False, "FULL178 overclaim")

    req(v42["schema"] == "STAGE32_MAIN_GRF04_V42_HPADJ21_FULL178_MAIN_BOUND_REPLACEMENT_V1", "V42 receipt schema")
    req(v42["replacement"]["authoritative_remaining_terminals"] == CURRENT_AUTH, "V42 bound")
    req(v42["consumed_handoff"]["full178_rows"] == 178, "HPADJ21 row coverage")
    req(v42["replacement"]["additive_subtraction_performed"] is False, "V42 additive firewall")

    req(row["schema"] == "STAGE32EX5_HPADJ21_FULL_QA_ROW_CERT_V1", "row certificate schema")
    req(row.get("canonical_sha256_without_this_field") == ROW_CERT_CANON, "row certificate canonical identity")
    req(canonical(row) == ROW_CERT_CANON, "row certificate canonical replay")
    req(int(row["row"]["index"]) == 22 and row["row"]["row_id"] == "g1-d192", "row identity")
    req(int(row["row"]["g"]) == 1 and int(row["row"]["d"]) == 192, "row g/d")
    req(int(row["totals"]["hpadj21_cellwise_floor_sum"]) == ROW_FLOOR, "row HPADJ21 floor")
    req(len(row["cell_records"]) == 8, "row cell count")

    src = args.row_worker.read_text()
    normalized = re.sub(r"\s+", "", src)
    req("lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))" in normalized, "HPADJ21 lower formula drift")
    g, d, route_e = 1, 192, 32
    current_constant_lower = d - 4 * g + 4
    req(current_constant_lower == 192, "current row lower arithmetic")
    req(route_e < current_constant_lower, "audited route unexpectedly intersects current e domain")

    acct = a["source_key_accounting"]
    req(acct["current_row_constant_lower_value"] == current_constant_lower, "adapter lower value")
    req(acct["route_e_below_current_domain"] is True, "adapter domain relation")
    req(acct["exact_current_source_key_overlap_count"] == 0, "adapter overlap count")
    req(acct["overlap_semantics"] == "DISJOINT_BY_CANONICAL_E_COORDINATE", "adapter overlap semantics")
    req(acct["current_main_incremental_rejected_terminals_credit"] == "0", "adapter credit")
    req(acct["additive_subtraction_authorized"] is False, "adapter additive firewall")
    req(acct["main_numeric_bound_replacement_authorized"] is False, "adapter replacement firewall")
    req(acct["double_charge"] is False, "adapter double charge")

    for rec in row["cell_records"]:
        req(int(rec["post_mass"]) <= int(rec["pre_mass"]), "row mass direction")
        req(int(rec["hpadj21_floor"]) <= int(rec["post_mass"]), "row floor exceeds post mass")

    for k in ("main_credit_changed","theorem_credit_changed","endpoint_credit_changed","full178_complete","stage32_closed","merge"):
        req(a["firewalls"][k] is False, f"adapter firewall {k}")

    print("V43_SOURCE_KEY_ACCOUNTING_E32_SUMMARY=" + json.dumps({
        "current_main_head": MAIN_HEAD,
        "row_id": "g1-d192",
        "current_hpadj21_e_lower": current_constant_lower,
        "audited_route_e": route_e,
        "exact_current_overlap": 0,
        "current_main_credit": 0,
        "pivot": a["pivot"]["required_research"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
