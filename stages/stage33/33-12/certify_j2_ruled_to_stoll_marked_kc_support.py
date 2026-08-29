#!/usr/bin/env python3
"""Exact J2 support bridge from the audited ruled model to Stoll's marked K_c model."""
import hashlib, json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
r2 = sp.sqrt(2)
i = sp.I
u1,v1,u2,v2 = sp.symbols("u1 v1 u2 v2")
A1,A2,A3,B1,B2,B3 = sp.symbols("A1 A2 A3 B1 B2 B3")

D1 = v1**2-u1**2
D2 = v2**2-u2**2
e = sp.expand(D1*D2)
x = sp.expand(2*u1*v1*D2)
p = sp.expand((u1**2+v1**2)*D2)
y = sp.expand(2*u2*v2*D1)
q = sp.expand((u2**2+v2**2)*D1)
assert sp.expand(e**2+x**2-p**2) == 0
assert sp.expand(e**2+y**2-q**2) == 0

# Stoll K_c coordinates are (A1,A2,A3,B1,B2,B3)=(e,x,y,z,q,p).
K_eqs = [A1**2+A2**2-B3**2, A2**2+A3**2-B1**2, A1**2+A3**2-B2**2]
varsK = [A1,A2,A3,B1,B2,B3]
J = sp.Matrix([[sp.diff(f,v) for v in varsK] for f in K_eqs])

def affine_image(t,s):
    vals = [sp.simplify(f.subs({u1:t,v1:1,u2:s,v2:1})) for f in [e,x,y,q,p]]
    return vals[:3] + [sp.Integer(0)] + vals[3:]

def normalize_by_A2(P):
    return [sp.simplify(a/P[1]) for a in P]

Pplus = normalize_by_A2(affine_image(1+r2,-i))
Pminus = normalize_by_A2(affine_image(1-r2,-i))
Pinf = [sp.Integer(1),0,0,0,-1,-1]
assert Pplus == [-1,1,i,0,0,r2]
assert Pminus == [-1,1,i,0,0,-r2]

for P,rank in ((Pplus,3),(Pminus,3),(Pinf,2)):
    sub = dict(zip(varsK,P))
    assert all(sp.simplify(f.subs(sub)) == 0 for f in K_eqs)
    assert J.subs(sub).rank() == rank

# B+ : X+iY=0; x=2X,y=2Y and z^2=x^2+y^2, hence z=0.
# In Stoll coordinates: B1=0 and i*A2-A3=0, namely C2sK[2]=CsK[22].
for P in (Pplus,Pminus,Pinf):
    sub=dict(zip(varsK,P))
    assert sp.simplify(B1.subs(sub)) == 0
    assert sp.simplify((i*A2-A3).subs(sub)) == 0

# Resolve the infinity singularity geometrically.  In the A1=1 chart write
# a=A2, b=A3, c=B1.  Eliminating B2,B3 to quadratic order leaves the A1
# tangent cone c^2=a^2+b^2.  The marked B+ branch has c=0, i*a-b=0,
# so its strict transform meets the exceptional conic in [a:b:c]=[1:i:0].
a,b,c=sp.symbols("a b c")
tangent_cone = sp.expand(c**2-a**2-b**2)
assert sp.simplify(tangent_cone.subs({a:1,b:i,c:0})) == 0

cert = {
  "schema":"STAGE33_12_J2_RULED_TO_STOLL_MARKED_KC_SUPPORT_V2",
  "source_locks":{
    "stage29_07_sign_tower_adapter_git_blob_sha1":"82f039ab9ff793598ddb0b2a02808b92364c7046",
    "stage33_12_cv_to_ruled_canonical_sha256":"63c09f6ac52cef43d529d17a48907b5818cb19d18efcced3aa35e1ccc080b061",
    "stoll_upstream_git_blob_sha1":"0422b69847f2afb97cb7b3ed02ebef91279f61b1",
    "stage33_07_kc_discriminant_derivation_git_blob_sha1":"62724b75eba42bf980574b4b57b936775a1a893c"
  },
  "anticanonical_map":{
    "D1":"v1^2-u1^2","D2":"v2^2-u2^2","e":"D1*D2",
    "x":"2*u1*v1*D2","p":"(u1^2+v1^2)*D2",
    "y":"2*u2*v2*D1","q":"(u2^2+v2^2)*D1",
    "stoll_coordinate_identification":["A1=e","A2=x","A3=y","B1=z","B2=q","B3=p"],
    "prior_frozen_relation":["x=2*X","y=2*Y","z=2*w"]
  },
  "branch_component":{
    "cv_equation":"X+i*Y=0",
    "stoll_equations":["B1=0","i*A2-A3=0"],
    "stoll_known_curve_family":"C2sK",
    "stoll_known_curve_family_index_1based":2,
    "stoll_CsK_index_1based":22,
    "marked_curve_identified_exactly":True
  },
  "j2_support_images":{
    "P_plus":{"ruled":["[1+sqrt(2):1]","[-i:1]"],"stoll":["-1","1","i","0","0","sqrt(2)"],"jacobian_rank":3,"smooth_on_Kc":True},
    "P_minus":{"ruled":["[1-sqrt(2):1]","[-i:1]"],"stoll":["-1","1","i","0","0","-sqrt(2)"],"jacobian_rank":3,"smooth_on_Kc":True},
    "infinity_minus":{"ruled":["[1:0]","[1:0]"],"stoll":["1","0","0","0","-1","-1"],"jacobian_rank":2,"singular_on_Kc":True}
  },
  "j2_infinity_resolution":{
    "singular_point_stoll":["1","0","0","0","-1","-1"],
    "affine_chart":"A1=1",
    "local_tangent_cone":"c^2=a^2+b^2 with a=A2, b=A3, c=B1",
    "branch_tangent_equations":["c=0","i*a-b=0"],
    "exceptional_conic_attachment_direction":["1","i","0"],
    "geometric_exceptional_attachment_materialized":True,
    "stoll_ptsK_order_index_materialized":False,
    "qPicK_exceptional_coordinate_materialized":False
  },
  "three_support_images_materialized":True,
  "infinity_resolved_exceptional_attachment_materialized":True,
  "branch_jacobian_2torsion_to_picard_discriminant_kummer_glue_materialized":False,
  "J2_kc_discriminant_coordinate_materialized":False,
  "J2_q1_kc_adapter_unique":False,
  "GL2_F2_adapter_survivors":6,
  "finite_v4_kummer_defect_matrix_shape":[75,10],
  "finite_v4_kummer_defect_columns_materialized":0,
  "next_exact_leaf":"MATERIALIZE_STOLL_PTSK_INDEX_AND_QPICK_COORDINATE_FOR_J2_INFINITY_EXCEPTIONAL_THEN_BRANCH_JACOBIAN_2TORSION_TO_KC_PICARD_DISCRIMINANT_KUMMER_GLUE",
  "theorem_credit":False,"endpoint_credit":False,
  "perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False
}
raw = json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
(ROOT/"j2-ruled-to-stoll-marked-kc-support.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"certificate_sha256":cert["canonical_sha256"],"marked_curve":"CsK[22]","infinity_singular":True,"exceptional_attachment":"[1:i:0]","next_exact_leaf":cert["next_exact_leaf"]},indent=2,sort_keys=True))
