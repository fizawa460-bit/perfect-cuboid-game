#!/usr/bin/env python3
"""One-shot Stage33 V39 routing repair: locator-first, construct-on-miss."""
from __future__ import annotations
import hashlib, json, shutil, subprocess
from pathlib import Path

H = Path(__file__).resolve().parent
ROOT = H.parent.parent
D = H / "33-12"
POLICY = D / "j2-post-v38-locator-first-construction-policy-v39.json"
POLICY_SHA = "2fddd4bda3d853a42656b32483cefd116677e5bd70f633dc4791440b0269b230"
OLD_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V59_POST_V36_FIRST_ADAPTED_COLUMN_REUSE_STOP"
NEW_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V60_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE"
NEXT = "QUERY_EVIDENCE_LOCATOR_THEN_CONSTRUCT_REMAINING_GENUINE_H2_MU2_LIFT_IF_MISS"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

p = json.loads(POLICY.read_text())
pb = dict(p)
assert pb.pop("canonical_sha256") == POLICY_SHA == csha(pb)

cp = H / "controller.json"
c = json.loads(cp.read_text())
assert c["schema"] == OLD_SCHEMA, c["schema"]
cb = dict(c)
old_projection = cb.pop("projection_canonical_sha256")
assert old_projection == csha(cb)

c["schema"] = NEW_SCHEMA
c["advance_allowed"] = True
c["advance_scope"] = "LOCATOR_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT"
c["next_item"] = NEXT
c["current_exact_promotion_scope"] = "V25_V36_EXACT_MATH_WITH_V39_OPERATIONAL_ROUTING_NO_MATH_CHANGE"
c["current"].update({
    "status": "CURRENT_LOCATOR_FIRST_CONSTRUCTION_ACTIVE_POST_V39",
    "substep": "LOCATOR_FIRST_THEN_CONSTRUCT_GENUINE_H2_MU2_LIFT",
    "next_exact_leaf": NEXT,
})
c["execution"].update({
    "advance_allowed": True,
    "advance_scope": "LOCATOR_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT",
    "next_item": NEXT,
})
c["loop_state"].update({
    "active": True,
    "last_cycle_route_status": "POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE",
    "last_new_view": "V39 operational repair: #1498 remains the reuse-first locator; a suitable miss routes to new construction instead of parking ordinary MAIN.",
    "stagnation_count": 0,
})
pa = c["post_v36_authority"]
pa["status"] = "HISTORICAL_EXACT_V36_BOUNDARY_OPERATIONAL_STOP_SUPERSEDED_BY_V39"
pa["next_exact_leaf"] = "HISTORICAL_V36_STOP_SUPERSEDED_BY_V39"
pa["broad_historical_search_permitted"] = False
pa["v39_operational_routing_policy_canonical_sha256"] = POLICY_SHA

remaining = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
c["post_v39_routing"] = {
    "status": "ACTIVE_OPERATIONAL_ROUTING_NO_MATH_CHANGE",
    "policy_v39_canonical_sha256": POLICY_SHA,
    "evidence_locator_pr": 1498,
    "evidence_locator_index_path": "docs/evidence-locator/index.json",
    "evidence_locator_query_path": "docs/evidence-locator/query_evidence.py",
    "query_locator_first_for_existing_evidence": True,
    "locator_miss_proves_repository_absence": False,
    "construction_authorized_after_locator_miss": True,
    "broad_historical_search_permitted": False,
    "broad_search_exceptions": p["routing_contract"]["broad_search_exceptions"],
    "register_new_reusable_positive_asset_after_exact_verification": True,
    "remaining_adapted_source_labels": remaining,
    "construction_priority": remaining,
    "next_exact_leaf": NEXT,
}
s = c["stage33_12"]
s["status"] = "OPEN_CURRENT_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE"
s["current_v39_locator_first_construction_policy_canonical_sha256"] = POLICY_SHA
s["current_v39_locator_miss_authorizes_new_construction"] = True
s["current_v39_broad_history_fallback_permitted"] = False
s["current_remaining_j2_adapted_source_labels"] = remaining
seq = s.get("logical_internal_sequence", [])
if seq:
    assert seq[0]["id"] == "33-13"
    seq[0]["status"] = "CURRENT_J2_ADAPTED_COLUMNS_1_OF_10_STANDARD_COLUMNS_0_OF_10_LOCATOR_FIRST_CONSTRUCTION_ACTIVE"

