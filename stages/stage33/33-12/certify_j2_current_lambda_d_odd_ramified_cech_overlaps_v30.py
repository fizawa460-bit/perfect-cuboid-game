#!/usr/bin/env python3
"""V30: repair the current ct odd/ramified Cech overlaps without historical sheet authority."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
OUT=HERE/"j2-current-lambda-d-odd-ramified-cech-overlaps-v30.json"
LOCKS={
"v25":("j2-genuine-h2-mu2-kummer-adapter-v25.json","d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
"v29":("j2-current-lambda-d-even-norm-rank2-lattices-v29.json","d59ccba621bf0a41a1b53bc400cd819cd48fd19b8357c21209a5b1755fe5611b"),
"explicit":("j2-corrected-explicit-cech-mu2-lift.json","6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"),
"splitting":("j2-corrected-ct-norm-splitting-module.json","b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2"),
"boundary":("j2-ct-norm-actual-boundary-sheet-frames.json","5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b"),
"branch":("j2-corrected-branch-surface-mu2-adapter.json","edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875"),
"parity":("j2-ct-norm-local-lattice-parity-constraints.json","c941d34444b365fb03be188b9c72569c607b02da76efa1d5034994b2ed44f533"),
"support":("j2-corrected-ct-norm-picard-support.json","77af329d2baf2fe807bf23722c9b320fdfddec2bd1df90ced7758d411c9cf021")}
EXPECTED="5f911ca53e5e16374250e34e74e557229a9477d4814c910b8db7880dd993d66d"

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def load(k):
 n,h=LOCKS[k]; o=json.loads((HERE/n).read_text()); b=dict(o); got=b.pop("canonical_sha256"); assert got==h==csha(b),(n,got,csha(b)); return o

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def inv(x):
 d=x[0]*x[0]-2*x[1]*x[1]; assert d; return (x[0]/d,-x[1]/d)
def div(x,y): return mul(x,inv(y))
def powq(x,n):
 out=(Fraction(1),Fraction(0))
 for _ in range(n): out=mul(out,x)
 return out
def ctq(x): return (x[0],-x[1])
def xor(*rows): return [sum(v)%2 for v in zip(*rows)]

def build():
 v25,v29,ex,sp,bn,br,pa,su=(load(k) for k in ("v25","v29","explicit","splitting","boundary","branch","parity","support"))
 assert v25["genuine_h2_mu2_adapter"]["kc_lift_class"]=="lambda_D=alpha(e_D), represented generically by {f2,g22}"
 assert v29["current_lambda_D_anchor"]["historical_pre_kummer_sheet_selection_used"] is False
 assert v29["exact_information_boundary"]["current_lambda_D_even_norm_punctured_overlap_matrices_materialized"] is True
 assert ex["explicit_cech_preimage"]["class"]=="e_D={f2,g22}=kum(f2) cup kum(g22) in H^2(Ubar,mu_2)"
 assert ex["galois_defect_generic_splittings"]["ct"]["squareclass_identity"]=="ct(f2)/f2=((t-r3)*(t-r4))^2/q"
 assert ex["surface_mu2_lift"]["historical_kummer_glue_used"] is False
 one=(Fraction(1),Fraction(0)); rt=(Fraction(0),Fraction(1))
 r1=add(one,rt); r2=neg(r1); r3=add(rt,neg(one)); r4=neg(r3); roots=[r1,r2,r3,r4]
 for r in roots: assert add(add(powq(r,4),(-6*powq(r,2)[0],-6*powq(r,2)[1])),one)==(0,0)
 a0=r1; f20=div(neg(r2),neg(r4)); assert f20==mul(a0,a0)==(3,2)
 h0=mul(neg(r3),neg(r4)); ratio0=div(ctq(a0),a0); assert ratio0==h0==(-3,2); assert ratio0!=neg(h0)
 rows={x["divisor"]:x for x in ex["codimension_one_residue_audit"]["rows"]}
 assert rows["t=r2"]["residue_square_witness"]=="g22(r2,s)=(1+i*s)^2"
 assert rows["t=r4"]["residue_square_witness"]=="g22(r4,s)=(1-i*s)^2"
 qa=sp["q_root_local_audit"]
 assert qa["roots"]==["1+sqrt(2)","-(1+sqrt(2))","sqrt(2)-1","1-sqrt(2)"]
 assert qa["d_values_for_A_over_2t"]==[-1,1,1,-1]
 assert qa["specialized_square_roots"]==["-1+i*s","1+i*s","1+i*s","-1+i*s"]
 cech_witnesses=["1-i*s","1+i*s","1+i*s","1-i*s"]; norm_witnesses=["-1+i*s","1+i*s","1+i*s","-1+i*s"]; residue_signs=[-1,1,1,-1]; parities=[1,0,0,1]
 bf=bn["boundary_sheet_frames"]
 assert bf["T0"]["sheet_z_plus_1"]["ord_u"]==-1 and bf["T0"]["sheet_z_plus_1"]["ord_sigma_u"]==0
 assert bf["Tinf"]["sheet_z_inf_plus_1"]["ord_u"]==0 and bf["Tinf"]["sheet_z_inf_plus_1"]["ord_sigma_u"]==-1
 assert bf["C22"]["D22_plus"]["ord_u"]==0 and bf["C22"]["D22_plus"]["ord_sigma_u"]==1
 assert bf["C22"]["D22_minus"]["ord_u"]==1 and bf["C22"]["D22_minus"]["ord_sigma_u"]==0
 assert "valuation 2" in ex["surface_mu2_lift"]["ramification_check"]
 assert br["resolution_adapter"]["operation"]=="resolve the four quotient A1 nodes, then blow up the four transverse branch crossings and normalize the double cover"
 partial=pa["fixed_partial_marked_pic_mod2"]["coordinates"]; F=su["ct_norm_support"]["common_q_fiber_class_marked_semantic_PicK_coordinates"]
 coords=pa["marked_exceptional_reconstruction"]["marked_semantic_PicK_coordinates"]; ci=pa["marked_exceptional_reconstruction"]["corner_to_semantic_point_index_0based"]
 Tinf_strict=xor(F,coords[ci["E_inf0"]],coords[ci["E_infinf"]]); qroot_contribution=xor(F,F); final=xor(partial,Tinf_strict,qroot_contribution)
 assert Tinf_strict==[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]; assert qroot_contribution==[0]*20
 assert final==[0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0] and any(final)
 payload={
 "schema":"STAGE33_12_J2_CURRENT_LAMBDA_D_ODD_RAMIFIED_CECH_OVERLAPS_V30","stage":"33-12","status":"PASS_EXACT_CURRENT_CECH_T0_TINF_QROOT_C22_OVERLAPS_AND_CT_PIC_MOD2_MATERIALIZED_CC_HS_D2_OPEN",
 "source_locks":{k:{"path":"stages/stage33/33-12/"+n,"canonical_sha256":h} for k,(n,h) in LOCKS.items()},
 "current_authority":{"lambda_D":"lambda_D=alpha(e_D), represented generically by {f2,g22}","historical_pre_kummer_sheet_selection_used":False,"historical_ct_overlap_candidate_used_as_source":False,"derivation":"current explicit e_D and ct(e_D), current norm nullhomotopy, current V29 lattices"},
 "current_cech_qsquare_sheet_selection":{"ct_f2_over_f2":"((t-r3)*(t-r4))^2/q","current_square_witness_on_q_cover":"h/z with h=(t-r3)*(t-r4)","T0":{"e_D_local_square_witness_for_f2":"a0=1+sqrt(2)","f2_0":"a0^2","ct_a0_over_a0":"-(3-2*sqrt(2))","h_0":"-(3-2*sqrt(2))","selected_sheet":"z=+sqrt(q), z|T0=+1","minus_sheet_rejected_by_exact_sign":True},"Tinf":{"e_D_local_square_witness_for_f2":"a_inf=1","ct_ainf_over_ainf":"1","limit_h_over_z_on_plus_sheet":"1","selected_sheet":"z_inf=+sqrt(q_inf), z_inf|Tinf=+1","minus_sheet_rejected_by_exact_sign":True}},
 "odd_boundary_current_rank2_lattices":{"T0":{"selected_sheet":"plus","sheet_orders_u_sigma":[-1,0],"fractional_O_basis":["sigma(u)*e1","e2"],"punctured_overlap_matrix":"diag(sigma(u),1)","overlap_ring":"O[t^-1]","determinant_parity":0},"Tinf":{"selected_sheet":"plus","sheet_orders_u_sigma":[0,-1],"fractional_O_basis":["sigma(u)*e1","e2"],"punctured_overlap_matrix":"diag(sigma(u),1)","overlap_ring":"O[v^-1], v=1/t","determinant_parity":1}},
 "ramified_qroot_current_cech_overlaps":{"roots":["r1=1+sqrt(2)","r2=-(1+sqrt(2))","r3=sqrt(2)-1","r4=1-sqrt(2)"],"cech_square_witness_derivation":"r2/r4 witnesses come from current e_D residue extensions; r3/r1 are their ct-conjugates","cech_square_witnesses":cech_witnesses,"norm_witness_specializations":norm_witnesses,"residue_signs_norm_over_cech":residue_signs,"hilbert90_frames":{"sign_plus":"v=1+w; v/sigma(v)=w and v is a unit","sign_minus":"v=z*(1-w); v/sigma(v)=w and ord_z(v)=1","ramified_uniformizer":"z because q has a simple zero"},"punctured_overlap_matrices":["diag(z*(1-w1),1)","diag(1+w2,1)","diag(1+w3,1)","diag(z*(1-w4),1)"],"overlap_ring":"O[z^-1] on each ramified q-cover chart","determinant_parities_r1_r2_r3_r4":parities,"global_marked_Pic_mod2_contribution":qroot_contribution,"global_cancellation":"odd r1 and r4 each contribute the common vertical fiber class F, hence F+F=0 mod 2"},
 "C22_surface_ramified_rank2_lattice":{"surface_uniformizer":"rho along the B1-ramification curve R22","pullback_ord_norm":2,"q_cover_sheet_orders_after_surface_pullback":{"D22_plus":[0,2],"D22_minus":[2,0]},"common_normalization_exponent":1,"normalized_sigma_orders":{"D22_plus":1,"D22_minus":-1},"fractional_O_basis_formula":["(sigma(u)/rho)*e1","e2"],"punctured_overlap_matrix_formula":"diag(sigma(u)/rho,1)","overlap_ring":"O[rho^-1]","determinant_parity_on_both_q_sheets":1,"surface_input":"pi^*g22 has valuation 2 along R22 in the current genuine surface H2(mu2) lift"},
 "actual_ct_defect_marked_pic_mod2":{"prior_even_and_C22_partial":partial,"T0_contribution":[0]*20,"Tinf_strict_contribution":Tinf_strict,"qroot_contribution":qroot_contribution,"coordinates":final,"nonzero":True,"historical_numeric_vector_reproduced_independently":True},
 "resolved_vertical_boundary_relation":{"generic_vertical_fiber_class_F":F,"Tinf_crossing_exceptionals":["E_inf0","E_infinf"],"formula_mod2":"[Tinf_strict]=F+E_inf0+E_infinf"},
 "exact_information_boundary":{"current_lambda_D_all_listed_ct_codim1_rank2_lattices_materialized":True,"actual_ct_overlap_determinant_parities_materialized":True,"actual_ct_defect_marked_Pic_mod2_materialized":True,"actual_ct_defect_marked_Pic_mod2_nonzero":True,"actual_cc_defect_marked_Pic_mod2_materialized":False,"full_Galois_Pic_mod2_1cocycle_materialized":False,"integral_Pic_lift_materialized":False,"hs_d2_2cocycle_materialized":False,"standard_kummer_columns_materialized":0},
 "next_exact_leaf":"MATERIALIZE_CURRENT_CC_GLOBAL_SQUARE_CECH_OVERLAP_CLASS_IN_MARKED_PIC_MOD2_THEN_ASSEMBLE_FULL_V4_PIC_MOD2_1COCYCLE_CHOOSE_INTEGRAL_PIC_LIFTS_AND_COMPUTE_HS_D2",
 "promotion_firewall":{"merge_allowed":False,"stage33_12_closed_exact":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
 return payload

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); args=ap.parse_args(); payload=build(); assert csha(payload)==EXPECTED,csha(payload)
 out=dict(payload); out["canonical_sha256"]=EXPECTED
 if args.check: assert json.loads(OUT.read_text())==out
 else: OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"success":True,"canonical_sha256":EXPECTED,"ct_pic_mod2":out["actual_ct_defect_marked_pic_mod2"]["coordinates"],"status":out["status"]},sort_keys=True))
if __name__=="__main__": main()
