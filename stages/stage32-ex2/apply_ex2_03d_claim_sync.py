#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage32-ex2/MAIN-STATE.json"
VERIFY = ROOT / "stages/stage32-ex2/verify_main_state.py"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
LANES = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

CLAIM_ID = "S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1"
ART_PATH = "stages/stage32-ex2/EX2-03/remaining-five-conic-restriction-preflight.json"
ART_BLOB = "32e19797812f35ad15fc5cad7559be76140480ef"
ART_CANONICAL = "3f8ef39f3bd52804394b704fc2d6c2d810843d9f9f94530796c8c12c75d6f120"
VER_PATH = "stages/stage32-ex2/verify_ex2_03d_five_conic_restriction.py"
VER_BLOB = "f7a3f88969b0599f20b0217e806f9441cfe68f01"
CURRENT_MAIN = "f2a89e613cdf91191a0aada9e90c9fc93373a6c6"
CORE_KEYS = ["claim_id","kind","statement","scope_key","scope","proves","does_not_prove","requires","bridges","source_locks","replay_verifier"]

def csha(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",",":")).encode()).hexdigest()

def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")

def new_claim():
    c = {
      "claim_id": CLAIM_ID,
      "kind": "mathematical_claim",
      "statement": "EX2-03D identifies the five still-unresolved retained V6-zero curves 21,24,25,30,31 as pairwise-disjoint smooth rational conic strict transforms with self-intersection -4 and K-degree 2; for each C, O_S(V6)|C is trivial and fixedness is exactly the one-dimensional H0 restriction/evaluation question, with chi(V6)=294, chi(V6-C)=293 and h2(V6-C)=0.",
      "scope_key": "S32.EX2.V6_LINEAR_SYSTEM",
      "scope": {"field":"Qbar","lane":"EX2","picard_class":"V6","unit":"EX2-03D","retained_labels_1based":[21,24,25,30,31]},
      "proves": [
        "The retained curves 21,24,25,30,31 are pairwise-disjoint smooth rational conic strict transforms, each with C^2=-4, K.C=2 and V6.C=0.",
        "For each of these five conics, O_S(V6)|C is isomorphic to O_P1 and C is fixed in |V6| iff the restriction map H0(S,O(V6))->H0(C,O_C) is zero.",
        "For each such C, chi(O(V6))=294, chi(O(V6-C))=293 and h2(O(V6-C))=0, reducing the unresolved fixedness question to H0 evaluation or equivalent H1-jump control."
      ],
      "does_not_prove": [
        "Any of curves 21,24,25,30,31 is fixed or nonfixed.",
        "The fixed part of the complete V6 linear system is fully classified or empty.",
        "A complete basis or exact dimension of H0(S,O_S(V6)).",
        "An integral irreducible geometric-genus-1 V6 member.",
        "Population-wide nonexistence of such members.",
        "Stage32 MAIN, Q602, O210, receiver, theorem, endpoint, or Perfect Cuboid credit."
      ],
      "requires": ["S32.EX2.LANE_CONTRACT.V3","S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1","S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1"],
      "source_locks": [
        {"blob_sha1":ART_BLOB,"canonical_sha256":ART_CANONICAL,"path":ART_PATH},
        {"blob_sha1":VER_BLOB,"path":VER_PATH}
      ],
      "replay_verifier": VER_PATH,
      "authority_status": "PROVISIONAL",
      "audit_receipt": None
    }
    c["claim_core_sha256"] = csha({k:c[k] for k in CORE_KEYS if k in c})
    assert c["claim_core_sha256"] == "1a4220aae62ee856710131f5dd89173ced6ce3f40ecc741af349697677955576"
    return c

r=json.loads(REGISTRY.read_text())
claims={c["claim_id"]:c for c in r["claims"]}
for dep in ["S32.EX2.LANE_CONTRACT.V3","S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1","S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1"]:
    assert dep in claims
if CLAIM_ID in claims:
    assert claims[CLAIM_ID] == new_claim()
else:
    r["claims"].append(new_claim())
dump(REGISTRY,r)

l=json.loads(LANES.read_text())
ex2=next(x for x in l["lanes"] if x["lane"]=="EX2")
if CLAIM_ID not in ex2["claim_refs"]:
    idx=ex2["claim_refs"].index("S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V3")
    ex2["claim_refs"].insert(idx,CLAIM_ID)
ex2["notes"]="EX2 attacks actual-member reconstruction and complete-linear-system nonexistence. EX2-03C provisionally certifies zero curves 17 and 98 nonfixed. EX2-03D provisionally identifies the remaining five zero curves 21,24,25,30,31 as pairwise-disjoint rational conics with trivial O(V6) restriction; their fixedness is reduced to five one-dimensional restriction/evaluation or H1-jump questions. No full fixed-part, member, or MAIN credit is granted."
dump(LANES,l)

