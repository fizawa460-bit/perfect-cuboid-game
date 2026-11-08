# evaluate every F_p point of the part-C systems: W = net member, |Omega|, then Singular irreducibility/smoothness
import sys, itertools, importlib.util, re
P=int(sys.argv[1]); I=int(sys.argv[2]); sys.argv=['pwfam.py',str(P),str(I),'0','/dev/null']
spec=importlib.util.spec_from_file_location('pwfam','pwfam.py'); pf=importlib.util.module_from_spec(spec); spec.loader.exec_module(pf)
Mt=[p for p in range(36) if pf.TY[p//6]==pf.TY[p%6]]
nets={}; n=0
for S in itertools.combinations(Mt,6):
    ns=pf.nullspace([pf.R[p] for p in S])
    if len(ns)!=3: continue
    n+=1; nets[n]=ns
pts=set()
for l in open(sys.argv_file if False else f'slack0C_dec_{P}.out'):
    m=re.match(r'PRIME (\d+)\s+1\s+(.*)',l)
    if not m: continue
    k=int(m.group(1)); gens=m.group(2).split(',')
    # solve the two linear forms in l0,l1,l2
    rows=[]
    for g in gens:
        c=[0,0,0]
        for sgn,coef,var in re.findall(r'([+-]?)(\d*)\*?(l[012])',g.replace(' ','')):
            v=int(coef) if coef else 1
            c[int(var[1])]=(c[int(var[1])]+(-v if sgn=='-' else v))%P
        rows.append(c)
    a,b=rows; sol=[(a[1]*b[2]-a[2]*b[1])%P,(a[2]*b[0]-a[0]*b[2])%P,(a[0]*b[1]-a[1]*b[0])%P]
    pts.add((k,tuple(sol)))
hits=[]
for k,sol in pts:
    ns=nets[k]; w=[(sol[0]*ns[0][m]+sol[1]*ns[1][m]+sol[2]*ns[2][m])%P for m in range(9)]
    om,sp,vl,npt=pf.omega([pf.F(x) for x in w])
    if om<=4 and not vl: hits.append((k,om,sp,npt,w))
print('points',len(pts),'hits',len(hits))
out=[f'LIB "elim.lib"; ring r={P},(X0,X1,Y0,Y1),dp; list F; poly W; int irr=0; ideal J; proc sat2(ideal I0, ideal Q) {{ def T = sat(I0, Q); ideal R2; if (typeof(T) == "list") {{ R2 = T[1]; }} else {{ R2 = T; }} return(std(R2)); }}']
for k,om,sp,npt,w in hits:
    out.append(f'W={pf.polystr(w)}; F=factorize(W); if (size(F[1])==2 && F[2][2]==1) {{ irr++; J=W,jacob(W); J=sat2(J,ideal(X0,X1)); J=sat2(J,ideal(Y0,Y1)); "IRRED net {k} om {om} sp {sp} npts {npt} singdim", dim(J); }}')
out.append('"irreducible hits",irr; quit;'); open(f's0C_{P}.sing','w').write('\n'.join(out))
