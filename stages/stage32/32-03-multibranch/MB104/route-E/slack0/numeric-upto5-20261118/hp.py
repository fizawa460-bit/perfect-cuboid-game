import mpmath as mp
mp.mp.dps=40
from common import BP
def refine(p,q,an,n,iters=8):
    """Gauss-Newton refinement in mpmath of (P,Q, crit points); returns refined an (odd pts, dbl pts) as python complex and residual"""
    ys=[y for y in range(6) for _ in an[y][1]]
    crit=[mp.mpc(z) for y in range(6) for z in an[y][1]]
    s=max(abs(v) for v in list(p)+list(q))
    co=[mp.mpc(v/s) for v in list(p)+list(q)]
    k0=max(range(2*n+2),key=lambda i:abs(co[i])); 
    Y=[(mp.mpc(BP[y][0]),mp.mpc(BP[y][1])) for y in ys]
    K=len(ys)
    for it in range(iters):
        R=[];J=[]
        for k in range(K):
            c=crit[k]; y0,y1=Y[k]
            pw=[c**m for m in range(n+1)]
            dpw=[m*c**(m-1) if m>0 else mp.mpc(0) for m in range(n+1)]
            ddpw=[m*(m-1)*c**(m-2) if m>1 else mp.mpc(0) for m in range(n+1)]
            Pc=sum(co[m]*pw[m] for m in range(n+1)); Qc=sum(co[n+1+m]*pw[m] for m in range(n+1))
            dP=sum(co[m]*dpw[m] for m in range(n+1)); dQ=sum(co[n+1+m]*dpw[m] for m in range(n+1))
            ddP=sum(co[m]*ddpw[m] for m in range(n+1)); ddQ=sum(co[n+1+m]*ddpw[m] for m in range(n+1))
            R.append(y1*Pc-y0*Qc); R.append(y1*dP-y0*dQ)
            r1=[y1*pw[m] for m in range(n+1)]+[-y0*pw[m] for m in range(n+1)]+[0]*K
            r2=[y1*dpw[m] for m in range(n+1)]+[-y0*dpw[m] for m in range(n+1)]+[0]*K
            r1[2*n+2+k]=y1*dP-y0*dQ; r2[2*n+2+k]=y1*ddP-y0*ddQ
            J.append(r1);J.append(r2)
        R.append(co[k0]-1); r=[0]*(2*n+2+K); r[k0]=1; J.append(r)
        J=[row[:2*n+2]+row[2*n+2+3:] for row in J]
        Jm=mp.matrix(J); Rm=mp.matrix(R)
        # minimal norm step: dx = J^H (J J^H)^{-1} R
        dx=mp.lu_solve(Jm,Rm)
        for i in range(2*n+2): co[i]-=dx[i]
        for k in range(3,K): crit[k]-=dx[2*n+2+k-3]
        res=mp.norm(Rm)
    # odd points: Newton on fibre polynomial
    out={}; hpodd={}
    kk=0; critby={y:[] for y in range(6)}
    for k in range(K): critby[ys[k]].append(crit[k])
    for y in range(6):
        y0,y1=mp.mpc(BP[y][0]),mp.mpc(BP[y][1])
        f=[y1*co[m]-y0*co[n+1+m] for m in range(n+1)]   # low->high
        odd=[]
        for z in an[y][0]:
            if z is None:
                # check leading coefficient ~0
                odd.append(None); hpodd.setdefault(y,[]).append(None); continue
            z=mp.mpc(z)
            for _ in range(12):
                fz=sum(f[m]*z**m for m in range(n+1)); dfz=sum(m*f[m]*z**(m-1) for m in range(1,n+1))
                z=z-fz/dfz
            odd.append(complex(z)); hpodd.setdefault(y,[]).append(z)
        out[y]=(odd,[complex(c) for c in critby[y]])
    lead=[abs(co[n]),abs(co[2*n+1])]
    return out,float(res),[complex(c) for c in co],hpodd
