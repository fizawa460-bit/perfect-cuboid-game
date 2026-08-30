#!/usr/bin/env python3
"""Materialize the full-surface Stage-B adjustment contract after the J2 hostile reopen.

The historical Stage33-05 audit is retained as history, but the specific
Q-defined ell_J2 representative may no longer be charged into the full-surface
d2 kernel: Batch4 proved it is zero in the geometric CV function quotient.
"""
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
STAGE33=HERE.parent
BR2=STAGE33/"33-07"/"proper-brauer2-from-discriminant.json"
GLUE=STAGE33/"33-07"/"coordinate-k3-transcendental-glue-index.json"
K3_AUDIT=STAGE33/"33-05"/"audit-state.json"
H10=STAGE33/"33-10"/"handoff.json"
SCALARS=HERE/"boundary-function-scalar-descent-certificate.json"
REOPEN=HERE/"j2-cv-lclass-zero-regression.json"
CONTROLLER=STAGE33/"controller.json"
OUT=HERE/"full-surface-hs-adjustment-contract.json"
EXPECTED_BR2="c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_GLUE="0cc5321d02b56cea801b8def71a4c3b0946bd8011d8c30767a9602faba2fa8d8"
EXPECTED_K3_AUDIT_TEXT_LF="08a4bb374a29266aa9c59dd433ac0fb6cac89eaca31829339f7a6ce9e32a7fa6"
EXPECTED_H10="4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f"
EXPECTED_SCALARS="e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b"
N=14

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load_locked(path,expected):
    o=json.loads(path.read_text()); b=dict(o); claimed=b.pop("canonical_sha256",None)
    if claimed!=expected or csha(b)!=expected: raise SystemExit(f"canonical source lock moved: {path}")
    return o
def text_lf_sha(path): return hashlib.sha256(path.read_text().replace("\r\n","\n").encode()).hexdigest()
def rank(rows):
    a=[[int(x)&1 for x in r] for r in rows if any(int(x)&1 for x in r)]; rr=0
    for c in range(len(a[0]) if a else N):
        p=next((i for i in range(rr,len(a)) if a[i][c]),None)
        if p is None: continue
        a[rr],a[p]=a[p],a[rr]
        for i in range(len(a)):
            if i!=rr and a[i][c]: a[i]=[x^y for x,y in zip(a[i],a[rr])]
        rr+=1
    return rr
def fixed_dimension(cc,ct):
    eq=[]
    for action in (cc,ct):
        for j in range(N): eq.append([action[i][j]^int(i==j) for i in range(N)])
    return N-rank(eq)

br2=load_locked(BR2,EXPECTED_BR2); glue=load_locked(GLUE,EXPECTED_GLUE); h10=load_locked(H10,EXPECTED_H10); scalars=load_locked(SCALARS,EXPECTED_SCALARS)
k3=json.loads(K3_AUDIT.read_text()); reopen=json.loads(REOPEN.read_text()); controller=json.loads(CONTROLLER.read_text())
if text_lf_sha(K3_AUDIT)!=EXPECTED_K3_AUDIT_TEXT_LF: raise SystemExit("Stage33-05 historical audit state moved")
if k3["audit_verdict"]!="PASS_AFTER_INDEPENDENT_Q_SURVIVAL_AND_HS_D2_VERIFICATION": raise SystemExit("historical Stage33-05 audit record moved")
if not k3["q1_hs_d2_nonzero"]: raise SystemExit("historical q1 d2 record moved")
if reopen["status"]!="PASS_EXACT_UPSTREAM_REPRESENTATIVE_CONTRADICTION" or reopen["class3_promotion_allowed"]: raise SystemExit("hostile reopen certificate regression")
if controller["stage33_05_hostile_reopen"]["named_representative_credit"]!="REVOKED_PENDING_REPAIR": raise SystemExit("controller did not preserve hostile reopen")
if controller["stage33_07"]["j2_q_defined"]: raise SystemExit("stale J2 Q-defined promotion reappeared")
if h10["status"]!="CLOSED_EXACT": raise SystemExit("Stage33-10 is not exact-closed")
if glue["integral_glue"]["actual_glue_subgroup_identified"]: raise SystemExit("historical full-surface glue state unexpectedly promoted")
if not scalars["exact_conclusion"]["all_cc_ct_function_level_scalar_ratios_equal_one"]: raise SystemExit("boundary scalar adapter regression")
cc=br2["proper_Br2_cc_action_f2"]; ct=br2["proper_Br2_ct_action_f2"]
if fixed_dimension(cc,ct)!=10: raise SystemExit("full-surface proper invariant dimension regression")

