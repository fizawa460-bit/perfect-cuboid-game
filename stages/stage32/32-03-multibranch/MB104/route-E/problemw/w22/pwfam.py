# Pencil analysis for w22g output.  usage: pwfam.py P I NODE infile
# For every FAMILY (rank 7 incl. node base rows) whose two generators are coprime, |Omega| is evaluated at all event
# values of t (extra point: linear; fibre discriminant: quadratic; node Hessian discriminant: quadratic) over F_p / F_p^2.
import sys
P=int(sys.argv[1]); I=int(sys.argv[2]); NODE=int(sys.argv[3]); INF=sys.argv[4]
xs=[0,None,1,P-1,I,(-I)%P]; TY=[0,0,1,1,2,2]; TYY=[1,1,0,0,2,2] if NODE==2 else TY
NR=next(n for n in range(2,P) if pow(n,(P-1)//2,P)==P-1)
def ptc(b): return (0,1) if xs[b] is None else (1,xs[b])
def row(p):
    bx,by=divmod(p,6); X0,X1=ptc(bx); Y0,Y1=ptc(by)
    return [pow(X0,a,P)*pow(X1,2-a,P)*pow(Y0,b,P)*pow(Y1,2-b,P)%P for a in range(3) for b in range(3)]
R=[row(p) for p in range(36)]
BASE=[[1 if m==c else 0 for m in range(9)] for c in (8,5,7)] if NODE else []
def nullspace(rows):
    M=[r[:] for r in rows]; piv=[]; r=0
    for c in range(9):
        k=next((i for i in range(r,len(M)) if M[i][c]),None)
        if k is None: continue
        M[r],M[k]=M[k],M[r]; f=pow(M[r][c],P-2,P); M[r]=[v*f%P for v in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]: g=M[i][c]; M[i]=[(a-g*b)%P for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
    out=[]
    for f in [c for c in range(9) if c not in piv]:
        v=[0]*9; v[f]=1
        for i,c in enumerate(piv): v[c]=(-M[i][f])%P
        out.append(v)
    return out
def add(a,b): return ((a[0]+b[0])%P,(a[1]+b[1])%P)
def sub(a,b): return ((a[0]-b[0])%P,(a[1]-b[1])%P)
def mul(a,b): return ((a[0]*b[0]+NR*a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0])%P)
def isz(a): return a[0]==0 and a[1]==0
def F(x): return (x%P,0)
def fib(w,b,axis):
    X0,X1=ptc(b); q=[]
    for k in range(3):
        s=(0,0)
        for l in range(3):
            m=3*l+k if axis==0 else 3*k+l
            s=add(s,mul(w[m],F(pow(X0,l,P)*pow(X1,2-l,P))))
        q.append(s)
    return q
def disc(q): return sub(mul(q[1],q[1]),mul(F(4),mul(q[0],q[2])))
def omega(w):
    on=[]
    for p in range(36):
        s=(0,0)
        for m in range(9): s=add(s,mul(w[m],F(R[p][m])))
        on.append(isz(s))
    O1=O2=j=h=sp=vl=0; dx=[0]*6; dy=[0]*6
    for b in range(6):
        for axis,d in ((0,dx),(1,dy)):
            q=fib(w,b,axis)
            if all(isz(c) for c in q): vl=1
            else:
                d[b]=not isz(disc(q))
                if axis==0: O1+=2*d[b]
                else: O2+=2*d[b]
    start=0
    if NODE:
        start=1; a,bq,c=w[2],w[4],w[6]
        if not isz(sub(mul(bq,bq),mul(F(4),mul(a,c)))) and not isz(a) and not isz(c):
            O1+=2; O2+=2
            if TY[0]==TYY[0]: j+=2
            else: h+=2
    for p in range(start,36):
        if on[p]:
            bx,by=divmod(p,6)
            if dx[bx] and dy[by]:
                if TY[bx]==TYY[by]: j+=1
                else: h+=1
            elif not dx[bx] and not dy[by]: sp=1
    return O1+O2-2*j-h,sp,vl,sum(on)
SQ={}
def sqrtp(a):
    a%=P
    if a not in SQ: SQ[a]=next((x for x in range(P) if x*x%P==a),None)
    return SQ[a]
def roots_quad(a,b,c):
    a%=P;b%=P;c%=P
    if a==0: return [] if b==0 else [F(-c*pow(b,P-2,P))]
    D=(b*b-4*a*c)%P; i2a=pow(2*a,P-2,P)
    if pow(D,(P-1)//2,P) in (0,1): r=sqrtp(D); return [F((-b+r)*i2a),F((-b-r)*i2a)]
    u=sqrtp(D*pow(NR,P-2,P)); return [((-b*i2a)%P,(u*i2a)%P),((-b*i2a)%P,(-u*i2a)%P)]
def quadcoef(qa,qb):  # disc of (qa + t qb) as polynomial in t
    return (qb[1]*qb[1]-4*qb[0]*qb[2], 2*qa[1]*qb[1]-4*(qa[0]*qb[2]+qb[0]*qa[2]), qa[1]*qa[1]-4*qa[0]*qa[2])
def polystr(w):
    return '+'.join(f"{w[3*a+b]}*X0^{a}*X1^{2-a}*Y0^{b}*Y1^{2-b}" for a in range(3) for b in range(3) if w[3*a+b]) or '0'
fams=[]; seen=set()
for l in open(INF):
    if l.startswith('FAMILY'):
        pts=tuple(map(int,l.split()[4:]))
        if pts not in seen: seen.add(pts); fams.append(pts)
hits=[]; gens=[]
for k,pts in enumerate(fams):
    A,B=nullspace(BASE+[R[p] for p in pts])
    gens.append((A,B))
    ts=set()
    for p in range(36):
        a=sum(A[m]*R[p][m] for m in range(9))%P; b=sum(B[m]*R[p][m] for m in range(9))%P
        if b: ts.add(F(-a*pow(b,P-2,P)))
    for bb in range(6):
        for axis in (0,1):
            X0,X1=ptc(bb); qa=[];qb=[]
            for kk in range(3):
                sa=sb=0
                for l2 in range(3):
                    m=3*l2+kk if axis==0 else 3*kk+l2
                    v=pow(X0,l2,P)*pow(X1,2-l2,P); sa+=A[m]*v; sb+=B[m]*v
                qa.append(sa%P); qb.append(sb%P)
            for r in roots_quad(*quadcoef(qa,qb)): ts.add(r)
    if NODE:
        for r in roots_quad(*quadcoef([A[2],A[4],A[6]],[B[2],B[4],B[6]])): ts.add(r)
        for c in (2,6):
            if B[c]: ts.add(F(-A[c]*pow(B[c],P-2,P)))
    cands=[([add(F(A[m]),mul(t,F(B[m]))) for m in range(9)],t) for t in ts]+[([F(B[m]) for m in range(9)],'inf'),([F(A[m]+7*B[m]) for m in range(9)],'gen')]
    for w,t in cands:
        om,sp,vl,n=omega(w)
        if om<=4 and not vl and all(c[1]==0 for c in w): hits.append((k,t,om,sp,n,[c[0] for c in w]))
        elif om<=4 and not vl: hits.append((k,t,om,sp,n,None))
print('families',len(fams),'hits',len(hits),'in F_p^2 (not checked by factorization):',sum(1 for h in hits if h[5] is None))
# Singular: coprimality of the generators and irreducibility of each F_p hit
out=[f'ring r={P},(X0,X1,Y0,Y1),dp; list F; poly g; int irr=0;']
for k,t,om,sp,n,w in hits:
    A,B=gens[k]
    if w is None: continue
    out.append(f'g=gcd({polystr(A)},{polystr(B)}); F=factorize({polystr(w)}); if (deg(g)==0 && size(F[1])==2 && F[2][2]==1) {{ irr++; "IRRED fam {k} t {t} om {om} sp {sp} npts {n} w {" ".join(map(str,w))}"; }}')
out.append('"irreducible hits",irr; quit;')
open(INF+'.fam.sing','w').write('\n'.join(out))
