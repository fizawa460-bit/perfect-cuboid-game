#!/usr/bin/env python3
"""Goal4AJ diagnostic: full degree-19 denominator residual generator via reflexive products.

Use the passing reflexive-product constructor to build the divisorial ideal of
all 22 active strict components of the post-Q-peel denominator residual.  The
passing rigidity diagnostic proves the target degree-19 section space is exactly
one-dimensional.  This leaf therefore searches only for the unique minimal
degree generator modulo the four surface quadrics, records its exact split-field
text hash/size, and reports whether the returned normalization already has Q
coefficients.  It does not yet reattach the 12 peeled Q-linear factors and does
not grant literal denominator/F_B credit.
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

CASES=[
 (37,13,'b2,ii*a3+1*a1,a2+1*c'),
 (39,13,'b2,ii*a3-1*a1,a2+1*c'),
 (26,9,'c,ii*a1-1*b1,ii*a2+1*b2,ii*a3+1*b3'),
 (31,9,'c,ii*a1+1*b1,ii*a2-1*b2,ii*a3-1*b3'),
 (58,9,'a2-1*a3,ss*a2+1*b1,b2-1*b3'),
 (60,9,'a2-1*a3,ss*a2-1*b1,b2-1*b3'),
 (25,7,'c,ii*a1+1*b1,ii*a2+1*b2,ii*a3+1*b3'),
 (32,7,'c,ii*a1-1*b1,ii*a2-1*b2,ii*a3-1*b3'),
 (1,3,'a1,a2+1*b3,a3+1*b2,b1+1*c'),
 (8,3,'a1,a2-1*b3,a3-1*b2,b1-1*c'),
 (9,3,'a2,a3+1*b1,a1+1*b3,b2+1*c'),
 (17,3,'a3,a1+1*b2,a2+1*b1,b3+1*c'),
 (11,2,'a2,a3+1*b1,a1-1*b3,b2+1*c'),
 (21,2,'a3,a1-1*b2,a2+1*b1,b3+1*c'),
 (33,2,'b1,ii*a2+1*a3,a1+1*c'),
 (35,2,'b1,ii*a2-1*a3,a1+1*c'),
 (16,1,'a2,a3-1*b1,a1-1*b3,b2-1*c'),
 (24,1,'a3,a1-1*b2,a2-1*b1,b3-1*c'),
 (28,1,'c,ii*a1-1*b1,ii*a2-1*b2,ii*a3+1*b3'),
 (29,1,'c,ii*a1+1*b1,ii*a2+1*b2,ii*a3-1*b3'),
 (65,1,'a3-1*a1,ss*a3+1*b2,b3+1*b1'),
 (67,1,'a3-1*a1,ss*a3-1*b2,b3+1*b1'),
]
expected={i:m for i,m,_ in CASES}
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
proc sympow(ideal P,int m)
{
 ideal Sk=std(surf+P); ideal Candidate; ideal Sn; list L; int kk;
 for(kk=2;kk<=m;kk++)
 {
  Candidate=surf+Sk*P; L=sat(Candidate,Sing); Sn=std(L[1]); Sk=Sn;
 }
 return(Sk);
}
proc reflexiveProduct(ideal A,ideal B)
{
 ideal Candidate=surf+A*B; list L=sat(Candidate,Sing); return(std(L[1]));
}
ideal P; ideal T; ideal D;
'''
parts=[common]
for step,(idx,m,ideal_text) in enumerate(CASES,1):
    parts.append(f'P={ideal_text};\n')
    parts.append(f'if(dim(std(surf+P))!=2){{ERROR("strict curve {idx} height mismatch");}}\n')
    parts.append(f'T=sympow(P,{m});\n')
    if step==1:
        parts.append('D=T;\n')
    else:
        parts.append('D=reflexiveProduct(D,T);\n')
    parts.append(f'print("GOAL4AJ_DEN_REFLEXIVE_STEP={step}:{idx}:{m}:"+string(size(D)));\n')
parts.append(r'''
list DL=sat(D,Sing); ideal Dstable=std(DL[1]);
if(equalideal(D,Dstable)!=1){ERROR("full denominator divisorial ideal not saturation-stable");}
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
  if(dq==19){d19++; candidate=q;}
 }
}
print("GOAL4AJ_DEN_REFLEXIVE_FINAL_GENERATORS="+string(size(D)));
print("GOAL4AJ_DEN_REFLEXIVE_NONSURF_GENERATORS="+string(nonSurf));
print("GOAL4AJ_DEN_REFLEXIVE_MIN_DEG="+string(minDeg));
print("GOAL4AJ_DEN_REFLEXIVE_DEG19_COUNT="+string(d19));
if(minDeg!=19){ERROR("minimum nonsurface generator degree is not 19");}
if(d19!=1){ERROR("degree19 reduced standard-basis candidate count is not one");}
print("GOAL4AJ_DEN_RESIDUAL_CANDIDATE_BEGIN");
print(string(candidate));
print("GOAL4AJ_DEN_RESIDUAL_CANDIDATE_END");
print("GOAL4AJ_DEN_REFLEXIVE_BUILD=PASS");
quit;
''')
script=''.join(parts)
with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'goal4aj-den-reflexive-full.sing'
    p.write_text(script,encoding='utf-8')
    try:
        cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=1500)
        timed_out=False
    except subprocess.TimeoutExpired as exc:
        stdout=exc.stdout or ''
        if isinstance(stdout,bytes): stdout=stdout.decode('utf-8',errors='replace')
        steps=[x for x in stdout.splitlines() if x.startswith('GOAL4AJ_DEN_REFLEXIVE_STEP=')]
        print('GOAL4AJ_DEN_REFLEXIVE_TIMEOUT_STEPS='+json.dumps(steps[-22:]))
        raise SystemExit('Goal4AJ full denominator reflexive build timed out; no mathematical obstruction credit')
stdout=cp.stdout; stderr=cp.stderr
error_text=any(s in stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign'))
lines=stdout.splitlines()
steps=[x for x in lines if x.startswith('GOAL4AJ_DEN_REFLEXIVE_STEP=')]
def val(prefix):
    return int(next(x for x in lines if x.startswith(prefix)).split('=',1)[1])
try:
    i0=lines.index('GOAL4AJ_DEN_RESIDUAL_CANDIDATE_BEGIN')
    i1=lines.index('GOAL4AJ_DEN_RESIDUAL_CANDIDATE_END')
    candidate='\n'.join(lines[i0+1:i1]).strip()
except ValueError:
    candidate=''
completion='GOAL4AJ_DEN_REFLEXIVE_BUILD=PASS' in lines
out={
 'schema':'STAGE35_EX_GOAL4AJ_DENOMINATOR_RESIDUAL_REFLEXIVE_GENERATOR_DIAGNOSTIC_V1',
 'source_locks':{
   'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,
   'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,
   'q_hyperplane_factor_peel_canonical_sha256':QPEEL_SHA,
   'a1_residual_jet_canonical_sha256':A1_SHA,
   'denominator_rigidity_canonical_sha256':DEN_RIGIDITY_SHA,
   'numerator_rigidity_canonical_sha256':NUM_RIGIDITY_SHA,
   'reflexive_product_preflight_canonical_sha256':REFLEXIVE_PREFLIGHT_SHA,
 },
 'singular_returncode':cp.returncode,
 'singular_error_text_present':error_text,
 'singular_timed_out':timed_out,
 'completed_component_count':len(steps),
 'expected_component_count':len(CASES),
 'final_standard_basis_generator_count':val('GOAL4AJ_DEN_REFLEXIVE_FINAL_GENERATORS=') if completion else None,
 'nonsurface_standard_basis_generator_count':val('GOAL4AJ_DEN_REFLEXIVE_NONSURF_GENERATORS=') if completion else None,
 'minimum_nonsurface_generator_degree':val('GOAL4AJ_DEN_REFLEXIVE_MIN_DEG=') if completion else None,
 'degree19_candidate_count':val('GOAL4AJ_DEN_REFLEXIVE_DEG19_COUNT=') if completion else None,
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
print('GOAL4AJ_DEN_REFLEXIVE_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
if cp.returncode!=0 or error_text or not completion or len(steps)!=len(CASES) or not candidate:
    if stderr: print('GOAL4AJ_DEN_REFLEXIVE_STDERR='+json.dumps(stderr[-12000:]))
    raise SystemExit('Goal4AJ full denominator reflexive generator failed closed; no mathematical obstruction credit')
print('GOAL4AJ_DEN_REFLEXIVE=PASS')
