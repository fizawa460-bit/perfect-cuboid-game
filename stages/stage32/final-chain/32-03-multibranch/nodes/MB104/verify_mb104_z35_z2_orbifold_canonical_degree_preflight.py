#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name(
 "MB104-Z35-Z2-ORBIFOLD-CANONICAL-DEGREE-PREFLIGHT-CERTIFICATE.json").read_text())

assert d["schema"]=="STAGE32_MB104_Z35_Z2_ORBIFOLD_CANONICAL_DEGREE_PREFLIGHT_V2"
r=d["retained"]
assert r["K2"]==16 and r["c2"]==80

s=d["sabatino_boundary_family"]
for n in range(49):
    assert (16-2*n)-(80-2*n)==-64
assert s["difference"]=="-64"

x=d["sabatino_theorem11i"]
assert x["applicable_with_KplusD_Q_effective"] is True
assert x["curve_singularity_classification_required"] is False
assert x["inequality_polynomial"]=="168*l*(l+1)*alpha^2-(224-8*t)*l*alpha+224-4*r"
assert x["vertex_alpha"]=="(28-t)/(42*(l+1))"
assert x["uniform_minimum_lower_bound"]==">40/3"

for t in range(15):
    # Worst legal boundary r=34+t.
    lim=Fraction(88-4*t)-Fraction((224-8*t)**2,672)
    assert lim == Fraction(2*(189-(t-7)**2),21)
    assert lim >= Fraction(40,3)
    for l in range(1,101):
        a=Fraction(28-t,42*(l+1))
        assert 0 <= a <= 1
        A=168*l*(l+1)
        B=-(224-8*t)*l
        C=88-4*t
        fmin=Fraction(C)-Fraction(B*B,4*A)
        assert fmin > Fraction(40,3)

assert x["all_l_all_exceptional_boundaries_strictly_satisfied"] is True

la=d["langer"]
assert la["normal_log_pair_generality"] is True
assert la["local_orbifold_terms_required"] is True
assert la["current_local_correction_source_complete"] is False
sc=la["log_canonicity_scaling"]
assert sc["alpha_upper_bound"]=="1/(4l)"
assert sc["log_pair_square_independent_of_l"] is True

assert d["disposition"]=="PARK_Z2_AS_SOURCE_COMPLETE_ALL_L_THEOREM_NO_GO"
assert d["next_leaf"]=="MB104-Z37-SURVIVING-768-FIRST-NORMAL-EXACT-TRANSITION-REOPEN-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())

print("PASS: Z35/Z2 source-valid theorem application")
print("Sabatino Theorem 1.1(i): F=168*l*(l+1)*a^2-(224-8*t)*l*a+224-4*r")
print("all legal exceptional boundaries and alpha in [0,1]: F > 40/3")
print("Z2 is an exact all-l no-go on the balanced N14 ray")
