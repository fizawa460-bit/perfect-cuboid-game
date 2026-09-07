#!/usr/bin/env python3
"""Goal4AJ diagnostic: denominator degree-19 candidate by process-sharded reflexive products, generation6.

Generation2 proved every equal-multiplicity group power computable but accumulated
resource pressure while keeping all Singular intermediates alive.  This driver
reuses that exact reflexive-product constructor while running each of the six
group powers and each binary merge in a fresh Singular process.  Standard-basis
generators are transferred as exact polynomial strings between processes.  Thus
no Singular process retains earlier Groebner state. Diagnostic only: no literal
Q-normalized degree31 denominator/F_B/E1 credit.
"""
from __future__ import annotations
import ast,hashlib,json,subprocess,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ACTIVE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py'
PARENT=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_reflexive_generator.py'
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
PARENT_BLOB='7dbf3179ca800b16109de3f423fc919541237dd7'
DEN_RIGIDITY_SHA='e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc'
REFLEXIVE_PREFLIGHT_SHA='1d1395746942bd7d5748e408192761ebf6dce92eeb2760fd34fe9295d674db3b'
ONESHOT_PREFLIGHT_SHA='da58a9c6b72a71d71c9af6f87fa987d2589b0fb3568918bc6994c3960de28a80'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'
PEELED_FACTOR_SHA='8818b4e1f29359b6a5579ded427ba65ae1686d09c71b8772bf2b9934a41688a5'

def git_blob(path:Path)->str:
 b=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert git_blob(PARENT)==PARENT_BLOB
tree=ast.parse(PARENT.read_text(encoding='utf-8')); vals={}
for node in tree.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in {'IDEALS','GROUPS'}:
  vals[node.targets[0].id]=ast.literal_eval(node.value)
IDEALS=vals['IDEALS']; GROUPS=vals['GROUPS']
expected={int(i):int(m) for m,ids in GROUPS.items() for i in ids}; assert len(expected)==22 and sum(expected.values())==102
ap=subprocess.run(['python','-B',str(ACTIVE)],text=True,capture_output=True,timeout=60); assert ap.returncode==0
line=next(x for x in ap.stdout.splitlines() if x.startswith('GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON=')); active=json.loads(line.split('=',1)[1]); assert active['canonical_sha256']==ACTIVE_SHA
observed={int(k):int(v) for k,v in active['denominator_residual']['strict_multiplicities_1based'].items()}; assert observed==expected and active['denominator_residual']['homogeneous_degree_after_q_peel']==19

COMMON=r'''
option(redSB); LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp; minpoly=u^4+1; number ii=u^2; number ss=u-u^3;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
matrix Jac=jacob(surf); ideal Sing=minor(Jac,4);
proc contained(ideal A,ideal B){ideal G=std(B); int j; for(j=1;j<=size(A);j++){if(reduce(A[j],G)!=0){return(0);}} return(1);}
proc equalideal(ideal A,ideal B){return(contained(A,B)==1 && contained(B,A)==1);}
proc rprod(ideal A,ideal B){ideal C=surf+A*B; list LL=sat(C,Sing); return(std(LL[1]));}
'''

