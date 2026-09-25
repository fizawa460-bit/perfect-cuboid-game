#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STOP=HERE/"V48-FULLSUPPORT-EXACT-TQ-MULTIPLICITY-PICARD-COLD-STOP.json"
STOP_BLOB="7fcf877eea789333ce06905394a29834d9205c21"
STOP_CANON="a1f462a6db37a911cc8cd6aee69b521258f08642e968ecc04428d44c9577e916"
RUNKEY=HERE/"V48-FULLSUPPORT-EXACT-TQ-MULTIPLICITY-PICARD-RUNKEY.json"
RUNKEY_BLOB="b69660c5602936969b46c6aaeee769735e1a7cc5"
RUNKEY_CANON="5289162d6720d44f70b232aaf61fbfae2b229ec00755074e44249306d815ba1b"
SUCCESSOR=HERE/"V48-FULLSUPPORT-EXACT-TQ-MULTIPLICITY-PICARD-SUCCESSOR-PREFLIGHT.json"
SUCCESSOR_BLOB="3f4dfff736aafa0f84e85bfb488e83870e18d95c"
SUCCESSOR_CANON="58a4825bfab902678be6167f9d01cb487f1bd555f7d6dc5fbf6b02b9f362cd5a"
MULT=HERE/"SUPPORT-QBC-EXACT-TQ-MULTIPLICITY-PREFLIGHT.json"
MULT_BLOB="a7629266c1815c03eb8691566a6e64cbbf1cddab"
MULT_CANON="f4930f2a4ebd06ae287b89cae2213d4fe9a429d8636e765f3500ce4e80ce867b"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_locked(path,blob_sha,canon_sha,label):
    req(path.is_file() and blob(path)==blob_sha,label+" blob drift")
    obj=json.loads(path.read_text())
    req(canon(obj)==canon_sha==obj["canonical_sha256_without_this_field"],label+" canonical drift")
    return obj

def main():
    stop=load_locked(STOP,STOP_BLOB,STOP_CANON,"cold stop")
    rk=load_locked(RUNKEY,RUNKEY_BLOB,RUNKEY_CANON,"runkey")
    succ=load_locked(SUCCESSOR,SUCCESSOR_BLOB,SUCCESSOR_CANON,"successor")
    mult=load_locked(MULT,MULT_BLOB,MULT_CANON,"multiplicity")

    req(stop["status"]=="BLOCKED_EXECUTION_AUTHORIZATION_REQUIRED","cold-stop status drift")
    req(stop["observed_live_main"]["head"]=="a834864923086e5f7c1647e462804f45ff9ac28d","live-main lock drift")
    req(stop["current_lane_candidate"]["candidate_upper_bound_if_promoted"]=="128443221087959579960","candidate drift")
    req(stop["new_nonheavy_weapon"]["id"]=="EXACT_T_QBC_MULTIPLICITY_CORRELATION","weapon id drift")
    req(stop["new_nonheavy_weapon"]["active_qbc_bins"]==23335,"qBC bin drift")
    req(stop["new_nonheavy_weapon"]["active_multi_t_qbc_bins"]==23147,"multi-t bin drift")
    req(stop["new_nonheavy_weapon"]["active_h_multiplicity_qcap"]==36294583,"H multiplicity drift")
    req(stop["successor"]["preflight_blob_sha1"]==SUCCESSOR_BLOB,"successor lock drift")
    req(stop["locked_execution_contract"]["runkey_blob_sha1"]==RUNKEY_BLOB,"runkey lock drift")

    req(rk["generation"]==0 and rk["mode"]=="COLD" and rk["armed"] is False,"runkey not cold")
    req(rk["authorized_c_values"]==[] and rk["planned_effective_heavy_concurrency"]==0,"cold runkey authorizes work")
    req(rk["firewalls"]["heavy_execution_authorized"] is False,"heavy execution unexpectedly authorized")
    req(rk["firewalls"]["artifact_production_authorized"] is False,"artifact production unexpectedly authorized")

    req(succ["route_decision"]["successor"]=="EXACT_T_QBC_MULTIPLICITY_CORRELATED_PICARD_OVER_CURRENT_FULLSUPPORT","successor route drift")
    req(succ["scope"]["new_numeric_tightening_claimed"] is False,"successor numeric overclaim")
    req(mult["claim"]["actual_weighted_v48_gain_claimed"] is False,"multiplicity numeric overclaim")
    req(stop["blocker"]["numerical_progress_without_execution"] is False,"cold stop numeric overclaim")
    req(stop["blocker"]["additional_representation_rewrite_required"] is False,"representation not complete")
    req(stop["blocker"]["heavy_or_artifact_execution_currently_authorized"] is False,"execution authorization drift")

    req([x["id"] for x in stop["reopen_conditions"]]==[
        "EXACT_TQ_MULTIPLICITY_BOUNDED_PANEL_AUTHORIZED",
        "MAIN_REASSIGNS_178",
        "NEW_NONHEAVY_MATHEMATICAL_WEAPON",
    ],"reopen conditions drift")

    for k in ("full_row_census_claimed","full178_new_census_claimed","main_credit_changed",
              "theorem_credit_changed","effectivity_credit","receiver_credit","route_credit",
              "endpoint_credit_changed","stage32_closed","perfect_cuboid_claim","merge"):
        req(stop["firewalls"][k] is False,"cold-stop firewall "+k)

    print("V48_FULLSUPPORT_EXACT_TQ_MULTIPLICITY_COLD_STOP=PASS")
    print("RUNKEY=generation0_modeCOLD_armedfalse")
    print("H_SIDE_REPRESENTATION_COMPLETE_FOR_CURRENT_CONSUMER=true")
    print("NEXT_NUMERIC_STEP_REQUIRES_EXPLICIT_AUTHORIZATION=true")
    print("MAIN_CREDIT_CHANGED=false")

if __name__=="__main__": main()
