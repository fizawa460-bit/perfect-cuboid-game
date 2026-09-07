#!/usr/bin/env python3
from __future__ import annotations
import itertools,json,math,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'
AV=ROOT/'stages/stage36/36-09AV/tunnell-actual-receiver-coordinate-specialization-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
AM_SRC=ROOT/'stages/stage36/36-09AM/tunnell-rankzero-torsion-sector-source-lock.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='d43db1874b0e657143fa07b1a16eb87fc27e0238'
AV_HEAD='b1b716f955d1a0b50bb5633364896b2f140d3f00'
AV_CI='34086307686'
CERT_BLOB='c1970a020803275ba87b249229e319367fa8f811'
AV_BLOB='a64689ae6f8683c4d4b66e4f67a24f58624150f5'
AE_BLOB='ddae37dd35cd0e732cebadf9c17f3f3fa57930df'
AM_SRC_BLOB='0c64262ac11979fa1f5e25039cfc0f4f0426ca62'
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def factor(n):
 n=abs(n); out=[]; p=2
 while p*p<=n:
  if n%p==0:
   out.append(p)
   while n%p==0:n//=p
  p+=1 if p==2 else 2
 if n>1:out.append(n)
 return out
def divs(ps):
 return [math.prod(p for p,b in zip(ps,z) if b) for z in itertools.product((0,1),repeat=len(ps))]
def jacobi(a,n):
 if n==1:return 1
 a%=n; r=1
 while a:
  while a%2==0:
   a//=2
   if n%8 in (3,5):r=-r
  a,n=n,a
  if a%4==3 and n%4==3:r=-r
  a%=n
 return r if n==1 else 0
def ae_ok(A,B,C,D,eta,e,f):
 rows=(jacobi(-eta*(2**e)*B*C,A),jacobi((2**f)*B*D,A),jacobi(eta*(2**e)*A*C,B),jacobi((2**f)*A*D,B),jacobi(A*B,C),jacobi((2**(1-f))*A*D,C),jacobi(-A*B,D),jacobi(eta*(2**(1-e))*A*C,D))
 return all(x==1 for x in rows)
def count_form(m,ax,az):
 tot=0
 for z in range(math.isqrt(m//az)+1):
  remz=m-az*z*z
  for x in range(math.isqrt(remz//ax)+1):
   rem=remz-ax*x*x; y=math.isqrt(rem)
   if y*y==rem:tot+=(1 if z==0 else 2)*(1 if x==0 else 2)*(1 if y==0 else 2)
 return tot
def tunnell(N):
 if N%2:a=count_form(N,2,32); b=count_form(N,2,8)
 else:
  m=N//2; a=count_form(m,4,32); b=count_form(m,4,8)
 return a,b,2*a==b
def enumerate_p(a,b):
 P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b)
 pp=[p for p in factor(P) if p!=2]; pm=[p for p in factor(M) if p!=2]; pd=[p for p in factor(D0) if p!=2]
 out=[]
 for A in divs(pp):
  for B in divs(pm):
   for ass in itertools.product((0,1,2),repeat=len(pd)):
    C=D=1
    for p,z in zip(pd,ass):
     if z==1:C*=p
     elif z==2:D*=p
    for e,f in itertools.product((0,1),repeat=2):
     if A%8==B%8 and (e,f)==(1,0):continue
     if A%8!=B%8 and (e,f)==(0,1):continue
     for eta in (-1,1):
      if ae_ok(A,B,C,D,eta,e,f):out.append((A,B,C,D,eta,e,f,2**((e+f)&1)*A*B*C*D))
 return P,M,D0,pp,pm,pd,out
def summary(a,b):
 P,M,D0,pp,pm,pd,br=enumerate_p(a,b); ns=sorted({x[-1] for x in br}); tr={n:tunnell(n) for n in ns}; surv=[x for x in br if tr[x[-1]][2]]; sns=sorted({x[-1] for x in surv})
 return dict(P=P,M=M,D0=D0,pp=pp,pm=pm,pd=pd,branches=len(br),distinct=len(ns),surv=len(surv),surv_distinct=len(sns),surv_N=sns)
def main():
 assert blob(CERT)==CERT_BLOB and blob(AV)==AV_BLOB and blob(AE)==AE_BLOB and blob(AM_SRC)==AM_SRC_BLOB
 subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
 subprocess.check_call(['git','merge-base','--is-ancestor',AV_HEAD,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); assert c['batch_parent']['36_09AV_exact_head']==AV_HEAD and c['batch_parent']['36_09AV_exact_head_ci']==AV_CI
 s12=summary(1,2); assert (s12['branches'],s12['distinct'],s12['surv'],s12['surv_distinct'])==(14,7,6,4); assert s12['surv_N']==[6,7,14,21]
 s=summary(2,11); assert (s['P'],s['M'],s['D0'])==(-73,-161,-2574); assert (s['pp'],s['pm'],s['pd'])==([73],[7,23],[3,11,13]); assert (s['branches'],s['distinct'],s['surv'],s['surv_distinct'])==(158,70,105,51)
 assert tunnell(73073)==(480,896,False); assert tunnell(240097)==(384,768,True)
 st=json.loads(STATE.read_text()); assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V85_36_09AW_CANDIDATE'; aw=st['authority_frontier']['36-09AW']; assert aw['FIXED_P_FINITE_OUTER_BRANCH_SIEVE']==True and aw['FIXED_P_EXCLUSION_RULE']==True; assert aw['P_2_OVER_11_EXCLUDED']==False; assert aw['CANDIDATE_PARAMETER_SET_SHRUNK']==False and aw['RECEIVER_CLOSED']==False; assert st['current']['unit']=='36-09AX' and st['current']['36_09AX_entry_allowed']==True
 print('36-09AW verified: fixed-p support-compatible branch set is finite; p=1/2 gives 14->6 branch instances and p=2/11 gives 158->105 after Tunnell. Zero survivors would certify fixed-p receiver emptiness; neither diagnostic p is excluded.')
if __name__=='__main__':main()
