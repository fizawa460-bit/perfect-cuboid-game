import json,math,time,sys
from pathlib import Path
from fractions import Fraction as Q
from flint import fmpz_poly
P=Path(__file__).resolve().parent/'parents/rank6.json'
D=json.loads(P.read_text());h=D['h2_coefficients_ascending'];A=D['A_coefficients_ascending']
def v2(x):return (abs(x)&-abs(x)).bit_length()-1 if x else 10**9
def fast_inverse_y(K,M):
 steps=M.bit_length()+2;prec=M+steps;mod=1<<prec
 invA=[1]
 for n in range(1,K+1):invA.append(-sum(A[j]*invA[n-j]for j in range(1,min(n,len(A)-1)+1))%mod)
 c=fmpz_poly(invA);hp=fmpz_poly(h)
 def trunc(p,m):return fmpz_poly([int(p[i])%m for i in range(min(len(p),K+1))])
 for _ in range(steps):
  error=trunc(3-hp*trunc(c*c,mod),mod)
  if any(int(z)%2 for z in error.coeffs()):raise ArithmeticError('inverse-square-root parity')
  error=fmpz_poly([int(z)//2 for z in error.coeffs()]);prec-=1;mod=1<<prec;c=trunc(c*error,mod)
 diff=trunc(c*c*hp-1,mod)
 if diff!=fmpz_poly([]):raise ArithmeticError('inverse-square-root identity')
 if any((int(c[i])-invA[i])%8 for i in range(K+1)):raise ArithmeticError('positive square-root branch')
 return[int(c[i])for i in range(K+1)]
def check_point(q):
 N=q['N'];K=q['K'];scale=q['scale'];shift=v2(scale);M=N+K.bit_length()+6;mod=1<<M;mask=mod-1
 c=fast_inverse_y(K,M);a=q['a_coefficients'];power=[[int(i==j)for j in range(17)]for i in range(17)];p=[]
 for k in range(1,K+1):
  last=power[-1];power=[[( (power[i-1][j]if i else 0)-a[i]*last[j])&mask for j in range(17)]for i in range(17)]
  pk=sum(power[i][i]for i in range(17))&mask;s=v2(k)
  if pk%(1<<(s+shift)):raise ArithmeticError('trace logarithm denominator')
  p.append((pk>>(s+shift))*pow(k>>s,-1,1<<N)%(1<<N))
 result=[sum(c[k-j-1]*p[k-1]for k in range(j+1,K+1))%(1<<N)for j in range(17)]
 target=[]
 for j in range(17):
  r=0
  for k in range(j+1,K+1):
   s=v2(k)
   if 4*k-4-s<N:r+=c[k-j-1]*(16**k>>(4+s))*pow(k>>s,-1,1<<N)
  target.append(r%(1<<N))
 if result!=target:raise ArithmeticError('independent actual logarithm mismatch')
 return{'N':N,'K':K,'scale':scale,'actual_17_logs_recomputed':True,'tail_degree_lower':K//17+1,'tail_v2_lower':(K//17+1)-(K//17+1).bit_length()-shift}
