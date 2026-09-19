#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z49C-SIZE48-CANONICAL-COVER-RESOLUTION-GRAPH-CERTIFICATE.json"

def mat_vec(M,v):
    return [sum(Fraction(M[i][j])*v[j] for j in range(len(v))) for i in range(len(M))]

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_Z49C_SIZE48_CANONICAL_COVER_RESOLUTION_GRAPH_V1"

    assert d["pre_resolution_Q_self_intersections"] == ["-4/3","-2/3","-4/3"]
    assert d["local_A2"]["boundary_self_intersection_correction_per_node"] == "-2/3"

    g=d["resolved_graph"]
    assert g["self_intersections"] == [-2]*7
    assert g["genera"] == [1,0,0,0,0,0,1]
    assert g["chain"] is True

    M=[[0]*7 for _ in range(7)]
    for i in range(7):
        M[i][i]=-2
        if i<6:
            M[i][i+1]=M[i+1][i]=1

    a=[Fraction(-2) for _ in range(7)]
    assert mat_vec(M,a) == [Fraction(2),0,0,0,0,0,Fraction(2)]
    assert d["discrepancy"]["coefficients"] == [-2]*7
    assert d["discrepancy"]["gorenstein"] is True
    assert d["discrepancy"]["log_canonical"] is False

    z=[Fraction(1) for _ in range(7)]
    mz=mat_vec(M,z)
    assert mz == [Fraction(-1),0,0,0,0,0,Fraction(-1)]
    z2=sum(z[i]*mz[i] for i in range(7))
    kz=Fraction(4)
    pa=1+(z2+kz)/2
    assert z2 == -2
    assert pa == 2
    assert d["fundamental_cycle"]["arithmetic_genus"] == 2

    for key,val in d["firewalls"].items():
        assert val is False, key

    print("MB104 Z49C size48 canonical-cover resolution graph verifier: PASS")

if __name__=="__main__":
    main()
