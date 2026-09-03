#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
H = ROOT / 'stages/stage33'
D = H / '33-12'
LOC = ROOT / 'docs/evidence-locator'
MAIN = 'b05c925137c4bb17b1f6286fb27f6d4ba2d64937'
BLOBS = {
    LOC / 'index.json': 'a32d83a0e5529b444f0d5f58dcad44517b5fe087',
    LOC / 'query_evidence.py': '306205983a30932f318e33a0e78c1c53b7233593',
    LOC / 'stage32-post1498.json': '935bb4f0821af4fd451d45003d4e430a751e68ac',
    LOC / 'stage33.json': '0ecf26acd08170cea09aba3a4972cdb44428ca6e',
}
EXPECTED_CANDIDATE = 'EVID-S33-GERSTEN-CONNECTING-26COL-AUDITED'
LIMIT = 'this asset does not itself identify a standalone genuine full-surface H2(mu2) lift for any remaining retained10 adapted source'
NEXT = 'QUERY_ALL_CURRENT_EVIDENCE_REGISTRIES_THEN_CONSTRUCT_REMAINING_GENUINE_H2_MU2_LIFT_IF_NO_SUITABLE_HIT'
SCOPE = 'CURRENT_MULTI_REGISTRY_LOCATOR_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT'
CSCHEMA = 'STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V61_POST_V39_CURRENT_MULTI_REGISTRY_CONSTRUCTION_ACTIVE'
SSCHEMA = 'STAGE33_MAIN_COMPACT_STATE_V18_POST_V39_CURRENT_MULTI_REGISTRY_CONSTRUCTION_ACTIVE'

def csha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def blob(path):
    return subprocess.check_output(['git','hash-object','--',str(path)], cwd=ROOT, text=True).strip()

for path, sha in BLOBS.items():
    assert path.is_file() and blob(path) == sha, (path, blob(path), sha)

query = json.loads(subprocess.check_output([
    'python3','-B',str(LOC/'query_evidence.py'),
    'genuine full-surface H2(mu2) lift another retained10 adapted source e3 e1 e4 e5 e6 e7 e8 e9 e10',
    '--stage','33','--limit','20'
], cwd=ROOT, text=True))
assert query['schema'] == 'PERFECT_CUBOID_EVIDENCE_QUERY_RESULT_V3_MULTI_STAGE'
assert {x['file'] for x in query['registry_sources']} == {'index.json','stage32-post1498.json','stage33.json'}
match = next(x for x in query['matches'] if x['asset_id'] == EXPECTED_CANDIDATE)
assert LIMIT in match['limitations']
suitable = [x for x in query['matches'] if LIMIT not in x.get('limitations', [])]
assert suitable == [], suitable
assert query['firewalls']['query_miss_proves_repo_absence'] is False
assert query['firewalls']['locator_match_grants_mathematical_credit'] is False
assert query['firewalls']['live_stage_authority_must_be_refetched'] is True

