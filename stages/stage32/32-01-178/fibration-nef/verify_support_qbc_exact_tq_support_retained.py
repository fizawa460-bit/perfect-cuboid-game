#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ART=HERE/"SUPPORT-QBC-EXACT-TQ-SUPPORT-PREFLIGHT.json"
ART_BLOB="efd6113e1b10b89b117d3a80cb9b97ff1adaa284"
ART_CANON="6bc7beb8c8a0b76d6b150950f0341ff97f5193551fd0882c2504bae172a65d26"
VERIFY=HERE/"verify_support_qbc_exact_tq_support_preflight.py"
VERIFY_BLOB="1f6ede0e60689bcd4c42f4a41252289b241bd213"
RMIN_BLOB="bb8ccb843a2e2bacaf5c25f88116e2ddddfc4439"
PANEL_BLOB="19cfa17b049b94dee5f406cb8db32ca94e8cf318"
PANEL_CANON="ec9aa7f7300f7613bd05ef3dbdd56de45db0193f91c1d7a82ed7f3e4c972de60"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    req(ART.is_file() and blob(ART)==ART_BLOB,"exact tq artifact blob drift")
    req(VERIFY.is_file() and blob(VERIFY)==VERIFY_BLOB,"exact tq verifier blob drift")
    art=json.loads(ART.read_text())
    req(canon(art)==ART_CANON==art["canonical_sha256_without_this_field"],"exact tq artifact canonical drift")
    sl=art["source_locks"]
    req(sl["canonical_r_joint_min_verifier_blob_sha1"]==RMIN_BLOB,"r-min source lock drift")
    req(sl["exact_tq_support_verifier_blob_sha1"]==VERIFY_BLOB,"self verifier lock drift")
    req(sl["retained_exact_tset_panel_blob_sha1"]==PANEL_BLOB,"panel source lock drift")
    req(sl["retained_exact_tset_panel_canonical_sha256"]==PANEL_CANON,"panel canonical lock drift")
    req(art["bounded_literal_enumeration"]=={"literal_keys":197,"formula_mismatches":0,"total_exact_q_values":256,"max_q_values_per_state":3},"bounded literal summary drift")
    totals=art["active_three_cell_totals"]
    req(totals=={"exact_hist_qbc_bins":23335,"strict_qbc_bins":15976,"removed_t_total":243749,"max_removed_t_in_one_qbc_bin":60},"active total drift")
    rows=art["active_three_cell_structural_scan"]
    req([(x["c"],x["exact_hist_qbc_bins"],x["strict_qbc_bins"],x["removed_t_total"],x["max_removed_t"]) for x in rows]==[
        (83,8274,5912,97503,59),(85,7909,5478,85294,60),(89,7152,4586,60952,57)
    ],"active row summary drift")
    req(rows[0]["max_removed_witness"]=={"support":4,"r":0,"qbc":4707,"floor_tset_size":60,"exact_tset":[95],"removed_t":59},"c83 witness drift")
    req(rows[1]["max_removed_witness"]=={"support":4,"r":0,"qbc":4947,"floor_tset_size":61,"exact_tset":[97],"removed_t":60},"c85 witness drift")
    req(rows[2]["max_removed_witness"]=={"support":4,"r":0,"qbc":4863,"floor_tset_size":58,"exact_tset":[83],"removed_t":57},"c89 witness drift")
    req(art["claim"]["actual_weighted_v48_gain_claimed"] is False,"weighted gain overclaim")
    for k,v in art["firewalls"].items(): req(v is False,"credit firewall "+k)
    subprocess.run([sys.executable,str(VERIFY)],check=True)
    print("SUPPORT_QBC_EXACT_TQ_SUPPORT_RETAINED=PASS")
    print("ACTIVE_EXACT_QBC_BINS=23335")
    print("STRICT_QBC_BINS=15976")
    print("REMOVED_T_TOTAL=243749")
    print("WEIGHTED_V48_GAIN_CLAIMED=false")
    print("MAIN_CREDIT_CHANGED=false")

if __name__=="__main__": main()
