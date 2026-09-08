#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT = ROOT / "stages/stage32/scratch/ex1-ex4-deraux-r123-retained-l1-adapter-20260908.json"

# Z[r], r^2=-2. Elements are pairs (a,b)=a+b*r.
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
Z=(0,0); O=(1,0); R=(0,1)

def mm(A,B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def mtc(A):
    return [[conj(A[j][i]) for j in range(2)] for i in range(2)]
def eq(A,B): return A==B

def powm(A,n):
    X=[[O,Z],[Z,O]]
    while n:
        if n&1: X=mm(X,A)
        A=mm(A,A); n//=2
    return X

def ring2_to4(A):
    out=[[0]*4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            a,b=A[i][j]
            out[i][j]=a
            out[i][j+2]=-2*b
            out[i+2][j]=b
            out[i+2][j+2]=a
    return out

def mv2(A,v):
    return tuple(sum(A[i][j]*v[j] for j in range(4))&1 for i in range(4))

def fixed_nonzero(A):
    A2=[[x&1 for x in row] for row in A]
    ans=[]
    for bits in range(1,16):
        v=tuple((bits>>i)&1 for i in range(4))
        if mv2(A2,v)==v: ans.append(v)
    return ans

def main():
    cert=json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["schema"]=="STAGE32_MAIN_SCRATCH_EX1_EX4_DERAUX_R123_RETAINED_L1_ADAPTER_V1"
    assert cert["status"]=="SCRATCH_EXACT_UNAUDITED_MARKED_LATTICE_ADAPTER_WITH_CURVE_CONJUGACY_GAP"

    # Twice Deraux's displayed Hermitian form, to avoid halves.
    HD=[[ (2,0), (-1,-1) ], [(-1,1),(2,0)]]
    HC=[[ (2,0), (1,1) ], [(1,-1),(2,0)]]
    D=[[O,Z],[Z,(-1,0)]]
    assert eq(mm(mm(mtc(D),HD),D),HC)

    A1=[[O,Z],[add(O,neg(R)),(-1,0)]]
    A2=[[add((-1,0),R),(2,0)],[add(O,R),add(O,neg(R))]]
    A3=[[O,add((-1,0),neg(R))],[Z,(-1,0)]]
    R123=mm(mm(A1,A2),A3)
    expected_R123=[[add((-1,0),R),O],[R,O]]
    assert eq(R123,expected_R123)

    B=mm(mm(D,R123),D)
    expected_B=[[add((-1,0),R),(-1,0)],[neg(R),O]]
    assert eq(B,expected_B)

    b3=[[(-1,0),(-1,0)],[O,Z]]
    b4=[[O,add(O,R)],[Z,(-1,0)]]
    word=mm(mm(mm(mm(b4,powm(b3,2)),b4),powm(b3,2)),b4)
    assert eq(B,word)
    assert eq(powm(B,8),[[O,Z],[Z,O]])
    assert not eq(powm(B,4),[[O,Z],[Z,O]])

    B4=ring2_to4(B)
    expected4=[[-1,-1,-2,0],[0,1,2,0],[1,0,-1,-1],[-1,0,0,1]]
    assert B4==expected4
    assert fixed_nonzero(B4)==[(0,0,1,0)]

    mod=cert["mod2_fixed_line"]
    assert mod["B_on_retained_Z_basis"]==expected4
    assert mod["unique_nonzero_fixed_vector"]==[0,0,1,0]
    assert mod["unique_fixed_W_line"]=="L1"
    assert mod["corresponding_Q602_residue"]==73

    boundary=cert["semantic_boundary"]
    assert boundary["Deraux_R123_to_retained_lattice_element_closed"] is True
    assert boundary["curve_B9_to_Deraux_labelled_R123_closed"] is False
    assert boundary["KRR_conjugating_automorphism_on_A2_materialized"] is False
    dec=cert["decision"]
    assert dec["absolute_delta0inf_retained_W_line_identified_now"] is False
    assert dec["authority_changed"] is False
    assert dec["Q602_excluded"] is False
    assert dec["O210_excluded"] is False

    print("PASS scratch Deraux R123 -> retained L1 exact lattice adapter")
    print("retained_word=b4*b3^2*b4*b3^2*b4 fixed_W_line=L1 conditional_residue=73")
    print("curve_B9_to_labelled_R123=UNRESOLVED authority=SCRATCH_UNAUDITED")

if __name__=="__main__":
    main()
