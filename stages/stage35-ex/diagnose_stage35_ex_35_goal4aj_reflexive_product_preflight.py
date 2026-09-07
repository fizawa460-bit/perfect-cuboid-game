#!/usr/bin/env python3
"""Goal4AJ preflight: reflexive product builder for sums of strict divisors.

The direct denominator lane used repeated intersections and was both logically
misinitialized and computationally unattractive.  For height-one divisors on a
normal surface, the divisorial ideal of D1+D2 is the reflexive product of the
individual divisorial ideals.  Away from the isolated A1 singular locus the
strict primes are Cartier, so ordinary ideal product already adds valuations;
saturating by the singular locus repairs only the codimension-two A1 defect.

This preflight checks that construction exactly against direct intersections on
small actual Stoll strict-curve powers inside the cuboid four-quadric surface.
It is only an API/mathematical-constructor preflight; it materializes no section.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile

SINGULAR = r'''
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

proc contained(ideal A, ideal B)
{
  ideal G=std(B);
  int j;
  for (j=1; j<=size(A); j++)
  {
    if (reduce(A[j],G)!=0) { return(0); }
  }
  return(1);
}
proc equalideal(ideal A, ideal B)
{
  return(contained(A,B)==1 && contained(B,A)==1);
}
proc sympow(ideal P, int m)
{
  ideal Sk=std(surf+P);
  ideal Candidate;
  ideal Sn;
  list SatL;
  int kk;
  for (kk=2; kk<=m; kk++)
  {
    Candidate=surf+Sk*P;
    SatL=sat(Candidate,Sing);
    Sn=std(SatL[1]);
    Sk=Sn;
  }
  return(Sk);
}
proc reflexiveProduct(ideal A, ideal B)
{
  ideal Candidate=surf+A*B;
  list L=sat(Candidate,Sing);
  return(std(L[1]));
}

// Actual retained C1[1], C1[8], C2[37].
ideal P1=a1,a2+b3,a3+b2,b1+c;
ideal P8=a1,a2-b3,a3-b2,b1-c;
ideal P37=b2,ii*a3+a1,a2+c;
if (dim(std(surf+P1))!=2 || dim(std(surf+P8))!=2 || dim(std(surf+P37))!=2)
{ ERROR("strict prime height regression"); }

// Case A: distinct C1 powers 2 and 3.
ideal A1=sympow(P1,2);
ideal A8=sympow(P8,3);
ideal IA=std(intersect(A1,A8));
list IAL=sat(IA,Sing);
IA=std(IAL[1]);
ideal RA=reflexiveProduct(A1,A8);
if (equalideal(IA,RA)!=1) { ERROR("C1/C1 reflexive product mismatch"); }
print("GOAL4AJ_REFLEXIVE_PRODUCT_C1_C1=PASS");
print("GOAL4AJ_REFLEXIVE_PRODUCT_C1_C1_GENERATORS="+string(size(RA)));

// Case B: C1 power2 plus Q(i)-defined C2 power2.
ideal A37=sympow(P37,2);
ideal IB=std(intersect(A1,A37));
list IBL=sat(IB,Sing);
IB=std(IBL[1]);
ideal RB=reflexiveProduct(A1,A37);
if (equalideal(IB,RB)!=1) { ERROR("C1/C2 reflexive product mismatch"); }
print("GOAL4AJ_REFLEXIVE_PRODUCT_C1_C2=PASS");
print("GOAL4AJ_REFLEXIVE_PRODUCT_C1_C2_GENERATORS="+string(size(RB)));

// Associativity up to reflexive hull on three actual primes.
ideal LHS=reflexiveProduct(RA,A37);
ideal T=reflexiveProduct(A8,A37);
ideal RHS=reflexiveProduct(A1,T);
if (equalideal(LHS,RHS)!=1) { ERROR("reflexive product associativity mismatch"); }
print("GOAL4AJ_REFLEXIVE_PRODUCT_ASSOCIATIVE=PASS");
print("GOAL4AJ_REFLEXIVE_PRODUCT_PREFLIGHT=PASS");
quit;
'''

with tempfile.TemporaryDirectory() as td:
    from pathlib import Path
    p=Path(td)/"goal4aj-reflexive-product.sing"
    p.write_text(SINGULAR,encoding="utf-8")
    cp=subprocess.run(["Singular","-q",str(p)],text=True,capture_output=True,timeout=420)
stdout=cp.stdout; stderr=cp.stderr
print(stdout,end="")
if stderr:
    print("GOAL4AJ_REFLEXIVE_PRODUCT_STDERR="+json.dumps(stderr[-12000:]))
error_text=any(s in stdout.lower() for s in ("error occurred","? error","? cannot","? wrong","? member","? assign"))
markers={
  "c1_c1_exact":"GOAL4AJ_REFLEXIVE_PRODUCT_C1_C1=PASS" in stdout,
  "c1_c2_exact":"GOAL4AJ_REFLEXIVE_PRODUCT_C1_C2=PASS" in stdout,
  "associative_exact":"GOAL4AJ_REFLEXIVE_PRODUCT_ASSOCIATIVE=PASS" in stdout,
  "completion_marker_present":"GOAL4AJ_REFLEXIVE_PRODUCT_PREFLIGHT=PASS" in stdout,
}
out={
 "schema":"STAGE35_EX_GOAL4AJ_REFLEXIVE_PRODUCT_PREFLIGHT_DIAGNOSTIC_V1",
 "singular_returncode":cp.returncode,
 "singular_error_text_present":error_text,
 **markers,
 "constructor":"reflexive_product(A,B)=saturation(surface+A*B,jacobian_singular_locus)",
 "direct_intersection_comparison_saturated_at_singular_locus":True,
 "actual_stoll_strict_primes_used":[1,8,37],
 "full_packet_built":False,
 "literal_numerator_coefficients_materialized":False,
 "literal_denominator_coefficients_materialized":False,
 "literal_F_B_materialized":False,
 "E1_proved":False,
 "stage35_closed":False,
 "theorem_credit":False,
 "endpoint_credit":False,
}
out["canonical_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":" )).encode()).hexdigest()
print("GOAL4AJ_REFLEXIVE_PRODUCT_JSON="+json.dumps(out,sort_keys=True,separators=(",",":")))
if cp.returncode!=0 or error_text or not all(markers.values()):
    raise SystemExit("Goal4AJ reflexive-product preflight failed closed")
