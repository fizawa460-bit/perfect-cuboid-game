#!/usr/bin/env python3
"""Goal4AJ diagnostic: numerator degree-31 candidate via native Singular qring products, generation4.

All strict-prime products and multiplicity powers are formed natively in the
canonical surface quotient ring. The full quotient ideal is lifted once to the
ambient ring and receives one final saturation at the isolated A1 singular locus.
Diagnostic only: no Q-normalized numerator/F_B/E1 credit.
"""
from __future__ import annotations
import ast,hashlib,json,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ACTIVE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py'
PARENT=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_reflexive_generator_gen2.py'
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
PARENT_BLOB='a6c4a4f6e1db1817149c09d02d440d612e4549b2'
NUM_RIGIDITY_SHA='c85baccb7de0e3e3e88d0b2a1c9c47c10da383a8a6f9d34a29f307a37243afd7'
QRING_PREFLIGHT_SHA='b45e715565a7cd4f8b2f683fac695216be0f565a906aed326f9d139b3eefdb6b'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'

def git_blob(path:Path)->str:
 b=path.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert git_blob(PARENT)==PARENT_BLOB
tree=ast.parse(PARENT.read_text(encoding='utf-8')); vals={}
for node in tree.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in {'IDEALS','GROUPS'}:
  vals[node.targets[0].id]=ast.literal_eval(node.value)
IDEALS=vals['IDEALS']; GROUPS=vals['GROUPS']
expected={int(i):int(m) for m,ids in GROUPS.items() for i in ids}; assert len(expected)==27 and sum(expected.values())==202
ap=subprocess.run(['python','-B',str(ACTIVE)],text=True,capture_output=True,timeout=60); assert ap.returncode==0
line=next(x for x in ap.stdout.splitlines() if x.startswith('GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON=')); active=json.loads(line.split('=',1)[1]); assert active['canonical_sha256']==ACTIVE_SHA
observed={int(k):int(v) for k,v in active['numerator']['strict_multiplicities_1based'].items()}; assert observed==expected and active['numerator']['homogeneous_degree_after_q_peel']==31
parts=[r'''
option(redSB); LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp; minpoly=u^4+1; number ii=u^2; number ss=u-u^3;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
matrix Jac=jacob(surf); ideal Sing=minor(Jac,4);
qring qr=std(surf); number ii=u^2; number ss=u-u^3;
proc qprod(ideal A,ideal B){return(std(A*B));}
ideal P; ideal G; ideal X2; ideal X3; ideal X4; ideal X5; ideal X6; ideal X8; ideal X10; ideal X12; ideal X16; ideal X20; ideal T;
''']
def emit(m,ids):
 first=True
 for idx in ids:
  parts.append(f'P={IDEALS[idx]}; if(dim(std(P))!=2){{ERROR("strict curve {idx} height mismatch in qring");}}\n')
  if first: parts.append('G=std(P);\n'); first=False
  else: parts.append('G=qprod(G,P);\n')
 parts.append(f'print("GOAL4AJ_NUM_QRING_GROUP_BASE_DONE={m}:"+string(size(G)));\n')
 if m==1: parts.append('ideal D1=G;\n')
 elif m==3: parts.append('X2=qprod(G,G); X3=qprod(X2,G); ideal D3=X3;\n')
 elif m==4: parts.append('X2=qprod(G,G); X4=qprod(X2,X2); ideal D4=X4;\n')
 elif m==9: parts.append('X2=qprod(G,G); X4=qprod(X2,X2); X8=qprod(X4,X4); T=qprod(X8,G); ideal D9=T;\n')
 elif m==10: parts.append('X2=qprod(G,G); X4=qprod(X2,X2); X8=qprod(X4,X4); X10=qprod(X8,X2); ideal D10=X10;\n')
 elif m==12: parts.append('X2=qprod(G,G); X3=qprod(X2,G); X6=qprod(X3,X3); X12=qprod(X6,X6); ideal D12=X12;\n')
 elif m==13: parts.append('X2=qprod(G,G); X3=qprod(X2,G); X6=qprod(X3,X3); X12=qprod(X6,X6); T=qprod(X12,G); ideal D13=T;\n')
 elif m==18: parts.append('X2=qprod(G,G); X4=qprod(X2,X2); X8=qprod(X4,X4); X16=qprod(X8,X8); T=qprod(X16,X2); ideal D18=T;\n')
 elif m==21: parts.append('X2=qprod(G,G); X4=qprod(X2,X2); X5=qprod(X4,G); X10=qprod(X5,X5); X20=qprod(X10,X10); T=qprod(X20,G); ideal D21=T;\n')
 parts.append(f'print("GOAL4AJ_NUM_QRING_GROUP_POWER_DONE={m}:"+string(size(D{m})));\n')
