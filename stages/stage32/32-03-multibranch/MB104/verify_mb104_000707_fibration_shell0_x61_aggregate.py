#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x61_packet as packet

HERE=Path(__file__).resolve().parent
GEN13_MANIFEST=HERE/"MB104-000707-GEN13-SHARD0-CARRY-MANIFEST.json"
GEN17_MANIFEST=HERE/"MB104-000707-GEN17-SECONDARY-CARRY-MANIFEST.json"
GEN17_BUNDLE=HERE/"MB104-000707-GEN17-SECONDARY-CARRY-BUNDLE.json"

def fsha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def expected_gen13(m):
    a=m["artifact"]
    return {"certificate_file_sha256":a["certificate_file_sha256"],"certificate_canonical_sha256":a["certificate_canonical_sha256"],"artifact_id":int(a["id"]),"artifact_zip_digest_sha256":a["zip_digest_sha256"],"exact_bytes_not_regenerated":bool(a["retained_certificate_bundle"]["exact_bytes_not_regenerated"])}

def gen15_zip_digest(r):
    v=r.get("zip_digest_sha256",r.get("zip_digest"))
    assert isinstance(v,str) and v
    return v.split(":",1)[1] if v.startswith("sha256:") else v

def expected_gen15(m):
    rows=[{"value":int(r["value"]),"certificate_file_sha256":r["certificate_file_sha256"],"canonical_sha256":r["canonical"],"artifact_id":int(r["artifact_id"]),"artifact_zip_digest_sha256":gen15_zip_digest(r)} for r in m["generation15_singleton_carry"]["artifact_provenance"]]
    return sorted(rows,key=lambda r:r["value"])

def expected_gen17(m):
    rows=[{"primary_value":int(r["primary_value"]),"secondary_residue":int(r["secondary_residue"]),"certificate_file_sha256":r["certificate_file_sha256"],"canonical_sha256":r["canonical_sha256"],"artifact_id":int(r["artifact_id"]),"artifact_zip_digest_sha256":r["artifact_zip_digest_sha256"]} for r in m["artifact_provenance"]]
    rows.sort(key=lambda r:(r["primary_value"],r["secondary_residue"]))
    return {"manifest_file_sha256":fsha(GEN17_MANIFEST),"bundle_file_sha256":fsha(GEN17_BUNDLE),"bundle_payload_sha256":m["durable_bundle"]["payload_sha256"],"bundle_gzip_sha256":m["durable_bundle"]["gzip_sha256"],"exact_bytes_not_regenerated":bool(m["durable_bundle"]["exact_bytes_not_regenerated"]),"complete_certificate_count":27,"complete_certificate_identities":rows}

def validate(path:Path,require_complete:bool=False):
    d=json.loads(path.read_text())
    assert d["schema"]=="STAGE32_MB104_000707_FIBRATION_SHELL0_X61_PACKET_AGGREGATE_V2"
    claimed=d["canonical_sha256_without_this_field"]; body=dict(d); body.pop("canonical_sha256_without_this_field")
    assert parent.csha(body)==claimed
    p=d["provenance"]
    assert isinstance(p["producing_execution_head"],str) and len(p["producing_execution_head"])==40
    current=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    assert p["producing_execution_head"]==current
    assert p["semantic_source_locks"]==packet.semantic_source_locks()
    m13=json.loads(GEN13_MANIFEST.read_text()); m17=json.loads(GEN17_MANIFEST.read_text())
    assert p["gen13_carry"]==expected_gen13(m13)
    assert p["gen15_carry_identities"]==expected_gen15(m13) and len(p["gen15_carry_identities"])==29
    assert p["gen17_carry"]==expected_gen17(m17) and len(p["gen17_carry"]["complete_certificate_identities"])==27
    expected_parents={tuple(map(int,x)) for x in m17["incomplete_cells"]}
    packet_hashes=d["packet_input_canonical_sha256"]
    assert set(packet_hashes)=={f"{p0}:{s}" for p0,s in expected_parents} if d["complete"] else set(packet_hashes).issubset({f"{p0}:{s}" for p0,s in expected_parents})
    assert d["coverage"]["expected_packet_count"]==29 and d["coverage"]["expected_singleton_child_count"]==146
    assert d["coverage"]["refinement_is_exact_disjoint"] is True
    assert all(v is False for v in d["credit_firewall"].values())
    if d["complete"]:
        assert d["status"]=="COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT"
        assert d["coverage"]["observed_packet_count"]==29
        assert d["coverage"]["missing_packets"]==[] and d["coverage"]["incomplete_packets"]==[]
        assert len(packet_hashes)==29
        assert d["result"]["integral_known140_nonnegative_solution_count"] is not None
        assert d["result"]["primitive_candidate_count"]==len(d["result"]["primitive_candidates"])
    else:
        assert d["status"]=="PARTIAL_X61_PACKET_RECOVERY_NO_CREDIT"
    if require_complete: assert d["complete"] is True
    return d

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--require-complete",action="store_true"); a=ap.parse_args()
    d=validate(a.certificate,a.require_complete)
    print(json.dumps({"success":True,"complete":d["complete"],"producing_execution_head":d["provenance"]["producing_execution_head"],"gen15_bound":len(d["provenance"]["gen15_carry_identities"]),"gen17_bound":len(d["provenance"]["gen17_carry"]["complete_certificate_identities"]),"packet_hashes_bound":len(d["packet_input_canonical_sha256"]),"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
