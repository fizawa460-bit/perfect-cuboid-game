#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-P5-SIX-BRANCH-HURWITZ-PASSPORT-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-SIX-BRANCH-HURWITZ-PASSPORT.md","d421c11ecd6577234823b6e9604c8cc99ce48fec"),
 "FULL_DECK_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-FULL-DECK-STABILIZER-RIGIDITY-CERTIFICATE.json","1c03b78456a704e50f8af0640e1d23dc36948a3c"),
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

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_GENUS1_P5_SIX_BRANCH_HURWITZ_PASSPORT_V1","schema")
    preflight(cert)
    req(cert["status"].startswith("REPAIRED_"),"repaired status")
    req(8 == 8*(-2)+3*8,"C8/G RH")
    for l in range(1,9):
        n=56*l
        total_r=2*n
        total_u=6*n-2*total_r
        req(total_r==112*l,"total ramification")
        req(total_u==112*l,"unramified capacity")
        u_pairs=(40*l,40*l,32*l)
        r_pairs=tuple((2*n-u)//2 for u in u_pairs)
        req(r_pairs==(36*l,36*l,40*l),"pair ramification totals")
        req(sum(u_pairs)==total_u and sum(r_pairs)==total_r,"capacity sums")
    re=cert["retraction"]
    req(re["u_q_divisible_by_8l_claimed"] is False,"no 8l divisibility")
    req(re["per_node_all_branches_same_branch_value_claimed"] is False,"no per-node concentration")
    req(re["finite_six_integer_passport_retained"] is False,"finite split retracted")
    req(cert["frontier"]["old_5_5_4_support_is_current_survivor"] is False,"non-frontier")
    for k,v in cert["credit_firewall"].items(): req(v is False,f"firewall {k}")
    print("PASS STAGE32_MB104_GENUS1_P5_SIX_BRANCH_HURWITZ_PASSPORT_V1_REPAIRED")
    print("historical (5,5,4) support: capacity equality retained; per-node 8l concentration and finite split retracted")

if __name__=="__main__": main()
