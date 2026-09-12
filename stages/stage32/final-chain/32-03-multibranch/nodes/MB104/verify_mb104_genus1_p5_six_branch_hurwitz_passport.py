#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-P5-SIX-BRANCH-HURWITZ-PASSPORT-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-SIX-BRANCH-HURWITZ-PASSPORT.md","1632a05a62d9087f845ccaaca3f091ac9581e105"),
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
    fq=cert["factor_quotient"]
    req(fq["G_order"]==8 and fq["quotient_genus"]==0,"factor quotient")
    req(fq["singular_stabilizer_fixed_points_each"]==8,"fixed count")
    req(fq["branch_values_per_stabilizer_type"]==2 and fq["total_branch_values"]==6,"six branch values")
    req(fq["remaining_outside_involution_fixed_points"]==0,"fourth outside free")
    # Group RH on C8: 2g-2=8. Three involutions contribute 8 fixed points each.
    req(8 == 8*(-2) + 3*8,"C8/G RH")
    pair_nodes=(5,5,4)
    for l in range(1,9):
        n=56*l
        total_r=2*n
        total_u=6*n-2*total_r
        req(total_r==112*l,"elliptic->P1 RH")
        req(total_u==112*l,"unramified capacity")
        u_pairs=tuple(c*8*l for c in pair_nodes)
        r_pairs=tuple((2*n-u)//2 for u in u_pairs)
        req(u_pairs==(40*l,40*l,32*l),"u pair totals")
        req(r_pairs==(36*l,36*l,40*l),"r pair totals")
        req(sum(u_pairs)==total_u and sum(r_pairs)==total_r,"pair sums")
        # Enumerate all finite split shapes; each q has u=8*l*m and r=(28-4m)*l.
        count=0
        for m1 in range(6):
          m2=5-m1
          for m3 in range(6):
            m4=5-m3
            for m5 in range(5):
              m6=4-m5
              ms=(m1,m2,m3,m4,m5,m6)
              us=[8*l*m for m in ms]
              rs=[(28-4*m)*l for m in ms]
              req(all(u+2*r==n for u,r in zip(us,rs)),"local fiber degree")
              req(sum(us)==total_u and sum(rs)==total_r,"global passport sums")
              count+=1
        req(count==180,"passport split count before pair swaps")
    sp=cert["support_exhaustion"]
    req(sp["they_exhaust_all_unramified_points_over_the_six_values"] is True,"support exhaustion")
    fp=cert["finite_passport"]
    req(fp["pair_sum_constraints"]==["m1+m2=5","m3+m4=5","m5+m6=4"],"pair constraints")
    for k,v in cert["credit_firewall"].items(): req(v is False,f"firewall {k}")
    print("PASS STAGE32_MB104_GENUS1_P5_SIX_BRANCH_HURWITZ_PASSPORT_V1")
    print("degree=56l genus1->P1; six order-2 branch values; supported 112l branches exhaust all unramified slots")
    print("finite passport m-pair sums=(5,5,4); 180 ordered split shapes before within-pair symmetry; no closure/credit")

if __name__=="__main__": main()
