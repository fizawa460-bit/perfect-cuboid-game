# E25 audit (section 4): independent high-precision check of pairs (f, g∘M) of degree-5 slack-0 covers whose
# |Omega| lies strictly between |O| = 14 and 4k = 20. Input: candidates dumped by a copy of search2.py
# (mid_5_5_*.pkl: (fi, qi, M, om, j, h, ...)) and all_5.pkl (40-digit covers). Everything below is recomputed
# here from the cover coefficients only: cone points (simple roots over B) at 60 digits, the Mobius map
# (re-fitted at 60 digits from 3 coincidences), the coincidences, |Omega|, and birationality.
import pickle, sys, glob, random, mpmath as mp
mp.mp.dps=60
BP=[(0,1),(1,0),(1,1),(-1,1),(1j,1),(-1j,1)]; BLAB=[0,0,1,1,2,2]
def cone_points(p,q):
    n=len(p)-1; out=[]
    for k,(b0,b1) in enumerate(BP):
        c=[mp.mpc(b1)*p[m]-mp.mpc(b0)*q[m] for m in range(n+1)]   # low -> high
        deg=max(m for m in range(n+1) if abs(c[m])>mp.mpf(10)**-30)
        roots=mp.polyroots(c[:deg+1][::-1],maxsteps=400,extraprec=400) if deg>0 else []
        pts=[(r,mp.mpc(1)) for r in roots]+[(mp.mpc(1),mp.mpc(0))]*(n-deg)          # n-deg roots at infinity
        # simple points = odd local degree (indices are 1 or 2 at slack 0)
        for i,x in enumerate(pts):
            mult=sum(1 for y in pts if chd(x,y)<mp.mpf(10)**-20)
            if mult%2==1: out.append((x,BLAB[k]))
    return out
def chd(u,v):
    return abs(u[0]*v[1]-u[1]*v[0])/(mp.sqrt(abs(u[0])**2+abs(u[1])**2)*mp.sqrt(abs(v[0])**2+abs(v[1])**2))
def frame(P):
    M=mp.matrix([[P[0][0],P[1][0]],[P[0][1],P[1][1]]]); l=mp.lu_solve(M,mp.matrix([P[2][0],P[2][1]]))
    return mp.matrix([[M[0,0]*l[0],M[0,1]*l[1]],[M[1,0]*l[0],M[1,1]*l[1]]])
def app(M,x): return (M[0,0]*x[0]+M[0,1]*x[1], M[1,0]*x[0]+M[1,1]*x[1])
def ev(p,q,t):
    n=len(p)-1
    return (sum(p[m]*t[0]**m*t[1]**(n-m) for m in range(n+1)), sum(q[m]*t[0]**m*t[1]**(n-m) for m in range(n+1)))
def compose_src(p,q,S):
    # coefficients (low->high) of P(S t), Q(S t) with S a 2x2 matrix acting on homogeneous (t0,t1)
    n=len(p)-1
    a,b,c,d=S[0,0],S[0,1],S[1,0],S[1,1]
    def polmul(u,v):
        w=[mp.mpc(0)]*(len(u)+len(v)-1)
        for i,x in enumerate(u):
            for j,y in enumerate(v): w[i+j]+=x*y
        return w
    def sub(cf):
        out=[mp.mpc(0)]*(n+1)
        for m in range(n+1):
            t=[mp.mpc(cf[m])]
            for _ in range(m): t=polmul(t,[b,a])          # (a z + b), z = t0/t1, low->high
            for _ in range(n-m): t=polmul(t,[d,c])        # (c z + d)
            for i,x in enumerate(t): out[i]+=x
        return out
    return sub(p),sub(q)
