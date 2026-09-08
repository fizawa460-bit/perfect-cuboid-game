#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
ART=HERE/"ex5-10-bounded-breadth-exhaustion-ledger.json"
EXPECTED_CANON="82a5ae06c29e76b40c09a568971b64edf637584785e817ac7d1492cfc68160e1"
EXPECTED_IDS={"EX5R-XSTAGE-001","EX5R-EFC-001","EX5R-EHS-001","EX5R-LGS-001","EX5R-MOD-001","EX5R-GAL-001","EX5R-ENUM-001"}

def req(c,m):
    if not c: raise SystemExit(f"FAIL: {m}")
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def bsha(p):
    d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()

def main():
    d=json.loads(ART.read_text())
    stored=d.pop("canonical_sha256_without_this_field")
    req(stored==EXPECTED_CANON and csha(d)==stored,"canonical drift")
    req(d["status"]=="FROZEN_BREADTH_PACKAGE_CLASSIFIED_WITHOUT_QUALIFIED_ROUTE_UNAUDITED_RETAINED","status drift")
    for lock in d["source_locks"]:
        p=ROOT/lock["path"]; req(p.is_file(),f"missing {lock['path']}"); req(bsha(p)==lock["blob_sha1"],f"blob drift {lock['path']}")
        if "canonical_sha256" in lock:
            o=json.loads(p.read_text()); s=o.pop("canonical_sha256_without_this_field"); req(s==lock["canonical_sha256"] and csha(o)==s,f"canonical source drift {lock['path']}")
    recs=d["terminal_package_records"]
    req(len(recs)==7,"must classify seven frozen routes")
    req({r["route_id"] for r in recs}==EXPECTED_IDS,"frozen route coverage drift")
    req(all(r["qualified"] is False for r in recs),"qualified route unexpectedly present")
    counts=Counter(r["package_status"] for r in recs)
    req(sum(v for k,v in counts.items() if k.startswith("BLOCKED_BY_"))==5,"blocked count drift")
    req(counts["INAPPLICABLE_WITH_SEMANTIC_MISMATCH"]==1,"inapplicable count drift")
    req(counts["DUPLICATE_WITH_EXACT_PARENT"]==1,"duplicate count drift")
    byid={r["route_id"]:r for r in recs}
    req(byid["EX5R-LGS-001"]["blocker_code"]=="LGS_MISSING_POPULATION_WIDE_GLOBAL_TO_LOCAL_DEFECT_ADAPTER","LGS blocker drift")
    req(byid["EX5R-MOD-001"]["blocker_code"]=="MOD_MISSING_EXACT_178_ROW_MODULAR_OBJECT_PREIMAGE_ADAPTER","MOD blocker drift")
    req("S32-PW01" in byid["EX5R-ENUM-001"]["duplicate_parent"],"ENUM parent drift")
    s34=(ROOT/"docs/arsenal/cards/formal/S34-W03.md").read_text()
    req("exact source/receiver contract" in s34 and "receiver branch closed = allowed" in s34,"S34-W03 scope marker missing")
    s30=(ROOT/"docs/arsenal/cards/formal/S30-W01.md").read_text()
    req("source/common-model anchor" in s30 and "adapter closure => endpoint/route closure" in s30,"S30-W01 scope marker missing")
    pc=d["frozen_package_contract"]
    req(pc["clean_room_route_family_count"]==7 and pc["candidate_universe_broadened"] is False,"frozen package drift")
    req(pc["heavy_compute_used"] is False,"heavy compute unexpectedly used")
    req(pc["bounded_exhaustion_is_global_no_route_theorem"] is False,"global no-route firewall lost")
    ps=d["package_summary"]
    req(ps["record_count"]==7 and ps["qualified_count"]==0 and ps["blocked_count"]==5 and ps["inapplicable_count"]==1 and ps["duplicate_count"]==1,"summary count drift")
    req(ps["all_frozen_candidates_terminally_classified"] is True,"coverage not complete")
    req(ps["frozen_breadth_package_exhausted_without_qualified_route"] is True,"bounded exhaustion missing")
    req(ps["terminal_certificate_assembled"] is False and ps["audit_ready_EX5_route_decision_closure"] is False and ps["EX5_route_decision_closure"] is False,"terminal credit pregranted")
    req(ps["next_leaf"]=="EX5-11_TERMINAL_ROUTE_DECISION_CERTIFICATE","next leaf drift")
    for k in ["nontrivial_receiver_effect_obtained","qualified_independent_route_established","receiver_credit","theorem_credit","stage32_main_credit"]: req(d["credit"][k] is False,f"credit pregranted {k}")
    for k,v in d["firewalls"].items(): req(v is False,f"firewall {k} must remain false")
    print("PASS: Stage32EX5 EX5-10 frozen seven-route package fully classified; bounded exhaustion only, terminal certificate next")
if __name__=="__main__": main()
