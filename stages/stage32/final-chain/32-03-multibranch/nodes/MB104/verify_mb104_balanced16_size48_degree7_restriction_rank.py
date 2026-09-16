#!/usr/bin/env python3
import hashlib, json
from math import comb
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-SPAN5-BALANCED16-SIZE48-DEGREE7-RESTRICTION-RANK-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-SIZE48-DEGREE7-RESTRICTION-RANK.md","5107e872fedf670aa7908e4ba65413493c3f01da"),
 "NULL_UNION_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-NULL-UNION-COHOMOLOGY-CERTIFICATE.json","e7c5be93372f653bb42d8528ab68bcfaa4d6de60"),
 "STABILIZER_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json","31695c6908cff73d04baab2ed11dfd04608a2464"),
 "FORMAL_PICARD":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md","de83fc169814681109bcbc1576ad24f67d6159e0"),
 "KNOWN_QUOTIENT_VERIFIER":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_genus1_span5_known_conic_balanced_quotient.py","fe55e8a7bcd5b790f8d65419a9a88ba59106ba54")
}
P,II=1097,341

def req(c,m):
    if not c: raise SystemExit("FAIL: "+m)
def root():
    p=HERE
    while p!=p.parent:
        if (p/"AGENTS.md").is_file() and (p/"stages").is_dir(): return p
        p=p.parent
    raise SystemExit("FAIL: repo root")
def blob(p):
    d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()
