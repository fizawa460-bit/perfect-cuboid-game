import sys
P=10009; I=pow(792,2,P)
xs=[0,None,1,P-1,I,(-I)%P]
def pt(b): return (0,1) if xs[b] is None else (1,xs[b])
def row(p):
    bx,by=divmod(p,6); X0,X1=pt(bx); Y0,Y1=pt(by)
    return [pow(X0,a,P)*pow(X1,2-a,P)*pow(Y0,b,P)*pow(Y1,2-b,P)%P for a in range(3) for b in range(3)]
def nullspace(rows):
    M=[r[:] for r in rows]; piv=[]; r=0
    for c in range(9):
        k=next((i for i in range(r,len(M)) if M[i][c]),None)
        if k is None: continue
        M[r],M[k]=M[k],M[r]; f=pow(M[r][c],P-2,P); M[r]=[v*f%P for v in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]:
                g=M[i][c]; M[i]=[(a-g*b)%P for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
    free=[c for c in range(9) if c not in piv]; out=[]
    for f in free:
        v=[0]*9; v[f]=1
        for i,c in enumerate(piv): v[c]=(-M[i][f])%P
        out.append(v)
    return out
def poly(w):
    t=[f"{w[3*a+b]}*X0^{a}*X1^{2-a}*Y0^{b}*Y1^{2-b}" for a in range(3) for b in range(3) if w[3*a+b]]
    return '+'.join(t) if t else '0'
seen=set(); out=['ring r=10009,(X0,X1,Y0,Y1),dp; int n0=0; int n1=0; poly g;']
k=0
for l in open('w22.out'):
    if not l.startswith('FAMILY'): continue
    pts=tuple(map(int,l.split()[4:]))
    if pts in seen: continue
    seen.add(pts)
    ns=nullspace([row(p) for p in pts])
    assert len(ns)==2,(pts,len(ns))
    out.append(f"g=gcd({poly(ns[0])},{poly(ns[1])}); if (deg(g)>0) {{n1++;}} else {{n0++; \"COPRIME {k} npts {len(pts)} : {' '.join(map(str,pts))}\";}}")
    k+=1
out.append('"families",'+str(k)+'," with common factor",n1," coprime",n0; quit;')
open('fam.sing','w').write('\n'.join(out)); print('unique families',k)
