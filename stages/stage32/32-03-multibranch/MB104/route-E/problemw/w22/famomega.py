# For each coprime pencil W_t = A + t*B (and B), compute |Omega| at the generic member and at every event value of t
# (extra point of BxB on W_t: linear in t; a fibre discriminant vanishing: quadratic in t), over F_p or F_{p^2}.
import sys
from fam import P, row, nullspace
NR=next(n for n in range(2,P) if pow(n,(P-1)//2,P)==P-1)   # non-residue; F_{p^2} = F_p[s]/(s^2-NR)
def add(a,b): return ((a[0]+b[0])%P,(a[1]+b[1])%P)
def sub(a,b): return ((a[0]-b[0])%P,(a[1]-b[1])%P)
def mul(a,b): return ((a[0]*b[0]+NR*a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0])%P)
def isz(a): return a[0]==0 and a[1]==0
def F(x): return (x%P,0)
TY=[0,0,1,1,2,2]
from fam import pt as ptc
def fib(w,bx,axis):  # quadratic coefficients of W restricted to x=beta (axis 0) or y=beta (axis 1); w: 9 field elements
    X0,X1=ptc(bx); q=[]
    for k in range(3):
        s=(0,0)
        for l in range(3):
            m=3*l+k if axis==0 else 3*k+l
            s=add(s,mul(w[m],F(pow(X0,l,P)*pow(X1,2-l,P))))
        q.append(s)
    return q
def disc(q): return sub(mul(q[1],q[1]),mul(F(4),mul(q[0],q[2])))
R=[row(p) for p in range(36)]
def omega(w):
    on=[]
    for p in range(36):
        s=(0,0)
        for m in range(9): s=add(s,mul(w[m],F(R[p][m])))
        on.append(isz(s))
    O1=O2=j=h=0; sp=vl=0; dx=[0]*6; dy=[0]*6
    for b in range(6):
        q=fib(w,b,0)
        if all(isz(c) for c in q): vl=1
        else:
            dx[b]=not isz(disc(q)); O1+=2*dx[b]
        q=fib(w,b,1)
        if all(isz(c) for c in q): vl=1
        else:
            dy[b]=not isz(disc(q)); O2+=2*dy[b]
    for p in range(36):
        if on[p]:
            bx,by=divmod(p,6)
            if dx[bx] and dy[by]:
                if TY[bx]==TY[by]: j+=1
                else: h+=1
            elif not dx[bx] and not dy[by]: sp=1
    return O1+O2-2*j-h,sp,vl,sum(on)
def sqrtp(a):  # sqrt in F_p (Tonelli via p = 1 mod 8: use pow brute for small p)
    a%=P
    for x in range(P):
        if x*x%P==a: return x
    return None
SQ={}
def sqrt_cached(a):
    a%=P
    if a not in SQ: SQ[a]=sqrtp(a)
    return SQ[a]
def roots_quad(a,b,c):  # roots of a t^2 + b t + c in F_{p^2} (a,b,c in F_p)
    a%=P;b%=P;c%=P
    if a==0:
        return [] if b==0 else [F(-c*pow(b,P-2,P))]
    D=(b*b-4*a*c)%P; i2a=pow(2*a,P-2,P)
    if pow(D,(P-1)//2,P) in (0,1):
        r=sqrt_cached(D); return [F((-b+r)*i2a),F((-b-r)*i2a)]
    u=sqrt_cached(D*pow(NR,P-2,P)); # sqrt(D) = u*s
    return [((-b*i2a)%P,(u*i2a)%P),((-b*i2a)%P,(-u*i2a)%P)]
def famlines():
    seen=set()
    for l in open('w22.out'):
        if l.startswith('FAMILY'):
            pts=tuple(map(int,l.split()[4:]))
            if pts not in seen: seen.add(pts); yield pts
copr=set()
for l in open('fam.out'):
    if l.startswith('COPRIME'): copr.add(int(l.split()[1]))
res={}; hits=[]
for k,pts in enumerate(famlines()):
    if k not in copr: continue
    A,B=nullspace([R[p] for p in pts])
    ts=set()
    for p in range(36):
        a=sum(A[m]*R[p][m] for m in range(9))%P; b=sum(B[m]*R[p][m] for m in range(9))%P
        if b: ts.add(F(-a*pow(b,P-2,P)))
    for bx in range(6):
        for axis in (0,1):
            # fibre coefficients are linear in t: q_k = qa_k + t qb_k; disc is quadratic in t
            X0,X1=ptc(bx); qa=[];qb=[]
            for kk in range(3):
                sa=sb=0
                for l in range(3):
                    m=3*l+kk if axis==0 else 3*kk+l
                    v=pow(X0,l,P)*pow(X1,2-l,P)
                    sa+=A[m]*v; sb+=B[m]*v
                qa.append(sa%P); qb.append(sb%P)
            # disc = (qa1+t qb1)^2 - 4 (qa0+t qb0)(qa2+t qb2)
            c2=qb[1]*qb[1]-4*qb[0]*qb[2]; c1=2*qa[1]*qb[1]-4*(qa[0]*qb[2]+qb[0]*qa[2]); c0=qa[1]*qa[1]-4*qa[0]*qa[2]
            for r in roots_quad(c2,c1,c0): ts.add(r)
    gen=omega([F(A[m]+7*B[m]) for m in range(9)])  # a generic-looking member (t=7)
    vals=[(omega([add(F(A[m]),mul(t,F(B[m]))) for m in range(9)]),t) for t in ts]
    vals.append((omega([F(B[m]) for m in range(9)]),'inf'))
    best=min(v[0][0] for v in vals+[(gen,None)])
    res[best]=res.get(best,0)+1
    for (om,sp,vl,n),t in vals+[(gen,'gen')]:
        if om<=4 and not vl: hits.append((k,pts,t,om,sp,n))
print('pencils',sum(res.values()),'min-omega distribution',sorted(res.items()))
print('hits (om<=4, no vertical line):',len(hits))
with open('famhits.txt','w') as f:
    for x in hits: f.write(repr(x)+'\n')
