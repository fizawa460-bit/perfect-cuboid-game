import itertools,math,json
from pathlib import Path

class Ring:
 def __init__(self,squares):self.squares=squares
 def c(self,x):return (x,0,0,0,0,0,0,0)
 def root(self,i):return tuple(int(k==1<<i) for k in range(8))
 def add(self,a,b):return tuple(x+y for x,y in zip(a,b))
 def neg(self,a):return tuple(-x for x in a)
 def sub(self,a,b):return self.add(a,self.neg(b))
 def scale(self,a,k):return tuple(k*x for x in a)
 def mul(self,a,b):
  z=[0]*8
  for i,x in enumerate(a):
   if not x:continue
   for j,y in enumerate(b):
    if not y:continue
    v=x*y
    for k in range(3):
     if (i&j)&(1<<k):v*=self.squares[k]
    z[i^j]+=v
  return tuple(z)
 def power(self,a,n):
  z=self.c(1)
  for _ in range(n):z=self.mul(z,a)
  return z

def p_int(R,A):
 Z=R*R;Q=[a*a*(2*Z-a*a) for a in A]
 D=Z**4+sum(q*q for q in Q)-2*Z*Z*sum(Q)-2*sum(Q[i]*Q[j] for i,j in itertools.combinations(range(3),2))
 return D*D-64*Z*Z*Q[0]*Q[1]*Q[2]

samples=0;inverse_coordinates=0;unique_branches=0
for u,v,w in itertools.product(range(1,9),range(1,6),range(1,6)):
 e=(2*u*v,2*u*w,abs(u*u-v*v-w*w));R=u*u+v*v+w*w
 if not all(e):continue
 assert sum(x*x for x in e)==R*R
 m=[R*R-x*x for x in e]
 assert all(m) and not all(math.isqrt(q)**2==q for q in m)
 K=Ring(m);Z=K.c(R*R);f=[K.root(i) for i in range(3)]
 A=[K.add(K.c(x),y) for x,y in zip(e,f)];Y=[K.sub(K.c(x),y) for x,y in zip(e,f)]
 qi=[K.sub(K.scale(Z,2),K.power(a,2)) for a in A]
 Q=[K.mul(K.power(a,2),q) for a,q in zip(A,qi)]
 for q,y in zip(qi,Y):assert q==K.power(y,2)
 U=[2*x*x-R*R for x in e]
 for a,y,b in zip(A,Y,U):assert K.mul(a,y)==K.c(b)
 assert sum(U)==-R*R
 D=K.power(Z,4)
 for q in Q:D=K.add(D,K.power(q,2));D=K.sub(D,K.scale(K.mul(K.power(Z,2),q),2))
 for i,j in itertools.combinations(range(3),2):D=K.sub(D,K.scale(K.mul(Q[i],Q[j]),2))
 P=K.sub(K.power(D,2),K.scale(K.mul(K.power(Z,2),K.mul(K.mul(Q[0],Q[1]),Q[2])),64))
 assert P==K.c(0)
 Ki=[K.sub(Z,K.power(a,2)) for a in A];grad=[]
 for i in range(3):
  j,k=[j for j in range(3) if j!=i]
  dD=K.sub(K.sub(K.scale(Q[i],2),K.scale(K.power(Z,2),2)),K.scale(K.add(Q[j],Q[k]),2))
  g=K.mul(K.scale(K.mul(A[i],Ki[i]),4),K.sub(K.scale(K.mul(D,dD),2),K.scale(K.mul(K.power(Z,2),K.mul(Q[j],Q[k])),64)))
  grad.append(g)
 h=K.c(0)
 for i in range(3):
  j,k=[j for j in range(3) if j!=i]
  h=K.add(h,K.mul(K.mul(A[i],Ki[i]),K.mul(grad[j],grad[k])))
 assert h!=K.c(0)
 for i in range(3):
  j,k=[j for j in range(3) if j!=i]
  Ni=K.scale(K.mul(Ki[i],K.mul(grad[j],grad[k])),-R*R)
  assert K.mul(Y[i],h)==Ni
  inverse_coordinates+=1
 branches=[s for s in itertools.product((-1,1),repeat=3) if R*R+sum(a*b for a,b in zip(s,U))==0]
 assert branches==[(1,1,1)]
 unique_branches+=1;samples+=1

# Rational integer P census. No off-boundary physical point is asserted or found.
points=0;zeros=0;boundary_zeros=0;off_boundary_zeros=0
for R in range(1,21):
 lim=math.isqrt(2*R*R)
 for A in itertools.combinations_with_replacement(range(1,lim+1),3):
  points+=1
  if p_int(R,A):continue
  zeros+=1
  if any(a*a==R*R for a in A):boundary_zeros+=1
  else:
   off_boundary_zeros+=1
   roots=[]
   for a in A:
    q=2*R*R-a*a;assert q>0 and math.isqrt(q)**2==q
    roots.append(math.isqrt(q))
   valid=[s for s in itertools.product((-1,1),repeat=3) if sum(a*y*si for a,y,si in zip(A,roots,s))==-R*R]
   assert len(valid)==1

out={'status':'PASS','real_algebraic_sphere_samples':samples,
 'exact_gradient_inverse_coordinate_checks':inverse_coordinates,
 'unique_signed_branch_checks':unique_branches,'rational_integer_projection_census':points,
 'P_zero_points':zeros,'boundary_P_zero_points':boundary_zeros,
 'off_boundary_P_zero_points':off_boundary_zeros,'physical_endpoints_enumerated':0,
 'global_counting_credit':0,'audit':'within-session; not external'}
Path(__file__).with_name('verification146.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