policy_path = D / 'j2-post-v38-locator-first-construction-policy-v39.json'
p = json.loads(policy_path.read_text())
p['schema'] = 'STAGE33_POST_V39_CURRENT_MAIN_MULTI_REGISTRY_ROUTING_REPAIR_V40'
p['status'] = 'OPERATIONAL_ROUTING_REPAIR_CURRENT_MULTI_REGISTRY_NO_MATH_CHANGE'
sl = p.setdefault('source_locks', {})
sl['current_main_commit_sha'] = MAIN
sl['evidence_locator_index_blob_sha1'] = BLOBS[LOC/'index.json']
sl['evidence_locator_query_blob_sha1'] = BLOBS[LOC/'query_evidence.py']
sl['evidence_locator_stage32_post1498_blob_sha1'] = BLOBS[LOC/'stage32-post1498.json']
sl['evidence_locator_stage33_blob_sha1'] = BLOBS[LOC/'stage33.json']
sl['current_registry_paths'] = ['docs/evidence-locator/index.json','docs/evidence-locator/stage32-post1498.json','docs/evidence-locator/stage33.json']
p['current_locator_audit'] = {
    'query_schema': query['schema'],
    'query_terms': query['query'],
    'registry_sources': [x['file'] for x in query['registry_sources']],
    'match_count': query['match_count'],
    'bounded_candidate_asset_id': EXPECTED_CANDIDATE,
    'bounded_candidate_registry_file': match['registry_file'],
    'bounded_candidate_limitation': LIMIT,
    'suitable_direct_lift_hit': False,
    'classification': 'RELEVANT_CANDIDATE_BUT_NOT_STANDALONE_GENUINE_REMAINING_ADAPTED_SOURCE_LIFT',
    'construction_authorized_after_complete_query_and_bounded_classification': True,
}
rc = p.setdefault('routing_contract', {})
rc['locator_miss_definition'] = 'NO_SUITABLE_DIRECT_LIFT_AFTER_COMPLETE_CURRENT_MULTI_REGISTRY_QUERY_AND_BOUNDED_CANDIDATE_CLASSIFICATION'
rc['all_current_registries_must_be_queried_before_construction'] = True
rc['bounded_candidate_suitability_classification_required'] = True
rc['construction_authorized_after_complete_current_registry_query_with_no_suitable_hit'] = True
rc['broad_repository_or_history_fallback_after_miss'] = False
p.setdefault('audit_finding', {})['current_multi_registry_locator_required'] = True
p['audit_finding']['old_single_registry_empty_result_is_not_a_fresh_live_miss'] = True
p['audit_finding']['locator_miss_proves_repository_absence'] = False
p['current_leaf'] = {
    'target_source_label': 'e3',
    'action': NEXT,
    'suitable_direct_lift_hit': False,
    'bounded_candidate_asset_id': EXPECTED_CANDIDATE,
    'construction_authorized': True,
}
p.pop('canonical_sha256', None)
p_sha = csha(p)
p['canonical_sha256'] = p_sha
policy_path.write_text(json.dumps(p, indent=2, sort_keys=True) + '\n')

cpath = H / 'controller.json'
c = json.loads(cpath.read_text())
c['schema'] = CSCHEMA
c['advance_allowed'] = True
c['advance_scope'] = SCOPE
c['next_item'] = NEXT
c['current']['next_exact_leaf'] = NEXT
c['current']['status'] = 'CURRENT_LOCATOR_FIRST_CONSTRUCTION_ACTIVE_POST_V39_CURRENT_MULTI_REGISTRY'
c['execution']['advance_allowed'] = True
c['execution']['advance_scope'] = SCOPE
c['execution']['next_item'] = NEXT
c['post_v36_authority']['v39_operational_routing_policy_canonical_sha256'] = p_sha
r = c['post_v39_routing']
r['policy_v39_canonical_sha256'] = p_sha
r['status'] = 'ACTIVE_CURRENT_MULTI_REGISTRY_OPERATIONAL_ROUTING_NO_MATH_CHANGE'
r['current_main_commit_sha'] = MAIN
r['current_registry_paths'] = ['docs/evidence-locator/index.json','docs/evidence-locator/stage32-post1498.json','docs/evidence-locator/stage33.json']
r['current_registry_blob_sha1'] = {str(k.relative_to(ROOT)): v for k,v in BLOBS.items() if k.name != 'query_evidence.py'}
r['evidence_locator_query_blob_sha1'] = BLOBS[LOC/'query_evidence.py']
r['all_current_registries_must_be_queried_before_construction'] = True
r['bounded_candidate_suitability_classification_required'] = True
r['construction_authorized_after_locator_miss'] = True
r['locator_miss_definition'] = rc['locator_miss_definition']
r['bounded_current_candidate_asset_id'] = EXPECTED_CANDIDATE
r['bounded_current_candidate_suitable_direct_lift'] = False
r['next_exact_leaf'] = NEXT
c['loop_state']['last_cycle_route_status'] = 'POST_V39_CURRENT_MULTI_REGISTRY_LOCATOR_FIRST_CONSTRUCTION_ACTIVE'
c['loop_state']['last_new_view'] = 'Hostile-audit repair: all current locator registries are queried; relevant candidates are boundedly classified before a no-suitable-hit construction route is authorized.'
c['current_exact_promotion_scope'] = 'V25_V36_EXACT_MATH_WITH_V39_CURRENT_MULTI_REGISTRY_OPERATIONAL_ROUTING_NO_MATH_CHANGE'
c.pop('projection_canonical_sha256', None)
c_sha = csha(c)
c['projection_canonical_sha256'] = c_sha
cpath.write_text(json.dumps(c, sort_keys=True, separators=(',', ':')) + '\n')

