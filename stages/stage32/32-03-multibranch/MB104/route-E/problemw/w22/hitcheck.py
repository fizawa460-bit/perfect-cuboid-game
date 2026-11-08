import ast, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import fam
from fam import P,row,nullspace,poly
H=[ast.literal_eval(l) for l in open('famhits.txt')]
R=[row(p) for p in range(36)]
out=['ring r=10009,(X0,X1,Y0,Y1),dp; list F; int irr=0;']
for n,(k,pts,t,om,sp,npt) in enumerate(H):
    A,B=nullspace([R[p] for p in pts])
    if t=='inf': w=B
    elif t=='gen': w=[(a+7*b)%P for a,b in zip(A,B)]
    else: w=[(a+t[0]*b)%P for a,b in zip(A,B)]
    out.append(f'F=factorize({poly(w)}); if (size(F[1])==2 && F[2][2]==1) {{ irr++; "IRRED {n} t {t} om {om} sp {sp} npts {npt}"; }}')
out.append('"irreducible members:",irr; quit;')
open('hit.sing','w').write('\n'.join(out))
