#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md","e22de5a6f4be163268e699cde03d37e1e564d43b"),
 "RESIDUAL_CHARACTER_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER-CERTIFICATE.json","5e12d24f85d1fe27e53edab337bbacc45fb34cdb"),
 "ABSENT_HALF_FIBER_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ABSENT-HALF-FIBER-PICARD-CERTIFICATE.json","a27445aff8191cf81582ba7ab5a8d985e01bb577"),
 "FIBRATION_SOURCE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md","b71225ac859eef5afefeebd019a97c403ed27655"),
 "SECTION_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16-CERTIFICATE.json","9c36555e495df0d8d6b816f1c0dc7d4c35b55848"),
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
    req(cert["schema"]=="STAGE32_MB104_BALANCED16_000707_ONE_FACTOR_HALF_BRANCH_CLASS_V1","schema")
    preflight(cert)
    rc=load("RESIDUAL_CHARACTER_CERT")
    hf=load("ABSENT_HALF_FIBER_CERT")
    sec=load("SECTION_CERT")

    req(rc["scope"]["mask"]=="000707000f0f" and rc["scope"]["node_type_counts"]==[7,7,0],"upstream scope")
    req(rc["scope"]["allowed_e"]==[2,4],"upstream e cases")
    req(rc["case_classification"]["e2_eta_zero"] is True and rc["case_classification"]["e4_eta_nonzero"] is True,"eta case classification")
    req(hf["half_fiber_relation"]["formula"]=="2*(Q_a-Q_b) ~ sum_(p in T_b)E_p - sum_(p in T_a)E_p","half-fiber relation")
    req(hf["carrier_restriction"]["integral_carrier_disjoint_from_absent_exceptionals"] is True,"carrier avoids absent exceptionals")
    req(sec["incidence16_size3"]["section"]=="4 smooth elliptic quartics","four G2 quartics in b_j=0 section")
    req(sec["incidence16_size3"]["node_component_incidence"]=="each of 16 section nodes lies on exactly two quartics","node incidence")

    hb=cert["half_branch"]
    req(hb["T_a_size"]==8 and hb["T_b_size"]==8 and hb["T_a_T_b_disjoint"] is True,"8+8 partition")
    req(hb["absent_nodes_total"]==16 and hb["relation"]=="2*L_abs ~ B_abs","half-branch relation")

    # Numerical consequences of B_abs = sum of 16 disjoint (-2)-curves and 2L_abs=B_abs.
    B2=16*(-2)
    L2=B2//4
    req(B2==-32 and L2==-8,"B_abs/L_abs squares")
    n=cert["numerics"]
    req(n["B_abs_square"]==-32 and n["L_abs_square"]==-8,"certificate squares")
    req(n["H_dot_L_abs"]==0 and n["K_dot_L_abs"]==0 and n["D_l_dot_L_abs"]==0,"orthogonality")
    req(n["L_abs_dot_each_absent_exceptional"]==-1,"branch-half exceptional pairing")

    cr=cert["carrier_restriction"]
    req(cr["carrier_disjoint_from_B_abs"] is True and cr["eta"]=="O_E(L_abs|_E)","restriction class")
    req(cr["e2_iff_eta_zero"] is True and cr["e4_iff_eta_nonzero"] is True,"case classification")

    wall=cert["route_wall"]
    req(wall["pure_numerical_Picard_pairings_decide_eta_zero_vs_nonzero"] is False,"numerical wall")
    req(wall["surface_cohomology_without_normalization_conductor_adapter_sufficient"] is False,"conductor caveat")

    fw=cert["credit_firewall"]
    req(fw["e2_closed"] is False and fw["e4_closed"] is False and fw["orbit_000707_closed"] is False,"no closure")
    req(fw["MB104_complete"] is False and fw["merge_authorized"] is False,"credit firewall")

    print("PASS STAGE32_MB104_BALANCED16_000707_ONE_FACTOR_HALF_BRANCH_CLASS_V1")
    print("2L_abs=B_abs (16 absent exceptional curves); L_abs^2=-8 and eta=O_E(L_abs|_E)")
    print("numerical Picard pairings alone cannot distinguish eta=0 from eta!=0")
    print("firewall: e=2,e=4 and 000707 remain open")

if __name__=="__main__": main()
