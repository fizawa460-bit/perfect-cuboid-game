#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x60_singleton_packet as packet
import aggregate_mb104_000707_fibration_shell0_x60_singleton_packets as agg
def validate(path,require_complete=False):
    d=json.loads(Path(path).read_text()); assert d["schema"]==agg.SCHEMA; cl=d["canonical_sha256_without_this_field"]; b=dict(d); b.pop("canonical_sha256_without_this_field"); assert parent.csha(b)==cl and d["provenance"]["producing_execution_head"]==subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip() and d["provenance"]["semantic_source_locks"]==packet.semantic_source_locks() and d["provenance"]["gen21_carry"]==agg.chain(); c=d["coverage"]; assert c["carried_complete_x60_interval_child_count"]==122 and c["expected_packet_count"]==62 and c["expected_x60_singleton_child_count"]==311 and c["refinement_coordinate_0based"]==60 and c["refinement_is_exact_disjoint"] is True and all(v is False for v in d["credit_firewall"].values())
    if d["complete"]: assert d["status"]=="COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT" and c["observed_packet_count"]==62 and c["missing_packets"]==[] and c["incomplete_packets"]==[]
    else: assert d["status"]=="PARTIAL_X60_SINGLETON_RECOVERY_NO_CREDIT"
    if require_complete: assert d["complete"] is True
    return d
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--require-complete",action="store_true"); a=ap.parse_args(); d=validate(a.certificate,a.require_complete); print(json.dumps({"success":True,"complete":d["complete"],"observed_packets":d["coverage"]["observed_packet_count"],"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
