#!/usr/bin/env python3
import hashlib
import itertools
import json
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex4-05c-galois-complex-conjugation-marking-preflight-scratch.json"

# Z[r], r^2=-2, encoded as (a,b)=a+b*r.
def qadd(x,y): return (x[0]+y[0], x[1]+y[1])
def qneg(x): return (-x[0],-x[1])
def qsub(x,y): return qadd(x,qneg(y))
def qmul(x,y): return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def qbar(x): return (x[0],-x[1])

Z=(0,0); O=(1,0); R=(0,1)

def mm(A,B):
    return tuple(tuple(qadd(qmul(A[i][0],B[0][j]),qmul(A[i][1],B[1][j]))
                       for j in range(2)) for i in range(2))

def mt(A):
    return tuple(tuple(A[j][i] for j in range(2)) for i in range(2))

def mbar(A):
    return tuple(tuple(qbar(x) for x in row) for row in A)

def mstar(A):
    return mt(mbar(A))

def key(A):
    return tuple(x for row in A for x in row)

def meq(A,B):
    return key(A)==key(B)

def det(A):
    return qsub(qmul(A[0][0],A[1][1]),qmul(A[0][1],A[1][0]))

def qinv_unit(x):
    n=x[0]*x[0]+2*x[1]*x[1]
    assert n==1
    return (x[0],-x[1])

def minv_unit(A):
    di=qinv_unit(det(A))
    return (
      (qmul(di,A[1][1]),qmul(di,qneg(A[0][1]))),
      (qmul(di,qneg(A[1][0])),qmul(di,A[0][0]))
    )

I=((O,Z),(Z,O))
H=(((2,0),(1,1)),((1,-1),(2,0)))
HB=mbar(H)
S=((O,qadd(O,R)),(Z,qneg(O)))
T=((O,O),(qneg(O),Z))

W={"L1":(1,0),"L2":(0,1),"L3":(1,1)}
WINV={v:k for k,v in W.items()}

def mod2_a0(A):
    return tuple(tuple(A[i][j][0] & 1 for j in range(2)) for i in range(2))

def act2(M,v):
    return (
      (M[0][0]*v[0]+M[0][1]*v[1]) & 1,
      (M[1][0]*v[0]+M[1][1]*v[1]) & 1
    )

def wperm(A):
    M=mod2_a0(A)
    return tuple(WINV[act2(M,W[k])] for k in ("L1","L2","L3"))

def parse_q(s):
    s=s.replace(" ","")
    table={
      "0":Z,"1":O,"-1":qneg(O),"r":R,"-r":qneg(R),
      "1+r":qadd(O,R),"1-r":qsub(O,R),
      "-1+r":qadd(qneg(O),R),"-1-r":qsub(qneg(O),R)
    }
    return table[s]

def parse_matrix(rows):
    return tuple(tuple(parse_q(x) for x in row) for row in rows)

def canonical_sha256_without_field(obj):
    x=dict(obj)
    expected=x.pop("canonical_sha256_without_this_field")
    payload=json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    actual=hashlib.sha256(payload).hexdigest()
    assert actual==expected,(actual,expected)

