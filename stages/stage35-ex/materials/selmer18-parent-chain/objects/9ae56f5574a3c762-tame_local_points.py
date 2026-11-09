"""Construct actual Q2 divisors via tame e=3 Hensel points."""
from local2_arithmetic import *
import time

def irreducible(f):
 n=pgf_deg(f)
 if n==1:return True
 r=2
 for i in range(1,n+1):
  r=pgf_mul(r,r,f)
  if i<=n//2:
   a=r^2;b=f
   while a:b,a=a,pgf_mod(b,a)
   if b!=1:return False
 return r==2

class Tame:
 def __init__(self,m,prec):
  self.m=m;self.f=pgf_deg(m);self.n=3*self.f;self.prec=prec;self.mod=1<<prec
  if self.n*self.n*(self.mod-1)**3>=2**63:raise ValueError('unsafe int64 bound')
  self.mc=[(m>>i)&1 for i in range(self.f)]
  self.one=np.zeros(self.n,dtype=np.int64);self.one[0]=1
  self.pi=self.one*0;self.pi[1]=1
  def wp(k):
   v=[0]*self.f
   if k<self.f:v[k]=1;return v
   v=wp(k-1);lead=v[-1];v=[0]+v[:-1]
   return[v[i]-lead*self.mc[i]for i in range(self.f)]
  wps=[wp(k)for k in range(2*self.f+1)]
  self.tab=np.zeros((self.n,self.n,self.n),dtype=np.int64)
  for i in range(self.n):
   for j in range(self.n):
    r=(i%3+j%3)%3;q=i//3+j//3+(i%3+j%3)//3;c=2**((i%3+j%3)//3)
    for k,cc in enumerate(wps[q]):self.tab[i,j,3*k+r]=c*cc%self.mod
  self.G=[]
  for i,c in enumerate(F):
   r=i%3;q=i//3;shift=q-12
   if shift<0:
    if c%(1<<(-shift)):raise ValueError('normalized coefficient')
    c//=1<<(-shift)
   else:c<<=shift
   vv=self.one*0
   for k,cc in enumerate(wp(q)):vv[3*k+r]=c*cc%self.mod
   self.G.append(vv)
 def mul(self,a,b):return np.einsum('i,j,ijk->k',a,b,self.tab,optimize=False)%self.mod
 def pow(self,a,n):
  out=self.one.copy()
  while n:
   if n&1:out=self.mul(out,a)
   a=self.mul(a,a);n>>=1
  return out
 def res(self,a):return sum((int(a[3*k])&1)<<k for k in range(self.f))
 def lift(self,r):
  v=self.one*0
  for k in range(self.f):v[3*k]=(r>>k)&1
  return v
 def inv(self,a):
  r=self.res(a)
  if not r:raise ValueError('nonunit')
  ri=pgf_pow(r,(1<<self.f)-2,self.m)
  c=self.lift(ri)
  for i in range(2+self.prec.bit_length()):c=self.mul(c,(2*self.one-self.mul(a,c))%self.mod)
  if not np.array_equal(self.mul(a,c),self.one):raise ValueError('tame inverse')
  return c
 def peval(self,coeff,z):
  v=self.one*0
  for c in reversed(coeff):v=(self.mul(v,z)+c)%self.mod
  return v
 def solve(self,y):
  z=self.one.copy();target=self.mul(y,y)
  deriv=[(i*self.G[i])%self.mod for i in range(1,len(self.G))]
  for it in range(8):
   err=(self.peval(self.G,z)-target)%self.mod
   if not np.any(err):break
   dz=self.mul(err,self.inv(self.peval(deriv,z)))
   z=(z-dz)%self.mod
  if np.any((self.peval(self.G,z)-target)%self.mod):raise ValueError('Hensel precision not reached')
  return self.mul(self.pi,z)
 def charpoly(self,a):
  n=self.n
  mat=np.einsum('i,ijk->kj',a,self.tab,optimize=False)%self.mod
  mat=mat.astype(object)
  pp=np.eye(n,dtype=object);traces=[0]
  for k in range(1,n+1):
   pp=pp@mat;traces.append(sum(pp[i,i]for i in range(n)))
  cc=[1]
  for k in range(1,n+1):
   numer=-sum(cc[k-j]*traces[j]for j in range(1,k+1))
   if numer%k:raise ValueError('Newton trace division')
   cc.append(numer//k)
  return[list(reversed(cc))[i]%self.mod for i in range(n+1)]

def image_unit(g,f):
 # Norm u-U divided by rational 2^f; Newton slope implies integrality.
 v=ZERO.copy()
 for j,c in enumerate(g):
  shift=j//3-f
  if shift<0:
   dd=1<<(-shift)
   if c%dd:raise ValueError('norm polynomial divisibility')
   c//=dd
  else:c<<=shift
  if j<36:v[j]=(v[j]+c)%MOD
  else:raise ValueError('excess norm degree')
 return v

if __name__=='__main__':
 start=time.time();scalar=unit_class((-ONE)%MOD);vec=[scalar]
 records=[]
 prior=json.loads((ROOT/'explore-unramified-generators.json').read_text())
 for r in prior['vectors']:
  c=unit_class(eval_u(r['poly_u']))
  if rank(vec+[c])>rank(vec):vec.append(c)
 print('INITIAL fake rank',rank(vec)-1,flush=True)
 for f in range(1,9):
  polys=[m for m in range((1<<f)|1,1<<(f+1),2)if (f==1 or irreducible(m)) and pgf_mod(R,m)!=0 and pgf_mod(sum(((i*int((R>>i)&1))&1)<<(i-1)for i in range(1,13)),m)!=0]
  if not polys:continue
  m=polys[0];E=Tame(m,PREC+f+1)
  rs=pgf_pow(pgf_mod(R,m),1<<(f-1),m);y0=E.lift(rs)
  for level in range(0,5):
   for k in range(1 if level==0 else f):
    y=y0.copy()
    if level:
     b=E.one*0;b[3*k]=1;y=(y+E.mul(E.pow(E.pi,level),b))%E.mod
    u=E.solve(y);g=E.charpoly(u);a=image_unit(g,f)
    if residue(a)==0:raise ValueError('nonunit image')
    c=unit_class(a)
    if rank(vec+[c])>rank(vec):
     vec.append(c)
     rec={'f':f,'m_binary':m,'level':level,'k':k,'field_precision':E.prec,'y_basis_mod':list(map(int,y)),
       'u_basis_mod':list(map(int,u)),'norm_poly_mod':g,'unit_basis_mod':list(map(int,a)),
       'character_hex':hex(c),'fake_rank':rank(vec)-1}
     records.append(rec);print('NEW',f,level,k,hex(c),'rank',rank(vec)-1,'seconds',round(time.time()-start,2),flush=True)
     (ROOT/'tame-local-point-candidates.json').write_text(json.dumps({'records':records,'prior':prior,'fake_rank':rank(vec)-1},indent=2)+'\n')
    if rank(vec)-1>=18:break
   if rank(vec)-1>=18:break
  print('END f',f,'rank',rank(vec)-1,flush=True)
  if rank(vec)-1>=18:break
 print('FINAL',rank(vec)-1,'new',len(records),'seconds',time.time()-start,flush=True)
