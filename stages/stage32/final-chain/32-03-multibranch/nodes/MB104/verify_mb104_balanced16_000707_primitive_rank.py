#!/usr/bin/env python3
from fractions import Fraction
import hashlib, json
from math import comb
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md","6b973691df9c835d14ac388082111d202a07d8c7"),
 "STOLL_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-CANONICAL-C0-SOURCE-NOTE.md","e344290d5241c3f7f165ea3027cfc778abec3360"),
 "FORMAL_PICARD":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md","de83fc169814681109bcbc1576ad24f67d6159e0"),
 "PIC0_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json","1a92336433816883757fee844b736181e6848813"),
 "STABILIZER_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json","31695c6908cff73d04baab2ed11dfd04608a2464"),
 "TWO_QUARTIC_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-CERTIFICATE.json","658516458e0af20bbcac28f5f778eeeb361cd468"),
}
P,II=1097,341
MASK="000707000f0f"

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
    for v in range(d+1): yield from exact_monoms(n-1,d-v,prefix+(v,))
def monoms_upto(n,d):
    out=[]
    for e in range(d+1): out.extend(exact_monoms(n,e))
    return out
def basis(d):
    out=[]
    for f3 in (0,1):
     for f4 in (0,1):
      for f5 in (0,1):
       for f6 in (0,1):
        rem=d-f3-f4-f5-f6
        if rem<0: continue
        for e0 in range(rem+1):
         for e1 in range(rem-e0+1): out.append((e0,e1,rem-e0-e1,f3,f4,f5,f6))
    return out
GB7=basis(7); GB6=basis(6); IDX7={e:i for i,e in enumerate(GB7)}
QTERMS=[
 [(1,(2,0,0,0,0,0,0)),(1,(0,2,0,0,0,0,0)),(-1,(0,0,0,0,0,2,0))],
 [(1,(0,2,0,0,0,0,0)),(1,(0,0,2,0,0,0,0)),(-1,(0,0,0,2,0,0,0))],
 [(1,(2,0,0,0,0,0,0)),(1,(0,0,2,0,0,0,0)),(-1,(0,0,0,0,2,0,0))],
 [(1,(2,0,0,0,0,0,0)),(1,(0,2,0,0,0,0,0)),(1,(0,0,2,0,0,0,0)),(-1,(0,0,0,0,0,0,2))],
]

def from_mask(h):
    x=int(h,16); return frozenset(i for i in range(48) if (x>>i)&1)
SIGMA=from_mask(MASK)

# Exact Gaussian rationals, represented as pairs of Fraction.
def gg(a=0,b=0): return (Fraction(a),Fraction(b))
Z,O,I=gg(),gg(1),gg(0,1)
def ga(x,y): return (x[0]+y[0],x[1]+y[1])
def gs(x,y): return (x[0]-y[0],x[1]-y[1])
def gm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def gi(x):
    d=x[0]*x[0]+x[1]*x[1]; return (x[0]/d,-x[1]/d)
def gz(x): return x[0]==0 and x[1]==0
def gp(x,n):
    r=O
    while n:
        if n&1:r=gm(r,x)
        x=gm(x,x); n//=2
    return r

def rref_g(rows):
    A=[r[:] for r in rows if any(not gz(x) for x in r)]
    if not A:return [],[]
    m,n=len(A),len(A[0]); piv=[]; r=0
    for c in range(n):
        pv=next((j for j in range(r,m) if not gz(A[j][c])),None)
        if pv is None: continue
        A[r],A[pv]=A[pv],A[r]
        inv=gi(A[r][c]); A[r]=[gm(x,inv) for x in A[r]]; ar=A[r]
        for j in range(m):
            if j!=r and not gz(A[j][c]):
                f=A[j][c]; A[j]=[gs(A[j][k],gm(f,ar[k])) for k in range(n)]
        piv.append(c); r+=1
        if r==m: break
    return A[:r],piv

