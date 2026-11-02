#!/usr/bin/env python3
from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[5]
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
STATE=HERE.parents[1]/"fib"/"STATE.json"
COLD=HERE/"MB104-000707-GEN24-X59-INTERVAL-COLD-PREFLIGHT.json"
DERIVE=HERE/"derive_mb104_000707_gen24_nextcoord_cold.py"
RESIDUAL=HERE/"MB104-000707-GEN24-X60-SINGLETON-RESIDUAL30.json"
PATHS={
 "gen23_carry_source_git_blob":HERE/"MB104-000707-GEN23-X60-SINGLETON-CARRY-SOURCE.json",
 "gen23_carry_index_git_blob":HERE/"MB104-000707-GEN23-X60-SINGLETON-CARRY-INDEX.json",
 "gen23_carry_verifier_git_blob":HERE/"verify_mb104_000707_gen23_x60_singleton_carry.py",
 "gen24_residual_git_blob":RESIDUAL,
 "gen24_nextcoord_derive_git_blob":DERIVE,
 "gen24_x59_cold_preflight_git_blob":COLD,
 "gen24_x59_cold_verifier_git_blob":HERE/"verify_mb104_000707_gen24_x59_interval_cold.py",
 "local_exact_engine_git_blob":HERE/"run_mb104_000707_fibration_shell_local_exact.py",
 "runner_git_blob":HERE/"run_mb104_000707_fibration_isotropic_shells.py",
}
def blob(p): return subprocess.check_output(["git","hash-object",str(p)],cwd=REPO,text=True).strip()
def main():
 k=json.loads(RUNKEY.read_text()); s=json.loads(STATE.read_text()); sl=k["source_locks"]
 for field,path in PATHS.items(): assert blob(path)==sl[field],(field,blob(path),sl[field])
 frozen=json.loads(COLD.read_text())
 raw=subprocess.check_output([sys.executable,str(DERIVE)],cwd=HERE,text=True)
 derived=json.loads(raw)
 assert frozen==derived
 assert frozen["schema"]=="STAGE32_MB104_000707_GEN24_NEXTCOORD_COLD_PREFLIGHT_V1"
 assert frozen["status"]=="COLD_PREPARED_NO_HEAVY_EXECUTION_NO_CREDIT"
 assert frozen["canonical_sha256_without_this_field"]=="2e275b5d3dded8cd2b01e5b5707a682aa3add52425525af9ded8ffb07be67904"
 assert int(frozen["source_generation"])==23 and int(frozen["carried_complete_x60_singletons"])==281 and int(frozen["residual_timeout_leaf_count"])==30
 c=frozen["next_coordinate_contract"]
 assert int(c["coordinate_0based"])==59 and c["bound"]==[-20,20] and int(c["domain_size"])==41
 assert c["intervals"]==[[-20,-16],[-15,-11],[-10,-6],[-5,-1],[0,4],[5,9],[10,14],[15,20]]
 assert int(c["shard_count"])==8 and c["coverage_is_exact_disjoint"] is True
 assert int(frozen["planned_packet_count"])==30 and int(frozen["planned_interval_child_count"])==240 and int(frozen["planned_effective_heavy_concurrency"])==4
 assert frozen["recompute_carried_complete_regions"] is False and frozen["heavy_armed"] is False and frozen["execution_authorized"] is False
 assert all(v is False for v in frozen["credit_firewall"].values())
 sc=k["successor_cold"]
 assert int(sc["source_generation"])==23 and int(sc["refinement_coordinate_0based"])==59 and sc["bound"]==[-20,20] and sc["intervals"]==c["intervals"]
 assert int(sc["expected_packet_count"])==30 and int(sc["expected_interval_child_count"])==240 and int(sc["max_parallel"])==4 and sc["recompute_prior_complete_regions"] is False
 assert sc["cold_canonical_sha256"]==frozen["canonical_sha256_without_this_field"]
 if int(k["generation"])==24:
  assert k["mode"]=="COLD" and k["armed"] is False
  assert s["audit"]["status"]=="PENDING" and s["execution"]["heavy_armed"] is False and s["execution"]["execution_authorized"] is False
 else:
  assert int(k["generation"])>=25 and k["mode"]=="RECOVERY"
 print(json.dumps({"success":True,"generation":k["generation"],"coordinate_0based":59,"packets":30,"interval_children":240,"canonical":frozen["canonical_sha256_without_this_field"],"credit":False},sort_keys=True))
if __name__=="__main__": main()
