#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
RECEIPT=HERE/"V48-178-SUPPORT-QBC-AUTHORITY-SYNC.json"
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
RECEIPT_BLOB="2733e5519629e6365558bc1b4bfbc6305e0b5533"
RECEIPT_CANON="d106029369dd5a029cd7a56e1c7d80fdd29f8471454fd2ed6c638af2b70288b1"
OLD=128645575147764659235
NEW=128470212118313474449
TIGHT=175363029451184786
AUDITED_HEAD="fb81be66f260879eec79e55be140857b5fc32bbc"

LOCKS={
"stages/stage32/32-01-178/fibration-nef/local-support-qbc/GENERATION4-COMPLETE.json":"a917f6a98e8f4db57d0ada5193fe263f52162732",
"stages/stage32/32-01-178/fibration-nef/run_v47_support_qbc_intersection_unit.py":"af3026f5d7608181845e2ee0f9e0ab91feee60d1",
"stages/stage32/32-01-178/fibration-nef/aggregate_v47_support_qbc_intersection.py":"e56a6b1796c067fde61e34f695df410dfa50aa43",
"stages/stage32/32-01-178/fibration-nef/V47-SUPPORT-QBC-INTERSECTION-PREFLIGHT.json":"1f3abf84f1ff5f9eb4fb319a06e988a22132c26b",
"stages/stage32/32-01-178/fibration-nef/V47-SUPPORT-QBC-INTERSECTION-RUNKEY.json":"46cf52224e84ebd58ea5a17390834616ec266778",
".github/workflows/stage32-01-178-v47-support-qbc-intersection.yml":"1e7683453193cbd46d605b60afdf4e532d579e1a",
}
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--lane178-root",type=Path);args=ap.parse_args()
    req(RECEIPT.is_file() and blob(RECEIPT)==RECEIPT_BLOB,"receipt blob")
    r=json.loads(RECEIPT.read_text())
    req(r["canonical_sha256_without_this_field"]==RECEIPT_CANON and canon(r)==RECEIPT_CANON,"receipt canonical")
    req(r["source"]["audited_exact_head"]==AUDITED_HEAD and r["source"]["hostile_audit_status"]=="PASS","audit binding")
    a=r["authority"]
    req(int(a["predecessor_v47_upper_bound"])==OLD and int(a["v48_same_population_replacement_upper_bound"])==NEW,"bounds")
    req(int(a["exact_incremental_tightening_vs_v47"])==TIGHT and OLD-NEW==TIGHT,"tightening")
    req(a["replacement_formula"]=="V47_total - covered_V47 + covered_V47_support_qBC","replacement formula")
    req(a["additive_subtraction"] is False and a["statistical_independence"] is False and a["no_double_charge"] is True,"accounting")
    req(r["coverage"]["completed_coordinates"]==r["coverage"]["expected_coordinates"]==384 and r["coverage"]["gaps"]==0 and r["coverage"]["overlaps"]==0,"coverage")
    if args.lane178_root:
        for rel,sha in LOCKS.items():
            p=args.lane178_root/rel;req(p.is_file() and blob(p)==sha,"178 source drift "+rel)
    st=json.loads(STATE.read_text())
    req(canon(st)==st["canonical_sha256_without_this_field"],"MAIN state canonical")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V48_178_SUPPORT_QBC_AUDIT_SYNCED","MAIN schema")
    f=st["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"]==NEW and f["v48_exact_tightening_vs_v47"]==TIGHT,"MAIN authority")
    req(f["full178_numerical_census_complete"] is True and f["v48_178_support_qbc_main_numeric_bound_replacement_consumed"] is True,"MAIN consumption")
    for k in ("effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(st["firewalls"][k] is False,"firewall "+k)
    print("PASS: Stage32 MAIN V48 consumes hostile-audited 178 support-qBC as same-population exact bound replacement")
if __name__=="__main__": main()
