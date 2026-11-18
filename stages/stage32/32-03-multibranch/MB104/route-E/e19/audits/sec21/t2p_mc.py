# Independent check of Lemma T2' (1): the Maurer-Cartan Killing field X(v) of z -> A_z,
# evaluated at an arbitrary point q, against |e^w - 1| cosh d + |grad w| sinh d.
# Also (2) integrated along geodesics with long L and maps far from isometries, and (3).
import mpmath as mp, random
mp.mp.dps = 30
def Mb(b,u): return (u+b)/(1+mp.conj(b)*u)
def Mbi(b,u): return (u-b)/(1-mp.conj(b)*u)
def dist(a,b): return 2*mp.atanh(abs(Mbi(a,b)))
def geod(z0,z1,s):
    v=Mbi(z0,z1); return Mb(z0, mp.tanh(s/2)*v/abs(v))
rng=random.Random(7)
def rc(r): return mp.mpc(rng.uniform(-r,r),rng.uniform(-r,r))
worst1=0; worst2=0; worst3=0; n1=n2=n3=0
while n1<400 or n2<150:
    co=[rc(.6) for _ in range(3)]; sh=rc(.3); rot=mp.expjpi(rng.uniform(0,2)); cc=mp.mpf(rng.uniform(.3,1.0))
    P=lambda u: u+co[0]*u**2+co[1]*u**3+co[2]*u**4
    dP=lambda u: 1+2*co[0]*u+3*co[1]*u**2+4*co[2]*u**3
    G=lambda u: Mb(sh, rot*cc*P(u))
    def dG(u):
        x=rot*cc*P(u); return (1-abs(sh)**2)/(1+mp.conj(sh)*x)**2*rot*cc*dP(u)
    def A(z,u): return Mb(G(z), mp.expj(mp.arg(dG(z)))*Mbi(z,u))
    def Ainv(z,u): return Mb(z, mp.expj(-mp.arg(dG(z)))*Mbi(G(z),u))
    def w(u): return mp.log(abs(dG(u))*(1-abs(u)**2)/(1-abs(G(u))**2))
    def gw(u):
        h=mp.mpf('1e-15')
        gx=(w(u+h)-w(u-h))/(2*h); gy=(w(u+1j*h)-w(u-1j*h))/(2*h)
        return mp.sqrt(gx**2+gy**2)*(1-abs(u)**2)/2
    z=rc(.5)
    if abs(z)>.6 or abs(G(z))>.97 or abs(dP(z))<.2: continue
    # (1): random unit hyperbolic v, random q
    th=rng.uniform(0,6.283); v=mp.expj(th)*(1-abs(z)**2)/2
    q=rc(.8)
    if abs(q)>.95: continue
    h=mp.mpf('1e-18')
    Kq=Ainv(z, A(z+h*v, q)); Km=Ainv(z, A(z-h*v,q))
    X=(Kq-Km)/(2*h); Xn=abs(X)*2/(1-abs(q)**2)
    d=dist(q,z)
    bound=abs(mp.e**w(z)-1)*mp.cosh(d)+gw(z)*mp.sinh(d)
    if bound>1e-12:
        worst1=max(worst1, mp.re(Xn/bound)); n1+=1
    # (2): geodesic from z to z1 (long)
    z1=rc(.9)
    if abs(z1)<.95 and n2<150:
        ok=all(abs(dP(geod(z,z1,mp.mpf(k)/40*dist(z,z1))))>.1 and abs(G(geod(z,z1,mp.mpf(k)/40*dist(z,z1))))<.98 for k in range(41))
        if ok:
            L=dist(z,z1)
            f=lambda s: abs(mp.e**w(geod(z,z1,s))-1)*mp.cosh(L-s)+gw(geod(z,z1,s))*mp.sinh(L-s)
            I=mp.re(mp.quad(f,[0,L/2,L]))
            lhs=dist(G(z1),A(z,z1))
            worst2=max(worst2,lhs/I); n2+=1
print("(1) samples",n1,"max |X(v)(q)| / bound =",mp.nstr(worst1,6))
print("(2) samples",n2,"max lhs/rhs =",mp.nstr(worst2,6))
# (3) rotation: chord of rotation by theta at distance d equals 2 asinh(sin(theta/2) sinh d)
for _ in range(200):
    d=mp.mpf(rng.uniform(.1,5)); th=mp.mpf(rng.uniform(0,3.14))
    q=mp.tanh(d/2); Rq=mp.expj(th)*q
    lhs=dist(q,Rq); rhs=2*mp.asinh(mp.sin(th/2)*mp.sinh(d))
    worst3=max(worst3,abs(lhs-rhs))
print("(3) max |chord - formula| =",mp.nstr(worst3,3))