def nodes_exact():
    out=[]
    for j in range(3):
     for sa in (1,-1):
      for s1 in (1,-1):
       for s2 in (1,-1):
        z=[Z]*7; z[j]=gg(sa); o=[t for t in range(3) if t!=j]
        z[3+o[0]],z[3+o[1]],z[6]=gg(s1),gg(s2),O; out.append(tuple(z))
    for j in range(3):
     o=[t for t in range(3) if t!=j]; a,b=o
     for sr in (1,-1):
      for ep in (1,-1):
       for eq in (1,-1):
        z=[Z]*7; z[a]=O; z[b]=gm(I,gg(sr)); z[3+a]=gm(I,gg(ep)); z[3+b]=gg(-eq*sr); out.append(tuple(z))
    req(len(out)==48 and len(set(out))==48,"48 exact nodes"); return out
VE=nodes_exact()

def pmul_g(A,B,cut):
    C={}
    for a,ca in A.items():
     for b,cb in B.items():
      m=tuple(a[i]+b[i] for i in range(6))
      if sum(m)<cut: C[m]=ga(C.get(m,Z),gm(ca,cb))
    return {m:c for m,c in C.items() if not gz(c)}
def mon_local_g(exp,pt,cut):
    j0=next(j for j,x in enumerate(pt) if not gz(x)); iv=gi(pt[j0]); pp=[gm(x,iv) for x in pt]
    vm={}; k=0
    for j in range(7):
        if j==j0: vm[j]=None
        else: vm[j]=k; k+=1
    A={(0,0,0,0,0,0):O}
    for j,e in enumerate(exp):
        if not e or j==j0: continue
        B={}
        for u in range(min(e,cut-1)+1):
            m=[0]*6; m[vm[j]]=u; B[tuple(m)]=gm(gg(comb(e,u)),gp(pp[j],e-u))
        A=pmul_g(A,B,cut)
    return A
def poly_local_g(terms,pt,cut):
    out={}
    for cf,e in terms:
     for m,c in mon_local_g(e,pt,cut).items(): out[m]=ga(out.get(m,Z),gm(gg(cf),c))
    return {m:c for m,c in out.items() if not gz(c)}
def relation_rref_g(pt,cut=4):
    U=monoms_upto(6,cut-1); UI={m:i for i,m in enumerate(U)}; MUL=monoms_upto(6,cut-2)
    def vec(poly):
        v=[Z]*len(U)
        for m,c in poly.items(): v[UI[m]]=c
        return v
    rel=[]
    for qt in QTERMS:
        q=poly_local_g(qt,pt,cut)
        for b in MUL:
            s={}
            for m,c in q.items():
                mm=tuple(m[i]+b[i] for i in range(6))
                if sum(mm)<cut:s[mm]=c
            if s:rel.append(vec(s))
    return rref_g(rel),U,UI

def section_local_vec_g(sparse,pt,cut=4):
    U=monoms_upto(6,cut-1); UI={m:i for i,m in enumerate(U)}; out={}
    for idx,(re,im) in sparse.items():
        cf=gg(re,im)
        for m,c in mon_local_g(GB7[idx],pt,cut).items(): out[m]=ga(out.get(m,Z),gm(cf,c))
    v=[Z]*len(U)
    for m,c in out.items():v[UI[m]]=c
    return v
def in_span_g(v,R,piv):
    v=v[:]
    for row,p in zip(R,piv):
        if not gz(v[p]):
            f=v[p]; v=[gs(v[j],gm(f,row[j])) for j in range(len(v))]
    return all(gz(x) for x in v)

# Explicit integral Gaussian sections; keys are indices in the deterministic GB7 order.
F={0:(0,2),1:(4,0),2:(0,-4),8:(4,0),9:(0,-8),10:(-4,0),15:(0,-4),16:(-4,0),64:(-3,0),65:(0,4),66:(3,0),71:(0,4),72:(8,0),73:(0,-4),77:(3,0),78:(0,-4),114:(1,0),116:(-1,0),127:(-1,0),163:(0,2),205:(1,0),207:(-1,0),216:(-1,0),253:(0,2),290:(0,-2),325:(2,0)}
G={0:(0,-2),1:(2,0),2:(0,-2),8:(2,0),9:(0,-4),10:(-2,0),15:(0,-2),16:(-2,0),64:(3,0),65:(0,2),66:(3,0),71:(0,2),72:(4,0),73:(0,-2),77:(3,0),78:(0,-2),113:(0,2),114:(-1,0),116:(-1,0),126:(0,-2),127:(-1,0),162:(-4,0),164:(-2,0),198:(0,2),200:(0,-2),205:(-1,0),207:(-1,0),216:(-1,0),247:(-4,0),258:(-2,0),283:(0,-2),285:(0,2),294:(0,2),319:(4,0)}