directions=[f"A2_{i:02d}" for i in range(1,27)]
certificate={
"schema":"STAGE33_12_FULL_SURFACE_HS_ADJUSTMENT_CONTRACT_V2_HOSTILE_REOPEN",
"source_locks":{"proper_brauer2_from_discriminant_sha256":EXPECTED_BR2,"coordinate_k3_transcendental_glue_sha256":EXPECTED_GLUE,"stage33_05_audit_state_text_lf_sha256":EXPECTED_K3_AUDIT_TEXT_LF,"stage33_10_handoff_sha256":EXPECTED_H10,"boundary_function_scalar_descent_sha256":EXPECTED_SCALARS,"hostile_reopen_certificate":"stages/stage33/33-12/j2-cv-lclass-zero-regression.json"},
"full_surface_proper_adjustment_module":{"module":"P=Br(Sbar)[2]^{G_Q}","dimension_f2":10,"action_source":"source-locked 14-dimensional full-surface proper Br2 module","hs_adjustment_map":"d2_S|P: P -> H^2(G_Q,Pic(Sbar))[2]","map_materialized":False,"kernel_contains_q_defined_J2":False,"kernel_dimension_lower_bound_f2":0,"kernel_dimension_upper_bound_f2":10,"reason_for_downgrade":"Stage33-05 current ell_J2 nonzero Q-defined representative credit revoked by exact geometric CV L-class zero regression."},
"k3_to_full_surface_firewall":{"historical_stage33_05_audit_verdict_retained_as_history":True,"historical_audited_Kc_invariant_basis":["J2","q1"],"historical_audited_Kc_d2_kernel_basis":["J2"],"audited_Kc_q1_d2_nonzero":True,"current_ell_J2_nonzero_geometric_representative_credit":False,"J2_full_surface_q_defined_pullback_certified_elsewhere":False,"q1_full_surface_nonzero_pullback_certified":False,"q1_full_surface_d2_image_generator_promoted":False,"reason":"Hostile audit found the specific promoted ell_J2 is zero in the geometric CV function quotient. Abstract J2 is not revoked, but no current nonzero Q-defined representative may be charged into the full-surface kernel."},
"finite_stage_B_obstruction":{"directions":directions,"direction_count":26,"stage_A_localization_zero_exact_audited":26,"boundary_function_scalar_correction_zero_exact":26,"invariant_geometric_lift_fiber":"torsor under P","lift_independent_obstruction_target":"coker(d2_S|P)","obstruction_coset_definition":"omega(r)=[d2(beta)] mod im(d2_S|P), for any invariant geometric lift beta of r","independence_of_beta":"Changing beta by p in P changes d2(beta) by d2_S(p).","global_Q_lift_criterion":"omega(r)=0","obstruction_cosets_materialized":0,"global_Q_lifts_promoted":0},
"exact_information_boundary":{"literal_d2_zero_of_one_arbitrary_lift_required":False,"proper_adjustment_cokernel_is_the_correct_receiver":True,"zero_localization_and_zero_boundary_scalar_determine_any_stage_B_coset":False,"full_surface_proper_d2_map_or_equivalent_quotient_required":True,"one_full_surface_invariant_Kummer_defect_per_generator_or_equivalent_direct_coset_required":True,"named_J2_representative_repair_required_before_J2_kernel_charge":True},
"next_exact_leaf":"REPAIR_OR_REPLACE_STAGE33_05_NAMED_J2_CV_REPRESENTATIVE_BEFORE_RESUMING_FULL_SURFACE_J2_ADJUSTMENT_CREDIT",
"promotion_firewall":{"arithmetic_hs_d2_computed":False,"global_q_br0g_residue_lifts_complete":False,"stage33_12_closed":False,"stage33_07_closed":False,"stage33_progress":"5/11","class3_promoted":False}}
certificate["canonical_sha256"]=csha(certificate)
OUT.write_text(json.dumps(certificate,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"proper_invariant_dimension_f2":10,"J2_current_Q_defined_kernel_charge":False,"stage33_05_reopened":True,"certificate_sha256":certificate["canonical_sha256"]},indent=2,sort_keys=True))
