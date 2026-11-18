import numpy as np, itertools, sys, pickle, time
from common import *
rng=np.random.default_rng(int(sys.argv[3]) if len(sys.argv)>3 else 1)

def newton_batch(n, ys, N, fixed, iters=60):
    """ys: list of B indices of crit points (len 2n-2). first 3 crits fixed to 'fixed'."""
    K=len(ys); y0=np.array([BP[y][0] for y in ys],complex); y1=np.array([BP[y][1] for y in ys],complex)
    nf=K-3; nu=2*(n+1)+nf
    L=rng.normal(size=2*(n+1))+1j*rng.normal(size=2*(n+1))
    c=np.empty((N,K),complex); c[:,:3]=fixed
    c[:,3:]=(rng.normal(size=(N,nf))+1j*rng.normal(size=(N,nf)))*1.5
    # init coeffs by smallest singular vector
    m=np.arange(n+1)
    def mats(c):
        V=c[:,:,None]**m            # N,K,n+1
        D=np.zeros_like(V); D[:,:,1:]=m[1:]*c[:,:,None]**(m[1:]-1)
        D2=np.zeros_like(V); D2[:,:,2:]=m[2:]*(m[2:]-1)*c[:,:,None]**(m[2:]-2)
        return V,D,D2
    V,D,D2=mats(c)
    A=np.concatenate([np.concatenate([y1[:,None]*V, -y0[:,None]*V],2), np.concatenate([y1[:,None]*D,-y0[:,None]*D],2)],1)
    _,_,vh=np.linalg.svd(A); x=vh[:,-1,:].conj()
    x=x/(x@L)[:,None]
    for it in range(iters):
        V,D,D2=mats(c)
        p=x[:,:n+1]; q=x[:,n+1:]
        F=y1*np.einsum('nkm,nm->nk',V,p)-y0*np.einsum('nkm,nm->nk',V,q)
        Fd=y1*np.einsum('nkm,nm->nk',D,p)-y0*np.einsum('nkm,nm->nk',D,q)
        Fdd=y1*np.einsum('nkm,nm->nk',D2,p)-y0*np.einsum('nkm,nm->nk',D2,q)
        R=np.concatenate([F,Fd,(x@L-1)[:,None]],1)
        J=np.zeros((N,2*K+1,nu),complex)
        J[:,:K,:n+1]=y1[:,None]*V; J[:,:K,n+1:2*n+2]=-y0[:,None]*V
        J[:,K:2*K,:n+1]=y1[:,None]*D; J[:,K:2*K,n+1:2*n+2]=-y0[:,None]*D
        J[:,2*K,:2*n+2]=L
        for k in range(3,K):
            J[:,k,2*n+2+k-3]=Fd[:,k]; J[:,K+k,2*n+2+k-3]=Fdd[:,k]
        try: dx=np.linalg.solve(J,R[:,:,None])[:,:,0]
        except np.linalg.LinAlgError:
            dx=np.array([np.linalg.lstsq(J[i],R[i],rcond=None)[0] for i in range(N)])
        nrm=np.linalg.norm(dx,axis=1); s=np.minimum(1,2/np.maximum(nrm,1e-300))[:,None]
        x=x-s*dx[:,:2*n+2]; c[:,3:]=c[:,3:]-s*dx[:,2*n+2:]
        bad=~np.isfinite(x).all(1)|~np.isfinite(c).all(1)
        x[bad]=1; c[bad,3:]=1
    return x,c,np.linalg.norm(R,axis=1)

def fibre(p,q,y):
    """roots (homog) of y1 P - y0 Q, P,Q coeff arrays low->high; return list of (root_hom, mult) via clustering"""
    f=BP[y][1]*p-BP[y][0]*q
    n=len(p)-1
    nz=np.nonzero(np.abs(f)>1e-9*np.abs(f).max())[0]; deg=nz.max()
    r=np.roots(f[:deg+1][::-1]) if deg>0 else np.array([])
    pts=[(complex(z),1) for z in r]+[(None,1)]*(n-deg)
    return pts

def polish(f,z,it=8):
    df=np.polyder(f)
    for _ in range(it):
        d=np.polyval(df,z)
        if d==0: break
        z=z-np.polyval(f,z)/d
    return z

