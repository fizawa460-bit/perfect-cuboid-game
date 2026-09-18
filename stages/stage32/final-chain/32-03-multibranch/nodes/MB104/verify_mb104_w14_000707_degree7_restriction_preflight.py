#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=Path(__file__).resolve().parents[6]
CERT=HERE/"MB104-W14-000707-DEGREE7-RESTRICTION-PREFLIGHT-CERTIFICATE.json"
HIST=HERE/"verify_mb104_balanced16_size48_degree7_restriction_rank.py"

LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_size48_degree7_restriction_rank.py":
"bca311f6ad643a3ee8a803871119e9d71e4b2ab0",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-NULL-UNION-COHOMOLOGY-CERTIFICATE.json":
"e7c5be93372f653bb42d8528ab68bcfaa4d6de60",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json":
"31695c6908cff73d04baab2ed11dfd04608a2464",
}

def blob(path):
    d=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()

def req(ok,msg):
    if not ok: raise SystemExit("FAIL: "+msg)

def load_hist():
    spec=importlib.util.spec_from_file_location("mb104_size48_rank",HIST)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main():
    for rel,sha in LOCKS.items():
        p=ROOT/rel
        req(p.is_file(),"missing "+rel)
        req(blob(p)==sha,"source drift "+rel)

    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W14_000707_DEGREE7_RESTRICTION_PREFLIGHT_V1","schema")
    m=load_hist()
    S=m.from_mask("000707000f0f")
    req(len(S)==14,"support size")

    q0=tuple(c["finite_field"]["q0_point"])
    q1=tuple(c["finite_field"]["q1_point"])
    req(m.on_surface(q0) and m.on_surface(q1),"quartic points on surface")
    req(not any(m.peq(q0,n) for n in m.V),"q0 away from nodes")
    req(not any(m.peq(q1,n) for n in m.V),"q1 away from nodes")

    # exact Q0/Q1 equations at p=1097
    a1,a2,a3,b1,b2,b3,cc=q0
    req(b1==0 and (m.II*a2-a3)%m.P==0 and (a1-cc)%m.P==0,"Q0 equations")
    a1,a2,a3,b1,b2,b3,cc=q1
    req(b2==0 and (m.II*a3+a1)%m.P==0 and (a2-cc)%m.P==0,"Q1 equations")

    rows=[]
    for idx in sorted(S):
        rows.extend(m.node_rows(m.V[idx]))
    R,piv=m.rref(rows)
    r0=len(piv)
    rq0=len(m.rref(R+[m.evalrow(q0)])[1])
    rq1=len(m.rref(R+[m.evalrow(q1)])[1])
    rq01=len(m.rref(R+[m.evalrow(q0),m.evalrow(q1)])[1])
    got=(r0,rq0,rq1,rq01)
    req(got==(220,221,221,221),"rank pattern")

    b=c["char0_bounds"]
    req(b["degree7_ambient_dimension"]==344 and b["chi_A"]==120,"RR constants")
    req(b["null_union_h1_lower_bound"]==3 and b["h2_A"]==0,"cohom bounds")
    req(b["h0_A_lower_bound"]==123,"h0 bound")
    req(b["exact_remaining_options"]==[220,221],"one-bit window")

    d=c["decision"]
    req(d["disposition"]=="PASS_TO_SECOND_SCAN","disposition")
    req(d["deep_candidate"] is False,"not deep")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit firewall "+k)

    print("PASS STAGE32_MB104_W14_000707_DEGREE7_RESTRICTION_PREFLIGHT_V1")
    print("p=1097 jet=220 q0=221 q1=221 both=221")
    print("char0_jet_rank in {220,221}; W14=SECOND_SCAN no_credit")

if __name__=="__main__":
    main()
