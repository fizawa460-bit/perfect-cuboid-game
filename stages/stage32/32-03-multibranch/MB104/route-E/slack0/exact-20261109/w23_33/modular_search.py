import itertools,json,sys,time
from flint import nmod_poly
from sympy import primerange,sqrt_mod

def build(p):
 ii=int(sqrt_mod(-1,p));B=[(0,1),(1,0),(1,1),(p-1,1),(ii,1),(p-ii,1)]
 def det(a,b):return (a[0]*b[1]-a[1]*b[0])%p
 def frame(x,y,z):
  u=det(z,y);v=det(x,z);return [x[0]*u%p,y[0]*v%p,x[1]*u%p,y[1]*v%p]
 def inv(A):return [A[3],-A[1]%p,-A[2]%p,A[0]]
 def val(M,b):return ((M[0]*b[0]+M[1]*b[1])%p,(M[2]*b[0]+M[3]*b[1])%p)
 def make(P,Q,n):
  pts=[]; labs=[]
  for lab,(x,y) in enumerate(B):
   cf=[(y*u-x*v)%p for u,v in zip(P,Q)]
   f=nmod_poly(cf,p); rr=f.roots(); total=sum(m for _,m in rr)+n-f.degree()
   if total!=n:return None
   for rt,m in rr:
    if m==1:pts.append(int(rt));labs.append(lab//2)
    elif m!=2:return None
   if n-f.degree()==1:pts.append(p);labs.append(lab//2)
  assert len(pts)==2*n+4 and len(set(pts))==len(pts)
  return dict(n=n,P=P,Q=Q,pts=pts,labs=labs)
 out=[]
 for u,v in itertools.combinations(B,2):
  P=[u[0],0,v[0]];Q=[u[1],0,v[1]]
  m=make(P,Q,2)
  if m is None:return None
  out.append(m)
 for ids in itertools.combinations(range(6),4):
  ys=[B[i] for i in ids];T=frame(ys[1],ys[0],ys[2]);N=inv(T);z0,z1=val(N,ys[3]);z=z0*pow(z1,-1,p)%p
  H=nmod_poly([z,-8-2*z,36,-54,27],p);rr=H.roots()
  if len(rr)!=4 or any(m!=1 for _,m in rr):return None
  for k,_ in rr:
   k=int(k);A=(2*k-1)%p;C=(2-3*k)%p;P0=[0,0,C,A];Q0=[-k%p,1,0,0]
   P=[(T[0]*u+T[1]*v)%p for u,v in zip(P0,Q0)];Q=[(T[2]*u+T[3]*v)%p for u,v in zip(P0,Q0)]
   m=make(P,Q,3)
   if m is None:return None
   out.append(m)
 return dict(p=p,i=ii,B=B,maps=out)
if __name__=='__main__':
 if len(sys.argv)>1:
  p=int(sys.argv[1]);d=build(p);assert d is not None and len(d['maps'])==75
  json.dump(d,open('exact_w/split_data.json','w'),indent=2)
  print('verified split prime',p);sys.exit(0)
 for count,p in enumerate(primerange(1000,2000000)):
  if p%4!=1:continue
  d=build(p)
  if d:
   print('split prime',p,'covers',len(d['maps']),flush=True)
   json.dump(d,open('exact_w/split_data.json','w'),indent=2)
   break
 else:raise RuntimeError('no split prime in range')
