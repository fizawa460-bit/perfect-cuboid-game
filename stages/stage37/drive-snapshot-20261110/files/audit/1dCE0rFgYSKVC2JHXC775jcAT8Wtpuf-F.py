import json, math
from pathlib import Path
class Poly:
 def __init__(self,d): self.d={k:v for k,v in d.items() if v}
 @staticmethod
 def coerce(x): return x if isinstance(x,Poly) else Poly({(0,0):x})
 def __add__(self,b):
  b=self.coerce(b);d=self.d.copy()
  for k,v in b.d.items():d[k]=d.get(k,0)+v
  return Poly(d)
 __radd__=__add__
 def __neg__(self): return Poly({k:-v for k,v in self.d.items()})
 def __sub__(self,b): return self+-self.coerce(b)
 def __mul__(self,b):
  b=self.coerce(b);d={}
  for (i,j),v in self.d.items():
   for (k,l),w in b.d.items():d[i+k,j+l]=d.get((i+k,j+l),0)+v*w
  return Poly(d)
 __rmul__=__mul__
 def __pow__(self,n):
  a=Poly({(0,0):1})
  for _ in range(n):a=a*self
  return a
 def derivative_m(self): return Poly({(i-1,j):i*v for (i,j),v in self.d.items() if i})
m,n=Poly({(1,0):1}),Poly({(0,1):1})
A=(m**4-n**4)*(m**4-81*n**4)
B=4*m*n*(m*m-3*n*n)*(m**4+2*m*m*n*n+9*n**4)
C=16*m*m*n*n*(m**4-9*n**4)
D1=m**8+46*m**4*n**4+81*n**8
D2=4*m*n*(m*m-3*n*n)*(m**4+10*m*m*n*n+9*n**4)
D=(m**4-2*m*m*n*n+9*n**4)*(m**4+10*m*m*n*n+9*n**4)
assert all(not z.d for z in [A*A+C*C-D1*D1,B*B+C*C-D2*D2,A*A+B*B+C*C-D*D])
J=(m*m+n*n)*(m*m+9*n*n)
L=(m*m-n*n)*(m*m-9*n*n)
assert not (A-J*L).d
assert not (D2-4*m*n*(m*m-3*n*n)*J).d
assert (C.derivative_m()*D-C*D.derivative_m()).d
checked=0; examples=[]
for nn in range(1,115):
 for mm in range(3*nn+1,401):
  if math.gcd(mm,nn)!=1: continue
  aa=(mm**4-nn**4)*(mm**4-81*nn**4)
  bb=4*mm*nn*(mm*mm-3*nn*nn)*(mm**4+2*mm*mm*nn*nn+9*nn**4)
  cc=16*mm*mm*nn*nn*(mm**4-9*nn**4)
  d1=mm**8+46*mm**4*nn**4+81*nn**8
  d2=4*mm*nn*(mm*mm-3*nn*nn)*(mm**4+10*mm*mm*nn*nn+9*nn**4)
  dd=(mm**4-2*mm*mm*nn*nn+9*nn**4)*(mm**4+10*mm*mm*nn*nn+9*nn**4)
  both=mm%2==1 and nn%2==1; div3=mm%3==0
  g=math.gcd(math.gcd(aa,bb),cc);g1=math.gcd(aa,cc);g2=math.gcd(bb,cc)
  k=4*mm*nn*(mm*mm-3*nn*nn)
  e=g2//k; jj=(mm*mm+nn*nn)*(mm*mm+9*nn*nn)
  assert g==2**(5*both)*3**(4*div3)
  assert g1==2**(7*both)*3**(4*div3)
  assert e==2**(2*both)*3**(2*div3)
  f1=(cc//g1,aa//g1,d1//g1);f2=(cc//g2,bb//g2,d2//g2)
  c12=math.gcd(f1[2],f2[1]);c21=math.gcd(f2[2],f1[1]); cr=c12*c21;rr=dd//g
  assert c21*e*g1>=jj
  assert cr==math.gcd(f1[2]*f2[2],rr)
  assert rr%cr==0
  assert math.gcd(aa//g,math.gcd(bb//g,cc//g))==1
  assert (aa//g)**2+(bb//g)**2+(cc//g)**2==rr*rr
  checked+=1
  if (mm,nn) in [(15,4),(19,5),(39,10),(77,20),(151,40)]:
   examples.append(dict(m=mm,n=nn,R=rr,c12=c12,c21=c21,c=cr))
out=dict(status='PASS',symbolic_identities=5,exact_primitive_and_crossgcd_cases=checked,examples=examples,finite_replay_not_universal_proof=True,global_counting_credit=0)
Path('/workspace/scratch/a5e20b2bdfbe/verify156-result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
