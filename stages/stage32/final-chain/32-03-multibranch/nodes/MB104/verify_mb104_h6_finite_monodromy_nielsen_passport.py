#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-H6-FINITE-MONODROMY-NIELSEN-PASSPORT-CERTIFICATE.json")

LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-UNIFORM-CLOSURE-RESTART-20260917.md":"3e9fb440ea8a9c491ad58c9846d880fbd3373f66",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-CLASS3-ROADMAP-20260918.md":"3e21d1c1a7f5d388f2fe524bf91d27947c55d888",
}

def blob(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def req(ok,msg):
    if not ok:
        raise SystemExit("FAIL: "+msg)

def main():
    for rel,expected in LOCKS.items():
        p=ROOT/rel
        req(p.is_file(),"missing "+rel)
        req(blob(p)==expected,"source drift "+rel)

    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_H6_FINITE_MONODROMY_NIELSEN_PASSPORT_GATE_V1","schema")
    req(c["status"]=="H6_SHALLOW_FAIL_PARKED_NO_CREDIT","status")

    # Exact aggregate family replay.
    for l in range(1,9):
        n=28*l
        count=0
        for i in range(0,12*l+1):
            ua=4*l+2*i
            uma=28*l-2*i
            req(0<=ua<=n and 0<=uma<=n,f"a bounds l={l} i={i}")
            req(ua+uma==32*l,f"a total l={l} i={i}")
            req(ua%2==0 and uma%2==0,f"a parity l={l} i={i}")
            req((ua//2)%2==(uma//2)%2,f"a sign parity l={l} i={i}")
            for j in range(0,12*l+1):
                ub=2*j
                umb=24*l-2*j
                req(0<=ub<=n and 0<=umb<=n,f"b bounds l={l} j={j}")
                req(ub+umb==24*l,f"b total l={l} j={j}")
                req(ub%2==0 and umb%2==0,f"b parity l={l} j={j}")
                req((ub//2)%2==(umb//2)%2,f"b sign parity l={l} j={j}")
                u=[ua,uma,ub,umb,n,n,0,0]
                req(sum(u)==112*l,f"sum u l={l}")
                r=[(n-x)//2 for x in u]
                req(all((n-x)%2==0 and y>=0 for x,y in zip(u,r)),f"r integral l={l}")
                req(sum(r)==56*l,f"sum r l={l}")
                count+=1
        req(count==(12*l+1)**2,f"count l={l}")

    fam=c["explicit_interface_admissible_family"]
    req(fam["distinct_aggregate_cycle_type_count"]=="(12*l+1)^2","family count")
    req(fam["grows_unboundedly_with_l"] is True,"unbounded family")
    req(fam["actual_cover_realization_claimed"] is False,"no existence overclaim")

    a=c["adapters"]
    req(a["aggregate_packet_to_l_independent_finite_nielsen_object"]=="FAIL","finite adapter")
    req(a["reverse_adapter"]=="FAIL","reverse adapter")

    d=c["decision"]
    req(d["shallow_gate"]=="FAIL","H6 fail")
    req(d["roadmap_action"]=="PARK_H6","H6 parked")
    req(d["cycle_2_status"]=="COMPLETE_NO_DEEP_CANDIDATE","cycle2")
    req(d["next_shallow_gate"]=="H9_UNIFORM_STABLE_BASE_ZARISKI_RAY","H9 next")
    req(d["finite_degree_window_proved"] is False,"no finite window")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit firewall "+k)

    print("PASS STAGE32_MB104_H6_FINITE_MONODROMY_NIELSEN_PASSPORT_GATE_V1")
    print("H6=FAIL_PARKED aggregate_cycle_types>=(12*l+1)^2 reverse_adapter=FAIL")
    print("cycle2=complete next=H9_uniform_stable_base_zariski_ray no_credit")

if __name__=="__main__":
    main()
