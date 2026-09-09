#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/"stages/stage32-ex3/ex3-09-o210-cover-geometry-exclusion-candidate.json"
def bsha(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def csha(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
a=json.loads(ART.read_text())
assert a["status"]=="RETAINED_PROVISIONAL_TERMINAL_CANDIDATE_CLAIM_SYNC_PENDING_UNAUDITED"
assert csha(a)==a["canonical_sha256_without_this_field"]
L=a["source_locks"]
for k,v in L.items():
    p=ROOT/v["path"]; assert bsha(p)==v["blob_sha1"],k
    if "canonical_sha256" in v: assert csha(json.loads(p.read_text()))==v["canonical_sha256"],k
road=(ROOT/L["roadmap"]["path"]).read_text()
for m in ["O210_COVER_GEOMETRY_EXCLUDED","EX3-09","population-preserving","finite monodromy"]: assert m in road
tower=json.loads((ROOT/L["typed_cover_tower"]["path"]).read_text())
assert tower["verdict"]["EX3_00_source_lock_complete"] and tower["verdict"]["typed_cover_tower_complete"]
gate=json.loads((ROOT/L["self_contained_trace_gate"]["path"]).read_text())
assert gate["verdict"]["retained"] and not gate["verdict"]["hostile_audited"]
assert gate["verdict"]["provisional_terminal_candidate"]=="O210_COVER_GEOMETRY_EXCLUDED"
assert gate["q602_contradiction"]["graph_geometry_forced_trace"]==0 and gate["q602_contradiction"]["required_trace_mod8"]==4
assert not gate["q602_contradiction"]["zero_is_allowed"]
runpy.run_path(str(ROOT/L["self_contained_trace_verifier"]["path"]),run_name="__ex3_04h__")
p=a["population_exhaustiveness"]
assert p["population_preserving_from_carrier_hypothesis"] and not p["finite_monodromy_search_used"]
assert not p["monodromy_or_nielsen_case_choice_enters_argument"] and p["later_casework_dominated_not_claimed_executed"]
assert p["dominated_roadmap_leaves"]==["EX3-05","EX3-06","EX3-07","EX3-08"]
t=a["terminal_proposal"]
assert t["outcome"]=="O210_COVER_GEOMETRY_EXCLUDED" and t["mathematical_terminal_candidate_complete"] and t["full_target_closure_candidate"]
r=a["checkpoint_readiness"]
assert r["currently_retained"] and not r["currently_claim_synced"] and not r["currently_hostile_audited"]
assert r["ready_for_claim_dag_sync"] and r["ready_for_hostile_audit_after_claim_sync"]
for k in ["EX3_audited_authority","O210_excluded_as_audited_stage32_fact","Q602_globally_excluded","stage32_main_credit","stage32_closed","endpoint_credit"]:
    assert a["credit_ceiling"][k] is False
print("PASS Stage32EX3 EX3-09 retained terminal candidate; claim sync pending")
print(json.dumps({"terminal_candidate":"O210_COVER_GEOMETRY_EXCLUDED","retained":True,"claim_sync_pending":True,"hostile_audited":False,"stage32_main_credit":False},sort_keys=True))
