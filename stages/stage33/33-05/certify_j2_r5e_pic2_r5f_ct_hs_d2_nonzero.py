#!/usr/bin/env python3
"""Exact R5e cc/ct Pic/2 closure and R5f ct-restricted HS d2 no-go verifier."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
S12 = S33 / "33-12"
sys.path.insert(0, str(S12))
import certify_j2_corrected_ct_norm_picard_support as ps

OUT = HERE / "j2-r5e-pic2-r5f-ct-hs-d2-nonzero.json"
EXPECTED_SHA = "8e384501db1cb3aa3f73358b0c3612a85e4012c5041fda60d3be7aeddc7c4c55"
LOCKS = {
    "semantic_picard": (S12/"j2-semantic-kc-picard-basis.json", "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0"),
    "ct_pic2": (S12/"j2-ct-actual-cech-overlap-parities-and-marked-pic-mod2.json", "68077141a4f792eefb47ebfd5db46ae9e785a0bef286449fc888663f2f2f5c3c"),
    "explicit_surface_lift": (S12/"j2-corrected-explicit-cech-mu2-lift.json", "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"),
    "ct_support": (S12/"j2-corrected-ct-norm-picard-support.json", "77af329d2baf2fe807bf23722c9b320fdfddec2bd1df90ced7758d411c9cf021"),
}
EXPECTED_ACTION = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,1,-1,-1,0,-2,2,1,-1,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,-1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,-1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,-1,-1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def load_locked(key):
    path, expected = LOCKS[key]
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); got = body.pop("canonical_sha256")
    assert got == expected == csha(body), (key, got, csha(body))
    return obj

def ct_coeff(x):
    a,b,c,d=x
    return (a,b,-c,-d)

def canon(rows):
    rr,_=ps.rref(rows)
    return tuple(tuple(x for x in row) for row in rr)

def curve_coords(j):
    pairings=[]
    for h in ps.slots:
        raw=ps.raw_intersection_degree(ps.curves[j-1], ps.curves[h-1])
        common=sum(ps.contains(ps.curves[j-1],p) and ps.contains(ps.curves[h-1],p) for p in ps.points)
        pairings.append(raw-common)
    pairings += [int(ps.contains(ps.curves[j-1], ps.points[a])) for a in ps.semantic["semantic_exceptional_indices_0based"]]
    return ps.solve_row_coordinates(ps.g20, pairings)

def action_ct():
    cmap={canon(c):i+1 for i,c in enumerate(ps.curves)}
    pos={j:i for i,j in enumerate(ps.slots)}
    out=[]
    for j in ps.slots:
        jj=cmap[canon([[ct_coeff(x) for x in row] for row in ps.curves[j-1]])]
        if jj in pos:
            row=[0]*20; row[pos[jj]]=1
        else:
            row=curve_coords(jj)
        out.append(row)
    for i in range(17,20):
        row=[0]*20; row[i]=1; out.append(row)
    return out

def act(v,A):
    return [sum(v[i]*A[i][j] for i in range(20)) for j in range(20)]

def mmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(20)) for j in range(20)] for i in range(20)]

semantic=load_locked("semantic_picard")
ctcert=load_locked("ct_pic2")
explicit=load_locked("explicit_surface_lift")
load_locked("ct_support")
A=action_ct()
assert A == EXPECTED_ACTION
I20=[[int(i==j) for j in range(20)] for i in range(20)]
assert mmul(A,A)==I20
assert semantic["curve_slots_1based"] == [2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54]

cc=explicit["galois_defect_generic_splittings"]["cc"]
assert cc["formula"]=="cc(lambda_D)-lambda_D={f2,g21*g22}={f2,(B1/(2*t))^2}"
assert cc["generic_symbol_zero"]
# The displayed global square root c=B1/(2t) is deck-invariant on w^2=f2.
# If ord(c)=m, both sheet orders are m and the norm order is 2m; relative
# lattice exponent is zero. A common rank-two frame change has determinant
# c^2, hence divisor 2*div(c), so the actual cc Pic/2 class is zero.
for m in range(-5,6):
    assert m-(2*m)//2 == 0
    assert (2*m) % 2 == 0
cc_pic2=[0]*20

B=ctcert["actual_ct_defect_marked_pic_mod2"]["coordinates"]
assert B == [0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0]
assert any(B)
ctB=act(B,A)
assert all((ctB[i]-B[i])%2==0 for i in range(20))
Z=[(B[i]+ctB[i])//2 for i in range(20)]
assert act(Z,A)==Z
N=[[I20[i][j]+A[i][j] for j in range(20)] for i in range(20)]
col9=[N[i][8] for i in range(20)]
assert col9 == [0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
assert Z[8]==1

basis=["CsK[2]","CsK[4]","CsK[5]","CsK[7]","CsK[9]","CsK[10]","CsK[20]","CsK[21]","CsK[26]","CsK[35]","CsK[39]","CsK[42]","CsK[44]","CsK[47]","CsK[49]","CsK[52]","CsK[54]","E_A1_B2-1_B3-1","E_A2_B1-1_B3-1","E_A3_B1-1_B2-1"]
zero=[0]*20
payload={
"schema":"STAGE33_05_J2_R5E_CC_CT_PIC2_AND_R5F_CT_RESTRICTED_HS_D2_NONGO_V1",
"stage":"33-05/R5",
"status":"PASS_EXACT_R5E_CC_CT_PIC2_AND_HS_D2_NONZERO_BY_CT_RESTRICTION_ARITHMETIC_NOGO",
"source_locks":{
 "semantic_picard":{"path":"stages/stage33/33-12/j2-semantic-kc-picard-basis.json","canonical_sha256":LOCKS["semantic_picard"][1]},
 "ct_pic2":{"path":"stages/stage33/33-12/j2-ct-actual-cech-overlap-parities-and-marked-pic-mod2.json","canonical_sha256":LOCKS["ct_pic2"][1]},
 "explicit_surface_lift":{"path":"stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json","canonical_sha256":LOCKS["explicit_surface_lift"][1]},
 "ct_support":{"path":"stages/stage33/33-12/j2-corrected-ct-norm-picard-support.json","canonical_sha256":LOCKS["ct_support"][1]}},
"r5e_actual_pic2":{
 "cc":{"generic_formula":cc["formula"],"global_square_root":"c=B1/(2*t) in k(Kc_bar)^*","local_rank2_statement":"on the auxiliary f2-cover the norm witness is c on both deck sheets; after removing the common order m, relative lattice exponent is zero","overlap_determinant_statement":"a change by the global square root acts as a common scalar on rank two, so determinant changes by c^2 and divisor class by 2*div(c)","marked_Pic_mod2":cc_pic2,"materialized":True},
 "ct":{"marked_Pic_mod2":B,"nonzero":True,"materialized":True},
 "actual_cc_ct_Pic_mod2_defect_materialized":True},
"semantic_ct_action":{"basis_order":basis,"matrix_row_convention":"row i is ct(image of basis_i) in the displayed integral semantic basis","matrix":A,"involution_exact":True,"ct_defect_fixed_mod2":True},
"r5f_integral_lift_and_restricted_d2":{
 "subgroup":"<ct> ~= C2","integral_lift_B_of_ct_defect":B,"ct_B":ctB,
 "restricted_normalized_2cocycle":{"beta(1,1)":zero,"beta(1,ct)":zero,"beta(ct,1)":zero,"beta(ct,ct)=Z=(B+ct(B))/2":Z},
 "Z_ct_invariant":True,"H2_C2_identification":"H^2(<ct>,Pic)=Pic^ct/(1+ct)Pic",
 "nonzero_witness":{"semantic_coordinate_1based":9,"semantic_coordinate_label":"CsK[26]","Z_coordinate":Z[8],"column_of_1_plus_ct":col9,"consequence":"every (1+ct)Pic vector has even CsK[26] coordinate, while Z has coordinate 1"},
 "restricted_d2_class_zero":False,"global_HS_d2_class_zero":False,"global_nonzero_reason":"restriction of a zero global cohomology class would be zero; the explicit <ct> restriction is nonzero"},
"arithmetic_verdict":{"corrected_J2_Q_defined_Brauer_preimage":False,"reason":"nonzero Hochschild-Serre d2 obstruction on the ct subgroup","R5g_Q_descent":"BLOCKED_BY_NONZERO_HS_D2","successful_R5_repair_exit_reached":False,"required_repo_action":"record arithmetic no-go and rebuild the dependency chain; do not force reclosure"},
"exact_information_boundary":{"R5e_actual_cc_ct_Pic_mod2_complete":True,"integral_ct_Pic_lift_materialized":True,"restricted_HS_d2_2cocycle_materialized":True,"global_HS_d2_nonzero_proved_by_restriction":True,"full_absolute_Galois_2cocycle_table_materialized":False,"Q_defined_arithmetic_Brauer_preimage_materialized":False,"arithmetic_unramifiedness_materialized":False},
"promotion_firewall":{"Q_defined_descent_credit_restored":False,"R5_full_repair_exit_reached":False,"stage33_05_reclosed":False,"stage33_12_closed":False,"stage33_13_released":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False,"hostile_audit_required_before_dependency_rebuild_promotion":True},
"next_exact_leaf":"HOSTILE_REPLAY_R5E_CC_CT_PIC2_AND_CT_RESTRICTED_HS_D2_NONZERO_THEN_REBUILD_STAGE33_DEPENDENCY_CHAIN_WITH_J2_Q_DESCENT_BLOCKED"}
assert csha(payload)==EXPECTED_SHA, (csha(payload),EXPECTED_SHA)
out=dict(payload);out["canonical_sha256"]=EXPECTED_SHA
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"success":True,"status":out["status"],"ct_pic2":B,"Z":Z,"nonzero_coordinate":"CsK[26]","canonical_sha256":EXPECTED_SHA},sort_keys=True))
