#!/usr/bin/env python3
"""Goal4AJ diagnostic: isolate the generation6 D13 x D9 bottleneck.

Generation6 proved all six equal-multiplicity group powers are computable in fresh
Singular processes, but timed out only when merging the compact D13 basis with the
large 87-generator D9 basis.  This preflight never materializes the full denominator.
It replaces D9 by four independently powered multiplicity-9 prime divisors and folds
those four factors into D13 one at a time in fresh Singular processes.  PASS means
only that this exact bottleneck can be crossed without first materializing the large
D9 aggregate basis.  Diagnostic only: no literal denominator/F_B/E1 credit.
"""
from __future__ import annotations
import ast,hashlib,json,subprocess,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
PARENT=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_reflexive_generator.py'
GEN6=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_multiprocess_generator_gen6.py'
PARENT_BLOB='7dbf3179ca800b16109de3f423fc919541237dd7'
GEN6_BLOB='45d08379e95054facb6f8a6d7f4649ae3840b591'
GEN6_RUN=34112730244
GEN6_JOB=101712969213
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'
DEN_RIGIDITY_SHA='e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc'
REFLEXIVE_PREFLIGHT_SHA='1d1395746942bd7d5748e408192761ebf6dce92eeb2760fd34fe9295d674db3b'

def git_blob(path:Path)->str:
 b=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert git_blob(PARENT)==PARENT_BLOB
assert git_blob(GEN6)==GEN6_BLOB

tree=ast.parse(PARENT.read_text(encoding='utf-8')); vals={}
for node in tree.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in {'IDEALS','GROUPS'}:
  vals[node.targets[0].id]=ast.literal_eval(node.value)
IDEALS=vals['IDEALS']; GROUPS=vals['GROUPS']
assert GROUPS[13]==[37,39] and GROUPS[9]==[26,31,58,60]

COMMON=r'''
option(redSB); LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp; minpoly=u^4+1; number ii=u^2; number ss=u-u^3;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
matrix Jac=jacob(surf); ideal Sing=minor(Jac,4);
proc contained(ideal A,ideal B){ideal G=std(B); int j; for(j=1;j<=size(A);j++){if(reduce(A[j],G)!=0){return(0);}} return(1);}
proc equalideal(ideal A,ideal B){return(contained(A,B)==1 && contained(B,A)==1);}
proc rprod(ideal A,ideal B){ideal C=surf+A*B; list LL=sat(C,Sing); return(std(LL[1]));}
'''

def run_singular(tag:str,body:str,timeout:int=600)->list[str]:
 script=COMMON+body+'\nquit;\n'
 with tempfile.TemporaryDirectory() as td:
  p=Path(td)/(tag+'.sing'); p.write_text(script,encoding='utf-8')
  try: cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=timeout)
  except subprocess.TimeoutExpired as exc:
   out=exc.stdout or ''; out=out.decode('utf-8',errors='replace') if isinstance(out,bytes) else out
   print('GOAL4AJ_DEN_G9_SPLIT_TIMEOUT_TAG='+tag,flush=True)
   if out: print('GOAL4AJ_DEN_G9_SPLIT_TIMEOUT_TAIL='+json.dumps(out[-12000:]),flush=True)
   raise SystemExit('Goal4AJ group9 split bottleneck timed out; no mathematical obstruction credit')
 low=cp.stdout.lower()
 if cp.returncode!=0 or any(s in low for s in ('error occurred','? error','? cannot','? wrong','? member','? assign')):
  print('GOAL4AJ_DEN_G9_SPLIT_FAIL_TAG='+tag,flush=True)
  print('GOAL4AJ_DEN_G9_SPLIT_STDOUT_TAIL='+json.dumps(cp.stdout[-12000:]),flush=True)
  if cp.stderr: print('GOAL4AJ_DEN_G9_SPLIT_STDERR='+json.dumps(cp.stderr[-12000:]),flush=True)
  raise SystemExit('Goal4AJ group9 split bottleneck failed closed')
 gens=[x.split('=',1)[1] for x in cp.stdout.splitlines() if x.startswith('GOAL4AJ_G9_GEN=')]
 if not gens: raise SystemExit('Goal4AJ group9 split stage returned no generators')
 payload='\n'.join(gens).encode(); sha=hashlib.sha256(payload).hexdigest()
 print(f'GOAL4AJ_DEN_G9_SPLIT_STAGE={tag}:gens={len(gens)}:bytes={len(payload)}:sha256={sha}',flush=True)
 return gens

