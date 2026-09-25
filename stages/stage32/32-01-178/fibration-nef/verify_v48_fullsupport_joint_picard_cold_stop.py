#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STOP=HERE/"V48-FULLSUPPORT-JOINT-PICARD-COLD-STOP.json"
STOP_BLOB="1f19066739cf7e9509fce9ee0fcb1207f14a6334"
STOP_CANON="fc64194b18893dce1db2eb3fff349c9635abb052c7123fa10721b6bb68c9cb0d"
RUNKEY=HERE/"V48-FULLSUPPORT-JOINT-PICARD-RUNKEY.json"
RUNKEY_BLOB="4f60d326f5560aa559c3eb3349f72b164e0f00a8"
DOM=HERE/"V48-FULLSUPPORT-JOINT-PICARD-UNIFORM-DOMINANCE.json"
DOM_BLOB="50ca55cdb03b68e1eff3399cfdabe2d82f8d7328"
DOM_CANON="15e475bd6dec8a8047f20df0ae2379df1fb2218a1dfd8e3f7db7d0806d343ca3"
PREF=HERE/"V48-FULLSUPPORT-JOINT-PICARD-SUCCESSOR-PREFLIGHT.json"
PREF_BLOB="e5165896e879567a8f18a2d41164ee225d7ac90e"
PREF_CANON="fe6723e39689e72e64510c3f8c68b6215e271bbcd21b9fd793a8f53ce1905d7a"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    for p,h,n in ((STOP,STOP_BLOB,"cold stop"),(RUNKEY,RUNKEY_BLOB,"runkey"),(DOM,DOM_BLOB,"dominance"),(PREF,PREF_BLOB,"preflight")):
        req(p.is_file() and blob(p)==h,n+" blob drift")
    stop=json.loads(STOP.read_text()); rk=json.loads(RUNKEY.read_text()); dom=json.loads(DOM.read_text()); pref=json.loads(PREF.read_text())
    req(canon(stop)==STOP_CANON==stop["canonical_sha256_without_this_field"],"cold-stop canonical drift")
    req(canon(dom)==DOM_CANON==dom["canonical_sha256_without_this_field"],"dominance canonical drift")
    req(canon(pref)==PREF_CANON==pref["canonical_sha256_without_this_field"],"preflight canonical drift")
    req(stop["status"]=="BLOCKED_EXECUTION_AUTHORIZATION_REQUIRED","cold-stop status drift")
    req(stop["observed_live_main"]["head"]=="a834864923086e5f7c1647e462804f45ff9ac28d","live-main lock drift")
    req(stop["current_lane_candidate"]["candidate_upper_bound_if_promoted"]=="128443221087959579960","candidate drift")
    req(stop["locked_execution_contract"]["runkey_blob_sha1"]==RUNKEY_BLOB,"runkey lock drift")
    req(rk["generation"]==0 and rk["mode"]=="COLD" and rk["armed"] is False,"runkey not cold")
    req(rk["authorized_c_values"]==[] and rk["planned_effective_heavy_concurrency"]==0,"cold runkey authorizes work")
    req(rk["firewalls"]["heavy_execution_authorized"] is False and rk["firewalls"]["artifact_production_authorized"] is False,"heavy/artifact firewall drift")
    req(stop["blocker"]["heavy_or_artifact_execution_currently_authorized"] is False,"cold-stop execution authorization drift")
    req(stop["blocker"]["additional_representation_rewrite_required"] is False,"representation unexpectedly incomplete")
    req(stop["blocker"]["numerical_progress_without_execution"] is False,"numerical progress overclaim")
    req([x["id"] for x in stop["reopen_conditions"]]==["BOUNDED_PANEL_AUTHORIZED","MAIN_REASSIGNS_178","NEW_NONHEAVY_MATHEMATICAL_WEAPON"],"reopen conditions drift")
    for k in ("full_row_census_claimed","full178_new_census_claimed","main_credit_changed","theorem_credit_changed","effectivity_credit","receiver_credit","route_credit","endpoint_credit_changed","stage32_closed","perfect_cuboid_claim","merge"):
        req(stop["firewalls"][k] is False,"cold-stop firewall "+k)
    print("V48_FULLSUPPORT_JOINT_PICARD_COLD_STOP=PASS")
    print("RUNKEY=generation0_modeCOLD_armedfalse")
    print("NEXT_NUMERIC_STEP_REQUIRES_EXPLICIT_AUTHORIZATION=true")
    print("MAIN_CREDIT_CHANGED=false")
if __name__=="__main__":main()
