#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, gzip, hashlib, json, os, subprocess, tempfile, zipfile
from pathlib import Path

PACKET_SCHEMA = "STAGE32_MB104_000707_FIBRATION_SHELL0_X60_SINGLETON_PACKET_V1"
AGG_SCHEMA = "STAGE32_MB104_000707_FIBRATION_SHELL0_X60_SINGLETON_AGGREGATE_V1"
RUNKEY_REL = "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/runkeys/000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"

def csha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def gh_json(path):
    return json.loads(subprocess.check_output(["gh", "api", "--method", "GET", path], text=True))

def fetch_zip(repo, aid, path):
    with path.open("wb") as f:
        subprocess.run(["gh", "api", "--method", "GET", f"repos/{repo}/actions/artifacts/{int(aid)}/zip"], check=True, stdout=f)

def one_json(path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        assert len(names) == 1 and names[0].endswith(".json"), names
        return names[0], z.read(names[0])

def child_key(r):
    return (r["primary_value"], r["secondary_residue"], r["fixed_x61_value"], r["x60_residue"], r["fixed_x60_value"])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--bundle", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--residual", type=Path, required=True)
    a = ap.parse_args()
    repo = os.environ.get("GITHUB_REPOSITORY")
    assert repo and os.environ.get("GH_TOKEN")
    src = json.loads(a.source.read_text())
    assert src["schema"] == "STAGE32_MB104_000707_GEN23_X60_SINGLETON_CARRY_SOURCE_V1"
    run_id = int(src["producing_workflow_run_id"])
    head = src["producing_execution_head"]
    assert head == "99601aef02a82858d32729dec344f103ae40af09" and run_id == 35663858139
    run = gh_json(f"repos/{repo}/actions/runs/{run_id}")
    assert run["head_sha"] == head and run["status"] == "completed"
    arts = gh_json(f"repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100")
    assert int(arts["total_count"]) == 63
    packets = [x for x in arts["artifacts"] if x["name"].startswith("stage32-mb-fib-x60-singleton-")]
    aggs = [x for x in arts["artifacts"] if x["name"] == "stage32-mb-fib-shell0-x60-singleton-aggregate"]
    assert len(packets) == 62 and len(aggs) == 1 and all(not x["expired"] for x in packets + aggs)
    assert len({x["name"] for x in packets}) == 62 and all(x["workflow_run"]["head_sha"] == head for x in packets + aggs)

    runkey = json.loads(Path(RUNKEY_REL).read_text())
    assert int(runkey["generation"]) == 23 and runkey["mode"] == "RECOVERY" and runkey["armed"] is True
    expected_run_locks = runkey["source_locks"]
    certs = []
    provenance = []
    complete = []
    incomplete = []
    canon = {}
    semantic_locks = None

    with tempfile.TemporaryDirectory() as td0:
        td = Path(td0)
        for row in sorted(packets, key=lambda x: x["name"]):
            digest = row.get("digest")
            assert isinstance(digest, str) and digest.startswith("sha256:")
            zpath = td / f"{int(row['id'])}.zip"
            fetch_zip(repo, row["id"], zpath)
            assert hashlib.sha256(zpath.read_bytes()).hexdigest() == digest.split(":", 1)[1]
            fname, raw = one_json(zpath)
            d = json.loads(raw)
            assert d["schema"] == PACKET_SCHEMA
            assert d["provenance"] == {"producing_generation": 23, "producing_mode": "RECOVERY"}
            assert all(v is False for v in d["credit_firewall"].values())
            locks = d["semantic_source_locks"]
            if semantic_locks is None:
                semantic_locks = locks
                assert all(expected_run_locks.get(k) == v for k, v in semantic_locks.items())
            else:
                assert locks == semantic_locks
            claimed = d["canonical_sha256_without_this_field"]
            body = dict(d); body.pop("canonical_sha256_without_this_field")
            assert csha(body) == claimed
            p = d["partition"]
            key = (int(p["primary_value"]), int(p["secondary_residue"]), int(p["fixed_x61_value"]), int(p["x60_residue"]))
            assert p["coverage_is_exact_disjoint"] is True
            assert len(p["x60_singleton_values"]) == len(d["children"]) == int(d["result"]["child_count"])
            cc = 0
            for child in d["children"]:
                cb = dict(child); ch = cb.pop("canonical_sha256_without_this_field")
                assert csha(cb) == ch
                rec = {"primary_value": key[0], "secondary_residue": key[1], "fixed_x61_value": key[2], "x60_residue": key[3], "fixed_x60_value": int(child["fixed_x60_value"]), "canonical_sha256": ch}
                if child["result"]["complete"]:
                    assert child["status"] == "COMPLETE_EXACT_X60_SINGLETON_ZERO_CREDIT"
                    assert child["solver"]["final_solver_result"] == "unsat" and child["solver"]["reason"] is None
                    assert child["result"]["integral_known140_nonnegative_solution_count"] == 0
                    assert child["result"]["primitive_known140_nonnegative_candidate_count"] == 0
                    assert child["result"]["primitive_known140_nonnegative_candidates"] == []
                    complete.append(rec); cc += 1
                else:
                    assert child["status"] == "PARTIAL_UNKNOWN_NO_CREDIT"
                    assert child["solver"]["final_solver_result"] == "unknown" and child["solver"]["reason"] == "timeout"
                    rec.update({"solver_result": "unknown", "reason": "timeout"})
                    incomplete.append(rec)
            assert cc == int(d["result"]["complete_child_count"])
            assert d["result"]["complete"] is (cc == int(d["result"]["child_count"]))
            fsha = hashlib.sha256(raw).hexdigest()
            provenance.append({"artifact_id": int(row["id"]), "artifact_name": row["name"], "artifact_zip_digest_sha256": digest.split(":", 1)[1], "certificate_filename": fname, "certificate_file_sha256": fsha, "canonical_sha256": claimed, "primary_value": key[0], "secondary_residue": key[1], "fixed_x61_value": key[2], "x60_residue": key[3], "child_count": int(d["result"]["child_count"]), "complete_child_count": cc})
            certs.append({"artifact_name": row["name"], "certificate_filename": fname, "certificate_file_sha256": fsha, "canonical_sha256": claimed, "base64": base64.b64encode(raw).decode("ascii")})
            canon[f"{key[0]}:{key[1]}:{key[2]}:{key[3]}"] = claimed

        ar = aggs[0]
        digest = ar["digest"]; assert digest.startswith("sha256:")
        az = td / "aggregate.zip"; fetch_zip(repo, ar["id"], az)
        assert hashlib.sha256(az.read_bytes()).hexdigest() == digest.split(":", 1)[1]
        afname, araw = one_json(az); ag = json.loads(araw)
        assert ag["schema"] == AGG_SCHEMA
        ac = ag["canonical_sha256_without_this_field"]; ab = dict(ag); ab.pop("canonical_sha256_without_this_field")
        assert csha(ab) == ac == src["aggregate_canonical_sha256"]
        assert ag["complete"] is False and ag["status"] == "PARTIAL_X60_SINGLETON_RECOVERY_NO_CREDIT"
        assert int(ag["coverage"]["observed_packet_count"]) == 62 and ag["coverage"]["missing_packets"] == []
        assert len(ag["coverage"]["incomplete_packets"]) == 29
        assert ag["packet_input_canonical_sha256"] == canon
        aggregate = {"artifact_id": int(ar["id"]), "artifact_name": ar["name"], "artifact_zip_digest_sha256": digest.split(":",1)[1], "certificate_filename": afname, "certificate_file_sha256": hashlib.sha256(araw).hexdigest(), "canonical_sha256": ac, "base64": base64.b64encode(araw).decode("ascii")}

    complete.sort(key=child_key); incomplete.sort(key=child_key)
    provenance.sort(key=lambda r:(r["primary_value"],r["secondary_residue"],r["fixed_x61_value"],r["x60_residue"]))
    certs.sort(key=lambda r:r["artifact_name"])
    assert len(complete) == int(src["expected_complete_singleton_child_count"]) == 281
    assert len(incomplete) == int(src["expected_incomplete_singleton_child_count"]) == 30
    assert len(complete) + len(incomplete) == int(src["singleton_child_count"]) == 311
    expected_residual = sorted(src["expected_residual_singletons"], key=child_key)
    actual_residual = [{k:r[k] for k in ("primary_value","secondary_residue","fixed_x61_value","x60_residue","fixed_x60_value")} for r in incomplete]
    assert actual_residual == expected_residual

    payload = {"schema":"STAGE32_MB104_000707_GEN23_X60_SINGLETON_PACKET_CARRY_BUNDLE_V1","producing_generation":23,"producing_mode":"RECOVERY","producing_execution_head":head,"producing_workflow_run_id":run_id,"source_locks":semantic_locks,"packet_count":62,"singleton_child_count":311,"complete_singleton_child_count":281,"incomplete_singleton_child_count":30,"complete_children":complete,"incomplete_children":incomplete,"certificates":certs,"aggregate_certificate":aggregate}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(); packed = gzip.compress(raw, mtime=0)
    env = {"schema":"STAGE32_MB104_000707_GEN23_X60_SINGLETON_DURABLE_PACKET_CARRY_ENVELOPE_V1","encoding":"gzip+base64","gzip_sha256":hashlib.sha256(packed).hexdigest(),"payload_sha256":hashlib.sha256(raw).hexdigest(),"byte_length":len(raw),"compressed_byte_length":len(packed),"base64":base64.b64encode(packed).decode("ascii"),"exact_bytes_not_regenerated":True}
    a.bundle.write_text(json.dumps(env, indent=2, sort_keys=True)+"\n")
    manifest = dict(src)
    manifest["schema"] = "STAGE32_MB104_000707_GEN23_X60_SINGLETON_PACKET_CARRY_MANIFEST_V1"
    manifest["artifact_provenance"] = provenance
    manifest["complete_children"] = complete
    manifest["incomplete_children"] = incomplete
    manifest["aggregate_provenance"] = {k:v for k,v in aggregate.items() if k != "base64"}
    manifest["durable_bundle"] = {"schema":env["schema"],"gzip_sha256":env["gzip_sha256"],"payload_sha256":env["payload_sha256"],"exact_bytes_not_regenerated":True}
    a.manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True)+"\n")
    residual = {"schema":"STAGE32_MB104_000707_GEN24_X60_SINGLETON_RESIDUAL30_V1","source_generation":23,"source_execution_head":head,"source_workflow_run_id":run_id,"complete_singleton_child_count":281,"residual_timeout_singleton_count":30,"residual_singletons":incomplete,"credit":False}
    a.residual.write_text(json.dumps(residual, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"success":True,"packets":62,"singleton_children":311,"complete_singletons":281,"residual_timeout_singletons":30,"payload_sha256":env["payload_sha256"],"gzip_sha256":env["gzip_sha256"],"compressed_bytes":len(packed)}, sort_keys=True))

if __name__ == "__main__":
    main()
