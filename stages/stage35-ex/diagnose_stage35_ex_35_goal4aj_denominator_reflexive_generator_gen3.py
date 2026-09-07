#!/usr/bin/env python3
"""Goal4AJ diagnostic: degree-19 denominator residual generator, one-shot generation3.

Generation2 completed all six equal-multiplicity group powers but timed out while
reflexively merging those six divisorial ideals.  The passing one-shot reflexive
hull preflight (canonical SHA da58a9c6...) verifies on actual Stoll prime powers
that an iterated reflexive product agrees exactly with ordinary ideal product
followed by one saturation at the A1 singular locus.  Generation3 therefore:
(1) forms each reduced equal-multiplicity prime group with one final hull,
(2) raises each group by short reflexive addition chains, and
(3) combines the six finished group powers by one ordinary product + one hull.
Diagnostic only: no literal denominator/F_B/E1 credit until Q-normalization,
peeled-factor reattachment, and exact divisor verification are separately fixed.
"""
from __future__ import annotations
import hashlib,json,subprocess,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ACTIVE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py'
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
DEN_RIGIDITY_SHA='e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc'
NUM_RIGIDITY_SHA='c85baccb7de0e3e3e88d0b2a1c9c47c10da383a8a6f9d34a29f307a37243afd7'
REFLEXIVE_PREFLIGHT_SHA='1d1395746942bd7d5748e408192761ebf6dce92eeb2760fd34fe9295d674db3b'
ONESHOT_PREFLIGHT_SHA='da58a9c6b72a71d71c9af6f87fa987d2589b0fb3568918bc6994c3960de28a80'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'
QPEEL_SHA='c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba'
A1_SHA='b98f761bf26edfc9af060934a9921722b85b9a867b0716360ab38950d53d4a66'
PEELED_Q_FACTOR='c*b1^11'

IDEALS={
37:'b2,ii*a3+1*a1,a2+1*c',39:'b2,ii*a3-1*a1,a2+1*c',
26:'c,ii*a1-1*b1,ii*a2+1*b2,ii*a3+1*b3',31:'c,ii*a1+1*b1,ii*a2-1*b2,ii*a3-1*b3',
58:'a2-1*a3,ss*a2+1*b1,b2-1*b3',60:'a2-1*a3,ss*a2-1*b1,b2-1*b3',
25:'c,ii*a1+1*b1,ii*a2+1*b2,ii*a3+1*b3',32:'c,ii*a1-1*b1,ii*a2-1*b2,ii*a3-1*b3',
1:'a1,a2+1*b3,a3+1*b2,b1+1*c',8:'a1,a2-1*b3,a3-1*b2,b1-1*c',
9:'a2,a3+1*b1,a1+1*b3,b2+1*c',17:'a3,a1+1*b2,a2+1*b1,b3+1*c',
11:'a2,a3+1*b1,a1-1*b3,b2+1*c',21:'a3,a1-1*b2,a2+1*b1,b3+1*c',
33:'b1,ii*a2+1*a3,a1+1*c',35:'b1,ii*a2-1*a3,a1+1*c',
16:'a2,a3-1*b1,a1-1*b3,b2-1*c',24:'a3,a1-1*b2,a2-1*b1,b3-1*c',
28:'c,ii*a1-1*b1,ii*a2-1*b2,ii*a3+1*b3',29:'c,ii*a1+1*b1,ii*a2+1*b2,ii*a3-1*b3',
65:'a3-1*a1,ss*a3+1*b2,b3+1*b1',67:'a3-1*a1,ss*a3-1*b2,b3+1*b1'}
GROUPS={13:[37,39],9:[26,31,58,60],7:[25,32],3:[1,8,9,17],2:[11,21,33,35],1:[16,24,28,29,65,67]}
expected={i:m for m,idxs in GROUPS.items() for i in idxs}
assert len(expected)==22 and sum(expected.values())==102
ap=subprocess.run(['python','-B',str(ACTIVE)],text=True,capture_output=True,timeout=60)
assert ap.returncode==0
line=next(x for x in ap.stdout.splitlines() if x.startswith('GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON='))
active=json.loads(line.split('=',1)[1]); assert active['canonical_sha256']==ACTIVE_SHA
observed={int(k):int(v) for k,v in active['denominator_residual']['strict_multiplicities_1based'].items()}
assert observed==expected and active['denominator_residual']['homogeneous_degree_after_q_peel']==19

