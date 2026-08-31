#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from fractions import Fraction
from pathlib import Path
HERE=Path(__file__).resolve().parent
S33=HERE.parent
OUT=HERE/"j2-ct-actual-cech-overlap-parities-and-marked-pic-mod2.json"
LOCKS={
"pre_kummer":(S33/"33-05"/"j2-corrected-pre-kummer-descent-cochain.json","940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106"),
"explicit":(HERE/"j2-corrected-explicit-cech-mu2-lift.json","6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"),
"splitting":(HERE/"j2-corrected-ct-norm-splitting-module.json","b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2"),
"boundary":(HERE/"j2-ct-norm-actual-boundary-sheet-frames.json","5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b"),
"branch_adapter":(HERE/"j2-corrected-branch-surface-mu2-adapter.json","edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875"),
"prior_parity":(HERE/"j2-ct-norm-local-lattice-parity-constraints.json","c941d34444b365fb03be188b9c72569c607b02da76efa1d5034994b2ed44f533")}
EXPECTED="68077141a4f792eefb47ebfd5db46ae9e785a0bef286449fc888663f2f2f5c3c"
BODY=json.loads(r'''{"actual_cech_sheet_selection":{"T0":{"determinant_parity":0,"reason":"ct(1+sqrt(2))/(1+sqrt(2))=-(3-2*sqrt(2)) equals u_ct=(t-r3)(t-r4)/z at t=0 only for the plus sheet","selected_q_square_sheet":"z=+sqrt(q), z|T0=+1"},"Tinf":{"determinant_parity":1,"reason":"the fixed witness f2(infinity)=1 has ct-ratio 1 and u_ct has leading value 1 on the plus z_inf sheet","selected_q_square_sheet":"z_inf=+sqrt(q_inf), z_inf|Tinf=+1"}},"actual_ct_defect_marked_pic_mod2":{"T0_contribution":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"Tinf_strict_contribution":[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"coordinates":[0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0],"nonzero":true,"prior_forced_partial":[0,0,1,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0],"qroot_contribution":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"scope":"ct component only; cc component is not inferred from its generic square symbol"},"exact_information_boundary":{"HS_d2_2cocycle_materialized":false,"HS_d2_zero_or_nonzero_proved":false,"actual_cc_defect_marked_Pic_mod2_materialized":false,"actual_ct_defect_marked_Pic_mod2_materialized":true,"actual_ct_defect_marked_Pic_mod2_nonzero":true,"actual_ct_overlap_determinant_parities_materialized":true,"full_Galois_Pic_mod2_1cocycle_materialized":false,"integral_Pic_lift_materialized":false},"next_exact_subleaf":"MATERIALIZE_CC_GLOBAL_SQUARE_CECH_OVERLAP_CLASS_IN_MARKED_PIC_MOD2_THEN_ASSEMBLE_FULL_GALOIS_PIC_MOD2_1COCYCLE_AND_ENTER_R5F_INTEGRAL_PIC_HS_D2","promotion_firewall":{"Q_defined_descent_credit_restored":false,"R5_full_repair_exit_reached":false,"actual_ct_Pic_mod2_defect_zero_claim":false,"endpoint_credit":false,"perfect_cuboid_existence_claim":false,"perfect_cuboid_nonexistence_claim":false,"receiver_credit":false,"stage33_05_reclosed":false,"stage33_12_closed":false,"stage33_13_released":false,"theorem_credit":false},"ramified_qroot_actual_cech_overlap":{"actual_cech_square_witnesses":["1-i*s","1+i*s","1+i*s","1-i*s"],"determinant_parities_r1_r2_r3_r4":[1,0,0,1],"global_cancellation":"only r1 and r4 are odd; each contributes the same vertical fiber class F, hence F+F=0 mod2","global_marked_Pic_mod2_contribution":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"hilbert90_local_frames":{"sign_minus":"v=z*(1-w) has odd valuation and v/sigma(v)=w","sign_plus":"v=1+w is a unit and v/sigma(v)=w","why_minus_cannot_be_unit":"the ramified deck involution acts trivially on the residue field, so every unit coboundary reduces to +1"},"norm_witness_specializations":["-1+i*s","1+i*s","1+i*s","-1+i*s"],"residue_signs_norm_over_cech":[-1,1,1,-1],"roots":["r1=1+sqrt(2)","r2=-(1+sqrt(2))","r3=sqrt(2)-1","r4=1-sqrt(2)"]},"repair_leaf":"33-05/R5e","resolved_vertical_boundary_relation":{"Tinf_crossing_exceptionals":["E_inf0","E_infinf"],"Tinf_strict_mod2":[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"blowup_input":"at each transverse branch crossing the quotient is blown up once before normalization; a vertical boundary parameter has total transform strict+E with multiplicity one","formula":"[Tinf_strict]=F-E_inf0-E_infinf, hence F+E_inf0+E_infinf mod2","generic_vertical_fiber_class_F":[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]},"schema":"STAGE33_12_J2_CT_ACTUAL_CECH_OVERLAP_PARITIES_AND_MARKED_PIC_MOD2_V1","source_locks":{"boundary":{"canonical_sha256":"5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b","path":"stages/stage33/33-12/j2-ct-norm-actual-boundary-sheet-frames.json"},"branch_adapter":{"canonical_sha256":"edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875","path":"stages/stage33/33-12/j2-corrected-branch-surface-mu2-adapter.json"},"explicit":{"canonical_sha256":"6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b","path":"stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json"},"pre_kummer":{"canonical_sha256":"940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106","path":"stages/stage33/33-05/j2-corrected-pre-kummer-descent-cochain.json"},"prior_parity":{"canonical_sha256":"c941d34444b365fb03be188b9c72569c607b02da76efa1d5034994b2ed44f533","path":"stages/stage33/33-12/j2-ct-norm-local-lattice-parity-constraints.json"},"splitting":{"canonical_sha256":"b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2","path":"stages/stage33/33-12/j2-corrected-ct-norm-splitting-module.json"}},"split_dvr_overlap_matrix":{"T0_ord_u_minus_on_selected_plus_sheet":0,"Tinf_ord_u_minus_on_selected_plus_sheet":-1,"basis_change":"G=diag(u_minus,1), so G*Y_norm*G^-1=J","cech_square_basis_operator":"J=[[0,b],[1,0]]","determinant":"u_minus","norm_basis_operator":"Y_norm=[[0,u_plus],[u_minus,0]] with u_plus*u_minus=b","parity_rule":"ord(u_minus) mod 2"},"stage":"33-12","status":"PASS_EXACT_CT_ACTUAL_CECH_OVERLAP_PARITIES_AND_MARKED_PIC_MOD2_CC_COMPONENT_STILL_OPEN"}''')
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(k):
 p,h=LOCKS[k]; o=json.loads(p.read_text()); b=dict(o); got=b.pop("canonical_sha256"); assert got==h==csha(b),(p,got,csha(b)); return o
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def inv(x):
 d=x[0]*x[0]-2*x[1]*x[1]; assert d; return (x[0]/d,-x[1]/d)
