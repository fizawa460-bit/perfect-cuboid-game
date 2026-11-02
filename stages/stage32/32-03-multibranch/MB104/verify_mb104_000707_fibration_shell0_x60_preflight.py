#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent; REPO=HERE.parents[5]; RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"; STATE=HERE.parents[1]/"fib"/"STATE.json"
PATHS={
"local_exact_engine_git_blob":HERE/"run_mb104_000707_fibration_shell_local_exact.py",
"carry_manifest_git_blob":HERE/"MB104-000707-GEN13-SHARD0-CARRY-MANIFEST.json",
"carry_verifier_git_blob":HERE/"verify_mb104_000707_gen13_shard0_carry.py",
"gen15_carry_bundle_git_blob":HERE/"MB104-000707-GEN15-SINGLETON-CARRY-BUNDLE.json",
"rehydrate_gen15_carry_git_blob":HERE/"rehydrate_mb104_000707_gen15_carry.py",
"recovery_runner_git_blob":HERE/"run_mb104_000707_fibration_shell0_recovery_singleton.py",
"gen17_carry_manifest_git_blob":HERE/"MB104-000707-GEN17-SECONDARY-CARRY-MANIFEST.json",
"gen17_carry_bundle_git_blob":HERE/"MB104-000707-GEN17-SECONDARY-CARRY-BUNDLE.json",
"gen17_carry_verifier_git_blob":HERE/"verify_mb104_000707_gen17_secondary_carry.py",
"rehydrate_gen17_carry_git_blob":HERE/"rehydrate_mb104_000707_gen17_secondary_carry.py",
"gen19_carry_manifest_git_blob":HERE/"MB104-000707-GEN19-X61-PACKET-CARRY-MANIFEST.json",
"gen19_carry_bundle_git_blob":HERE/"MB104-000707-GEN19-X61-PACKET-CARRY-BUNDLE.json",
"gen19_carry_verifier_git_blob":HERE/"verify_mb104_000707_gen19_x61_packet_carry.py",
"rehydrate_gen19_carry_git_blob":HERE/"rehydrate_mb104_000707_gen19_x61_packet_carry.py",
"x60_packet_runner_git_blob":HERE/"run_mb104_000707_fibration_shell0_x60_packet.py",
"x60_packet_verifier_git_blob":HERE/"verify_mb104_000707_fibration_shell0_x60_packet.py",
"x60_packet_aggregate_git_blob":HERE/"aggregate_mb104_000707_fibration_shell0_x60_packets.py",
"x60_packet_aggregate_verifier_git_blob":HERE/"verify_mb104_000707_fibration_shell0_x60_aggregate.py",
"x60_packet_preflight_git_blob":HERE/"verify_mb104_000707_fibration_shell0_x60_preflight.py",
"workflow_git_blob":REPO/".github/workflows/stage32-mb-fib-isotropic-shell-pilot.yml",
"runner_git_blob":HERE/"run_mb104_000707_fibration_isotropic_shells.py",
"stage33_stoll_helper_blob":REPO/"stages/stage33/33-07/stoll_cuboid_source.py",
"stage33_picard_marking_blob":REPO/"stages/stage33/33-07/stage32_picard_marking_retained.py",
"stage33_picard_base_rows_blob":REPO/"stages/stage33/33-07/picard_base_rows_retained.py",
"hperp_integral_adapter_blob":REPO/"stages/stage32/residual-32-01-production/hperp_integral_adapter.py",
"pairing_prefix_engine_blob":REPO/"stages/stage32/residual-32-01-production/pairing_prefix_engine.py",
}
def blob(p): return subprocess.check_output(["git","hash-object",str(p)],cwd=REPO,text=True).strip()
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path); assert spec and spec.loader
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
def main():
    k=json.loads(RUNKEY.read_text()); s=json.loads(STATE.read_text()); sl=k["source_locks"]
    for field,path in PATHS.items(): assert blob(path)==sl[field],(field,blob(path),sl[field])
    carry19=load("gen19carry_x60_preflight",HERE/"verify_mb104_000707_gen19_x61_packet_carry.py"); runner=load("x60runner_preflight",HERE/"run_mb104_000707_fibration_shell0_x60_packet.py")
    m19,p19,c19=carry19.decode_bundle(); assert len(c19)==29 and int(m19["complete_child_count"])==123 and int(m19["incomplete_child_count"])==23
    assert len(runner.residual_leaves())==23 and runner.x60_contract()["bound"]==[-20,20] and len(runner.x60_contract()["intervals"])==8
    assert int(k["recovery_x60"]["expected_packet_count"])==23 and int(k["recovery_x60"]["expected_interval_child_count"])==184 and int(k["recovery_x60"]["refinement_coordinate_0based"])==60 and k["recovery_x60"]["refinement_bound"]==[-20,20]
    assert k["concurrency"]["planned_effective_heavy_concurrency"]==4 and k["concurrency"]["stage_heavy_cap"]==18
    assert all(v is False for v in k["credit"].values()) and all(v is False for v in s["credit_firewall"].values())
    if not k["armed"]:
        assert int(k["generation"])>=20 and k["mode"]=="COLD" and s["execution"]["heavy_armed"] is False and s["execution"]["execution_authorized"] is False and int(s["execution"]["runkey_generation"])==int(k["generation"]) and k["execution_gate"]["automatic_execution_authorized"] is False and k["execution_gate"]["current_head_execution_blocked"] is True
    else:
        assert int(k["generation"])>=21 and k["mode"]=="RECOVERY" and k["execution_gate"]["hostile_audit_status"]=="PASS" and k["execution_gate"]["audited_surface"]["status"]=="PASS" and s["execution"]["heavy_armed"] is True and s["execution"]["execution_authorized"] is True
    print(json.dumps({"success":True,"generation":k["generation"],"mode":k["mode"],"gen19_carried_complete_x61":123,"residual_timeout_leaves":23,"x60_packets":23,"x60_interval_children":184,"x60_bound":[-20,20],"max_parallel":4,"heavy_authorized":bool(k["armed"]),"credit":False},sort_keys=True))
if __name__=="__main__": main()