sync = H / 'sync_main_state.py'
s = sync.read_text()
s = s.replace('STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V60_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE', CSCHEMA)
s = s.replace('STAGE33_MAIN_COMPACT_STATE_V17_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE', SSCHEMA)
s = s.replace('QUERY_EVIDENCE_LOCATOR_THEN_CONSTRUCT_REMAINING_GENUINE_H2_MU2_LIFT_IF_MISS', NEXT)
s = s.replace('LOCATOR_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT', SCOPE)
s = s.replace('2fddd4bda3d853a42656b32483cefd116677e5bd70f633dc4791440b0269b230', p_sha)
s = s.replace("ROOT / \"docs/evidence-locator/query_evidence.py\": \"84fd86fce8e1bc5966d47d453ebd7b60aaba3a9f\",", "ROOT / \"docs/evidence-locator/query_evidence.py\": \"306205983a30932f318e33a0e78c1c53b7233593\",\n    ROOT / \"docs/evidence-locator/stage32-post1498.json\": \"935bb4f0821af4fd451d45003d4e430a751e68ac\",\n    ROOT / \"docs/evidence-locator/stage33.json\": \"0ecf26acd08170cea09aba3a4972cdb44428ca6e\",")
s = s.replace('"docs/evidence-locator/query_evidence.py",\n        "stages/stage33/33-12/j2-post-v35-evidence-locator-handoff-v36.json"', '"docs/evidence-locator/query_evidence.py",\n        "docs/evidence-locator/stage32-post1498.json",\n        "docs/evidence-locator/stage33.json",\n        "stages/stage33/33-12/j2-post-v35-evidence-locator-handoff-v36.json"')
marker = 'for path, expected in LOCATOR_BLOBS.items():\n    assert path.is_file(), path\n    assert git_blob(path) == expected, path\n'
extra = marker + "\n# HOSTILE_AUDIT_CURRENT_MULTI_REGISTRY_V40\nq = json.loads(subprocess.check_output([\"python3\", \"-B\", str(ROOT / \"docs/evidence-locator/query_evidence.py\"), \"genuine full-surface H2(mu2) lift another retained10 adapted source e3 e1 e4 e5 e6 e7 e8 e9 e10\", \"--stage\", \"33\", \"--limit\", \"20\"], cwd=ROOT, text=True))\nassert q[\"schema\"] == \"PERFECT_CUBOID_EVIDENCE_QUERY_RESULT_V3_MULTI_STAGE\"\nassert {x[\"file\"] for x in q[\"registry_sources\"]} == {\"index.json\", \"stage32-post1498.json\", \"stage33.json\"}\nqm = next(x for x in q[\"matches\"] if x[\"asset_id\"] == \"EVID-S33-GERSTEN-CONNECTING-26COL-AUDITED\")\nassert \"this asset does not itself identify a standalone genuine full-surface H2(mu2) lift for any remaining retained10 adapted source\" in qm[\"limitations\"]\nassert not [x for x in q[\"matches\"] if \"this asset does not itself identify a standalone genuine full-surface H2(mu2) lift for any remaining retained10 adapted source\" not in x.get(\"limitations\", [])]\n"
if 'HOSTILE_AUDIT_CURRENT_MULTI_REGISTRY_V40' not in s:
    assert marker in s
    s = s.replace(marker, extra)
sync.write_text(s)

