#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_fibration_nef_selective_picard_workunit.py"
WORKER_BLOB = "4533280fe489547395fd6c51fdb0e4de8403e54b"
PLAN = HERE / "verify_fibration_nef_selective_workunit_plan_certificate.py"
PLAN_BLOB = "37745be7877f32a1804a350d8ebbeedc893d4a5b"
SCHEMA = "STAGE32_32_01_178_SELECTIVE_PICARD_RECOVERY_SNAPSHOT_V1"

def req(v, m):
    if not v: raise ValueError(m)

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec); sys.modules[name] = mod; spec.loader.exec_module(mod)
    return mod

def csha(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def stream_sha(records):
    h = hashlib.sha256()
    for r in records:
        h.update(json.dumps(r, sort_keys=True, separators=(",", ":")).encode()); h.update(b"\n")
    return h.hexdigest()

def expected_units(worker, rt):
    out = {}
    slice_summary = []
    for x4 in worker.SELECTED_X4:
        rows, _ = rt["sel"].survivor_rows(
            sf=rt["sf"], depth2=rt["depth2"], depth1=rt["depth1"], sigmod=rt["sigmod"],
            prefix=rt["prefix"], bnb=rt["bnb"], kernel=rt["kernel"], cert=rt["cert"],
            static_keys=rt["static_keys"], g=rt["g"], d=rt["d"], e=rt["e"], x4_values=(x4,))
        req(len(rows) == 1 and rows[0][0] == x4, "single-slice reconstruction drift")
        ordered = tuple(sorted(rows[0][1]))
        req(len(ordered) == len(set(ordered)), "duplicate survivor key")
        records = [{"row_id":"g1-d192","e":rt["e"],"x4":x4,"a":a,"b":b,"c":c,"t":t} for a,b,c,t in ordered]
        count = 0
        for ordinal, start in enumerate(range(0, len(records), worker.WORKUNIT_SIZE)):
            chunk = records[start:start+worker.WORKUNIT_SIZE]
            ident = {"workunit_id":f"g1-d192-e032-x4-{x4:04d}-u{ordinal:04d}","x4":x4,
                     "start_index":start,"stop_index_exclusive":start+len(chunk),
                     "static_key_count":len(chunk),"static_key_stream_sha256":stream_sha(chunk)}
            out[ident["workunit_id"]] = ident; count += 1
        slice_summary.append({"x4":x4,"survivor_static_key_count":len(records),"workunit_count":count,
                              "survivor_static_key_stream_sha256":stream_sha(records)})
    return out, slice_summary

def validate_receipt(worker, rt, receipt, expected):
    req(receipt.get("schema") == worker.SCHEMA, "wrong receipt schema")
    ident = receipt.get("workunit_identity"); req(isinstance(ident, dict), "missing identity")
    wid = ident.get("workunit_id"); req(wid in expected, "receipt workunit not in expected plan")
    req(ident == expected[wid], "receipt identity mismatch")
    locks = receipt.get("source_locks", {})
    req(locks.get("worker_blob_sha1") == WORKER_BLOB, "worker source lock mismatch")
    req(locks.get("workunit_preflight_blob_sha1") == worker.WORKUNIT_BLOB, "workunit preflight lock mismatch")
    req(locks.get("workunit_plan_certificate_producer_blob_sha1") == PLAN_BLOB, "plan producer lock mismatch")
    req(locks.get("selective_weighted_survivor_blob_sha1") == rt["wu"].SELECTIVE_BLOB,
        "selective producer lock mismatch")
    sem = receipt.get("execution_semantics", {})
    req(int(sem.get("unknown_count", -1)) == 0, "UNKNOWN count nonzero")
    req(int(sem.get("completed_key_count", -1)) == ident["static_key_count"], "completed key count mismatch")
    req(sem.get("atomic_receipt_written_only_after_complete_unit") is True, "atomic-completion flag missing")
    result = receipt.get("result", {})
    rows = result.get("key_evidence_rows"); req(isinstance(rows, list), "missing evidence rows")
    req(len(rows) == ident["static_key_count"], "evidence row count mismatch")
    req(stream_sha(rows) == result.get("key_evidence_stream_sha256"), "evidence stream digest mismatch")
    env = exact = 0
    for row in rows:
        e = int(row["depth2_envelope_weighted_mass"]); x = int(row["exact_picard_weighted_mass"])
        req(x <= e, "row exact mass exceeds envelope")
        if row.get("exact_picard_threshold") is None:
            req(x == 0, "no-Picard row has positive exact mass")
        else:
            req(int(row["exact_picard_threshold"]) <= int(row["depth2_envelope_threshold"]),
                "row exact threshold exceeds envelope")
        env += e; exact += x
    req(str(env) == str(result.get("depth2_envelope_weighted_mass")), "aggregate envelope mass mismatch")
    req(str(exact) == str(result.get("exact_picard_weighted_mass")), "aggregate exact mass mismatch")
    req(str(env-exact) == str(result.get("exact_picard_tightening")), "aggregate tightening mismatch")
    canon = receipt.get("canonical_sha256_without_this_field"); req(isinstance(canon, str), "missing canonical digest")
    body = dict(receipt); body.pop("canonical_sha256_without_this_field", None)
    req(csha(body) == canon, "receipt canonical digest mismatch")
    fw = receipt.get("firewalls", {})
    req(fw.get("main_credit_changed") is False and fw.get("full178_census_claimed") is False,
        "receipt credit firewall violated")
    return wid, exact, env, canon

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--receipts-dir", type=Path, required=True)
    p.add_argument("--snapshot", type=Path)
    a = p.parse_args()

    if not (WORKER.is_file() and git_blob(WORKER) == WORKER_BLOB):
        raise SystemExit("FAIL: worker source drift")
    if not (PLAN.is_file() and git_blob(PLAN) == PLAN_BLOB):
        raise SystemExit("FAIL: plan producer drift")
    worker = load_module(WORKER, "s32_178_resume_worker")
    rt = worker.load_runtime()
    expected, slices = expected_units(worker, rt)

    complete, rejected = {}, []
    aggregate_exact = aggregate_env = 0
    for path in sorted(a.receipts_dir.glob("*.json")):
        try:
            receipt = json.loads(path.read_text())
            wid, exact, env, digest = validate_receipt(worker, rt, receipt, expected)
            if wid in complete:
                raise ValueError("duplicate completed workunit")
            complete[wid] = {"path":path.name,"receipt_sha256":digest}
            aggregate_exact += exact; aggregate_env += env
        except Exception as exc:
            rejected.append({"path":path.name,"reason":str(exc)})

    missing = sorted(set(expected) - set(complete))
    complete_ids = sorted(complete)
    snapshot = {
      "schema":SCHEMA,
      "role":"RECOVERY_AND_RESUME_SNAPSHOT__PARTIAL_RESULTS_NOT_MAIN_CREDIT",
      "source_locks":{"worker_blob_sha1":WORKER_BLOB,"plan_certificate_producer_blob_sha1":PLAN_BLOB},
      "expected_plan":{"selected_x4_slices":list(worker.SELECTED_X4),"workunit_size_ceiling":worker.WORKUNIT_SIZE,
                       "workunit_count":len(expected),"workunit_identity_stream_sha256":stream_sha([expected[k] for k in sorted(expected)]),
                       "slice_summaries":slices},
      "recovery_state":{"complete_workunit_count":len(complete_ids),"missing_workunit_count":len(missing),
                        "rejected_receipt_count":len(rejected),"complete_workunit_ids":complete_ids,
                        "missing_workunit_ids":missing,"rejected_receipts":rejected,
                        "resume_rule":"schedule only missing workunit ids; never reuse rejected receipts",
                        "completed_unit_reexecution_required":False},
      "partial_aggregate":{"depth2_envelope_weighted_mass_of_complete_units":str(aggregate_env),
                           "exact_picard_weighted_mass_of_complete_units":str(aggregate_exact),
                           "creditable_as_full_selected_slice_result":len(missing)==0 and len(rejected)==0},
      "firewalls":{"selected_slice_only":True,"full_row_census_claimed":False,"full178_census_claimed":False,
                   "main_credit_changed":False,"theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False}}
    snapshot["canonical_sha256_without_this_field"] = csha(snapshot)
    if a.snapshot:
        a.snapshot.parent.mkdir(parents=True, exist_ok=True)
        a.snapshot.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n")
    print("SELECTIVE_PICARD_RECOVERY_SUMMARY=" + json.dumps({
        "expected":len(expected),"complete":len(complete_ids),"missing":len(missing),"rejected":len(rejected),
        "snapshot_sha256":snapshot["canonical_sha256_without_this_field"]}, sort_keys=True))
    print(json.dumps(snapshot, indent=2, sort_keys=True))
    if rejected: raise SystemExit(2)

if __name__ == "__main__": main()
