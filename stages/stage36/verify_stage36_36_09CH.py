#!/usr/bin/env python3
from __future__ import annotations

import importlib.util,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CH/selected-alpha-beta-hmu1-local-realization-preflight.json'
CG=ROOT/'stages/stage36/36-09CG/beta-even-m-unused-hmu0-local-realization-preflight.json'
CGV=ROOT/'stages/stage36/verify_stage36_36_09CG.py'
CFV=ROOT/'stages/stage36/verify_stage36_36_09CF.py'
CEV=ROOT/'stages/stage36/verify_stage36_36_09CE.py'
CC=ROOT/'stages/stage36/36-09CC/general-old-six-qq-source-pullback-preflight.json'
CCV=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='6431ec2a90ed9260d4362d7146a9788cbc21c8d1'
PARENT='b1df8d28a9875a4089102bf6d7d6067cd24d9b3f'
PCI='34167627515/101881727503'
CERT_BLOB='abedc4b33bf1c92e98efdcc43b5f0744630750a7'
LOCKS={CG:'5640b5a0dd498b893066913f241f885872e1d29a',CGV:'7a210e55a5e2386fb02a59de00502a4e810b9410',CFV:'195741b765957a2b3c014eaab2c38ef1d6ad0a30',CEV:'8eefd1d859b71d33693d85e5f03e4cdeb0ccf0cc',CC:'5067d1723952edce9f4bab55cc427eb1745211cc',CCV:'56edc0cb232290a0e369be10d6f4c972dac279e7',AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',BUV:'64b889c2dde22d021fb2933b976311d903f57dce'}

def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p):return git('hash-object',str(p.relative_to(ROOT)))
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);assert s.loader;s.loader.exec_module(m);return m

def generic_square_y(q,k,r,leg):
 return any(y not in (0,1,q-1) and leg(y,q)==1 and leg(1-y,q)==k and leg(1+y,q)==r for y in range(1,q))

def unused_odd_hmu1_ok(a,b,row,q,cev):
 A,B,C,D,eta,e,f,mu,qok=row;D0=a*b*(a-b)*(a+b);m=cev.vq(D0,q)
 assert m%2==1 and C%q and D%q and mu%q==0 and cev.legendre(A*B,q)==1
 kappa=eta*(2**e)*C;rho=(2**f)*D
 k=cev.legendre(kappa*A,q);r=cev.legendre(rho*A,q);eps=cev.legendre(-1,q);s=cev.legendre(2,q)
 if k==r==1:return True
 if generic_square_y(q,k,r,cev.legendre):return True
 if eps*k==1 and r==1:return True
 if m>=3 and s*r==1:return True
 if m>=3 and eps==1 and s*k==1:return True
 return False

def beta_hmu1_ok(a,b,row,cev):
 A,B,C,D,eta,e,f,mu,qok=row;D0=a*b*(a-b)*(a+b)
 for q in cev.primes(D0):
  if q==2 or mu%q!=0:continue
  m=cev.vq(D0,q);csel=C%q==0;dsel=D%q==0
  assert cev.legendre(A*B,q)==1
  if m%2==1 and not csel and not dsel:
   if not unused_odd_hmu1_ok(a,b,row,q,cev):return False
  elif m%2==0 and csel and not dsel:
   # AE q|C plus row has the character of 2*rho*A.
   assert cev.legendre((2**(1-f))*A*D,q)==1
  elif m%2==0 and dsel and not csel:
   # AE q|D gives chi(-AB)=1, so CC chi(AB)=1 forces chi(-1)=1.
   assert cev.legendre(-A*B,q)==1 and cev.legendre(-1,q)==1
   assert cev.legendre(eta*(2**(1-e))*A*C,q)==1
  else:
   raise AssertionError(('unexpected hmu1 species',a,b,row,q,m,csel,dsel))
 return True

def selected_alpha_rows_consistent(a,b,row,cev):
 A,B,C,D,eta,e,f,mu,qok=row;P=a*a+2*a*b-b*b;M=a*a-2*a*b-b*b;kappa=eta*(2**e)*C;rho=(2**f)*D
 for q in cev.primes(P):
  if q!=2 and A%q==0:
   assert q%8==1
   assert cev.legendre(-kappa*B,q)==1 and cev.legendre(rho*B,q)==1
   assert cev.legendre(kappa*B,q)==1
 for q in cev.primes(M):
  if q!=2 and B%q==0:
   assert q%8==1
   assert cev.legendre(kappa*A,q)==1 and cev.legendre(rho*A,q)==1
   assert cev.legendre(-kappa*A,q)==1
 return True