def main():
    obj=json.loads(ART.read_text())
    canonical_sha256_without_field(obj)
    assert obj["schema"]=="STAGE32EX4_EX4_05C_GALOIS_COMPLEX_CONJUGATION_MARKING_PREFLIGHT_SCRATCH_V1"
    assert obj["status"].startswith("SCRATCH_REPLAYABLE_")
    assert obj["field_restriction"]["cc_on_K"]=="r -> -r"
    assert obj["field_restriction"]["ct_on_K"]=="r -> -r"
    assert obj["source_W_galois_action"]["cc_action_on_W_lines"]=="identity"
    assert obj["source_W_galois_action"]["ct_action_on_W_lines"]=="identity"

    # Retained unitary group <S,T>.
    G={key(I):I}
    dq=deque([I])
    while dq:
        A=dq.popleft()
        for g in (S,T):
            B=mm(A,g)
            if key(B) not in G:
                G[key(B)]=B
                dq.append(B)
    assert len(G)==48
    assert all(det(A) in (O,qneg(O)) for A in G.values())

    # Exhaust anti-polarization matrices. The positive-definite norm bound is
    # recorded in the artifact; it reduces every entry to |a|<=2, |b|<=1.
    vals=[(a,b) for a in range(-2,3) for b in range(-1,2)]
    anti=[]
    for e in itertools.product(vals, repeat=4):
        C=((e[0],e[1]),(e[2],e[3]))
        if det(C)==Z:
            continue
        if meq(mm(mm(mstar(C),H),C),HB):
            anti.append(C)
    assert len(anti)==48

    inv=[C for C in anti if meq(mm(C,mbar(C)),I)]
    assert len(inv)==18
    perms=Counter(wperm(C) for C in inv)
    assert perms==Counter({
      ("L1","L2","L3"):6,
      ("L3","L2","L1"):4,
      ("L1","L3","L2"):4,
      ("L2","L1","L3"):4,
    })

    wid=[C for C in inv if wperm(C)==("L1","L2","L3")]
    assert len(wid)==6
    listed=[parse_matrix(x["C"]) for x in obj["retained_semilinear_enumeration"]["six_W_identity_lifts"]]
    assert {key(C) for C in wid}=={key(C) for C in listed}

    # For an exact retained semilinear lift C, residual unitary markings h
    # satisfy h C = C bar(h). Each W-trivial lift has stabilizer order 8,
    # with one invariant W-line; all three possible invariant lines occur twice.
    fixed_lines=[]
    for entry,C in zip(obj["retained_semilinear_enumeration"]["six_W_identity_lifts"],listed):
        stab=[h for h in G.values() if meq(mm(h,C),mm(C,mbar(h)))]
        assert len(stab)==8
        invariant=[]
        for j,L in enumerate(("L1","L2","L3")):
            images={wperm(h)[j] for h in stab}
            if images=={L}:
                invariant.append(L)
        assert len(invariant)==1
        assert invariant[0]==entry["unique_stabilizer_fixed_W_line"]
        fixed_lines.append(invariant[0])
    assert Counter(fixed_lines)==Counter({"L1":2,"L2":2,"L3":2})

    C0=parse_matrix(obj["conditional_differential_real_structure"]["transported_C0"])
    assert C0==((O,Z),(R,O))
    assert C0 in wid
    assert meq(mm(C0,mbar(C0)),I)
    assert meq(mm(mm(mstar(C0),H),C0),HB)
    st0=[h for h in G.values() if meq(mm(h,C0),mm(C0,mbar(h)))]
    assert len(st0)==8
    pset={wperm(h) for h in st0}
    assert pset=={("L1","L2","L3"),("L3","L2","L1")}
    assert obj["conditional_differential_real_structure"]["conditional_line_if_C0_is_independently_source_bound"]=="L2"
    assert obj["conditional_differential_real_structure"]["conditional_residue_if_C0_is_independently_source_bound"]==97

    d=obj["decision"]
    assert d["absolute_W_line_identified"] is False
    assert d["absolute_Q602_residue_identified"] is False
    assert d["Q602_excluded"] is False
    assert d["O210_excluded"] is False
    assert d["stage32_main_credit"] is False
    assert obj["firewalls"]["literal_C0_promoted_to_geometric_retained_real_structure"] is False

    print("PASS EX4-05C Galois/complex-conjugation marking preflight")
    print("retained unitary group: 48")
    print("anti-polarization matrices: 48; involutions: 18")
    print("W-trivial involutive lifts: 6")
    print("residual fixed-line distribution across six lifts: L1/L2/L3 = 2/2/2")
    print("conditional literal C0 stabilizer: order 8, fixed line L2 -> residue 97 (not promoted)")

if __name__=="__main__":
    main()
