#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/"BR204-GENERATION4-RECOVERY-PLAN.json").read_text())
d=json.loads((ROOT/"BR204-GENERATION4-RECOVERY-DESIGN.json").read_text())
assert p["schema"]=="STAGE32_BR204_GENERATION4_RECOVERY_PLAN_V1"
assert p["status"]=="COLD_PLAN_ONLY__NO_HEAVY_AUTHORIZATION__ZERO_CREDIT"
assert p["design_blob"]=="13037b1271f66161dd7ef590d1ac4ffd85319878"
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
assert r["flat_bc16_child_count"]==576
assert r["hierarchical_bc64_child_count"]==2108
assert r["representative_child_certificate_hard_cap_bytes"]==65536
assert r["projected_peak_storage_bytes"]==175898624
assert r["projected_peak_storage_bytes"] < r["repository_storage_budget_bytes"]
assert r["storage_gate_passed"] is True
assert r["representative_payload_measurement_required"] is True
assert r["measured_representative_payload_bytes"]==448
assert r["measured_projection_bytes"]==1202432
assert r["measurement_status"]=="RETAINED_SOURCE_LOCKED"
assert len(r["measurement_receipt_blob"])==40
assert len(r["measurement_payload_blob"])==40
assert r["raw_child_state_upload_forbidden"] is True
a=p["authorization"]
assert a["runkey_generation"]==0 and a["runkey_armed"] is False and a["heavy_compute_authorized"] is False
assert all(v is False for v in p["credit"].values())
assert d["status"]=="COLD_DESIGN_ONLY__NO_HEAVY_AUTHORIZATION__ZERO_CREDIT"
print("BR204 G4 cold recovery plan: PASS")
