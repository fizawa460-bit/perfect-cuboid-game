#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
ART=HERE/"ex5-11-terminal-route-decision-certificate.json"
EXPECTED_CANON="b0d0a81cf79448703d5e10d9280e6e19ac5f4f32dc31061c9c836d323bcebba7"
EXPECTED_IDS={"EX5R-XSTAGE-001","EX5R-EFC-001","EX5R-EHS-001","EX5R-LGS-001","EX5R-MOD-001","EX5R-GAL-001","EX5R-ENUM-001"}
ALLOWED_OUTCOMES={"QUALIFIED_INDEPENDENT_STAGE32_ROUTE_ESTABLISHED","FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE"}

def req(c,m):
    if not c: raise SystemExit(f"FAIL: {m}")
def csha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def bsha(p):
    d=p.read_bytes()
    return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()

def main():
    d=json.loads(ART.read_text())
    stored=d.pop("canonical_sha256_without_this_field")
    req(stored==EXPECTED_CANON and csha(d)==stored,"certificate canonical drift")
    req(d["schema"]=="STAGE32EX5_EX5_11_TERMINAL_ROUTE_DECISION_CERTIFICATE_V1","schema drift")
    req(d["status"]=="AUDIT_READY_EX5_ROUTE_DECISION_CLOSURE_CANDIDATE_UNAUDITED","status drift")

    locks={x["id"]:x for x in d["source_locks"]}
    req(set(locks)=={"SRC-EX5-01","SRC-EX5-03","SRC-EX5-10","SRC-ROADMAP","SRC-AUDIT-CONTRACT"},"source lock set drift")
    for lock in d["source_locks"]:
        p=ROOT/lock["path"]
        req(p.is_file(),f"missing source: {lock['path']}")
        req(bsha(p)==lock["blob_sha1"],f"source blob drift: {lock['path']}")
        if "canonical_sha256" in lock:
            o=json.loads(p.read_text())
            req(o.get("canonical_sha256_without_this_field")==lock["canonical_sha256"],f"stored source canonical drift: {lock['path']}")

    ledger=json.loads((HERE/"ex5-01-exact-receiver-ledger.json").read_text())
    rows=ledger["receiver_rows"]
    req(len(rows)==185 and len({r["ledger_row_id"] for r in rows})==185,"receiver ledger coverage drift")
    counts=Counter(r["current_status"] for r in rows)
    expected={"CLOSED":5,"OPEN":180,"UNKNOWN":0,"CONDITIONAL":0,"OUT_OF_SCOPE":0}
    req({k:counts.get(k,0) for k in expected}==expected,"receiver status count drift")
    req(ledger["coverage_contract"]["coverage_checksum_sha256"]==d["receiver_package"]["coverage_checksum"],"coverage checksum lock drift")
    req(d["receiver_package"]["ledger_row_count"]==185 and d["receiver_package"]["ledger_status_counts"]==expected,"certificate receiver counts drift")
    req(d["receiver_package"]["receiver_ids"]==["R29-LG2","R29-LG2-EFF","R29-LG2-MB"],"receiver IDs drift")
    req(d["receiver_package"]["receiver_ledger_frozen"] is True and d["receiver_package"]["receiver_coverage_certified"] is True,"receiver freeze/coverage missing")
    req(d["receiver_package"]["open_receivers_closed_by_this_certificate"] is False,"terminal certificate cannot close receiver rows")

    ex10=json.loads((HERE/"ex5-10-bounded-breadth-exhaustion-ledger.json").read_text())
    ex10recs={r["route_id"]:r for r in ex10["terminal_package_records"]}
    certrecs={r["route_id"]:r for r in d["terminal_records"]}
    req(set(ex10recs)==set(certrecs)==EXPECTED_IDS,"terminal route coverage drift")
    req(ex10["package_summary"]["all_frozen_candidates_terminally_classified"] is True,"EX5-10 classification incomplete")
    req(ex10["package_summary"]["qualified_count"]==0,"qualified route unexpectedly present")
    for rid in EXPECTED_IDS:
        if rid in {"EX5R-XSTAGE-001","EX5R-EFC-001","EX5R-EHS-001","EX5R-LGS-001","EX5R-MOD-001"}:
            req(certrecs[rid]["terminal_status"]=="BLOCKED","blocked route status drift")
            req(certrecs[rid]["blocker_code"]==ex10recs[rid]["blocker_code"],f"blocker drift {rid}")
        elif rid=="EX5R-GAL-001":
            req(certrecs[rid]["terminal_status"]=="INAPPLICABLE","GAL status drift")
        else:
            req(certrecs[rid]["terminal_status"]=="DUPLICATE","ENUM status drift")

    cp=d["candidate_package"]
    req(cp["clean_room_route_family_count"]==7 and cp["candidate_universe_frozen_before_asset_lookup"] is True,"candidate freeze drift")
    req(cp["candidate_universe_broadened_after_freeze"] is False,"candidate universe silently broadened")
    req(cp["terminal_status_counts"]=={"BLOCKED":5,"INAPPLICABLE":1,"DUPLICATE":1,"QUALIFIED":0},"terminal status counts drift")
    req(cp["all_frozen_candidates_terminally_classified"] is True,"candidate classification incomplete")
    req(cp["qualified_independent_route_established"] is False and cp["nontrivial_receiver_effect_obtained"] is False,"positive route credit pregranted")

    td=d["terminal_decision"]
    req(td["selected_outcome"] in ALLOWED_OUTCOMES,"unknown terminal outcome")
    req(td["selected_outcome"]=="FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE","wrong selected outcome")
    req(td["selected_outcome_supported_as_audit_ready_candidate"] is True,"audit-ready candidate not asserted")
    req(td["bounded_to_explicitly_frozen_EX5_package"] is True,"bounded scope lost")
    req(td["global_no_route_theorem"] is False,"global no-route theorem forbidden")
    req(td["stage32_full_target_closure"] is False and td["stage32_main_promotion"] is False,"Stage32 credit leakage")
    req(td["hostile_audit_required_for_EX5_route_decision_closure"] is True,"audit gate lost")
    req(td["hostile_audit_pass_present"] is False and td["EX5_route_decision_closure"] is False,"unaudited candidate promoted to closure")
    req(td["next_leaf"]=="EX5-12_HOSTILE_AUDIT_AND_STAGE32_PROMOTION_BOUNDARY","next leaf drift")

    audit=d["audit_candidate"]
    req(audit["candidate_pr"]==1710 and audit["exact_head"] is None,"audit target/head drift")
    req(audit["audit_status"]=="AUDIT_READY_UNAUDITED","audit status drift")
    req(audit["strongest_pre_audit_credit_ceiling"]=="AUDIT_READY_EX5_ROUTE_DECISION_CLOSURE / FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE","credit ceiling drift")
    req(audit["pass_auto_merges"] is False and audit["pass_auto_promotes_to_stage32_main"] is False,"audit firewall lost")

    roadmap=(HERE/"stage32-ex5.md").read_text()
    for marker in ["FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE","EX5_ROUTE_DECISION_CLOSURE","not a global no-route theorem"]:
        req(marker in roadmap,f"roadmap terminal marker missing: {marker}")
    audit_text=(HERE/"AUDIT-CONTRACT.md").read_text()
    req("AUDIT_READY_EX5_ROUTE_DECISION_CLOSURE / <terminal outcome>" in audit_text,"audit-ready credit ceiling marker missing")
    req("only after exact-head hostile-audit PASS" in audit_text,"hostile audit gate marker missing")

    for k,v in d["firewalls"].items():
        req(v is False,f"firewall must remain false: {k}")
    print("PASS: Stage32EX5 EX5-11 bounded-exhaustion terminal candidate is audit-ready but unaudited; no Stage32 MAIN credit")

if __name__=="__main__":
    main()
