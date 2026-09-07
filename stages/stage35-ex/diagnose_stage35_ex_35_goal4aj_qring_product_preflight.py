#!/usr/bin/env python3
"""Goal4AJ diagnostic: quotient-ring product preflight on actual Stoll primes.

Checks that forming products inside Singular's quotient ring by the four canonical
surface quadrics, lifting back to the ambient polynomial ring, and taking one
final saturation at the isolated A1 singular locus gives the same reflexive ideal
as the retained ambient constructor. Diagnostic only: no literal F_B/E1 credit.
"""
from __future__ import annotations
import hashlib,json,subprocess,tempfile
from pathlib import Path

ONESHOT_SHA='da58a9c6b72a71d71c9af6f87fa987d2589b0fb3568918bc6994c3960de28a80'
script=r'''
option(redSB); LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp; minpoly=u^4+1; number ii=u^2; number ss=u-u^3;
ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;
matrix Jac=jacob(surf); ideal Sing=minor(Jac,4);
ideal P1=a1,a2+b3,a3+b2,b1+c;
ideal P8=a1,a2-b3,a3+b2,b1-c;
ideal P37=a2,a1+b3,a3+b1,b2+c;
proc contained(ideal A,ideal B){ideal G=std(B); int j; for(j=1;j<=size(A);j++){if(reduce(A[j],G)!=0){return(0);}} return(1);}
proc equalideal(ideal A,ideal B){return(contained(A,B)==1 && contained(B,A)==1);}
proc rprod(ideal A,ideal B){ideal C=surf+A*B; list LL=sat(C,Sing); return(std(LL[1]));}
// Ambient references.
ideal A1=rprod(rprod(P1,P1),P1);
ideal A3=rprod(rprod(P1,P8),P37);
// Quotient-ring products.
qring qr=std(surf);
ideal qP1=imap(r,P1); ideal qP8=imap(r,P8); ideal qP37=imap(r,P37);
ideal qCube=std(std(qP1*qP1)*qP1);
ideal qTriple=std(std(qP1*qP8)*qP37);
setring r;
ideal LCube=imap(qr,qCube); ideal LTriple=imap(qr,qTriple);
ideal ACube0=std(surf+LCube); list LC=sat(ACube0,Sing); ideal ACube=std(LC[1]);
ideal ATriple0=std(surf+LTriple); list LT=sat(ATriple0,Sing); ideal ATriple=std(LT[1]);
if(equalideal(A1,ACube)!=1){ERROR("qring cube lift mismatch");}
if(equalideal(A3,ATriple)!=1){ERROR("qring triple lift mismatch");}
print("GOAL4AJ_QRING_CUBE=PASS");
print("GOAL4AJ_QRING_TRIPLE=PASS");
print("GOAL4AJ_QRING_CUBE_GENS="+string(size(ACube)));
print("GOAL4AJ_QRING_TRIPLE_GENS="+string(size(ATriple)));
print("GOAL4AJ_QRING_PRODUCT_PREFLIGHT=PASS");
quit;
'''
with tempfile.TemporaryDirectory() as td:
    p=Path(td)/'goal4aj-qring-preflight.sing'; p.write_text(script,encoding='utf-8')
    cp=subprocess.run(['Singular','-q',str(p)],text=True,capture_output=True,timeout=180)
stdout=cp.stdout; stderr=cp.stderr; lines=stdout.splitlines()
error_text=any(s in stdout.lower() for s in ('error occurred','? error','? cannot','? wrong','? member','? assign'))
completion='GOAL4AJ_QRING_PRODUCT_PREFLIGHT=PASS' in lines
out={
 'schema':'STAGE35_EX_GOAL4AJ_QRING_PRODUCT_PREFLIGHT_V1',
 'source_locks':{'oneshot_reflexive_hull_preflight_canonical_sha256':ONESHOT_SHA},
 'constructor':'Singular qring product modulo canonical surface, ambient lift, one final A1 saturation',
 'actual_stoll_prime_labels':[1,8,37],
 'cube_equal':('GOAL4AJ_QRING_CUBE=PASS' in lines),
 'triple_equal':('GOAL4AJ_QRING_TRIPLE=PASS' in lines),
 'singular_returncode':cp.returncode,
 'singular_error_text_present':error_text,
 'literal_F_B_materialized':False,
 'E1_proved':False,
 'theorem_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_QRING_PRODUCT_PREFLIGHT_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
if cp.returncode!=0 or error_text or not completion or not out['cube_equal'] or not out['triple_equal']:
    if stdout: print('GOAL4AJ_QRING_STDOUT='+json.dumps(stdout[-12000:]))
    if stderr: print('GOAL4AJ_QRING_STDERR='+json.dumps(stderr[-12000:]))
    raise SystemExit('Goal4AJ qring product preflight failed closed')
print('GOAL4AJ_QRING_PRODUCT_PREFLIGHT=PASS')