def main():
 assert blob(CERT)==CERT_BLOB
 for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
 subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT);subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text());cg=json.loads(CG.read_text());cc=json.loads(CC.read_text());ae=json.loads(AE.read_text())
 assert c['base_main_sha']==BASE;assert c['batch_parent']=={'pr':1699,'36_09CG_exact_green_head':PARENT,'36_09CG_exact_head_ci':PCI};assert cg['route_result']['next_leaf']=='36-09CH_SELECTED_ALPHA_AND_BETA_HMU1_LOCAL_REALIZATION_PREFLIGHT';assert cc['route_result']['alpha_selected_filter_exact'] is True
 sa=c['selected_alpha_sufficiency'];bh=c['beta_hmu1_species'];uo=c['unused_odd_m_beta'];oc=c['old_six_completion']
 assert sa['selected_alpha_local_realization_complete'] is True and sa['new_branch_filter'] is False
 assert 'odd m with q unused' in bh['classification']
 assert uo['criterion'].startswith('the disjunction of the five') and uo['point_independent'] is True
 assert oc['all_old_six_local_realization_complete'] is True and oc['does_not_cover_Q_reservoir'] is True
 assert ae['selected_prime_local_rows']['q_divides_C']==['(A*B/q)=+1','(2^(1-f)*A*D/q)=+1']
 assert ae['selected_prime_local_rows']['q_divides_D']==['(-A*B/q)=+1','(eta*2^(1-e)*A*C/q)=+1']

 cgv=load(CGV,'cgv');cfv=load(CFV,'cfv');cev=load(CEV,'cev');ccv=load(CCV,'ccv');buv=load(BUV,'buv')
 expected={(1,2):(3,3),(2,11):(5,5),(3,4):(5,3),(1,8):(3,3)}
 for p,want in expected.items():
  rows=cev.cd_rows(ccv,buv,*p);rows=[r for r in rows if cev.ce_ok(*p,r) and cfv.unused_alpha_ok(*p,r,cev)[0] and cgv.cg_ok(*p,r,cev)]
  for r in rows:selected_alpha_rows_consistent(*p,r,cev)
  good=[r for r in rows if beta_hmu1_ok(*p,r,cev)]
  assert (len(rows),len(good))==want,(p,len(rows),len(good),want)
 # The diagnostic p=3/4 loss is genuinely beta-hmu1 and not a selected-alpha effect.
 rows=cev.cd_rows(ccv,buv,3,4);rows=[r for r in rows if cev.ce_ok(3,4,r) and cfv.unused_alpha_ok(3,4,r,cev)[0] and cgv.cg_ok(3,4,r,cev)]
 removed=[r for r in rows if not beta_hmu1_ok(3,4,r,cev)];assert len(removed)==2
 d=c['exact_fixed_p_diagnostics'];assert (d['p_1_over_2']['CG_survivors'],d['p_1_over_2']['after_CH_all_old_six'])==(3,3);assert (d['p_2_over_11']['CG_survivors'],d['p_2_over_11']['after_CH_all_old_six'])==(5,5);assert d['diagnostic_p_3_over_4']['after_CH_all_old_six']==3
 rr=c['route_result'];fw=c['scope_firewalls'];assert rr['all_old_six_local_realization_complete'] is True;assert rr['fixed_p_parameter_exclusion_obtained'] is False;assert rr['next_leaf']=='36-09CI_GENERAL_Q_RESERVOIR_LOCAL_REALIZATION_PREFLIGHT'
 for k in ['old_six_complete_means_Q_reservoir_complete','CH_survivor_is_global_receiver','simultaneous_all_place_local_point_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:assert fw[k] is False
 st=json.loads(STATE.read_text());assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V126_36_09CH_OLD_SIX_LOCAL_COMPLETE';assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
 cgp=st['authority_frontier']['36-09CG'];assert cgp['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and cgp['exact_head']==PARENT and cgp['exact_head_ci']==PCI
 ch=st['authority_frontier']['36-09CH'];assert ch['certificate_blob_sha']==CERT_BLOB and ch['ALL_OLD_SIX_LOCAL_REALIZATION_COMPLETE'] is True and ch['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
 assert st['current']['next_exact_leaf']=='36-09CI_GENERAL_Q_RESERVOIR_LOCAL_REALIZATION_PREFLIGHT' and st['current']['36_09CI_entry_allowed'] is True
 for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:assert st['claims'][k] is False
 print('36-09CH verified: selected-alpha and beta-hmu1 local realization are exact. All six old-six reservoirs are locally classified branch-by-branch. Retained diagnostics p=1/2=3, p=2/11=5 survive; Q-reservoir remains next.')
if __name__=='__main__':main()