c.pop("projection_canonical_sha256", None)
c["projection_canonical_sha256"] = csha(c)
cp.write_text(json.dumps(c, sort_keys=True, separators=(",", ":")) + "\n")

shutil.copyfile(H / "v39-sync-main-state-template.py", H / "sync_main_state.py")
shutil.copyfile(H / "v39-main-start-template.md", H / "MAIN-START-HERE.md")
shutil.copyfile(H / "v39-current-template.md", H / "CURRENT.md")

v38p = D / "verify_j2_post_v36_controller_generator_sync_v38.py"
v38 = v38p.read_text()
needle = 'r = json.loads(RECEIPT.read_text())\n'
assert needle in v38
compat = 'controller_schema_now = json.loads((STAGE33 / "controller.json").read_text())["schema"]\nif controller_schema_now == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V60_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE":\n    import runpy\n    runpy.run_path(str(HERE / "verify_j2_post_v38_locator_first_construction_policy_v39.py"), run_name="__main__")\n    raise SystemExit(0)\n\n'
if "controller_schema_now" not in v38:
    v38 = v38.replace(needle, compat + needle, 1)
v38p.write_text(v38)

wfpath = ROOT / ".github/workflows/stage33-12-main.yml"
wf = wfpath.read_text()
wf = wf.replace(
    "# Stage33 state is checked through the exact V21-V38 authority chain and the\n# synchronized V59 compact-state generator.",
    "# Stage33 mathematics is replayed through V36; V39 verifies the locator-first\n# operational routing repair and synchronized V60/V17 compact-state generator."
)
if "docs/evidence-locator/**" not in wf:
    wf = wf.replace(
        "      - 'stages/stage33/sync_main_state.py'\n",
        "      - 'stages/stage33/sync_main_state.py'\n      - 'docs/evidence-locator/**'\n      - 'docs/research-os/policies/repository-asset-discovery.md'\n"
    )
old_block = '''          # V35/V36 are handoff/STOP certificates; V37 is the superseded
          # operational repair receipt. V38 verifies the synchronized V59/V16
          # controller-generator projection without granting mathematical credit.
          python stages/stage33/33-12/verify_j2_post_v36_controller_generator_sync_v38.py
'''
new_block = '''          # V35/V36 remain exact historical handoff/locator-miss evidence.
          # V39 supersedes only the operational STOP: query #1498 first, then
          # construct the missing exact lift on a suitable locator miss.
          python stages/stage33/33-12/verify_j2_post_v38_locator_first_construction_policy_v39.py
'''
assert old_block in wf
wf = wf.replace(old_block, new_block)
wf = wf.replace(
    "# Promotion audit remains historical/read-only. The synchronized V59\n          # generator must reproduce MAIN-STATE exactly.",
    "# Promotion audit remains historical/read-only. The synchronized V60/V17\n          # generator must reproduce MAIN-STATE exactly."
)
wfpath.write_text(wf)

subprocess.run(["python", str(H / "sync_main_state.py")], cwd=ROOT, check=True)
subprocess.run(["python", str(D / "verify_j2_post_v38_locator_first_construction_policy_v39.py")], cwd=ROOT, check=True)
subprocess.run(["python", str(H / "sync_main_state.py"), "--check"], cwd=ROOT, check=True)
subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
print(json.dumps({
    "success": True,
    "old_controller_projection_canonical_sha256": old_projection,
    "new_controller_projection_canonical_sha256": c["projection_canonical_sha256"],
    "controller_schema": NEW_SCHEMA,
    "policy_v39_canonical_sha256": POLICY_SHA,
    "advance_allowed": True,
    "advance_scope": c["advance_scope"],
    "marker": "STAGE33_V39_ROUTING_REPAIR_APPLIED",
}, sort_keys=True))
