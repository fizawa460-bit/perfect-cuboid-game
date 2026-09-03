#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
ROOT = STAGE33.parent.parent
LOC = ROOT / "docs/evidence-locator"
EXPECTED = "26e47d41b94caf1cb931f765468d6779a760adec434d4b1b6698f838b3db46b2"
MAIN = "b05c925137c4bb17b1f6286fb27f6d4ba2d64937"
BLOBS = {
    LOC / "index.json": "a32d83a0e5529b444f0d5f58dcad44517b5fe087",
    LOC / "query_evidence.py": "306205983a30932f318e33a0e78c1c53b7233593",
    LOC / "stage32-post1498.json": "935bb4f0821af4fd451d45003d4e430a751e68ac",
    LOC / "stage33.json": "0ecf26acd08170cea09aba3a4972cdb44428ca6e",
}
LIMIT = 'this asset does not itself identify a standalone genuine full-surface H2(mu2) lift for any remaining retained10 adapted source'
def csha(o): return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def git_blob(path): return subprocess.check_output(["git","hash-object","--",str(path)], cwd=ROOT, text=True).strip()
p = json.loads((HERE / "j2-post-v38-locator-first-construction-policy-v39.json").read_text())
pb = dict(p); claimed = pb.pop("canonical_sha256")
assert claimed == EXPECTED == csha(pb)
assert p["source_locks"]["current_main_commit_sha"] == MAIN
for path, sha in BLOBS.items(): assert path.is_file() and git_blob(path) == sha, path
q = json.loads(subprocess.check_output(["python3","-B",str(LOC / "query_evidence.py"), "genuine full-surface H2(mu2) lift another retained10 adapted source e3 e1 e4 e5 e6 e7 e8 e9 e10", "--stage","33","--limit","20"], cwd=ROOT, text=True))
assert q["schema"] == "PERFECT_CUBOID_EVIDENCE_QUERY_RESULT_V3_MULTI_STAGE"
assert {x["file"] for x in q["registry_sources"]} == {"index.json","stage32-post1498.json","stage33.json"}
m = next(x for x in q["matches"] if x["asset_id"] == "EVID-S33-GERSTEN-CONNECTING-26COL-AUDITED")
assert m["registry_file"] == "stage33.json" and LIMIT in m["limitations"]
suitable = [x for x in q["matches"] if LIMIT not in x.get("limitations", [])]
assert suitable == [], suitable
assert p["current_locator_audit"]["suitable_direct_lift_hit"] is False
assert p["current_locator_audit"]["construction_authorized_after_complete_query_and_bounded_classification"] is True
assert p["audit_finding"]["old_single_registry_empty_result_is_not_a_fresh_live_miss"] is True
assert q["firewalls"]["query_miss_proves_repo_absence"] is False
assert q["firewalls"]["locator_match_grants_mathematical_credit"] is False
assert q["firewalls"]["live_stage_authority_must_be_refetched"] is True
c = json.loads((STAGE33 / "controller.json").read_text())
cb = dict(c); cclaimed = cb.pop("projection_canonical_sha256")
assert cclaimed == csha(cb)
assert c["schema"] == 'STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V61_POST_V39_CURRENT_MULTI_REGISTRY_CONSTRUCTION_ACTIVE'
assert c["post_v39_routing"]["policy_v39_canonical_sha256"] == EXPECTED
assert c["post_v39_routing"]["current_main_commit_sha"] == MAIN
assert c["post_v39_routing"]["all_current_registries_must_be_queried_before_construction"] is True
assert c["post_v39_routing"]["bounded_candidate_suitability_classification_required"] is True
assert c["post_v39_routing"]["bounded_current_candidate_suitable_direct_lift"] is False
assert c["advance_allowed"] is True and c["execution"]["advance_allowed"] is True
assert c["advance_scope"] == 'CURRENT_MULTI_REGISTRY_LOCATOR_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT'
assert c["current"]["next_exact_leaf"] == c["next_item"] == c["execution"]["next_item"] == 'QUERY_ALL_CURRENT_EVIDENCE_REGISTRIES_THEN_CONSTRUCT_REMAINING_GENUINE_H2_MU2_LIFT_IF_NO_SUITABLE_HIT'
state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
sb = dict(state); sclaimed = sb.pop("canonical_sha256")
assert sclaimed == csha(sb)
assert state["schema"] == 'STAGE33_MAIN_COMPACT_STATE_V18_POST_V39_CURRENT_MULTI_REGISTRY_CONSTRUCTION_ACTIVE'
assert state["controller_projection_canonical_sha256"] == cclaimed
assert state["execution_gate"]["advance_scope"] == 'CURRENT_MULTI_REGISTRY_LOCATOR_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT'
print(json.dumps({"success": True, "marker": "PROOF_REPLAY_COMPLETE", "current_main": MAIN, "query_schema": q["schema"], "registry_sources": [x["file"] for x in q["registry_sources"]], "bounded_candidate": m["asset_id"], "suitable_direct_lift_hit": False, "construction_authorized": True, "policy_canonical_sha256": EXPECTED, "controller_projection_canonical_sha256": cclaimed, "main_state_canonical_sha256": sclaimed, "mathematical_change": False}, sort_keys=True))
