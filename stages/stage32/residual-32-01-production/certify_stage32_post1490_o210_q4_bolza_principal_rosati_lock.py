#!/usr/bin/env python3
import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT = Path("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-principal-rosati-lock.json")

def require(cond, msg):
    if not cond:
        raise AssertionError(msg)

def load_json(rel):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)

def blob_sha1(rel):
    data = (ROOT / rel).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()

def canonical_sha256_obj(obj):
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    data = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()

# Q(r), r^2=-2, represented as (a,b)=a+b*r.
def qa(a=0, b=0):
    return (Fraction(a), Fraction(b))

def qadd(x, y):
    return (x[0]+y[0], x[1]+y[1])

def qneg(x):
    return (-x[0], -x[1])

def qsub(x, y):
    return qadd(x, qneg(y))

def qmul(x, y):
    return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def qconj(x):
    return (x[0], -x[1])

def mat_add(A, B):
    return [[qadd(A[i][j], B[i][j]) for j in range(2)] for i in range(2)]

def mat_mul(A, B):
    return [[qadd(qmul(A[i][0],B[0][j]), qmul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]

def mat_ct(A):
    return [[qconj(A[j][i]) for j in range(2)] for i in range(2)]

ZERO=qa(); ONE=qa(1); R=qa(0,1)
b1=[[qa(-1,1),qa(-2)],[qa(0,-1),qa(1,-1)]]
b2=[[qa(1),R],[R,qa(-1)]]
H=[[qa(2),qa(1,1)],[qa(1,-1),qa(2)]]
HINV=[[qa(2),qa(-1,-1)],[qa(-1,1),qa(2)]]
HA=[[ONE,ZERO],[ZERO,ZERO]]
HB=[[ZERO,ZERO],[ZERO,ONE]]
HC=[[ZERO,ONE],[ONE,ZERO]]
HD=[[ZERO,R],[qneg(R),ZERO]]
HBASIS=[HA,HB,HC,HD]

def invariance_delta(M, X):
    negX=[[qneg(X[i][j]) for j in range(2)] for i in range(2)]
    return mat_add(mat_mul(mat_mul(mat_ct(M), X), M), negX)

def rational_rank(rows):
    A=[[Fraction(x) for x in row] for row in rows if any(Fraction(x) != 0 for x in row)]
    if not A:
        return 0
    m,n=len(A),len(A[0]); rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,m) if A[i][col] != 0),None)
        if pivot is None:
            continue
        A[rank],A[pivot]=A[pivot],A[rank]
        p=A[rank][col]
        A[rank]=[x/p for x in A[rank]]
        for i in range(m):
            if i != rank and A[i][col] != 0:
                f=A[i][col]
                A[i]=[A[i][j]-f*A[rank][j] for j in range(n)]
        rank+=1
        if rank==m:
            break
    return rank

def herm(v,w):
    s=ZERO
    for i in range(2):
        for j in range(2):
            s=qadd(s,qmul(qmul(qconj(v[i]),H[i][j]),w[j]))
    return s

def riemann(v,w):
    d=qsub(herm(v,w),herm(w,v))
    require(d[0] == 0, "Riemann numerator must be pure r")
    return d[1]/2

