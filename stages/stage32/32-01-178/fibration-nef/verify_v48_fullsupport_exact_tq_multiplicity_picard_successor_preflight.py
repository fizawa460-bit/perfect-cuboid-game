#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ART=HERE/"V48-FULLSUPPORT-EXACT-TQ-MULTIPLICITY-PICARD-SUCCESSOR-PREFLIGHT.json"
ART_BLOB="3f4dfff736aafa0f84e85bfb488e83870e18d95c"
ART_CANON="58a4825bfab902678be6167f9d01cb487f1bd555f7d6dc5fbf6b02b9f362cd5a"
MULT_ART=HERE/"SUPPORT-QBC-EXACT-TQ-MULTIPLICITY-PREFLIGHT.json"
MULT_ART_BLOB="a7629266c1815c03eb8691566a6e64cbbf1cddab"
MULT_ART_CANON="f4930f2a4ebd06ae287b89cae2213d4fe9a429d8636e765f3500ce4e80ce867b"
MULT_VERIFY=HERE/"verify_support_qbc_exact_tq_multiplicity_retained.py"
MULT_VERIFY_BLOB="e40e6abe0e163571b810927d5ddf4d086570faf1"
PROBE=HERE/"run_v48_fullsupport_exact_tq_multiplicity_picard_cell_probe.py"
PROBE_BLOB="b349ece87438bd78909e25f5edca7e157201b201"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p):
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    for p,h,n in (
        (ART,ART_BLOB,"successor artifact"),
        (MULT_ART,MULT_ART_BLOB,"multiplicity artifact"),
        (MULT_VERIFY,MULT_VERIFY_BLOB,"multiplicity retained verifier"),
        (PROBE,PROBE_BLOB,"multiplicity consumer"),
    ):
        req(p.is_file() and blob(p)==h,n+" blob drift")

    art=json.loads(ART.read_text())
    mult=json.loads(MULT_ART.read_text())
    req(canon(art)==ART_CANON==art["canonical_sha256_without_this_field"],"successor canonical drift")
    req(canon(mult)==MULT_ART_CANON==mult["canonical_sha256_without_this_field"],"multiplicity canonical drift")
    req(art["status"]=="EXACT_TQ_MULTIPLICITY_SUCCESSOR_PREPARED__ZERO_MAIN_CREDIT__EXECUTION_PENDING","status drift")

    sl=art["source_locks"]
    req(sl["exact_tq_multiplicity_preflight_blob_sha1"]==MULT_ART_BLOB,"multiplicity artifact source drift")
    req(sl["exact_tq_multiplicity_preflight_canonical_sha256"]==MULT_ART_CANON,"multiplicity canonical source drift")
    req(sl["exact_tq_multiplicity_retained_verifier_blob_sha1"]==MULT_VERIFY_BLOB,"multiplicity retained verifier source drift")
    req(sl["exact_tq_multiplicity_probe_blob_sha1"]==PROBE_BLOB,"consumer source drift")

    e=art["structural_evidence"]
    req(e["active_three_cell_qbc_bins"]==23335,"qBC bin count drift")
    req(e["active_three_cell_multi_t_qbc_bins"]==23147,"multi-t bin count drift")
    req(e["active_three_cell_joint_t_qbc_cells"]==770757,"joint t-qBC cell count drift")
    req(e["active_three_cell_total_h_multiplicity_qcap"]==36294583,"H multiplicity drift")
    req(abs(float(e["active_three_cell_multi_t_fraction"])-23147/23335)<1e-15,"multi-t fraction drift")

    d=art["dominance"]
    req("sum_t m(t,qBC)*count_x4(single t)" in d["exact_multiplicity_over_union"],"correlated dominance statement drift")
    req("sum_t m(t,qBC)=source qBC histogram multiplicity" in d["marginal_identity"],"marginal identity statement drift")
    req(d["h_side_exactness"].startswith("for the current consumer"),"H-side exactness statement drift")
    req(art["route_decision"]["exact_tq_union_route_superseded_for_future_execution"] is True,"exact-tq union not superseded")
    req(art["route_decision"]["successor"]=="EXACT_T_QBC_MULTIPLICITY_CORRELATED_PICARD_OVER_CURRENT_FULLSUPPORT","successor drift")

    text=PROBE.read_text()
    for needle in (
        "sum(t_mult.values()) == int(hist[qbc])",
        "exact_tq_multiplicity[qbc] = t_mult",
        "mw[ap] += mc",
        "mm = mw[ap][qa] * mult",
        "req(mm <= tt <= rr <= q <= p <= f <= z <= y <= x",
        '"every_qbc_bin_marginal_replayed_against_source_histogram": True',
    ):
        req(needle in text,"consumer contract missing "+needle)

    req(art["scope"]=={
        "heavy_execution_armed":False,
        "production_scaleout_authorized":False,
        "new_numeric_tightening_claimed":False,
        "main_consumption_performed":False,
    },"scope overclaim")
    for k,v in art["firewalls"].items():
        if k=="hostile_audit_required_before_promotion":
            req(v is True,k)
        else:
            req(v is False,"credit firewall "+k)

    subprocess.run([sys.executable,str(MULT_VERIFY)],check=True)

    print("V48_FULLSUPPORT_EXACT_TQ_MULTIPLICITY_SUCCESSOR_PREFLIGHT=PASS")
    print("ACTIVE_MULTI_T_QBC_BINS=23147/23335")
    print("H_SIDE_CORRELATION_EXACT_AFTER_MARGINAL_REPLAY=true")
    print("NUMERIC_GAIN_REQUIRES_AUTHORIZED_EXECUTION=true")
    print("MAIN_CREDIT_CHANGED=false")

if __name__=="__main__": main()
