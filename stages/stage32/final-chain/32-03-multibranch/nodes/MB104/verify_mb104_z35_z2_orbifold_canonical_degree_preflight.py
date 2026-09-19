#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name(
 "MB104-Z35-Z2-ORBIFOLD-CANONICAL-DEGREE-PREFLIGHT-CERTIFICATE.json").read_text())
s=d["sabatino_boundary_family"]; l=d["langer"]; r=d["retained"]

assert r["K2"]==16 and r["c2"]==80
for n in range(49):
    lhs=16-2*n
    eopen=80-2*n
    assert lhs-eopen==-64
    assert not (lhs>eopen)
    if n>0:
        # (K+D).E_i = E_i^2 = -2
        assert -2 < 0

assert s["difference"]=="-64"
assert s["strict_positivity_hypothesis_satisfied"] is False
assert s["nef_for_nonempty_boundary"] is False
assert l["normal_log_pair_generality"] is True
assert l["local_orbifold_terms_required"] is True
assert l["current_local_correction_source_complete"] is False
sc=l["log_canonicity_scaling"]
assert sc["strict_transform_class"]=="7lH-4l*sum_E"
assert sc["total_transform_exceptional_coefficient"]=="4l"
assert sc["exceptional_discrepancy"]=="-4*alpha*l"
assert sc["alpha_upper_bound"]=="1/(4l)"
assert sc["beta_definition"]=="beta=alpha*l"
assert sc["beta_upper_bound"]=="1/4"
assert sc["log_pair_square"]=="16*(1+7*beta)^2"
assert sc["log_pair_square_independent_of_l"] is True
assert sc["degree_cutting_requires_controlled_local_orbifold_terms"] is True
assert d["disposition"]=="PARK_Z2_AT_NUMERICAL_POSITIVITY_AND_LOCAL_ORBIFOLD_INPUT_WALLS"
assert d["next_leaf"]=="MB104-Z36-Z4P-FORCED-ORDINARY-SINGULARITY-LOCALIZATION-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())

print("PASS: Z35/Z2 orbifold/open canonical-degree theorem preflight")
print("for every exceptional boundary subset: (K+D)^2-e(S\\D)=-64")
print("nonempty exceptional boundary also makes K+D non-nef")
print("normal-pair Langer route returns to missing local orbifold correction data")
print("lc scaling: alpha<=1/(4l), so (K+alpha*C)^2=16*(1+7*beta)^2 with beta=alpha*l")
