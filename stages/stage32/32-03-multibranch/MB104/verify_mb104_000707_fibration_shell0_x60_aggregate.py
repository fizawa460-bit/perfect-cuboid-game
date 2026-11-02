#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x60_packet as packet
import aggregate_mb104_000707_fibration_shell0_x60_packets as agg

def validate(path,require_complete=False):
    d=json.loads(Path(path).read_text()); assert d["schema"]==agg.SCHEMA
    claimed=d["canonical_sha256_without_this_field"]; body=dict(d); body.pop("canonical_sha256_without_this_field"); assert parent.csha(body)==claimed
    p=d["provenance"]; assert isinstance(p["producing_execution_head"],str) and len(p["producing_execution_head"])==40
    assert p["producing_execution_head"]==subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    assert p["semantic_source_locks"]==packet.semantic_source_locks() and p["carry_chain"]==agg.carry_chain()
    expected={f"{a}:{b}:{c}" for a,b,c in packet.residual_leaves()}; hashes=d["packet_input_canonical_sha256"]
    assert set(hashes).issubset(expected); cov=d["coverage"]; assert cov["expected_packet_count"]==23 and cov["expected_x60_interval_child_count"]==184 and cov["refinement_coordinate_0based"]==60 and cov["refinement_bound"]==[-20,20] and cov["refinement_intervals"]==packet.x60_contract()["intervals"] and cov["refinement_is_exact_disjoint"] is True
    assert all(v is False for v in d["credit_firewall"].values())
    if d["complete"]:
        assert d["status"]=="COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT" and cov["observed_packet_count"]==23 and cov["missing_packets"]==[] and cov["incomplete_packets"]==[] and len(hashes)==23 and d["result"]["integral_known140_nonnegative_solution_count"] is not None and d["result"]["primitive_candidate_count"]==len(d["result"]["primitive_candidates"])
    else:
        assert d["status"]=="PARTIAL_X60_INTERVAL_RECOVERY_NO_CREDIT"
    if require_complete: assert d["complete"] is True
    return d
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--require-complete",action="store_true"); a=ap.parse_args(); d=validate(a.certificate,a.require_complete); print(json.dumps({"success":True,"complete":d["complete"],"observed_packets":d["coverage"]["observed_packet_count"],"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
