#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ART=HERE/"SUPPORT-QBC-CANONICAL-R-JOINT-MIN-PREFLIGHT.json"
ART_BLOB="e6a996aee1cfff1424320c9c664df0ae3ac89c1d"
ART_CANON="297cf63ea734a7409f1165af6e2b59610bd04feea68e1d1eaaee077e14fafc11"
FORMULA=HERE/"verify_support_qbc_canonical_r_joint_min_preflight.py"
FORMULA_BLOB="bb8ccb843a2e2bacaf5c25f88116e2ddddfc4439"
CANON_BLOB="4296a18f9fb1b59f963206ff28af73a4e9cf7ef0"
SOURCE_BLOB="37e72735125c232e534d92c6e24c7afc0a0f4f24"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    req(ART.is_file() and blob(ART)==ART_BLOB,"r-conditioned artifact blob drift")
    req(FORMULA.is_file() and blob(FORMULA)==FORMULA_BLOB,"r-conditioned formula verifier blob drift")
    art=json.loads(ART.read_text())
    req(canon(art)==ART_CANON==art["canonical_sha256_without_this_field"],"r-conditioned artifact canonical drift")
    req(art["source_locks"]=={
        "support_qbc_worker_blob_sha1":SOURCE_BLOB,
        "canonical_joint_min_verifier_blob_sha1":CANON_BLOB,
        "canonical_r_joint_min_verifier_blob_sha1":FORMULA_BLOB,
    },"source lock drift")
    req(art["bounded_formula_regression"]=={
        "states":5904,"canonical_finite":2256,"r_finite":1859,
        "r_infeasible_canonical_finite":397,"strict_finite":396,
        "equal_finite":1463,"max_strict_gain":30,"weakening":0,
    },"bounded formula summary drift")
    req(art["bounded_literal_enumeration"]=={
        "literal_keys":1064,"formula_mismatches":0,
        "strict_vs_canonical_without_r":145,"max_strict_gain":4,
    },"literal summary drift")
    w=art["active_structural_witness"]
    req((w["b"],w["c"],w["t"],w["support"])==(36,83,35,3),"active witness target drift")
    req((w["separate_floor"],w["relaxed_joint_floor"],w["canonical_floor_without_r"],w["canonical_r0_floor"],w["canonical_r1_floor"])==(4753,4825,4825,4825,8115),"active witness floors drift")
    p=art["active_three_cell_structural_scan"]
    req(p["strict_with_canonical_floor_at_most_4992_total"]==555,"active strict total drift")
    req(p["qbc_cap_crossing_total"]==32,"active cap crossing total drift")
    req(sum(x["r_infeasible_canonical_finite"] for x in p["rows"])==76,"active r-infeasible total drift")
    req(art["claim"]["actual_weighted_v48_gain_claimed"] is False,"weighted gain overclaim")
    for k,v in art["firewalls"].items(): req(v is False,"credit firewall "+k)
    subprocess.run([sys.executable,str(FORMULA)],check=True)
    print("SUPPORT_QBC_CANONICAL_R_JOINT_MIN_RETAINED=PASS")
    print("ACTIVE_PANEL_STRUCTURAL_STRICT_STATES_LE4992=555")
    print("ACTIVE_PANEL_QBC_CAP_CROSSINGS=32")
    print("ACTIVE_WITNESS_R1=4825_to_8115")
    print("WEIGHTED_V48_GAIN_CLAIMED=false")
    print("MAIN_CREDIT_CHANGED=false")

if __name__=="__main__": main()
