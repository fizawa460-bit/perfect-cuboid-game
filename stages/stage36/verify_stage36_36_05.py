#!/usr/bin/env python3
from __future__ import annotations
import hashlib,itertools,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
CERT=ROOT/"stages/stage36/36-05/uniform-ramification-support.json"
PREV=ROOT/"stages/stage36/36-04/h-torsor-lift-class.json"
CERT_BLOB="621128511e72dc3ceca5e4ac6963b87ef29b1b3c"
PREV_BLOB="a06e201a9b554da71c5e75d8f8541e7284f8d020"
BASE="dca962cdf37d4252316885dc57f3c0a591db4ecb"
SOURCES={
 "stage36_roadmap":("stages/stage36/ROADMAP.md","eeedda0e89e24f851c989b5ec83e7b320e1ad99e"),
 "stage29_arithmetic_routing":("stages/stage29/29-02hb/arithmetic-routing.md","ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),
 "stage29_campedelli_quotient_adapter":("stages/stage29/29-02hb/campedelli-quotient-adapter.md","5f959d60106243bb31df06a3961ab04182d78fc7"),
 "stage29_exact_sign_cover_model":("stages/stage29/29-02ha/exact-sign-cover-model.md","fc2d5284a259750f45d2d756a952002671e3bccc"),
}
ARSENAL={
 "router":("docs/arsenal/index.json","aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
 "S30-WF02":("docs/arsenal/cards/workflows/S30-WF02.md","38e4625155eb079bbe3d50d663c6256559319886"),
 "S30-WF03":("docs/arsenal/cards/workflows/S30-WF03.md","12740198aba19ade18302819f8e890dbda4eb701"),
 "S34-W01":("docs/arsenal/cards/formal/S34-W01.md","01a8e90e34b4aa46edbfa825803d488e5230e9d0"),
}
LINES={
 "A1":(1,0,0),"A2":(0,1,0),"A3":(0,0,1),
 "B3":(1,1,0),"B2":(1,0,1),"B1":(0,1,1),"C":(1,1,1),
}
FORMS={"A1":"x","A2":"y","A3":"z","B3":"x+y","B2":"x+z","B1":"y+z","C":"x+y+z"}
PROMO={"pr":1568,"exact_head":"53b0c3b2a84ef200848d6b4b515c94589798d295","exact_head_ci_run":33924921726,"exact_head_ci_job":101191239139,"merged_main_sha":BASE,"scope":"mechanical audited-state promotion only","NEW_THEOREM_CREDIT":False}

def blob_sha(path):
 data=path.read_bytes()
 return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def req(ok,msg):
 if not ok: raise SystemExit(msg)
def det(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def main():
 req(blob_sha(CERT)==CERT_BLOB,"36-05 certificate blob drift")
 req(blob_sha(PREV)==PREV_BLOB,"36-04 audited certificate blob drift")
 cert=json.loads(CERT.read_text())
 req(cert.get("schema")=="STAGE36_36_05_UNIFORM_RAMIFICATION_SUPPORT_V1","36-05 schema moved")
 req(cert.get("status")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT_PENDING_HOSTILE_AUDIT","36-05 status moved")
 req(cert.get("base_main_sha")==BASE,"36-05 base moved")
 req(cert.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT","36-05 legal outcome moved")
 req(cert.get("pass_condition")=={"UNIFORM_FINITE_RAMIFICATION_SUPPORT_PROVED":False,"FINITE_EXHAUSTIVE_H_TWIST_FAMILY":False,"ARBITRARY_PRIME_PHYSICAL_RECEIVER_POINT_CLAIM":False},"36-05 pass condition moved")

 auth=cert.get("source_authority",{})
 req(auth.get("stage36_36_04_certificate")=={"path":"stages/stage36/36-04/h-torsor-lift-class.json","blob_sha":PREV_BLOB},"36-04 certificate authority moved")
 req(auth.get("stage36_36_04_hostile_audit_review")==5118098931,"36-04 hostile review moved")
 req(auth.get("stage36_36_04_hostile_audited_head")=="ce3eea151743b4ce031c84f09abd17221b7fe019","36-04 hostile head moved")
 req(auth.get("stage36_36_04_final_user_approved_head")=="dcdae282120f29a42679b654e21bd35f843e4cbf","36-04 final approved head moved")
 req(auth.get("stage36_36_04_merge")=="de1df3d25c39306e5601646309b38aaad56967bd","36-04 merge moved")
 p=auth.get("stage36_36_04_promotion",{})
 req(p=={k:v for k,v in PROMO.items() if k not in {"scope","NEW_THEOREM_CREDIT"}},"36-04 promotion source moved")

 for key,(rel,sha) in SOURCES.items():
  req(cert.get("source_locks",{}).get(key)=={"path":rel,"blob_sha":sha},f"source declaration moved: {key}")
  req(blob_sha(ROOT/rel)==sha,f"source blob drift: {key}")
 for key,(rel,sha) in ARSENAL.items():
  row=cert.get("arsenal_locks",{}).get(key,{})
  req(row.get("path")==rel and row.get("blob_sha")==sha,f"Arsenal declaration moved: {key}")
  req(blob_sha(ROOT/rel)==sha,f"Arsenal blob drift: {key}")

 routing=(ROOT/SOURCES["stage29_arithmetic_routing"][0]).read_text()
 req("Without ramification conditions this set is infinite" in routing,"Stage29 H1 infinitude anchor missing")
 req("A finite twist list requires a separate Selmer/ramification argument" in routing,"Stage29 finite-twist firewall missing")
 roadmap=(ROOT/SOURCES["stage36_roadmap"][0]).read_text()
 req("BLOCKED_MOVING_RAMIFICATION_SUPPORT" in roadmap,"roadmap blocked outcome missing")
 req("A bounded prime experiment does not prove finite support" in roadmap,"roadmap bounded-prime firewall missing")
 w01=(ROOT/ARSENAL["S34-W01"][0]).read_text()
 for needle in ["SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT","primitive numerator coordinates","pairwise gcd/resultant","complete sign and 2-adic bookkeeping"]:
  req(needle in w01,f"S34-W01 hypothesis anchor missing: {needle}")
 al=cert.get("arsenal_locks",{})
 req(al.get("S34-W01",{}).get("consulted") is True and al.get("S34-W01",{}).get("triggered") is False,"S34-W01 activation moved")
 req(al.get("S34-W03")=="PREPARED_IN_36_03_NOT_EXECUTED","S34-W03 execution drift")
 req(al.get("S30-W02")=="NOT_TRIGGERED_Q_FORM_ALREADY_EXACT","S30-W02 activation drift")

 geo=cert.get("fixed_geometric_support",{})
 req(geo.get("seven_line_forms")==FORMS,"seven-line forms moved")
 req({k:tuple(v) for k,v in geo.get("line_coefficient_vectors",{}).items()}==LINES,"line coefficient vectors moved")
 nonzero_abs=sorted({abs(det(*(LINES[k] for k in comb))) for comb in itertools.combinations(LINES,3) if det(*(LINES[k] for k in comb))!=0})
 req(nonzero_abs==[1,2],"seven-line determinant spectrum moved")
 req(geo.get("absolute_nonzero_triple_determinants")==[1,2],"certificate determinant spectrum moved")
 req(geo.get("seven_line_arrangement_combinatorial_bad_prime_candidates")==[2],"line-arrangement bad-prime candidate moved")
 req(geo.get("FULL_C_H_GOOD_REDUCTION_OUTSIDE_2_PROVED") is False,"full quotient good reduction overclaimed")
 b=geo.get("boundary",{})
 req(b.get("coordinate_zero_excluded_from_physical_receiver") is True,"coordinate boundary moved")
 req(b.get("noncoordinate_zero_strata_chart_switched_in_36_04") is True,"noncoordinate boundary moved")
 req(b.get("six_quotient_A1_exceptional_curves_outside_physical_image") is True,"exceptional boundary moved")

 gap=cert.get("arithmetic_specialization_gap",{})
 req(gap.get("UNIFORM_Q_PRIME_SUPPORT_PROVED") is False,"uniform specialization support overclaimed")
 req(gap.get("numerator_denominator_support_controlled_uniformly") is False,"numerator/denominator support overclaimed")
 req(gap.get("primitive_receiver_gcd_resultant_support_theorem_available") is False,"gcd/resultant theorem invented")
 req(gap.get("S_integrality_theorem_available") is False,"S-integrality theorem invented")
 req(gap.get("ARBITRARY_PRIME_PHYSICAL_RECEIVER_POINT_CLAIM") is False,"ambient witness promoted to physical receiver")
 req(gap.get("PHYSICAL_RECEIVER_POINT_FAMILY_EXHIBITED") is False,"ambient family promoted to receiver family")
 fam=gap.get("ambient_square_coordinate_family",{})
 req(fam.get("family")=="q_n=[1:n^2:1]" and fam.get("B3_value")=="1+n^2","ambient family moved")
 for n in range(1,8):
  vals=[1,n*n,1,1+n*n,2,1+n*n,2+n*n]
  req(all(v!=0 for v in vals),"ambient square-coordinate family hit boundary")
 req("finite prime set T" in fam.get("infinitely_many_prime_divisors_proof","") and "1+N^2" in fam.get("infinitely_many_prime_divisors_proof",""),"ambient infinitude proof record missing")
 missing=cert.get("exact_missing_theorem",{})
 req(missing.get("currently_proved") is False,"missing theorem prematurely proved")
 req("one finite set S" in missing.get("target","") and "every physically relevant delta_H(P)" in missing.get("target",""),"missing theorem quantifier moved")

 promo=cert.get("promotion",{})
 req(promo.get("hostile_audit_required") is True and promo.get("promoted_to_audited_authority") is False,"36-05 promotion boundary moved")
 req(promo.get("next_leaf_36_06_allowed") is False,"36-06 opened without uniform support")
 req(all(v is False for v in cert.get("claims",{}).values()),"36-05 certificate leaked higher credit")

 s=json.loads(STATE.read_text())
 req(s.get("schema")=="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V10_36_05_PENDING_AUDIT","Stage36 V10 schema moved")
 req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==BASE,"V10 lifecycle moved")
 req(s.get("stage36_36_04_promotion")==PROMO,"36-04 promotion state provenance moved")
 u=s.get("completed_units",{}).get("36-05",{})
 req(u.get("status")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT_PENDING_HOSTILE_AUDIT","36-05 unit status moved")
 req(u.get("certificate_blob_sha")==CERT_BLOB,"36-05 state certificate blob moved")
 req(u.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT","36-05 state outcome moved")
 req(u.get("UNIFORM_FINITE_RAMIFICATION_SUPPORT_PROVED") is False and u.get("FINITE_EXHAUSTIVE_H_TWIST_FAMILY") is False,"36-05 state credit moved")
 req(u.get("ARBITRARY_PRIME_PHYSICAL_RECEIVER_POINT_CLAIM") is False,"36-05 state physical-prime claim moved")
 req(u.get("promotion_status")=="PROVISIONAL_NOT_AUDITED","36-05 prematurely audited")
 g=s.get("promotion_gates",{})
 for key in ["source_authority_lock_complete","three_Q_representatives_exact","physical_open_push_and_boundary_complete","pointwise_H_torsor_class_explicit"]:
  req(g.get(key) is True,f"audited predecessor gate lost: {key}")
 for key in ["uniform_finite_ramification_support_proved","finite_exhaustive_H_twist_family_proved","local_solubility_filter_exhaustive","all_global_survivors_closed","quotient_Q_point_emptiness_proved","receiver_matched_replacement_theorem_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
  req(g.get(key) is False,f"later gate prematurely promoted: {key}")
 req(s.get("current",{}).get("unit")=="36-05" and s.get("current",{}).get("36_06_entry_allowed") is False,"36-06 entry opened")
 req("36-06" not in s.get("completed_units",{}),"36-06 started before 36-05 audit/support proof")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 print("PASS STAGE36_36_05_BLOCKED_MOVING_RAMIFICATION_SUPPORT")
 print("fixed seven-line divisor support exact; nonzero triple determinant abs values={1,2}")
 print("uniform specialization-prime support NOT proved; no physical arbitrary-prime point claimed")
 print("arsenal=S30-WF02,S30-WF03 applied; S34-W01 consulted but hypotheses not met")
 print("finite_twist_family=false; 36-06 entry forbidden; no receiver/endpoint/perfect-cuboid credit")

if __name__=="__main__":
 main()
