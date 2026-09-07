#!/usr/bin/env python3
"""Goal4AJ diagnostic: degree-19 denominator residual generator, grouped reflexive-product generation2.

Generation1 built every symbolic power separately and then multiplied 22 divisorial
ideals.  This generation groups strict primes by equal target multiplicity, forms
the reduced divisor of each group once, raises that divisorial ideal by an exact
short addition chain, and combines only the six multiplicity groups.  The passing
reflexive-product preflight certifies the divisor-addition constructor, while the
passing denominator rigidity diagnostic proves that the degree-19 section line is
one-dimensional.  This leaf only materializes one split-field degree-19 candidate;
it does not yet reattach the peeled degree-12 Q factor or grant literal F_B/E1 credit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[2]
ACTIVE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py'
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
DEN_RIGIDITY_SHA='e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc'
NUM_RIGIDITY_SHA='c85baccb7de0e3e3e88d0b2a1c9c47c10da383a8a6f9d34a29f307a37243afd7'
REFLEXIVE_PREFLIGHT_SHA='1d1395746942bd7d5748e408192761ebf6dce92eeb2760fd34fe9295d674db3b'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'
QPEEL_SHA='c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba'
A1_SHA='b98f761bf26edfc9af060934a9921722b85b9a867b0716360ab38950d53d4a66'
GALOIS_SHA='e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30'

IDEALS={
 37:'b2,ii*a3+1*a1,a2+1*c',
 39:'b2,ii*a3-1*a1,a2+1*c',
 26:'c,ii*a1-1*b1,ii*a2+1*b2,ii*a3+1*b3',
 31:'c,ii*a1+1*b1,ii*a2-1*b2,ii*a3-1*b3',
 58:'a2-1*a3,ss*a2+1*b1,b2-1*b3',
 60:'a2-1*a3,ss*a2-1*b1,b2-1*b3',
 25:'c,ii*a1+1*b1,ii*a2+1*b2,ii*a3+1*b3',
 32:'c,ii*a1-1*b1,ii*a2-1*b2,ii*a3-1*b3',
 1:'a1,a2+1*b3,a3+1*b2,b1+1*c',
 8:'a1,a2-1*b3,a3-1*b2,b1-1*c',
 9:'a2,a3+1*b1,a1+1*b3,b2+1*c',
 17:'a3,a1+1*b2,a2+1*b1,b3+1*c',
 11:'a2,a3+1*b1,a1-1*b3,b2+1*c',
 21:'a3,a1-1*b2,a2+1*b1,b3+1*c',
 33:'b1,ii*a2+1*a3,a1+1*c',
 35:'b1,ii*a2-1*a3,a1+1*c',
 16:'a2,a3-1*b1,a1-1*b3,b2-1*c',
 24:'a3,a1-1*b2,a2-1*b1,b3-1*c',
 28:'c,ii*a1-1*b1,ii*a2-1*b2,ii*a3+1*b3',
 29:'c,ii*a1+1*b1,ii*a2+1*b2,ii*a3-1*b3',
 65:'a3-1*a1,ss*a3+1*b2,b3+1*b1',
 67:'a3-1*a1,ss*a3-1*b2,b3+1*b1',
}
GROUPS={
 13:[37,39],
 9:[26,31,58,60],
 7:[25,32],
 3:[1,8,9,17],
 2:[11,21,33,35],
 1:[16,24,28,29,65,67],
}
expected={i:m for m,idxs in GROUPS.items() for i in idxs}
assert len(expected)==22 and sum(expected.values())==102

ap=subprocess.run(['python','-B',str(ACTIVE)],text=True,capture_output=True,timeout=60)
assert ap.returncode==0
line=next(x for x in ap.stdout.splitlines() if x.startswith('GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON='))
active=json.loads(line.split('=',1)[1])
assert active['canonical_sha256']==ACTIVE_SHA
observed={int(k):int(v) for k,v in active['denominator_residual']['strict_multiplicities_1based'].items()}
assert observed==expected
assert active['denominator_residual']['homogeneous_degree_after_q_peel']==19

common=r'''
option(redSB);
LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
number ss=u-u^3;
ideal surf=
 a1^2+a2^2-b3^2,
 a2^2+a3^2-b1^2,
 a1^2+a3^2-b2^2,
 a1^2+a2^2+a3^2-c^2;
matrix Jac=jacob(surf);
ideal Sing=minor(Jac,4);
proc contained(ideal A,ideal B)
{
 ideal G=std(B); int j;
 for(j=1;j<=size(A);j++){ if(reduce(A[j],G)!=0){return(0);} }
 return(1);
}
proc equalideal(ideal A,ideal B)
{
 return(contained(A,B)==1 && contained(B,A)==1);
}
proc reflexiveProduct(ideal A,ideal B)
{
 ideal Candidate=surf+A*B; list L=sat(Candidate,Sing); return(std(L[1]));
}
ideal P; ideal G; ideal T; ideal X2; ideal X3; ideal X4; ideal X6; ideal X8; ideal X12;
'''
parts=[common]

def emit_group(m:int, idxs:list[int]) -> None:
    name=f'D{m}'
    for pos,idx in enumerate(idxs):
        parts.append(f'P={IDEALS[idx]};\n')
        parts.append(f'if(dim(std(surf+P))!=2){{ERROR("strict curve {idx} height mismatch");}}\n')
        if pos==0:
            parts.append('G=std(surf+P);\n')
        else:
            parts.append('G=reflexiveProduct(G,std(surf+P));\n')
        parts.append(f'print("GOAL4AJ_DEN_GROUP_BASE_STEP={m}:{pos+1}:{idx}:"+string(size(G)));\n')
    # Exact short addition chains in the divisor group.
    if m==1:
        parts.append(f'ideal {name}=G;\n')
    elif m==2:
        parts.append('X2=reflexiveProduct(G,G);\n')
        parts.append(f'ideal {name}=X2;\n')
    elif m==3:
        parts.append('X2=reflexiveProduct(G,G); X3=reflexiveProduct(X2,G);\n')
        parts.append(f'ideal {name}=X3;\n')
    elif m==7:
        parts.append('X2=reflexiveProduct(G,G); X3=reflexiveProduct(X2,G); X6=reflexiveProduct(X3,X3); T=reflexiveProduct(X6,G);\n')
        parts.append(f'ideal {name}=T;\n')
    elif m==9:
        parts.append('X2=reflexiveProduct(G,G); X4=reflexiveProduct(X2,X2); X8=reflexiveProduct(X4,X4); T=reflexiveProduct(X8,G);\n')
        parts.append(f'ideal {name}=T;\n')
    elif m==13:
        parts.append('X2=reflexiveProduct(G,G); X3=reflexiveProduct(X2,G); X6=reflexiveProduct(X3,X3); X12=reflexiveProduct(X6,X6); T=reflexiveProduct(X12,G);\n')
        parts.append(f'ideal {name}=T;\n')
    else:
        raise AssertionError(m)
    parts.append(f'print("GOAL4AJ_DEN_GROUP_POWER_DONE={m}:"+string(size({name})));\n')

for m in [13,9,7,3,2,1]:
    emit_group(m,GROUPS[m])

parts.append(r'''
ideal A=reflexiveProduct(D13,D9);
ideal B=reflexiveProduct(D7,D3);
ideal C=reflexiveProduct(D2,D1);
ideal AB=reflexiveProduct(A,B);
ideal D=reflexiveProduct(AB,C);
print("GOAL4AJ_DEN_GROUPED_COMBINE_DONE="+string(size(D)));
list DL=sat(D,Sing); ideal Dstable=std(DL[1]);
if(equalideal(D,Dstable)!=1){ERROR("grouped full denominator divisorial ideal not saturation-stable");}
ideal SurfStd=std(surf);
int j; int nonSurf=0; int minDeg=999; int d19=0; poly q; poly candidate=0; int dq;
for(j=1;j<=size(D);j++)
{
 q=reduce(D[j],SurfStd);
 if(q!=0)
 {
  nonSurf++;
  dq=deg(q);
  if(dq<minDeg){minDeg=dq;}
  if(dq==19)
  {
   d19++;
   if(candidate==0){candidate=q;}
  }
 }
}
print("GOAL4AJ_DEN_GROUPED_FINAL_GENERATORS="+string(size(D)));
print("GOAL4AJ_DEN_GROUPED_NONSURF_GENERATORS="+string(nonSurf));
print("GOAL4AJ_DEN_GROUPED_MIN_DEG="+string(minDeg));
print("GOAL4AJ_DEN_GROUPED_DEG19_COUNT="+string(d19));
if(minDeg!=19){ERROR("minimum nonsurface generator degree is not 19");}
if(d19<1){ERROR("no degree19 reduced standard-basis candidate");}
print("GOAL4AJ_DEN_RESIDUAL_CANDIDATE_BEGIN");
print(string(candidate));
print("GOAL4AJ_DEN_RESIDUAL_CANDIDATE_END");
print("GOAL4AJ_DEN_GROUPED_REFLEXIVE_BUILD=PASS");
quit;
''')
script=''.join(parts)
with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'goal4aj-den-reflexive-grouped.sing'
    p.write_text(script,encoding='utf-8')
    try:
        cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=1200)
        timed_out=False
    except subprocess.TimeoutExpired as exc:
        stdout=exc.stdout or ''
        if isinstance(stdout,bytes): stdout=stdout.decode('utf-8',errors='replace')
        marks=[x for x in stdout.splitlines() if x.startswith('GOAL4AJ_DEN_GROUP_')]
        print('GOAL4AJ_DEN_GROUPED_TIMEOUT_MARKERS='+json.dumps(marks[-40:]))
        raise SystemExit('Goal4AJ grouped denominator reflexive build timed out; no mathematical obstruction credit')
stdout=cp.stdout; stderr=cp.stderr
error_text=any(s in stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign'))
lines=stdout.splitlines()
def val(prefix): return int(next(x for x in lines if x.startswith(prefix)).split('=',1)[1])
try:
    i0=lines.index('GOAL4AJ_DEN_RESIDUAL_CANDIDATE_BEGIN')
    i1=lines.index('GOAL4AJ_DEN_RESIDUAL_CANDIDATE_END')
    candidate='\n'.join(lines[i0+1:i1]).strip()
except ValueError:
    candidate=''
completion='GOAL4AJ_DEN_GROUPED_REFLEXIVE_BUILD=PASS' in lines
group_done=[x for x in lines if x.startswith('GOAL4AJ_DEN_GROUP_POWER_DONE=')]
base_steps=[x for x in lines if x.startswith('GOAL4AJ_DEN_GROUP_BASE_STEP=')]
out={
 'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_RESIDUAL_GROUPED_REFLEXIVE_GENERATOR_DIAGNOSTIC_V2',
 'source_locks':{
   'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,
   'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,
   'q_hyperplane_factor_peel_canonical_sha256':QPEEL_SHA,
   'a1_residual_jet_canonical_sha256':A1_SHA,
   'denominator_rigidity_canonical_sha256':DEN_RIGIDITY_SHA,
   'numerator_rigidity_canonical_sha256':NUM_RIGIDITY_SHA,
   'reflexive_product_preflight_canonical_sha256':REFLEXIVE_PREFLIGHT_SHA,
   'galois_known_class_permutations_canonical_sha256':GALOIS_SHA,
 },
 'constructor':'group equal-multiplicity primes, short addition-chain reflexive powers, balanced six-group product',
 'theoretical_reflexive_saturation_count_upper_bound':37,
 'generation1_reflexive_saturation_count_upper_bound':101,
 'strict_prime_count':22,
 'strict_total_multiplicity':102,
 'multiplicity_groups':{str(m):GROUPS[m] for m in sorted(GROUPS,reverse=True)},
 'singular_returncode':cp.returncode,
 'singular_error_text_present':error_text,
 'singular_timed_out':timed_out,
 'completed_base_prime_count':len(base_steps),
 'completed_multiplicity_group_count':len(group_done),
 'expected_multiplicity_group_count':6,
 'final_standard_basis_generator_count':val('GOAL4AJ_DEN_GROUPED_FINAL_GENERATORS=') if completion else None,
 'nonsurface_standard_basis_generator_count':val('GOAL4AJ_DEN_GROUPED_NONSURF_GENERATORS=') if completion else None,
 'minimum_nonsurface_generator_degree':val('GOAL4AJ_DEN_GROUPED_MIN_DEG=') if completion else None,
 'degree19_candidate_count':val('GOAL4AJ_DEN_GROUPED_DEG19_COUNT=') if completion else None,
 'candidate_materialized_over_split_field':bool(candidate),
 'candidate_text_sha256':hashlib.sha256(candidate.encode()).hexdigest() if candidate else None,
 'candidate_text_bytes':len(candidate.encode()),
 'candidate_contains_extension_symbol_u':('u' in candidate),
 'candidate_text':candidate if candidate and len(candidate.encode())<=60000 else None,
 'candidate_text_persisted_inline':bool(candidate) and len(candidate.encode())<=60000,
 'denominator_residual_degree19_line_rigidity_used':True,
 'q_coefficient_normalization_completed':False,
 'peeled_degree12_q_factor_reattached':False,
 'literal_degree31_denominator_materialized':False,
 'literal_numerator_coefficients_materialized':False,
 'literal_F_B_materialized':False,
 'local_evaluations_computed':False,
 'brauer_manin_obstruction_obtained':False,
 'E1_proved':False,
 'stage35_closed':False,
 'theorem_credit':False,
 'endpoint_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_DEN_GROUPED_REFLEXIVE_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
if cp.returncode!=0 or error_text or not completion or len(group_done)!=6 or len(base_steps)!=22 or not candidate:
    if stderr: print('GOAL4AJ_DEN_GROUPED_REFLEXIVE_STDERR='+json.dumps(stderr[-12000:]))
    raise SystemExit('Goal4AJ grouped denominator reflexive generator failed closed; no mathematical obstruction credit')
print('GOAL4AJ_DEN_GROUPED_REFLEXIVE=PASS')