def decl(name:str,gens:list[str])->str: return f'ideal {name}='+','.join(gens)+';\n'
def dump(name:str)->str: return f'int j; for(j=1;j<=size({name});j++){{print("GOAL4AJ_G9_GEN="+string({name}[j]));}}\n'

def group13_body()->str:
 return (
  f'ideal P={IDEALS[37]}; ideal G=std(surf+P); P={IDEALS[39]}; G=rprod(G,std(surf+P)); '
  'ideal X2=rprod(G,G); ideal X3=rprod(X2,G); ideal X6=rprod(X3,X3); ideal X12=rprod(X6,X6); ideal D=rprod(X12,G); '+dump('D')
 )

def prime9_body(idx:int)->str:
 return (
  f'ideal P={IDEALS[idx]}; ideal G=std(surf+P); '
  'ideal X2=rprod(G,G); ideal X4=rprod(X2,X2); ideal X8=rprod(X4,X4); ideal D=rprod(X8,G); '+dump('D')
 )

def merge_body(A:list[str],B:list[str])->str:
 return decl('A',A)+decl('B',B)+'ideal D=rprod(A,B); '+dump('D')

D=run_singular('group13',group13_body(),600)
stage_shas={'group13':hashlib.sha256('\n'.join(D).encode()).hexdigest()}
stage_counts={'group13':len(D)}
for idx in GROUPS[9]:
 P9=run_singular(f'prime{idx}_pow9',prime9_body(idx),600)
 stage_shas[f'prime{idx}_pow9']=hashlib.sha256('\n'.join(P9).encode()).hexdigest(); stage_counts[f'prime{idx}_pow9']=len(P9)
 D=run_singular(f'fold_prime{idx}_into_D13',merge_body(D,P9),600)
 stage_shas[f'fold_prime{idx}_into_D13']=hashlib.sha256('\n'.join(D).encode()).hexdigest(); stage_counts[f'fold_prime{idx}_into_D13']=len(D)

# The resulting divisor is exactly 13(P37+P39)+9(P26+P31+P58+P60).
inspect=decl('D',D)+r'''
list L=sat(D,Sing); ideal DS=std(L[1]); if(equalideal(D,DS)!=1){ERROR("folded bottleneck ideal not saturation-stable");}
print("GOAL4AJ_G9_GEN="+string(size(D)));
'''
# Re-run only a tiny saturation-stability check; its one integer generator marker is not used as a basis.
with tempfile.TemporaryDirectory() as td:
 p=Path(td)/'inspect.sing'; p.write_text(COMMON+inspect+'quit;\n',encoding='utf-8')
 cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=600)
 if cp.returncode!=0 or 'error' in cp.stdout.lower():
  print('GOAL4AJ_DEN_G9_SPLIT_INSPECT_TAIL='+json.dumps(cp.stdout[-12000:]),flush=True); raise SystemExit('Goal4AJ group9 split final stability check failed closed')

out={'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_GROUP9_PRIMEWISE_BOTTLENECK_PREFLIGHT_V7','source_locks':{'parent_generation2_blob_sha1':PARENT_BLOB,'generation6_blob_sha1':GEN6_BLOB,'generation6_failed_run':GEN6_RUN,'generation6_failed_job':GEN6_JOB,'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,'denominator_rigidity_canonical_sha256':DEN_RIGIDITY_SHA,'reflexive_product_preflight_canonical_sha256':REFLEXIVE_PREFLIGHT_SHA},'constructor':'fresh Singular process for D13, each multiplicity-9 prime power, and each sequential fold into D13','generation6_completed_all_six_group_powers':True,'generation6_only_observed_failure_stage':'merge13_9 timeout at 600 seconds','group9_prime_indices':GROUPS[9],'stage_basis_sha256':stage_shas,'stage_generator_counts':stage_counts,'crossed_generation6_merge13_9_bottleneck':True,'final_folded_basis_generator_count':len(D),'literal_degree19_denominator_residual_materialized':False,'literal_degree31_denominator_materialized':False,'literal_F_B_materialized':False,'E1_proved':False,'stage35_closed':False,'theorem_credit':False,'endpoint_credit':False}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest(); print('GOAL4AJ_DEN_G9_SPLIT_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')),flush=True); print('GOAL4AJ_DEN_G9_SPLIT=PASS',flush=True)
