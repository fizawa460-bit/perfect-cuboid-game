"""40-digit check of the 'BIRATIONAL' hits: rebuild M from three matched odd points at 40 digits and test
whether M carries the whole labelled f^{-1}(B) (odd and double points) onto q^{-1}(B); if so q∘M = V∘f (V in Aut(B)),
a composite, hence non-birational. Also prints the 40-digit fibre test."""
import pickle,numpy as np,mpmath as mp,sys,itertools
mp.mp.dps=40
import hp
from common import BP,AUT,BLAB
def refine_mp(p,q,an,n,iters=10):
    src=open(hp.__file__).read(); return None
O=pickle.load(open('all2_6_old.pkl','rb'))
# patched refine returning mp data
src=open(hp.__file__).read().replace("return out,float(res),[complex(c) for c in co],hpodd","return out,float(res),co,hpodd,crit,ys")
ns={}; exec(src,ns); refine=ns['refine']
def pts(co,crit,ys,hpo,n):
    P=[]
    for y in range(6):
        for z in hpo.get(y,[]): P.append((y,0,(mp.mpc(1),mp.mpc(0)) if z is None else (z,mp.mpc(1))))
    for c,y in zip(crit,ys): P.append((y,1,(c,mp.mpc(1))))
    return P
def wedge(u,v): return u[0]*v[1]-u[1]*v[0]
def cd(u,v): return abs(wedge(u,v))/(mp.sqrt(abs(u[0])**2+abs(u[1])**2)*mp.sqrt(abs(v[0])**2+abs(v[1])**2))
def app(M,u): return (M[0][0]*u[0]+M[0][1]*u[1], M[1][0]*u[0]+M[1][1]*u[1])
def mob3(a,b):
    # Moebius sending a_k -> b_k (homogeneous)
    def frame(z):
        Mt=mp.matrix([[z[0][0],z[1][0]],[z[0][1],z[1][1]]]); lm=mp.lu_solve(Mt,mp.matrix([z[2][0],z[2][1]]))
        return mp.matrix([[Mt[0,0]*lm[0],Mt[0,1]*lm[1]],[Mt[1,0]*lm[0],Mt[1,1]*lm[1]]])
    T=frame(b)*mp.inverse(frame(a)); return [[T[0,0],T[0,1]],[T[1,0],T[1,1]]]
cache={}
def get(ri):
    if ri not in cache:
        p,q,an,aut=O['reps'][ri][:4]; n=len(p)-1
        an2,res,co,hpo,crit,ys=refine(p,q,an,n,iters=12); cache[ri]=(pts(co,crit,ys,hpo,n),res)
    return cache[ri]
PAIRS=[tuple(map(int,a.split(':'))) for a in sys.argv[1:]] or [(4391,39982),(1816,42833),(4391,256),(4386,57139),(4386,66137)]
for fi0,qi0 in PAIRS:
    R=pickle.load(open(f'res2_6_6bk_{fi0}_{qi0}_0of1.pkl','rb'))
    c=O['all'][qi0]; r,u=c[4],c[5]; perm=AUT[u][1]
    Pf,resf=get(fi0); Pr,resr=get(r)
    Pq=[(perm[y],t,z) for y,t,z in Pr]     # q = U∘rep: q^{-1}(perm y) = rep^{-1}(y)
    for _,_,M,om in R['hitsM']:
        Md=[[mp.mpc(complex(M[0,0])),mp.mpc(complex(M[0,1]))],[mp.mpc(complex(M[1,0])),mp.mpc(complex(M[1,1]))]]
        # match each f point to nearest q point of same label/type under M (double M)
        match=[]
        for y,t,z in Pf:
            w=app(Md,z); best=min(((cd(w,zz),k) for k,(yy,tt,zz) in enumerate(Pq) if BLAB[yy]==BLAB[y] and tt==t),key=lambda a:a[0])
            match.append(best)
        good=[i for i,(d,k) in enumerate(match) if d<1e-4]
        # 40-digit M from three well separated matched odd points
        oddg=[i for i in good if Pf[i][1]==0]
        best=None
        for tri in itertools.combinations(oddg[:8],3):
            a=[Pf[i][2] for i in tri]; s=min(cd(a[0],a[1]),cd(a[0],a[2]),cd(a[1],a[2]))
            if best is None or s>best[0]: best=(s,tri)
        tri=best[1]; M40=mob3([Pf[i][2] for i in tri],[Pq[match[i][1]][2] for i in tri])
        ds=[]
        for i,(y,t,z) in enumerate(Pf):
            w=app(M40,z); d=min(cd(w,zz) for yy,tt,zz in Pq if tt==t and BLAB[yy]==BLAB[y])
            ds.append(float(d))
        lab_ok=all(Pq[match[i][1]][0]==Pq[match[j][1]][0] for i in range(len(Pf)) for j in range(len(Pf)) if Pf[i][0]==Pf[j][0] and i in good and j in good)
        print(fi0,qi0,'om',om,'refine res',f'{resf:.1e}','matched(double)',len(good),'/',len(Pf),
              ' 40-digit max dist over all f^-1(B) points',f'{max(ds):.1e}','fibres consistent',lab_ok)

