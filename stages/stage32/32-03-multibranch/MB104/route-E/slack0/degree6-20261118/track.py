import numpy as np
from common import *
"""Monodromy solver: move the 6 branch values along closed loops and track solutions of
   y1(s) P(c_k) - y0(s) Q(c_k) = 0 = y1 P'(c_k) - y0 Q'(c_k),  L.x = 1, first 3 crits fixed."""
def system(x,c,Y0,Y1,L,n,K):
    N=x.shape[0]; m=np.arange(n+1)
    V=c[:,:,None]**m
    D=np.zeros_like(V); D[:,:,1:]=m[1:]*c[:,:,None]**(m[1:]-1)
    D2=np.zeros_like(V); D2[:,:,2:]=m[2:]*(m[2:]-1)*c[:,:,None]**(m[2:]-2)
    p=x[:,:n+1]; q=x[:,n+1:]
    Pv=np.einsum('nkm,nm->nk',V,p); Qv=np.einsum('nkm,nm->nk',V,q)
    Pd=np.einsum('nkm,nm->nk',D,p); Qd=np.einsum('nkm,nm->nk',D,q)
    Pdd=np.einsum('nkm,nm->nk',D2,p); Qdd=np.einsum('nkm,nm->nk',D2,q)
    F=Y1*Pv-Y0*Qv; Fd=Y1*Pd-Y0*Qd; Fdd=Y1*Pdd-Y0*Qdd
    R=np.concatenate([F,Fd,(x@L-1)[:,None]],1)
    nu=2*(n+1)+K-3
    J=np.zeros((N,2*K+1,nu),complex)
    J[:,:K,:n+1]=Y1[:,:,None]*V; J[:,:K,n+1:2*n+2]=-Y0[:,:,None]*V
    J[:,K:2*K,:n+1]=Y1[:,:,None]*D; J[:,K:2*K,n+1:2*n+2]=-Y0[:,:,None]*D
    J[:,2*K,:2*n+2]=L
    for k in range(3,K):
        J[:,k,2*n+2+k-3]=Fd[:,k]; J[:,K+k,2*n+2+k-3]=Fdd[:,k]
    # derivative wrt Y0 (Y1 fixed =1 along paths): dF/dY0 = -Q, dFd/dY0=-Q'
    return R,J,-Qv,-Qd
def safesolve(J,R,ok):
    J=J.copy(); R=R.copy()
    bad=~(np.isfinite(J).all((1,2))&np.isfinite(R).all(1))
    J[bad]=np.eye(J.shape[1],J.shape[2]); R[bad]=0; ok&=~bad
    try: return np.linalg.solve(J,R[:,:,None])[:,:,0]
    except np.linalg.LinAlgError:
        out=np.zeros((J.shape[0],J.shape[2]),complex)
        for r in range(J.shape[0]):
            try: out[r]=np.linalg.solve(J[r],R[r])
            except np.linalg.LinAlgError: ok[r]=False
        return out
def track(x,c,W0,W1,L,n,ys,steps=300):
    """W0: (S+1, 6) path of finite target values (y1=1). x,c: (N,...) start at W0[0]. Returns x,c,ok"""
    K=len(ys); ys=np.array(ys); ok=np.ones(x.shape[0],bool)
    x=x.copy(); c=c.copy()
    for s in range(1,len(W0)):
        Y0=np.broadcast_to(W0[s][ys],(x.shape[0],K)); Y1=np.ones_like(Y0)
        dY=(W0[s]-W0[s-1])[ys]
        # predictor (Euler) at previous point
        Yp=np.broadcast_to(W0[s-1][ys],(x.shape[0],K))
        R,J,dQ,dQd=system(x,c,Yp,np.ones_like(Yp),L,n,K)
        rhs=np.concatenate([dQ*dY,dQd*dY,np.zeros((x.shape[0],1))],1)
        dz=safesolve(J,-rhs,ok)
        x=x+dz[:,:2*n+2]; c[:,3:]=c[:,3:]+dz[:,2*n+2:]
        for it in range(4):
            R,J,_,_=system(x,c,Y0,Y1,L,n,K)
            dz=safesolve(J,R,ok)
            x=x-dz[:,:2*n+2]; c[:,3:]=c[:,3:]-dz[:,2*n+2:]
        nr=np.linalg.norm(R,axis=1)
        ok&=np.isfinite(nr)&(nr<1e-6)
        x[~ok]=1; c[~ok,3:]=1
    R,J,_,_=system(x,c,Y0,Y1,L,n,K)
    ok&=np.linalg.norm(R,axis=1)<1e-7
    return x,c,ok
