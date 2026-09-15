#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
STATE=HERE/"MAIN-STATE.json"; CAND=HERE/"management/grf04-uniform-bound/GRF04-V35-INDEPENDENT-UNIFORM-BLOCK-BOUND-CANDIDATE.json"; VERIFY=HERE/"management/grf04-uniform-bound/verify_grf04_v35_uniform_block_bound_candidate.py"; CROSS=HERE/"proof/verify_cross_lane_demands.py"; CLAIMS=HERE/"proof/CLAIM-REGISTRY.json"; FRONTIER=HERE/"proof/ACTIVE-FRONTIER.json"; ADAPTERS=HERE/"proof/LANE-ADAPTERS.json"
STATE_BLOB="ec0243cb998c5c58340100d8151559516c474193"; STATE_CANON="25e68a40148ce1ca4bb893ef47d23a0e213898aca8be3a76f497252cb2adc2eb"; CAND_BLOB="a203df7b15a9cc655b78aa70b849933b98404a2d"; CAND_CANON="221f7bc44989130de39b639d4a0a0af85a056ea0ab9461e61a1cb24be907d5b5"; VERIFY_BLOB="1e6c2d2305e9e41e8d6bb9c0ba447a6faedf01d7"; CROSS_BLOB="9d7c3ee0e74f8d32d54904faf817f1b387c1f01b"; CLAIMS_BLOB="f3a884adc1c82aace81cb73d049ff14720ace862"; FRONTIER_BLOB="4c251be4aa5c355481fe3bcfc71c292fb6389ba4"; ADAPTERS_BLOB="c0ef34e5838e27046a20fed77063593009c56f40"
CURRENT=3360778813767800658369; CANDIDATE=511195899564352597589; TIGHTENING=2849582914203448060780

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
    req(blob(STATE)==STATE_BLOB,"V34 state blob"); st=json.loads(STATE.read_text()); req(st.get("canonical_sha256_without_this_field")==STATE_CANON and canon(st)==STATE_CANON,"V34 state canonical")
    req(blob(CAND)==CAND_BLOB,"V35 candidate blob"); c=json.loads(CAND.read_text()); req(c.get("canonical_sha256_without_this_field")==CAND_CANON and canon(c)==CAND_CANON,"V35 candidate canonical")
    req(blob(VERIFY)==VERIFY_BLOB,"V35 verifier"); req(blob(CROSS)==CROSS_BLOB,"cross verifier"); req(blob(CLAIMS)==CLAIMS_BLOB and blob(FRONTIER)==FRONTIER_BLOB and blob(ADAPTERS)==ADAPTERS_BLOB,"claim core drift")
    runpy.run_path(str(CROSS),run_name="__main__")
    f=st["current_exact_frontier"]; req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==CURRENT,"V34 authority unchanged")
    cb=c["candidate_bound"]; req(cb["candidate_upper_bound"]==CANDIDATE and cb["candidate_tightening_vs_v34"]==TIGHTENING,"candidate arithmetic"); req(cb["dual_threshold"]=="1/15","dual threshold")
    req(c["status"]=="RETAINED_INDEPENDENT_PARALLEL_CANDIDATE_HOSTILE_AUDIT_REQUIRED_NO_AUTHORITY_CHANGE","candidate status"); req(c["promotion_gate"]["hostile_audit_required"] is True and c["promotion_gate"]["main_authority_mutated"] is False and c["promotion_gate"]["main_credit_granted"] is False,"audit firewall")
    req(c["ownership"]["source_lane_state_mutated"] is False and c["ownership"]["source_lane_credit_inherited"] is False,"ownership"); req(c["firewalls"]["full178_complete"] is False and c["firewalls"]["merge_authorized"] is False,"closure firewalls")
    print("PASS: Stage32 MAIN V35 retains canonical-capacity LP candidate with zero authority mutation")
    print("CURRENT_AUTHORITY=3360778813767800658369 CANDIDATE=511195899564352597589 AUDIT_REQUIRED=true")
if __name__=="__main__": main()
