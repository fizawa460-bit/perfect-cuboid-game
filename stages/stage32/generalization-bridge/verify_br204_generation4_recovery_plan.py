#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLAN = ROOT / "BR204-GENERATION4-RECOVERY-PLAN.json"
DESIGN = ROOT / "BR204-GENERATION4-RECOVERY-DESIGN.json"
RUNKEY = ROOT / "runkeys/br204-recovery-g4.json"
STATE = ROOT / "STATE.json"
PREDECESSOR = ROOT / "BR204-G4-PREDECESSOR-CERTIFICATE.json"

PLAN_REL = "stages/stage32/generalization-bridge/BR204-GENERATION4-RECOVERY-PLAN.json"
DESIGN_REL = "stages/stage32/generalization-bridge/BR204-GENERATION4-RECOVERY-DESIGN.json"
RUNKEY_REL = "stages/stage32/generalization-bridge/runkeys/br204-recovery-g4.json"
STATE_REL = "stages/stage32/generalization-bridge/STATE.json"
PREDECESSOR_REL = "stages/stage32/generalization-bridge/BR204-G4-PREDECESSOR-CERTIFICATE.json"
VERIFIER_REL = "stages/stage32/generalization-bridge/verify_br204_generation4_recovery_plan.py"

def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()

def git_blob_at(ref: str, rel: str) -> str:
    return subprocess.check_output(["git", "rev-parse", f"{ref}:{rel}"], text=True).strip()

def git_json_at(ref: str, rel: str):
    raw = subprocess.check_output(["git", "show", f"{ref}:{rel}"], text=True)
    return json.loads(raw)

