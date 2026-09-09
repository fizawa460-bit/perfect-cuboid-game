#!/usr/bin/env python3
import json, hashlib, os, zlib, base64

ROOT = os.path.dirname(__file__)
DOMAIN_PATH = os.path.join(ROOT, "ex1-05af-cellular-h2-domain-certificate.json")
PULL_PATH = os.path.join(ROOT, "ex1-05af-cellular-pullback-smith-certificate.json")

def load_cert(path):
    with open(path, "r", encoding="utf-8") as f:
        x=json.load(f)
    claimed=x.pop("canonical_sha256_without_this_field")
    raw=json.dumps(x, sort_keys=True, separators=(",",":"))
    got=hashlib.sha256(raw.encode()).hexdigest()
    assert got==claimed, (path,got,claimed)
    x["canonical_sha256_without_this_field"]=claimed
    return x

def decode_payload(cert):
    p=cert["matrix_payload"]
    raw=zlib.decompress(base64.b85decode(p["encoded"].encode()))
    assert len(raw)==p["uncompressed_bytes"]
    assert hashlib.sha256(raw).hexdigest()==p["uncompressed_sha256"]
    return json.loads(raw.decode())

def shape(A):
    return (len(A), len(A[0]) if A else 0)

def zeros(m,n):
    return [[0]*n for _ in range(m)]

def eye(n):
    A=zeros(n,n)
    for i in range(n): A[i][i]=1
    return A

def transpose(A):
    m,n=shape(A)
    return [[A[i][j] for i in range(m)] for j in range(n)]

def mm(A,B):
    m,k=shape(A); k2,n=shape(B); assert k==k2
    BT=transpose(B)
    return [[sum(a*b for a,b in zip(A[i],BT[j])) for j in range(n)] for i in range(m)]

def add(A,B):
    assert shape(A)==shape(B)
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def cols(A, lo, hi):
    return [row[lo:hi] for row in A]

def diag_matrix(ds):
    A=zeros(len(ds),len(ds))
    for i,d in enumerate(ds): A[i][i]=d
    return A

