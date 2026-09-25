#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
STATE=HERE.parents[1]/"fib"/"STATE.json"
COLD=HERE/"MB104-000707-GEN25-ADAPTIVE-AFFINE-COLD.json"
COLD_VERIFIER=HERE/"verify_mb104_000707_gen25_adaptive_affine_cold.py"

PATHS={
    "workflow_git_blob":HERE.parents[5]/".github/workflows/stage32-mb-fib-isotropic-shell-pilot.yml",
    "local_exact_engine_git_blob":HERE/"run_mb104_000707_fibration_shell_local_exact.py",
    "x60_packet_runner_git_blob":HERE/"run_mb104_000707_fibration_shell0_x60_packet.py",
    "gen19_carry_manifest_git_blob":HERE/"MB104-000707-GEN19-X61-PACKET-CARRY-MANIFEST.json",
    "recovery_runner_git_blob":HERE/"run_mb104_000707_fibration_shell0_recovery_singleton.py",
    "gen23_carry_source_git_blob":HERE/"MB104-000707-GEN23-X60-SINGLETON-CARRY-SOURCE.json",
    "gen23_carry_index_git_blob":HERE/"MB104-000707-GEN23-X60-SINGLETON-CARRY-INDEX.json",
    "gen23_carry_verifier_git_blob":HERE/"verify_mb104_000707_gen23_x60_singleton_carry.py",
    "gen24_residual_git_blob":HERE/"MB104-000707-GEN24-X60-SINGLETON-RESIDUAL30.json",
    "gen25_successor_design_spec_git_blob":HERE/"MB104-000707-GEN25-SUCCESSOR-REDESIGN-COLD-SPEC.json",
    "gen25_successor_cold_diagnostic_git_blob":HERE/"derive_mb104_000707_gen25_adaptive_affine_cold.py",
    "gen25_successor_cold_verifier_git_blob":COLD_VERIFIER,
    "gen25_adaptive_cold_output_git_blob":COLD,
    "adaptive_x58_preflight_git_blob":Path(__file__).resolve(),
    "adaptive_x58_packet_runner_git_blob":HERE/"run_mb104_000707_fibration_shell0_adaptive_x58_packet.py",
    "adaptive_x58_packet_verifier_git_blob":HERE/"verify_mb104_000707_fibration_shell0_adaptive_x58_packet.py",
    "adaptive_x58_aggregate_git_blob":HERE/"aggregate_mb104_000707_fibration_shell0_adaptive_x58_packets.py",
    "adaptive_x58_aggregate_verifier_git_blob":HERE/"verify_mb104_000707_fibration_shell0_adaptive_x58_aggregate.py",
    "runner_git_blob":HERE/"run_mb104_000707_fibration_isotropic_shells.py",
    "stage33_stoll_helper_blob":HERE.parents[4]/"stage33/33-07/stoll_cuboid_source.py",
    "stage33_picard_marking_blob":HERE.parents[4]/"stage33/33-07/stage32_picard_marking_retained.py",
    "stage33_picard_base_rows_blob":HERE.parents[4]/"stage33/33-07/picard_base_rows_retained.py",
    "hperp_integral_adapter_blob":HERE.parents[3]/"residual-32-01-production/hperp_integral_adapter.py",
    "pairing_prefix_engine_blob":HERE.parents[3]/"residual-32-01-production/pairing_prefix_engine.py",
}

def git_blob(path):
    return subprocess.check_output(["git","hash-object",str(path)],text=True).strip()

def canonical_without_field(d):
    b=dict(d); saved=b.pop("canonical_sha256_without_this_field")
    got=hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert got==saved,(got,saved)
    return saved

