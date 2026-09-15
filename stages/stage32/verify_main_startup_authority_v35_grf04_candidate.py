#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
CAND = HERE / "management/grf04-uniform-bound/GRF04-V35-INDEPENDENT-UNIFORM-BLOCK-BOUND-CANDIDATE.json"
VERIFY = HERE / "management/grf04-uniform-bound/verify_grf04_v35_uniform_block_bound_candidate.py"
CROSS = HERE / "proof/verify_cross_lane_demands.py"
CLAIMS = HERE / "proof/CLAIM-REGISTRY.json"
FRONTIER = HERE / "proof/ACTIVE-FRONTIER.json"
ADAPTERS = HERE / "proof/LANE-ADAPTERS.json"

STATE_BLOB = "ec0243cb998c5c58340100d8151559516c474193"
STATE_CANON = "25e68a40148ce1ca4bb893ef47d23a0e213898aca8be3a76f497252cb2adc2eb"
CAND_BLOB = "f2a50838e9a443d70a13957c2f65626c7af5d4cc"
CAND_CANON = "aa60c5710f86891628420389b0aa5a7f12675264287bd18742e7e9255b2841e6"
VERIFY_BLOB = "274c84c8efb9a3a710c9f7374d6ab41fbcf62923"
CROSS_BLOB = "9d7c3ee0e74f8d32d54904faf817f1b387c1f01b"
CLAIMS_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

CURRENT = 3360778813767800658369
CANDIDATE = 2640734831876112735041
TIGHTENING = 720043981891687923328

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    req(blob(STATE)==STATE_BLOB,"V34 authority state blob")
    st=json.loads(STATE.read_text())
    req(st.get("canonical_sha256_without_this_field")==STATE_CANON and canon(st)==STATE_CANON,"V34 authority state canonical")
    req(blob(CAND)==CAND_BLOB,"V35 candidate blob")
    c=json.loads(CAND.read_text())
    req(c.get("canonical_sha256_without_this_field")==CAND_CANON and canon(c)==CAND_CANON,"V35 candidate canonical")
    req(blob(VERIFY)==VERIFY_BLOB,"V35 candidate verifier")
    req(blob(CROSS)==CROSS_BLOB,"cross-lane verifier")
    req(blob(CLAIMS)==CLAIMS_BLOB and blob(FRONTIER)==FRONTIER_BLOB and blob(ADAPTERS)==ADAPTERS_BLOB,"claim core drift")
    runpy.run_path(str(CROSS),run_name="__main__")
    f=st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==CURRENT,"V34 authority unchanged")
    req(st["current"]["mainbatch_stop_gate"]=="NONE","V34 operational gate remains synchronized")
    cb=c["candidate_bound"]
    req(cb["candidate_upper_bound"]==CANDIDATE and cb["candidate_tightening_vs_v34"]==TIGHTENING,"candidate arithmetic")
    req(c["status"]=="RETAINED_INDEPENDENT_PARALLEL_CANDIDATE_HOSTILE_AUDIT_REQUIRED_NO_AUTHORITY_CHANGE","candidate status")
    req(c["promotion_gate"]["hostile_audit_required"] is True and c["promotion_gate"]["main_authority_mutated"] is False,"candidate audit firewall")
    req(c["ownership"]["source_lane_state_mutated"] is False and c["ownership"]["source_lane_credit_inherited"] is False,"independent-parallel ownership")
    req(c["firewalls"]["full178_complete"] is False and c["firewalls"]["merge_authorized"] is False,"closure firewalls")
    print("PASS: Stage32 MAIN V35 retains independent GRF04 13/33 candidate with zero authority mutation")
    print("CURRENT_AUTHORITY=3360778813767800658369 CANDIDATE=2640734831876112735041 AUDIT_REQUIRED=true")

if __name__=="__main__": main()
