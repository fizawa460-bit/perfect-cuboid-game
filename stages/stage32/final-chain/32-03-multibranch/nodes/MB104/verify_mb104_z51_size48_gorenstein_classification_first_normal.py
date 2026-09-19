#!/usr/bin/env python3
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z51-SIZE48-GORENSTEIN-CLASSIFICATION-FIRST-NORMAL-CERTIFICATE.json"

def chain_rank_n1():
    # Endpoint evaluations are zero. Five rational constants c1..c5 map to six node
    # discrepancies (-c1,c1-c2,c2-c3,c3-c4,c4-c5,c5), rank 5.
    rows=[
        [-1,0,0,0,0],
        [1,-1,0,0,0],
        [0,1,-1,0,0],
        [0,0,1,-1,0],
        [0,0,0,1,-1],
        [0,0,0,0,1],
    ]
    # exact Gaussian rank over Q
    from fractions import Fraction
    A=[[Fraction(x) for x in row] for row in rows]
    m,n=len(A),len(A[0]); r=0
    for col in range(n):
        piv=next((i for i in range(r,m) if A[i][col]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        q=A[r][col]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][col]:
                q=A[i][col]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
    return r

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_Z51_SIZE48_GORENSTEIN_CLASSIFICATION_FIRST_NORMAL_V1"
    assert d["endpoint_normal_bundle"]["exact_class"]=="O_E(-2p)"
    assert d["endpoint_normal_bundle"]["picard_degree_minus2_ambiguity_remaining"] is False

    assert chain_rank_n1()==5
    f=d["formal_picard"]
    assert f["n1"]["endpoint_restriction"]=="O_E(p)"
    assert f["n1"]["endpoint_evaluation_at_attachment"]=="zero"
    assert f["n1"]["h1_dimension"]==1
    assert f["n_ge_2"]["endpoint_globally_generated"] is True
    assert f["n_ge_2"]["h1_dimension"]==0

    c=d["conclusions"]
    assert c["exact_first_normal_residual_dimension"]==1
    assert c["higher_additive_picard_residual_dimension"]==0
    assert c["full_analytic_moduli_identified"] is False
    assert c["explicit_affine_normal_form_known"] is False

    for key,val in d["firewalls"].items():
        assert val is False, key

    print("MB104 Z51 size48 Gorenstein classification/first-normal verifier: PASS")

if __name__=="__main__":
    main()
