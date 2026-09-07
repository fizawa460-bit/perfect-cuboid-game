#!/usr/bin/env python3
"""Goal4AJ diagnostic: denominator degree-19 residual via quotient products, generation4.

Computational refinement of the passing one-shot reflexive-hull route.  Every
ordinary product is reduced exactly modulo the four canonical surface quadrics
with std(surface+A*B), while saturation at the A1 singular locus is deferred to
one final hull.  A small actual Stoll prime cube is first compared with the older
iterated reflexive power.  Diagnostic only: no degree31 denominator/F_B/E1 credit.
"""
from __future__ import annotations
import ast,hashlib,json,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ACTIVE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py'
PARENT=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_reflexive_generator_gen3.py'
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
PARENT_BLOB='6ffb4f5127a1a300c9e9e9827de4a8b0b2ae7409'
DEN_RIGIDITY_SHA='e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc'
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
parts=[r'''
option(redSB); LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp; minpoly=u^4+1; number ii=u^2; number ss=u-u^3;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
matrix Jac=jacob(surf); ideal Sing=minor(Jac,4);
proc contained(ideal A,ideal B){ideal G=std(B); int j; for(j=1;j<=size(A);j++){if(reduce(A[j],G)!=0){return(0);}} return(1);}
proc equalideal(ideal A,ideal B){return(contained(A,B)==1 && contained(B,A)==1);}
proc rprod(ideal A,ideal B){ideal C=surf+A*B; list LL=sat(C,Sing); return(std(LL[1]));}
proc qprod(ideal A,ideal B){return(std(surf+A*B));}
ideal PP=a1,a2+b3,a3+b2,b1+c; ideal R2=rprod(PP,PP); ideal R3=rprod(R2,PP); ideal Q2=qprod(PP,PP); ideal Q3=qprod(Q2,PP); list PL=sat(Q3,Sing); ideal O3=std(PL[1]);
if(equalideal(R3,O3)!=1){ERROR("raw quotient power / final hull preflight mismatch");}
print("GOAL4AJ_DEN_QPROD_POWER_PREFLIGHT=PASS");
ideal P; ideal G; ideal X2; ideal X3; ideal X4; ideal X6; ideal X8; ideal X12; ideal T;
''']
def emit(m,ids):
 first=True
 for idx in ids:
  parts.append(f'P={IDEALS[idx]}; if(dim(std(surf+P))!=2){{ERROR("strict curve {idx} height mismatch");}}\n')
  if first: parts.append('G=std(surf+P);\n'); first=False
  else: parts.append('G=qprod(G,P);\n')
 parts.append(f'print("GOAL4AJ_DEN_QPROD_GROUP_BASE_DONE={m}:"+string(size(G)));\n')
 if m==1: parts.append('ideal D1=G;\n')
 elif m==2: parts.append('X2=qprod(G,G); ideal D2=X2;\n')
 elif m==3: parts.append('X2=qprod(G,G); X3=qprod(X2,G); ideal D3=X3;\n')
 elif m==7: parts.append('X2=qprod(G,G); X3=qprod(X2,G); X6=qprod(X3,X3); T=qprod(X6,G); ideal D7=T;\n')
 elif m==9: parts.append('X2=qprod(G,G); X4=qprod(X2,X2); X8=qprod(X4,X4); T=qprod(X8,G); ideal D9=T;\n')
 elif m==13: parts.append('X2=qprod(G,G); X3=qprod(X2,G); X6=qprod(X3,X3); X12=qprod(X6,X6); T=qprod(X12,G); ideal D13=T;\n')
 parts.append(f'print("GOAL4AJ_DEN_QPROD_GROUP_POWER_DONE={m}:"+string(size(D{m})));\n')
for m in [13,9,7,3,2,1]: emit(m,GROUPS[m])
parts.append(r'''
ideal A=qprod(D13,D9); ideal B=qprod(D7,D3); ideal C=qprod(D2,D1); ideal AB=qprod(A,B); ideal RAW=qprod(AB,C);
print("GOAL4AJ_DEN_QPROD_RAW_FINAL_GENERATORS="+string(size(RAW)));
list FL=sat(RAW,Sing); ideal D=std(FL[1]); print("GOAL4AJ_DEN_QPROD_FINAL_HULL_DONE="+string(size(D)));
list SL=sat(D,Sing); ideal DS=std(SL[1]); if(equalideal(D,DS)!=1){ERROR("final hull not saturation-stable");}
ideal SurfStd=std(surf); int j; int nonSurf=0; int minDeg=999; int d19=0; poly q; poly candidate=0; int dq;
for(j=1;j<=size(D);j++){q=reduce(D[j],SurfStd); if(q!=0){nonSurf++; dq=deg(q); if(dq<minDeg){minDeg=dq;} if(dq==19){d19++; if(candidate==0){candidate=q;}}}}
print("GOAL4AJ_DEN_QPROD_FINAL_GENERATORS="+string(size(D))); print("GOAL4AJ_DEN_QPROD_NONSURF_GENERATORS="+string(nonSurf)); print("GOAL4AJ_DEN_QPROD_MIN_DEG="+string(minDeg)); print("GOAL4AJ_DEN_QPROD_DEG19_COUNT="+string(d19));
if(minDeg!=19){ERROR("minimum nonsurface generator degree is not 19");} if(d19<1){ERROR("no degree19 candidate");}
print("GOAL4AJ_DEN_QPROD_CANDIDATE_BEGIN"); print(string(candidate)); print("GOAL4AJ_DEN_QPROD_CANDIDATE_END"); print("GOAL4AJ_DEN_QPROD_BUILD=PASS"); quit;
''')
script=''.join(parts)
with tempfile.TemporaryDirectory() as td:
 p=Path(td)/'goal4aj-den-qprod-gen4.sing'; p.write_text(script,encoding='utf-8')
 try: cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=1500); timed_out=False
 except subprocess.TimeoutExpired as exc:
  stdout=exc.stdout or ''; stdout=stdout.decode('utf-8',errors='replace') if isinstance(stdout,bytes) else stdout; marks=[x for x in stdout.splitlines() if x.startswith('GOAL4AJ_DEN_QPROD_')]; print('GOAL4AJ_DEN_QPROD_TIMEOUT_MARKERS='+json.dumps(marks[-80:])); raise SystemExit('Goal4AJ denominator quotient-product gen4 timed out; no mathematical obstruction credit')