print('--- 40-digit fibre test for the |Omega|=4 hits')
cacheco={}
def getco(ri):
    if ri not in cacheco:
        p,q,an,aut=O['reps'][ri][:4]; n=len(p)-1
        an2,res,co,hpo,crit,ys=refine(p,q,an,n,iters=12); cacheco[ri]=co
    return cacheco[ri]
for fi0,qi0 in [pq for pq in PAIRS if any(h[3]==4 for h in pickle.load(open(f'res2_6_6bk_{pq[0]}_{pq[1]}_0of1.pkl','rb'))['hitsM'])]:
    R=pickle.load(open(f'res2_6_6bk_{fi0}_{qi0}_0of1.pkl','rb'))
    c=O['all'][qi0]; r,u=c[4],c[5]; MU=AUT[u][0]
    Pf,_=get(fi0); Pr,_=get(r); perm=AUT[u][1]; Pq=[(perm[y],t,z) for y,t,z in Pr]
    cf=getco(fi0); cr=getco(r); n=6
    for _,_,M,om in R['hitsM']:
        if om!=4: continue
        Md=[[mp.mpc(complex(M[i,j])) for j in range(2)] for i in range(2)]
        match=[]
        for y,t,z in Pf:
            w=app(Md,z); match.append(min(((cd(w,zz),k) for k,(yy,tt,zz) in enumerate(Pq) if BLAB[yy]==BLAB[y] and tt==t),key=lambda a:a[0]))
        oddg=[i for i,(d,k) in enumerate(match) if d<1e-4 and Pf[i][1]==0]
        best=max(((min(cd(Pf[a][2],Pf[b][2]),cd(Pf[a][2],Pf[c_][2]),cd(Pf[b][2],Pf[c_][2])),(a,b,c_)) for a,b,c_ in itertools.combinations(oddg,3)),key=lambda x:x[0])
        tri=best[1]; M40=mob3([Pf[i][2] for i in tri],[Pq[match[i][1]][2] for i in tri])
        dmatch=sorted(float(min(cd(app(M40,z),zz) for yy,tt,zz in Pq if tt==t and BLAB[yy]==BLAB[y])) for y,t,z in Pf)
        def p2(z):
            w=app(M40,(z,mp.mpc(1))); P=sum(cr[m]*w[0]**m*w[1]**(n-m) for m in range(n+1)); Q=sum(cr[n+1+m]*w[0]**m*w[1]**(n-m) for m in range(n+1))
            return (MU[0,0]*P+MU[0,1]*Q, MU[1,0]*P+MU[1,1]*Q)
        rng=np.random.default_rng(3); rows=[]
        for tr in range(3):
            t=mp.mpc(*map(float,rng.normal(size=2)))
            v=(sum(cf[m]*t**m for m in range(n+1)), sum(cf[n+1+m]*t**m for m in range(n+1)))
            poly=[v[1]*cf[m]-v[0]*cf[n+1+m] for m in range(n+1)][::-1]
            rts=mp.polyroots(poly,maxsteps=300,extraprec=80)
            g0=p2(t); rows.append(sorted(float(cd(p2(z),g0)) for z in rts))
        print(fi0,qi0,'om 4: 40-digit point distances (sorted)',' '.join(f'{d:.0e}' for d in dmatch[:14]),'...')
        for rr in rows: print('    fibre', ' '.join(f'{d:.1e}' for d in rr))