def preflight(cert):
    dec={x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    req(dec==LOCKS,"source locks")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel
        if not p.is_file(): raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got=blob(p)
        if got!=sha: raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")

def exact_monoms(n,d,prefix=()):
    if n==1:
        yield prefix+(d,); return
    for v in range(d+1):
        yield from exact_monoms(n-1,d-v,prefix+(v,))
def monoms_upto(n,d):
    out=[]
    for e in range(d+1): out.extend(exact_monoms(n,e))
    return out
U=monoms_upto(6,3); UI={m:i for i,m in enumerate(U)}; MUL=monoms_upto(6,2)

def rref(M):
    A=[[x%P for x in row] for row in M if any(x%P for x in row)]
    if not A: return [],[]
    m,n=len(A),len(A[0]); piv=[]; r=0
    for c in range(n):
        pv=next((i for i in range(r,m) if A[i][c]),None)
        if pv is None: continue
        A[r],A[pv]=A[pv],A[r]
        iv=pow(A[r][c],P-2,P); A[r]=[(x*iv)%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]; A[i]=[(A[i][j]-f*A[r][j])%P for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    return A[:r],piv

def nullspace(M):
    R,piv=rref(M); n=len(M[0]); free=[j for j in range(n) if j not in piv]; out=[]
    for f in free:
        v=[0]*n; v[f]=1
        for k,p in enumerate(piv): v[p]=(-R[k][f])%P
        out.append(v)
    return out

def nodes():
    out=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[0]*7; z[j]=sa%P; o=[t for t in range(3) if t!=j]
                    z[3+o[0]],z[3+o[1]],z[6]=s1%P,s2%P,1; out.append(tuple(z))
    for j in range(3):
        o=[t for t in range(3) if t!=j]; a,b=o
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[0]*7; z[a]=1; z[b]=II*sr%P; z[3+a]=II*ep%P; z[3+b]=(-eq*sr)%P
                    out.append(tuple(z))
    req(len(out)==48 and len(set(out))==48,"48 nodes"); return out
V=nodes()

def from_mask(h):
    m=int(h,16); return frozenset(i for i in range(48) if (m>>i)&1)
SUPPORTS={h:from_mask(h) for h in ("0000770000ff","00007b0000ff")}

QTERMS=[
 [(1,(2,0,0,0,0,0,0)),(1,(0,2,0,0,0,0,0)),(-1,(0,0,0,0,0,2,0))],
 [(1,(0,2,0,0,0,0,0)),(1,(0,0,2,0,0,0,0)),(-1,(0,0,0,2,0,0,0))],
 [(1,(2,0,0,0,0,0,0)),(1,(0,0,2,0,0,0,0)),(-1,(0,0,0,0,2,0,0))],
 [(1,(2,0,0,0,0,0,0)),(1,(0,2,0,0,0,0,0)),(1,(0,0,2,0,0,0,0)),(-1,(0,0,0,0,0,0,2))]
]
GB=[]
for f3 in (0,1):
 for f4 in (0,1):
  for f5 in (0,1):
   for f6 in (0,1):
    rem=7-f3-f4-f5-f6
    for e0 in range(rem+1):
     for e1 in range(rem-e0+1): GB.append((e0,e1,rem-e0-e1,f3,f4,f5,f6))
req(len(GB)==344,"degree7 basis")

def pmul(A,B):
    C={}
    for a,ca in A.items():
        for b,cb in B.items():
            m=tuple(a[i]+b[i] for i in range(6))
            if sum(m)<=3: C[m]=(C.get(m,0)+ca*cb)%P
    return {m:c for m,c in C.items() if c}
def mon_local(exp,pt):
    j0=next(j for j,x in enumerate(pt) if x); iv=pow(pt[j0],P-2,P); pp=[x*iv%P for x in pt]
    vm={}; k=0
    for j in range(7):
        if j==j0: vm[j]=None
        else: vm[j]=k; k+=1
    A={(0,0,0,0,0,0):1}
    for j,e in enumerate(exp):
        if not e or j==j0: continue
        B={}
        for u in range(min(e,3)+1):
            m=[0]*6; m[vm[j]]=u; B[tuple(m)]=comb(e,u)*pow(pp[j],e-u,P)%P
        A=pmul(A,B)
    return A
def poly_local(terms,pt):
    out={}
    for cf,e in terms:
        for m,c in mon_local(e,pt).items(): out[m]=(out.get(m,0)+cf*c)%P
    return {m:c for m,c in out.items() if c}
def vec(poly):
    v=[0]*84
    for m,c in poly.items(): v[UI[m]]=c
    return v
def shift(poly,b):
    out={}
    for m,c in poly.items():
        mm=tuple(m[i]+b[i] for i in range(6))
        if sum(mm)<=3: out[mm]=c
    return out

def node_rows(pt):
    rel=[]
    for qt in QTERMS:
        q=poly_local(qt,pt)
        req(q.get((0,0,0,0,0,0),0)==0,"node on surface")
        for b in MUL:
            s=shift(q,b)
            if s: rel.append(vec(s))
    RR,piv=rref(rel); req(len(piv)==68,"local relation rank68")
    W=nullspace(RR); req(len(W)==16,"A1 m4 quotient length16")
    cols=[vec(mon_local(e,pt)) for e in GB]
    rows=[]
    for w in W:
        rows.append([sum(w[i]*col[i] for i in range(84))%P for col in cols])
    return rows

def evalrow(pt):
    row=[]
    for e in GB:
        x=1
        for j,a in enumerate(e):
            if a: x=x*pow(pt[j],a,P)%P
        row.append(x)
    return row

def on_surface(z):
    a1,a2,a3,b1,b2,b3,c=z
    return [(a1*a1+a2*a2-b3*b3)%P,(a2*a2+a3*a3-b1*b1)%P,(a1*a1+a3*a3-b2*b2)%P,(a1*a1+a2*a2+a3*a3-c*c)%P]==[0,0,0,0]

def peq(a,b):
    j=next((k for k,x in enumerate(a) if x),None)
    return j is not None and b[j] and all(a[k]*b[j]%P==b[k]*a[j]%P for k in range(7))

QPTS={
 (-1,-1):(1,341,1,0,407,0,1),
 (-1, 1):(1096,341,1,0,407,0,1),
 ( 1,-1):(1,756,1,0,407,0,1),
 ( 1, 1):(1096,756,1,0,407,0,1)
}

def qpoint_ok(st,z):
    s,t=st; a1,a2,a3,b1,b2,b3,c=z
    return on_surface(z) and b1==0 and (a2+s*II*a3)%P==0 and (a1+t*c)%P==0 and not any(peq(z,n) for n in V)

def main():
    cert=json.loads(CERT.read_text()); req(cert["schema"]=="STAGE32_MB104_BALANCED16_SIZE48_DEGREE7_RESTRICTION_RANK_V1","schema"); preflight(cert)
    req(II*II%P==P-1,"i specialization")
    for st,z in QPTS.items(): req(qpoint_ok(st,z),f"generic quartic point {st}")
    cache={}
    for idx in sorted(set().union(*SUPPORTS.values())): cache[idx]=node_rows(V[idx])
    out={}
    evals=[evalrow(QPTS[st]) for st in sorted(QPTS)]
    for h,S in SUPPORTS.items():
        C=[r for idx in sorted(S) for r in cache[idx]]; R,piv=rref(C); r0=len(piv)
        _,piv2=rref(R+evals); r1=len(piv2)
        req((r0,r1)==(220,222),f"{h} ranks 220/222")
        out[h]={"jet_rank_mod_p":r0,"augmented_rank_mod_p":r1,"restriction_rank_lower_bound_char0":r1-r0}
    req(cert["finite_field_results"]==out,"certificate rank table")
    # RR/null-union side: chi(A)=120, h1(A)>=4, h2(A)=0 => h0(A)>=124.
    # modular rank 220 => char0 jet rank>=220 => h0(A)<=124, hence equality.
    req(cert["char0_consequence"]["h0_A"]==124,"h0 char0")
    req(cert["char0_consequence"]["h1_A"]==4,"h1 char0")
    req(cert["char0_consequence"]["all_four_zero_quartics_nonfixed_both_size48_orbits"] is True,"nonfixedness")
    print("PASS STAGE32_MB104_BALANCED16_SIZE48_DEGREE7_RESTRICTION_RANK_V1")
    print("both size48 masks: jet rank mod1097=220; +4 quartic evaluations rank=222")
    print("RR h0>=124 plus good-prime rank gives h0=124,h1=4; char0 restriction rank>=2")
    print("stabilizer all-or-none => all four zero quartics nonfixed; powers give all l>=1")
if __name__=="__main__": main()
