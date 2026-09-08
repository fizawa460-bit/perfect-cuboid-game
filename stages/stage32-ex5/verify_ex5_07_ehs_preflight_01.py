#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "ex5-07-ehs-preflight-01.json"
EXPECTED_CANON = "fb5b922febeef3b2b3259fcf32a9f03186f3dc78600dcef79c89ae4a6127c927"
ORDER = ["exact_complete_linear_system_dimension_for_complete_block","exact_genus_defect_for_target_geometric_genus","source_valid_codimension_bound_for_every_allowed_singularity_type","population_complete_allowed_singularity_inventory","strict_codimension_greater_than_dimension_implication"]

def req(c,m):
    if not c: raise SystemExit(f"FAIL: {m}")
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def bsha(p):
    d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()

def main():
    d=json.loads(ART.read_text())
    stored=d.pop("canonical_sha256_without_this_field")
    req(stored==EXPECTED_CANON and csha(d)==stored,"canonical drift")
    req(d["status"]=="ROUTE_BLOCKED_BY_NAMED_MISSING_INPUT","status drift")
    req(d["preflight_contract"]["required_field_order"]==ORDER,"field order drift")
    req(d["preflight_contract"]["repository_search_miss_used_as_absence_proof"] is False,"search miss cannot prove absence")
    for lock in d["source_locks"]:
        p=ROOT/lock["path"]; req(p.is_file(),f"missing {lock['path']}"); req(bsha(p)==lock["blob_sha1"],f"blob drift {lock['path']}")
        if "canonical_sha256" in lock:
            o=json.loads(p.read_text()); s=o.pop("canonical_sha256_without_this_field"); req(s==lock["canonical_sha256"] and csha(o)==s,f"canonical source drift {lock['path']}")
    ledger=json.loads((HERE/"ex5-01-exact-receiver-ledger.json").read_text())
    rows={r["ledger_row_id"]:r for r in ledger["receiver_rows"]}
    eff=rows["R29-LG2-EFF::ALL_NUMERICAL_SURVIVORS"]
    req(eff["field_model_ref"]=="FM-GEO-S","EFF field model drift")
    req(eff["current_status"]=="OPEN","EFF must remain open")
    card=(ROOT/"docs/arsenal/cards/provisional/S36-PW01.md").read_text()
    for marker in ["Maturity | **PROVISIONAL**","ELEMENTARY_ABELIAN_COVER_CHARACTER_QUOTIENT_GENUS_INVENTORY","DO_NOT_USE_FOR","receiver closure"]:
        req(marker in card,f"S36-PW01 scope marker missing: {marker}")
    fr=d["field_results"]
    req(fr[0]["field"]==ORDER[0] and fr[0]["result"]=="UNSATISFIED","first field must fail")
    req(all(x["result"]=="NOT_REACHED_AFTER_FIRST_FAILURE" for x in fr[1:]),"preflight did not stop after first failure")
    rd=d["route_decision"]
    req(rd["blocker_code"]=="EHS_MISSING_SOURCE_BOUND_EXACT_LINEAR_SYSTEM_DIMENSION_ADAPTER","blocker drift")
    req(rd["next_route_id"]=="EX5-10_RESIDUAL_PACKAGE_STATUS_OR_RESERVE_ROUTE_REVIEW","next route drift")
    req(rd["route_failure_is_stage_exhaustion"] is False,"route block cannot exhaust stage")
    req(rd["global_nonexistence_of_required_inputs_claimed"] is False,"must not claim required inputs globally nonexistent")
    req(d["credit"]["ehs_preflight_complete"] is True,"EHS preflight completion missing")
    for k in ["nontrivial_receiver_effect_obtained","qualified_independent_route_established","receiver_credit","theorem_credit","stage32_main_credit"]: req(d["credit"][k] is False,f"credit pregranted {k}")
    for k,v in d["firewalls"].items(): req(v is False,f"firewall {k} must remain false")
    print("PASS: Stage32EX5 EHS-PREFLIGHT-01 blocked at missing source-bound exact linear-system dimension adapter; reserve review next")
if __name__=="__main__": main()