s=json.loads(STATE.read_text())
assert s["schema"]=="STAGE32EX2_MAIN_COMPACT_STATE_V8_EX2_03C_TWO_ZERO_CURVES_NONFIXED_EX2_03D_ACTIVE"
s["schema"]="STAGE32EX2_MAIN_COMPACT_STATE_V9_EX2_03D_FIVE_CONIC_RESTRICTION_REDUCTION_EX2_03E_ACTIVE"
s["authority"].update({
 "EX2_03D_restriction_preflight":ART_PATH,
 "EX2_03D_artifact_blob_sha1":ART_BLOB,
 "EX2_03D_artifact_canonical_sha256":ART_CANONICAL,
 "EX2_03D_verifier_blob_sha1":VER_BLOB,
 "EX2_03D_candidate_claim_id":CLAIM_ID,
 "EX2_03D_claim_status":"PROVISIONAL_CLAIM_DAG_SYNCHRONIZED_NOT_HOSTILE_AUDITED"
})
s["freshness"].update({
 "last_reconciled_current_main_sha":CURRENT_MAIN,
 "current_main_observed_sha":CURRENT_MAIN,
 "unreconciled_main_commit_count":0,
 "freshness_sync_deferred_until_retained_promotion_checkpoint":False
})
s["claim_sync"].update({
 "candidate_claim_id":CLAIM_ID,
 "checkpoint_claim_dag_complete":True,
 "claim_dag_integrity_verifier_passed":True,
 "active_frontier_verifier_passed":True,
 "current_main_reconciliation_required":False,
 "mathematical_frontier_semantics_changed":False,
 "promotion_attempted":False,
 "reason":"EX2-03D adds a narrow provisional structural claim for the five remaining zero curves: they are pairwise-disjoint rational conics with trivial O(V6) restrictions, reducing fixedness to one-dimensional evaluation/H1-jump control. MAIN authority/frontier is unchanged.",
 "reconciled_current_main_sha":CURRENT_MAIN,
 "required_verification_run":None,
 "shared_claim_files_written_from_stale_branch":False,
 "stage32_main_authority_changed":False,
 "status":"COMPLETE_CURRENT_MAIN_RECONCILED_LOCAL_DAG_VERIFIERS_PASS_EXACT_HEAD_CI_REQUIRED_BEFORE_AUDIT",
 "trigger":"RETAINED_CONSOLIDATION",
 "triggered_for_EX2_03D":True
})
s["credit"]["level"]="CERTIFIED_1D_ABSTRACT_SECTION_SUBSPACE_PLUS_BOUNDED_NEGATIVE_SCAN_PLUS_TWO_ZERO_CURVES_NONFIXED_PLUS_FIVE_CONIC_RESTRICTION_REDUCTION_NO_MEMBER_CREDIT"
s["credit"]["remaining_five_conic_restriction_reduction_obtained"]=True
s["current"].update({
 "leaf":"EX2-03E_FIVE_CONIC_RESTRICTION_EVALUATION_OR_H1_JUMP_PREFLIGHT",
 "status":"EX2_03D_FIVE_REMAINING_ZERO_CURVES_REDUCED_TO_TRIVIAL_CONIC_RESTRICTION_EVALUATION",
 "subroute":"FIVE_ONE_DIMENSIONAL_RESTRICTION_MAPS_OR_EQUIVALENT_H1_JUMP_CONTROL",
 "objective":"For each C in [21,24,25,30,31], decide whether H0(S,O(V6))->H0(C,O_C)=Qbar is zero or nonzero, or equivalently control h1(V6-C)-h1(V6). Do not infer fixedness from degree zero, -4I5, or known140 omission UNSAT.",
 "next_route_on_success":"RETAIN_EXACT_FIXEDNESS_OR_NONFIXEDNESS_CLASSIFICATION_FOR_EACH_CONIC_WITH_SOURCE_BOUND_EVALUATION",
 "next_route_on_block":"ROUTE_TO_EX2_04_EXPLICIT_SECTION_IDEAL_SYZYGY_RECONSTRUCTION_OUTSIDE_KNOWN140_MONOID"
})
s["frontier"].update({
 "EX2_03D_compact_zero_curve_geometry_complete":True,
 "EX2_03D_remaining_five_are_pairwise_disjoint_rational_conics":True,
 "EX2_03D_remaining_five_intersection_matrix":"-4I5",
 "EX2_03D_remaining_five_restriction_bundle_abstractly_trivial":True,
 "EX2_03D_RR_chi_drop_each":1,
 "EX2_03D_h2_V6_minus_each_conic_zero":True,
 "EX2_03D_remaining_five_H0_restriction_maps_computed":False,
 "EX2_03D_remaining_five_fixedness_classified":False,
 "EX2_03E_five_conic_evaluation_preflight_active":True,
 "fixed_part_fully_classified":False,
 "moving_system_structure_classified":False,
 "full_target_closure":False
})
for k in ["trivial_conic_restriction_promoted_to_nonfixedness","trivial_conic_restriction_promoted_to_fixedness","rr_chi_drop_promoted_to_h0_drop"]:
    s["firewalls"][k]=False
