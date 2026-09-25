#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x59_packet as runner
def validate_certificate(path,p,s,x61,r60,x60):
 d=json.loads(Path(path).read_text()); assert d["schema"]==runner.SCHEMA; cl=d["canonical_sha256_without_this_field"]; b=dict(d); b.pop("canonical_sha256_without_this_field"); assert parent.csha(b)==cl
 key=(int(p),int(s),int(x61),int(r60),int(x60)); assert key in set(runner.residual_rows()); q=d["partition"]; assert (int(q["primary_value"]),int(q["secondary_residue"]),int(q["fixed_x61_value"]),int(q["x60_residue"]),int(q["fixed_x60_value"]))==key and int(q["refinement_coordinate_0based"])==59 and q["x59_intervals"]==runner.contract()["intervals"] and q["coverage_is_exact_disjoint"] is True and d["semantic_source_locks"]==runner.semantic_source_locks()
 assert len(d["children"])==8; allc=True
 for child,(lo,hi) in zip(d["children"],runner.contract()["intervals"]):
  ch=child["canonical_sha256_without_this_field"]; cb=dict(child); cb.pop("canonical_sha256_without_this_field"); assert parent.csha(cb)==ch and child["x59_interval"]==[lo,hi]; allc=allc and child["result"]["complete"]
  if child["result"]["complete"]: assert child["status"]=="COMPLETE_EXACT_X59_INTERVAL_ZERO_CREDIT" and child["solver"]["final_solver_result"]=="unsat" and child["solver"]["reason"] is None
  else: assert child["status"] in {"PARTIAL_UNKNOWN_NO_CREDIT","PARTIAL_PACKET_WALL_NO_CREDIT","PARTIAL_MODEL_CAP_NO_CREDIT","NOT_RUN_PACKET_WALL_NO_CREDIT"}
 assert d["result"]["complete"] is allc and int(d["result"]["complete_child_count"])==sum(c["result"]["complete"] for c in d["children"]) and int(d["result"]["child_count"])==8 and d["status"]==("COMPLETE_EXACT_X59_INTERVAL_PACKET_ZERO_CREDIT" if allc else "PARTIAL_X59_INTERVAL_PACKET_NO_CREDIT") and all(v is False for v in d["credit_firewall"].values()); return d
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--primary-value",type=int,required=True); ap.add_argument("--secondary-residue",type=int,required=True); ap.add_argument("--x61-value",type=int,required=True); ap.add_argument("--x60-residue",type=int,required=True); ap.add_argument("--x60-value",type=int,required=True); a=ap.parse_args(); d=validate_certificate(a.certificate,a.primary_value,a.secondary_residue,a.x61_value,a.x60_residue,a.x60_value); print(json.dumps({"success":True,"complete":d["result"]["complete"],"complete_children":d["result"]["complete_child_count"],"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