# Modular linear algebra.
def rref_mod(M,p=P):
    A=[[x%p for x in row] for row in M if any(x%p for x in row)]
    if not A:return [],[]
    m,n=len(A),len(A[0]); piv=[]; r=0
    for c in range(n):
        pv=next((j for j in range(r,m) if A[j][c]),None)
        if pv is None: continue
        A[r],A[pv]=A[pv],A[r]
        iv=pow(A[r][c],p-2,p); A[r]=[(x*iv)%p for x in A[r]]; ar=A[r]
        for j in range(m):
            if j!=r and A[j][c]:
                f=A[j][c]; A[j]=[(A[j][k]-f*ar[k])%p for k in range(n)]
        piv.append(c); r+=1
        if r==m: break
    return A[:r],piv
def null_mod(M,p=P):
    R,piv=rref_mod(M,p); n=len(M[0]); free=[j for j in range(n) if j not in piv]; out=[]
    for f in free:
        v=[0]*n; v[f]=1
        for k,p in enumerate(piv):v[p]=(-R[k][f])%P
        out.append(v)
    return out

def nodes_mod():
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
        z=[0]*7; z[a]=1; z[b]=II*sr%P; z[3+a]=II*ep%P; z[3+b]=(-eq*sr)%P; out.append(tuple(z))
    req(len(out)==48 and len(set(out))==48,"48 modular nodes"); return out
VM=nodes_mod()

def local_rows_mod(pt,d,cut):
    U=monoms_upto(6,cut-1); UI={m:i for i,m in enumerate(U)}; MUL=monoms_upto(6,cut-2); GB=basis(d)
    def pmul(A,B):
        C={}
        for a,ca in A.items():
         for b,cb in B.items():
          m=tuple(a[i]+b[i] for i in range(6))
          if sum(m)<cut:C[m]=(C.get(m,0)+ca*cb)%P
        return {m:c for m,c in C.items() if c}
    def ml(exp):
        j0=next(j for j,x in enumerate(pt) if x); iv=pow(pt[j0],P-2,P); pp=[x*iv%P for x in pt]
        vm={}; k=0
        for j in range(7):
            if j==j0:vm[j]=None
            else:vm[j]=k;k+=1
        A={(0,0,0,0,0,0):1}
        for j,e in enumerate(exp):
            if not e or j==j0:continue
            B={}
            for u in range(min(e,cut-1)+1):
                m=[0]*6;m[vm[j]]=u;B[tuple(m)]=comb(e,u)*pow(pp[j],e-u,P)%P
            A=pmul(A,B)
        return A
    def pl(terms):
        out={}
        for cf,e in terms:
         for m,c in ml(e).items():out[m]=(out.get(m,0)+cf*c)%P
        return {m:c for m,c in out.items() if c}
    def vec(poly):
        v=[0]*len(U)
        for m,c in poly.items():v[UI[m]]=c
        return v
    rel=[]
    for qt in QTERMS:
        q=pl(qt)
        for b in MUL:
            s={}
            for m,c in q.items():
                mm=tuple(m[i]+b[i] for i in range(6))
                if sum(mm)<cut:s[mm]=c
            if s:rel.append(vec(s))
    RR,piv=rref_mod(rel); W=null_mod(RR)
    req(len(W)==cut*cut,f"A1 quotient length {cut*cut}")
    cols=[vec(ml(e)) for e in GB]; rows=[]
    for w in W:rows.append([sum(w[i]*col[i] for i in range(len(U)))%P for col in cols])
    return rows

def global_jet_rank(d,cut):
    rows=[]
    for idx in sorted(SIGMA):rows.extend(local_rows_mod(VM[idx],d,cut))
    return len(rref_mod(rows)[1])

def sparse_mod(s):
    v=[0]*len(GB7)
    for idx,(a,b) in s.items():v[idx]=(a+b*II)%P
    return v

