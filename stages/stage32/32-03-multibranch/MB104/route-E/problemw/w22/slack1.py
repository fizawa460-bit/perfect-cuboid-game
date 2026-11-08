# Problem W (2,2), slack sum 1 (and the 7-point part of slack 0): W through exactly 7 distinct points of BxB off its node.
# 2j + h >= 12 + 2S and j + h = 7 give j >= 5 + 2S; S = 1 forces all 7 points label-matched (7 of the 12 matched points).
# W through >= 8 points or with a node on BxB was covered by w22g (modes 0, 1, 2).  usage: slack1.py P I
import sys, itertools, importlib.util
P=int(sys.argv[1]); I=int(sys.argv[2])
sys.argv=['pwfam.py',str(P),str(I),'0','/dev/null']
spec=importlib.util.spec_from_file_location('pwfam','pwfam.py'); pf=importlib.util.module_from_spec(spec); spec.loader.exec_module(pf)
M=[p for p in range(36) if pf.TY[p//6]==pf.TY[p%6]]
assert len(M)==12
hits=[]; nets=0; pencils=0
for S in itertools.combinations(M,7):
    ns=pf.nullspace([pf.R[p] for p in S])
    if len(ns)>2: nets+=1; print('NET',S); continue
    pencils+=1; A,B=ns
    ts=set()
    for p in range(36):
        a=sum(A[m]*pf.R[p][m] for m in range(9))%P; b=sum(B[m]*pf.R[p][m] for m in range(9))%P
        if b: ts.add(pf.F(-a*pow(b,P-2,P)))
    for bb in range(6):
        for axis in (0,1):
            X0,X1=pf.ptc(bb); qa=[];qb=[]
            for kk in range(3):
                sa=sb=0
                for l2 in range(3):
                    m=3*l2+kk if axis==0 else 3*kk+l2
                    v=pow(X0,l2,P)*pow(X1,2-l2,P); sa+=A[m]*v; sb+=B[m]*v
                qa.append(sa%P); qb.append(sb%P)
            for r in pf.roots_quad(*pf.quadcoef(qa,qb)): ts.add(r)
    cands=[([pf.add(pf.F(A[m]),pf.mul(t,pf.F(B[m]))) for m in range(9)],t) for t in ts]+[([pf.F(B[m]) for m in range(9)],'inf'),([pf.F(A[m]+7*B[m]) for m in range(9)],'gen')]
    for w,t in cands:
        om,sp,vl,n=pf.omega(w)
        if om<=4 and not vl: hits.append((S,t,om,sp,n,[c for c in w]))
print('pencils',pencils,'nets',nets,'hits',len(hits),'in F_p^2:',sum(1 for h in hits if any(c[1] for c in h[5])))
out=[f'LIB "elim.lib"; ring r={P},(X0,X1,Y0,Y1),dp; list F; poly W; int irr=0; ideal J; proc sat2(ideal I0, ideal Q) {{ def T = sat(I0, Q); ideal R2; if (typeof(T) == "list") {{ R2 = T[1]; }} else {{ R2 = T; }} return(std(R2)); }}']
for S,t,om,sp,n,w in hits:
    if any(c[1] for c in w): continue
    wp=[c[0] for c in w]
    out.append(f'W={pf.polystr(wp)}; F=factorize(W); if (size(F[1])==2 && F[2][2]==1) {{ irr++; J=W,jacob(W); J=sat2(J,ideal(X0,X1)); J=sat2(J,ideal(Y0,Y1)); "IRRED om {om} sp {sp} npts {n} singdim", dim(J); }}')
out.append('"irreducible hits",irr; quit;')
open(f'slack1_{P}.sing','w').write('\n'.join(out))