def validate_static(p, d, s):
    assert p["schema"]=="STAGE32_BR204_GENERATION4_RECOVERY_PLAN_V2_COMPACT_CERT"
    assert p["status"]=="COLD_EXECUTION_PLAN__LOSSLESS_COMPACT_CERT__AUDIT_REQUIRED__ZERO_CREDIT"
    assert p["design_blob"]==blob(DESIGN)
    assert p["unchanged_target_count"]==69
    assert p["flat_target_count"]==36 and len(p["flat_targets"])==36
    assert p["hierarchical_target_count"]==33 and len(p["hierarchical_targets"])==33
    keys={(x["b"],x["d"]) for x in p["flat_targets"]}|{(x["b"],x["d"]) for x in p["hierarchical_targets"]}
    assert len(keys)==69
    c=p["restored_predecessor_carry"]
    assert (c["b"],c["d"],c["parent_bc16_index"])==(2,148,0)
    assert c["exact_child64_indices"]==[0,16,32,48]
    assert c["parent_payload_sha256"]=="d3a84475e3d7c68614fa101f166b0c342c32ea9c73453e5ea331fa608a284973"
    assert c["recompute"] is False
    h=[x for x in p["hierarchical_targets"] if (x["b"],x["d"])==(2,148)]
    assert len(h)==1 and h[0]["parent_bc16_indices"]==list(range(1,16))
    for x in p["hierarchical_targets"]:
        if (x["b"],x["d"])!=(2,148):
            assert x["parent_bc16_indices"]==list(range(16))
    persist=p["persistence"]
    assert persist["compact_certificate_schema"]=="STAGE32_BR204_G4_COMPACT_CHILD_CERT_V2"
    assert persist["compact_codec"]=="delta-varint-zlib-base64-v1"
    assert persist["raw_target_level_retention_replay_forbidden"] is True
    rp=p["resource_preflight"]
    assert rp["repository_storage_budget_bytes"]==524288000
    assert rp["planned_effective_heavy_concurrency"]==12
    assert rp["repository_stage_concurrency_ceiling"]==18
    assert rp["evidence_unit_count"]==2688
    assert rp["flat_bc16_child_count"]==576
    assert rp["hierarchical_bc64_child_count"]==2108
    assert rp["newly_computed_child_certificate_count"]==2684
    assert rp["restored_predecessor_child_certificate_count"]==4
    assert rp["retained_certificate_count"]==2688
    assert rp["representative_child_certificate_hard_cap_bytes"]==65536
    assert rp["actual_predecessor_sample_certificate_bytes"]==[7737,7386,7235,7128]
    assert rp["measured_representative_payload_bytes"]==7737
    assert rp["measured_projection_bytes"]==20797056
    assert rp["conservative_single_generation_hard_cap_projection_bytes"]==176160768
    assert rp["conservative_two_generation_hard_cap_projection_bytes"]==352321536
    assert rp["conservative_two_generation_hard_cap_projection_bytes"] < rp["repository_storage_budget_bytes"]
    assert rp["intermediate_retention_days"]==14
    assert rp["actual_roundtrip_byte_exact"] is True
    assert rp["storage_gate_passed"] is True
    assert rp["raw_child_state_upload_forbidden"] is True
    a=p["authorization"]
    assert a["workflow_implemented"] is True
    assert a["runkey_generation"]==1 and a["runkey_armed"] is True
    assert a["generation1_arm_is_inert"] is True
    assert a["heavy_compute_authorized"] is False
    assert a["hostile_audit_required_before_arm"] is True
    assert a["next_heavy_generation"]==2
    assert a["next_arm_must_be_runkey_only"] is True
    assert all(v is False for v in p["credit"].values())

    assert d["schema"]=="STAGE32_BR204_GENERATION4_RECOVERY_DESIGN_V3_COMPACT_EXECUTION"
    assert d["status"]=="COLD_EXECUTION_SURFACE__LOSSLESS_COMPACT_CERT__AUDIT_REQUIRED__ZERO_CREDIT"
    assert d["predecessor_certificate"]["blob"]==blob(PREDECESSOR)
    assert d["resource_preflight"]["actual_roundtrip_byte_exact"] is True
    assert d["resource_preflight"]["intermediate_retention_days"]==14
    assert d["gates"]["current_runkey_generation"]==1
    assert d["gates"]["current_runkey_armed"] is True
    assert d["gates"]["current_generation1_arm_is_inert"] is True
    assert d["gates"]["heavy_compute_authorized"] is False
    assert all(v is False for v in d["credit"].values())

    assert s["schema"]=="STAGE32_GENERALIZATION_BRIDGE_STATE_V23_G4_GENERATION3_RUNTIME_REPAIR_COLD"
    assert s["source_locks"]["g4_design_blob"]==blob(DESIGN)
    assert s["source_locks"]["g4_plan_blob"]==blob(PLAN)
    assert s["source_locks"]["g4_plan_verifier_blob"]==blob(Path(__file__))
    assert s["source_locks"]["br203_mu_verifier_blob"]=="56c932c90ce2adaf702956e0b600b0a958fd29fe"
    assert s["source_locks"]["br203_mu_emitter_blob"]=="26f1a0cb87140a5050b01fc1cd076f947091ac27"
    assert s["routing"]["heavy_compute_armed"] is False
    assert s["routing"]["BR204_FULL178_scaleout_authorized"] is False
    assert s["generation4_recovery_design"]["generation1_arm_is_inert"] is True
    assert s["generation4_recovery_design"]["heavy_compute_authorized"] is False
    assert s["generation4_recovery_design"]["next_heavy_generation"]==3
    assert s["generation4_recovery_design"]["generation2_transition_adapter"]["status"]=="AUDITED_PASS_ARMED_CHILD__RUNTIME_FAILED_PRETARGET"
    assert s["generation4_recovery_design"]["generation2_execution"]["completed_target_count"]==0
    assert s["generation4_recovery_design"]["generation3_transition_adapter"]["status"]=="COLD_RUNTIME_BUILD_REPAIRED_AWAIT_HOSTILE_AUDIT"
    assert s["generation4_recovery_design"]["generation3_transition_adapter"]["runkey_only_child"] is True
    assert s["next_obligation"]["id"]=="BR204_G4_GENERATION3_RUNTIME_REPAIR_AUDIT"
    assert all(v is False for v in s["credit_firewall"].values())

