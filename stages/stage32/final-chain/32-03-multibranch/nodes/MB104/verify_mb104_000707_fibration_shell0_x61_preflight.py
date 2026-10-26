#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[5]
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
STATE=HERE.parents[1]/"fib"/"STATE.json"
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
"x61_packet_runner_git_blob":HERE/"run_mb104_000707_fibration_shell0_x61_packet.py",
"x61_packet_verifier_git_blob":HERE/"verify_mb104_000707_fibration_shell0_x61_packet.py",
"x61_packet_aggregate_git_blob":HERE/"aggregate_mb104_000707_fibration_shell0_x61_packets.py",
"x61_packet_aggregate_verifier_git_blob":HERE/"verify_mb104_000707_fibration_shell0_x61_aggregate.py",
"x61_packet_preflight_git_blob":HERE/"verify_mb104_000707_fibration_shell0_x61_preflight.py",
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
    carry=load("gen17carry_preflight",HERE/"verify_mb104_000707_gen17_secondary_carry.py")
    packet=load("packet_preflight",HERE/"run_mb104_000707_fibration_shell0_x61_packet.py")
    m,p,c=carry.decode_bundle()
    assert len(c)==27 and len(m["incomplete_cells"])==29
    vals=sum(len(packet.child_values(*tuple(x))) for x in m["incomplete_cells"]); assert vals==146
    carry19=load("gen19carry_preflight",HERE/"verify_mb104_000707_gen19_x61_packet_carry.py")
    m19,p19,c19=carry19.decode_bundle()
    assert len(c19)==29 and int(m19["singleton_child_count"])==146
    assert int(m19["complete_child_count"])==123 and int(m19["incomplete_child_count"])==23
    assert all(r["reason"]=="timeout" and r["solver_result"]=="unknown" for r in m19["incomplete_children"])
    assert k["recovery"]["gen17_complete_secondary_count"]==27 and k["recovery"]["gen17_incomplete_secondary_count"]==29
    assert k["recovery"]["expected_new_packet_count"]==29 and k["recovery"]["expected_new_singleton_child_count"]==146
    assert k["concurrency"]["planned_effective_heavy_concurrency"]==4 and k["concurrency"]["stage_heavy_cap"]==18
    assert all(v is False for v in k["credit"].values()) and all(v is False for v in s["credit_firewall"].values())
    if not k["armed"]:
        assert int(k["generation"])>=18 and k["mode"]=="COLD"
        assert s["execution"]["heavy_armed"] is False and s["execution"]["execution_authorized"] is False and int(s["execution"]["runkey_generation"])==int(k["generation"])
        assert k["execution_gate"]["automatic_execution_authorized"] is False and k["execution_gate"]["current_head_execution_blocked"] is True
    else:
        assert int(k["generation"])>=19 and k["mode"]=="RECOVERY"
        assert k["execution_gate"]["hostile_audit_status"]=="PASS" and k["execution_gate"]["audited_surface"]["status"]=="PASS"
        assert s["execution"]["heavy_armed"] is True and s["execution"]["execution_authorized"] is True
    print(json.dumps({"success":True,"generation":k["generation"],"mode":k["mode"],"gen17_carried_complete":len(c),"refined_parent_packets":29,"singleton_children":146,"max_parallel":4,"heavy_authorized":bool(k["armed"]),"credit":False},sort_keys=True))
if __name__=="__main__": main()
