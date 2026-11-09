# Independent Z_2 unramified7 with uniformizer pi^3=2, truncated mod pi^12.
# No author row372 verifier used. Pure Python integers.
from math import comb
import json,hashlib
D=json.load(open('curve_C29.json'))
A=D['A_star_ascending']; B=D['B_star_ascending']
MOD=16; Z=7; N=21
# basis indexed pi-exp*7+z-exp
Zmult=[]
for i in range(Z):
  line=[]
  for j in range(Z):
    vec=[0]*(2*Z-1);vec[i+j]=1
    for k in range(2*Z-2, Z-1,-1):
      c=vec[k]
      if c:
        vec[k]=0;vec[k-7]-=c;vec[k-6]-=c # z^7=-(z+1)
    line.append(vec[:Z])
  Zmult.append(line)

def cst(a):
  r=[0]*N;r[0]=a%MOD;return tuple(r)
ZERO=cst(0);ONE=cst(1)
def pi_pow(k):
  r=[0]*N
  if 0<=k<12:r[k%3*Z]=2**(k//3)
  return tuple(r)
PI=pi_pow(1)
def add(a,b):return tuple((x+y)%MOD for x,y in zip(a,b))
def neg(a):return tuple(-x%MOD for x in a)
def sub(a,b):return tuple((x-y)%MOD for x,y in zip(a,b))
def mul(a,b):
  out=[0]*N
  for n,v in enumerate(a):
    if not v:continue
    ni, nj=divmod(n,Z)
    for m,w in enumerate(b):
      if not w:continue
      mi,mj=divmod(m,Z)
      k=ni+mi;factor=2 if k>=3 else 1; k=k%3
      for z,c in enumerate(Zmult[nj][mj]):
        if c:out[k*Z+z]+=v*w*factor*c
  return tuple(x%MOD for x in out)
def pwr(a,n):
  r=ONE
  while n:
    if n&1:r=mul(r,a)
    a=mul(a,a);n//=2
  return r

def red(a):return sum((a[i]%2)<<i for i in range(7))
def fm(a,b):
  r=0
  while b:
    if b&1:r^=a
    b>>=1;a<<=1
    if a&128:a^=0x83 # x^7+x+1
  return r

def fpow(a,n):
  r=1
  while n:
    if n&1:r=fm(r,a)
    a=fm(a,a);n//=2
  return r

def basis_residue(m):
  r=[0]*N
  for i in range(7):r[i]=(m>>i)&1
  return tuple(r)

def inv(a):
  a0=red(a);assert a0
  r=basis_residue(fpow(a0,126))
  for _ in range(5):r=mul(r,sub(cst(2),mul(a,r)))
  assert mul(a,r)==ONE,(a,mul(a,r))
  return r

def polyval(coeff,w):
  r=ZERO
  for c in coeff[::-1]:r=add(mul(r,w),c)
  return r

def tayl(poly):
  return [sum(poly[k]*comb(k,i) for k in range(i,len(poly))) for i in range(len(poly))]

def norm_polynomial(coeff,M):
  # P=W-polynomial for pi^-M f(1+pi W)
  out=[]
  for i,c in enumerate(coeff):
    q=(M-i+2)//3
    assert c%(2**q)==0,(i,c,q)
    j=i+3*q-M
    assert 0<=j<=2
    z=[0]*N;z[j*Z]=c//(2**q)%16;out.append(tuple(z))
  return out

def bit0(a,k):return red(a[k*Z:(k+1)*Z])
def pf(a):
  return {'u0':hex(bit0(a,0)),'u1':hex(bit0(a,1)),'u2':hex(bit0(a,2)),'vector':[hex(bit0(a,k)) for k in range(3)]}
# polynomials G(t) and B(-t²)
G=[0]*106;bt=[0]*105
for i,(a,b) in enumerate(zip(A,B)):
  G[2*i]=a*(-1)**i
  G[2*i+1]=b*(-1)**i
  bt[2*i]=b*(-1)**i
cg=tayl(G);cb=tayl(bt)
print('degree G',len(G)-1,'deg b',len(bt)-1)
P=norm_polynomial(cg,105)
Q=norm_polynomial(cb,104)
# check W0=z^85=0x6d
w0=fpow(2,85)
print('w0',hex(w0));assert w0==0x6d
W=basis_residue(w0)
Deriv=[mul(cst(i),P[i]) for i in range(1,len(P))]
print('P(w0) first residue',hex(bit0(polyval(P,W),0)),'Pprime residue',hex(bit0(polyval(Deriv,W),0)))
assert bit0(polyval(P,W),0)==0
assert bit0(polyval(Deriv,W),0)!=0
for k in range(6):
  v=polyval(P,W)
  W=sub(W,mul(v,inv(polyval(Deriv,W))))
  print('Newton iter',k+1,'P(W) zero?',polyval(P,W)==ZERO)
  if polyval(P,W)==ZERO:break
assert polyval(P,W)==ZERO
WINV=inv(W)
uplus=add(ONE,add(mul(PI,pwr(WINV,2)),mul(pi_pow(2),WINV)))
uminus=add(ONE,mul(pi_pow(2),WINV))
print('D+ coefficients',pf(uplus),'D- coefficients',pf(uminus))
BH=polyval(Q,W)
s0=bit0(BH,0)
print('B normalized residue',hex(s0))
assert s0
# unram degree-7 square root of residue B(theta)/pi^104
s=basis_residue(fpow(s0,64))
uH=mul(BH,pwr(inv(s),2))
print('H normalized',pf(uH))
# Square test of D- with sqrt U2, calculate 3rd coefficient
c=fpow(bit0(uminus,2),64)
sqrtcand=add(ONE,mul(PI,basis_residue(c)))
obstruction=sub(uminus,mul(sqrtcand,sqrtcand))
print('D- U2 sqrt',hex(c),'obstruction U0/1/2',pf(obstruction), 'pi3 residue',hex(red(obstruction[0:7]) if False else ((sum(((obstruction[i]>>1)&1)<<i for i in range(7))))))
# coefficient of pi^3 = 2-adic bit1 in pi0 coefficient; pi1/2 lower should vanish
v3=sum(((obstruction[i]>>1)&1)<<i for i in range(7))
assert bit0(uplus,1)==0x77 and bit0(uH,1)==0x3c
assert bit0(uminus,1)==0 and bit0(uminus,2)==0x55
assert c==0x0f and v3==0x08
# rank3: two different U1 bits + D- non-square deeper
print('RESULT PASS; independent Kummer 3-vector proof', 'U1 H',hex(bit0(uH,1)), 'D+',hex(bit0(uplus,1)), 'D- obstruction',hex(v3))