for m in [21,18,13,12,10,9,4,3,1]: emit(m,GROUPS[m])
parts.append(r'''
ideal A=qprod(D21,D18); ideal B=qprod(D13,D12); ideal C=qprod(D10,D9); ideal E=qprod(D4,D3); ideal AB=qprod(A,B); ideal CE=qprod(C,E); ideal ACE=qprod(AB,CE); ideal QRAW=qprod(ACE,D1);
print("GOAL4AJ_NUM_QRING_RAW_GENERATORS="+string(size(QRAW)));
setring r;
ideal L=imap(qr,QRAW); ideal RAW=std(surf+L); list FL=sat(RAW,Sing); ideal D=std(FL[1]);
print("GOAL4AJ_NUM_QRING_FINAL_HULL_DONE="+string(size(D)));
proc contained(ideal A,ideal B){ideal G=std(B); int j; for(j=1;j<=size(A);j++){if(reduce(A[j],G)!=0){return(0);}} return(1);}
proc equalideal(ideal A,ideal B){return(contained(A,B)==1 && contained(B,A)==1);}
list SL=sat(D,Sing); ideal DS=std(SL[1]); if(equalideal(D,DS)!=1){ERROR("final hull not saturation-stable");}
ideal SurfStd=std(surf); int j; int nonSurf=0; int minDeg=999; int d31=0; poly q; poly candidate=0; int dq;
for(j=1;j<=size(D);j++){q=reduce(D[j],SurfStd); if(q!=0){nonSurf++; dq=deg(q); if(dq<minDeg){minDeg=dq;} if(dq==31){d31++; if(candidate==0){candidate=q;}}}}
print("GOAL4AJ_NUM_QRING_FINAL_GENERATORS="+string(size(D))); print("GOAL4AJ_NUM_QRING_NONSURF_GENERATORS="+string(nonSurf)); print("GOAL4AJ_NUM_QRING_MIN_DEG="+string(minDeg)); print("GOAL4AJ_NUM_QRING_DEG31_COUNT="+string(d31));
if(minDeg!=31){ERROR("minimum nonsurface generator degree is not 31");} if(d31<1){ERROR("no degree31 candidate");}
print("GOAL4AJ_NUM_QRING_CANDIDATE_BEGIN"); print(string(candidate)); print("GOAL4AJ_NUM_QRING_CANDIDATE_END"); print("GOAL4AJ_NUM_QRING_BUILD=PASS"); quit;
''')
script=''.join(parts)
with tempfile.TemporaryDirectory() as td:
 p=Path(td)/'goal4aj-num-qring-gen4.sing'; p.write_text(script,encoding='utf-8')
 try: cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=1500); timed_out=False
 except subprocess.TimeoutExpired as exc:
  stdout=exc.stdout or ''; stdout=stdout.decode('utf-8',errors='replace') if isinstance(stdout,bytes) else stdout; marks=[x for x in stdout.splitlines() if x.startswith('GOAL4AJ_NUM_QRING_')]; print('GOAL4AJ_NUM_QRING_TIMEOUT_MARKERS='+json.dumps(marks[-80:])); raise SystemExit('Goal4AJ numerator qring gen4 timed out; no mathematical obstruction credit')
stdout=cp.stdout; stderr=cp.stderr; lines=stdout.splitlines(); error_text=any(s in stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign'))
try: i0=lines.index('GOAL4AJ_NUM_QRING_CANDIDATE_BEGIN'); i1=lines.index('GOAL4AJ_NUM_QRING_CANDIDATE_END'); candidate='\n'.join(lines[i0+1:i1]).strip()
except ValueError: candidate=''
completion='GOAL4AJ_NUM_QRING_BUILD=PASS' in lines
def val(p): return int(next(x for x in lines if x.startswith(p)).split('=',1)[1])
out={'schema':'STAGE35_EX_GOAL4AJ_NUMERATOR_QRING_GENERATOR_DIAGNOSTIC_V4','source_locks':{'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,'parent_generator_blob_sha1':PARENT_BLOB,'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,'numerator_rigidity_canonical_sha256':NUM_RIGIDITY_SHA,'qring_product_preflight_canonical_sha256':QRING_PREFLIGHT_SHA},'constructor':'native Singular qring products; one ambient lift and one final A1 saturation','strict_prime_count':27,'strict_total_multiplicity':202,'multiplicity_groups':{str(m):GROUPS[m] for m in sorted(GROUPS,reverse=True)},'singular_returncode':cp.returncode,'singular_error_text_present':error_text,'singular_timed_out':timed_out,'completed_group_base_count':sum(x.startswith('GOAL4AJ_NUM_QRING_GROUP_BASE_DONE=') for x in lines),'completed_group_power_count':sum(x.startswith('GOAL4AJ_NUM_QRING_GROUP_POWER_DONE=') for x in lines),'final_hull_completed':any(x.startswith('GOAL4AJ_NUM_QRING_FINAL_HULL_DONE=') for x in lines),'final_standard_basis_generator_count':val('GOAL4AJ_NUM_QRING_FINAL_GENERATORS=') if completion else None,'nonsurface_standard_basis_generator_count':val('GOAL4AJ_NUM_QRING_NONSURF_GENERATORS=') if completion else None,'minimum_nonsurface_generator_degree':val('GOAL4AJ_NUM_QRING_MIN_DEG=') if completion else None,'degree31_candidate_count':val('GOAL4AJ_NUM_QRING_DEG31_COUNT=') if completion else None,'candidate_materialized_over_split_field':bool(candidate),'candidate_text_sha256':hashlib.sha256(candidate.encode()).hexdigest() if candidate else None,'candidate_text_bytes':len(candidate.encode()),'candidate_contains_extension_symbol_u':('u' in candidate),'candidate_text':candidate if candidate and len(candidate.encode())<=60000 else None,'candidate_text_persisted_inline':bool(candidate) and len(candidate.encode())<=60000,'q_coefficient_normalization_completed':False,'literal_numerator_coefficients_materialized':False,'literal_F_B_materialized':False,'E1_proved':False,'stage35_closed':False,'theorem_credit':False,'endpoint_credit':False}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest(); print('GOAL4AJ_NUM_QRING_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
if cp.returncode!=0 or error_text or not completion or not candidate:
 if stdout: print('GOAL4AJ_NUM_QRING_STDOUT_TAIL='+json.dumps(stdout[-12000:]));
 if stderr: print('GOAL4AJ_NUM_QRING_STDERR='+json.dumps(stderr[-12000:]));
 raise SystemExit('Goal4AJ numerator qring gen4 failed closed')
print('GOAL4AJ_NUM_QRING=PASS')
