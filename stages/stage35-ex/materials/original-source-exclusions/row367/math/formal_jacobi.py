import sys,json,time,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from fractions import Fraction
import os
os.environ['LOCAL2_PRECISION']='16'
import local2_arithmetic as L
import numpy as np
PARENT=ROOT
D=json.loads((ROOT/'parents/rank6.json').read_text());A=D['A_coefficients_ascending'];B=D['B_coefficients_ascending'];h=D['h2_coefficients_ascending']
G=17
def solve(cols,target):
 piv={}
 for i,v in enumerate(cols):
  word=1<<i
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,word);break
   w,m=piv[k];v^=w;word^=m
 word=0
 while target:
  k=target.bit_length()-1
  if k not in piv:return None,len(piv)
  v,m=piv[k];target^=v;word^=m
 return word,len(piv)
def series(K,mod):
 d=[0]*35
 for i,a in enumerate(B):
  for j,b in enumerate(B):d[i+j]+=(a//2)*(b//2)
 z=[0]*(K+1);y=[0]*(K+1);y[0]=1
 for n in range(1,K+1):
  z[n]=(-sum(A[i]*z[n-i] for i in range(1,min(n,len(A)-1)+1))-sum(z[i]*z[n-i]for i in range(1,n))-(d[n-1]if n-1<len(d)else 0))%mod
  y[n]=((A[n]if n<len(A)else 0)+2*z[n])%mod
 c=[1]
 for n in range(1,K+1):c.append((-sum(y[i]*c[n-i]for i in range(1,n+1)))%mod)
 return y,c
def v2(n):return (n&-n).bit_length()-1 if n else 10**9
def lift(N=20,X=16,scale=2):
 K=34*(N+2);M=N+K.bit_length()+6;mod=1<<M;outmod=1<<N;vs=v2(scale)
 y,c=series(K,mod)
 def logmap(b):
  aa=[0]+[((-1)**i)*scale*b[i-1] for i in range(1,18)];p=[0]*(K+1)
  for k in range(1,K+1):p[k]=(-sum(aa[i]*p[k-i]for i in range(1,min(k-1,17)+1))-(k*aa[k]if k<=17 else 0))%mod
  q=[]
  for k in range(1,K+1):
   s=v2(k)
   if p[k]%(1<<(s+vs)):raise ArithmeticError('nonintegral logarithm')
   q.append((p[k]>>(s+vs))*pow(k>>s,-1,outmod)%outmod)
  return [sum(c[k-j-1]*q[k-1]for k in range(j+1,K+1))%outmod for j in range(17)]
 target=[]
 for j in range(17):
  value=0
  for k in range(j+1,K+1):
   s=v2(k)
   if 4*k-4-s>=N:continue
   value+=c[k-j-1]*(X**k>>(4+s))*pow(k>>s,-1,outmod)
  target.append(value%outmod)
 T=[sum((c[i-j-1]%2)<<j for j in range(i))for i in range(1,18)]
 if scale==2:
  matrix=[sum(((c[i-j-1]if i>j else 0)^(c[2*i-j-1]if 2*i>j else 0))%2<<j for j in range(17))for i in range(1,18)]
 else:matrix=T
 init,rk=solve(matrix,sum((t%2)<<j for j,t in enumerate(target)))
 if init is None:raise ArithmeticError('no initial root')
 b=[init>>i&1 for i in range(17)]
 residuals=[]
 for n in range(1,N):
  got=logmap(b);err=[(got[i]-target[i])%outmod for i in range(17)]
  if any(e%2**n for e in err):raise ArithmeticError('Hensel residual')
  r=sum(((e>>n)&1)<<j for j,e in enumerate(err));corr,_=solve(T,r)
  b=[bb+(1<<n)*(corr>>i&1)for i,bb in enumerate(b)];residuals.append(n)
 if logmap(b)!=target:raise ArithmeticError('final logarithm')
 a=[0]*18;a[17]=1
 for i,bb in enumerate(b,1):a[17-i]=((-1)**i*scale*bb)%(1<<(N+vs))
 # Original X=theta=2u-3, so evaluate in the inherited maximal order.
 raw=L.eval_theta([z%65536 for z in a])
 # theta is a fourth power; denominator theta^17 is a square, hence may be
 # omitted for the fake character, but normalize by its inverse for clarity.
 theta=L.eval_u([-3,2]);z=L.power(theta,17)
 zi=L.inv(z);unit=L.mul(raw,zi)%256
 L.MOD=256;L.PREC=8;char=L.unit_class(unit);L.MOD=65536;L.PREC=16
 return {'N':N,'X':X,'scale':scale,'K':K,'initial_mod2_rank':rk,'initial_bits_hex':hex(init),'b_mod2N':b,'a_coefficients':a,'target':target,'unit_mod256':list(map(int,unit)),'fake_character_hex':hex(char)}
if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=256);ap.add_argument('--output-dir',type=Path,required=True);args=ap.parse_args()
 args.output_dir.mkdir(parents=True,exist_ok=True)
 for n,scale in [(32,4),(args.precision,2)]:
  q=lift(n,16,scale);name=('q4' if scale==4 else 'q8')+'_P'+str(n)+'.json'
  (args.output_dir/name).write_text(json.dumps(q,indent=2)+'\n')
  print(json.dumps({'output':name,'precision':n,'scale':scale,'raw_character':q['fake_character_hex']}),flush=True)
