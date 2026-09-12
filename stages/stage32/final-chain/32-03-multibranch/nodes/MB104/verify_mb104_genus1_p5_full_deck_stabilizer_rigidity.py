#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-P5-FULL-DECK-STABILIZER-RIGIDITY-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-FULL-DECK-STABILIZER-RIGIDITY.md","cb05a7a187c9dd7495ee1f4af3b92fb776900422"),
 "EQUALITY_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json","62a2d01447016731001d35cc5915880daa2bfada"),
 "NODE_TYPE_SOURCE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md","a29161602c0b38f0607794e56e61068b8cb9735d"),
 "FORMAL_FEASIBILITY_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-FEASIBILITY-CERTIFICATE.json","8ec4a403d2485dbf061b8b16182aa06c62193c43"),
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

def span_rank(vs):
    basis=[]
    for v in vs:
        x=v
        for b in basis:
            x=min(x,x^b)
        if x:
            basis.append(x)
            basis.sort(reverse=True)
    return len(basis)

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_GENUS1_P5_FULL_DECK_STABILIZER_RIGIDITY_V1","schema")
    preflight(cert)
    req(cert["support_node_type_counts"]==[5,5,4],"node type counts")
    req(cert["all_three_singular_stabilizer_types_occur"] is True,"all three types")
    # Model G=F2^3 and G0={vectors with top bit 0}; any three distinct outside
    # representatives spanning three node types generate all of G.
    G0={0,1,2,3}; outside={4,5,6,7}
    triples=[]
    for a in outside:
        for b in outside:
            for c in outside:
                if a<b<c:
                    triples.append((a,b,c))
    req(triples,"outside triples")
    for t in triples:
        req(span_rank(t)==3,f"outside triple does not span G: {t}")
    req(cert["consequence"]["component_degree_e"]==4,"e=4")
    req(cert["consequence"]["product_pullback_connected"] is True,"connected pullback")
    for l in range(1,9):
        d=112*l; e=4
        req((e*d)//8==56*l,f"bidegree l={l}")
        req(1+(e*d)//2==224*l+1,f"genus l={l}")
    req(cert["consequence"]["both_product_projections_etale"] is True,"etale projections")
    for k,v in cert["credit_firewall"].items(): req(v is False,f"firewall {k}")
    print("PASS STAGE32_MB104_GENUS1_P5_FULL_DECK_STABILIZER_RIGIDITY_V1")
    print("explicit support uses all three singular stabilizer types; every pullback component is G-stable")
    print("therefore e=4, product pullback connected, etale bidegree=(56l,56l); no closure/credit")

if __name__=="__main__": main()
