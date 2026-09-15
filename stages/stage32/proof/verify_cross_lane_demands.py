#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, runpy
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REGISTRY = HERE / "CROSS-LANE-DEMANDS.json"
MONITOR = HERE / "ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
CONSUMPTION_VERIFIER = ROOT / "stages/stage32/management/cut201-main-disposition/verify_cut201_v26_main_consumption_preflight.py"
REGISTRY_BLOB = "e14bea1a62ec287710064a96f80abe57f8b0c3f4"
REGISTRY_CANON = "9a30646b5567adb30f0192b43f89a8d8a01d1464199b2f0a0d19e1138a7d9c74"
MONITOR_BLOB = "53f286f78574cfad59fc397a9d3268d345331594"
MONITOR_CANON = "48a0f92b1325e80507594c25e8d78dd28a0f0bf5d624bc1afd6d9d43be56e32c"
DEMAND_ID = "S32.DEMAND.CUT201.CUT.MAIN.V26_CURRENT_AUTHORITY_ADAPTER.V1"

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
    reg = locked_json(REGISTRY, REGISTRY_BLOB, REGISTRY_CANON)
    mon = locked_json(MONITOR, MONITOR_BLOB, MONITOR_CANON)
    req(reg["schema"] == "STAGE32_CROSS_LANE_DEMANDS_V5_CUT201_V27_CONSUMED", "registry schema")
    byid = {d["demand_id"]: d for d in reg["demands"]}
    req(byid["S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"]["status"] == "SATISFIED", "CUT192 demand")
    req(byid["S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1"]["status"] == "SATISFIED", "HPADJ demand")
    req(byid["S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1"]["status"] == "OBSOLETE", "N398 demand")
    req(byid["S32.DEMAND.N400.178.MAIN.COMPACT_CONSUMPTION.V1"]["status"] == "SATISFIED", "N400 demand")
    c = byid[DEMAND_ID]
    req(c["status"] == "SATISFIED", "CUT201 demand")
    sp = c["source_population_semantics"]
    req(sp["exact_incremental_rejected_terminals"] == 18758 and sp["exact_incremental_blocks"] == 166, "CUT201 increment")
    req(sp["certlift03_overlap_terminals"] == 6780 and sp["other_consumed_route_overlap_terminals"] == 0 and sp["double_charge"] is False, "CUT201 overlap")
    req(sp["producer_lane_main_authority_subtraction_performed"] is False, "producer subtraction")
    open_ids = [d["demand_id"] for d in reg["demands"] if d["status"] == "OPEN"]
    req(open_ids == [], "unexpected OPEN demands")
    req(mon["schema"] == "STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V4_CUT201_V27_CONSUMED", "monitor schema")
    lanes = {x["lane"]: x for x in mon["active_specialists"]}
    req(set(lanes) == {"32-01-178","EX5","CUT","MB"}, "monitor coverage")
    req(lanes["CUT"]["pending_main_handoff_ids"] == [], "CUT pending handoff not cleared")
    req(mon["credit_firewall"]["duplicate_pruning_credit_authorized"] is False and mon["credit_firewall"]["merge_authorized"] is False, "monitor firewall")
    runpy.run_path(str(CONSUMPTION_VERIFIER), run_name="__main__")
    print("PASS: Stage32 cross-lane demand coordination verified after CUT201 V27 MAIN consumption")
if __name__ == "__main__":
    main()
