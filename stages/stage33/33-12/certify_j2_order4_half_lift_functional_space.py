#!/usr/bin/env python3
"""Enumerate every mixed-Smith order-4 half-lift 2w=u1 and its proper-Br2 functional."""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
U1 = HERE / "j2-semantic-u1-full-surface-smith-source.json"
PROPER = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
OUT = HERE / "j2-order4-half-lift-functional-space.json"
LOCKS = {
    U1: "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec",
    PROPER: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    TARGET: "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path):
    x=json.loads(path.read_text()); b=dict(x); h=b.pop("canonical_sha256")
    assert h == LOCKS[path] == csha(b), path
    return x


def rowmul(v,m):
    return [sum((int(v[i])&1)*(int(m[i][j])&1) for i in range(len(v)))&1 for j in range(len(m[0]))]


def solve10(basis,target):
    for bits in itertools.product((0,1), repeat=10):
        v=[0]*14
        for bit,row in zip(bits,basis):
            if bit: v=[a^(int(b)&1) for a,b in zip(v,row)]
        if v==target: return list(bits)
    return None


u1=locked(U1); proper=locked(PROPER); target=locked(TARGET)
mods=u1["retained_common_smith_source"]["discriminant_moduli"]
y2=u1["exact_normalization"]["nontrivial_smith_coordinates_mixed_moduli"]
b8=u1["retained_common_smith_source"]["discriminant_bilinear_numerator_over_8_reduced"]
assert mods == [2]*4+[4]*6+[8]*4
assert all(v in (0,m//2) for v,m in zip(y2,mods))
scales=[m//2 for m in mods]
choices=[]
for v,m in zip(y2,mods):
    cs=[x for x in range(m) if (2*x)%m==v]
    assert len(cs)==2
    choices.append(cs)
assert 2**14 == 16384
basis10=target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]

functional_to_count={}
functional_to_witness={}
invariant_to_count={}
invariant_to_witness={}
divisibility_fail=0
for w in itertools.product(*choices):
    nums=[sum(w[i]*scales[j]*int(b8[i][j]) for i in range(14)) for j in range(14)]
    if any(x%4 for x in nums):
        divisibility_fail += 1
        continue
    f=tuple((x//4)&1 for x in nums)
    functional_to_count[f]=functional_to_count.get(f,0)+1
    functional_to_witness.setdefault(f,list(w))
    if rowmul(f,proper["proper_Br2_cc_action_f2"])==list(f) and rowmul(f,proper["proper_Br2_ct_action_f2"])==list(f):
        invariant_to_count[f]=invariant_to_count.get(f,0)+1
        invariant_to_witness.setdefault(f,list(w))

invariants=[]
for f,count in sorted(invariant_to_count.items()):
    coord=solve10(basis10,list(f))
    assert coord is not None
    invariants.append({
        "proper_Br2_14D_coordinate_f2": list(f),
        "weight": sum(f),
        "half_lift_count": count,
        "one_half_lift_witness_mixed_smith": invariant_to_witness[f],
        "retained_10D_coordinate_f2": coord,
    })

out={
    "schema":"STAGE33_12_J2_ORDER4_HALF_LIFT_FUNCTIONAL_SPACE_V1",
    "stage":"33-12",
    "status":"PASS_EXACT_HALF_LIFT_FUNCTIONAL_SPACE_ENUMERATED",
    "source_locks":{
        "semantic_u1_full_surface_smith_source_sha256":LOCKS[U1],
        "proper_brauer2_sha256":LOCKS[PROPER],
        "retained_10D_target_basis_sha256":LOCKS[TARGET],
    },
    "equations":{
        "half_lift":"2*w = locked semantic u1 mixed-Smith coordinate",
        "functional":"f_j=2*b(w,(m_j/2)e_j)=(sum_i w_i*(m_j/2)*B8[i][j])/4 mod2",
        "q_defined_test":"f fixed by proper-Br2 cc and ct actions",
    },
    "enumeration":{
        "half_lifts_total":16384,
        "pairing_divisibility_failures":divisibility_fail,
        "distinct_functionals":len(functional_to_count),
        "distinct_joint_v4_fixed_functionals":len(invariant_to_count),
        "joint_v4_fixed_functionals":invariants,
        "zero_functional_present_among_joint_v4_fixed":tuple([0]*14) in invariant_to_count,
        "nonzero_joint_v4_fixed_functional_count":sum(1 for f in invariant_to_count if any(f)),
    },
    "interpretation_firewall":{
        "actual_J2_functional_selected_by_half_lift_and_q_definedness_alone":len(invariant_to_count)==1 and tuple([0]*14) not in invariant_to_count,
        "half_lift_relation_proven_for_actual_full_surface_J2":False,
        "proper_Br2_14D_coordinate_promoted":False,
        "retained_10D_coordinate_promoted":False,
        "first_75D_matrix_column_materialized":False,
        "stage33_12_closed_exact":False,
        "stage33_13_released":False,
        "theorem_credit":False,
        "receiver_credit":False,
        "endpoint_credit":False,
    },
}
out["canonical_sha256"]=csha(out)
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({
    "success":True,
    "distinct_functionals":len(functional_to_count),
    "joint_v4_fixed":len(invariant_to_count),
    "nonzero_joint_v4_fixed":sum(1 for f in invariant_to_count if any(f)),
    "invariants":invariants,
    "canonical_sha256":out["canonical_sha256"],
},sort_keys=True))
