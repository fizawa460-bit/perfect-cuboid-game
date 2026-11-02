#!/usr/bin/env python3
import json
from pathlib import Path
from sympy import Matrix

def req(x,msg):
    if not x:
        raise SystemExit("FAIL: "+msg)

def main():
    p=Path(__file__).with_name("MB104-000707-GENUS7-FIBRATION-CERTIFICATE.json")
    d=json.loads(p.read_text())
    req(d["schema"]=="STAGE32_MB104_000707_GENUS7_FIBRATION_V1","schema")

    M=Matrix([
      [-4, 2, 0, 0, 1, 1, 0, 0, 0, 0],
      [ 2,-4, 0, 0, 0, 0, 1, 1, 0, 0],
      [ 0, 0,-4, 0, 0, 1, 0, 1, 1, 1],
      [ 0, 0, 0,-4, 1, 0, 1, 0, 1, 1],
      [ 1, 0, 0, 1,-2, 0, 0, 0, 0, 0],
      [ 1, 0, 1, 0, 0,-2, 0, 0, 0, 0],
      [ 0, 1, 0, 1, 0, 0,-2, 0, 0, 0],
      [ 0, 1, 1, 0, 0, 0, 0,-2, 0, 0],
      [ 0, 0, 1, 1, 0, 0, 0, 0,-2, 0],
      [ 0, 0, 1, 1, 0, 0, 0, 0, 0,-2],
    ])
    one=Matrix([1]*10)
    req(M*one==Matrix.zeros(10,1),"positive kernel")
    req(M.rank()==9,"corank one")
    req((one.T*M*one)[0]==0,"square zero")

    H=[4,4,2,2,0,0,0,0,0,0]
    P=[0,0,14,6,8,0,8,0,0,0]
    req(sum(H)==12,"H degree")
    req(sum(P)==36,"P degree")
    req(1+12//2==7,"genus")

    pos={0,1,2,3,8,9,10,11,24,25,30,31,32,33,38,39}
    blocks=[set(range(0,8)),set(range(8,16)),set(range(16,24)),
            set(range(24,32)),set(range(32,40)),set(range(40,48))]
    pair=[(12-len(pos&B))//2 for B in blocks]
    req(pair==[4,4,6,4,4,6],"rank3 pairings")

    a=d["degree10_audit"]
    req(a["quartic_conic"]["total"]==1920,"quartic-conic total")
    req(a["quartic_conic"]["moving_pencil"]==0,"quartic-conic moving")
    req(a["distinct_three_conics"]["total"]==4960,"conic triple total")
    req(a["distinct_three_conics"]["moving_pencil"]==96,"moving triples")
    prof={r["M"]:(r["count"],r["P_dot"]) for r in a["moving_profile"]}
    req(prof=={0:(1,70),1:(6,66),2:(27,62),3:(28,58),4:(34,54)},"degree10 profile")
    req(sum(v[0] for v in prof.values())==96,"moving count")

    req(d["fiber"]["H_dot"]==12 and d["fiber"]["P_dot"]==36,"fiber fields")
    req(d["fiber"]["basepoint_free"] is True,"basepoint free")
    req(d["fiber"]["primitive_fiber_class"] is True,"primitive")
    req(d["size768_global_fibration_minimum"]==36,"global minimum")
    req(all(v is False for v in d["firewalls"].values()),"credit firewall")

    print("PASS: 000707 genus-7 fibration certificate")
    print("G^2=0 H.G=12 P.G=36 genus=7")
    print("rank3 pairings",pair)
    print("size768 global fibration minimum 36 (pre-audit)")

if __name__=="__main__":
    main()
