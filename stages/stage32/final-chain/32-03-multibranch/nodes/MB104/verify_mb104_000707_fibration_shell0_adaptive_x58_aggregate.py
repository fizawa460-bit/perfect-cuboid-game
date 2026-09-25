#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_adaptive_x58_packet as packet
import verify_mb104_000707_fibration_shell0_adaptive_x58_packet as pv
import aggregate_mb104_000707_fibration_shell0_adaptive_x58_packets as agg

def packet_key(d):
    q=d["partition"]
    return (int(q["primary_value"]),int(q["secondary_residue"]),int(q["fixed_x61_value"]),
            int(q["x60_residue"]),int(q["fixed_x60_value"]))

def validated_packet_union(input_dir):
    expected=set(packet.split_rows()); obs={}; integral=0; prim=[]; sx=set(); sf=set()
    for path in sorted(Path(input_dir).glob("*.json")):
        raw=json.loads(path.read_text())
        key=packet_key(raw)
        assert key in expected and key not in obs
        d=pv.validate_certificate(path,*key)
        obs[key]=d
        integral+=int(d["result"]["integral_known140_nonnegative_solution_count"])
        for rec in d["result"]["primitive_known140_nonnegative_candidates"]:
            replay=parent.replay_solution(0,[int(v) for v in rec["x_hperp_coordinates"]])
            assert replay==rec and replay["primitive"] is True
            xk=tuple(int(v) for v in rec["x_hperp_coordinates"])
            fk=tuple(int(v) for v in rec["picard_basis_coordinates"])
            assert xk not in sx and fk not in sf
            sx.add(xk); sf.add(fk); prim.append(rec)
    prim.sort(key=lambda rec:tuple(rec["picard_basis_coordinates"]))
    missing=sorted([list(k) for k in expected-set(obs)])
    incomplete=sorted([list(k) for k,d in obs.items() if not d["result"]["complete"]])
    hashes={":".join(map(str,k)):d["canonical_sha256_without_this_field"] for k,d in sorted(obs.items())}
    return obs,integral,prim,missing,incomplete,hashes

def validate(path,input_dir,require_complete=False):
    d=json.loads(Path(path).read_text())
    assert d["schema"]==agg.SCHEMA
    cl=d["canonical_sha256_without_this_field"]; b=dict(d); b.pop("canonical_sha256_without_this_field")
    assert parent.csha(b)==cl
    assert d["provenance"]["producing_execution_head"]==subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    assert d["provenance"]["semantic_source_locks"]==packet.semantic_source_locks()
    assert d["provenance"]["gen23_carry_gen25_cold_chain"]==agg.chain()
    c=d["coverage"]
    assert int(c["carried_complete_x60_singleton_child_count"])==281
    assert int(c["residual_timeout_x60_singleton_count"])==30
    assert int(c["necessary_condition_empty_leaf_count"])==14
    assert int(c["adaptive_split_leaf_count"])==16
    assert int(c["expected_packet_count"])==16
    assert int(c["expected_adaptive_x58_interval_child_count"])==128
    assert int(c["refinement_coordinate_0based"])==58
    assert c["refinement_is_exact_disjoint"] is True
    expected_empties=[{"key":list(k),"conditioned_residual_energy":v["conditioned_residual_energy"],
                       "source_canonical_sha256":v["source_canonical_sha256"]} for k,v in sorted(packet.empty_rows().items())]
    assert d["necessary_condition_empty_leaves"]==expected_empties
    assert all(int(x["conditioned_residual_energy"][0])<0 for x in expected_empties)
    obs,integral,prim,missing,incomplete,hashes=validated_packet_union(input_dir)
    assert int(c["observed_packet_count"])==len(obs)
    assert c["missing_packets"]==missing and c["incomplete_packets"]==incomplete
    assert d["packet_input_canonical_sha256"]==hashes
    complete=not missing and not incomplete and len(obs)==16
    assert d["complete"] is complete
    assert all(v is False for v in d["credit_firewall"].values())
    if complete:
        assert d["status"]=="COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT"
        assert int(d["result"]["integral_known140_nonnegative_solution_count"])==integral
        assert int(d["result"]["primitive_candidate_count"])==len(prim)
        assert d["result"]["primitive_candidates"]==prim
    else:
        assert d["status"]=="PARTIAL_ADAPTIVE_X58_RECOVERY_NO_CREDIT"
        assert d["result"]["integral_known140_nonnegative_solution_count"] is None
        assert d["result"]["primitive_candidate_count"] is None
        assert d["result"]["primitive_candidates"]==[]
    if require_complete:
        assert complete
    return d

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--certificate",type=Path,required=True)
    ap.add_argument("--input-dir",type=Path,required=True)
    ap.add_argument("--require-complete",action="store_true")
    a=ap.parse_args()
    d=validate(a.certificate,a.input_dir,a.require_complete)
    print(json.dumps({"success":True,"complete":d["complete"],"observed_packets":d["coverage"]["observed_packet_count"],
                      "primitive_candidates":d["result"]["primitive_candidate_count"],
                      "canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":
    main()
