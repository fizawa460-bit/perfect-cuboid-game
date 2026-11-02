#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x60_packet as packet
import verify_mb104_000707_fibration_shell0_x60_packet as packet_verify
import verify_mb104_000707_gen19_x61_packet_carry as carry19

HERE=Path(__file__).resolve().parent
GEN13=HERE/"MB104-000707-GEN13-SHARD0-CARRY-MANIFEST.json"; GEN17=HERE/"MB104-000707-GEN17-SECONDARY-CARRY-MANIFEST.json"; GEN17B=HERE/"MB104-000707-GEN17-SECONDARY-CARRY-BUNDLE.json"; GEN19=HERE/"MB104-000707-GEN19-X61-PACKET-CARRY-MANIFEST.json"; GEN19B=HERE/"MB104-000707-GEN19-X61-PACKET-CARRY-BUNDLE.json"
SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X60_INTERVAL_AGGREGATE_V1"
def fsha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def gen15_digest(r):
    v=r.get("zip_digest_sha256",r.get("zip_digest")); assert isinstance(v,str) and v
    return v.split(":",1)[1] if v.startswith("sha256:") else v
def carry_chain():
    m13=json.loads(GEN13.read_text()); m17=json.loads(GEN17.read_text()); m19,p19,c19=carry19.decode_bundle()
    a=m13["artifact"]
    gen13={"certificate_file_sha256":a["certificate_file_sha256"],"certificate_canonical_sha256":a["certificate_canonical_sha256"],"artifact_id":int(a["id"]),"artifact_zip_digest_sha256":a["zip_digest_sha256"],"exact_bytes_not_regenerated":bool(a["retained_certificate_bundle"]["exact_bytes_not_regenerated"])}
    gen15=sorted([{"value":int(r["value"]),"certificate_file_sha256":r["certificate_file_sha256"],"canonical_sha256":r["canonical"],"artifact_id":int(r["artifact_id"]),"artifact_zip_digest_sha256":gen15_digest(r)} for r in m13["generation15_singleton_carry"]["artifact_provenance"]],key=lambda r:r["value"])
    gen17={"manifest_file_sha256":fsha(GEN17),"bundle_file_sha256":fsha(GEN17B),"payload_sha256":m17["durable_bundle"]["payload_sha256"],"gzip_sha256":m17["durable_bundle"]["gzip_sha256"],"complete_count":int(m17["complete_count"]),"incomplete_count":len(m17["incomplete_cells"]),"exact_bytes_not_regenerated":bool(m17["durable_bundle"]["exact_bytes_not_regenerated"])}
    gen19={"manifest_file_sha256":fsha(GEN19),"bundle_file_sha256":fsha(GEN19B),"payload_sha256":m19["durable_bundle"]["payload_sha256"],"gzip_sha256":m19["durable_bundle"]["gzip_sha256"],"packet_count":int(m19["packet_count"]),"singleton_child_count":int(m19["singleton_child_count"]),"complete_child_count":int(m19["complete_child_count"]),"incomplete_child_count":int(m19["incomplete_child_count"]),"artifact_provenance":m19["artifact_provenance"],"exact_bytes_not_regenerated":bool(m19["durable_bundle"]["exact_bytes_not_regenerated"])}
    assert len(c19)==29 and gen19["complete_child_count"]==123 and gen19["incomplete_child_count"]==23
    return {"gen13":gen13,"gen15":gen15,"gen17":gen17,"gen19":gen19}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input-dir",type=Path,required=True); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args()
    expected=set(packet.residual_leaves()); observed={}; candidates=[]; sx=set(); sf=set(); integral=0
    for path in sorted(a.input_dir.glob("*.json")):
        d=json.loads(path.read_text()); p=d.get("partition",{}); key=(int(p.get("primary_value",999)),int(p.get("secondary_residue",999)),int(p.get("fixed_x61_value",999)))
        if key not in expected or key in observed: continue
        d=packet_verify.validate_certificate(path,*key); observed[key]=d
        integral+=int(d["result"]["integral_known140_nonnegative_solution_count"])
        for rec in d["result"]["primitive_known140_nonnegative_candidates"]:
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"]); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); candidates.append(rec)
    missing=sorted([list(x) for x in expected-set(observed)])
    incomplete=sorted([list(k) for k,d in observed.items() if not d["result"]["complete"]])
    complete=not missing and not incomplete and len(observed)==23
    hashes={f"{k[0]}:{k[1]}:{k[2]}":d["canonical_sha256_without_this_field"] for k,d in sorted(observed.items())}
    candidates.sort(key=lambda r:tuple(r["picard_basis_coordinates"]))
    out={"schema":SCHEMA,"status":"COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT" if complete else "PARTIAL_X60_INTERVAL_RECOVERY_NO_CREDIT","complete":complete,"provenance":{"producing_generation":json.loads((HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json").read_text())["generation"],"producing_mode":json.loads((HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json").read_text())["mode"],"producing_execution_head":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"semantic_source_locks":packet.semantic_source_locks(),"carry_chain":carry_chain()},"packet_input_canonical_sha256":hashes,"coverage":{"expected_packet_count":23,"observed_packet_count":len(observed),"expected_x60_interval_child_count":184,"refinement_coordinate_0based":60,"refinement_bound":[-20,20],"refinement_intervals":packet.x60_contract()["intervals"],"refinement_is_exact_disjoint":True,"missing_packets":missing,"incomplete_packets":incomplete},"result":{"integral_known140_nonnegative_solution_count":integral if complete else None,"primitive_candidate_count":len(candidates) if complete else None,"primitive_candidates":candidates if complete else []},"credit_firewall":{"numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,"global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=parent.csha(out); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"success":True,"complete":complete,"observed_packets":len(observed),"missing":len(missing),"incomplete":len(incomplete),"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
    raise SystemExit(0 if complete else 2)
if __name__=="__main__": main()