def main():
    k=json.loads(RUNKEY.read_text()); s=json.loads(STATE.read_text()); sl=k["source_locks"]
    assert int(k["generation"])>=26 and k["mode"] in {"COLD","RECOVERY"}
    if k["mode"]=="COLD":
        assert k["armed"] is False and k["execution_gate"]["automatic_execution_authorized"] is False
        assert s["execution"]["heavy_armed"] is False and s["execution"]["execution_authorized"] is False
    c=k["concurrency"]
    assert int(c["planned_effective_heavy_concurrency"])==8
    assert int(c["reserved_stage_headroom"])==10
    assert int(c["stage_heavy_cap"])==18
    assert int(c["max_other_live_stage32_concurrency_for_arm"])==10
    assert c["prearm_live_concurrency_recheck_required"] is True
    assert c["live_gate_fail_closed"] is True
    assert c["live_gate_counting_method"]=="ALL_QUEUED_OR_IN_PROGRESS_JOBS_IN_OTHER_STAGE32_WORKFLOW_RUNS__CURRENT_RUN_EXCLUDED__CONSERVATIVE_UPPER_BOUND"
    cm=c["current_main_coordination"]
    assert cm["repository_main"]=="e7fd29d24dd21e8529dbdb45b221a53f2cc21ed3"
    assert cm["main_heavy_workflow_path"]==".github/workflows/stage32-main-grf04-hpadj22-full178.yml"
    assert cm["main_heavy_workflow_git_blob"]=="eedc196d369a7e489f9fdfd75f9e3910cba15b8c"
    assert cm["main_heavy_runkey_path"]=="stages/stage32/management/grf04-hpadj22-joint/runkeys/V46-GRF04-HPADJ22-FULL178.json"
    assert cm["main_heavy_runkey_git_blob"]=="f011a66e48789b40bf3b54c4118cfdd0faa0f585"
    assert int(cm["main_heavy_generation"])==17
    assert cm["main_heavy_armed"] is True
    assert int(cm["main_planned_effective_heavy_concurrency"])==14
    assert s["execution"]["planned_effective_heavy_concurrency"]==8
    pred=k["execution_gate"]["predecessor_audited_surface"]
    assert pred["status"]=="PASS"
    assert pred["exact_head"]=="17473b02de084c086fe3abeaf0b7fc8107e4a997"
    assert int(pred["review_id"])==5285955013
    for field,path in PATHS.items():
        got=git_blob(path)
        assert got==sl[field],(field,got,sl[field])
    d=json.loads(COLD.read_text())
    assert canonical_without_field(d)=="6daaaef5e82aaefab0b676c24392b08894e7ecf63b6a930f0327d74ffd48a1d7"
    assert d["schema"]=="STAGE32_MB104_000707_GEN25_ADAPTIVE_AFFINE_COLD_V1"
    assert d["status"]=="COLD_ADAPTIVE_AFFINE_SUCCESSOR_DESIGNED_NO_HEAVY_EXECUTION_NO_CREDIT"
    assert d["heavy_armed"] is False and d["execution_authorized"] is False and d["heavy_surface_present"] is False
    assert all(v is False for v in d["credit_firewall"].values())
    split=[r for r in d["leaves"] if r["status"]=="ADAPTIVE_AFFINE_CONDITIONED_SPLIT"]
    empty=[r for r in d["leaves"] if r["status"]=="REAL_EMPTY_NORM_PLUS_P_NECESSARY_CONDITION"]
    assert len(split)==16 and len(empty)==14
    assert all(int(r["selected_coordinate"]["coordinate_0based"])==58 and len(r["intervals"])==8 for r in split)
    assert sum(len(r["intervals"]) for r in split)==128
    assert all(int(r["conditioned_residual_energy"][0])<0 for r in empty)
    print(json.dumps({"success":True,"generation":int(k["generation"]),"mode":k["mode"],
                      "carried_complete":281,"residual":30,"necessary_empty":14,
                      "adaptive_packets":16,"adaptive_children":128,"coordinate_0based":58,
                      "planned_effective_heavy_concurrency":8,"max_other_live_stage32_concurrency_for_arm":10,
                      "heavy_armed":bool(k["armed"])},sort_keys=True))

if __name__=="__main__":
    main()
