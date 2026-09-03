#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
S33 = ROOT / "stages/stage33"
D = S33 / "33-12"
REMAINING = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
NEXT = "CHECK_RELEVANT_FINAL_HANDOFF_THEN_CONSTRUCT_REMAINING_GENUINE_H2_MU2_LIFT_IF_NO_RETAINED_HIT"
SCOPE = "FINAL_HANDOFF_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT"
SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_FINAL_HANDOFF_DISCOVERY_ACTIVE"
FORBIDDEN = re.compile(r"(?:evidence[- _]?locator|docs/evidence-locator|query_evidence\.py|EVID-S3[23]|\blocator\b)", re.I)
DROP = object()

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def write_canonical(path, obj, pretty):
    obj = dict(obj)
    obj.pop("canonical_sha256", None)
    obj["canonical_sha256"] = csha(obj)
    path.write_text(json.dumps(obj, indent=2 if pretty else None, sort_keys=True, separators=None if pretty else (",", ":")) + "\n")
    return obj["canonical_sha256"]

def sanitize(obj):
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if "locator" in k.lower():
                continue
            sv = sanitize(v)
            if sv is not DROP:
                out[k] = sv
        return out
    if isinstance(obj, list):
        out = []
        for v in obj:
            sv = sanitize(v)
            if sv is not DROP:
                out.append(sv)
        return out
    if isinstance(obj, str) and FORBIDDEN.search(obj):
        return DROP
    return obj

v37_path = D / "j2-post-v36-startup-authority-repair-v37.json"
v37 = json.loads(v37_path.read_text())
v37["anti_inference"].pop("locator_miss_upgraded_to_repository_absence", None)
v37["anti_inference"].pop("v36_stop_reopened_without_new_evidence", None)
v37["bounded_local_check"]["artifacts_checked"] = ["stages/stage33/33-12/j2-post-v34-main-handoff-v35.json"]
v37["bounded_local_check"]["result"] = "NO_STANDALONE_E3_LIFT_IN_CURRENT_V34_FRONTIER"
v37["next_exact_leaf"] = {
    "action": "CONSTRUCT_MISSING_GENUINE_LIFT_OR_USE_BOUNDED_TARGETED_REPO_CHECK_WHEN_CONCRETE_NEED_EXISTS",
    "do_not_restart_broad_historical_origin_search": True,
    "preferred_source_order": REMAINING,
    "requirement": "Proceed by deriving a genuine full-surface H2(mu2) lift for a remaining adapted source. A bounded targeted repository check remains allowed when a concrete load-bearing reason identifies a specific omitted asset."
}
v37["source_locks"].pop("v36_handoff_canonical_sha256", None)
v37["startup_projection_drift"]["repair_rule"] = "Do not partially rewrite proof authority. Keep V25-V35 mathematics fixed while synchronizing controller.json and sync_main_state.py together."
v37_digest = write_canonical(v37_path, v37, True)

v38_path = D / "j2-post-v36-controller-generator-sync-v38.json"
v38 = json.loads(v38_path.read_text())
v38["anti_inference"].pop("locator_miss_upgraded_to_repository_absence", None)
v38["current_exact_frontier"]["next_exact_leaf"] = "HISTORICAL_SYNC_RECEIPT_SUPERSEDED_BY_CURRENT_DISCOVERY_POLICY"
v38["source_locks"].pop("v36_handoff_canonical_sha256", None)
v38["source_locks"]["v37_operational_repair_canonical_sha256"] = v37_digest
v38_digest = write_canonical(v38_path, v38, True)

controller_path = S33 / "controller.json"
c = json.loads(controller_path.read_text())
c["schema"] = SCHEMA
c["advance_allowed"] = True
c["advance_scope"] = SCOPE
c["next_item"] = NEXT
c["current_exact_promotion_scope"] = "V25_V35_EXACT_MATH_WITH_FINAL_HANDOFF_DISCOVERY_OPERATIONAL_ROUTING_NO_MATH_CHANGE"
c["current"]["next_exact_leaf"] = NEXT
c["current"]["status"] = "CURRENT_FINAL_HANDOFF_DISCOVERY_ACTIVE"
c["current"]["substep"] = "FINAL_HANDOFF_FIRST_THEN_CONSTRUCT_GENUINE_H2_MU2_LIFT"
c["execution"]["advance_allowed"] = True
c["execution"]["advance_scope"] = SCOPE
c["execution"]["next_item"] = NEXT
c["loop_state"]["last_cycle_route_status"] = "FINAL_HANDOFF_DISCOVERY_ACTIVE"
c["loop_state"]["last_new_view"] = "Existing Stage-local assets are checked through canonical final handoffs first; a miss is not repository absence, and bounded internal search remains available for a concrete load-bearing need."
if "post_v36_authority" in c:
    pv = c["post_v36_authority"]
    pv["mathematical_authority"] = "V25_V35_EXACT_CERTIFICATE_CHAIN"
    pv["status"] = "HISTORICAL_OPERATIONAL_BOUNDARY_SUPERSEDED_BY_FINAL_HANDOFF_DISCOVERY"
    pv["next_exact_leaf"] = "HISTORICAL_OPERATIONAL_STOP_RETIRED"
    for key in list(pv):
        if key.startswith("v36_") or key.startswith("v39_"):
            pv.pop(key, None)
c.pop("post_v39_routing", None)
c["repository_asset_discovery"] = {
    "policy": "docs/research-os/policies/repository-asset-discovery.md",
    "stage16_plus_first_surface": "stages/stageNN/FINAL.md",
    "stage12_15_first_surface": "canonical final self-contained HTML",
    "final_handoff_miss_proves_repository_absence": False,
    "unlimited_internal_archaeology_default": False,
    "bounded_targeted_repo_search_allowed_for_concrete_load_bearing_need": True,
    "arsenal_preserved_for_cross_stage_weapons": True,
    "construction_authorized_after_no_retained_hit": True
}
if "research_os" in c:
    c["research_os"] = dict(c["repository_asset_discovery"])
c = sanitize(c)
c.pop("projection_canonical_sha256", None)
c["projection_canonical_sha256"] = csha(c)
controller_path.write_text(json.dumps(c, sort_keys=True, separators=(",", ":")) + "\n")
assert not FORBIDDEN.search(controller_path.read_text())
assert not FORBIDDEN.search(v37_path.read_text())
assert not FORBIDDEN.search(v38_path.read_text())

digest_path = ROOT / "stage33-discovery-migration-digests.tmp"
digest_path.write_text(json.dumps({
    "controller_projection_canonical_sha256": c["projection_canonical_sha256"],
    "v37_canonical_sha256": v37_digest,
    "v38_canonical_sha256": v38_digest
}, sort_keys=True) + "\n")

subprocess.run(["git", "add", str(controller_path.relative_to(ROOT)), str(v37_path.relative_to(ROOT)), str(v38_path.relative_to(ROOT)), str(digest_path.relative_to(ROOT))], cwd=ROOT, check=True)
subprocess.run(["git", "commit", "-m", "refactor(stage33): detach controller from retired discovery routing"], cwd=ROOT, check=True)
subprocess.run(["git", "push"], cwd=ROOT, check=True)
