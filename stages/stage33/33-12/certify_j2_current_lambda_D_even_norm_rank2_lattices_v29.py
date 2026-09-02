#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
OUT=HERE/"j2-current-lambda-D-even-norm-rank2-lattices-v29.json"
LOCKS={
"v25":(HERE/"j2-genuine-h2-mu2-kummer-adapter-v25.json","d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
"explicit":(HERE/"j2-corrected-explicit-cech-mu2-lift.json","6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"),
"v27":(HERE/"j2-ct-norm-splitting-boundary-valuations-v27.json","355c2a6dcb27f163ba6236a4e6790f090d03dbd7e74c89d76c2cf7a5c2e1ccc4"),
"boundary":(HERE/"j2-ct-norm-actual-boundary-sheet-frames.json","5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b"),
"exceptionals":(HERE/"j2-ct-norm-resolution-exceptional-sheet-frames.json","bbde421a54d2b7159f8d3ff4cf641cbddf2bbbc45fe4791cb7ed18d7cfb69591"),
"v28":(HERE/"j2-post-v27-exceptional-overlap-inheritance-audit-v28.json","919c1fd1dfb57f0e86677e64052636918082d7ef0cf9a9f79afe51051eb96095")}
EXPECTED="4a37679fba5ef820595a3508dd3aaed674374e931c5375d4ba2c2f4541d99cd5"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def locked(p,h):
 o=json.loads(p.read_text()); b=dict(o); got=b.pop("canonical_sha256"); assert got==h==csha(b),(p,got,csha(b)); return o
def row(label,pi,k,ou,osig,chart,sheet):
 assert k%2==0; half=k//2; s0=osig-half; u0=ou-half; assert u0+s0==0
 scalar=f"{pi}^({-half})*sigma(u)"
 return [label,chart,sheet,pi,ou,osig,k,f"({scalar})*e1","e2",scalar,"0","0","1",s0,s0%2,f"O[{pi}^-1]"]
def build():
 d={k:locked(*v) for k,v in LOCKS.items()}; v25,ex,v27,bn,exc,v28=(d[k] for k in ("v25","explicit","v27","boundary","exceptionals","v28"))
 assert v25["genuine_h2_mu2_adapter"]["kc_lift_class"]=="lambda_D=alpha(e_D), represented generically by {f2,g22}"
 assert v25["current_named_source"]["retained10_mask_decimal"]==6 and v25["current_named_source"]["two_bit_value_a_b"]==[0,1]
 assert ex["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True and "valuation 2" in ex["surface_mu2_lift"]["ramification_check"]
 assert v27["norm_consistency"]["all_rows_satisfy_v_u_plus_v_deck_u_equals_v_g22"] is True
 assert v28["historical_overlap_promotion_audit"]["historical_candidate_inherited_as_current_authority"] is False
 bf=bn["boundary_sheet_frames"]; ef=exc["actual_ct_resolution_exceptional_sheet_frames"]
 rows=[row("C21","eta21",bf["C21"]["ord_norm"],0,0,"C21","generic"),row("Sinf","w",bf["Sinf"]["ord_norm"],-1,-1,"s=infinity","generic"),row("C22_ram","rho",2,0,2,"Kc ramification over C22","u-unit orientation")]
 for name in ("E_00","E_0inf","E_inf0","E_infinf"):
  for key,short in (("sheet_plus","plus"),("sheet_minus","minus")):
   x=ef[name]; s=x[key]; rows.append(row(f"{name}_{short}","e",x["ord_norm"],s["ord_u"],s["ord_sigma_u"],"resolution exceptional",short))
 q=exc["quotient_A1_exceptional_frames"]; assert [q["generic_ord_u_on_every_auxiliary_q_cover_component"],q["generic_ord_sigma_u_on_every_auxiliary_q_cover_component"],q["generic_ord_norm"]]==[0,0,0]
 for i in range(1,9): rows.append(row(f"Q_A1_{i}","e",0,0,0,"unbranched quotient-A1 exceptional",f"lift_{i}"))
 assert len(rows)==19
 parity={r[0]:r[14] for r in rows}; forced=v28["retainable_local_parity_constraints"]["forced_parities"]
 assert parity["C21"]==forced["C21"]==0 and parity["Sinf"]==forced["Sinf"]==0 and parity["C22_ram"]==forced["C22_on_Kc_ramification_pullback"]==1
 assert [parity["E_00_plus"],parity["E_00_minus"]]==[forced["E_00"]]*2
 assert [parity["E_0inf_plus"],parity["E_0inf_minus"]]==[forced["E_0inf"]]*2
 assert [parity["E_inf0_plus"],parity["E_inf0_minus"]]==[forced["E_inf0"]]*2
 assert [parity["E_infinf_plus"],parity["E_infinf_minus"]]==[forced["E_infinf"]]*2
 assert all(parity[f"Q_A1_{i}"]==0 for i in range(1,9))
 out={"schema":"STAGE33_12_J2_CURRENT_LAMBDA_D_EVEN_NORM_RANK2_LATTICES_V29","stage":"33-12","status":"PASS_CURRENT_LAMBDA_D_EVEN_NORM_RANK2_LATTICES_19_RECORDS_ODD_BOUNDARY_QROOT_OPEN","source_locks":{k:h for k,(_,h) in LOCKS.items()},"current_lambda_D":{"class":"lambda_D=alpha(e_D), generically {f2,g22}","retained10_mask":6,"two_bit":[0,1],"historical_overlap_used":False},"model":{"normalize":"k even: u0=pi^(-k/2)u, su0=pi^(-k/2)sigma(u), b0=pi^(-k)g22","operator":"Y0=[[0,u0],[su0,0]]","basis":"L=<su0*e1,e2>","transition":"G=diag(su0,1)","identity":"G*Y0*G^-1=[[0,b0],[1,0]]","det":"ord(det G)=ord(sigma(u))-k/2","ring":"G entries are in the declared punctured DVR overlap ring"},"local_rank2_lattice_table":{"columns":["label","chart","sheet","pi","ord_u","ord_sigma_u","ord_norm","basis1","basis2","G11","G12","G21","G22","ord_det","det_mod2","overlap_ring"],"rows":rows},"checks":{"record_count":19,"forced_parities":{"C21":0,"Sinf":0,"C22_ram":1,"E_00":[1,1],"E_0inf":[0,0],"E_inf0":[1,1],"E_infinf":[0,0],"Q_A1":[0,0,0,0,0,0,0,0]},"reproduces_v28":True},"open":{"T0":True,"Tinf":True,"qroots":True,"cc_component":True,"full_cech_lattice_system":True,"ct_marked_pic_mod2":True,"HS_d2":True,"standard_kummer_columns":0},"next":"MATERIALIZE_CURRENT_LAMBDA_D_T0_TINF_QROOT_RANK2_LATTICES_AND_2X2_OVERLAPS_THEN_ASSEMBLE_CURRENT_CT_MARKED_PIC_MOD2","firewall":{"stage33_12_closed":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"merge_allowed":False}}
 assert csha(out)==EXPECTED
 return out
def main():
 out=build()
 if "--check" in sys.argv: assert locked(OUT,EXPECTED)=={**out,"canonical_sha256":EXPECTED}
 else:
  p=dict(out); p["canonical_sha256"]=EXPECTED; OUT.write_text(json.dumps(p,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"success":True,"canonical_sha256":EXPECTED,"rank2_records":19,"T0_Tinf_qroots_open":True,"historical_overlap_used":False,"marker":"PROOF_REPLAY_COMPLETE"},sort_keys=True))
if __name__=="__main__": main()