def run_singular(tag:str, body:str, timeout:int=600)->list[str]:
 script=COMMON+body+'\nquit;\n'
 with tempfile.TemporaryDirectory() as td:
  p=Path(td)/f'{tag}.sing'; p.write_text(script,encoding='utf-8')
  cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=timeout)
 if cp.returncode!=0 or any(s in cp.stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign')):
  print(f'GOAL4AJ_DEN_MP_FAIL_TAG={tag}',flush=True)
  print('GOAL4AJ_DEN_MP_STDOUT_TAIL='+json.dumps(cp.stdout[-12000:]),flush=True)
  if cp.stderr: print('GOAL4AJ_DEN_MP_STDERR='+json.dumps(cp.stderr[-12000:]),flush=True)
  raise SystemExit(f'Goal4AJ denominator multiprocess stage {tag} failed closed')
 gens=[x.split('=',1)[1] for x in cp.stdout.splitlines() if x.startswith('GOAL4AJ_MP_GEN=')]
 if not gens: raise SystemExit(f'Goal4AJ denominator multiprocess stage {tag} returned no generators')
 payload='\n'.join(gens).encode(); sha=hashlib.sha256(payload).hexdigest()
 print(f'GOAL4AJ_DEN_MP_STAGE={tag}:gens={len(gens)}:bytes={len(payload)}:sha256={sha}',flush=True)
 return gens

def ideal_decl(name:str, gens:list[str])->str:
 return f'ideal {name}='+','.join(gens)+';\n'

def group_body(m:int, ids:list[int])->str:
 b=['ideal P; ideal G; ideal X2; ideal X3; ideal X4; ideal X6; ideal X8; ideal X12; ideal T;\n']
 for pos,idx in enumerate(ids):
  b.append(f'P={IDEALS[idx]}; if(dim(std(surf+P))!=2){{ERROR("strict curve {idx} height mismatch");}}\n')
  if pos==0: b.append('G=std(surf+P);\n')
  else: b.append('G=rprod(G,std(surf+P));\n')
 if m==1: b.append('ideal D=G;\n')
 elif m==2: b.append('X2=rprod(G,G); ideal D=X2;\n')
 elif m==3: b.append('X2=rprod(G,G); X3=rprod(X2,G); ideal D=X3;\n')
 elif m==7: b.append('X2=rprod(G,G); X3=rprod(X2,G); X6=rprod(X3,X3); T=rprod(X6,G); ideal D=T;\n')
 elif m==9: b.append('X2=rprod(G,G); X4=rprod(X2,X2); X8=rprod(X4,X4); T=rprod(X8,G); ideal D=T;\n')
 elif m==13: b.append('X2=rprod(G,G); X3=rprod(X2,G); X6=rprod(X3,X3); X12=rprod(X6,X6); T=rprod(X12,G); ideal D=T;\n')
 else: raise AssertionError(m)
 b.append('int j; for(j=1;j<=size(D);j++){print("GOAL4AJ_MP_GEN="+string(D[j]));}\n')
 return ''.join(b)

def merge(tag:str,A:list[str],B:list[str])->list[str]:
 body=ideal_decl('A',A)+ideal_decl('B',B)+'ideal D=rprod(A,B); int j; for(j=1;j<=size(D);j++){print("GOAL4AJ_MP_GEN="+string(D[j]));}\n'
 return run_singular(tag,body,600)

basis={}
for m in [13,9,7,3,2,1]: basis[m]=run_singular(f'group{m}',group_body(m,GROUPS[m]),600)
A=merge('merge13_9',basis[13],basis[9]); B=merge('merge7_3',basis[7],basis[3]); C=merge('merge2_1',basis[2],basis[1]); AB=merge('mergeA_B',A,B); D=merge('mergeAB_C',AB,C)

inspect=ideal_decl('D',D)+r'''
list SL=sat(D,Sing); ideal DS=std(SL[1]); if(equalideal(D,DS)!=1){ERROR("final denominator ideal not saturation-stable");}
ideal SurfStd=std(surf); int j; int nonSurf=0; int minDeg=999; int d19=0; poly q; poly candidate=0; int dq;
for(j=1;j<=size(D);j++){q=reduce(D[j],SurfStd); if(q!=0){nonSurf++; dq=deg(q); if(dq<minDeg){minDeg=dq;} if(dq==19){d19++; if(candidate==0){candidate=q;}}}}
print("GOAL4AJ_DEN_MP_FINAL_GENERATORS="+string(size(D))); print("GOAL4AJ_DEN_MP_NONSURF="+string(nonSurf)); print("GOAL4AJ_DEN_MP_MIN_DEG="+string(minDeg)); print("GOAL4AJ_DEN_MP_DEG19_COUNT="+string(d19));
if(minDeg!=19){ERROR("minimum nonsurface generator degree is not 19");} if(d19<1){ERROR("no degree19 candidate");}
print("GOAL4AJ_DEN_MP_CANDIDATE="+string(candidate));
'''
script=COMMON+inspect+'\nquit;\n'
with tempfile.TemporaryDirectory() as td:
 p=Path(td)/'inspect.sing'; p.write_text(script,encoding='utf-8'); cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=600)
lines=cp.stdout.splitlines(); error_text=any(s in cp.stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign'))
if cp.returncode!=0 or error_text:
 print('GOAL4AJ_DEN_MP_INSPECT_STDOUT='+json.dumps(cp.stdout[-12000:]),flush=True); raise SystemExit('Goal4AJ denominator multiprocess final inspection failed closed')
def val(prefix): return int(next(x for x in lines if x.startswith(prefix)).split('=',1)[1])
candidate=next(x for x in lines if x.startswith('GOAL4AJ_DEN_MP_CANDIDATE=')).split('=',1)[1]
stage_shas={}
for m,v in basis.items(): stage_shas[f'group{m}']=hashlib.sha256('\n'.join(v).encode()).hexdigest()
for k,v in [('merge13_9',A),('merge7_3',B),('merge2_1',C),('mergeA_B',AB),('mergeAB_C',D)]: stage_shas[k]=hashlib.sha256('\n'.join(v).encode()).hexdigest()
out={'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_MULTIPROCESS_REFLEXIVE_GENERATOR_DIAGNOSTIC_V6','source_locks':{'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,'parent_generation2_blob_sha1':PARENT_BLOB,'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,'denominator_rigidity_canonical_sha256':DEN_RIGIDITY_SHA,'reflexive_product_preflight_canonical_sha256':REFLEXIVE_PREFLIGHT_SHA,'oneshot_reflexive_hull_preflight_canonical_sha256':ONESHOT_PREFLIGHT_SHA,'peeled_q_factor_canonical_sha256':PEELED_FACTOR_SHA},'constructor':'fresh Singular process per equal-multiplicity group power and per binary reflexive merge','strict_prime_count':22,'strict_total_multiplicity':102,'stage_basis_sha256':stage_shas,'final_standard_basis_generator_count':val('GOAL4AJ_DEN_MP_FINAL_GENERATORS='),'nonsurface_standard_basis_generator_count':val('GOAL4AJ_DEN_MP_NONSURF='),'minimum_nonsurface_generator_degree':val('GOAL4AJ_DEN_MP_MIN_DEG='),'degree19_candidate_count':val('GOAL4AJ_DEN_MP_DEG19_COUNT='),'candidate_materialized_over_split_field':bool(candidate),'candidate_text_sha256':hashlib.sha256(candidate.encode()).hexdigest(),'candidate_text_bytes':len(candidate.encode()),'candidate_contains_extension_symbol_u':('u' in candidate),'candidate_text':candidate if len(candidate.encode())<=60000 else None,'peeled_degree12_q_factor':'c*b1^11','q_coefficient_normalization_completed':False,'peeled_degree12_q_factor_reattached':False,'literal_degree31_denominator_materialized':False,'literal_F_B_materialized':False,'E1_proved':False,'stage35_closed':False,'theorem_credit':False,'endpoint_credit':False}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest(); print('GOAL4AJ_DEN_MP_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')),flush=True); print('GOAL4AJ_DEN_MP=PASS',flush=True)