def analyse(p,q,n,prof,crit=None,ys=None,tol=1e-6):
    s=np.abs(np.concatenate([p,q])).max(); p=p/s; q=q/s
    out={}
    for y in range(6):
        f=(BP[y][1]*p-BP[y][0]*q)[::-1]   # high->low
        cs=[crit[k] for k in range(len(ys)) if ys[k]==y]
        g=f.copy()
        for cc in cs:
            for _ in range(2):
                g,r=np.polydiv(g,np.array([1,-cc]))
                if abs(r).max()>1e-7*max(1,abs(g).max()): return None
        # g degree n-2t ; leading zeros => roots at infinity
        g=np.trim_zeros(np.where(np.abs(g)<1e-11*np.abs(g).max(),0,g),'f') if np.abs(g).max()>0 else g
        deg=len(g)-1; ninf=n-2*len(cs)-deg
        if ninf>1: return None
        odd=[complex(polish(f,z)) for z in (np.roots(g) if deg>0 else [])]+[None]*ninf
        dbl=list(cs)
        # check no double among odd: f'(z)!=0
        df=np.polyder(f)
        for z in odd:
            if z is not None and abs(np.polyval(df,z))<1e-6*np.abs(df).max()*max(1,abs(z))**(n-1): return None
        if len(odd)!=n-2*prof[y]: return None
        out[y]=(odd,dbl)
    allp=[hom(z) for y in range(6) for t in (0,1) for z in out[y][t]]
    for i in range(len(allp)):
        for j in range(i):
            u,v=allp[i],allp[j]
            if abs(u[0]*v[1]-u[1]*v[0])<1e-6*(abs(u[0])+abs(u[1]))*(abs(v[0])+abs(v[1])): return None
    return out

def hom(z): return (1+0j,0j) if z is None else (complex(z),1+0j)
def norm_mob(a,b,c):
    """Mobius sending a->0, b->inf, c->1 (homog)."""
    # T(z) = (z-a)(c-b)/((z-b)(c-a)) in homog
    def lin(u,v): return u[0]*v[1]-u[1]*v[0]
    def T(z): return (lin(z,a)*lin(c,b), lin(z,b)*lin(c,a))
    return T
def chord(w):
    a,b=w; d=abs(a)**2+abs(b)**2
    z=2*a*b.conjugate()/d; Z=(abs(a)**2-abs(b)**2)/d
    return (round(z.real+0.0,4)+0.0,round(z.imag,4)+0.0,round(Z,4)+0.0)

def fingerprint(an):
    crit=[(y,hom(z)) for y in range(6) for z in an[y][1]]
    allp=[(y,t,hom(z)) for y in range(6) for t in (0,1) for z in an[y][t]]
    best=None; keys=[]
    for i,j,k in itertools.permutations(range(len(crit)),3):
        T=norm_mob(crit[i][1],crit[j][1],crit[k][1])
        key=(crit[i][0],crit[j][0],crit[k][0])+tuple(sorted((y,t,chord(T(w))) for y,t,w in allp))
        keys.append(key)
    best=min(keys)
    return best, sum(1 for kk in keys if kk==best)

_OM=[np.exp(2j*np.pi*np.array([0.123,0.377,0.581,0.733,0.912,0.055])),np.exp(2j*np.pi*np.array([0.311,0.645,0.082,0.457,0.268,0.799]))]
def invariant(an):
    pts=[];ys=[]
    for y in range(6):
        for t in (0,1):
            for z in an[y][t]:
                w=np.array((1,0) if z is None else (z,1),complex); pts.append(w/np.linalg.norm(w)); ys.append(y+6*t)
    pts=np.array(pts); ys=np.array(ys)
    S=np.array(list(itertools.combinations(range(len(pts)),4)))
    P=pts[S]
    def wd(u,v): return u[...,0]*v[...,1]-u[...,1]*v[...,0]
    num=wd(P[:,0],P[:,2])*wd(P[:,1],P[:,3]); den=wd(P[:,0],P[:,3])*wd(P[:,1],P[:,2])
    # lambda=num/den; j = (l^2-l+1)^3/(l^2 (l-1)^2) homogeneous: (num^2-num den+den^2)^3/(num^2 den^2 (num-den)^2)
    A=(num**2-num*den+den**2)**3; Bq=(num*den*(num-den))**2
    jj=A/Bq; h=jj/np.sqrt(1+np.abs(jj)**2)
    out=[]
    for om in _OM:
        omg=np.concatenate([om,om**2])
        out.append((np.prod(omg[ys[S]],1)*h).sum())
    return np.array(out)
