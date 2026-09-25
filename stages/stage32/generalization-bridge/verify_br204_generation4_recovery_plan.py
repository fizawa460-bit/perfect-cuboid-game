#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/"BR204-GENERATION4-RECOVERY-PLAN.json").read_text())
d=json.loads((ROOT/"BR204-GENERATION4-RECOVERY-DESIGN.json").read_text())
assert p["schema"]=="STAGE32_BR204_GENERATION4_RECOVERY_PLAN_V2_COMPACT_CERT"
assert p["status"]=="COLD_EXECUTION_PLAN__LOSSLESS_COMPACT_CERT__AUDIT_REQUIRED__ZERO_CREDIT"
assert p["design_blob"]=="a92ae6677310b8ed104e6356ca2442936a1245f5"
assert p["unchanged_target_count"]==69
assert p["flat_target_count"]==36 and len(p["flat_targets"])==36
assert p["hierarchical_target_count"]==33 and len(p["hierarchical_targets"])==33
keys={(x["b"],x["d"]) for x in p["flat_targets"]}|{(x["b"],x["d"]) for x in p["hierarchical_targets"]}
assert len(keys)==69
c=p["restored_predecessor_carry"]
assert (c["b"],c["d"],c["parent_bc16_index"])==(2,148,0)
assert c["exact_child64_indices"]==[0,16,32,48] and c["recompute"] is False
h=[x for x in p["hierarchical_targets"] if x["b"]==2 and x["d"]==148]
assert len(h)==1 and h[0]["parent_bc16_indices"]==list(range(1,16))
for x in p["hierarchical_targets"]:
    if (x["b"],x["d"])!=(2,148): assert x["parent_bc16_indices"]==list(range(16))
r=p["resource_preflight"]
assert r["repository_storage_budget_bytes"]==524288000
assert r["planned_effective_heavy_concurrency"]==12<=r["repository_stage_concurrency_ceiling"]==18
assert r["evidence_unit_count"]==2684
assert r["flat_bc16_child_count"]==576 and r["hierarchical_bc64_child_count"]==2108
assert r["representative_child_certificate_hard_cap_bytes"]==65536
assert r["actual_predecessor_sample_certificate_bytes"]==[7737,7386,7235,7128]
assert r["measured_representative_payload_bytes"]==7737
assert r["measured_projection_bytes"]==20766108
assert r["conservative_two_generation_hard_cap_projection_bytes"]==351797248
assert r["conservative_two_generation_hard_cap_projection_bytes"] < r["repository_storage_budget_bytes"]
assert r["intermediate_retention_days"]==14
assert r["actual_roundtrip_byte_exact"] is True
assert r["raw_child_state_upload_forbidden"] is True
a=p["authorization"]
assert a["runkey_generation"]==1 and a["runkey_armed"] is True
assert a["generation1_arm_is_inert"] is True and a["heavy_compute_authorized"] is False
assert a["next_heavy_generation"]==2 and a["next_arm_must_be_runkey_only"] is True
assert all(v is False for v in p["credit"].values())
assert d["schema"]=="STAGE32_BR204_GENERATION4_RECOVERY_DESIGN_V3_COMPACT_EXECUTION"
assert d["status"]=="COLD_EXECUTION_SURFACE__LOSSLESS_COMPACT_CERT__AUDIT_REQUIRED__ZERO_CREDIT"
assert d["predecessor_certificate"]["blob"]=="5a4a990a1588c71facbb9640a4c26b8641e44b02"
assert d["resource_preflight"]["maximum_actual_sample_certificate_bytes"]==7737
assert d["resource_preflight"]["intermediate_retention_days"]==14
assert d["gates"]["current_generation1_arm_is_inert"] is True
assert d["gates"]["heavy_compute_authorized"] is False
print("BR204 G4 compact execution plan: PASS")
