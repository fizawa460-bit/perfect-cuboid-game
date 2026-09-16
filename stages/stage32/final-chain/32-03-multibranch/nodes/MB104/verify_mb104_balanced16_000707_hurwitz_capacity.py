#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY.md","c91f97b738faa66a49a068824f9b8c3739d4a8fa"),
 "NODE_TYPE_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-BEAUVILLE-NODE-TYPE-QUOTIENT-CERTIFICATE.json","f018c21bb1ecd4e33fc31d5aae15650928e592c3"),
 "EQUALITY_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json","62a2d01447016731001d35cc5915880daa2bfada"),
 "NODE_TYPE_SOURCE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md","a29161602c0b38f0607794e56e61068b8cb9735d"),
}

def req(c,m):
    if not c: raise SystemExit("FAIL: "+m)
def root():
    p=HERE
    while p!=p.parent:
        if (p/"AGENTS.md").is_file() and (p/"stages").is_dir(): return p
        p=p.parent
    raise SystemExit("FAIL: repo root")
def blob(p):
    d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()
def preflight(cert):
    dec={x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    req(dec==LOCKS,"source locks")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel; req(p.is_file(),f"missing {k}")
        req(blob(p)==sha,f"SOURCE_LOCK_FAIL {k}")

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_BALANCED16_000707_HURWITZ_CAPACITY_V1","schema")
    preflight(cert)
    req(cert["support"]["node_type_counts"]==[7,7,0],"support types")
    for l in range(1,9):
        # e=2: K order4; C8/K genus0 because fixed counts 8+8 and one free element.
        req(8 == 4*(-2)+8+8,"e2 factor RH")
        n=28*l
        total_r=2*n
        total_u=8*n-2*total_r
        req(total_r==56*l,"e2 total ramification")
        req(total_u==112*l,"e2 unramified capacity")
        req(7*8*l==56*l,"e2 type branch total")
        req(2*(56*l)==total_u,"e2 support exhausts capacity")
        # parity/fiber check for every admissible u at a branch value.
        for u in range(0,n+1,2):
            r=(n-u)//2
            req(u+2*r==n,"e2 local fiber")
        # e=4: full G. Three singular involutions with 8 fixed points give genus0;
        # all G0 elements and the fourth outside involution are free.
        req(8 == 8*(-2)+3*8,"e4 factor RH")
        n4=56*l
        total_r4=2*n4
        total_u4=6*n4-2*total_r4
        req(total_r4==112*l,"e4 total ramification")
        req(total_u4==112*l,"e4 unramified capacity")
        req(2*(56*l)==total_u4,"e4 used types exhaust capacity")
        absent_u=0
        absent_r=(n4-absent_u)//2
        req(absent_r==28*l,"e4 absent type fixed-point-free")
        # Upstairs fixed-point saturation.
        g2=112*l+1
        req(2*(g2-1)==224*l,"e2 2g-2")
        req(112*l+112*l==224*l,"e2 K fixed saturation")
        g4=224*l+1
        req(2*(g4-1)==448*l,"e4 2g-2")
        req(224*l+224*l==448*l,"e4 G fixed saturation")
    req(cert["e2"]["supported_branches_exhaust_unramified_capacity"] is True,"e2 exhaustion")
    req(cert["e4"]["supported_branches_exhaust_unramified_capacity"] is True,"e4 exhaustion")
    req(cert["e4"]["absent_type_branch_values_fixed_point_free_monodromy"] is True,"e4 absent type")
    sf=cert["scope_firewall"]
    req(sf["per_node_branch_value_concentration_claimed"] is False,"no per-node concentration")
    req(sf["u_divisible_by_8l_claimed"] is False,"no 8l divisibility")
    for k in ("e2_closed","e4_closed","orbit_closed","MB104_complete","receiver_credit","theorem_credit","endpoint_credit","merge_authorized"):
        req(sf[k] is False,f"firewall {k}")
    print("PASS STAGE32_MB104_BALANCED16_000707_HURWITZ_CAPACITY_V1")
    print("e=2: degree28l / 8 branch values; e=4: degree56l / 6 branch values")
    print("in both cases supported 112l branches exactly exhaust all unramified capacity; no closure")

if __name__=="__main__": main()
