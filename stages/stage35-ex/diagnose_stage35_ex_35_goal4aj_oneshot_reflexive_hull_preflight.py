#!/usr/bin/env python3
"""Goal4AJ preflight: one-shot reflexive hull for a sum of strict divisors.

The grouped denominator generation2 completed all six multiplicity-group powers
but timed out while reflexively merging those six already-built divisorial ideals.
For a normal surface with isolated A1 singularities, the divisor sum can instead
be formed by the ordinary product followed by one reflexive hull, implemented
here as saturation by the singular locus.  This preflight checks that one-shot
construction against the already-verified iterated reflexive product on small
actual Stoll strict-prime powers.

Diagnostic only: no full packet, literal section, F_B, E1, or theorem credit.
"""
from __future__ import annotations
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

SINGULAR=r'''
option(redSB);
LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
ideal surf=
 a1^2+a2^2-b3^2,
 a2^2+a3^2-b1^2,
 a1^2+a3^2-b2^2,
 a1^2+a2^2+a3^2-c^2;
matrix J=jacob(surf);
ideal Sing=minor(J,4);
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
proc sympow(ideal P,int m)
{
 ideal Sk=std(surf+P); ideal Candidate; ideal Sn; list L; int k;
 for(k=2;k<=m;k++)
 {
  Candidate=surf+Sk*P; L=sat(Candidate,Sing); Sn=std(L[1]); Sk=Sn;
 }
 return(Sk);
}
ideal P1=a1,a2+b3,a3+b2,b1+c;
ideal P8=a1,a2-b3,a3-b2,b1-c;
ideal P37=b2,ii*a3+a1,a2+c;
if(dim(std(surf+P1))!=2 || dim(std(surf+P8))!=2 || dim(std(surf+P37))!=2)
{ERROR("strict prime height regression");}
ideal A1=sympow(P1,2);
ideal A8=sympow(P8,3);
ideal A37=sympow(P37,2);
ideal R12=reflexiveProduct(A1,A8);
ideal ITER=reflexiveProduct(R12,A37);
ideal Raw=surf+A1*A8*A37;
list OL=sat(Raw,Sing); ideal ONE=std(OL[1]);
if(equalideal(ITER,ONE)!=1){ERROR("one-shot reflexive hull mismatch");}
print("GOAL4AJ_ONESHOT_REFLEXIVE_THREE_FACTOR=PASS");
print("GOAL4AJ_ONESHOT_REFLEXIVE_ITER_GENERATORS="+string(size(ITER)));
print("GOAL4AJ_ONESHOT_REFLEXIVE_ONE_GENERATORS="+string(size(ONE)));
list StableL=sat(ONE,Sing); ideal Stable=std(StableL[1]);
if(equalideal(ONE,Stable)!=1){ERROR("one-shot result not saturation-stable");}
print("GOAL4AJ_ONESHOT_REFLEXIVE_STABLE=PASS");
print("GOAL4AJ_ONESHOT_REFLEXIVE_PREFLIGHT=PASS");
quit;
'''
with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'goal4aj-oneshot-reflexive.sing'
    p.write_text(SINGULAR,encoding='utf-8')
    cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=420)
stdout=cp.stdout; stderr=cp.stderr
print(stdout,end='')
if stderr: print('GOAL4AJ_ONESHOT_REFLEXIVE_STDERR='+json.dumps(stderr[-12000:]))
error_text=any(s in stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign'))
markers={
 'three_factor_exact':'GOAL4AJ_ONESHOT_REFLEXIVE_THREE_FACTOR=PASS' in stdout,
 'saturation_stable':'GOAL4AJ_ONESHOT_REFLEXIVE_STABLE=PASS' in stdout,
 'completion_marker_present':'GOAL4AJ_ONESHOT_REFLEXIVE_PREFLIGHT=PASS' in stdout,
}
out={
 'schema':'STAGE35_EX_GOAL4AJ_ONESHOT_REFLEXIVE_HULL_PREFLIGHT_DIAGNOSTIC_V1',
 'singular_returncode':cp.returncode,
 'singular_error_text_present':error_text,
 **markers,
 'constructor':'one_shot_reflexive_hull(A_1,...,A_n)=saturation(surface+product(A_i),jacobian_singular_locus)',
 'compared_against_iterated_reflexive_product':True,
 'actual_stoll_strict_primes_used':[1,8,37],
 'strict_prime_powers_used':[2,3,2],
 'full_packet_built':False,
 'literal_numerator_coefficients_materialized':False,
 'literal_denominator_coefficients_materialized':False,
 'literal_F_B_materialized':False,
 'E1_proved':False,
 'stage35_closed':False,
 'theorem_credit':False,
 'endpoint_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_ONESHOT_REFLEXIVE_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
if cp.returncode!=0 or error_text or not all(markers.values()):
    raise SystemExit('Goal4AJ one-shot reflexive hull preflight failed closed')