common=r'''
option(redSB);
LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
number ss=u-u^3;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
matrix Jac=jacob(surf); ideal Sing=minor(Jac,4);
proc contained(ideal A,ideal B){ ideal G=std(B); int j; for(j=1;j<=size(A);j++){if(reduce(A[j],G)!=0){return(0);}} return(1); }
proc equalideal(ideal A,ideal B){return(contained(A,B)==1 && contained(B,A)==1);}
proc reflexiveProduct(ideal A,ideal B){ideal Candidate=surf+A*B; list LL=sat(Candidate,Sing); return(std(LL[1]));}
ideal P; ideal Raw; ideal G; ideal T; ideal X2; ideal X3; ideal X4; ideal X6; ideal X8; ideal X12; list L;
'''
parts=[common]
def emit_group(m,idxs):
    first=True
    for idx in idxs:
        parts.append(f'P={IDEALS[idx]}; if(dim(std(surf+P))!=2){{ERROR("strict curve {idx} height mismatch");}}\n')
        if first:
            parts.append('Raw=surf+P;\n'); first=False
        else:
            parts.append('Raw=surf+Raw*P;\n')
    parts.append('L=sat(Raw,Sing); G=std(L[1]);\n')
    parts.append(f'print("GOAL4AJ_DEN_GEN3_GROUP_BASE_DONE={m}:"+string(size(G)));\n')
    if m==1: parts.append(f'ideal D{m}=G;\n')
    elif m==2: parts.append('X2=reflexiveProduct(G,G); ideal D2=X2;\n')
    elif m==3: parts.append('X2=reflexiveProduct(G,G); X3=reflexiveProduct(X2,G); ideal D3=X3;\n')
    elif m==7: parts.append('X2=reflexiveProduct(G,G); X3=reflexiveProduct(X2,G); X6=reflexiveProduct(X3,X3); T=reflexiveProduct(X6,G); ideal D7=T;\n')
    elif m==9: parts.append('X2=reflexiveProduct(G,G); X4=reflexiveProduct(X2,X2); X8=reflexiveProduct(X4,X4); T=reflexiveProduct(X8,G); ideal D9=T;\n')
    elif m==13: parts.append('X2=reflexiveProduct(G,G); X3=reflexiveProduct(X2,G); X6=reflexiveProduct(X3,X3); X12=reflexiveProduct(X6,X6); T=reflexiveProduct(X12,G); ideal D13=T;\n')
    parts.append(f'print("GOAL4AJ_DEN_GEN3_GROUP_POWER_DONE={m}:"+string(size(D{m})));\n')
for m in [13,9,7,3,2,1]: emit_group(m,GROUPS[m])
parts.append(r'''
Raw=surf+D13*D9*D7*D3*D2*D1;
L=sat(Raw,Sing); ideal D=std(L[1]);
print("GOAL4AJ_DEN_GEN3_ONESHOT_COMBINE_DONE="+string(size(D)));
L=sat(D,Sing); ideal Dstable=std(L[1]); if(equalideal(D,Dstable)!=1){ERROR("gen3 full ideal not saturation-stable");}
ideal SurfStd=std(surf); int j; int nonSurf=0; int minDeg=999; int d19=0; poly q; poly candidate=0; int dq;
for(j=1;j<=size(D);j++){
 q=reduce(D[j],SurfStd);
 if(q!=0){nonSurf++; dq=deg(q); if(dq<minDeg){minDeg=dq;} if(dq==19){d19++; if(candidate==0){candidate=q;}}}
}
print("GOAL4AJ_DEN_GEN3_FINAL_GENERATORS="+string(size(D)));
print("GOAL4AJ_DEN_GEN3_NONSURF_GENERATORS="+string(nonSurf));
print("GOAL4AJ_DEN_GEN3_MIN_DEG="+string(minDeg));
print("GOAL4AJ_DEN_GEN3_DEG19_COUNT="+string(d19));
if(minDeg!=19){ERROR("minimum nonsurface generator degree is not 19");}
if(d19<1){ERROR("no degree19 candidate");}
print("GOAL4AJ_DEN_GEN3_CANDIDATE_BEGIN"); print(string(candidate)); print("GOAL4AJ_DEN_GEN3_CANDIDATE_END");
print("GOAL4AJ_DEN_GEN3_BUILD=PASS"); quit;
''')
script=''.join(parts)
with tempfile.TemporaryDirectory() as td:
 p=Path(td)/'goal4aj-den-gen3.sing'; p.write_text(script,encoding='utf-8')
 try:
  cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=1320); timed_out=False
 except subprocess.TimeoutExpired as exc:
  stdout=exc.stdout or ''; stdout=stdout.decode('utf-8',errors='replace') if isinstance(stdout,bytes) else stdout
  marks=[x for x in stdout.splitlines() if x.startswith('GOAL4AJ_DEN_GEN3_')]
  print('GOAL4AJ_DEN_GEN3_TIMEOUT_MARKERS='+json.dumps(marks[-40:])); raise SystemExit('Goal4AJ denominator gen3 timed out; no mathematical obstruction credit')