def det4(A):
    total=Fraction(0)
    for p in itertools.permutations(range(4)):
        inv=sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])
        term=Fraction(-1 if inv%2 else 1)
        for i in range(4):
            term*=Fraction(A[i][p[i]])
        total+=term
    return total

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check", type=Path, default=DEFAULT)
    args=ap.parse_args()
    obj=load_json(args.check)

    require(obj["schema"]=="STAGE32_POST1490_O210_Q4_BOLZA_PRINCIPAL_ROSATI_LOCK_V1","schema")
    require(obj["fixed_target"]=={"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32],"O":210,"qprime":4},"fixed target")

    front=obj["source_locks"]["frontier"]
    require(blob_sha1(Path(front["path"]))==front["blob_sha1"],"frontier blob lock")
    fobj=load_json(Path(front["path"]))
    require(fobj["canonical_sha256_without_this_field"]==front["canonical_sha256"],"frontier stored canonical")
    require(canonical_sha256_obj(fobj)==front["canonical_sha256"],"frontier canonical replay")
    note=obj["source_locks"]["source_note"]
    require(blob_sha1(Path(note["path"]))==note["blob_sha1"],"source-note blob lock")
    ext=obj["source_locks"]["external_principal_g12"]
    require(ext["arxiv"]=="2509.24605v1","external arxiv lock")
    require(ext["locators"]==["Section 3.2 equations (3.19)-(3.20)","Appendix B equations (B.1)-(B.6), Fact 18"],"external locators")

    deltas=[[invariance_delta(M,X) for X in HBASIS] for M in (b1,b2)]
    rows=[]
    for block in deltas:
        for i in range(2):
            for j in range(2):
                for coeff in range(2):
                    rows.append([block[k][i][j][coeff] for k in range(4)])
    require(rational_rank(rows)==3,"invariant Hermitian space must have dimension one")
    coeff=[Fraction(2),Fraction(2),Fraction(1),Fraction(1)]
    require(all(sum(Fraction(row[k])*coeff[k] for k in range(4))==0 for row in rows),"primitive H vector must span invariant line")
    require(mat_mul(mat_mul(mat_ct(b1),H),b1)==H,"b1 invariance")
    require(mat_mul(mat_mul(mat_ct(b2),H),b2)==H,"b2 invariance")

    detH=qsub(qmul(H[0][0],H[1][1]),qmul(H[0][1],H[1][0]))
    require(detH==ONE,"det H")
    require(mat_mul(H,HINV)==[[ONE,ZERO],[ZERO,ONE]],"H inverse")
    pp=obj["principal_polarization"]
    require(pp["hermitian_matrix"]==[["2","1+r"],["1-r","2"]],"stored H")
    require(pp["determinant"]==1 and pp["positive_definite"] is True,"positive unimodular H")
    require(pp["product_polarization"] is False,"product-polarization firewall")

    basis=[[ONE,ZERO],[ZERO,ONE],[R,ZERO],[ZERO,R]]
    E=[[riemann(v,w) for w in basis] for v in basis]
    expected=[[Fraction(x) for x in row] for row in pp["riemann_form_matrix"]]
    require(E==expected,"Riemann form matrix")
    require(det4(E)==1==pp["riemann_form_determinant"],"principal Riemann determinant")
    require(pp["principal"] is True,"principal flag")

    ro=obj["rosati"]
    require(ro["formula"]=="T^dagger=H^{-1}*bar(T)^t*H","Rosati formula")
    require(ro["H_inverse"]==[["2","-1-r"],["-1+r","2"]],"stored H inverse")
    require(ro["exact_locked"] is True,"Rosati lock")

    enum=obj["enumeration_frontier"]
    require(enum["inequality"]=="T^dagger*T <= 8505","retained bound")
    require(enum["equivalent_hermitian_inequality"]=="bar(T)^t*H*T <= 8505*H","H inequality")
    fourHminusI=[[qa(7),qa(4,4)],[qa(4,-4),qa(7)]]
    detL=qsub(qmul(fourHminusI[0][0],fourHminusI[1][1]),qmul(fourHminusI[0][1],fourHminusI[1][0]))
    require(detL==ONE,"4H-I determinant")
    require(enum["column_h_bound"]==8505*2==17010,"column H bound")
    require(enum["column_euclidean_norm_squared_bound"]==4*17010==68040,"Euclidean bound")
    require(260*260<=68040<(261*261),"real coefficient floor")
    require(2*184*184<=68040<2*185*185,"r coefficient floor")
    require(enum["coefficient_box"]=={"abs_a_max":260,"abs_b_max":184},"coefficient box")
    require(enum["finite_box_certified"] is True and enum["enumeration_completed"] is False,"enumeration firewall")

    dec=obj["decision"]
    require(dec["O210_excluded"] is False,"O210 firewall")
    require(dec["rosati_matrix_source_locked"] is True,"Rosati decision")
    require(dec["principal_polarization_exact"] is True,"principal decision")
    require(dec["next_exact_leaf"]=="O210_Q4_BOLZA_ROSATI_EXACT_ENUMERATION_IN_BOX","next leaf")
    require(obj["firewalls"]["enumeration_claimed_complete"] is False,"no completeness claim")

    actual=canonical_sha256_obj(obj)
    require(actual==obj["canonical_sha256_without_this_field"],"canonical sha256")
    print(json.dumps({"ok":True,"canonical_sha256":actual,"H":[["2","1+r"],["1-r","2"]],"riemann_det":1,"rosati_exact":True,"coefficient_box":{"abs_a_max":260,"abs_b_max":184},"O210_excluded":False,"next_exact_leaf":dec["next_exact_leaf"]},sort_keys=True))

if __name__=="__main__":
    main()
