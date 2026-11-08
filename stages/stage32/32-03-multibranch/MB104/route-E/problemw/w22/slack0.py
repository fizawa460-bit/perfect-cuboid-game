# Problem W (2,2), both slacks 0.  2j + h >= 12.  Node off BxB: >= 8 points (done, w22g mode 0); exactly 7 points with
# j >= 5 (part B, pencils); exactly 6 points, all matched (part C, nets -> Singular).  Node on BxB with >= 5 more points
# (done, modes 1/2); node + exactly 4 more points: j = 6 forces a matched node and 4 matched points (part D, pencils).
# In parts B and D only members with |O1| = |O2| = 8 matter (S >= 1 is done), i.e. t a common root of >= 2 x-fibre and
# >= 2 y-fibre discriminants.  usage: slack0.py P I
import sys, itertools, importlib.util
from collections import defaultdict
P=int(sys.argv[1]); I=int(sys.argv[2])
def load(node):
    sys.argv=['pwfam.py',str(P),str(I),str(node),'/dev/null']
    spec=importlib.util.spec_from_file_location('pwfam%d'%node,'pwfam.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
pf=load(0)
def tsqrt(a):  # Tonelli-Shanks
    a%=P
    if a==0: return 0
    if pow(a,(P-1)//2,P)!=1: return None
    q,s=P-1,0
    while q%2==0: q//=2; s+=1
    z=pf.NR; m,c,t,r=s,pow(z,q,P),pow(a,q,P),pow(a,(q+1)//2,P)
    while t!=1:
        i,t2=0,t
        while t2!=1: t2=t2*t2%P; i+=1
        b=pow(c,1<<(m-i-1),P); m,c,t,r=i,b*b%P,t*b*b%P,r*b%P
    return r
pf.sqrtp=tsqrt
def fibq(A,B,bb,axis):
    X0,X1=pf.ptc(bb); qa=[];qb=[]
    for kk in range(3):
        sa=sb=0
        for l2 in range(3):
            m=3*l2+kk if axis==0 else 3*kk+l2
            v=pow(X0,l2,P)*pow(X1,2-l2,P); sa+=A[m]*v; sb+=B[m]*v
        qa.append(sa%P); qb.append(sb%P)
    return pf.quadcoef(qa,qb)
def pencil_hits(pfm,A,B,tag):
    cnt=[defaultdict(set),defaultdict(set)]; always=[set(),set()]
    for bb in range(6):
        for axis in (0,1):
            c=fibq(A,B,bb,axis)
            if all(x%P==0 for x in c): always[axis].add(bb); continue
            for r in pf.roots_quad(*c): cnt[axis][r].add(bb)
    ts=set(cnt[0])|set(cnt[1])
    out=[]
    for t in ts:
        if len(cnt[0][t]|always[0])>=2 and len(cnt[1][t]|always[1])>=2:
            w=[pf.add(pf.F(A[m]),pf.mul(t,pf.F(B[m]))) for m in range(9)]
            om,sp,vl,n=pfm.omega(w)
            if om<=4 and not vl: out.append((tag,t,om,sp,n,w))
    # t = infinity and the whole pencil (if >= 2 discriminants vanish identically on both axes)
    for w,t in (([pf.F(B[m]) for m in range(9)],'inf'),([pf.F(A[m]+7*B[m]) for m in range(9)],'gen')):
        if t=='gen' and not (len(always[0])>=2 and len(always[1])>=2): continue
        om,sp,vl,n=pfm.omega(w)
        if om<=4 and not vl: out.append((tag,t,om,sp,n,w))
    return out
Mt=[p for p in range(36) if pf.TY[p//6]==pf.TY[p%6]]; U=[p for p in range(36) if p not in Mt]
hits=[]; npen=0; nnet=[]
# part B: 7 points, >= 5 matched
for k in (5,6,7):
    for Sm in itertools.combinations(Mt,k):
        for Su in itertools.combinations(U,7-k):
            S=Sm+Su; ns=pf.nullspace([pf.R[p] for p in S])
            if len(ns)!=2: nnet.append(S); continue
            npen+=1; hits+=pencil_hits(pf,ns[0],ns[1],('B',S))
print('part B pencils',npen,'higher-dim (skipped here, listed)',len(nnet),'hits',len(hits))
# part D: node at (0,0) (matched, labels std) + 4 more matched points
pn=load(1); pn.sqrtp=tsqrt; nD=0; hD=0
for S in itertools.combinations([p for p in Mt if p!=0],4):
    ns=pn.nullspace(pn.BASE+[pn.R[p] for p in S])
    if len(ns)!=2: nnet.append(('D',S)); continue
    nD+=1; h=pencil_hits(pn,ns[0],ns[1],('D',S)); hD+=len(h); hits+=h
print('part D pencils',nD,'hits',hD)
# part C: 6 matched points -> net; Singular script: for every pair of x-discriminants and pair of y-discriminants,
# the common zeros in the net P^2.
out=[f'ring r={P},(l0,l1,l2),dp; ideal Jc; int ne=0;']
nC=0
for S in itertools.combinations(Mt,6):
    ns=pf.nullspace([pf.R[p] for p in S])
    if len(ns)!=3: nnet.append(('C',S)); continue
    nC+=1
    W=[f'({ns[0][m]}*l0+{ns[1][m]}*l1+{ns[2][m]}*l2)' for m in range(9)]
    D=[]
    for axis in (0,1):
        for bb in range(6):
            X0,X1=pf.ptc(bb); q=[]
            for kk in range(3):
                terms=[]
                for l2 in range(3):
                    m=3*l2+kk if axis==0 else 3*kk+l2
                    v=pow(X0,l2,P)*pow(X1,2-l2,P)%P
                    if v: terms.append(f'{v}*{W[m]}')
                q.append('+'.join(terms) or '0')
            D.append(f'({q[1]})^2-4*({q[0]})*({q[2]})')
    out.append(f'list Dx{nC}={",".join(D[:6])}; list Dy{nC}={",".join(D[6:])};')
    out.append(f'for (int a{nC}=1;a{nC}<=5;a{nC}++) {{ for (int b{nC}=a{nC}+1;b{nC}<=6;b{nC}++) {{ for (int c{nC}=1;c{nC}<=5;c{nC}++) {{ for (int d{nC}=c{nC}+1;d{nC}<=6;d{nC}++) {{ Jc=std(ideal(Dx{nC}[a{nC}],Dx{nC}[b{nC}],Dy{nC}[c{nC}],Dy{nC}[d{nC}])); if (dim(Jc)>0) {{ ne++; "NONEMPTY {nC} {" ".join(map(str,S))}", a{nC},b{nC},c{nC},d{nC}, " dim", dim(Jc), " deg", mult(Jc); }} }} }} }} }}')
out.append('"part C nets",'+str(nC)+'," nonempty systems",ne; quit;')
open(f'slack0C_{P}.sing','w').write('\n'.join(out))
print('part C nets',nC,'; other higher-dim families',len(nnet))
import pickle; pickle.dump((hits,nnet),open(f'slack0_{P}.pkl','wb'))
# irreducibility / smoothness of F_p hits
out=[f'LIB "elim.lib"; ring r={P},(X0,X1,Y0,Y1),dp; list F; poly W; int irr=0; ideal J; proc sat2(ideal I0, ideal Q) {{ def T = sat(I0, Q); ideal R2; if (typeof(T) == "list") {{ R2 = T[1]; }} else {{ R2 = T; }} return(std(R2)); }}']
for tag,t,om,sp,n,w in hits:
    if any(c[1] for c in w): print('FP2-HIT',tag,t,om); continue
    out.append(f'W={pf.polystr([c[0] for c in w])}; F=factorize(W); if (size(F[1])==2 && F[2][2]==1) {{ irr++; J=W,jacob(W); J=sat2(J,ideal(X0,X1)); J=sat2(J,ideal(Y0,Y1)); "IRRED {tag[0]} om {om} sp {sp} npts {n} singdim", dim(J); }}')
out.append('"irreducible hits",irr; quit;')
open(f'slack0BD_{P}.sing','w').write('\n'.join(out))
