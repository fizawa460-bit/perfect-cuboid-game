#!/usr/bin/env python3
"""Materialize the full-surface Stage-B adjustment contract after Kc zero-survival closure.

Stage33-05 now closes exactly with zero Q-surviving classes in its 2D Kc Br[2]
block. That removes the historical J2 kernel charge, but it does not identify
or kill the distinct 10D full-surface invariant proper Br[2] receiver P.
"""
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STAGE33=HERE.parent
BR2=STAGE33/"33-07"/"proper-brauer2-from-discriminant.json"
GLUE=STAGE33/"33-07"/"coordinate-k3-transcendental-glue-index.json"
ZERO=STAGE33/"33-05"/"stage33-05-br2-zero-q-survival-hostile-replay.json"
H10=STAGE33/"33-10"/"handoff.json"
SCALARS=HERE/"boundary-function-scalar-descent-certificate.json"
CONTROLLER=STAGE33/"controller.json"
OUT=HERE/"full-surface-hs-adjustment-contract.json"

EXPECTED_BR2="c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_GLUE="0cc5321d02b56cea801b8def71a4c3b0946bd8011d8c30767a9602faba2fa8d8"
EXPECTED_ZERO="4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9"
EXPECTED_H10="4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f"
EXPECTED_SCALARS="e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b"
N=14

def csha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load_locked(path,expected):
    o=json.loads(path.read_text(encoding="utf-8"))
    b=dict(o); claimed=b.pop("canonical_sha256",None)
    if claimed!=expected or csha(b)!=expected:
        raise SystemExit(f"canonical source lock moved: {path}")
    return o

def rank(rows):
    a=[[int(x)&1 for x in r] for r in rows if any(int(x)&1 for x in r)]
    rr=0
    for c in range(len(a[0]) if a else N):
        p=next((i for i in range(rr,len(a)) if a[i][c]),None)
        if p is None: continue
        a[rr],a[p]=a[p],a[rr]
        for i in range(len(a)):
            if i!=rr and a[i][c]:
                a[i]=[x^y for x,y in zip(a[i],a[rr])]
        rr+=1
    return rr

def fixed_dimension(cc,ct):
    eq=[]
    for action in (cc,ct):
        for j in range(N):
            eq.append([action[i][j]^int(i==j) for i in range(N)])
    return N-rank(eq)

br2=load_locked(BR2,EXPECTED_BR2)
glue=load_locked(GLUE,EXPECTED_GLUE)
zero=load_locked(ZERO,EXPECTED_ZERO)
h10=load_locked(H10,EXPECTED_H10)
scalars=load_locked(SCALARS,EXPECTED_SCALARS)
controller=json.loads(CONTROLLER.read_text(encoding="utf-8"))

if zero["status"]!="PASS_HOSTILE_REPLAY_EXACT_ZERO_K3_BR2_Q_SURVIVAL":
    raise SystemExit("Stage33-05 zero-survival hostile replay moved")
if zero["hostile_checks"]["global_kernel_dimension_f2"]!=0:
    raise SystemExit("Kc zero-survival kernel regression")
if zero["verdict"]["corrected_J2_Q_defined_Brauer_preimage"] is not False:
    raise SystemExit("corrected J2 Q-preimage unexpectedly restored")
if controller["stage33_05"]["unit_closed"] is not True or controller["stage33_05"]["Q_relevant_surviving_dimension"]!=0:
    raise SystemExit("controller did not preserve Stage33-05 zero-survival closure")
if controller["stage33_progress"]!="6/11":
    raise SystemExit("Stage33 progress regression")
if h10["status"]!="CLOSED_EXACT":
    raise SystemExit("Stage33-10 is not exact-closed")
if glue["integral_glue"]["actual_glue_subgroup_identified"]:
    raise SystemExit("historical full-surface glue state unexpectedly promoted")
if not scalars["exact_conclusion"]["all_cc_ct_function_level_scalar_ratios_equal_one"]:
    raise SystemExit("boundary scalar adapter regression")

cc=br2["proper_Br2_cc_action_f2"]
ct=br2["proper_Br2_ct_action_f2"]
if fixed_dimension(cc,ct)!=10:
    raise SystemExit("full-surface proper invariant dimension regression")

