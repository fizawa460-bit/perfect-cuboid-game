#!/usr/bin/env python3
"""One-shot overlay of the exact V25-V36 frontier onto Stage33 controller V59."""
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
H = ROOT / "stages/stage33"
D = H / "33-12"
P = H / "controller.json"
REMAINING = ["e3","e1","e4","e5","e6","e7","e8","e9","e10"]
NEXT = "WAIT_FOR_NEW_GENUINE_H2_MU2_LIFT_OR_REGISTERED_POSITIVE_EVIDENCE_ASSET"
SCOPE = "STOP_REUSE_FIRST_UNTIL_NEW_GENUINE_H2_MU2_LIFT_OR_REGISTERED_POSITIVE_EVIDENCE_ASSET"
LOCKS = {
 "v25": (D/"j2-genuine-h2-mu2-kummer-adapter-v25.json","d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
 "v33": (D/"j2-current-hs-d2-nonzero-v33.json","59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f"),
 "v34": (D/"j2-adapted-first-kummer-column-v34.json","eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e"),
 "v35": (D/"j2-post-v34-main-handoff-v35.json","4837ebeb0dd4ea97f196f6e4a405923eede73b53f663f9e0acac66aaf4e5f8e9"),
 "v36": (D/"j2-post-v35-evidence-locator-handoff-v36.json","065c0ca8a92ad0994a88b2a62337a0ceb33af9823e746590e7de590676d6db7c"),
 "v37": (D/"j2-post-v36-startup-authority-repair-v37.json","8b3da6a1b747a39a54f329959d3cac0073ec1bc57c21acf9a71f979194de8dcf"),
}
def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def locked(p,h):
 x=json.loads(p.read_text()); b=dict(x); got=b.pop("canonical_sha256"); assert got==h==csha(b),p; return x
z={k:locked(*v) for k,v in LOCKS.items()}
assert z["v25"]["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True
assert z["v33"]["exact_information_boundary"]["current_hs_d2_nonzero_proved"] is True
assert z["v34"]["exact_information_boundary"]["adapted_kummer_columns_materialized"]==1
assert z["v34"]["exact_information_boundary"]["original_standard_kummer_columns_materialized"]==0
assert z["v36"]["bounded_reuse_first_search"]["positive_asset_match_materialized"] is False
assert z["v36"]["bounded_reuse_first_search"]["old_origin_search_restarted"] is False
c=json.loads(P.read_text())
assert c["schema"]=="STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V58_NAMED_J2_SOURCE_EXACT_GENUINE_KUMMER_ADAPTER_MISSING"
assert c["stage33_progress"]=="6/11" and c["merge_allowed"] is False
c["schema"]="STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V59_POST_V36_FIRST_ADAPTED_COLUMN_REUSE_STOP"
c["advance_allowed"]=False; c["advance_scope"]=SCOPE; c["next_item"]=NEXT
c["current_exact_promotion_scope"]="V25_V36_GENUINE_NAMED_J2_LIFT_CURRENT_HS_D2_FIRST_ADAPTED_COLUMN_AND_REUSE_STOP"
c["current"].update({"unit":"33-12","logical_internal_branch":"33-13_FINITE_V4_KUMMER_MATRIX_REPAIR","substep":"WAIT_FOR_NEW_GENUINE_H2_MU2_LIFT_OR_POSITIVE_EVIDENCE_ASSET","active_missing_interface":"STANDALONE_GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_ONE_REMAINING_J2_ADAPTED_SOURCE","next_exact_leaf":NEXT,"status":"CURRENT_STOP_REUSE_FIRST_POST_V36"})
c["execution"].update({"advance_allowed":False,"advance_scope":SCOPE,"next_item":NEXT,"next_expected_command":"Stage33-main-batch","heavy_actions_authorized":False,"merge_allowed":False})
c["loop_state"]={"active":False,"last_cycle_route_status":"POST_V36_REUSE_FIRST_STOP_NO_POSITIVE_GENUINE_LIFT_ASSET","last_new_view":"V25 genuine named-J2 lift; V33 current HS d2 nonzero; V34 one J2-adapted column; V36 reuse-first STOP with no additional registered genuine-lift asset.","stagnation_count":0}
s=c["stage33_12"]
s.update({"status":"OPEN_CURRENT_POST_V36_FIRST_J2_ADAPTED_COLUMN_REUSE_STOP","minimal_missing_exact_datum":"STANDALONE_GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_ONE_REMAINING_J2_ADAPTED_SOURCE","corrected_J2_actual_kummer_target_materialized":True,"corrected_J2_actual_kummer_target_materialized_via_v25":True,"corrected_J2_surface_mu2_lift_materialized":True,"corrected_J2_surface_mu2_lift_scope":"GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_CURRENT_NAMED_J2_V25","current_v25_genuine_h2_mu2_adapter_canonical_sha256":LOCKS["v25"][1],"current_v33_named_J2_hs_d2_nonzero":True,"current_v33_named_J2_hs_d2_canonical_sha256":LOCKS["v33"][1],"current_v34_j2_adapted_columns_materialized":1,"current_v34_j2_adapted_columns_total":10,"current_v34_original_standard_columns_materialized":0,"current_v34_j2_adapted_first_column_canonical_sha256":LOCKS["v34"][1],"current_v34_standard_basis_relation":"standard_col_2 XOR standard_col_3 = J2_adapted_col_1","current_v34_standard_col2_materialized":False,"current_v34_standard_col3_materialized":False,"current_v35_handoff_canonical_sha256":LOCKS["v35"][1],"current_v36_reuse_first_handoff_canonical_sha256":LOCKS["v36"][1],"current_v36_positive_asset_match_materialized":False,"current_v36_old_origin_search_restarted":False,"current_remaining_j2_adapted_source_labels":REMAINING,"finite_v4_kummer_adapted_columns_materialized":1,"finite_v4_kummer_adapted_columns_total":10,"finite_v4_kummer_columns_materialized":0,"first_exact_kummer_column_materialized":True,"first_exact_kummer_column_basis":"J2_ADAPTED_RETAINED10"})
if s.get("logical_internal_sequence"): s["logical_internal_sequence"][0]["status"]="CURRENT_J2_ADAPTED_COLUMNS_1_OF_10_STANDARD_COLUMNS_0_OF_10_REUSE_STOP"
c["post_v36_authority"]={"status":"SYNCHRONIZED_EXACT_PROJECTION_NO_MATH_CHANGE","mathematical_authority":"V25_V36_EXACT_CERTIFICATE_CHAIN","v25_genuine_h2_mu2_adapter_canonical_sha256":LOCKS["v25"][1],"v33_current_hs_d2_nonzero_canonical_sha256":LOCKS["v33"][1],"v34_first_adapted_column_canonical_sha256":LOCKS["v34"][1],"v35_handoff_canonical_sha256":LOCKS["v35"][1],"v36_handoff_canonical_sha256":LOCKS["v36"][1],"v37_operational_repair_receipt_canonical_sha256":LOCKS["v37"][1],"j2_adapted_columns_materialized":1,"original_standard_columns_materialized":0,"remaining_adapted_source_labels":REMAINING,"next_exact_leaf":NEXT,"broad_historical_search_permitted":False,"synthetic_standard_column_split_permitted":False}
c.pop("projection_canonical_sha256",None); c["projection_canonical_sha256"]=csha(c)
P.write_text(json.dumps(c,sort_keys=True,separators=(",",":"))+"\n")
subprocess.run(["python",str(H/"sync_main_state.py")],check=True)
subprocess.run(["python",str(H/"sync_main_state.py"),"--check"],check=True)
print(json.dumps({"success":True,"controller_schema":c["schema"],"controller_projection_canonical_sha256":c["projection_canonical_sha256"],"authority_sync":"SYNCHRONIZED_POST_V36","mathematical_change":False},sort_keys=True))
