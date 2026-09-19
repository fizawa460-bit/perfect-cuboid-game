#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

BASE="stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
ARCHIVE={
 f"{BASE}/AUTS-NODE-ACTION-SOURCE-NOTE.md":"cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693",
 f"{BASE}/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md":"a29161602c0b38f0607794e56e61068b8cb9735d",
}
CURRENT={
 f"{BASE}/MB104-P6A-KNOWN-LOW-DEGREE-TEST-CURVE-CERTIFICATE.json":"ab16e0757607c702fbc548dd9393d16d6c5f899b",
 f"{BASE}/MB104-P6D2-AUTOMATIC-ODD-EQUALITY-20260919.md":"1194fdd228c394d79262579df3930b4d8f619cf9",
 f"{BASE}/MB104-P6M-SINGULARITY-TYPE-LOG-BMY-CORRECTION-PREFLIGHT-CERTIFICATE.json":"59aeedc2a9ee0970fa552a2d08fdc67e0f81c4e0",
}
def req(c,m):
 if not c: raise SystemExit("FAIL: "+m)
def blob(p):
 b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def main():
 root=Path(__file__).resolve().parents[6]
 c=json.loads(Path(__file__).with_name("MB104-P6N-FULL-G-BRANCH-VALUE-PAIR-INCIDENCE-PREFLIGHT-CERTIFICATE.json").read_text())
 req(c["hostile_support"]["mask_hex"]=="0000093f442e","hostile mask")
 req(c["hostile_support"]["inertia_type_counts"]==[6,2,6],"type counts")
 r=c["retained_interface"]
 req(r["exact_48_node_coordinates"] is True,"node coordinates")
 req(r["exact_autS_node_action"] is True,"Aut(S) action")
 req(r["three_stabilizer_types_exact"] is True,"stabilizer types")
 req(r["individual_factor_branch_value_labels_source_locked"] is False,"no individual labels")
 req(r["node_to_factorwise_branch_pair_adapter_found"] is False,"no branch-pair adapter")
 req(c["disposition"]=="PARK_P6N_AT_MISSING_FACTORWISE_BRANCH_VALUE_LABEL_ADAPTER","disposition")
 req(c["next_leaf"]=="MB104-P6O-MODULAR-FIXED-POINT-BRANCH-LABEL-ADAPTER-PREFLIGHT","next leaf")
 req(all(v is False for v in c["firewalls"].values()),"credit firewall")
 print("PASS: P6N branch-value pair incidence preflight wall")
 print("three inertia types are exact; factorwise individual branch values are not source-locked")
 print("2x2 incidence is not inferred by coordinate/block heuristics")
 print("next: P6O modular fixed-point branch-label adapter preflight")
if __name__=="__main__": main()
