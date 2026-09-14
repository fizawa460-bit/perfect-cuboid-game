#!/usr/bin/env python3
import hashlib, json, math
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-P5-ETALE-CORRESPONDENCE-CUSP-WIDTH-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-ETALE-CORRESPONDENCE-CUSP-WIDTH-OBSTRUCTION.md","7c554e689bffe2c1644ad15bc04d1c2d2c0a9dfe"),
 "EQUALITY_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json","62a2d01447016731001d35cc5915880daa2bfada"),
 "PRODUCT_SOURCE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-PRODUCT-COVER-SOURCE-NOTE.md","974c6cfecb6e4141615583841a0c90146ad2b4a6"),
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
    d=p.read_bytes()
    return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()

def preflight(cert):
    dec={x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    req(dec==LOCKS,"source-lock table")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel
        if not p.is_file(): raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got=blob(p)
        if got!=sha: raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")

def load_locked(k):
    return json.loads((root()/LOCKS[k][0]).read_text())

def cusp_det_lemma(a,b,c,d):
    D=a*d-b*c
    req(D>0,"positive determinant")
    req(math.gcd(math.gcd(abs(a),abs(b)),math.gcd(abs(c),abs(d)))==1,"primitive A")
    req(all(v%D==0 for v in (a*a,a*c,c*c,b*b,b*d,d*d)),"cusp divisibilities")
    x=math.gcd(abs(a),abs(c)); y=math.gcd(abs(b),abs(d))
    req(x>0 and y>0,"nonzero columns")
    req(D%(x*y)==0,"column gcd factorization")
    delta=D//(x*y)
    req(y*abs(delta)<=x and x*abs(delta)<=y,"divisibility inequalities")
    req(abs(delta)==1 and x==y==1 and D==1,"primitive consequence Delta=1")
    return True

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_GENUS1_P5_ETALE_CORRESPONDENCE_CUSP_WIDTH_V1","schema")
    preflight(cert)
    eq=load_locked("EQUALITY_CERT")
    req(eq["product_cover"]["factor_genus"]==5,"factor genus")
    req(eq["equality_consequence"]["both_projections_etale"] is True,"compact etale upstream")
    req(eq["equality_consequence"]["projection_degrees"]=="n1=n2=e*d/8=14*e*l","degree formula")
    req(eq["product_cover"]["component_etale_degrees"]==[1,2,4],"allowed e")

    up=cert["upstream"]
    req(up["projection_degree"]=="14*e*l" and up["l_min"]==1,"degree target")
    req(up["allowed_e"]==[1,2,4],"e set")
    req(up["Z_normalization_of_product_component_required"] is True,"normalization-image audit gate")

    ur=cert["uniformization_reduction"]
    req(ur["pair_generic_degree_one_forces_Lambda_eq_Lambda0"] is True,"pair degree reduction")
    req(ur["g_commensurates_Gamma"] is True and ur["g_projectively_rational"] is True,"commensurator reduction")

    cw=cert["cusp_width_lemma"]
    req(cw["U_infinity"]==[[1,8],[0,1]],"U infinity")
    req(cw["U_zero"]==[[1,0],[-8,1]],"U zero")
    req(cw["primitive_consequence"]=="Delta=1","determinant conclusion")

    for A in ((1,0,0,1),(1,1,0,1),(1,0,1,1),(2,1,1,1)):
        a,b,c,d=A
        D=a*d-b*c
        if D==1 and D>0:
            cusp_det_lemma(a,b,c,d)
    bad=(2,0,0,1)
    a,b,c,d=bad; D=a*d-b*c
    req(not all(v%D==0 for v in (a*a,a*c,c*c,b*b,b*d,d*d)),"diag(2,1) rejected by two-cusp packet")

    co=cert["consequence"]
    req(co["projection_degree_forced"]==1,"forced degree one")
    req(co["required_projection_degree_min"]==14,"required degree >=14")
    req(co["uniform_F1_P5_equality_realization_possible"] is False,"candidate contradiction")

    gate=cert["audit_gate"]
    req(gate["hostile_audit_required"] is True and gate["state_promotion_done"] is False,"candidate-only gate")
    fw=cert["credit_firewall"]
    req(fw["candidate_uniform_F1_P5_equality_closed"] is True,"candidate closure")
    req(fw["retained_uniform_F1_P5_equality_closed"] is False,"not yet promoted")
    req(fw["MB104_complete"] is False and fw["merge_authorized"] is False,"credit firewall")

    print("PASS STAGE32_MB104_GENUS1_P5_ETALE_CORRESPONDENCE_CUSP_WIDTH_V1")
    print("candidate: compact etale + product birationality => commensurator cusp widths force degree 1")
    print("audit gate: normalization-image, compact-cusp etale, PSL sign interface must be hostile-audited before promotion")

if __name__=="__main__":
    main()
