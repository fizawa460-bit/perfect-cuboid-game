#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name(
 "MB104-Z39-COMPLETE-P-NULL-CURVE-FINITE-DEGREE-REDUCTION-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z39_COMPLETE_P_NULL_CURVE_FINITE_DEGREE_REDUCTION_V1"
x=d["derivation"]
assert x["e_divisible_by"]==4
assert x["R2_upper"]=="-3e^2/64"
assert x["R2_lower"]=="-e-2"
assert x["quadratic"]=="3e^2<=64e+128"

allowed=[]
for e in range(1,1000):
    if e%4==0 and 3*e*e <= 64*e+128:
        allowed.append(e)
assert allowed==[4,8,12,16,20]
assert x["possible_positive_degrees"]==allowed
assert x["integer_upper_bound"]==23

# Verify the rational Hodge/Cauchy coefficient:
# e^2/16 - 1/2 * 7e^2/32 = -3e^2/64.
assert Fraction(1,16)-Fraction(7,64)==Fraction(-3,64)

p=d["retained_picard_interface"]
assert p["exact_head"]=="dbf98cacc6d1349ead658ef064fefe48f6d5e4f4"
assert p["rank"]==64 and p["Hperp_rank"]==63
assert d["conclusion"]["nonexceptional_P_null_curves_finite_degree_reduced"] is True
assert d["conclusion"]["complete_null_locus_classified"] is False
assert d["next_leaf"]=="MB104-Z40-P-NULL-PICARD64-FINITE-ENUMERATION"
assert all(v is False for v in d["credit_firewall"].values())

print("PASS: Z39 finite P-null degree reduction")
print("P.R=0 + Z21 Hodge + Cauchy + adjunction => 3e^2<=64e+128 and 4|e")
print("nonexceptional P-null degrees are exactly among 4,8,12,16,20")
print("next: exact Picard64 finite enumeration")
