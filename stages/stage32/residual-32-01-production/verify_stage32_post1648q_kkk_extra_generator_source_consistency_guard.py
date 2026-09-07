#!/usr/bin/env python3
from __future__ import annotations

import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648q-kkk-extra-generator-source-consistency-guard.json"
N_PATH = HERE / "post1648n-canonical-period-marked-ppav-torsor-obstruction.json"
P_PATH = HERE / "post1648p-b9-fixed-weierstrass-pair-nonpruning.json"
EXPECTED_CERT = "a622dc8f3ffb91f5f6ee4b8b63c13842b2184c2b11ab03c922922f5ec9f4f088"
EXPECTED_N = "060d940626cd59b00efb67db7f27914e6a440c92968600a3d82a208d5a5d76ba"
EXPECTED_N_BLOB = "0ee05f679c7706113feed2c217e08a95b3bd6f06"
EXPECTED_P = "07984fe43fa6f80e7b79fa61ddbd2f87a05b16f9d9ea502361e6963f39229e71"
EXPECTED_P_BLOB = "89fb1978066c084cdfe9093a16068b79d0ea54e6"


def canonical(obj):
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def blob(path):
    data=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()


def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def negI(n): return [[-1 if i==j else 0 for j in range(n)] for i in range(n)]

def mpow(A,n):
    out=eye(len(A))
    for _ in range(n): out=mm(out,A)
    return out

def proj_scalar_identity_2(A):
    return A[0][1]==0 and A[1][0]==0 and A[0][0]==A[1][1] and A[0][0]!=0


def main():
    cert=json.loads(CERT.read_text()); n=json.loads(N_PATH.read_text()); p=json.loads(P_PATH.read_text())
    assert canonical(cert)==EXPECTED_CERT==cert["canonical_sha256_without_this_field"]
    assert canonical(n)==EXPECTED_N==n["canonical_sha256_without_this_field"] and blob(N_PATH)==EXPECTED_N_BLOB
    assert canonical(p)==EXPECTED_P==p["canonical_sha256_without_this_field"] and blob(P_PATH)==EXPECTED_P_BLOB

    # Printed reduced maps: mu2=(z+1)/(z-1), mu3=-1/z.
    m2=[[1,1],[1,-1]]; m3=[[0,-1],[1,0]]
    p23=mm(m2,m3); p32=mm(m3,m2)
    assert p32 == [[-x for x in row] for row in p23]  # same PGL2 element
    assert not proj_scalar_identity_2(p23)
    assert proj_scalar_identity_2(mm(p23,p23))
    assert proj_scalar_identity_2(mm(p32,p32))

    T2=[[-1,0,0,0],[1,1,0,0],[0,1,-1,1],[-1,0,0,1]]
    T3=[[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]
    A23=mm(T2,T3); A32=mm(T3,T2)
    assert A23==cert["exact_consistency_test"]["cycle_matrix_product_Tmu2_Tmu3"]
    assert A32==cert["exact_consistency_test"]["cycle_matrix_product_Tmu3_Tmu2"]
    assert mpow(A23,2) not in (eye(4),negI(4)) and mpow(A32,2) not in (eye(4),negI(4))
    assert mpow(A23,3)==negI(4) and mpow(A32,3)==negI(4)
    assert mpow(A23,6)==eye(4) and mpow(A32,6)==eye(4)

    test=cert["exact_consistency_test"]
    assert test["reduced_x_map_product_order"]==2
    assert test["cycle_product_order_mod_central_plusminus_identity"]==3
    assert test["orders_compatible"] is False
    dec=cert["decision"]
    assert dec["printed_mu2_mu3_x_maps_and_3_43_matrices_can_be_jointly_used_as_named_semantic_adapter"] is False
    assert dec["post1648N_mu1_only_result_revoked"] is False
    assert dec["post1648P_fixed_pair_result_revoked"] is False
    assert dec["absolute_delta0inf_retained_W_line_identified"] is False
    assert dec["survivors_current_credit"]==[73,97,235]
    assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
    assert cert["firewalls"]["paper_declared_globally_incorrect"] is False
    assert cert["firewalls"]["source_typo_asserted_without_independent_confirmation"] is False

    print("POST1648Q_KKK_EXTRA_GENERATOR_SOURCE_CONSISTENCY_GUARD_COMPLETE")
    print("printed_reduced_mu2_mu3_product_order=2")
    print("printed_cycle_product_mod_center_order=3")
    print("joint_named_semantic_adapter_allowed=false source_repair_required=true")
    print("post1648N_mu1_only_result_revoked=false post1648P_fixed_pair_result_revoked=false")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")

if __name__=="__main__": main()
