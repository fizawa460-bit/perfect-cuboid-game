#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
REG=ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json"
LANES=ROOT/"stages/stage32/proof/LANE-ADAPTERS.json"
STATE=ROOT/"stages/stage32-ex2/MAIN-STATE.json"
STATE_VERIFY=ROOT/"stages/stage32-ex2/verify_main_state.py"
CURRENT_MAIN="70265586b3f97be21c7621af73f443311f1f3fa3"
CLAIM_ID="S32.EX2.THREE_DIVISOR_SECTION_SUBSPACE.V1"
ART_PATH="stages/stage32-ex2/EX2-04/third-section-valuation-separation.json"
ART_BLOB="5e9cf16ece57162db995cb1b7014a9d583453202"
ART_CANON="9d50dc72c467edce946427f1b74786464e1c6401ca86dab6af87bea792d23c70"
VERIFY_PATH="stages/stage32-ex2/verify_ex2_04b_third_section_valuation_separation.py"
VERIFY_BLOB="95a3ae6d83babfdf54ca144f7a732e158d65a6f7"
CORE_KEYS=["claim_id","kind","statement","scope_key","scope","proves","does_not_prove","requires","bridges","source_locks","replay_verifier"]

def git(*args:str)->str:
    return subprocess.check_output(["git",*args],cwd=ROOT,text=True).strip()
def show_json(ref:str,path:str)->dict:
    return json.loads(git("show",f"{ref}:{path}"))
