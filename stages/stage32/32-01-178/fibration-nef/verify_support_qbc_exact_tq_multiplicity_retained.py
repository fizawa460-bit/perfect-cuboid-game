#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ART=HERE/"SUPPORT-QBC-EXACT-TQ-MULTIPLICITY-PREFLIGHT.json"
ART_BLOB="a7629266c1815c03eb8691566a6e64cbbf1cddab"
ART_CANON="f4930f2a4ebd06ae287b89cae2213d4fe9a429d8636e765f3500ce4e80ce867b"
VERIFY=HERE/"verify_support_qbc_exact_tq_multiplicity_preflight.py"
VERIFY_BLOB="eb870daf2825037bcbdce769e9ad8b58833b99b7"
TQ_VERIFY_BLOB="1f6ede0e60689bcd4c42f4a41252289b241bd213"
PANEL_BLOB="19cfa17b049b94dee5f406cb8db32ca94e8cf318"
PANEL_CANON="ec9aa7f7300f7613bd05ef3dbdd56de45db0193f91c1d7a82ed7f3e4c972de60"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p):
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    req(ART.is_file() and blob(ART)==ART_BLOB,"multiplicity artifact blob drift")
    req(VERIFY.is_file() and blob(VERIFY)==VERIFY_BLOB,"multiplicity verifier blob drift")
    art=json.loads(ART.read_text())
    req(canon(art)==ART_CANON==art["canonical_sha256_without_this_field"],"multiplicity artifact canonical drift")
    req(art["status"]=="EXACT_CANONICAL_T_QBC_MULTIPLICITY_FACTORIZATION__ZERO_MAIN_CREDIT","status drift")
    sl=art["source_locks"]
    req(sl["exact_tq_support_verifier_blob_sha1"]==TQ_VERIFY_BLOB,"exact tq source lock drift")
    req(sl["retained_exact_tset_panel_blob_sha1"]==PANEL_BLOB,"panel blob lock drift")
    req(sl["retained_exact_tset_panel_canonical_sha256"]==PANEL_CANON,"panel canonical lock drift")
    req(sl["exact_tq_multiplicity_verifier_blob_sha1"]==VERIFY_BLOB,"self verifier lock drift")

    req(art["bounded_literal_enumeration"]=={
        "literal_keys":197,
        "formula_mismatches":0,
        "total_tuple_multiplicity":686,
        "total_exact_q_values":256,
        "max_single_q_multiplicity":10,
    },"bounded literal summary drift")

    rows=art["active_three_cell_structural_scan"]
    req([(x["c"],x["qbc_bins"],x["joint_t_qbc_cells"],x["total_h_multiplicity_qcap"],x["max_single_t_qbc_multiplicity"],x["qbc_bins_with_multiple_t"],x["max_exact_t_per_qbc"]) for x in rows]==[
        (83,8274,268838,11772562,641,8202,56),
        (85,7909,261160,12073210,665,7841,58),
        (89,7152,240759,12448811,671,7104,59),
    ],"active multiplicity rows drift")
    req(art["active_three_cell_totals"]=={
        "qbc_bins":23335,
        "joint_t_qbc_cells":770757,
        "total_h_multiplicity_qcap":36294583,
        "qbc_bins_with_multiple_t":23147,
    },"active multiplicity totals drift")

    claim=art["claim"]
    req(claim["actual_weighted_v48_gain_claimed"] is False,"weighted gain overclaim")
    req("sum_t multiplicity(t,qBC)=the source qBC histogram multiplicity" in claim["marginal_identity_required_at_replay"],"marginal identity contract drift")
    route=art["route_decision"]
    req(route["exact_tq_union_route_superseded_for_future_execution"] is True,"union route not superseded")
    req(route["successor"]=="EXACT_T_QBC_MULTIPLICITY_CORRELATED_PICARD_OVER_CURRENT_FULLSUPPORT","successor drift")
    for k,v in art["firewalls"].items():
        req(v is False,"credit firewall "+k)

    subprocess.run([sys.executable,str(VERIFY)],check=True)

    print("SUPPORT_QBC_EXACT_TQ_MULTIPLICITY_RETAINED=PASS")
    print("ACTIVE_QBC_BINS=23335")
    print("ACTIVE_MULTI_T_QBC_BINS=23147")
    print("ACTIVE_H_MULTIPLICITY_QCAP=36294583")
    print("WEIGHTED_V48_GAIN_CLAIMED=false")
    print("MAIN_CREDIT_CHANGED=false")

if __name__=="__main__": main()