def mult_L_rows_mod():
    rows=[]
    for e in GB6:
        v=[0]*len(GB7)
        # -a1-a2-i*a3
        for j,cf in ((0,-1),(1,-1),(2,-II)):
            ee=list(e);ee[j]+=1;ee=tuple(ee);v[IDX7[ee]]=(v[IDX7[ee]]+cf)%P
        # +c, reducing c^2 by q4 if needed
        if e[6]==0:
            ee=list(e);ee[6]+=1;ee=tuple(ee);v[IDX7[ee]]=(v[IDX7[ee]]+1)%P
        else:
            base=list(e);base[6]-=1
            for j in (0,1,2):
                ee=base[:];ee[j]+=2;ee=tuple(ee);v[IDX7[ee]]=(v[IDX7[ee]]+1)%P
        rows.append(v)
    return rows

def q0_restriction(s):
    # Q0: b1=0, a3=i*a2, c=a1. Basis key=(a1exp,a2exp,b2exp,b3exp).
    out={}
    for idx,(re,im) in s.items():
        e=GB7[idx]
        if e[3]:continue
        cf=gg(re,im); cf=gm(cf,gp(I,e[2]))
        key=(e[0]+e[6],e[1]+e[2],e[4],e[5]);out[key]=ga(out.get(key,Z),cf)
    return {k:v for k,v in out.items() if not gz(v)}

def main():
    cert=json.loads(CERT.read_text()); req(cert["schema"]=="STAGE32_MB104_BALANCED16_000707_PRIMITIVE_RANK_V1","schema"); preflight(cert)
    req(len(SIGMA)==14,"support size"); req(len(GB7)==344 and len(GB6)==248,"canonical dimensions"); req(II*II%P==P-1,"i specialization")

    # Exact support hyperplane and exact membership of F,G in m_p^4 at all 14 nodes.
    for idx in sorted(SIGMA):
        a1,a2,a3,b1,b2,b3,c=VE[idx]
        req(gz(gs(gs(gs(c,a1),a2),gm(I,a3))),f"support hyperplane node {idx}")
        (R,piv),U,UI=relation_rref_g(VE[idx],4)
        req(len(piv)==68 and len(U)-len(piv)==16,f"A1 order4 quotient node {idx}")
        req(in_span_g(section_local_vec_g(F,VE[idx],4),R,piv),f"F m4 node {idx}")
        req(in_span_g(section_local_vec_g(G,VE[idx],4),R,piv),f"G m4 node {idx}")

    r63=global_jet_rank(6,3); r74=global_jet_rank(7,4)
    req((r63,r74)==(126,220),"modular jet ranks")

    LR=mult_L_rows_mod(); rL=len(rref_mod(LR)[1]); rLFG=len(rref_mod(LR+[sparse_mod(F),sparse_mod(G)])[1])
    req((rL,rLFG)==(248,250),"L/F/G independence")

    q0=q0_restriction(F)
    expected={
      (0,7,0,0):gg(2),
      (0,6,0,1):gg(2),
      (2,4,0,1):gg(-1),
      (0,6,1,0):gg(0,2),
      (2,4,1,0):gg(0,1),
      (0,5,1,1):gg(0,2),
    }
    req(q0==expected,"exact nonzero Q0 restriction")

    # RR arithmetic used in the human consequence.
    C2=6*6*16-14*3*3*2; KC=6*16; chiC=8+(C2-KC)//2
    A2=7*7*16-14*4*4*2; KA=7*16; chiA=8+(A2-KA)//2
    req((C2,KC,chiC)==(324,96,122),"C RR")
    req((A2,KA,chiA)==(336,112,120),"A RR")

    cc=cert["char0_consequence"]
    req(cc["h0_C"]==122 and cc["h1_C"]==0,"C consequence")
    req(cc["h0_A"]==124 and cc["h1_A"]==4 and cc["jet_rank_A"]==220,"A consequence")
    req(cc["Q0_Q1_nonfixed_all_l"] is True,"nonfixed consequence")
    req(cert["credit_firewall"]["closes_support_orbit"] is False,"no closure")
    print("PASS STAGE32_MB104_BALANCED16_000707_PRIMITIVE_RANK_V1")
    print("degree6 triple jets rank=126 => h0(C)=122; L multiplication injective")
    print("explicit exact F,G in m^4; rank(L*R6,F,G)=250 => h0(A)>=124")
    print("degree7 four-jets rank=220 => h0(A)=124,h1(A)=4")
    print("F|Q0 != 0; stabilizer transport and powers => Q0,Q1 nonfixed for all l>=1")
if __name__=="__main__": main()