def csha(c:dict)->str:
    core={k:c[k] for k in CORE_KEYS if k in c}
    return hashlib.sha256(json.dumps(core,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def dump(path:Path,obj:object)->None:
    path.write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")

assert git("rev-parse","origin/main")==CURRENT_MAIN
branch_reg=json.loads(REG.read_text())
branch_lanes=json.loads(LANES.read_text())
main_reg=show_json("origin/main","stages/stage32/proof/CLAIM-REGISTRY.json")
main_lanes=show_json("origin/main","stages/stage32/proof/LANE-ADAPTERS.json")
claim={
 "claim_id":CLAIM_ID,
 "kind":"mathematical_claim",
 "statement":"EX2-04B adjoins the exact post1648ag effective V6 divisor EAG to the retained EX2-04A pencil; valuation at C25 separates its canonical section from W, certifying a three-dimensional Qbar divisor-theoretic section subspace of H^0(S,O_S(V6)), not complete H0.",
 "scope_key":"S32.EX2.V6_LINEAR_SYSTEM",
 "scope":{"field":"Qbar","lane":"EX2","output":"certified three-dimensional divisor-theoretic section subspace only","picard_class":"V6","unit":"EX2-04B"},
 "proves":[
  "The retained post1648ag known-140 nonnegative decomposition is an exact effective divisor EAG linearly equivalent to V6.",
  "Every nonzero section in the EX2-04A pencil W vanishes along C25 to order at least 6, while the canonical section s_EAG vanishes along C25 to order exactly 4; therefore s_EAG is not in W.",
  "The span of s_E17, s_E98, and s_EAG is a certified three-dimensional Qbar section subspace of H^0(S,O_S(V6)).",
  "Within this certified three-dimensional subspace only, the common retained divisor on labels [21,24,25,30,31] has multiplicities [3,3,4,2,5]."
 ],
 "does_not_prove":[
  "A complete basis or exact dimension of H^0(S,O_S(V6)).",
  "Any ambient-coordinate, ideal/syzygy, Cox/graded, or symmetry-linearized section coefficients.",
  "An effective V6 divisor outside the retained known-140 monoid.",
  "Any of curves 21,24,25,30,31 is fixed in the complete linear system |V6|.",
  "An integral irreducible geometric-genus-1 V6 member.",
  "Population-wide nonexistence of such members.",
  "Stage32 MAIN, Q602, O210, receiver, theorem, endpoint, or Perfect Cuboid credit."
 ],
 "requires":["S32.EX2.TWO_DIVISOR_SECTION_PENCIL.V1"],
 "source_locks":[
  {"blob_sha1":ART_BLOB,"canonical_sha256":ART_CANON,"path":ART_PATH},
  {"blob_sha1":VERIFY_BLOB,"path":VERIFY_PATH}
 ],
 "replay_verifier":VERIFY_PATH,
 "authority_status":"PROVISIONAL",
 "audit_receipt":None,
}
claim["claim_core_sha256"]=csha(claim)
assert claim["claim_core_sha256"]=="62b09321988567f68eb7bb3a6c6de7bece7a9471093cab45f485a9230b2fc05d"

branch_claims={c["claim_id"]:c for c in branch_reg["claims"]}
main_claims={c["claim_id"]:c for c in main_reg["claims"]}
import_ids=[cid for cid in branch_claims if cid.startswith("S32.EX2.")]
if "S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V3" in branch_claims:
    import_ids.append("S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V3")
for cid in import_ids:
    bc=branch_claims[cid]
    if cid in main_claims:
        assert main_claims[cid]["claim_core_sha256"]==bc["claim_core_sha256"],cid
    main_claims[cid]=bc
main_claims[CLAIM_ID]=claim
ordered=[]; seen=set()
for c in main_reg["claims"]:
    cid=c["claim_id"]; ordered.append(main_claims[cid]); seen.add(cid)
for c in branch_reg["claims"]:
    cid=c["claim_id"]
    if cid in main_claims and cid not in seen:
        ordered.append(main_claims[cid]); seen.add(cid)
if CLAIM_ID not in seen:
    ordered.append(claim)
main_reg["claims"]=ordered
dump(REG,main_reg)

branch_ex2=next(x for x in branch_lanes["lanes"] if x["lane"]=="EX2")
main_ex2=next(x for x in main_lanes["lanes"] if x["lane"]=="EX2")
main_ex2["active_frontier_refs"]=branch_ex2["active_frontier_refs"]
main_ex2["claim_refs"]=list(branch_ex2["claim_refs"])
if CLAIM_ID not in main_ex2["claim_refs"]:
    main_ex2["claim_refs"].append(CLAIM_ID)
main_ex2["notes"]=(
 "EX2 attacks actual-member reconstruction and complete-linear-system nonexistence. "
 "PR #1709 exact head 0a39b08b767681f1a475dbe12d87e29315af041d passed hostile audit review 5142431810 through EX2-03F at the recorded intermediate ceiling. "
 "EX2-04A and EX2-04B are newer PROVISIONAL claims. EX2-04A certifies a 2-dimensional divisor-theoretic pencil; EX2-04B valuation-separates the exact post1648ag V6 divisor at C25 and certifies a 3-dimensional divisor-theoretic section subspace. "
 "Neither reconstructs complete H0, classifies the five conics in the complete linear system, produces an integral genus-1 member, or grants Stage32 MAIN credit."
)
dump(LANES,main_lanes)

s=json.loads(STATE.read_text())
s["schema"]="STAGE32EX2_MAIN_COMPACT_STATE_V12_EX2_04B_THREE_DIVISOR_SUBSPACE_EX2_04C_ACTIVE"
s["audit"]["status"]="NOT_READY_NEW_EX2_04A_04B_PROVISIONAL_AFTER_AUDITED_INTERMEDIATE_CHECKPOINT"
s["authority"].update({
 "EX2_04B_section_subspace":ART_PATH,
 "EX2_04B_artifact_blob_sha1":ART_BLOB,
 "EX2_04B_artifact_canonical_sha256":ART_CANON,
 "EX2_04B_verifier_blob_sha1":VERIFY_BLOB,
 "EX2_04B_candidate_claim_id":CLAIM_ID,
 "EX2_04B_claim_status":"PROVISIONAL_CLAIM_DAG_SYNCHRONIZED_NOT_HOSTILE_AUDITED",
})
s["freshness"].update({
 "current_main_observed_sha":CURRENT_MAIN,
 "last_reconciled_current_main_sha":CURRENT_MAIN,
 "unreconciled_main_commit_count":0,
 "intervening_main_commit_scope":"STAGE32EX5_CLOSURE_PLUS_SHARED_CLAIM_DAG_ONLY_COMPOSED_FROM_CURRENT_MAIN",
 "stage32ex2_source_drift_in_intervening_main_commit":False,
 "freshness_sync_deferred_until_retained_promotion_checkpoint":False,
 "promotion_requires_recheck_current_main":True,
})
s["claim_sync"].update({
 "candidate_claim_id":CLAIM_ID,
 "checkpoint_claim_dag_complete":True,
 "claim_dag_integrity_verifier_passed":True,
 "active_frontier_verifier_passed":True,
 "current_main_reconciliation_required":False,
 "mathematical_frontier_semantics_changed":False,
 "promotion_attempted":False,
 "reason":"Register EX2-04B as a narrow PROVISIONAL three-dimensional divisor-theoretic section-subspace claim. Shared claim files are composed from current main 70265586 so the newer EX5 audited closure metadata is preserved. EX2-04A remains provisional; Stage32 MAIN authority/frontier is unchanged.",
 "reconciled_current_main_sha":CURRENT_MAIN,
 "required_verification_run":None,
 "shared_claim_files_written_from_stale_branch":False,
 "stage32_main_authority_changed":False,
 "status":"COMPLETE_CURRENT_MAIN_COMPOSITION_EX2_04B_PROVISIONAL_REGISTERED_EXACT_HEAD_CI_REQUIRED",
 "trigger":"RETAINED_CONSOLIDATION",
 "triggered_for_EX2_04B":True,
})
s["credit"]["level"]="CERTIFIED_3D_DIVISOR_THEORETIC_SECTION_SUBSPACE_PLUS_AUDITED_INTERMEDIATE_EX2_00_THROUGH_03F_NO_COMPLETE_H0_NO_MEMBER_CREDIT"
s["current"].update({
 "leaf":"EX2-04_FINITE_DIMENSIONAL_SECTION_RECONSTRUCTION",
 "status":"EX2_04B_CERTIFIED_3D_DIVISOR_THEORETIC_SUBSPACE_EX2_04C_ACTIVE",
 "subroute":"EX2-04C_SECTION_SUBSPACE_ENLARGEMENT_OR_COORDINATE_MATERIALIZATION",
 "objective":"Either enlarge the source-bound divisor-theoretic section subspace beyond dimension 3 using another exact valuation-separated V6 divisor, or obtain coordinate/ideal-syzygy/restriction-gluing section data suitable for EX2-05 materialization.",
 "next_route_on_success":"IF_EXPLICIT_SOURCE_BOUND_SECTION_VECTOR_SUITABLE_FOR_MEMBER_MATERIALIZATION_IS_OBTAINED_ROUTE_TO_EX2_05_OTHERWISE_CONTINUE_BOUNDED_EX2_04_ENLARGEMENT",
 "next_route_on_block":"ROUTE_TO_MATERIALLY_DISTINCT_EX2_04_COORDINATE_IDEAL_SYZYGY_OR_RESTRICTION_GLUING_LANE",
})
s["frontier"].update({
 "EX2_04A_certified_two_dimensional_section_subspace":True,
 "EX2_04B_certified_three_dimensional_section_subspace":True,
 "EX2_04B_third_section_line_outside_04A_pencil":True,
 "EX2_04B_valuation_separator_curve_label_1based":25,
 "EX2_04B_04A_order_lower_bound":6,
 "EX2_04B_third_section_order":4,
 "EX2_04B_common_divisor_labels_1based":[21,24,25,30,31],
 "EX2_04B_common_divisor_multiplicities":[3,3,4,2,5],
 "certified_section_subspace_dimension":3,
 "complete_section_space_basis_obtained":False,
 "EX2_04_finite_dimensional_section_reconstruction_active":True,
})
for k in ["three_dimensional_section_subspace_promoted_to_complete_H0","known140_third_divisor_promoted_to_integral_member","valuation_separation_promoted_to_coordinate_section"]:
    s["firewalls"][k]=False
s["current_leaf_working_set"]=[
 ART_PATH,VERIFY_PATH,
 "stages/stage32-ex2/EX2-04/two-divisor-section-pencil.json",
 "stages/stage32-ex2/verify_ex2_04a_two_divisor_section_pencil.py",
 "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json",
 "stages/stage32-ex2/EX2-01/section-source-inventory.json",
 "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json",
 "stages/stage32-ex2/stage32-ex2.md",
]
dump(STATE,s)

STATE_VERIFY_TEXT='''#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
S=json.loads((HERE/"MAIN-STATE.json").read_text())
R=json.loads((ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json").read_text())
L=json.loads((ROOT/"stages/stage32/proof/LANE-ADAPTERS.json").read_text())
CURRENT_MAIN="70265586b3f97be21c7621af73f443311f1f3fa3"
AUDIT_HEAD="0a39b08b767681f1a475dbe12d87e29315af041d"
AUDIT_REVIEW=5142431810
CLAIM="S32.EX2.THREE_DIVISOR_SECTION_SUBSPACE.V1"
assert S["schema"]=="STAGE32EX2_MAIN_COMPACT_STATE_V12_EX2_04B_THREE_DIVISOR_SUBSPACE_EX2_04C_ACTIVE"
assert S["stage"]=="32EX2"
assert S["bootstrap"]["active_work_pr"]==1709 and S["bootstrap"]["merge_authorized"] is False
assert S["audit"]["previous_intermediate_pass"]=={"credit_ceiling":"NECESSARY_CONDITION_ONLY","exact_head":AUDIT_HEAD,"review_id":AUDIT_REVIEW,"status":"PASS","through":"EX2-03F"}
assert S["audit"]["status"]=="NOT_READY_NEW_EX2_04A_04B_PROVISIONAL_AFTER_AUDITED_INTERMEDIATE_CHECKPOINT"
assert S["freshness"]["current_main_observed_sha"]==CURRENT_MAIN
assert S["freshness"]["last_reconciled_current_main_sha"]==CURRENT_MAIN
assert S["freshness"]["unreconciled_main_commit_count"]==0
assert S["freshness"]["stage32ex2_source_drift_in_intervening_main_commit"] is False
assert S["claim_sync"]["reconciled_current_main_sha"]==CURRENT_MAIN
assert S["claim_sync"]["candidate_claim_id"]==CLAIM
assert S["claim_sync"]["triggered_for_EX2_04B"] is True
assert S["claim_sync"]["shared_claim_files_written_from_stale_branch"] is False
A=S["authority"]
assert A["EX2_04B_artifact_blob_sha1"]=="5e9cf16ece57162db995cb1b7014a9d583453202"
assert A["EX2_04B_artifact_canonical_sha256"]=="9d50dc72c467edce946427f1b74786464e1c6401ca86dab6af87bea792d23c70"
assert A["EX2_04B_verifier_blob_sha1"]=="95a3ae6d83babfdf54ca144f7a732e158d65a6f7"
assert A["EX2_04B_candidate_claim_id"]==CLAIM
assert A["EX2_04B_claim_status"]=="PROVISIONAL_CLAIM_DAG_SYNCHRONIZED_NOT_HOSTILE_AUDITED"
F=S["frontier"]
assert F["EX2_04B_certified_three_dimensional_section_subspace"] is True
assert F["EX2_04B_third_section_line_outside_04A_pencil"] is True
assert F["EX2_04B_valuation_separator_curve_label_1based"]==25
assert F["EX2_04B_04A_order_lower_bound"]==6 and F["EX2_04B_third_section_order"]==4
assert F["EX2_04B_common_divisor_labels_1based"]==[21,24,25,30,31]
assert F["EX2_04B_common_divisor_multiplicities"]==[3,3,4,2,5]
assert F["certified_section_subspace_dimension"]==3
assert F["complete_section_space_basis_obtained"] is False
assert S["current"]["subroute"]=="EX2-04C_SECTION_SUBSPACE_ENLARGEMENT_OR_COORDINATE_MATERIALIZATION"
assert S["completion_contract"]["terminal_outcome"] is None
assert S["credit"]["genuine_v6_genus1_member_established"] is False
assert S["credit"]["no_integral_irreducible_v6_genus1_member_in_linear_system"] is False
assert S["credit"]["stage32_main_credit"] is False
for k in ["three_dimensional_section_subspace_promoted_to_complete_H0","known140_third_divisor_promoted_to_integral_member","valuation_separation_promoted_to_coordinate_section","stage32_main_credit","Q602_excluded","O210_excluded","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
    assert S["firewalls"][k] is False,k
claims={c["claim_id"]:c for c in R["claims"]}
for cid in ["S32.EX2.SECTION_SOURCE_INVENTORY.V2","S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1","S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1","S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1"]:
    assert claims[cid]["authority_status"]=="AUDITED",cid
c=claims["S32.EX2.TWO_DIVISOR_SECTION_PENCIL.V1"]
assert c["authority_status"]=="PROVISIONAL" and c["audit_receipt"] is None
c=claims[CLAIM]
assert c["authority_status"]=="PROVISIONAL" and c["audit_receipt"] is None
assert c["claim_core_sha256"]=="62b09321988567f68eb7bb3a6c6de7bece7a9471093cab45f485a9230b2fc05d"
ex2=next(x for x in L["lanes"] if x["lane"]=="EX2")
assert "S32.EX2.TWO_DIVISOR_SECTION_PENCIL.V1" in ex2["claim_refs"]
assert CLAIM in ex2["claim_refs"]
assert any(c["claim_id"]=="S32.EX5.BOUNDED_EXHAUSTION_CANDIDATE.V2" for c in R["claims"])
for rel in ["verify_ex2_00_source_lock.py","verify_ex2_01_section_sources_v2.py","verify_ex2_02_fixed_components.py","verify_ex2_03_restriction_gap.py","verify_ex2_03b_v6_stabilizer_orbit.py","verify_ex2_03c_omission_witnesses.py","verify_ex2_03d_five_conic_restriction.py","verify_ex2_03e_adjoint_nef_blocker.py","verify_ex2_03f_corrected_adjoint_known140.py","verify_ex2_04a_two_divisor_section_pencil.py","verify_ex2_04b_third_section_valuation_separation.py"]:
    subprocess.check_call([sys.executable,"-B",str(HERE/rel)],cwd=ROOT)
print("PASS Stage32EX2 MAIN state V12")
print("current_leaf=EX2-04C section-subspace enlargement or coordinate materialization")
print("freshness_reconciled_main="+CURRENT_MAIN)
print("EX2-04B certified_subspace_dimension=3 provisional=true complete_H0=false")
print("merge_authorized=false stage32_main_credit=false")
'''
STATE_VERIFY.write_text(STATE_VERIFY_TEXT)
print("PASS apply EX2-04B current-main claim sync")
