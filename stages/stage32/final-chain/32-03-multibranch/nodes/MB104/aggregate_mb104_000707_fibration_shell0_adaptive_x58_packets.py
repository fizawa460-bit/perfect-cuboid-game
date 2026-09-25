#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_adaptive_x58_packet as packet
import verify_mb104_000707_fibration_shell0_adaptive_x58_packet as pv
import verify_mb104_000707_gen23_x60_singleton_carry as carry
HERE=Path(__file__).resolve().parent
INDEX=HERE/"MB104-000707-GEN23-X60-SINGLETON-CARRY-INDEX.json"
SOURCE=HERE/"MB104-000707-GEN23-X60-SINGLETON-CARRY-SOURCE.json"
RESIDUAL=HERE/"MB104-000707-GEN24-X60-SINGLETON-RESIDUAL30.json"
COLD=HERE/"MB104-000707-GEN25-ADAPTIVE-AFFINE-COLD.json"
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_AGGREGATE_V1"

def fsha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def chain():
    idx,_=carry.decode_carry()
    cold=packet.cold()
    k=json.loads(RUNKEY.read_text())
    pred=k["execution_gate"]["predecessor_audited_surface"]
    assert pred["status"]=="PASS"
    return {
        "gen23_index_file_sha256":fsha(INDEX),
        "gen23_source_file_sha256":fsha(SOURCE),
        "gen24_residual_file_sha256":fsha(RESIDUAL),
        "gen25_cold_file_sha256":fsha(COLD),
        "gen23_payload_sha256":idx["payload_sha256"],
        "gen23_gzip_sha256":idx["gzip_sha256"],
        "carried_complete_x60_singletons":281,
        "residual_timeout_x60_singletons":30,
        "necessary_condition_empty_leaf_count":14,
        "adaptive_split_leaf_count":16,
        "adaptive_interval_child_count":128,
        "gen25_cold_canonical_sha256":cold["canonical_sha256_without_this_field"],
        "predecessor_audited_surface":pred,
        "exact_bytes_not_regenerated":True,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    expected=set(packet.split_rows())
    obs={}; prim=[]; sx=set(); sf=set(); integral=0
    for path in sorted(a.input_dir.glob("*.json")):
        d=json.loads(path.read_text()); q=d.get("partition",{})
        key=(int(q.get("primary_value",999)),int(q.get("secondary_residue",999)),int(q.get("fixed_x61_value",999)),
             int(q.get("x60_residue",999)),int(q.get("fixed_x60_value",999)))
        if key not in expected or key in obs:
            continue
        d=pv.validate_certificate(path,*key)
        obs[key]=d
        integral+=int(d["result"]["integral_known140_nonnegative_solution_count"])
        for rec in d["result"]["primitive_known140_nonnegative_candidates"]:
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"])
            assert xk not in sx and fk not in sf
            sx.add(xk); sf.add(fk); prim.append(rec)
    missing=sorted([list(k) for k in expected-set(obs)])
    incomplete=sorted([list(k) for k,d in obs.items() if not d["result"]["complete"]])
    complete=not missing and not incomplete and len(obs)==16
    hashes={":".join(map(str,k)):d["canonical_sha256_without_this_field"] for k,d in sorted(obs.items())}
    empties=[{"key":list(k),"conditioned_residual_energy":v["conditioned_residual_energy"],
              "source_canonical_sha256":v["source_canonical_sha256"]} for k,v in sorted(packet.empty_rows().items())]
    prim.sort(key=lambda q:tuple(q["picard_basis_coordinates"]))
    out={
        "schema":SCHEMA,
        "status":"COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT" if complete else "PARTIAL_ADAPTIVE_X58_RECOVERY_NO_CREDIT",
        "complete":complete,
        "provenance":{
            "producing_execution_head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
            "semantic_source_locks":packet.semantic_source_locks(),
            "gen23_carry_gen25_cold_chain":chain(),
        },
        "packet_input_canonical_sha256":hashes,
        "necessary_condition_empty_leaves":empties,
        "coverage":{
            "carried_complete_x60_singleton_child_count":281,
            "residual_timeout_x60_singleton_count":30,
            "necessary_condition_empty_leaf_count":14,
            "adaptive_split_leaf_count":16,
            "expected_packet_count":16,
            "observed_packet_count":len(obs),
            "expected_adaptive_x58_interval_child_count":128,
            "refinement_coordinate_0based":58,
            "refinement_is_exact_disjoint":True,
            "missing_packets":missing,
            "incomplete_packets":incomplete,
        },
        "result":{
            "integral_known140_nonnegative_solution_count":integral if complete else None,
            "primitive_candidate_count":len(prim) if complete else None,
            "primitive_candidates":prim if complete else [],
        },
        "credit_firewall":{
            "numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,
            "global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,
            "theorem_credit":False,"endpoint_credit":False,"merge_authorized":False
        }
    }
    out["canonical_sha256_without_this_field"]=parent.csha(out)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"success":True,"complete":complete,"observed_packets":len(obs),"missing":len(missing),
                      "incomplete":len(incomplete),"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
    raise SystemExit(0 if complete else 2)

if __name__=="__main__":
    main()
