#!/usr/bin/env python3
"""Exact CV-normalization to frozen ruled-model support adapter for named J2.

This leaf does not guess a Stoll PicK/discriminant coordinate.  It only
identifies the named J2 half-divisor support in the frozen Stage29 ruled
P1xP1 coordinates, thereby shrinking the remaining bridge to a resolved
ruled-model -> marked-Kc divisor map on three explicit supports.
"""

import hashlib
import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-cv-to-ruled-support-adapter.json"

t, s, z, u = sp.symbols("t s z u")
u1, v1, u2, v2 = sp.symbols("u1 v1 u2 v2")
i = sp.I
s2 = sp.sqrt(2)

q = sp.expand(t**4 - 6*t**2 + 1)
Dplus = sp.expand(t**2 - 2*t - 1)
Gplus = sp.expand(t*(1-s**2) + i*s*(1-t**2))
s_plus = sp.cancel(i*(1-t**2+z)/(2*t))

# Frozen Stage29 ruled model.
A1 = v1**2 - u1**2
A2 = v2**2 - u2**2
X = u1*v1*A2
Y = u2*v2*A1

# The CV branch coordinates are literally the ruled affine coordinates.
ruled_identity = sp.simplify(
    v1**2*v2**2*Gplus.subs({t:u1/v1, s:u2/v2}) - (X+i*Y)
)
assert ruled_identity == 0

r_plus = 1+s2
r_minus = 1-s2
for r in (r_plus, r_minus):
    assert sp.simplify(Dplus.subs(t, r)) == 0
    assert sp.simplify(q.subs(t, r)) == 0
    assert sp.simplify(s_plus.subs({t:r, z:0}) + i) == 0
    sub = {u1:r, v1:1, u2:-i, v2:1}
    assert sp.simplify((X+i*Y).subs(sub)) == 0

# At infinity-minus use u=1/t and Z=z/t^2=-1.  The reciprocal of s tends to 0,
# so the ruled second coordinate is [u2:v2]=[1:0].
Z = sp.symbols("Z")
s_inf = sp.cancel(i*(u**2 - 1 + Z)/(2*u))
inv_s_inf = sp.cancel(1/s_inf)
assert sp.simplify(inv_s_inf.subs({u:0, Z:-1})) == 0

cert = {
    "schema":"STAGE33_12_J2_CV_TO_RULED_SUPPORT_ADAPTER_V1",
    "source_locks":{
        "stage33_05_source_reduction_git_blob_sha1":"662ad27494c8e275012a5ce0e1656a7c62782730",
        "stage33_05_normalization_galois_skeleton_git_blob_sha1":"139a309c52a6646e649d37bdb03c3bb535d29cf1",
        "stage33_05_j2_arithmetic_descent_git_blob_sha1":"a63be5592c793c3812da99275478f14dd0d2687b",
        "stage33_12_j2_named_kummer_glue_input_git_blob_sha1":"7574bb1acdf458b67e65f609b6c361473ce406c6",
        "stoll_repository":"MichaelStollBayreuth/Verification",
        "stoll_commit":"51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "stoll_path":"Cuboids/cuboids.magma",
    },
    "exact_coordinate_identification":{
        "ruled_model":{
            "A1":"v1^2-u1^2",
            "A2":"v2^2-u2^2",
            "X":"u1*v1*A2",
            "Y":"u2*v2*A1",
            "branch_plus":"X+i*Y=0",
        },
        "cv_branch_plus":"t*(1-s^2)+i*s*(1-t^2)=0",
        "adapter":{"t":"u1/v1","s":"u2/v2"},
        "identity":"v1^2*v2^2*Gplus(t,s)=X+iY",
        "identity_verified_exact":True,
    },
    "j2_half_divisor":{
        "name":"E_J2",
        "definition":"2*infinity_minus-P_plus-P_minus",
        "Dplus":"t^2-2*t-1",
        "P_plus":{
            "t":"1+sqrt(2)","z":"0","s":"-i",
            "ruled_P1xP1":["[1+sqrt(2):1]","[-i:1]"],
        },
        "P_minus":{
            "t":"1-sqrt(2)","z":"0","s":"-i",
            "ruled_P1xP1":["[1-sqrt(2):1]","[-i:1]"],
        },
        "infinity_minus":{
            "t":"infinity","z_over_t2":"-1","s":"infinity",
            "ruled_P1xP1":["[1:0]","[1:0]"],
        },
        "finite_support_branch_identity_verified_exact":True,
        "infinity_support_projective_limit_verified_exact":True,
    },
    "ruled_ambient_images":{
        "P_plus":{
            "A1":"-2*(1+sqrt(2))","A2":"2","X":"2*(1+sqrt(2))",
            "Y":"2*i*(1+sqrt(2))","X_plus_iY":"0",
        },
        "P_minus":{
            "A1":"-2*(1-sqrt(2))","A2":"2","X":"2*(1-sqrt(2))",
            "Y":"2*i*(1-sqrt(2))","X_plus_iY":"0",
        },
        "infinity_minus":{
            "homogeneous_representative":"(u1:v1,u2:v2)=([1:0],[1:0])",
            "A1":"-1","A2":"-1","X":"0","Y":"0",
            "warning":"This is a boundary/base-locus support for the ruled chart; do not assign a Stoll marked Kc point without the audited ruled-to-Kc morphism/resolution.",
        },
    },
    "exact_gap_after_this_leaf":{
        "cv_to_ruled_support_adapter_materialized":True,
        "j2_support_in_ruled_P1xP1_materialized":True,
        "ruled_support_to_stoll_marked_Kc_materialized":False,
        "j2_kc_discriminant_coordinate_materialized":False,
        "adapter_survivors_after_this_leaf":6,
        "reason":"The named J2 divisor is now located exactly in the frozen ruled coordinates, but the retained interface still lacks the resolved ruled-model-to-Stoll marked Kc divisor map needed to evaluate qPicK/imageinPicK and the discriminant glue.",
    },
    "next_exact_leaf":"MATERIALIZE_RESOLVED_RULED_P1xP1_TO_STOLL_MARKED_KC_DIVISOR_MAP_ON_THREE_J2_SUPPORTS_THEN_COMPUTE_J2_KC_KERNEL_LINE",
    "promotion_firewall":{
        "finite_v4_kummer_defect_columns_materialized":0,
        "arithmetic_hs_d2_computed":False,
        "stage33_12_closed":False,
        "stage33_07_closed":False,
        "stage33_08_released":False,
        "theorem_credit":False,
        "endpoint_credit":False,
        "perfect_cuboid_existence_claim":False,
        "perfect_cuboid_nonexistence_claim":False,
    },
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "adapter": cert["exact_coordinate_identification"]["adapter"],
    "j2_support_in_ruled_P1xP1_materialized": True,
    "j2_kc_discriminant_coordinate_materialized": False,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
