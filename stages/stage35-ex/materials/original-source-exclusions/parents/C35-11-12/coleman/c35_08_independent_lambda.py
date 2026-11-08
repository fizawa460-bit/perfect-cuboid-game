"""Stage35EX C35-08: independent ramified-quadratic trace Coleman basepoint for F8,
no calls into Claude Coleman functions, Hensel on Q3 and ring Q3[beta].
"""
from c35_08_independent_log import F,P,N,M,K,FT,vpint,vpq,qm,fpoly,mulpoly,divint,raw_mumford_check,le
import pickle,os
from math import comb
class Quad:
    def __init__(self,A,B,x=0,y=0): self.A=A;self.B=B;self.x=x%M;self.y=y%M
    def __add__(self,z):return Quad(self.A,self.B,self.x+z.x,self.y+z.y)
    def __sub__(self,z):return Quad(self.A,self.B,self.x-z.x,self.y-z.y)
    def __mul__(self,z):return Quad(self.A,self.B,self.x*z.x-self.B*self.y*z.y,self.x*z.y+self.y*z.x-self.A*self.y*z.y)
    def scale(self,c):
        c=F(c);v=vpq(c)
        if v>=0:
            t=qm(c);return Quad(self.A,self.B,self.x*t,self.y*t)
        k=-v;assert self.x%3**k==0 and self.y%3**k==0,('non-divisor',c,self.x%3**k,self.y%3**k)
        t=qm(c*3**k)
        return Quad(self.A,self.B,self.x//3**k*t,self.y//3**k*t)
    def trace(self):return (2*self.x-self.A*self.y)%M
    def __repr__(self):return str((self.x,self.y))

def eval_quad(poly,z):
    s=Quad(z.A,z.B)
    for c in poly[::-1]:s=s*z+Quad(z.A,z.B,qm(c))
    return s

def inverse_gen(a,n):
    from c35_08_independent_log import invser
    a0=a[0]
    t=invser([x/a0 for x in a],n)
    return [x/a0 for x in t]

def taylor_compose(u,cs,k):
    one=[F(1)]+[F(0)]*k
    acc=[F(0)]*(k+1)
    for ci in cs[::-1]:
        acc=mulpoly(acc,u,k)
        acc[0]+=ci
    return acc

def power_quad(y,n):
    z=Quad(y.A,y.B,1,0)
    while n:
        if n&1:z=z*y
        y=y*y;n>>=1
    return z

uf,vf=pickle.load(open(os.path.join(os.path.dirname(__file__),'F_8.pkl'),'rb'))
raw_mumford_check(uf,vf)
root=2
assert fpoly(uf,root)%3==0
for j in range(1,N):
    step=3**j
    value=fpoly(uf,root)
    assert value%step==0
    der=sum(i*qm(uf[i])*pow(root,i-1,M) for i in range(1,4))%3
    assert der!=0
    d=(-value//step*pow(der,-1,3))%3
    root=(root+d*step)%M
assert fpoly(uf,root)==0
A1=(qm(uf[2])+root)%M
B1=(qm(uf[1])+A1*root)%M
assert A1%3==0 and B1%9==0
A=(A1//3)%M
B=(B1//9)%M
beta=Quad(A,B,0,1)
u=beta.scale(3)
# y=V(3 beta), using factor 3 to clear coefficient denominators
vscale=[F(3)*cc for cc in vf]
assert all(vpq(c)>=0 for c in vscale)
yraw=eval_quad(vscale,u)
assert yraw.x%3==0 and yraw.y%3==0,(yraw.x%3,yraw.y%3)
y=yraw.scale(F(1,3))
assert (y*y-eval_quad([F(c) for c in FT],u)).x%(3**9)==0
assert (y*y-eval_quad([F(c) for c in FT],u)).y%(3**9)==0
assert (y*y).x%3==0 and (y*y).y%3==0
Yraw=sum(qm(c)*pow(root,i,M) for i,c in enumerate(vscale))%M
assert Yraw%3==0
Y1=(Yraw//3)%M
assert Y1%3==2
assert (Y1*Y1-fpoly(FT,root))%3**8==0
# compositional inverse: ft(x(z))=z, at x0=0. exact Z_p power series.
L=K
usr=[F(0)]*(L+1)
for n in range(1,L+1):
    value=taylor_compose(usr,[F(c) for c in FT],n)[n]
    usr[n]=value-(1 if n==1 else 0)   # ft'(0)=-1
assert taylor_compose(usr,[F(c) for c in FT],L)==[F(0),F(1)]+[F(0)]*(L-1)
fprime=[F(i*FT[i]) for i in range(1,len(FT))]
inv_der=inverse_gen(taylor_compose(usr,fprime,L),L)
g=[]
pw=[F(1)]+[F(0)]*L
for i in range(3):
    g.append(mulpoly(pw,inv_der,L))
    pw=mulpoly(pw,usr,L)
IQ=[]
y2=y*y
for i in range(3):
    val=Quad(A,B)
    powy=y
    for n in range(L+1):
        val=val+powy.scale(g[i][n]/F(2*n+1))
        powy=powy*y2
    IQ.append(val.trace())
L26=[z*pow(26,-1,M)%M for z in le]
lam=[(8*z-IQ[i])%M for i,z in enumerate(L26)]
print('STATUS independent ramified quadratic Coleman F8 trace')
print('root',root%729,'Y1',Y1%729,'q cofactor scaled A/B mod3',A%3,B%3)
print('y² val3 coefficient bounds',vpint((y*y).x),vpint((y*y).y))
print('IQ/3 mod729',[(z//3)%729 for z in IQ])
print('LamR1/3 mod729',[(z//3)%729 for z in lam])
print('expected [503,268,626]')
assert [(z//3)%729 for z in lam]==[503,268,626]
print('PASS_INDEPENDENT_RAMIFIED_QUADRATIC_TRACE_LAMBDA_R1')
