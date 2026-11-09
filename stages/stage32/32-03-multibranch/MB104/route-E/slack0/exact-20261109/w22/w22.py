import sympy as sp,itertools,json,time,sys
from flint import fmpq_poly as Poly, fmpq
from collections import Counter
start=time.time();K=sp.QQ.algebraic_field(sp.sqrt(2),sp.sqrt(-1+sp.I));mod=Poly([100,0,-8,0,24,0,-4,0,1])
class F:
 def __init__(self,p):self.p=p
 def __add__(a,b):return F(a.p+b.p)
 def __sub__(a,b):return F(a.p-b.p)
 def __neg__(a):return F(-a.p)
 def __mul__(a,b):return F((a.p*b.p)%mod)
 def __truediv__(a,b):
  g,s,t=b.p.xgcd(mod);assert g==1;return F((a.p*s)%mod)
 def __eq__(a,b):return a.p==b.p

def cv(z):return F(Poly([fmpq(str(c)) for c in reversed(K.from_sympy(sp.sympify(z)).to_list())]))
O=cv(1);Z=cv(0);I=cv(sp.I);s=cv(sp.sqrt(2));r=cv(sp.sqrt(-1+sp.I))
B=[(Z,O),(O,Z),(O,O),(-O,O),(I,O),(-I,O)]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def mv(A,p):return(A[0]*p[0]+A[1]*p[1],A[2]*p[0]+A[3]*p[1])
def mm(A,B):return tuple(A[2*j]*B[k]+A[2*j+1]*B[k+2] for j in range(2) for k in range(2))
def adj(A):return(A[3],-A[1],-A[2],A[0])
def frame(p,q,r):return(p[0]*det(r,q),q[0]*det(p,r),p[1]*det(r,q),q[1]*det(p,r))
def eq(p,q):return det(p,q)==Z
A=frame(*B[:3]);autos=[]
for dst in itertools.permutations(B,3):
 M=mm(frame(*dst),adj(A));perm=[]
 for q in B:
  ix=[j for j,v in enumerate(B) if eq(mv(M,q),v)]
  if not ix:break
  perm+=ix
 if len(perm)==6:autos.append(perm)
assert len(autos)==24
assert list(K.mod.to_list())==[1,0,-4,0,24,0,-8,0,100]
pts=[[(v,O) for v in [O,-O,I,-I,(O+I)/s,-(O+I)/s,(O-I)/s,-(O-I)/s]],[(v,O) for v in [I,-I,I/s,-I/s,r/s,-r/s,O/r,-O/r]]]
vals=[[2,2,3,3,4,4,5,5],[1,1,3,3,4,4,5,5]];covers=[[],[]];seen=set()
for shape,pair in enumerate([(0,1),(0,2)]):
 for perm in autos:
  key=tuple(sorted(perm[x] for x in pair))
  if key in seen:continue
  seen.add(key);covers[shape].append({'branch':key,'labels':[perm[x]//2 for x in vals[shape]],'perm':perm})
assert list(map(len,covers))==[3,12]
for sh,Pts in enumerate(pts):
 for idx,(x,z) in enumerate(Pts):
  value=(x*x,z*z) if sh==0 else (x*x,x*x+z*z)
  assert eq(value,B[vals[sh][idx]])
 assert all(not eq(p,q) for j,p in enumerate(Pts) for q in Pts[j+1:])

# Reduction ONLY rules out equality. All possible equalities checked in number field.
p=10009;roots=[x for x in range(p) if (x**8-4*x**6+24*x**4-8*x*x+100)%p==0];assert roots;alpha=roots[0]
def red(x):
 v=0
 for c in reversed(list(x.p)):v=(v*alpha+int(c.numerator)*pow(int(c.denominator),-1,p))%p
 return v
rp=[[(red(x),red(y)) for x,y in P] for P in pts]
assert all((x*u-y*v)%p for P in rp for i,(x,y) in enumerate(P) for v,u in P[i+1:])
def d(x,y):return(x[0]*y[1]-x[1]*y[0])%p
def fr(P):
 x,y,z=P;u=d(z,y);v=d(x,z);return(x[0]*u%p,y[0]*v%p,x[1]*u%p,y[1]*v%p)
def matmul(a,b):return tuple((a[2*j]*b[k]+a[2*j+1]*b[k+2])%p for j in range(2) for k in range(2))
def ad(a):return(a[3],-a[1],-a[2],a[0])
hist=Counter();accepted=Counter();tested=field_tests=bir=physical=0
for si in range(2):
 for sj in range(2):
  for tri in itertools.combinations(range(8),3):
   Fsrc=fr([rp[si][k] for k in tri]);Esrc=frame(*[pts[si][k] for k in tri])
   for dst in itertools.permutations(range(8),3):
    pairs=[(a,b) for a in covers[si] for b in covers[sj] if all(a['labels'][k]==b['labels'][l] for k,l in zip(tri,dst))]
    if not pairs:continue
    physical+=1;M=matmul(fr([rp[sj][k] for k in dst]),ad(Fsrc));possible=[]
    for k,(x,y) in enumerate(rp[si]):
     u=(M[0]*x+M[1]*y)%p;v=(M[2]*x+M[3]*y)%p
     for l,(z,w) in enumerate(rp[sj]):
      if "--no-sieve" in sys.argv or (u*w-v*z)%p==0:possible.append((k,l))
    EM=mm(frame(*[pts[sj][k] for k in dst]),adj(Esrc));matches=[]
    for k,l in possible:
     field_tests+=1
     if eq(mv(EM,pts[si][k]),pts[sj][l]):matches.append((k,l))
    for a,b in pairs:
     tested+=1;j=sum(a['labels'][k]==b['labels'][l] for k,l in matches);h=len(matches)-j;om=16-2*j-h;hist[om]+=1
     if om<=4:
      accepted[om]+=1
      nonbir=(EM[1]==Z and EM[2]==Z) or (EM[0]==Z and EM[3]==Z)
      if not nonbir:bir+=1
  print('shape',si,sj,'tested',tested,'time',round(time.time()-start,1),flush=True)
res={'sieve_enabled':'--no-sieve' not in sys.argv,'degree2_covers':15,'shape_counts':[3,12],'field_minpoly':str(mod),'reduction_prime':p,'reduction_root':alpha,'tested_label_matched_triple_occurrences':tested,'shape_triple_jobs':physical,'exact_field_equality_checks':field_tests,'omega_histogram_raw':dict(sorted(hist.items())),'omega_le4_raw':dict(accepted),'birational_omega_le4':bir,'seconds':time.time()-start,'status':'PASS' if bir==0 else 'COUNTEREXAMPLE'}
print(json.dumps(res,indent=2));open('w22_nosieve_result.json' if '--no-sieve' in sys.argv else 'w22_result.json','w').write(json.dumps(res,indent=2));assert tested==157824;assert bir==0
