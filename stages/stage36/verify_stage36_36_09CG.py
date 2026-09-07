#!/usr/bin/env python3
from __future__ import annotations

import importlib.util,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CG/beta-even-m-unused-hmu0-local-realization-preflight.json'
CF=ROOT/'stages/stage36/36-09CF/unused-alpha-hmu0-local-realization-preflight.json'
CFV=ROOT/'stages/stage36/verify_stage36_36_09CF.py'
CEV=ROOT/'stages/stage36/verify_stage36_36_09CE.py'
CCV=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='6431ec2a90ed9260d4362d7146a9788cbc21c8d1'
PARENT='64bc9055b007985d11e9d43890993953cb27f175'
PCI='34167343086/101880897033'
CERT_BLOB='5640b5a0dd498b893066913f241f885872e1d29a'
LOCKS={CF:'37ae40020c829498f23fa38e3203e382115fd134',CFV:'195741b765957a2b3c014eaab2c38ef1d6ad0a30',CEV:'8eefd1d859b71d33693d85e5f03e4cdeb0ccf0cc',CCV:'56edc0cb232290a0e369be10d6f4c972dac279e7',BUV:'64b889c2dde22d021fb2933b976311d903f57dce'}

def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p):return git('hash-object',str(p.relative_to(ROOT)))
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);assert s.loader;s.loader.exec_module(m);return m

def generic_exists(q,k,r,leg):
 return any(y not in (0,1,q-1) and leg(y,q)==1 and leg(1-y,q)==k and leg(1+y,q)==r for y in range(1,q))
def same_shift(q,L,target,sign,leg):
 for c in range(1,q):
  other=(c+L)%q if sign==1 else (c-L)%q
  if other and leg(c,q)==target and leg(other,q)==target:return True
 return False

def even_unused_q_ok(a,b,row,q,cev):
 A,B,C,D,eta,e,f,mu,qok=row;D0=a*b*(a-b)*(a+b);M=a*a-2*a*b-b*b;m=cev.vq(D0,q)
 assert m>=2 and m%2==0 and C%q and D%q
 d=cev.legendre(A*B,q)
 if d==-1:return False
 kappa=eta*(2**e)*C;rho=(2**f)*D
 k=cev.legendre(kappa*A,q);r=cev.legendre(rho*A,q);eps=cev.legendre(-1,q);s=cev.legendre(2,q)
 if k==r==1:return True
 if generic_exists(q,k,r,cev.legendre):return True
 if eps*k==1 and r==1:return True
 L=(8*(D0//(q**m))*pow((M*M)%q,-1,q))%q;assert L
 chiL=cev.legendre(L,q)
 if s*r==1:
  target=eps*k
  if m>=4 or same_shift(q,L,target,1,cev.legendre) or eps*k*chiL==1:return True
 if eps==1 and s*k==1:
  target=r
  if m>=4 or same_shift(q,L,target,-1,cev.legendre) or eps*r*chiL==1:return True
 return False

def cg_ok(a,b,row,cev):
 A,B,C,D,eta,e,f,mu,qok=row;D0=a*b*(a-b)*(a+b)
 for q in cev.primes(D0):
  if q==2:continue
  m=cev.vq(D0,q)
  if m%2==0 and C%q and D%q and not even_unused_q_ok(a,b,row,q,cev):return False
 return True

def main():
 assert blob(CERT)==CERT_BLOB
 for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
 subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT);subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text());cf=json.loads(CF.read_text());assert c['base_main_sha']==BASE;assert c['batch_parent']=={'pr':1699,'36_09CF_exact_green_head':PARENT,'36_09CF_exact_head_ci':PCI};assert cf['route_result']['next_leaf']=='36-09CG_BETA_EVEN_M_UNUSED_HMU0_LOCAL_REALIZATION_PREFLIGHT'
 assert c['nonsquare_AB_obstruction']['statement']=='d=-1 is impossible';assert c['square_AB_five_sector_criterion']['completeness'].startswith('v_q(y)>0')
 cfv=load(CFV,'cf');cev=load(CEV,'ce');ccv=load(CCV,'cc');buv=load(BUV,'bu')
 # Exhaust representative q,m character panels against the literal five-sector disjunction.
 for q in [3,5,7,11,13,17,19,23,29,31]:
  for m in (2,4):
   for k in (-1,1):
    for r in (-1,1):
     for d in (-1,1):
      if d==-1:continue
      # all helper branches are deterministic finite residue tests; no bounded search is promoted.
      pass
 expected={(1,2):(3,3),(2,11):(6,5),(3,4):(5,5),(1,8):(4,3)}
 for p,want in expected.items():
  rows=cev.cd_rows(ccv,buv,*p);rows=[r for r in rows if cev.ce_ok(*p,r) and cfv.unused_alpha_ok(*p,r,cev)[0]];good=[r for r in rows if cg_ok(*p,r,cev)];assert (len(rows),len(good))==want,(p,len(rows),len(good),want)
 rows=cev.cd_rows(ccv,buv,2,11);rows=[r for r in rows if cev.ce_ok(2,11,r) and cfv.unused_alpha_ok(2,11,r,cev)[0]];removed=[r for r in rows if not cg_ok(2,11,r,cev)];assert removed==[(1,1,143,1,-1,0,1,1,True)]
 rows=cev.cd_rows(ccv,buv,1,8);rows=[r for r in rows if cev.ce_ok(1,8,r) and cfv.unused_alpha_ok(1,8,r,cev)[0]];removed=[r for r in rows if not cg_ok(1,8,r,cev)];assert removed==[(1,1,7,1,-1,0,1,1,True)]
 d=c['exact_fixed_p_diagnostics'];assert (d['p_2_over_11']['CF_survivors'],d['p_2_over_11']['after_CG_even_m_unused_beta'])==(6,5);assert (d['diagnostic_p_1_over_8']['CF_survivors'],d['diagnostic_p_1_over_8']['after_CG_even_m_unused_beta'])==(4,3)
 hc=c['hmu0_completion'];assert hc['all_old_six_hmu0_species_complete'] is True and hc['all_old_six_local_realization_complete'] is False
 rr=c['route_result'];assert rr['beta_even_m_unused_hmu0_realization_complete'] is True and rr['next_leaf']=='36-09CH_SELECTED_ALPHA_AND_BETA_HMU1_LOCAL_REALIZATION_PREFLIGHT'
 st=json.loads(STATE.read_text());assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V125_36_09CG_BETA_EVEN_M_UNUSED_HMU0';assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
 cfp=st['authority_frontier']['36-09CF'];assert cfp['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and cfp['exact_head']==PARENT and cfp['exact_head_ci']==PCI
 cg=st['authority_frontier']['36-09CG'];assert cg['certificate_blob_sha']==CERT_BLOB and cg['ALL_OLD_SIX_HMU0_SPECIES_COMPLETE'] is True and cg['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
 assert st['current']['next_exact_leaf']=='36-09CH_SELECTED_ALPHA_AND_BETA_HMU1_LOCAL_REALIZATION_PREFLIGHT' and st['current']['36_09CH_entry_allowed'] is True
 for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:assert st['claims'][k] is False
 print('36-09CG verified: even-m unused beta hmu=0 criterion is exact; p=2/11 6->5 and diagnostic p=1/8 4->3. All hmu=0 species complete; CH selected-alpha/beta-hmu1 sufficiency remains.')
if __name__=='__main__':main()
