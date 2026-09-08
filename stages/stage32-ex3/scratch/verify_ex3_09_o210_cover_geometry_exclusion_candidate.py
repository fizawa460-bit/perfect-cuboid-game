#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-09-o210-cover-geometry-exclusion-candidate.json"

def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def canonical_without(obj: dict, field: str = "canonical_sha256_without_this_field") -> str:
    x = dict(obj)
    x.pop(field, None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

a = json.loads(ART.read_text())
assert a["schema"] == "STAGE32EX3_EX3_09_O210_COVER_GEOMETRY_EXCLUSION_CANDIDATE_V1"
assert a["status"] == "SCRATCH_PROVISIONAL_TERMINAL_ASSEMBLY_READY_FOR_RETAINED_CONSOLIDATION_NOT_AUDITED"
assert canonical_without(a) == a["canonical_sha256_without_this_field"]

locks = a["source_locks"]
for name, lock in locks.items():
    p = ROOT / lock["path"]
    assert blob(p) == lock["blob_sha1"], f"blob drift: {name}"
    if "canonical_sha256" in lock:
        obj = json.loads(p.read_text())
        assert canonical_without(obj) == lock["canonical_sha256"], f"canonical drift: {name}"

roadmap = (ROOT / locks["roadmap"]["path"]).read_text()
for marker in ["O210_COVER_GEOMETRY_EXCLUDED","EX3-09","population-preserving","finite monodromy"]:
    assert marker in roadmap

tower = json.loads((ROOT / locks["typed_cover_tower"]["path"]).read_text())
assert tower["verdict"]["EX3_00_source_lock_complete"] is True
assert tower["verdict"]["typed_cover_tower_complete"] is True
assert tower["fixed_target"]["O"] == 210
assert tower["fixed_target"]["qprime"] == 4
assert tower["degree_adapter"]["n_pair_D_to_X8"] == [105,81]

gate = json.loads((ROOT / locks["self_contained_trace_gate"]["path"]).read_text())
assert gate["verdict"]["self_contained_without_scratch_prym_dependency"] is True
assert gate["verdict"]["provisional_terminal_candidate"] == "O210_COVER_GEOMETRY_EXCLUDED"
assert gate["q602_contradiction"]["graph_geometry_forced_trace"] == 0
assert gate["q602_contradiction"]["required_trace_mod8"] == 4
assert gate["q602_contradiction"]["zero_is_allowed"] is False
assert gate["population_domination"]["finite_monodromy_sample_used"] is False
assert gate["population_domination"]["does_not_claim_those_enumerations_were_run"] is True
assert gate["population_domination"]["all_fixed_O210_cover_configurations_disposed_if_source_chain_is_accepted"] is True

runpy.run_path(str(ROOT / locks["self_contained_trace_verifier"]["path"]), run_name="__stage32ex3_04h_replay__")

pop = a["population_exhaustiveness"]
assert pop["population_preserving_from_carrier_hypothesis"] is True
assert pop["finite_monodromy_search_used"] is False
assert pop["monodromy_or_nielsen_case_choice_enters_argument"] is False
assert pop["later_casework_dominated_not_claimed_executed"] is True
assert pop["dominated_roadmap_leaves"] == ["EX3-05","EX3-06","EX3-07","EX3-08"]

proposal = a["terminal_proposal"]
assert proposal["outcome"] == "O210_COVER_GEOMETRY_EXCLUDED"
assert proposal["mathematical_terminal_candidate_complete"] is True
assert proposal["genuine_positive_configuration_established"] is False

ready = a["checkpoint_readiness"]
assert ready["ready_for_retained_consolidation"] is True
assert ready["ready_for_claim_dag_sync_after_retention"] is True
assert ready["ready_for_hostile_audit_after_retention_and_claim_sync"] is True
assert ready["currently_retained"] is False
assert ready["currently_claim_synced"] is False
assert ready["currently_hostile_audited"] is False

assert a["credit_ceiling"]["level"] == "SCRATCH_PROVISIONAL_TERMINAL_CANDIDATE_ONLY"
for value in a["credit_ceiling"].values():
    if isinstance(value, bool):
        assert value is False
for k in ["hostile_audit_credit","stage32_main_credit","merge_authorized",
          "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
    assert a["firewalls"][k] is False

print(json.dumps({
    "success": True,
    "terminal_candidate": "O210_COVER_GEOMETRY_EXCLUDED",
    "population_preserving": True,
    "later_casework_dominated_not_claimed_executed": True,
    "ready_for_retained_consolidation": True,
    "currently_retained": False,
    "currently_hostile_audited": False,
    "stage32_main_credit": False
}, indent=2, sort_keys=True))
