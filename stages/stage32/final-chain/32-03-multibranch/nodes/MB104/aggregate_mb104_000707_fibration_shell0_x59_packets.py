#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x59_packet as packet
import verify_mb104_000707_fibration_shell0_x59_packet as pv
import verify_mb104_000707_gen23_x60_singleton_carry as carry
HERE=Path(__file__).resolve().parent
INDEX=HERE/"MB104-000707-GEN23-X60-SINGLETON-CARRY-INDEX.json"; SOURCE=HERE/"MB104-000707-GEN23-X60-SINGLETON-CARRY-SOURCE.json"; RESIDUAL=HERE/"MB104-000707-GEN24-X60-SINGLETON-RESIDUAL30.json"; COLD=HERE/"MB104-000707-GEN24-X59-INTERVAL-COLD-PREFLIGHT.json"
SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X59_INTERVAL_AGGREGATE_V1"
def fsha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def chain():
 idx,p=carry.decode_carry(); c=json.loads(COLD.read_text())
 return {"gen23_index_file_sha256":fsha(INDEX),"gen23_source_file_sha256":fsha(SOURCE),"gen24_residual_file_sha256":fsha(RESIDUAL),"gen24_cold_file_sha256":fsha(COLD),"gen23_payload_sha256":idx["payload_sha256"],"gen23_gzip_sha256":idx["gzip_sha256"],"carried_complete_x60_singletons":281,"residual_timeout_x60_singletons":30,"cold_canonical_sha256":c["canonical_sha256_without_this_field"],"exact_bytes_not_regenerated":True}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--input-dir",type=Path,required=True); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args(); expected=set(packet.residual_rows()); obs={}; prim=[]; sx=set(); sf=set(); integral=0
 for path in sorted(a.input_dir.glob("*.json")):
  d=json.loads(path.read_text()); q=d.get("partition",{}); key=(int(q.get("primary_value",999)),int(q.get("secondary_residue",999)),int(q.get("fixed_x61_value",999)),int(q.get("x60_residue",999)),int(q.get("fixed_x60_value",999)))
  if key not in expected or key in obs: continue
  d=pv.validate_certificate(path,*key); obs[key]=d; integral+=int(d["result"]["integral_known140_nonnegative_solution_count"])
  for rec in d["result"]["primitive_known140_nonnegative_candidates"]:
   xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"]); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); prim.append(rec)
 missing=sorted([list(k) for k in expected-set(obs)]); incomplete=sorted([list(k) for k,d in obs.items() if not d["result"]["complete"]]); complete=not missing and not incomplete and len(obs)==30; hashes={":".join(map(str,k)):d["canonical_sha256_without_this_field"] for k,d in sorted(obs.items())}
 out={"schema":SCHEMA,"status":"COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT" if complete else "PARTIAL_X59_INTERVAL_RECOVERY_NO_CREDIT","complete":complete,"provenance":{"producing_execution_head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"semantic_source_locks":packet.semantic_source_locks(),"gen23_carry_and_gen24_cold":chain()},"packet_input_canonical_sha256":hashes,"coverage":{"carried_complete_x60_singleton_child_count":281,"residual_timeout_x60_singleton_count":30,"expected_packet_count":30,"observed_packet_count":len(obs),"expected_x59_interval_child_count":240,"refinement_coordinate_0based":59,"refinement_is_exact_disjoint":True,"missing_packets":missing,"incomplete_packets":incomplete},"result":{"integral_known140_nonnegative_solution_count":integral if complete else None,"primitive_candidate_count":len(prim) if complete else None,"primitive_candidates":prim if complete else []},"credit_firewall":{"numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,"global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False}}
 out["canonical_sha256_without_this_field"]=parent.csha(out); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n"); print(json.dumps({"success":True,"complete":complete,"observed_packets":len(obs),"missing":len(missing),"incomplete":len(incomplete),"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True)); raise SystemExit(0 if complete else 2)
if __name__=="__main__": main()
