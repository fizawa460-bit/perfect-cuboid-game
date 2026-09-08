#!/usr/bin/env python3
"""Replay the Stage32EX5 EX5-01 exact receiver ledger.

This verifier proves coverage/status reconstruction only. It does not discharge
an open receiver, prove effectivity, qualify a route, or grant Stage32 MAIN
credit.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "ex5-01-exact-receiver-ledger.json"

CLOSED = {"g0-d002", "g0-d004", "g0-d006", "g1-d004", "g1-d006"}


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def expected_183() -> list[str]:
    return [f"g0-d{d:03d}" for d in range(2, 177, 2)] + [
        f"g1-d{d:03d}" for d in range(4, 193, 2)
    ]


def manifest_rows(manifest: dict) -> list[str]:
    out: list[str] = []
    for key in ("1", "2", "4", "8"):
        out.extend(manifest["m_class_rows"][key])
    return out


def main() -> None:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    stored = data.pop("canonical_sha256_without_this_field")
    require(csha(data) == stored, "artifact canonical SHA256 mismatch")
    require(stored == "d7ba8aac31b41941b71a77131af8a0e594eca0e2154fa612ea1dfb09ec23389e", "unexpected canonical SHA256")
    require(data["schema"] == "STAGE32EX5_EX5_01_EXACT_RECEIVER_LEDGER_V1", "wrong schema")
    require(data["leaf"] == "EX5-01", "wrong leaf")
    require(data["status"] == "EX5_01_RECEIVER_LEDGER_COMPLETE_UNAUDITED_RETAINED", "wrong status")

    locks = {x["id"]: x for x in data["source_locks"]}
    require(len(locks) == len(data["source_locks"]) == 7, "source lock ids are not unique/exact")
    for lock in data["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock: {lock['path']}")
        require(blob_sha1(path) == lock["blob_sha1"], f"source blob drift: {lock['path']}")
        if "canonical_sha256" in lock:
            obj = json.loads(path.read_text(encoding="utf-8"))
            expected = lock["canonical_sha256"]
            require(obj.get("canonical_sha256_without_this_field") == expected, f"stored canonical drift: {lock['path']}")
            stripped = dict(obj)
            stripped.pop("canonical_sha256_without_this_field", None)
            require(csha(stripped) == expected, f"recomputed canonical drift: {lock['path']}")

    ex5_00 = json.loads((ROOT / locks["SRC-EX5-00"]["path"]).read_text(encoding="utf-8"))
    require(ex5_00["unibranch_degree_population"]["frozen_genus_degree_row_count"] == 183, "EX5-00 183-row source drift")
    require(ex5_00["multibranch_population"]["silently_capped_by_unibranch_176_192_windows"] is False, "EX5-00 multibranch firewall drift")

    rf = json.loads((ROOT / locks["SRC-RF"]["path"]).read_text(encoding="utf-8"))
    require(rf["schema"] == "STAGE32_POST_B16_RESIDUAL_FEASIBILITY_STATE_V2_HOSTILE_AUDIT_PASS", "residual-feasibility authority drift")
    require(rf["hostile_audit"]["verdict"] == "PASS_RESIDUAL_FEASIBILITY_GATE_SCOPE_LOCKED", "residual-feasibility hostile audit not PASS")
    require(rf["static_analyzer"]["row_count"] == 183, "residual-feasibility row count drift")
    require(rf["coarse_partition"]["known_degree_le_6_rows_consumed"] == 5, "catalogue consumption count drift")
    require(rf["coarse_partition"]["residual_rows"] == 178, "residual row count drift")
    require(rf["credit"]["FULL_D176_D192_NUMERICAL_ORBIT_CENSUS"] is False, "full census unexpectedly complete")
    require(rf["credit"]["R29_LG2"] == "NOT_DISCHARGED", "R29-LG2 unexpectedly discharged")
    require(rf["credit"]["R29_LG2_EFF"] == "NOT_DISCHARGED", "R29-LG2-EFF unexpectedly discharged")
    require(rf["credit"]["R29_LG2_MB"] == "NOT_DISCHARGED", "R29-LG2-MB unexpectedly discharged")

    pre = json.loads((ROOT / locks["SRC-PRE"]["path"]).read_text(encoding="utf-8"))
    require(pre["source_provenance"]["audited_row_count"] == 183, "preflight audited row count drift")
    require(set(pre["source_provenance"]["excluded_degree_le_6_row_ids"]) == CLOSED, "preflight excluded row ids drift")
    require(pre["residual_row_count"] == 178, "preflight residual row count drift")
    require(pre["FULL_D176_D192_NUMERICAL_ORBIT_CENSUS"] is False, "preflight cannot claim full census")
    require(pre["R29_LG2"] == "NOT_DISCHARGED", "preflight cannot discharge R29-LG2")

    manifest = json.loads((ROOT / locks["SRC-MAN"]["path"]).read_text(encoding="utf-8"))
    all183 = expected_183()
    require(len(all183) == 183 and len(set(all183)) == 183, "internal 183-row construction failed")
    require(set(manifest["audited_source"]["exclude_degree_le_6"]) == CLOSED, "manifest excluded row ids drift")
    residual = manifest_rows(manifest)
    require(len(residual) == 178 and len(set(residual)) == 178, "manifest residual coverage is not exact 178")
    require(set(residual) == set(all183) - CLOSED, "manifest is not exact 183-minus-five residual population")
    require(manifest["m_class_counts"] == {"1": 23, "2": 23, "4": 44, "8": 88}, "m-class partition drift")

    prod = json.loads((ROOT / locks["SRC-PROD"]["path"]).read_text(encoding="utf-8"))
    require(prod["FULL_D176_D192_NUMERICAL_ORBIT_CENSUS"] is False, "current production state says full census complete")
    require(prod["R29_LG2"] == "NOT_DISCHARGED", "current production state says R29-LG2 discharged")

    main_state = json.loads((ROOT / locks["SRC-MAIN"]["path"]).read_text(encoding="utf-8"))
    target = main_state["fixed_target"]
    require(target["row_id"] == "g1-d186", "current representative row drift")
    require((target["O"], target["qprime"], target["Q"]) == (210, 4, 602), "current O/qprime/Q drift")
    require(target["surviving_residues_decimal"] == [73, 97, 235], "current survivors drift")

    rows = data["receiver_rows"]
    require(len(rows) == 185, "ledger must contain 183 numerical + EFF + MB rows")
    require(len({r["ledger_row_id"] for r in rows}) == 185, "ledger row ids are not unique")
    known_sources = set(locks)
    for row in rows:
        require(row["current_status"] in {"CLOSED", "OPEN", "UNKNOWN", "CONDITIONAL", "OUT_OF_SCOPE"}, f"bad row status: {row['ledger_row_id']}")
        require(set(row["evidence_locator_refs"]) <= known_sources, f"unknown evidence ref: {row['ledger_row_id']}")

    numerical = [r for r in rows if r["receiver_id"] == "R29-LG2"]
    require(len(numerical) == 183, "R29-LG2 numerical ledger must have 183 rows")
    num_by_id = {r["ledger_row_id"].split("::", 1)[1]: r for r in numerical}
    require(set(num_by_id) == set(all183), "numerical ledger does not cover exact frozen 183 rows")
    for pid in all183:
        row = num_by_id[pid]
        genus = int(pid[1])
        degree = int(pid.split("d", 1)[1])
        require(row["genus"] == genus and row["degree"] == degree, f"genus/degree drift: {pid}")
        require(row["branch_type"] == "UB", f"wrong branch type: {pid}")
        require(row["field_model_ref"] == "FM-GEO-S", f"wrong field/model ref: {pid}")
        if pid in CLOSED:
            require(row["current_status"] == "CLOSED", f"catalogue row not CLOSED: {pid}")
            require(row["numerical_effectivity_status_ref"] == "NES-CAT", f"catalogue semantic drift: {pid}")
            require(row["current_blocker_ref"] is None, f"closed catalogue row has blocker: {pid}")
        else:
            require(row["current_status"] == "OPEN", f"residual row must remain OPEN: {pid}")
            require(row["numerical_effectivity_status_ref"] == "NES-NUM-OPEN", f"residual semantic drift: {pid}")
            require(row["current_blocker_ref"] == "BLK-NUM", f"residual blocker drift: {pid}")
    cur = num_by_id["g1-d186"]
    require(cur["v6_o210_q602_relation_ref"] == "VREL-CUR", "current representative scope firewall lost")
    require(cur["representative_context"] == {"picard_class": "V6", "O": 210, "qprime": 4, "Q": 602, "surviving_residues": [73, 97, 235]}, "current representative context drift")
    for pid, row in num_by_id.items():
        if pid != "g1-d186" and pid not in CLOSED:
            require(row["v6_o210_q602_relation_ref"] == "VREL-NOTCUR", f"V6/O210/Q602 leaked to another row: {pid}")

    eff = [r for r in rows if r["receiver_id"] == "R29-LG2-EFF"]
    mb = [r for r in rows if r["receiver_id"] == "R29-LG2-MB"]
    require(len(eff) == len(mb) == 1, "EFF/MB meta receiver coverage mismatch")
    require(eff[0]["current_status"] == "OPEN" and eff[0]["current_blocker_ref"] == "BLK-EFF", "effectivity receiver status drift")
    require(mb[0]["current_status"] == "OPEN" and mb[0]["current_blocker_ref"] == "BLK-MB", "multibranch receiver status drift")
    require(mb[0]["degree"] == "NO_UNIBRANCH_CAP_INHERITED", "multibranch cap firewall lost")

    checksum = hashlib.sha256(
        json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    cov = data["coverage_contract"]
    require(checksum == cov["coverage_checksum_sha256"] == "3a700ed40b5d0e6bf212f569ed85279a15ac90bb8a87a96e61f01729ffa0ca95", "coverage checksum mismatch")
    counts = Counter(r["current_status"] for r in rows)
    expected_counts = {"CLOSED": 5, "OPEN": 180, "UNKNOWN": 0, "CONDITIONAL": 0, "OUT_OF_SCOPE": 0}
    require({k: counts.get(k, 0) for k in expected_counts} == expected_counts, "ledger status counts mismatch")
    require(cov["ledger_row_count"] == 185 and cov["unresolved_row_count"] == 180, "coverage count drift")
    require(cov["all_frozen_receiver_classes_represented"] is True, "receiver coverage not certified")
    require(cov["bounded_package_exhaustion_authorized"] is False, "EX5-01 cannot authorize package exhaustion")

    for key, value in data["firewalls"].items():
        require(value is False, f"firewall must remain false: {key}")
    ex5 = data["ex5_contract"]
    require(ex5["receiver_ledger_complete"] is True, "EX5-01 ledger not complete")
    require(ex5["receiver_ledger_coverage_certified"] is True, "EX5-01 coverage not certified")
    require(ex5["next_leaf"] == "EX5-02_CURRENT_COVERAGE_AND_DEPENDENCY_GRAPH", "wrong next leaf")
    require(ex5["arsenal_or_existing_solution_discovery_performed"] is False, "Arsenal discovery must remain deferred to EX5-04")
    require(ex5["route_credit_granted"] is False, "EX5-01 grants no route credit")

    print("PASS: Stage32EX5 EX5-01 exact receiver ledger (185 rows = 5 CLOSED + 180 OPEN)")


if __name__ == "__main__":
    main()
