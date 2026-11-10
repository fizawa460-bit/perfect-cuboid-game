from fractions import Fraction as F
from math import gcd
import json

def vp(x,p):
 x=F(x)
 if not x: return None
 n,d=abs(x.numerator),x.denominator; v=0
 while n%p==0: n//=p; v+=1
 while d%p==0: d//=p; v-=1
 return v

def gaussian_power(z,k):
 a,b=1,0
 for _ in range(k): a,b=a*z[0]-b*z[1],a*z[1]+b*z[0]
 return abs(a),abs(b)

cases=0; saturated=0; excess_examples=[]
for p,base in [(5,(2,1)),(13,(3,2)),(17,(4,1)),(29,(5,2))]:
 for lam in range(1,5):
  a,b=gaussian_power(base,2*lam); M=p**lam; N=a*a+b*b
  assert N==M*M and gcd(a,b)==1
  v=F(a*a,b*b); av=v+1
  for s in range(1,31):
   if s%p==0: continue
   t=M*M; w=F(a*t,b*s)
   theta=av*(av-12*w+4*w*w)/(4*v)
   if not theta: continue
   z=av*(3-2*w); x=-av
   assert z*z==x*(x*x+(9+4*theta)*x+4*theta)
   A,C=theta.numerator,theta.denominator
   assert A%M**4==0 and gcd(C,M)==1
   q=A//M**4; e=vp(q,p)
   D=16*A*A+56*A*C+81*C*C
   c4=16*C*C*(16*A*A+60*A*C+81*C*C)
   delta=256*A*A*C**8*D
   assert vp(c4,p)==0 and vp(delta,p)==8*lam+2*e
   assert gcd(abs(q),D) in [1,3,9,27,81]
   assert gcd(M,D)==1
   assert vp(C*C*x,p)==2*lam and vp(C**3*z,p)==2*lam
   n=8*lam+2*e
   order=n//gcd(n,2*lam)
   if e==0: assert order==4
   # Necessary fresh rational-r detector; no global physical realization asserted.
   xleg=F(s,16*a*b)
   residue=(xleg.numerator*pow(xleg.denominator,-1,p))%p
   rhs=residue*(1-residue)%p
   if p%12==5 and (rhs==0 or pow(rhs,(p-1)//2,p)==1):
    assert e==0; saturated+=1
   if e and len(excess_examples)<5:
    excess_examples.append({'p':p,'lambda':lam,'s':s,'e':e,'component_order':order})
   cases+=1

out={'card':'M3-T11-126','status':'PASS','exact_E_theta_point_cases':cases,
     'p5mod12_local_r_compatible_saturated_cases':saturated,
     'synthetic_overvaluation_examples':excess_examples,
     'scope':'Synthetic E_theta points verify adapters; original rational-r and physical R<=B are NOT asserted. Component classification uses cited theorem, not a Tate algorithm run.',
     'global_counting_credit':False,'primary_gate_closed':False}
with open('M3-T11-126-verification.json','w') as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