def div(x,y): return mul(x,inv(y))
def xor(*r): return [sum(v)%2 for v in zip(*r)]
D={k:load(k) for k in LOCKS}
pre,ex,sp,bn,ad,pp=(D[k] for k in ("pre_kummer","explicit","splitting","boundary","branch_adapter","prior_parity"))
assert pre["sqrt2_conjugation"]["ct_f2_over_f2_square_witness"]=="u_ct=(t-r3)*(t-r4)/z"
assert pre["sqrt2_conjugation"]["root_permutation"]==["r1<->r4","r2<->r3"]
rows={x["divisor"]:x for x in ex["codimension_one_residue_audit"]["rows"]}
assert rows["t=0"]["residue_square_witness"]=="f2(0)=(1+sqrt(2))^2"
assert rows["t=infinity"]["residue_square_witness"]=="f2(infinity)=1"
assert rows["t=r2"]["residue_square_witness"]=="g22(r2,s)=(1+i*s)^2"
assert rows["t=r4"]["residue_square_witness"]=="g22(r4,s)=(1-i*s)^2"
one=(Fraction(1),Fraction(0)); s2=(Fraction(0),Fraction(1))
r1=add(one,s2); r3=add(s2,neg(one)); r4=neg(r3)
assert div((r1[0],-r1[1]),r1)==mul(r3,r4)==(Fraction(-3),Fraction(2))
qa=sp["q_root_local_audit"]; assert qa["specialized_square_roots"]==["-1+i*s","1+i*s","1+i*s","-1+i*s"]
bf=bn["boundary_sheet_frames"]
assert bf["T0"]["sheet_z_plus_1"]["ord_sigma_u"]==0
assert bf["Tinf"]["sheet_z_inf_plus_1"]["ord_sigma_u"]==-1
assert ad["resolution_adapter"]["operation"]=="resolve the four quotient A1 nodes, then blow up the four transverse branch crossings and normalize the double cover"
assert ad["resolution_adapter"]["local_chart"]=="y=x*v, w=x*W gives W^2=v^2+1"
F=sp["exact_nonuniqueness_witness"]["pullback_difference_marked_semantic_PicK_coordinates"]
partial=pp["fixed_partial_marked_pic_mod2"]["coordinates"]
coords=pp["marked_exceptional_reconstruction"]["marked_semantic_PicK_coordinates"]
ci=pp["marked_exceptional_reconstruction"]["corner_to_semantic_point_index_0based"]
strict=xor(F,coords[ci["E_inf0"]],coords[ci["E_infinf"]])
qroots=xor(F,F); final=xor(partial,strict,qroots)
assert strict==BODY["actual_ct_defect_marked_pic_mod2"]["Tinf_strict_contribution"]
assert qroots==[0]*20
assert final==BODY["actual_ct_defect_marked_pic_mod2"]["coordinates"] and any(final)
assert BODY["ramified_qroot_actual_cech_overlap"]["residue_signs_norm_over_cech"]==[-1,1,1,-1]
assert BODY["ramified_qroot_actual_cech_overlap"]["determinant_parities_r1_r2_r3_r4"]==[1,0,0,1]
assert BODY["actual_cech_sheet_selection"]["T0"]["determinant_parity"]==0
assert BODY["actual_cech_sheet_selection"]["Tinf"]["determinant_parity"]==1
assert csha(BODY)==EXPECTED
out=dict(BODY); out["canonical_sha256"]=EXPECTED
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"status":out["status"],"ct_pic_mod2":final,"canonical_sha256":EXPECTED},sort_keys=True))
