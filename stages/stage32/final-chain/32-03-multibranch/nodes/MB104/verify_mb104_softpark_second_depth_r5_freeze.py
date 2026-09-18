#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
CERT=Path(__file__).with_name("MB104-SOFTPARK-SECOND-DEPTH-R5-FREEZE-CERTIFICATE.json")
def req(x,m):
    if not x: raise SystemExit("FAIL: "+m)
def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R5_FREEZE_V1","schema")
    # W3 exact infinite-subsequence counterwitness arithmetic.
    req(c["W3"]["chi_A"]==200,"W3 chi")
    for k in range(1,100):
        req(896*(12*k)==1536*(7*k),f"W3 subsequence k={k}")
    # W7 retained H8 domination.
    req(c["W7"]["H8_uniform_slack_lower"]==147,"W7 H8 slack")
    req(c["W7"]["H8_coefficients_cover_all_cyclic_boundary_weights"] is True,"W7 coefficient coverage")
    # W9/W12 compactification routing.
    req(c["W9"]["proper_genus1_compactification_available_in_principle"] is True,"W9 compactification")
    req(c["W9"]["ghost_boundary_present"] is True,"W9 ghost boundary")
    req(c["W12"]["proper_main_component_compactification_available"] is True,"W12 compactification")
    req(c["W12"]["explicit_packet_preserving_degeneration_available"] is False,"W12 missing degeneration")
    # W25 exact pencil invariants and slope compatibility.
    for l in range(1,100):
        g=1+168*l*l+56*l
        Kf2=1008*l*l+448*l+16
        chif=168*l*l+56*l+8
        ef=12*chif-Kf2
        Delta=g-1
        req(ef==1008*l*l+224*l+80,f"W25 ef l={l}")
        req(ef-Delta==840*l*l+168*l+80 and ef>Delta,f"W25 budget l={l}")
        req(Kf2*g > 4*(g-1)*chif,f"W25 slope l={l}")
    # Portfolio exact partition of all 26 broader-soft W labels.
    p=c["portfolio"]
    soft=set(p["broader_soft"])
    classified=set(p["third_depth"])|set(p["high_reserve"])|set(p["reserve"])|set(p["park"])
    req(len(soft)==26,"26 broader soft")
    req(classified==soft,"portfolio partition")
    req(len(set(p["third_depth"]) & set(p["reserve"]))==0,"no overlap")
    req(p["third_depth"]==["W4","W16","W20"],"third-depth set")
    req(p["next_third_depth_order"]==["W4","W20","W16"],"execution order")
    for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
    print("PASS STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R5_FREEZE_V1")
    print("third_depth=W4,W16,W20 high_reserve=W5 reserve=W12,W13,W17,W23")
    print("next_third_depth_order=W4,W20,W16")
    print("second_depth_portfolio=frozen no_credit")
if __name__=="__main__": main()
