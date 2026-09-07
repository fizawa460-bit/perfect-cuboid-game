#!/usr/bin/env python3
from __future__ import annotations
import json,math,subprocess
from pathlib import Path
import verify_stage36_36_09AW as aw
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09AY/universal-boundary-tunnell-survivor-preflight.json'
AX=ROOT/'stages/stage36/36-09AX/bounded-fixed-p-tunnell-sieve-scan-preflight.json'
AW=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='726198a3d8ca4834e45c2ef275a75266b0f752b4'
AX_HEAD='97e3f4bfc4345b05b74e9baf780ed8ff1baf38cb'
AX_CI='34086964554/101632741310'
CERT_BLOB='add18004debf95a218a6393f6c2f18f2bd4f7e10'
AX_BLOB='e72142f2ec8a2ab0dec4a6602874e1c2edc87c60'
AW_BLOB='c1970a020803275ba87b249229e319367fa8f811'
AD_BLOB='9d0388845955efee71d1a761ae4ee943d8b565d5'
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def v2(n):
 n=abs(n); k=0
 while n%2==0: n//=2; k+=1
 return k
def sf(n):
 n=abs(n); out=1; p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e^=1
  if e:out*=p
  p+=1 if p==2 else 2
 if n>1:out*=n
 return out
def odd_sf(n):
 s=sf(n); return s//2 if s%2==0 else s
def constructed(a,b):
 P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b); h=math.gcd(abs(P),abs(M))
 assert h==(2 if a%2 and b%2 else 1)
 U=(P//h)**2; V=(M//h)**2
 assert math.gcd(U,V)==1 and U!=V
 assert P*P-M*M==8*D0
 assert P*P+M*M==2*(a*a+b*b)**2
 A=B=D=1; C=odd_sf(D0); eta=1 if D0>0 else -1
 e=v2(U-V)&1; f=v2(U+V)&1
 assert f==1 and e==((1+v2(D0))&1)
 N=(2**((e+f)&1))*C
 assert N==sf(D0)
 assert sf(abs(U*V*(U*U-V*V)))==N
 assert M*M*U-P*P*V==0
 _,_,_,_,_,_,branches=aw.enumerate_p(a,b)
 branch=(A,B,C,D,eta,e,f,N)
 assert branch in branches
 assert aw.tunnell(N)[2] is True
 return branch
def main():
 assert blob(CERT)==CERT_BLOB and blob(AX)==AX_BLOB and blob(AW)==AW_BLOB and blob(AD)==AD_BLOB
 subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
 subprocess.check_call(['git','merge-base','--is-ancestor',AX_HEAD,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); assert c['base_main_sha']==BASE; assert c['freshness_sync']['current_main']==BASE; assert c['freshness_sync']['stage36_source_drift'] is False; assert c['batch_parent']['36_09AX_exact_head']==AX_HEAD and c['batch_parent']['36_09AX_exact_head_ci']==AX_CI
 tested=0
 for a in range(1,21):
  for b in range(1,21):
   if a==b or math.gcd(a,b)!=1:continue
   constructed(a,b); tested+=1
 assert tested==254
 assert c['tunnell_survival']['all_fixed_p_outer_sieves_have_at_least_one_Tunnell_survivor'] is True
 assert c['boundary_nature']['Lminus']=='M^2*U-P^2*V=0'
 assert c['boundary_nature']['retained_open_status']=='EXCLUDED_BRANCH_POINT'
 r=c['route_result']; assert r['route_status']=='BLOCKED_NEW_PATTERN_ISOLATED'; assert r['uniform_fixed_p_zero_exclusion_impossible_for_AW_outer_sieve'] is True; assert r['candidate_parameter_set_shrunk'] is False; assert r['receiver_closed'] is False
 st=json.loads(STATE.read_text()); assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V87_36_09AY_AUDIT_CHECKPOINT'; assert st['status']=='ACTIVE_BATCH_HOSTILE_AUDIT_CHECKPOINT'; ay=st['authority_frontier']['36-09AY']; assert ay['UNIVERSAL_BOUNDARY_TUNNELL_SURVIVOR'] is True; assert ay['AW_ZERO_SURVIVOR_FIXED_P_EXCLUSION_STRUCTURALLY_IMPOSSIBLE'] is True; assert ay['BOUNDARY_SURVIVOR_IS_RETAINED_RECEIVER'] is False; assert ay['CANDIDATE_PARAMETER_SET_SHRUNK'] is False; assert ay['RECEIVER_CLOSED'] is False; assert st['current']['unit']=='36-09AY-AUDIT-CHECKPOINT'; assert st['current']['36_09AZ_entry_allowed'] is False
 print(f'36-09AY verified on {tested} primitive diagnostics plus exact identities: universal AW Tunnell survivor A=B=D=1,C=odd_sf(D0) comes from X=K boundary with Lminus=0. Tunnell-only fixed-p zero sieve is structurally impossible; no retained receiver claimed.')
if __name__=='__main__':main()