stdout=cp.stdout; stderr=cp.stderr; lines=stdout.splitlines()
error_text=any(s in stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign'))
try:
 i0=lines.index('GOAL4AJ_DEN_GEN3_CANDIDATE_BEGIN'); i1=lines.index('GOAL4AJ_DEN_GEN3_CANDIDATE_END'); candidate='\n'.join(lines[i0+1:i1]).strip()
except ValueError: candidate=''
completion='GOAL4AJ_DEN_GEN3_BUILD=PASS' in lines
def val(prefix): return int(next(x for x in lines if x.startswith(prefix)).split('=',1)[1])
out={
 'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_RESIDUAL_ONESHOT_REFLEXIVE_GENERATOR_DIAGNOSTIC_V3',
 'source_locks':{'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,'q_hyperplane_factor_peel_canonical_sha256':QPEEL_SHA,'a1_residual_jet_canonical_sha256':A1_SHA,'denominator_rigidity_canonical_sha256':DEN_RIGIDITY_SHA,'numerator_rigidity_canonical_sha256':NUM_RIGIDITY_SHA,'reflexive_product_preflight_canonical_sha256':REFLEXIVE_PREFLIGHT_SHA,'oneshot_reflexive_hull_preflight_canonical_sha256':ONESHOT_PREFLIGHT_SHA},
 'constructor':'one-shot reduced-group bases + reflexive addition chains + one-shot six-group final hull',
 'strict_prime_count':22,'strict_total_multiplicity':102,'multiplicity_groups':{str(m):GROUPS[m] for m in sorted(GROUPS,reverse=True)},
 'singular_returncode':cp.returncode,'singular_error_text_present':error_text,'singular_timed_out':timed_out,
 'completed_group_base_count':sum(x.startswith('GOAL4AJ_DEN_GEN3_GROUP_BASE_DONE=') for x in lines),
 'completed_group_power_count':sum(x.startswith('GOAL4AJ_DEN_GEN3_GROUP_POWER_DONE=') for x in lines),
 'oneshot_final_combine_completed':any(x.startswith('GOAL4AJ_DEN_GEN3_ONESHOT_COMBINE_DONE=') for x in lines),
 'final_standard_basis_generator_count':val('GOAL4AJ_DEN_GEN3_FINAL_GENERATORS=') if completion else None,
 'nonsurface_standard_basis_generator_count':val('GOAL4AJ_DEN_GEN3_NONSURF_GENERATORS=') if completion else None,
 'minimum_nonsurface_generator_degree':val('GOAL4AJ_DEN_GEN3_MIN_DEG=') if completion else None,
 'degree19_candidate_count':val('GOAL4AJ_DEN_GEN3_DEG19_COUNT=') if completion else None,
 'candidate_materialized_over_split_field':bool(candidate),'candidate_text_sha256':hashlib.sha256(candidate.encode()).hexdigest() if candidate else None,'candidate_text_bytes':len(candidate.encode()),'candidate_contains_extension_symbol_u':('u' in candidate),'candidate_text':candidate if candidate and len(candidate.encode())<=60000 else None,'candidate_text_persisted_inline':bool(candidate) and len(candidate.encode())<=60000,
 'peeled_degree12_q_factor':PEELED_Q_FACTOR,'q_coefficient_normalization_completed':False,'peeled_degree12_q_factor_reattached':False,
 'literal_degree31_denominator_materialized':False,'literal_numerator_coefficients_materialized':False,'literal_F_B_materialized':False,'local_evaluations_computed':False,'brauer_manin_obstruction_obtained':False,'E1_proved':False,'stage35_closed':False,'theorem_credit':False,'endpoint_credit':False}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_DEN_GEN3_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
if cp.returncode!=0 or error_text or not completion or not candidate:
 if stderr: print('GOAL4AJ_DEN_GEN3_STDERR='+json.dumps(stderr[-12000:])); raise SystemExit('Goal4AJ denominator gen3 failed closed')
print('GOAL4AJ_DEN_GEN3=PASS')
