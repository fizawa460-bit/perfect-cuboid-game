#!/usr/bin/env python3
"""Goal4AJ diagnostic: compact Galois-orbit pair ideals for the denominator bottleneck.

Generation7 localized the denominator construction wall to folding the multiplicity-9
[58,60] pair after D13+[26,31].  This preflight checks whether the relevant conjugate
pairs admit much smaller Q-defined union ideals on the canonical four-quadric surface.
It grants no literal coefficient, F_B, E1, or theorem credit.
"""
from __future__ import annotations
import hashlib, json, subprocess, tempfile
from pathlib import Path

GEN7_RUN=34118817169
GEN7_JOB=101731930366
ACTIVE_SHA='59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'

sing=r'''
option(redSB);
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
number ss=u-u^3;
ideal surf=
 a1^2+a2^2-b3^2,
 a2^2+a3^2-b1^2,
 a1^2+a3^2-b2^2,
 a1^2+a2^2+a3^2-c^2;
proc contained(ideal A,ideal B)
{
 ideal G=std(B); int j;
 for(j=1;j<=size(A);j++){if(reduce(A[j],G)!=0){return(0);}}
 return(1);
}
proc equalideal(ideal A,ideal B)
{
 return(contained(A,B)==1 && contained(B,A)==1);
}
ideal P37=b2,ii*a3+a1,a2+c;
ideal P39=b2,ii*a3-a1,a2+c;
ideal P58=a2-a3,ss*a2+b1,b2-b3;
ideal P60=a2-a3,ss*a2-b1,b2-b3;
ideal P26=c,ii*a1-b1,ii*a2+b2,ii*a3+b3;
ideal P31=c,ii*a1+b1,ii*a2-b2,ii*a3-b3;
ideal I37=std(surf+P37); ideal I39=std(surf+P39);
ideal I58=std(surf+P58); ideal I60=std(surf+P60);
ideal I26=std(surf+P26); ideal I31=std(surf+P31);
ideal J3739=std(intersect(I37,I39));
ideal C3739=std(surf+ideal(b2,a2+c));
ideal J5860=std(intersect(I58,I60));
ideal C5860=std(surf+ideal(a2-a3,b2-b3));
ideal J2631=std(intersect(I26,I31));
if(equalideal(J3739,C3739)!=1){ERROR("37/39 compact pair ideal mismatch");}
if(equalideal(J5860,C5860)!=1){ERROR("58/60 compact pair ideal mismatch");}
print("GOAL4AJ_ORBIT_PAIR_3739_GENS="+string(size(J3739)));
print("GOAL4AJ_ORBIT_PAIR_5860_GENS="+string(size(J5860)));
print("GOAL4AJ_ORBIT_PAIR_2631_GENS="+string(size(J2631)));
print("GOAL4AJ_ORBIT_PAIR_3739_BASIS_BEGIN"); print(string(J3739)); print("GOAL4AJ_ORBIT_PAIR_3739_BASIS_END");
print("GOAL4AJ_ORBIT_PAIR_5860_BASIS_BEGIN"); print(string(J5860)); print("GOAL4AJ_ORBIT_PAIR_5860_BASIS_END");
print("GOAL4AJ_ORBIT_PAIR_2631_BASIS_BEGIN"); print(string(J2631)); print("GOAL4AJ_ORBIT_PAIR_2631_BASIS_END");
print("GOAL4AJ_ORBIT_PAIR_COMPACT=PASS");
quit;
'''
with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'orbit-pair.sing'; p.write_text(sing,encoding='utf-8')
    cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=300)
out_text=cp.stdout
err_text=cp.stderr
if cp.returncode!=0 or 'GOAL4AJ_ORBIT_PAIR_COMPACT=PASS' not in out_text:
    print(out_text[-12000:]); print(err_text[-4000:]); raise SystemExit('orbit-pair compactification failed; no mathematical obstruction credit')
lines=out_text.splitlines()
def intval(prefix:str)->int:
    return int(next(x for x in lines if x.startswith(prefix)).split('=',1)[1])
def block(tag:str)->str:
    a=lines.index(f'GOAL4AJ_ORBIT_PAIR_{tag}_BASIS_BEGIN')
    b=lines.index(f'GOAL4AJ_ORBIT_PAIR_{tag}_BASIS_END')
    return '\n'.join(lines[a+1:b]).strip()
b3739=block('3739'); b5860=block('5860'); b2631=block('2631')
assert len(b3739.encode())<20000 and len(b5860.encode())<20000 and len(b2631.encode())<20000
out={
 'schema':'STAGE35_EX_GOAL4AJ_GALOIS_ORBIT_PAIR_COMPACTIFICATION_DIAGNOSTIC_V1',
 'source_locks':{
   'active_divisor_condition_packet_canonical_sha256':ACTIVE_SHA,
   'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,
   'generation7_run':GEN7_RUN,
   'generation7_job':GEN7_JOB,
   'generation7_localized_timeout_tag':'fold_prime58_into_D13',
 },
 'pair_37_39':{
   'exact_union_equals_surface_plus_b2_a2_plus_c':True,
   'standard_basis_generator_count':intval('GOAL4AJ_ORBIT_PAIR_3739_GENS='),
   'basis_text':b3739,
   'basis_text_sha256':hashlib.sha256(b3739.encode()).hexdigest(),
   'basis_contains_extension_symbol_u':('u' in b3739),
 },
 'pair_58_60':{
   'exact_union_equals_surface_plus_a2_minus_a3_b2_minus_b3':True,
   'standard_basis_generator_count':intval('GOAL4AJ_ORBIT_PAIR_5860_GENS='),
   'basis_text':b5860,
   'basis_text_sha256':hashlib.sha256(b5860.encode()).hexdigest(),
   'basis_contains_extension_symbol_u':('u' in b5860),
 },
 'pair_26_31':{
   'exact_union_computed_by_intersection':True,
   'standard_basis_generator_count':intval('GOAL4AJ_ORBIT_PAIR_2631_GENS='),
   'basis_text':b2631,
   'basis_text_sha256':hashlib.sha256(b2631.encode()).hexdigest(),
   'basis_contains_extension_symbol_u':('u' in b2631),
   'reduced_basis_descends_to_Q':('u' not in b2631),
 },
 'orbit_pair_compactification_preflight_passed':True,
 'literal_denominator_coefficients_materialized':False,
 'literal_numerator_coefficients_materialized':False,
 'literal_F_B_materialized':False,
 'E1_proved':False,
 'theorem_credit':False,
 'endpoint_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_ORBIT_PAIR_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
print('GOAL4AJ_ORBIT_PAIR=PASS')