stdout=cp.stdout; stderr=cp.stderr; lines=stdout.splitlines(); error_text=any(s in stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign'))
try: i0=lines.index('GOAL4AJ_DEN_QPROD_CANDIDATE_BEGIN'); i1=lines.index('GOAL4AJ_DEN_QPROD_CANDIDATE_END'); candidate='\n'.join(lines[i0+1:i1]).strip()
except ValueError: candidate=''
completion='GOAL4AJ_DEN_QPROD_BUILD=PASS' in lines
def val(p): return int(next(x for x in lines if x.startswith(p)).split('=',1)[1])
out={'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_QUOTIENT_PRODUCT_ONE_FINAL_HULL_GENERATOR_DIAGNOSTIC_V4','source_locks':{'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,'parent_generator_blob_sha1':PARENT_BLOB,'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,'denominator_rigidity_canonical_sha256':DEN_RIGIDITY_SHA,'oneshot_reflexive_hull_preflight_canonical_sha256':ONESHOT_PREFLIGHT_SHA,'peeled_q_factor_canonical_sha256':PEELED_FACTOR_SHA},'constructor':'std(surface+A*B) after every quotient product; one singular-locus saturation only at final full residual divisor product','strict_prime_count':22,'strict_total_multiplicity':102,'multiplicity_groups':{str(m):GROUPS[m] for m in sorted(GROUPS,reverse=True)},'raw_power_one_final_hull_preflight_pass':('GOAL4AJ_DEN_QPROD_POWER_PREFLIGHT=PASS' in lines),'singular_returncode':cp.returncode,'singular_error_text_present':error_text,'singular_timed_out':timed_out,'completed_group_base_count':sum(x.startswith('GOAL4AJ_DEN_QPROD_GROUP_BASE_DONE=') for x in lines),'completed_group_power_count':sum(x.startswith('GOAL4AJ_DEN_QPROD_GROUP_POWER_DONE=') for x in lines),'final_hull_completed':any(x.startswith('GOAL4AJ_DEN_QPROD_FINAL_HULL_DONE=') for x in lines),'final_standard_basis_generator_count':val('GOAL4AJ_DEN_QPROD_FINAL_GENERATORS=') if completion else None,'nonsurface_standard_basis_generator_count':val('GOAL4AJ_DEN_QPROD_NONSURF_GENERATORS=') if completion else None,'minimum_nonsurface_generator_degree':val('GOAL4AJ_DEN_QPROD_MIN_DEG=') if completion else None,'degree19_candidate_count':val('GOAL4AJ_DEN_QPROD_DEG19_COUNT=') if completion else None,'candidate_materialized_over_split_field':bool(candidate),'candidate_text_sha256':hashlib.sha256(candidate.encode()).hexdigest() if candidate else None,'candidate_text_bytes':len(candidate.encode()),'candidate_contains_extension_symbol_u':('u' in candidate),'candidate_text':candidate if candidate and len(candidate.encode())<=60000 else None,'candidate_text_persisted_inline':bool(candidate) and len(candidate.encode())<=60000,'peeled_degree12_q_factor':'c*b1^11','q_coefficient_normalization_completed':False,'peeled_degree12_q_factor_reattached':False,'literal_degree31_denominator_materialized':False,'literal_F_B_materialized':False,'E1_proved':False,'stage35_closed':False,'theorem_credit':False,'endpoint_credit':False}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest(); print('GOAL4AJ_DEN_QPROD_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
if cp.returncode!=0 or error_text or not completion or not candidate or not out['raw_power_one_final_hull_preflight_pass']:
 if stderr: print('GOAL4AJ_DEN_QPROD_STDERR='+json.dumps(stderr[-12000:])); raise SystemExit('Goal4AJ denominator quotient-product gen4 failed closed')
print('GOAL4AJ_DEN_QPROD=PASS')
