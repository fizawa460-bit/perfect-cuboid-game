"""Fixed row344 Z_2 algebra and unit squareclasses; exploratory until verified."""
from pathlib import Path
from math import comb
import json
import os
import numpy as np

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'parents/PARENT_ROW345_LOCAL_DIMENSIONS/signed18_c2_full_maximal_order_certificate.json'
OLD=json.loads(CERT.read_text())
H=OLD['h2_coefficients_ascending']
F=[]
for j in range(37):
 c=sum(H[k]*comb(k,j)*2**j*(-3)**(k-j)for k in range(j,37))
 if c%2**36:raise ValueError('nonintegral F')
 F.append(c//2**36)
N=36
PREC=int(os.environ.get('LOCAL2_PRECISION','8'))
if not 8<=PREC<=16:raise ValueError('certified precision range8..16 only')
MOD=1<<PREC

def pgf_deg(a):return a.bit_length()-1
def pgf_mod(a,b):
 while a and pgf_deg(a)>=pgf_deg(b):a^=b<<(pgf_deg(a)-pgf_deg(b))
 return a
def pgf_mul(a,b,m):
 c=0
 while b:
  if b&1:c^=a
  a<<=1;b>>=1
 return pgf_mod(c,m)
def pgf_pow(a,k,m):
 c=1
 while k:
  if k&1:c=pgf_mul(c,a,m)
  a=pgf_mul(a,a,m);k>>=1
 return c
def pgf_inv(a,m):return pgf_pow(a,(1<<pgf_deg(m))-2,m)
R=sum(c<<i for i,c in enumerate(OLD['residual_coefficients_ascending']))
FACTORS=[]
for f in range(1<<4,1<<5):
 if f&1 and pgf_mod(R,f)==0:FACTORS.append(f);break
if not FACTORS:raise ValueError('no residual quartic')
def pgf_div(a,b):
 q=0
 while a and pgf_deg(a)>=pgf_deg(b):
  k=pgf_deg(a)-pgf_deg(b);q^=1<<k;a^=b<<k
 return q,a
FACTORS.append(pgf_div(R,FACTORS[0])[0])
def r_mul(a,b):return pgf_mul(a,b,R)
def r_pow(a,k):return pgf_pow(a,k,R)
def r_inv(a):
 # Every residue field has order dividing 2^8. Unit inverse exponent254.
 b=r_pow(a,254)
 if r_mul(a,b)!=1:raise ValueError('not a residue unit')
 return b
def r_sqrt(a):return r_pow(a,128)
def r_trace(a):
 out=[]
 for f in FACTORS:
  x=pgf_mod(a,f);t=0
  for i in range(pgf_deg(f)):
   t^=x;x=pgf_mul(x,x,f)
  if t not in (0,1):raise ValueError('bad trace')
  out.append(t)
 return out

# Powers of u in the monic F quotient, then exact diagonal basis scaling.
POW=[]
for k in range(71):
 if k<36: v=[int(i==k)for i in range(36)]
 else:
  v=[0]+POW[-1][:-1];a=POW[-1][-1]
  v=[v[i]-a*F[i]for i in range(36)]
 POW.append(v)
TABLE=np.empty((36,36,36),dtype=np.int64)
for i in range(36):
 for j in range(36):
  den=(i//3+j//3)
  out=[]
  for k,c in enumerate(POW[i+j]):
   shift=k//3-den
   if shift<0:
    if c%(1<<(-shift)):raise ValueError('nonintegral basis product')
    c//=1<<(-shift)
   else:c<<=shift
   out.append(c%MOD)
  TABLE[i,j,:]=out

ZERO=np.zeros(36,dtype=np.int64)
ONE=ZERO.copy();ONE[0]=1
U=ZERO.copy();U[1]=1
T=ZERO.copy();T[3]=1
def mul(a,b):return np.einsum('i,j,ijk->k',a,b,TABLE,optimize=False)%MOD
def power(a,n):
 out=ONE.copy()
 while n:
  if n&1:out=mul(out,a)
  a=mul(a,a);n>>=1
 return out
def residue(a):return sum((int(a[3*k])&1)<<k for k in range(12))
def lift(a):
 v=ZERO.copy()
 for k in range(12):v[3*k]=(a>>k)&1
 return v
def inv(a):
 c=lift(r_inv(residue(a)))
 # Initial inverse modulo u. Newton twice reaches modulo2, then doubles.
 for i in range(7):c=mul(c,(2*ONE-mul(a,c))%MOD)
 if not np.array_equal(mul(a,c),ONE):raise ValueError('inverse failed')
 return c
def divide_u(a,prec):
 m=1<<prec;newm=m//2
 aa=[int(c)%m for c in a]
 if any(aa[3*k]&1 for k in range(12)):raise ValueError('not divisible by u')
 final=[-F[k]*(1<<(k//3))//(1<<11)for k in range(36)]
 if any((-F[k]*(1<<(k//3)))%(1<<11)for k in range(36)):raise ValueError('u last column')
 if final[0]%4 not in (2,):raise ValueError('constant u coefficient')
 b35=(aa[0]//2)*pow((final[0]//2)%newm,-1,newm)%newm
 b=[]
 for k in range(1,36):
  n=(aa[k]-final[k]*b35)%m
  if k%3==0:
   if n&1:raise ValueError('division parity')
   n//=2
  b.append(n%newm)
 b.append(b35)
 return np.array(b,dtype=np.int64),prec-1
def leading(a,i):
 b=(a-ONE)%MOD;p=PREC
 for j in range(i):b,p=divide_u(b,p)
 return residue(b)

GEN={};GINV={}
for level in range(1,6):
 up=power(U,level)
 for k in range(12):
  v=ZERO.copy();v[3*k]=1
  g=(ONE+mul(up,v))%MOD
  GEN[(level,k)]=g;GINV[(level,k)]=inv(g)

def unit_class(a):
 a=a.copy()%MOD
 ar=residue(a)
 if ar!=1:
  b=lift(r_sqrt(ar));a=mul(a,power(inv(b),2))
 bits=0
 for level in range(1,6):
  c=leading(a,level)
  if level&1:
   slot=(level//2)*12
   for k in range(12):
    if(c>>k)&1:
     bits|=1<<(slot+k);a=mul(a,GINV[(level,k)])
  else:
   b=r_sqrt(c)
   for k in range(12):
    if(b>>k)&1:a=mul(a,power(GINV[(level//2,k)],2))
  if leading(a,level)!=0:raise ValueError('filtration elimination')
 c=leading(a,6)
 top=r_trace(r_mul(r_mul(2,2),c))  # t is the residue variable, bit polynomial 2
 bits|=top[0]<<36;bits|=top[1]<<37
 return bits

def eval_u(poly):
 v=ZERO.copy()
 for k,c in enumerate(poly):
  if k<36:v[k]=(v[k]+c*(1<<(k//3)))%MOD
  else:
   pp=np.array([(z*(1<<(i//3)))%MOD for i,z in enumerate(POW[k])],dtype=np.int64)
   v=(v+c*pp)%MOD
 return v
def eval_theta(poly):
 th=(2*U-3*ONE)%MOD;v=ZERO.copy()
 for c in reversed(poly):v=(mul(v,th)+c*ONE)%MOD
 return v

def rank(vectors):
 piv={}
 for vv in vectors:
  v=int(vv)
  while v:
   k=v.bit_length()-1
   if k in piv:v^=piv[k]
   else:piv[k]=v;break
 return len(piv)

if __name__=='__main__':
 import time
 start=time.time()
 chars=[]
 for level in (1,3,5):
  for k in range(12):
   c=unit_class(GEN[(level,k)])
   if c!=1<<((level//2)*12+k):raise ValueError(('basis character',level,k,c))
   chars.append(c)
 for k in range(12):
  v=ZERO.copy();v[3*k]=1
  chars.append(unit_class((ONE+mul(power(U,6),v))%MOD))
 print(json.dumps({'F_mod8':[(i,c%8)for i,c in enumerate(F)if c%8],
   'residual_factors':[bin(f)for f in FACTORS],'unit_basis_rank':rank(chars),
   'minus1':hex(unit_class((-ONE)%MOD)),'five':hex(unit_class(5*ONE)),
   'seconds':time.time()-start}))
