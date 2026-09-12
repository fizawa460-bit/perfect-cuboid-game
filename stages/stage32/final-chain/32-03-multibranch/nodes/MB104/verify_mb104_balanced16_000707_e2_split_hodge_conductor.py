#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-SPAN5-BALANCED16-000707-E2-SPLIT-HODGE-CONDUCTOR-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SPLIT-HODGE-CONDUCTOR.md","b8f876f78fa23a64911baa4b9057f7920bfea014"),
 "HALF_BRANCH_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS-CERTIFICATE.json","28929222eb46b9d30be4fed9218143aa5fecaa78"),
 "PRIMITIVE_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK-CERTIFICATE.json","c906de3f73f909f80f9d99e515a5161ee5f41905"),
 "STOLL_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-CANONICAL-C0-SOURCE-NOTE.md","e344290d5241c3f7f165ea3027cfc778abec3360"),
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
    req(dec==LOCKS,"source-lock table")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel
        if not p.is_file(): raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got=blob(p)
        if got!=sha: raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")

def load(k): return json.loads((root()/LOCKS[k][0]).read_text())

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_BALANCED16_000707_E2_SPLIT_HODGE_CONDUCTOR_V1","schema")
    preflight(cert)
    hb=load("HALF_BRANCH_CERT")
    pc=load("PRIMITIVE_CERT")

    req(hb["scope"]["mask"]=="000707000f0f" and hb["scope"]["allowed_e"]==[2,4],"half-branch scope")
    req(hb["half_branch"]["relation"]=="2*L_abs ~ B_abs","half-branch relation")
    req(hb["carrier_restriction"]["carrier_disjoint_from_B_abs"] is True,"carrier avoids branch")
    req(hb["carrier_restriction"]["e2_iff_eta_zero"] is True,"e2 split-normalization criterion")
    req(pc["support"]["primitive_class"]=="A=7H-4*sum_{p in Sigma}E_p","primitive class")
    req(pc["support"]["multiple_class"]=="D_l=l*A, l>=1","multiple class")

    # Recompute D_l^2 and K.D_l from H^2=16, E_i^2=-2, H.E_i=0, |Sigma|=14, K=H.
    A2=7*7*16 + 14*(4*4)*(-2)
    KA=7*16
    req(A2==336 and KA==112,"primitive intersections")

    ia=cert["intersection_arithmetic"]
    req(ia["D_l_square"]=="336*l^2" and ia["K_dot_D_l"]=="112*l","certificate intersections")
    req(ia["C1_square"]=="336*l^2-y" and ia["difference_square"]=="672*l^2-4*y","component arithmetic")

    # Hodge: 672 l^2 - 4y <= 0 => y >= 168 l^2.
    hc=cert["hodge_consequence"]
    req(hc["difference_orthogonal_to_pullback_ample"] is True and hc["difference_square_nonpositive"] is True,"Hodge hypotheses/consequence")
    req(hc["y_lower_bound"]=="168*l^2","Hodge lower bound")
    req(672//4==168,"Hodge coefficient")

    # Adjunction and genus-one normalization.
    # p_a=1+(336 l^2+112 l)/2 = 168 l^2+56 l+1.
    cb=cert["conductor_budget"]
    req(cb["arithmetic_genus"]=="168*l^2+56*l+1","arithmetic genus")
    req(cb["total_delta"]=="168*l^2+56*l","delta budget")
    req(cb["etale_pullback_total_normalization_defect"]=="336*l^2+112*l","double defect")
    req(cb["formula"]=="2*Delta(C)=2*delta_same+y","defect decomposition")
    req(cb["cross_sheet_delta_lower_bound"]=="y/2 >= 84*l^2","cross-sheet lower bound")
    req(cb["same_sheet_delta_upper_bound"]=="delta_same <= 84*l^2+56*l","same-sheet upper bound")

    sp=cert["split_normalization"]
    req(sp["normalization_components"]==2 and sp["global_irreducible_components"]==2,"two components after split normalization")
    req(sp["singular_curve_may_remain_connected"] is True,"conductor gluing firewall")

    fw=cert["credit_firewall"]
    req(fw["e2_closed"] is False and fw["e4_closed"] is False and fw["orbit_000707_closed"] is False,"no closure")
    req(fw["MB104_complete"] is False and fw["merge_authorized"] is False,"credit firewall")

    print("PASS STAGE32_MB104_BALANCED16_000707_E2_SPLIT_HODGE_CONDUCTOR_V1")
    print("e=2 split normalization forces cross-component intersection y >= 168*l^2")
    print("equivalently y/2 >= 84*l^2 of the downstairs delta budget is cross-sheet")
    print("firewall: this is a constraint, not an e=2 closure")

if __name__=="__main__": main()
