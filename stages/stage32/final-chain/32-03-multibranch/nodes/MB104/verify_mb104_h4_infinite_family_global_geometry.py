#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-H4-INFINITE-FAMILY-GLOBAL-GEOMETRY-CERTIFICATE.json")

def blob(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def req(ok,msg):
    if not ok: raise SystemExit("FAIL: "+msg)

def main():
    c=json.loads(CERT.read_text())
    for src in c["source_locks"]:
        p=ROOT/src["path"]
        req(p.is_file(),"missing "+src["path"])
        req(blob(p)==src["blob_sha1"],"source drift "+src["path"])

    req(c["schema"]=="STAGE32_MB104_H4_INFINITE_FAMILY_GLOBAL_GEOMETRY_GATE_V1","schema")
    req(c["status"]=="H4_SHALLOW_FAIL_PARKED_NO_CREDIT","status")

    # Exact ray arithmetic and Hilbert-polynomial nonconstancy.
    for l in range(1,9):
        self_int=336*l*l
        kint=112*l
        pa=1+(self_int+kint)//2
        req(pa==1+168*l*l+56*l,f"adjunction l={l}")
        # Use a symbolic positive A.D1=1; scaling by any fixed positive integer
        # preserves pairwise distinction of the polynomials.
        slope=l
        const=1-pa
        req((slope,const)==(l,-168*l*l-56*l),f"Hilbert data l={l}")
        req(self_int>0,f"not fiber l={l}")

    polys={(l,-168*l*l-56*l) for l in range(1,9)}
    req(len(polys)==8,"Hilbert polynomials must vary with l")

    tests=c["fixed_structure_tests"]
    req(tests["common_curve_component"]["result"]=="IMPOSSIBLE_FOR_DISTINCT_l","fixed component")
    req(tests["one_flat_family_across_l"]["result"]=="IMPOSSIBLE_WITH_FIXED_HILBERT_POLYNOMIAL","flat family")
    req(tests["fixed_fibration_as_fibers"]["result"]=="IMPOSSIBLE","fiber test")
    req(tests["fixed_fibration_as_multisections"]["result"]=="NOT_FORCED","multisection firewall")
    req(tests["bounded_finitely_generated_subsystem"]["result"]=="NOT_AVAILABLE","H2 firewall")

    dec=c["decision"]
    req(dec["shallow_gate"]=="FAIL","H4 fail")
    req(dec["roadmap_action"]=="PARK_H4","H4 parked")
    req(dec["h3_deep_release"] is False,"H3 unreleased")
    req(dec["next_cycle_order"]==[
        "H8_LOG_BOUNDARY_INEQUALITY",
        "H5_ETALE_CORRESPONDENCE_QUOTIENT_RIGIDITY",
        "H6_FINITE_MONODROMY_NIELSEN_PASSPORT"],"cycle2 order")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit firewall "+k)

    print("PASS STAGE32_MB104_H4_INFINITE_FAMILY_GLOBAL_GEOMETRY_GATE_V1")
    print("H4=FAIL_PARKED unbounded_Hilbert_Chow=true fixed_fiber=false")
    print("cycle1=complete deep_routes=0 next=H8,H5,H6 no_credit")

if __name__=="__main__":
    main()
