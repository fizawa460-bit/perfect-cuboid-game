#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z49C-SIZE48-INDEX-ONE-COVER-RESOLUTION-GRAPH-CERTIFICATE.json"

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_Z49C_SIZE48_INDEX_ONE_COVER_RESOLUTION_GRAPH_V1"

    # One A2 correction: solve 1-2a+b=0, a-2b=0.
    a=Fraction(2,3)
    b=Fraction(1,3)
    assert 1-2*a+b == 0
    assert a-2*b == 0

    q_before=Fraction(-4,3)
    b_before=Fraction(-2,3)
    assert q_before-a == -2
    assert b_before-a-a == -2

    r=d["resolved_cover"]
    assert r["vertex_self_intersections"] == [-2]*7
    assert r["vertex_genera"] == [1,0,0,0,0,0,1]
    assert r["discrepancy_coefficients"] == [-2]*7

    # Check discrepancy equations M*a = Kdot.
    n=7
    avec=[-2]*n
    kdot=[2]+[0]*5+[2]
    for i in range(n):
        lhs=-2*avec[i]
        if i>0:
            lhs+=avec[i-1]
        if i<n-1:
            lhs+=avec[i+1]
        assert lhs == kdot[i]

    z2=-2*7 + 2*6
    kz=4
    pa=1+(z2+kz)//2
    assert z2 == r["fundamental_cycle_square"] == -2
    assert kz == r["K_dot_fundamental_cycle"] == 4
    assert pa == r["fundamental_genus"] == 2

    assert r["gorenstein"] is True
    assert r["log_canonical"] is False
    assert d["conclusions"]["explicit_global_equation_known"] is False
    assert d["conclusions"]["local_symmetric_euler_computed"] is False

    for key,val in d["firewalls"].items():
        assert val is False, key

    print("MB104 Z49C size48 index-one cover resolution graph verifier: PASS")

if __name__=="__main__":
    main()
