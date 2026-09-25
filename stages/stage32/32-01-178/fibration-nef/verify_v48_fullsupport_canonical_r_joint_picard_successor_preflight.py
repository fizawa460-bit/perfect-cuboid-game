#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ART=HERE/"V48-FULLSUPPORT-CANONICAL-R-JOINT-PICARD-SUCCESSOR-PREFLIGHT.json"
ART_BLOB="b68033307bf450addb0ceae6d76a2ad9e0236809"
ART_CANON="6cd87e1339fae0a9aecc451248ce5db2cd4a7e606f68050fa33f9cec27515140"
RMIN=HERE/"verify_support_qbc_canonical_r_joint_min_retained.py"
RMIN_BLOB="f135ed7c6d8db5d2ddc08f2a2c2510dee03bd83c"
PROBE=HERE/"run_v48_fullsupport_canonical_r_joint_picard_cell_probe.py"
PROBE_BLOB="407d27d15102930381b9da38e15fae783ceb0fe5"
V2=HERE/"V48-FULLSUPPORT-CANONICAL-JOINT-PICARD-SUCCESSOR-PREFLIGHT.json"
V2_BLOB="fb2e208ec374d15e4a1bfc9fa859ac7d36773185"
V2_CANON="d3d4d1970cdf579c4492e3d393ccc1c6c943e2adc49c2f847cfc6f836ed645da"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    for p,h,n in ((ART,ART_BLOB,"v3 preflight"),(RMIN,RMIN_BLOB,"r-min retained verifier"),(PROBE,PROBE_BLOB,"v3 probe"),(V2,V2_BLOB,"v2 preflight")):
        req(p.is_file() and blob(p)==h,n+" blob drift")
    art=json.loads(ART.read_text());v2=json.loads(V2.read_text())
    req(canon(art)==ART_CANON==art["canonical_sha256_without_this_field"],"v3 canonical drift")
    req(canon(v2)==V2_CANON==v2["canonical_sha256_without_this_field"],"v2 canonical drift")
    req(art["status"]=="CANONICAL_R_JOINT_SUCCESSOR_PREPARED__ZERO_MAIN_CREDIT__EXECUTION_PENDING","status drift")
    sl=art["source_locks"]
    req(sl["canonical_r_joint_min_retained_verifier_blob_sha1"]==RMIN_BLOB,"r-min verifier lock drift")
    req(sl["canonical_r_successor_probe_blob_sha1"]==PROBE_BLOB,"v3 probe lock drift")
    req(sl["canonical_successor_v2_preflight_blob_sha1"]==V2_BLOB,"v2 source lock drift")
    d=art["dominance"]
    req("T_canonical_r(qBC) subset T_canonical(qBC)" in d["set_inclusion"],"set inclusion drift")
    req("canonical-r-joint-Picard survivors <= canonical-joint-Picard survivors" in d["picard_consequence"],"Picard dominance drift")
    req("exact index of every retained qBC histogram" in d["same_population_reason"],"r same-population bridge drift")
    e=art["structural_evidence"]
    req((e["bounded_formula_states"],e["bounded_literal_keys"],e["literal_formula_mismatches"])==(5904,1064,0),"bounded structural evidence drift")
    req((e["strict_finite_vs_canonical"],e["r_infeasible_canonical_finite"])==(396,397),"strict r evidence drift")
    req((e["active_panel_strict_states_with_canonical_floor_at_most_4992"],e["active_panel_qbc_cap_crossings"])==(555,32),"active panel r evidence drift")
    req(e["active_witness"]=={"b":36,"c":83,"t":35,"support":3,"r":1,"canonical_floor_without_r":4825,"canonical_r_floor":8115,"gain":3290},"active r witness drift")
    rd=art["route_decision"]
    req(rd["canonical_without_r_route_superseded_for_future_execution"] is True,"v2 supersession drift")
    req(rd["relaxed_joint_route_also_superseded_for_future_execution"] is True,"v1 supersession drift")
    req(rd["successor"]=="CANONICAL_R_JOINT_QBC_MIN_PLUS_PICARD_OVER_CURRENT_FULLSUPPORT","successor id drift")
    req(art["scope"]=={"heavy_execution_armed":False,"production_scaleout_authorized":False,"new_numeric_tightening_claimed":False,"main_consumption_performed":False},"scope overclaim")
    for k,v in art["firewalls"].items():
        if k=="hostile_audit_required_before_promotion": req(v is True,k)
        else: req(v is False,k)
    text=PROBE.read_text()
    for needle in ("cell_canonical_r_joint_picard_survivors","canonical_r_joint_picard_incremental_vs_current_fullsupport","exact_histogram_required_x4_parity_r_enforced","rr <= q <= p <= f"):
        req(needle in text,"v3 probe contract missing "+needle)
    subprocess.run([sys.executable,str(RMIN)],check=True)
    print("V48_FULLSUPPORT_CANONICAL_R_JOINT_PICARD_SUCCESSOR_PREFLIGHT=PASS")
    print("V1_V2_FUTURE_EXECUTION_SUPERSEDED=true")
    print("NEW_NUMERIC_TIGHTENING_CLAIMED=false")
    print("MAIN_CREDIT_CHANGED=false")

if __name__=="__main__": main()