def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A); assert all(len(r)==n for r in A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next((i for i in range(k+1,n) if A[i][k]!=0),None)
            assert p is not None
            A[k],A[p]=A[p],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*piv-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
        for i in range(k+1,n): A[i][k]=0
        prev=piv
    return sign*A[-1][-1]

H=range(4)
U=1; V=2; ID=0
EDGE_MON=[U,ID,V,ID]
CELLT={0:["v"],1:["e0","e1","e2","e3"],2:["f"]}

def fdiff(deg, typ, h):
    if deg==0: return []
    if deg==1:
        i=int(typ[1]); g=EDGE_MON[i]
        if g==ID: return []
        return [(1,"v",h^g),(-1,"v",h)]
    assert deg==2 and typ=="f"
    return [(1,"e1",h^U),(-1,"e1",h),(1,"e3",h^V),(-1,"e3",h)]

def factor_basis(deg):
    return [(t,h) for t in CELLT[deg] for h in H]

FB={d:factor_basis(d) for d in range(3)}
FI={d:{b:i for i,b in enumerate(FB[d])} for d in range(3)}

def factor_boundary(deg):
    if deg==0: return []
    M=zeros(len(FB[deg-1]),len(FB[deg]))
    for j,(t,h) in enumerate(FB[deg]):
        for c,t2,h2 in fdiff(deg,t,h):
            M[FI[deg-1][(t2,h2)]][j]+=c
    return M

D1=factor_boundary(1)
D2=factor_boundary(2)
DELTA0=transpose(D1)
DELTA1=transpose(D2)

def qbasis(n):
    out=[]
    for p in range(3):
        q=n-p
        if 0<=q<3:
            for t1 in CELLT[p]:
                for t2 in CELLT[q]:
                    for d in H:
                        out.append((p,t1,q,t2,d))
    return out

QB={n:qbasis(n) for n in range(5)}
QI={n:{b:i for i,b in enumerate(QB[n])} for n in range(5)}

def qboundary(n):
    M=zeros(len(QB[n-1]),len(QB[n]))
    for j,(p,t1,q,t2,d) in enumerate(QB[n]):
        for c,t,h in fdiff(p,t1,d):
            M[QI[n-1][(p-1,t,q,t2,h)]][j]+=c
        s=-1 if p%2 else 1
        for c,t,h in fdiff(q,t2,ID):
            M[QI[n-1][(p,t1,q-1,t,d^h)]][j]+=s*c
    return M

QB2=qboundary(2)
QB3=qboundary(3)
QDELTA1=transpose(QB2)
QDELTA2=transpose(QB3)

def pbasis(n):
    out=[]
    for p in range(3):
        q=n-p
        if 0<=q<3:
            for t1,h1 in FB[p]:
                for t2,h2 in FB[q]:
                    out.append((p,t1,h1,q,t2,h2))
    return out

PB={n:pbasis(n) for n in range(5)}
PI={n:{b:i for i,b in enumerate(PB[n])} for n in range(5)}

def pboundary(n):
    M=zeros(len(PB[n-1]),len(PB[n]))
    for j,(p,t1,h1,q,t2,h2) in enumerate(PB[n]):
        for c,t,h in fdiff(p,t1,h1):
            M[PI[n-1][(p-1,t,h,q,t2,h2)]][j]+=c
        s=-1 if p%2 else 1
        for c,t,h in fdiff(q,t2,h2):
            M[PI[n-1][(p,t1,h1,q-1,t,h)]][j]+=s*c
    return M

PDELTA1=transpose(pboundary(2))

def pullback2():
    M=zeros(len(PB[2]),len(QB[2]))
    for i,(p,t1,h1,q,t2,h2) in enumerate(PB[2]):
        j=QI[2][(p,t1,q,t2,h1^h2)]
        M[i][j]=1
    return M

P2=pullback2()

D=load_cert(DOMAIN_PATH)
P=load_cert(PULL_PATH)
assert P["source_domain_certificate"]["canonical_sha256"]==D["canonical_sha256_without_this_field"]
DP=decode_payload(D)
PP=decode_payload(P)

K=DP["K"]
KL=DP["Kleft"]
assert shape(K)==(72,51) and shape(KL)==(51,72)
assert mm(QDELTA2,K)==zeros(32,51)
assert mm(KL,K)==eye(51)
rr=D["s0_h2_kernel"]["delta2_rank_minor_rows"]
cc=D["s0_h2_kernel"]["delta2_rank_minor_cols"]
minor=[[QDELTA2[i][j] for j in cc] for i in rr]
assert det_bareiss(minor)==D["s0_h2_kernel"]["delta2_rank_minor_det"]!=0

ids=D["s0_coboundary_image"]["image_diagonal_in_kernel_basis"]
assert ids==[1]*20+[2]
BIMG=mm(cols(K,0,21),diag_matrix(ids))
assert mm(BIMG,DP["Ccombo"])==QDELTA1
assert mm(QDELTA1,DP["Dcombo"])==BIMG
QFREE=cols(K,21,51)
assert shape(QFREE)==(72,30)

F=D["factor_X8_cohomology"]
K1=DP["K1"]; K1L=DP["K1left"]
assert mm(DELTA1,K1)==zeros(4,13)
assert mm(K1L,K1)==eye(13)
rr=F["H1_delta1_rank_minor"]["rows"]; cc=F["H1_delta1_rank_minor"]["cols"]
assert det_bareiss([[DELTA1[i][j] for j in cc] for i in rr])==F["H1_delta1_rank_minor"]["det"]!=0
B01=cols(K1,0,3)
assert mm(B01,DP["C1"])==DELTA0
assert mm(DELTA0,DP["D1"])==B01
H1=cols(K1,3,13)
assert shape(H1)==(16,10)

H0=[[1],[1],[1],[1]]
assert mm(DELTA0,H0)==zeros(16,1)
rr=F["delta0_rank_minor"]["rows"]; cc=F["delta0_rank_minor"]["cols"]
assert det_bareiss([[DELTA0[i][j] for j in cc] for i in rr])==F["delta0_rank_minor"]["det"]!=0

K2=DP["K2"]; K2L=DP["K2left"]
assert mm(K2L,K2)==eye(4)
B2=cols(K2,0,3)
assert mm(B2,DP["C2"])==DELTA1
assert mm(DELTA1,DP["D2"])==B2
H2=cols(K2,3,4)
assert shape(H2)==(4,1)

def tensor_col(p, f, q, g):
    out=[0]*len(PB[p+q])
    f=[r[0] for r in f]; g=[r[0] for r in g]
    for k,(pp,t1,h1,qq,t2,h2) in enumerate(PB[p+q]):
        if pp==p and qq==q:
            out[k]=f[FI[p][(t1,h1)]]*g[FI[q][(t2,h2)]]
    return out

ucols=[]
ucols.append(tensor_col(2,H2,0,H0))
for i in range(10):
    fi=[[H1[r][i]] for r in range(16)]
    for j in range(10):
        gj=[[H1[r][j]] for r in range(16)]
        ucols.append(tensor_col(1,fi,1,gj))
ucols.append(tensor_col(0,H0,2,H2))
UK=transpose(ucols)
assert shape(UK)==(288,102)

ds=P["smith"]["invariant_factors"]
assert ds==[1]*25+[2,2,2,4,4]
assert P["smith"]["index"]==128
LS=PP["Lsat"]
LL=PP["Lleft"]
assert shape(LS)==(102,30) and shape(LL)==(30,102)
assert mm(LL,LS)==eye(30)
B=PP["Bcoef"]
assert shape(B)==(128,30)
lhs=mm(P2,QFREE)
rhs=add(mm(UK,mm(LS,diag_matrix(ds))), mm(PDELTA1,B))
assert lhs==rhs
prod=1
for x in ds: prod*=x
assert prod==128

print("PASS_EX1_05AF_FULL_CELLULAR_SMITH_CERTIFICATE")
print("S0_betti", D["model"]["S0_betti_numbers_over_Q"])
print("H2_pullback_smith_tail", ds[-5:], "index", P["smith"]["index"])
print("cokernel", P["smith"]["cokernel"])
