#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
DEFAULT=Path("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-birational-d4d4-trace-reduction.json")

def req(c,m):
    if not c: raise AssertionError(m)
def load(p):
    with (ROOT/p).open("r",encoding="utf-8") as f: return json.load(f)
def blob(p):
    b=(ROOT/p).read_bytes()
    return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock(x):
    p=Path(x["path"]); req(blob(p)==x["blob_sha1"],f"blob {p}")
    o=load(p)
    if "canonical_sha256" in x:
        req(o["canonical_sha256_without_this_field"]==x["canonical_sha256"],f"stored canonical {p}")
        req(canon(o)==x["canonical_sha256"],f"canonical {p}")
    return o

def a(x,y): return (x[0]+y[0],x[1]+y[1])
def m(x,y): return (x[0]*y[0]-2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def cj(x): return (x[0],-x[1])
def sm(xs):
    z=(0,0)
    for x in xs: z=a(z,x)
    return z
def mm(A,B):
    return [[sm(m(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def ct(A): return [[cj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
H=[[(2,0),(1,1)],[(1,-1),(2,0)]]
HI=[[(2,0),(-1,-1)],[(-1,1),(2,0)]]
def tmat(v): return [[(v[0],v[1]),(v[2],v[3])],[(v[4],v[5]),(v[6],v[7])]]
def q(v):
    T=tmat(v)
    P=mm(mm(mm(HI,ct(T)),H),T)
    z=a(P[0][0],P[1][1])
    req(z[1]==0,"Q rational")
    return z[0]
def gram_from_q():
    n=8; A=[[0]*n for _ in range(n)]; diag=[]
    for i in range(n):
        v=[0]*n; v[i]=1; diag.append(q(v)); A[i][i]=diag[-1]
    for i in range(n):
        for j in range(i):
            v=[0]*n; v[i]=v[j]=1
            d=q(v)-diag[i]-diag[j]; req(d%2==0,"integral bilinear")
            A[i][j]=A[j][i]=d//2
    return A
def imul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def det_bareiss(A):
    A=[row[:] for row in A]; n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next(i for i in range(k+1,n) if A[i][k]); A[k],A[p]=A[p],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n): A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]
def d4_coeff(N):
    s=[0]*(N+1)
    for d in range(1,N+1,2):
        for k in range(d,N+1,d): s[k]+=d
    return [1]+[24*s[i] for i in range(1,N+1)]
def d4d4_prefix(N):
    c=d4_coeff(N); pref=[]; z=0
    for x in c: z+=x; pref.append(z)
    return sum(c[i]*pref[N-i] for i in range(N+1))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",type=Path,default=DEFAULT); ns=ap.parse_args()
    o=load(ns.check)
    req(o["schema"]=="STAGE32_POST1490_O210_Q4_BOLZA_BIRATIONAL_D4D4_TRACE_REDUCTION_V1","schema")
    req(o["fixed_target"]=={"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32],"O":210,"qprime":4},"target")
    common=lock(o["source_locks"]["common_double_cover"]); prod=lock(o["source_locks"]["product_cover_v4"]); ros=lock(o["source_locks"]["principal_rosati"])
    note=o["source_locks"]["source_note"]; req(blob(Path(note["path"]))==note["blob_sha1"],"source note")
    req(common["group_quotient_square"]["H"]=="Gamma'[4]/Gamma[8] ~= V4, order 4, normal index 2","H quotient")
    req(prod["deck_group_model"]["group"]=="G=GammaPrime4/Gamma8 ~= F2^2","V4 deck")
    req(ros["principal_polarization"]["hermitian_matrix"]==[["2","1+r"],["1-r","2"]],"H")
    p=o["pair_map_birationality"]
    req(p["finite_etale_degree"]==4 and p["generic_pair_degree_allowed_by_deck_stabilizer"]==[1,2,4],"degree4/V4")
    req(p["projection_degrees"]==[105,81] and p["generic_pair_degree_divides_gcd"]==3,"gcd")
    req(set(p["generic_pair_degree_allowed_by_deck_stabilizer"]).intersection({1,3})=={1},"intersection")
    req(p["generic_pair_degree"]==1 and p["pair_map_birational"] and p["normalization_genus"]==106,"birational")
    c=o["correspondence_trace"]; constant=2*105*81+2*(105+81)-2*106+2
    req(constant==17172,"trace constant"); req(c["rational_rosati_trace"]=="Tr_Q(T^dagger*T)=17172-2*delta","trace formula")
    req(c["exact_identity"]=="Q(T)=8586-delta" and c["trace_upper_bound"]==8586,"Q identity")
    L=o["trace_lattice"]; A=gram_from_q(); req(A==L["gram_matrix"],"Gram expansion"); req(det_bareiss(A)==16==L["gram_determinant"],"Gram determinant")
    cols=L["unimodular_change_of_basis_columns"]; U=[[cols[j][i] for j in range(8)] for i in range(8)]
    req(det_bareiss(U)==1==L["change_of_basis_determinant"],"U determinant")
    D=L["d4_gram"]; Z=[[0]*4 for _ in range(4)]; target=[D[i]+Z[i] for i in range(4)]+[Z[i]+D[i] for i in range(4)]
    req(imul(imul(tr(U),A),U)==target,"D4+D4 isometry")
    e=o["exact_preflight"]
    req(d4d4_prefix(4293)==e["count_Q_le_8586"]==5516362054085041,"Q<=8586 count")
    req(d4d4_prefix(4252)==e["count_Q_le_8504"]==5309821812906193,"Q<=8504 count")
    req(e["count_Q_le_8586"]-e["count_Q_le_8504"]==e["remaining_shell_count"]==206540241178848,"shell count")
    req(e["frontier_materialization_safe"] is False,"materialization firewall")
    req(o["decision"]["O210_excluded"] is False and o["decision"]["next_exact_leaf"]=="O210_Q4_BOLZA_D4D4_COMMON_COVER_WEIERSTRASS_CONSTRAINT","decision")
    req(canon(o)==o["canonical_sha256_without_this_field"],"canonical")
    print(json.dumps({"ok":True,"canonical_sha256":canon(o),"pair_degree":1,"trace_lattice":"D4+D4","count_Q_le_8504":e["count_Q_le_8504"],"O210_excluded":False,"next_exact_leaf":o["decision"]["next_exact_leaf"]},sort_keys=True))
if __name__=="__main__": main()
