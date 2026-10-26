#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,os,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[5]
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
STATE=HERE.parents[1]/"fib"/"STATE.json"
PARENT=HERE/"run_mb104_000707_fibration_shell_local_exact.py"
RECOVERY=HERE/"run_mb104_000707_fibration_shell0_recovery_singleton.py"
RECOVERY_VERIFIER=HERE/"verify_mb104_000707_fibration_shell0_recovery_singleton.py"
RECOVERY_AGGREGATE=HERE/"aggregate_mb104_000707_fibration_shell0_recovery.py"
CARRY_VERIFIER=HERE/"verify_mb104_000707_gen13_shard0_carry.py"
CARRY_MANIFEST=HERE/"MB104-000707-GEN13-SHARD0-CARRY-MANIFEST.json"
REHYDRATE=HERE/"rehydrate_mb104_000707_gen15_carry.py"
RETAINED=HERE/"run_mb104_000707_fibration_isotropic_shells.py"
STOLL_HELPER=REPO/"stages/stage33/33-07/stoll_cuboid_source.py"
PICARD_MARKING=REPO/"stages/stage33/33-07/stage32_picard_marking_retained.py"
PICARD_BASE=REPO/"stages/stage33/33-07/picard_base_rows_retained.py"
HPERP_ADAPTER=REPO/"stages/stage32/residual-32-01-production/hperp_integral_adapter.py"
PAIRING_PREFIX=REPO/"stages/stage32/residual-32-01-production/pairing_prefix_engine.py"
WORKFLOW=REPO/".github/workflows/stage32-mb-fib-isotropic-shell-pilot.yml"
def blob(path): return subprocess.check_output(["git","hash-object",str(path)],cwd=REPO,text=True).strip()
def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path); assert spec and spec.loader
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
def main():
    k=json.loads(RUNKEY.read_text()); s=json.loads(STATE.read_text()); m=json.loads(CARRY_MANIFEST.read_text()); sl=k["source_locks"]
    paths={"local_exact_engine_git_blob":PARENT,"recovery_runner_git_blob":RECOVERY,"recovery_verifier_git_blob":RECOVERY_VERIFIER,"recovery_aggregate_git_blob":RECOVERY_AGGREGATE,"carry_verifier_git_blob":CARRY_VERIFIER,"carry_manifest_git_blob":CARRY_MANIFEST,"rehydrate_gen15_carry_git_blob":REHYDRATE,"runner_git_blob":RETAINED,"stage33_stoll_helper_blob":STOLL_HELPER,"stage33_picard_marking_blob":PICARD_MARKING,"stage33_picard_base_rows_blob":PICARD_BASE,"hperp_integral_adapter_blob":HPERP_ADAPTER,"pairing_prefix_engine_blob":PAIRING_PREFIX,"workflow_git_blob":WORKFLOW}
    for field,path in paths.items(): assert blob(path)==sl[field],(field,blob(path),sl[field])
    assert blob(Path(__file__))==sl["recovery_preflight_git_blob"]
    recovery=load_module("mbfib_recovery_v2",RECOVERY); carry=load_module("mbfib_carry_v2",CARRY_VERIFIER)
    carry_dir=Path(os.environ["GEN15_CARRY_DIR"]); carried=carry.validate_gen15_artifact_dir(m,carry_dir); sec=recovery.secondary_contract()
    assert sorted(carried)==recovery.GEN15_COMPLETE_VALUES
    assert recovery.PRIMARY_VALUES==[-14,-12,-8,0,4,8,12] and sec["secondary_shard_count"]==8 and len(sec["secondary_intervals"])==8
    assert k["recovery"]["residual_primary_values"]==recovery.PRIMARY_VALUES and k["recovery"]["gen15_complete_values"]==recovery.GEN15_COMPLETE_VALUES
    assert int(k["recovery"]["secondary_shard_count"])==8 and int(k["recovery"]["expected_new_workunit_count"])==56
    assert k["concurrency"]["planned_effective_heavy_concurrency"]==4
    assert all(v is False for v in k["credit"].values()) and all(v is False for v in s["credit_firewall"].values())
    if not k["armed"]:
        assert int(k["generation"])==16 and k["mode"]=="COLD"
        assert s["execution"]["heavy_armed"] is False and int(s["execution"]["runkey_generation"])==16 and s["execution"]["execution_authorized"] is False
        assert k["execution_gate"]["automatic_execution_authorized"] is False and k["execution_gate"]["current_head_execution_blocked"] is True
    else:
        assert int(k["generation"])>=17 and k["mode"]=="RECOVERY"
        assert s["execution"]["heavy_armed"] is True and s["execution"]["execution_authorized"] is True
        assert k["execution_gate"]["hostile_audit_status"]=="PASS" and k["execution_gate"]["audited_surface"]["status"]=="PASS"
        assert k["execution_gate"]["scaleout_authorized"] is False and k["execution_gate"]["shells_1_2_3_authorized"] is False
    print(json.dumps({"success":True,"generation":k["generation"],"mode":k["mode"],"gen15_carried_complete":len(carried),"residual_primary_values":recovery.PRIMARY_VALUES,"secondary_coordinate_0based":sec["secondary_coordinate_0based"],"secondary_coordinate_bound":sec["secondary_coordinate_bound"],"secondary_intervals":sec["secondary_intervals"],"new_workunits":56,"max_parallel":4,"heavy_authorized":bool(k["armed"]),"credit":False},sort_keys=True))
if __name__=="__main__": main()
