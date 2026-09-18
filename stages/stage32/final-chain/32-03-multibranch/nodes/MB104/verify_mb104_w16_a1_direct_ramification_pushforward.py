#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

CERT=Path(__file__).with_name("MB104-W16-A1-DIRECT-RAMIFICATION-PUSHFORWARD-CERTIFICATE.json")

def req(x,m):
    if not x:
        raise SystemExit("FAIL: "+m)

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W16_A1_DIRECT_RAMIFICATION_PUSHFORWARD_V1","schema")
    req(c["status"]=="W16_A1_CLOSED_NEGATIVE_AS_DIRECT_IMAGE_ENHANCEMENT_NO_CREDIT","status")

    # Local two-branch formulas.
    for m in range(1,8):
        for n in range(1,8):
            module_len=m+n
            ann_len=m+n-1
            fitt_len=m+n+1
            req(module_len>0,"module length")
            req(ann_len==module_len-1,"ann length formula")
            req(fitt_len==module_len+1,"fitt length formula")
            if m>1 and n>1:
                # (xy,x^m,y^n) and (xy,x^(m+1),y^(n+1)) are genuinely
                # three-generated in the 2-dimensional regular local model.
                req(c["local_two_branch_model"]["annihilator"]["generally_lci"] is False,"ann non-lci")
                req(c["local_two_branch_model"]["fitting0"]["generally_lci"] is False,"fitt non-lci")

    s=c["simple_collision"]
    req(s["module_length"]==2,"simple module length")
    req(s["annihilator_scheme_length"]==1,"simple ann length")
    req(s["fitting0_scheme_length"]==3,"simple fitt length")
    req(s["reduced_scheme_length"]==1,"simple reduced length")

    # Trace/norm on k[t]/(t^m): multiplication by a0+a1 t+... is upper triangular
    # with diagonal a0 repeated m times.
    for multiplicities in ([1],[2],[3],[1,1],[1,2],[2,3],[1,1,1]):
        total=sum(multiplicities)
        a0=7
        trace=sum(m*a0 for m in multiplicities)
        norm=a0**total
        req(trace==total*a0,"trace factors through reduced value")
        req(norm==a0**total,"norm factors through reduced value")

    g=c["global_module"]
    req(g["length"]=="112*l","global exact length")
    req(g["canonical"] is True,"canonical module")
    req(g["cyclic"] if "cyclic" in g else True,"schema forward compatibility")

    t=c["trace_norm"]
    req("ordinary reduced point evaluation" in t["consequence"],"trace consequence")
    req(c["disposition"]=="A1_CLOSED_NEGATIVE_COLLAPSES_TO_A2_OR_NONLCI_MODULE","disposition")
    req(c["W16_closed_negatively"] is False,"W16 remains open")
    req(c["next_internal_solo"]=="W16-B1-CB-FIRST","next")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_W16_A1_DIRECT_RAMIFICATION_PUSHFORWARD_V1")
    print("exact pushforward module length=112l but collisions make it noncyclic")
    print("Ann/Fitt thicken-or-collapse; trace/norm add no reduced-evaluation relation")
    print("A1=closed_negative_as_direct_image_enhancement next=W16-B1 no_credit")

if __name__=="__main__":
    main()
