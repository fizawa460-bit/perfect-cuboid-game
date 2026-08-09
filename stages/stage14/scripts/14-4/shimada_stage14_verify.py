#!/usr/bin/env python3
"""Independent exact verifier for the 4ak norm-16 void.
PARI is used only for the saturated integer kernel; enumeration is a separate
pure-Python exact LDL recursion, not qfminim.
"""
from fractions import Fraction
from math import isqrt, floor, ceil
import argparse, ast, json, subprocess
from pathlib import Path
N=20
OK=(ast.Expression,ast.List,ast.Tuple,ast.Constant,ast.UnaryOp,ast.USub,ast.UAdd,ast.Load)
def parse(path,name):
 t=path.read_text();k=t.find(name+':=');i=t.find('[',k);d=0;q=None;esc=False
 for j in range(i,len(t)):
  c=t[j]
  if q:
   if esc:esc=False
   elif c=='\\':esc=True
   elif c==q:q=None
   continue
  if c in "'\"":q=c
  elif c=='[':d+=1
  elif c==']':
   d-=1
   if d==0:
    z=ast.parse(t[i:j+1],mode='eval')
    if any(not isinstance(x,OK) for x in ast.walk(z)):raise ValueError(name)
    return ast.literal_eval(z)
 raise KeyError(name)
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def gps(M):return '['+';'.join(','.join(str(x) for x in r) for r in M)+']'
def dot(v,w,G):return sum(v[i]*G[i][j]*w[j] for i in range(N) for j in range(N))
def ldl(Q):
 n=len(Q);L=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)];D=[Fraction(0) for _ in range(n)]
 for i in range(n):
  D[i]=Fraction(Q[i][i])-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
  assert D[i]>0
  for j in range(i+1,n):L[j][i]=(Fraction(Q[j][i])-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/D[i]
 return L,D
def enum_exact(Q,B):
 L,D=ldl(Q);n=len(Q);z=[0]*n;hist={};vec=[]
 def rec(i,rem,total):
  if i<0:
   norm=int(total);hist[norm]=hist.get(norm,0)+1
   if norm==B:vec.append(z.copy())
   return
  off=sum(L[j][i]*z[j] for j in range(i+1,n));q=rem/D[i]
  rf=isqrt(q.numerator//q.denominator);center=-off
  lo=floor(center)-rf-2;hi=ceil(center)+rf+2
  for zi in range(lo,hi+1):
   term=D[i]*(Fraction(zi)+off)**2
   if term<=rem:
    z[i]=zi;rec(i-1,rem-term,total+term)
 rec(n-1,Fraction(B),Fraction(0));return hist,vec
def main():
 ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('refine',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 rr=json.loads(a.refine.read_text());p=[x for x in rr['candidates'] if x['pass']][0];M=p['M'];di=p['deck_candidates'][0]['index']
 s0=next(a.root.rglob('S0S3.txt'));b=next(a.root.rglob('Borcherds.txt'));G=parse(s0,'GramS0');Ts=parse(b,'Tsigma');inv=parse(b,'iotasigmaz');Dlt=mm(inv,Ts[di])
 A=[r[:] for r in Dlt]
 for i in range(N):A[i][i]+=1
 code=f'A={gps(A)};G={gps(G)};K=matkerint(A~);Q=-K~*G*K;print("R=",matsize(K)[2]);for(i=1,matsize(Q)[1],print("Q=",Vec(Q[i,])));'
 out=subprocess.run(['gp','-fq'],input=code,text=True,capture_output=True,check=True).stdout.splitlines();rank=int(next(x[2:] for x in out if x.startswith('R=')));Q=[ast.literal_eval(x[2:]) for x in out if x.startswith('Q=')];assert len(Q)==rank
 hist,v16=enum_exact(Q,16)
 result={'anti_rank':rank,'positive_form':Q,'exact_vector_histogram_norm_le_16':{str(k):v for k,v in sorted(hist.items())},'exact_norm16_vectors':len(v16),'norm16_void':len(v16)==0}
 a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'anti_rank':rank,'histogram':result['exact_vector_histogram_norm_le_16'],'norm16_void':result['norm16_void']},indent=2))
if __name__=='__main__':main()