s["current_leaf_working_set"]=[
 ART_PATH,VER_PATH,"stages/stage32-ex2/diagnose_ex2_03d_zero_curve_geometry.py",
 "stages/stage32-ex2/EX2-03/known140-zero-curve-omission-witnesses.json",
 "stages/stage32-ex2/verify_ex2_03c_omission_witnesses.py",
 "stages/stage32-ex2/EX2-03/zero-intersection-restriction-adapter-gap.json",
 "stages/stage32-ex2/verify_ex2_03_restriction_gap.py",
 "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json",
 "stages/stage32-ex2/verify_ex2_02_fixed_components.py",
 "stages/stage32-ex2/EX2-01/section-source-inventory.json",
 "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json",
 "stages/stage32-ex2/stage32-ex2.md",
 "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
]
dump(STATE,s)
VERIFY.write_text('#!/usr/bin/env python3\nfrom __future__ import annotations\nimport json, subprocess, sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[2]\nHERE=Path(__file__).resolve().parent\nS=json.loads((HERE/"MAIN-STATE.json").read_text())\nR=json.loads((ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json").read_text())\nL=json.loads((ROOT/"stages/stage32/proof/LANE-ADAPTERS.json").read_text())\nassert S["schema"]=="STAGE32EX2_MAIN_COMPACT_STATE_V9_EX2_03D_FIVE_CONIC_RESTRICTION_REDUCTION_EX2_03E_ACTIVE"\nassert S["stage"]=="32EX2"\nassert S["bootstrap"]["active_work_pr"]==1709 and S["bootstrap"]["merge_authorized"] is False\nassert S["audit"]["status"]=="NOT_READY_INTERMEDIATE_LEAF_ONLY"\nassert S["freshness"]["last_reconciled_current_main_sha"]=="f2a89e613cdf91191a0aada9e90c9fc93373a6c6"\nassert S["freshness"]["unreconciled_main_commit_count"]==0\nassert S["authority"]["EX2_03D_candidate_claim_id"]=="S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1"\nassert S["authority"]["EX2_03D_artifact_blob_sha1"]=="32e19797812f35ad15fc5cad7559be76140480ef"\nassert S["authority"]["EX2_03D_verifier_blob_sha1"]=="f7a3f88969b0599f20b0217e806f9441cfe68f01"\nF=S["frontier"]\nassert F["EX2_03_zero_curve_nonfixedness_classified_count"]==2\nassert F["EX2_03C_certified_nonfixed_zero_labels_1based"]==[17,98]\nassert F["EX2_03C_unresolved_zero_labels_1based"]==[21,24,25,30,31]\nassert F["EX2_03D_remaining_five_are_pairwise_disjoint_rational_conics"] is True\nassert F["EX2_03D_remaining_five_intersection_matrix"]=="-4I5"\nassert F["EX2_03D_remaining_five_restriction_bundle_abstractly_trivial"] is True\nassert F["EX2_03D_RR_chi_drop_each"]==1\nassert F["EX2_03D_h2_V6_minus_each_conic_zero"] is True\nassert F["EX2_03D_remaining_five_H0_restriction_maps_computed"] is False\nassert F["EX2_03D_remaining_five_fixedness_classified"] is False\nassert F["EX2_03E_five_conic_evaluation_preflight_active"] is True\nassert S["current"]["leaf"]=="EX2-03E_FIVE_CONIC_RESTRICTION_EVALUATION_OR_H1_JUMP_PREFLIGHT"\nassert S["completion_contract"]["terminal_outcome"] is None\nassert S["credit"]["genuine_v6_genus1_member_established"] is False\nassert S["credit"]["no_integral_irreducible_v6_genus1_member_in_linear_system"] is False\nassert S["credit"]["full_target_closure"] is False\nassert S["credit"]["stage32_main_credit"] is False\nfor k in ["trivial_conic_restriction_promoted_to_nonfixedness","trivial_conic_restriction_promoted_to_fixedness","rr_chi_drop_promoted_to_h0_drop","remaining_five_known140_unsat_promoted_to_fixedness","stage32_main_credit","Q602_excluded","O210_excluded","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:\n    assert S["firewalls"][k] is False, k\nclaims={c["claim_id"]:c for c in R["claims"]}\nc=claims["S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1"]\nassert c["authority_status"]=="PROVISIONAL"\nassert c["claim_core_sha256"]=="1a4220aae62ee856710131f5dd89173ced6ce3f40ecc741af349697677955576"\nex2=next(x for x in L["lanes"] if x["lane"]=="EX2")\nassert c["claim_id"] in ex2["claim_refs"]\nfor rel in [\n "verify_ex2_00_source_lock.py",\n "verify_ex2_01_section_sources.py",\n "verify_ex2_02_fixed_components.py",\n "verify_ex2_03_restriction_gap.py",\n "verify_ex2_03b_v6_stabilizer_orbit.py",\n "verify_ex2_03c_omission_witnesses.py",\n "verify_ex2_03d_five_conic_restriction.py",\n]:\n    subprocess.check_call([sys.executable,"-B",str(HERE/rel)],cwd=ROOT)\nprint("PASS Stage32EX2 MAIN state V9")\nprint("current_leaf=EX2-03E five one-dimensional conic restriction evaluations")\nprint("nonfixed_zero_curves=17,98 remaining=21,24,25,30,31")\nprint("merge_authorized=false stage32_main_credit=false")\n')
print("synced EX2-03D claim/state")
