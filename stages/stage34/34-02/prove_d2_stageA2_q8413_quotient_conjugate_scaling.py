#!/usr/bin/env python3
from __future__ import annotations
import json,pathlib

ROOT=pathlib.Path(__file__).resolve().parent
OUT=ROOT/"d2-stageA2-q8413-quotient-conjugate-scaling-certificate.json"

def mul(z,w):
    a,b=z; c,d=w
    return (a*c-b*d,a*d+b*c)

def conj(z): return (z[0],-z[1])
def power(z,n):
    r=(1,0)
    for _ in range(n): r=mul(r,z)
    return r

a2_38=(-89531,578508)
a4_38=(0,-51794399748)
a2_165=(1157016,-179062)
a4_165=(0,-207177598992)
lam=(0,2)       # 2*i
mu=(2,-2)       # 2-2*i

assert mul(lam,conj(a2_38))==a2_165
assert mul(power(lam,2),conj(a4_38))==a4_165
assert power(mu,2)==power(lam,3)==(0,-8)

payload={
  "schema":"STAGE34_02C_D2_STAGEA2_Q8413_QUOTIENT_CONJUGATE_SCALING_CERTIFICATE_V1",
  "status":"PASS_EXACT_QI_CONJUGATE_SCALING_RANK_OBSTRUCTION_IDENTIFIED_NO_CLOSURE",
  "source_script":"prove_d2_stageA2_q8413_quotient_conjugate_scaling.py",
  "field":"Q(i), i^2=-1",
  "source_branch":{"branch_id":"40dc8f63e92a8a3a65e8","model_id":38,"a2":"-89531+578508*i","a4":"-51794399748*i"},
  "target_branch":{"branch_id":"7a7ef1a67e794fe1651f","model_id":165,"a2":"1157016-179062*i","a4":"-207177598992*i"},
  "semilinear_map":{"first":"complex conjugation i -> -i","then":"x'=(2*i)*x, y'=(2-2*i)*y","lambda":"2*i","mu":"2-2*i"},
  "identities":{"lambda_times_conj_a2":"1157016-179062*i","lambda_squared_times_conj_a4":"-207177598992*i","mu_squared_equals_lambda_cubed":"-8*i"},
  "consequence":"The two q=84/13 elliptic quotients are Q(i)-isomorphic after field conjugation, hence their Mordell-Weil ranks are equal. The unresolved [0,1] rank obstruction is one arithmetic obstruction rather than two independent ones.",
  "non_consequence":"This semilinear isomorphism does not by itself prove that the rational quotient-X condition or parent pullback condition transfers between the two genus-two branches. Each rational-X/parent classification still needs an exact adapter before branch closure.",
  "credit":"Exact quotient-rank-obstruction compression only. No branch, sign partner, parent receiver, or Stage29 endpoint closes here.",
  "firewalls":{"rank_equal":True,"rational_X_transfer_proved":False,"parent_transfer_proved":False,"hostile_audit_passed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"D2_all_factor_branches_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"rank_equal":True,"closure":False},sort_keys=True))