verifier = D / 'verify_j2_post_v38_locator_first_construction_policy_v39.py'
verifier.write_text(f'''#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
ROOT = STAGE33.parent.parent
LOC = ROOT / "docs/evidence-locator"
EXPECTED = "{p_sha}"
MAIN = "{MAIN}"
BLOBS = {{
    LOC / "index.json": "a32d83a0e5529b444f0d5f58dcad44517b5fe087",
    LOC / "query_evidence.py": "306205983a30932f318e33a0e78c1c53b7233593",
    LOC / "stage32-post1498.json": "935bb4f0821af4fd451d45003d4e430a751e68ac",
    LOC / "stage33.json": "0ecf26acd08170cea09aba3a4972cdb44428ca6e",
}}
LIMIT = {LIMIT!r}
def csha(o): return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def git_blob(path): return subprocess.check_output(["git","hash-object","--",str(path)], cwd=ROOT, text=True).strip()
p = json.loads((HERE / "j2-post-v38-locator-first-construction-policy-v39.json").read_text())
pb = dict(p); claimed = pb.pop("canonical_sha256")
assert claimed == EXPECTED == csha(pb)
assert p["source_locks"]["current_main_commit_sha"] == MAIN
for path, sha in BLOBS.items(): assert path.is_file() and git_blob(path) == sha, path
q = json.loads(subprocess.check_output(["python3","-B",str(LOC / "query_evidence.py"), "genuine full-surface H2(mu2) lift another retained10 adapted source e3 e1 e4 e5 e6 e7 e8 e9 e10", "--stage","33","--limit","20"], cwd=ROOT, text=True))
assert q["schema"] == "PERFECT_CUBOID_EVIDENCE_QUERY_RESULT_V3_MULTI_STAGE"
assert {{x["file"] for x in q["registry_sources"]}} == {{"index.json","stage32-post1498.json","stage33.json"}}
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
assert c["schema"] == {CSCHEMA!r}
assert c["post_v39_routing"]["policy_v39_canonical_sha256"] == EXPECTED
assert c["post_v39_routing"]["current_main_commit_sha"] == MAIN
assert c["post_v39_routing"]["all_current_registries_must_be_queried_before_construction"] is True
assert c["post_v39_routing"]["bounded_candidate_suitability_classification_required"] is True
assert c["post_v39_routing"]["bounded_current_candidate_suitable_direct_lift"] is False
assert c["advance_allowed"] is True and c["execution"]["advance_allowed"] is True
assert c["advance_scope"] == {SCOPE!r}
assert c["current"]["next_exact_leaf"] == c["next_item"] == c["execution"]["next_item"] == {NEXT!r}
state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
sb = dict(state); sclaimed = sb.pop("canonical_sha256")
assert sclaimed == csha(sb)
assert state["schema"] == {SSCHEMA!r}
assert state["controller_projection_canonical_sha256"] == cclaimed
assert state["execution_gate"]["advance_scope"] == {SCOPE!r}
print(json.dumps({{"success": True, "marker": "PROOF_REPLAY_COMPLETE", "current_main": MAIN, "query_schema": q["schema"], "registry_sources": [x["file"] for x in q["registry_sources"]], "bounded_candidate": m["asset_id"], "suitable_direct_lift_hit": False, "construction_authorized": True, "policy_canonical_sha256": EXPECTED, "controller_projection_canonical_sha256": cclaimed, "main_state_canonical_sha256": sclaimed, "mathematical_change": False}}, sort_keys=True))
''')

# Keep startup wording honest about candidate classification.
for path in [H/'MAIN-START-HERE.md', H/'CURRENT.md']:
    t = path.read_text()
    note = '\n## Hostile-audit multi-registry repair\n\nCurrent-main locator routing means `index.json`, `stage32-post1498.json`, and `stage33.json` are all searched before construction. A nonempty candidate list is not a suitable-hit verdict: inspect only the bounded candidate limitations. The current Stage33 Gersten 26-column candidate is relevant but explicitly does not itself identify a standalone genuine remaining retained10 H2(mu2) lift, so construction is authorized only after that bounded classification.\n'
    if 'Hostile-audit multi-registry repair' not in t:
        path.write_text(t.rstrip() + '\n' + note)

subprocess.run(['python3', str(sync)], cwd=ROOT, check=True)
subprocess.run(['python3', str(verifier)], cwd=ROOT, check=True)
subprocess.run(['python3', str(sync), '--check'], cwd=ROOT, check=True)
subprocess.run(['git','diff','--check'], cwd=ROOT, check=True)
print(json.dumps({'success': True, 'marker': 'STAGE33_CURRENT_MULTI_REGISTRY_AUDIT_REPAIR_APPLIED', 'policy_sha': p_sha, 'controller_sha': c_sha}, sort_keys=True))
