#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x59_packet as packet
import aggregate_mb104_000707_fibration_shell0_x59_packets as agg
def validate(path,require_complete=False):
 d=json.loads(Path(path).read_text()); assert d["schema"]==agg.SCHEMA; cl=d["canonical_sha256_without_this_field"]; b=dict(d); b.pop("canonical_sha256_without_this_field"); assert parent.csha(b)==cl and d["provenance"]["producing_execution_head"]==subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip() and d["provenance"]["semantic_source_locks"]==packet.semantic_source_locks() and d["provenance"]["gen23_carry_and_gen24_cold"]==agg.chain()
 c=d["coverage"]; assert int(c["carried_complete_x60_singleton_child_count"])==281 and int(c["residual_timeout_x60_singleton_count"])==30 and int(c["expected_packet_count"])==30 and int(c["expected_x59_interval_child_count"])==240 and int(c["refinement_coordinate_0based"])==59 and c["refinement_is_exact_disjoint"] is True and all(v is False for v in d["credit_firewall"].values())
 if d["complete"]: assert d["status"]=="COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT" and int(c["observed_packet_count"])==30 and c["missing_packets"]==[] and c["incomplete_packets"]==[]
 else: assert d["status"]=="PARTIAL_X59_INTERVAL_RECOVERY_NO_CREDIT"
 if require_complete: assert d["complete"] is True
 return d
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--require-complete",action="store_true"); a=ap.parse_args(); d=validate(a.certificate,a.require_complete); print(json.dumps({"success":True,"complete":d["complete"],"observed_packets":d["coverage"]["observed_packet_count"],"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
