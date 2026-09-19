#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
CP=HERE/"BR204-GENERATION2-RECOVERY-CHECKPOINT.json"
TARGETS=HERE/"BR204-GENERATION1-FINER-TARGETS.json"

LOCKS={
    "targets_blob":"7b1ade20bcb3408bd7d66581033902a54ac90592",
    "bc_shard_worker_blob":"ca0a4985e788455432eb59d603da54fc3c703ea6",
    "bc_shard_combiner_blob":"efcbcc3e2b31604acea8f83bbf9524e5180e5139",
    "bc_shard_runner_blob":"15dcf1e21979d3de155c57a01f6a5922dddc1ba3",
    "bc_shard_finalizer_blob":"953f70ef3f9396249743f4fdcd68f1990d917b69",
}
PATHS={
    "targets_blob":TARGETS,
    "bc_shard_worker_blob":HERE/"run_br204_full178_bc_shard.cpp",
    "bc_shard_combiner_blob":HERE/"combine_br204_bc_shards.py",
    "bc_shard_runner_blob":HERE/"run_br204_resumable_bc_shards.py",
    "bc_shard_finalizer_blob":HERE/"finalize_br204_bc_shard_checkpoint.py",
}

def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)

def blob(p:Path)->str:
    return subprocess.check_output(["git","hash-object",str(p)],text=True).strip()

def pairs(xs):
    return {(int(x[0]),int(x[1])) for x in xs}

def main()->None:
    cp=json.loads(CP.read_text())
    t=json.loads(TARGETS.read_text())
    req(cp["schema"]=="STAGE32_BR204_GENERATION2_RECOVERY_CHECKPOINT_V1","checkpoint schema")
    req(cp["generation2_run"]["run_id"]==35445118788,"run id")
    req(cp["generation2_run"]["execution_head"]=="cc8c65a13b806b7c96be23dd9f04cd6bf7ec3029","execution head")
    req(cp["generation2_run"]["conclusion"]=="failure","run conclusion")
    for k,p in PATHS.items():
        req(blob(p)==LOCKS[k],f"{k} drift")
        req(cp["source_locks"][k]==LOCKS[k],f"checkpoint {k} drift")

    target={(int(x["b"]),int(x["d"])) for x in t["targets"]}
    req(t["target_count"]==69==len(target),"target count")
    partial=pairs(cp["reconciled_execution"]["durable_partial_targets"])
    undurable=pairs(cp["reconciled_execution"]["compute_complete_but_undurable_targets"])
    expected_partial={(b,148) for b in range(2,35)}
    req(partial==expected_partial,"durable partial target set")
    req(undurable==target-partial,"compute-complete undurable target set")
    req(len(partial)==33 and len(undurable)==36 and partial.isdisjoint(undurable),"69-way reconciliation")
    req(partial|undurable==target,"reconciliation coverage")

    e=cp["emitted_summary"]
    req(e["expected_target_count"]==69,"summary expected count")
    req(e["validated_target_artifact_count"]==33,"summary artifact count")
    req(e["complete_canonical_d_count"]==0,"summary complete count")
    req(e["partial_target_count"]==33 and e["missing_target_count"]==36,"summary partial/missing counts")
    req(e["wave_complete"] is False,"summary wave_complete")
    req(e["artifact_id"]==10588869870,"summary artifact id")
    req(e["raw_json_sha256"]=="b5a4558d66fbbfe86deb93c6d392b2730a708b4396cbce912640796af4eaacab","summary raw digest")
    req(e["canonical_json_sha256"]=="c67caa94d578f7d27323ebde54ff806a883aaa90bd950daf698bd0b51ff2a246","summary canonical digest")

    hard={(int(x["b"]),int(x["d"])) for x in cp["reconciled_execution"]["persisted_generation1_hard_stops"]}
    req(hard=={(2,110),(5,108),(30,104)},"hard-stop identity")
    req(hard<=undurable,"hard-stops must be compute-complete-but-undurable")
    req(all(x["generation2_compute"]=="COMPLETE_16_OF_16" for x in cp["reconciled_execution"]["persisted_generation1_hard_stops"]),"hard-stop compute closure")
    req(cp["reconciled_execution"]["d148_boundary"]["b2"]["completed_parent_bc16_shards"]==[0],"b2 d148 carry parent")
    req(cp["generation3_requirements"]["d148_hierarchical_class"]["retained_parent_shards"]==[{"b":2,"d":148,"parent_bc16_index":0}],"generation3 carry identity")
    req(cp["generation3_requirements"]["blind_generation2_rerun_forbidden"] is True,"blind rerun firewall")
    req(cp["generation3_requirements"]["fresh_hostile_audit_required_before_generation3_arm"] is True,"audit gate")
    req(all(v is False for v in cp["credit"].values()),"credit firewall")
    print("PASS BR204 generation2 recovery checkpoint")
    print("targets=69 compute_complete_undurable=36 durable_partial=33 hardstops_compute_complete=3")
    print("d148_hierarchical_targets=33 retained_parent16_shards=1")

if __name__=="__main__":
    main()
