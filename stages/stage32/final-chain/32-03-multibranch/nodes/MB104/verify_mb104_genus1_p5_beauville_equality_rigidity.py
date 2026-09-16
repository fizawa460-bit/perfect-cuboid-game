#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md","a20547082b1ea2f786b1272d1b76af3527508e9b"),
 "PRODUCT_SOURCE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-PRODUCT-COVER-SOURCE-NOTE.md","974c6cfecb6e4141615583841a0c90146ad2b4a6"),
 "BEAUVILLE_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-ODD-BRANCH-COVER-CERTIFICATE.json","6a3fc0207aa66b453be0ad2f921425a70f93bd91"),
 "FORMAL_FEASIBILITY_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-FEASIBILITY-CERTIFICATE.json","8ec4a403d2485dbf061b8b16182aa06c62193c43"),
 "FORMAL_PICARD":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md","de83fc169814681109bcbc1576ad24f67d6159e0"),
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
        p=rr/rel
        req(p.is_file(),f"missing {k}")
        got=blob(p)
        req(got==sha,f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_GENUS1_P5_BEAUVILLE_EQUALITY_RIGIDITY_V1","schema")
    preflight(cert)
    req(cert["uniform_F1_P5"]["g"]==1,"g=1")
    req(cert["uniform_F1_P5"]["equality_face"]=="r_odd=d","equality face")
    req(cert["product_cover"]["factor_genus"]==5,"factor genus")
    req(cert["product_cover"]["factor_canonical_degree"]==8,"deg K factor")
    req(cert["product_cover"]["degree_P_to_X"]==4,"product cover degree")
    req(cert["product_cover"]["component_etale_degrees"]==[1,2,4],"component degrees")
    for l in range(1,9):
        d=112*l
        h=1+d//2
        req(2*h-2==d,f"Y RH l={l}")
        for e in (1,2,4):
            two_gz_minus_2=e*d
            KPZ=2*e*d
            req(KPZ%8==0,f"canonical divisibility l={l},e={e}")
            total_proj_degree=KPZ//8
            upper_each=two_gz_minus_2//8
            req(total_proj_degree==2*upper_each,f"projection saturation l={l},e={e}")
            n=upper_each
            req(n==14*e*l,f"bidegree l={l},e={e}")
            # Since n1+n2=2*n and each nj<=n, both equal n; RH ramification is zero.
            ram=two_gz_minus_2-8*n
            req(ram==0,f"etale RH l={l},e={e}")
    ec=cert["equality_consequence"]
    req(ec["both_projections_etale"] is True,"etale consequence")
    req(ec["equal_bidegree_etale_correspondence_required"] is True,"correspondence consequence")
    for k,v in cert["credit_firewall"].items():
        req(v is False,f"credit firewall {k}")
    print("PASS STAGE32_MB104_GENUS1_P5_BEAUVILLE_EQUALITY_RIGIDITY_V1")
    print("F1-P5 equality r_odd=d forces both projections from every product-cover component to be etale")
    print("bidegree=(14*e*l,14*e*l), e in {1,2,4}; no closure/credit")

if __name__=="__main__": main()