directions=[f"A2_{i:02d}" for i in range(1,27)]
certificate={
  "schema":"STAGE33_12_FULL_SURFACE_HS_ADJUSTMENT_CONTRACT_V3_KC_ZERO_SURVIVAL_HANDOFF",
  "source_locks":{
    "proper_brauer2_from_discriminant_sha256":EXPECTED_BR2,
    "coordinate_k3_transcendental_glue_sha256":EXPECTED_GLUE,
    "stage33_05_zero_survival_hostile_sha256":EXPECTED_ZERO,
    "stage33_10_handoff_sha256":EXPECTED_H10,
    "boundary_function_scalar_descent_sha256":EXPECTED_SCALARS
  },
  "full_surface_proper_adjustment_module":{
    "module":"P=Br(Sbar)[2]^{G_Q}",
    "dimension_f2":10,
    "action_source":"source-locked 14-dimensional full-surface proper Br2 module",
    "hs_adjustment_map":"d2_S|P: P -> H^2(G_Q,Pic(Sbar))[2]",
    "map_materialized":False,
    "kernel_dimension_lower_bound_f2":0,
    "kernel_dimension_upper_bound_f2":10,
    "known_q_defined_zero_boundary_proper_subgroup_dimension_f2_charged":0,
    "reason":"Stage33-05 now closes by exact zero Kc Br[2] Q-survival: corrected J2 and q1 both have nonzero HS d2 and neither supplies a Q-defined proper class. That removes the old J2 kernel charge but does not identify the distinct full-surface invariant module P."
  },
  "k3_to_full_surface_firewall":{
    "Kc_geometric_GQ_invariant_dimension_f2":2,
    "Kc_Q_relevant_surviving_dimension_f2":0,
    "Kc_zero_survival_hostile_pass":True,
    "corrected_J2_Q_defined_Brauer_preimage":False,
    "q1_Q_defined_Brauer_preimage":False,
    "Kc_zero_survival_implies_full_surface_P_zero":False,
    "J2_full_surface_q_defined_pullback_certified_elsewhere":False,
    "q1_full_surface_d2_image_generator_promoted":False,
    "reason":"The closed Kc calculation classifies a 2-dimensional K3 block. The full-surface P is a separately source-locked 10-dimensional invariant receiver; no injection/surjection identifying the two receivers has been certified."
  },
  "finite_stage_B_obstruction":{
    "directions":directions,
    "direction_count":26,
    "stage_A_localization_zero_exact_audited":26,
    "boundary_function_scalar_correction_zero_exact":26,
    "invariant_geometric_lift_fiber":"torsor under P",
    "lift_independent_obstruction_target":"coker(d2_S|P)",
    "obstruction_coset_definition":"omega(r)=[d2(beta)] mod im(d2_S|P), for any invariant geometric lift beta of r",
    "independence_of_beta":"Changing beta by p in P changes d2(beta) by d2_S(p).",
    "global_Q_lift_criterion":"omega(r)=0",
    "obstruction_cosets_materialized":0,
    "global_Q_lifts_promoted":0
  },
  "exact_information_boundary":{
    "literal_d2_zero_of_one_arbitrary_lift_required":False,
    "proper_adjustment_cokernel_is_the_correct_receiver":True,
    "zero_localization_and_zero_boundary_scalar_determine_any_stage_B_coset":False,
    "full_surface_proper_d2_map_or_equivalent_quotient_required":True,
    "one_full_surface_invariant_Kummer_defect_per_generator_or_equivalent_direct_coset_required":True,
    "first_column_before_full_matrix_required":True,
    "full_75x10_matrix_should_not_be_started_by_guessed_zero_columns":True,
    "actual_full_surface_unimodular_glue_or_mu2_lift_interface_materialized":False
  },
  "next_exact_leaf":"MATERIALIZE_ONE_75_COORDINATE_FINITE_V4_KUMMER_DEFECT_COLUMN_FROM_A_FULL_SURFACE_MU2_LIFT_OR_EQUIVALENT_UNIMODULAR_GLUE_DATUM",
  "promotion_firewall":{
    "arithmetic_hs_d2_computed":False,
    "global_q_br0g_residue_lifts_complete":False,
    "stage33_12_closed":False,
    "stage33_07_closed":False,
    "stage33_progress":"6/11",
    "theorem_credit":False,
    "endpoint_credit":False
  }
}
certificate["canonical_sha256"]=csha(certificate)
OUT.write_text(json.dumps(certificate,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
  "success":True,
  "proper_invariant_dimension_f2":10,
  "Kc_Q_survival_dimension_f2":0,
  "known_full_surface_kernel_charge_from_Kc":0,
  "next_exact_leaf":certificate["next_exact_leaf"],
  "certificate_sha256":certificate["canonical_sha256"]
},indent=2,sort_keys=True))
