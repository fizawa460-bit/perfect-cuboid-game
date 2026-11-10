from fractions import Fraction as Q
import math,json,itertools
from pathlib import Path

def mul(p,q):
 r=[0]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]+=a*b
 return r

def sf(n):
 r=1;p=2
 while p*p<=n:
  odd=0
  while n%p==0:n//=p;odd^=1
  if odd:r*=p
  p+=1
 return r*n

def sc(n):
 # positive rational squareclass as a squarefree integer
 v=Q(n);return sf(v.numerator*v.denominator)

def C(x,A,F):return x*(x-A*A)*(x-F*F)
def H(x,A,F,k):return (x*x-A*A*F*F)**2-4*k*k*C(x,A,F)
def roots(A,F,k):return [(k+e*A)*(k+d*F) for e,d in itertools.product((1,-1),repeat=2)]
triples=[]
for m in range(2,101):
 for n in range(1,m):
  if math.gcd(m,n)!=1 or (m-n)%2==0:continue
  A=m*m-n*n;F=2*m*n;k=m*m+n*n
  triples.append((A,F,k))
poly=halves=descent=0
for A,F,k in triples:
 rr=roots(A,F,k);p=[1]
 for r in rr:p=mul(p,[-r,1])
 aa=A*A;bb=F*F
 expected=[aa*aa*bb*bb,-4*k*k*aa*bb,4*k**4-2*aa*bb,-4*k*k,1]
 assert p==expected and len(set(rr))==4
 disc=math.prod((rr[i]-rr[j])**2 for i in range(4) for j in range(i))
 assert disc==4096*A**8*F**8*k**4*(A*A-F*F)**2
 assert H(0,A,F,k)*H(aa,A,F,k)*H(bb,A,F,k)==A**8*F**8*(A*A-F*F)**4
 poly+=1
 # Exact zero-third-edge boundary, not a positive physical endpoint.
 x=(k+F)*(k+A);y=-(k+F)*(k+A)*(F+A)
 assert y*y==C(x,A,F)
 lam=Q(3*x*x-2*k*k*x+aa*bb,2*y)
 x2=lam*lam+k*k-2*x;y2=-y+lam*(x-x2)
 assert x2==k*k and y2==-k*A*F and H(x,A,F,k)==0
 assert -Q(x*x-aa*bb,2*y)==k
 assert -Q(x*x-2*aa*x+aa*bb,2*y)==F
 assert -Q(x*x-2*bb*x+aa*bb,2*y)==A
 assert k*k<=x<=4*k*k and abs(y)<=8*k**3
 halves+=1
 delta=sf(A+F)
 assert (2*abs(A*A-F*F))%delta==0
 assert sc(x)==2 and sc(x-aa)==delta and sc(x-bb)==sc(2*delta)
 descent+=1
# Nonzero full three-quadratic lift identities over finite fields.
field={};nonzero=0;phasechecks=0
for p in (41,73,89):
 rootsmod={}
 for v in range(1,p):rootsmod.setdefault(v*v%p,[]).append(v)
 count=0
 for A,F,k in ((3,4,5),(5,12,13),(8,15,17)):
  for t in range(1,p):
   for r1 in rootsmod.get((t*t+F*F)%p,[]):
    for r2 in rootsmod.get((t*t+A*A)%p,[]):
     for z in rootsmod.get((t*t+k*k)%p,[]):
      x=(z+r1)*(z+r2)%p;y=-(z+r1)*(z+r2)*(r1+r2)%p
      if y==0:continue
      assert y*y%p==C(x,A,F)%p
      lam=(3*x*x-2*k*k*x+A*A*F*F)*pow(2*y,-1,p)%p
      x2=(lam*lam+k*k-2*x)%p;y2=(-y+lam*(x-x2))%p
      assert x2==z*z%p and y2==(-z*r1*r2)%p
      inv=pow(2*y,-1,p)
      assert -(x*x-A*A*F*F)*inv%p==z
      assert -(x*x-2*A*A*x+A*A*F*F)*inv%p==r1
      assert -(x*x-2*F*F*x+A*A*F*F)*inv%p==r2
      w=2*y*t%p
      assert w*w%p==H(x,A,F,k)%p
      for f3 in (k,-k):
       NT=A*r1+F*r2+t*f3
       U=A*F*t-A*r2*f3-F*r1*f3-t*r1*r2
       V=r1*F*t+r2*A*t+f3*A*F-r1*r2*f3
       assert (U*U+V*V-z**6)%p==0
       assert (NT*V-2*A*F*t*z*z)%p==0
       phasechecks+=1
      count+=1
 field[str(p)]=count;nonzero+=count
# Actual adjacent-face pairs for integer-space diagonal synthetic triples:
# check conductor support where the pair exists; no positive cuboid found/asserted.
# Boundary identities above test squareclasses without implying positive occupancy.
out={'card':'M3-T11-190','status':'PASS','primitive_faces_checked':poly,'split_quartic_discriminant_resultant_checks':poly,'canonical_halfpoints_checked':halves,'boundary_kummer_label_checks':descent,'nonzero_finite_field_full_lifts':field,'finite_field_total':nonzero,'phase_polynomial_pullback_checks':phasechecks,'physical_endpoints_enumerated':0,'scope':'Exact boundary arithmetic and nonzero finite-field full-lift identities; neither positive rational endpoints nor a moving-family count.'}
Path('M3-T11-190-verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
