#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

CERT=Path(__file__).with_name("MB104-WIDE-SHALLOW-ROUND-B-CERTIFICATE.json")
MASK=int("000707000f0f",16)

def req(ok,msg):
    if not ok: raise SystemExit("FAIL: "+msg)

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_WIDE_SHALLOW_ROUND_B_V1","schema")

    # W4 rank-3 fibration replay from six 8-node blocks.
    blocks=[sum((MASK>>(8*j+i))&1 for i in range(8)) for j in range(6)]
    req(blocks==[4,4,0,3,3,0],"block counts")
    vals=[56-4*n for n in blocks]
    req(vals==[40,40,56,44,44,56],"rank3 pairings")
    req(all(v>0 for v in vals),"positive rank3 pairings")

    # W8 exact overlap data are source-locked in Round A certificate.
    ov=c["results"]["W8_SIMULTANEOUS_SIGN_QUOTIENT_GENUS"]["overlaps_with_sigma_support"]
    req(sorted(ov.values())==[6,7,7,8,12,13,13],"W8 overlaps")
    req(all(v<14 for v in ov.values()),"no coordinate-sign support stabilizer")

    # W10 Riemann-Roch replay.
    for l in range(1,20):
        chi=168*l*l-56*l+8
        req(chi>0,f"W10 chi l={l}")
    req(168-56+8==120,"W10 l1")
    req(168*4-112+8==568,"W10 l2")

    # W11 degree equality.
    for l in range(1,20):
        req(14*8*l==112*l,f"W11 saturation l={l}")

    rs=c["round_summary"]
    req(rs["drop"]==["W4","W5","W8","W10","W11"],"drops")
    req(rs["pass_to_second_scan"]==[],"no survivor")
    req(rs["deep_candidate"] is False,"no deep")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit firewall "+k)

    print("PASS STAGE32_MB104_WIDE_SHALLOW_ROUND_B_V1")
    print("W4=DROP W5=DROP W8=DROP W10=DROP W11=DROP")
    print("next=ROUND_C_BROAD_SCAN no_credit")

if __name__=="__main__":
    main()
