"""Construct global E_theta points, NOT physical endpoints; check exact coarse gates."""
from fractions import Fraction as F
from math import gcd,isqrt
import json

def prime(n): return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def mul(z,w): return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def rep(p):
 for y in range(0,isqrt(p)+1,4):
  x=isqrt(p-y*y)
  if x*x+y*y==p and x%2: return x,y
 raise AssertionError(p)
def gaussian_root(M):
 left=M; z=(1,0)
 for p in range(2,isqrt(M)+2):
  if left%p: continue
  assert prime(p) and p%24==17
  r=rep(p)
  while left%p==0: z=mul(z,r);left//=p
 if left>1:
  assert prime(left) and left%24==17; z=mul(z,rep(left))
 a,b=mul(z,z); return abs(a),abs(b)
def val(n,p):
 n=abs(n); assert n; v=0
 while n%p==0:n//=p;v+=1
 return v
def factors(n):
 out=[]
 for p in range(2,isqrt(n)+2):
  if n%p==0:
   e=0
   while n%p==0:n//=p;e+=1
   out.append((p,e))
 if n>1:out.append((n,1))
 return out
def quartic(a,b,M,t):
 return a*a*M**6*t**4-3*a*b*b*M**4*t**3-(11*a*a-b*b)*M*M*b*b*t*t//4+a*b**4*t-b**4//16

records=[]; nonsquares=0
mods=[p for p in range(17,5001) if p%24==17 and prime(p)]
mods += [17**2,17*41,41**2,17*41*89]
for M in mods:
 a,b=gaussian_root(M)
 assert a*a+b*b==M*M and gcd(a,b)==1 and b%8==0
 k0=((pow(8*a,-1,M)-1)*pow(b,-1,M))%M
 ts=[1+b*(k0+j*M) for j in range(27)]
 t0=next(t for t in ts if a%3 or quartic(a,b,M,t)%27==9)
 assert 1<=t0<=28*M*M and gcd(t0,b*M)==1
 s=b;t=M*M*t0;N=M*M
 Psi=b*b-12*a*b*b*t0+4*a*a*M*M*t0*t0
 H=(2*a*b*b)**2; g=gcd(Psi,H)
 assert g==4
 q=Psi//4; A=M**4*q;C=(a*b*b)**2
 theta=F(A,C)
 assert q>0 and gcd(A,C)==1 and A<=785*M**12 and C<=M**6
 u=F(a,b);v=u*u;w=F(a*M*M*t0,b*b);xx=-(v+1);zz=(v+1)*(3-2*w)
 assert zz*zz==xx*(xx*xx+(9+4*theta)*xx+4*theta)
 xleg=F(1,16*a*t0)
 rsq=(theta-3*(v+1))/16+xleg*(1-xleg)
 fr=quartic(a,b,M,t0)
 assert rsq==F(fr,(4*a*b*b*t0)**2) and fr>0 and fr%8==1
 if b%3: assert val(fr,3)==2 and fr//9%3==1
 else: assert fr%3==1
 for p,lam in factors(M):
  assert (16*a*t0-2)%p**lam==0
  assert gcd(q,p)==1 and val(A,p)==4*lam
  assert (fr*pow((4*a*b*b*t0)**2,-1,p))%p==pow(4,-1,p)
  assert (8*lam)//gcd(8*lam,2*lam)==4
 Phi=N*s**4-16*a*b*s**3*t+(44*a*a-4*b*b)*s*s*t*t+48*a*b*s*t**3-16*a*a*t**4
 assert -Phi//(M*M)==16*fr and Phi%(M*M)==0
 square=isqrt(fr)**2==fr
 nonsquares+=not square
 if len(records)<5:records.append({'M':M,'a':a,'b':b,'t0':t0,'quartic_F':fr,'global_r_square':square})
out={'card':'M3-T11-127','status':'PASS','constructed_global_E_theta_points':len(mods),
     'prime_M_cases':len(mods)-4,'multi_prime_or_power_M_cases':4,
     'missing_global_r_square_cases':nonsquares,'examples':records,
     'scope':'All cases pass Q, Q2, Q3, real and fresh-prime coarse adapters. Not all places, not original global r, not physical height or cuboids.',
     'global_counting_credit':False,'primary_gate_closed':False}
with open('M3-T11-127-verification.json','w') as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