def validate_cold_runkey(r, expected_blob: str, s):
    assert r["schema"]=="STAGE32_BR204_RECOVERY_G4_RUNKEY_V2_COMPACT_CERT"
    assert r["generation"]==2 and r["armed"] is True
    locks=r["source_locks"]
    assert locks["design_blob"]==blob(DESIGN)
    assert locks["plan_blob"]==blob(PLAN)
    assert locks["plan_verifier_blob"]==blob(Path(__file__))
    assert locks["predecessor_certificate_blob"]==blob(PREDECESSOR)
    assert locks["repository_main_head"]=="a834864923086e5f7c1647e462804f45ff9ac28d"
    assert locks["repository_main_state_blob"]=="070847c669120aef1ab3777239d45878937b41f3"
    assert locks["bc_shard_worker_blob"]=="ca0a4985e788455432eb59d603da54fc3c703ea6"
    assert locks["bc_shard_combiner_blob"]=="33089c2ca4876650a4ee9c6477e1e6242ad3741c"
    assert locks["bc64_group_combiner_blob"]=="5986168bca8ec63e1d1aab2e417e9157ae09ef23"
    assert locks["br203_mu_verifier_blob"]=="56c932c90ce2adaf702956e0b600b0a958fd29fe"
    assert locks["br203_mu_emitter_blob"]=="26f1a0cb87140a5050b01fc1cd076f947091ac27"
    assert r["storage"]["intermediate_retention_days"]==14
    assert r["storage"]["conservative_two_generation_hard_cap_projection_bytes"]==352321536
    ac=r["arm_contract"]
    assert ac["hostile_audit_status"]=="PASS"
    assert ac["generation1_heavy_execution_started"] is False
    assert ac["generation2_authorization_succeeded"] is True
    assert ac["generation2_runtime_failed_before_target"] is True
    assert ac["generation2_completed_target_count"]==0
    assert ac["generation2_execution_closed"] is True
    assert ac["fresh_hostile_audit_and_generation3_rearm_required"] is True
    assert ac["generation3_transition_adapter_status"]=="COLD_RUNTIME_BUILD_REPAIRED_AWAIT_HOSTILE_AUDIT"
    assert ac["generation3_heavy_authorized"] is False
    assert all(v is False for v in r["credit"].values())
    assert s["source_locks"]["g4_runkey_blob"]==expected_blob

def validate_parent_immutable(parent_ref: str):
    pairs=[
        (PLAN_REL, PLAN),
        (DESIGN_REL, DESIGN),
        (STATE_REL, STATE),
        (PREDECESSOR_REL, PREDECESSOR),
        (VERIFIER_REL, Path(__file__)),
    ]
    for rel,path in pairs:
        assert git_blob_at(parent_ref,rel)==blob(path), (rel,parent_ref)

def validate_armed_child(new, old, parent_ref: str):
    assert old["schema"]==new["schema"]=="STAGE32_BR204_RECOVERY_G4_RUNKEY_V2_COMPACT_CERT"
    assert old["generation"]==2 and old["armed"] is True
    assert new["generation"]==3 and new["armed"] is True
    for k in ("execution","source_locks","storage","resume","credit"):
        assert old[k]==new[k], k
    assert all(v is False for v in new["credit"].values())
    ac=new["arm_contract"]
    assert ac["audited_doorstep_head"]==parent_ref
    assert isinstance(ac["audited_doorstep_review_id"],int) and ac["audited_doorstep_review_id"]>0
    assert ac["hostile_audit_status"]=="PASS"
    assert ac["execution_surface_audit_status"]=="PASS"
    assert ac["generation3_transition_adapter_status"]=="AUDITED_PASS_ARMED_CHILD"
    assert ac["generation3_heavy_authorized"] is True
    assert ac["fresh_hostile_audit_and_generation3_rearm_required"] is False
    assert ac["runkey_only_arm_commit_required"] is True
    assert ac["planned_effective_heavy_concurrency"]==12
    assert ac["repository_stage_concurrency_ceiling"]==18
    assert 0 <= ac["observed_other_stage32_heavy_concurrency_at_arm"] <= 6
    assert ac["combined_effective_heavy_concurrency_at_arm"] == 12 + ac["observed_other_stage32_heavy_concurrency_at_arm"]
    assert ac["combined_effective_heavy_concurrency_at_arm"] <= 18

ap=argparse.ArgumentParser()
ap.add_argument("--mode", choices=("cold-surface","armed-child"), default="cold-surface")
ap.add_argument("--parent-ref")
ap.add_argument("--candidate-runkey")
args=ap.parse_args()

p=json.loads(PLAN.read_text())
d=json.loads(DESIGN.read_text())
s=json.loads(STATE.read_text())
validate_static(p,d,s)

if args.mode=="cold-surface":
    assert args.parent_ref is None
    assert args.candidate_runkey is None
    r=json.loads(RUNKEY.read_text())
    current_blob=blob(RUNKEY)
    validate_cold_runkey(r,current_blob,s)
else:
    assert args.parent_ref
    parent=args.parent_ref
    validate_parent_immutable(parent)
    parent_blob=git_blob_at(parent,RUNKEY_REL)
    old=git_json_at(parent,RUNKEY_REL)
    validate_cold_runkey(old,parent_blob,s)
    candidate=Path(args.candidate_runkey) if args.candidate_runkey else RUNKEY
    new=json.loads(candidate.read_text())
    validate_armed_child(new,old,parent)

print(f"BR204 G4 generation-3 runtime-repair arm adapter {args.mode}: PASS")
