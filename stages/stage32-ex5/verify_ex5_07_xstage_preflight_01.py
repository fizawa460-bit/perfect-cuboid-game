#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "ex5-07-xstage-preflight-01.json"
EXPECTED_CANON = "304a15d589f80b2bb20b243858ba32f404bbd74fc27e6388dc06b97b241c49c1"
ORDER = ["nonempty_exact_stage32_MB_subset_T","exact_map_T_to_source_branch_B","exact_receiver_condition_K_on_T","object_model_field_compatibility","branch_and_multiplicity_semantics","quantifier_compatibility_without_Q_narrowing","zero_pole_infinity_degenerate_exhaustiveness"]

def req(c,m):
    if not c: raise SystemExit(f"FAIL: {m}")
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def bsha(p):
    d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()

def main():
    d=json.loads(ART.read_text())
    stored=d.pop("canonical_sha256_without_this_field")
    req(stored==EXPECTED_CANON and csha(d)==stored,"canonical drift")
    req(d["status"]=="ROUTE_BLOCKED_BY_NAMED_MISSING_ADAPTER","status drift")
    req(d["preflight_contract"]["required_field_order"]==ORDER,"field order drift")
    for lock in d["source_locks"]:
        p=ROOT/lock["path"]; req(p.is_file(),f"missing {lock['path']}"); req(bsha(p)==lock["blob_sha1"],f"blob drift {lock['path']}")
        if "canonical_sha256" in lock:
            o=json.loads(p.read_text()); s=o.pop("canonical_sha256_without_this_field"); req(s==lock["canonical_sha256"] and csha(o)==s,f"canonical source drift {lock['path']}")
    ledger=json.loads((HERE/"ex5-01-exact-receiver-ledger.json").read_text())
    rows={r["ledger_row_id"]:r for r in ledger["receiver_rows"]}
    mb=rows["R29-LG2-MB::MULTIBRANCH_AT_NODE"]
    req(mb["field_model_ref"]=="FM-GEO-S-MB","MB field model drift")
    req(mb["current_status"]=="OPEN","MB must remain open")
    card=(ROOT/"docs/arsenal/cards/formal/S34-W03.md").read_text()
    req("B(Q) intersect K(Q) = empty" in card,"S34-W03 rational-point marker missing")
    fr=d["field_results"]
    req(fr[0]["field"]==ORDER[0] and fr[0]["result"]=="UNSATISFIED","first field must fail")
    req(all(x["result"]=="NOT_REACHED_AFTER_FIRST_FAILURE" for x in fr[1:]),"preflight did not stop after first failure")
    rd=d["route_decision"]
    req(rd["blocker_code"]=="XSTAGE_MISSING_EXACT_NONEMPTY_MB_SUBSET_ADAPTER","blocker drift")
    req(rd["next_route_id"]=="EX5R-EFC-001","next route drift")
    req(rd["route_failure_is_stage_exhaustion"] is False,"route block cannot exhaust stage")
    req(d["credit"]["primary_microdiagnostic_complete"] is True,"microdiagnostic completion missing")
    for k in ["nontrivial_receiver_effect_obtained","qualified_independent_route_established","receiver_credit","theorem_credit","stage32_main_credit"]: req(d["credit"][k] is False,f"credit pregranted {k}")
    for k,v in d["firewalls"].items(): req(v is False,f"firewall {k} must remain false")
    print("PASS: Stage32EX5 XSTAGE-PREFLIGHT-01 blocked at missing exact nonempty MB subset T; next EFC")
if __name__=="__main__": main()