def refine(p,q):
    # Newton refinement at 60 digits of a slack-0 cover: unknowns = 2(n+1) coefficients and the 2n-2 double
    # points; equations: value and derivative of b1 P - b0 Q vanish at each double point over its b; gauge:
    # three double points fixed, one linear normalisation of the coefficients.
    n=len(p)-1
    S=mp.matrix([[mp.mpc(0.83,0.21),mp.mpc(-0.37,0.55)],[mp.mpc(0.41,-0.66),mp.mpc(1.12,0.09)]])
    P,Q=compose_src([mp.mpc(complex(x)) for x in p],[mp.mpc(complex(x)) for x in q],S)
    dbl=[]
    for k,(b0,b1) in enumerate(BP):
        c=[mp.mpc(b1)*P[m]-mp.mpc(b0)*Q[m] for m in range(n+1)]
        r=mp.polyroots(c[::-1],maxsteps=200,extraprec=100)
        used=set()
        for i in range(len(r)):
            if i in used: continue
            js=[j for j in range(len(r)) if j!=i and j not in used and abs(r[i]-r[j])<1e-4]
            if js: used|={i,js[0]}; dbl.append([k,(r[i]+r[js[0]])/2])
    assert len(dbl)==2*n-2, len(dbl)
    x=P+Q+[z for _,z in dbl]
    L=[mp.mpc(0.3+0.1*i,0.7-0.05*i) for i in range(2*n+2)]; s0=sum(L[i]*x[i] for i in range(2*n+2))
    x=[v/s0 if i<2*n+2 else v for i,v in enumerate(x)]
    free=list(range(2*n+2))+list(range(2*n+2+3,len(x)))
    def F(x):
        Pc,Qc=x[:n+1],x[n+1:2*n+2]; out=[]
        for idx,(k,_) in enumerate(dbl):
            z=x[2*n+2+idx]; b0,b1=BP[k]
            out.append(sum((b1*Pc[m]-b0*Qc[m])*z**m for m in range(n+1)))
            out.append(sum(m*(b1*Pc[m]-b0*Qc[m])*z**(m-1) for m in range(1,n+1)))
        out.append(sum(L[i]*x[i] for i in range(2*n+2))-1)
        return out
    for it in range(40):
        f0=F(x); err=max(abs(v) for v in f0)
        if err<mp.mpf(10)**-55: break
        h=mp.mpf(10)**-35
        J=mp.matrix(len(f0),len(free))
        for cidx,vi in enumerate(free):
            xx=list(x); xx[vi]+=h; f1=F(xx)
            for r_ in range(len(f0)): J[r_,cidx]=(f1[r_]-f0[r_])/h
        dx=mp.lu_solve(J,mp.matrix([-v for v in f0]))
        for cidx,vi in enumerate(free): x[vi]+=dx[cidx]
    assert err<mp.mpf(10)**-50, err
    Pr,Qr=x[:n+1],x[n+1:2*n+2]
    return compose_src(Pr,Qr,mp.inverse(S))   # back to the original coordinate (up to an overall scalar)
def analyse(f,g,M0):
    f=refine(*f); g=refine(*g)
    X=cone_points(*f); Y=cone_points(*g)
    assert len(X)==14 and len(Y)==14, (len(X),len(Y))
    # coincidences under the float M0, then refit M at 60 digits from three of them and recount
    M=mp.matrix([[mp.mpc(complex(M0[0][0])),mp.mpc(complex(M0[0][1]))],[mp.mpc(complex(M0[1][0])),mp.mpc(complex(M0[1][1]))]])
    pairs=[(i,j) for i,(x,_) in enumerate(X) for j,(y,_) in enumerate(Y) if chd(app(M,x),y)<1e-6]
    if len(pairs)<3: return None
    M=frame([Y[j][0] for _,j in pairs[:3]])*mp.inverse(frame([X[i][0] for i,_ in pairs[:3]]))
    D=[[chd(app(M,x),y) for y,_ in Y] for x,_ in X]
    close=[(i,j) for i in range(len(X)) for j in range(len(Y)) if D[i][j]<mp.mpf(10)**-30]
    far=min(D[i][j] for i in range(len(X)) for j in range(len(Y)) if D[i][j]>=mp.mpf(10)**-30)
    worst=max([D[i][j] for i,j in close] or [0])
    jj=sum(1 for i,j in close if X[i][1]==Y[j][1]); hh=len(close)-jj
    om=len(X)+len(Y)-2*jj-hh
    # birationality of t -> (f(t), g(M^{-1} ... )): pair is (f, g∘M) on the f-sphere
    random.seed(1); bir=True
    for _ in range(2):
        t=(mp.mpc(random.gauss(0,1),random.gauss(0,1)),mp.mpc(1))
        v=ev(*f,t); p,q=f; n=len(p)-1
        c=[v[1]*p[m]-v[0]*q[m] for m in range(n+1)]
        fib=[(r,mp.mpc(1)) for r in mp.polyroots(c[::-1],maxsteps=400,extraprec=400)]
        g0=ev(*g,app(M,t))
        same=sum(1 for s in fib if chd(ev(*g,app(M,s)),g0)<mp.mpf(10)**-30)
        if same>=2: bir=False
    return dict(nX=len(X),nY=len(Y),common=len(close),j=jj,h=hh,om=om,worst=worst,far=far,birational=bir)
A=pickle.load(open(sys.argv[1]+'/all_5.pkl','rb'))
mid=[]
for fn in sorted(glob.glob(sys.argv[1]+'/mid_5_5_*.pkl')): mid+=pickle.load(open(fn,'rb'))
print('candidates with 14<|Omega|<20 in the dump:',len(mid))
random.seed(7); pick=random.sample(mid,min(int(sys.argv[2]) if len(sys.argv)>2 else 12,len(mid)))
ok=True
for fi,qi,M0,om,j,h,*_ in pick:
    f=A['reps'][fi][:2]; g=A['all'][qi][:2]
    r=analyse(f,g,M0)
    print((fi,qi),'search said |Omega|=',om,'j=',j,'h=',h,'| recomputed:',{k:(mp.nstr(v,3) if isinstance(v,mp.mpf) else v) for k,v in r.items()})
    ok&= r is not None and r['om']==om and r['birational'] and r['common']>=(28-om)//2 and r['common']==r['j']+r['h'] and r['far']>mp.mpf(10)**-8
print('PASS' if ok else 'FAIL')
