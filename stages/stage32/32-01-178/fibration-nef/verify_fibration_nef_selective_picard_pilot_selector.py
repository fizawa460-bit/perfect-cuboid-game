#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_fibration_nef_selective_picard_workunit.py"
WORKER_BLOB = "3bbc4ba84f7ba5bf7188929d56c4a273ca0532f5"
RESUME = HERE / "verify_fibration_nef_selective_picard_resume.py"
RESUME_BLOB = "bf17305df21a1da966decf4e5689df0789757cc6"

def req(v, m):
    if not v: raise SystemExit("FAIL: " + m)

def git_blob(path):
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def load_module(path, name):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod)
    return mod

def main():
    req(WORKER.is_file() and git_blob(WORKER)==WORKER_BLOB, "worker drift")
    req(RESUME.is_file() and git_blob(RESUME)==RESUME_BLOB, "resume verifier drift")
    worker=load_module(WORKER,"s32_178_pilot_worker")
    resume=load_module(RESUME,"s32_178_pilot_resume")
    rt=worker.load_runtime()
    expected,slices=resume.expected_units(worker,rt)
    req(expected, "empty expected workunit plan")
    maximum=max(int(v["static_key_count"]) for v in expected.values())
    candidates=sorted(k for k,v in expected.items() if int(v["static_key_count"])==maximum)
    chosen=candidates[0]
    ident=expected[chosen]
    proposal={
      "schema":"STAGE32_32_01_178_SELECTIVE_PICARD_PILOT_SELECTOR_V1",
      "purpose":"select one deterministic full-size workunit for compact-receipt size measurement; this selector does not arm or execute heavy compute",
      "selection_rule":{
        "primary":"maximum static_key_count",
        "tie_break":"lexicographically smallest workunit_id",
        "runtime_worst_case_claimed":False,
        "receipt_size_representative_claim_only":True
      },
      "expected_plan":{
        "workunit_count":len(expected),
        "selected_x4_slices":list(worker.SELECTED_X4),
        "slice_summaries":slices
      },
      "chosen_workunit":ident,
      "future_runkey_proposal":{
        "generation":1,
        "mode":"PILOT_MEASURE",
        "armed":False,
        "authorized_workunit_ids":[chosen],
        "planned_effective_heavy_concurrency":1,
        "representative_receipt_bytes":0,
        "projected_peak_storage_bytes":8*1024*1024,
        "requires_fresh_commit_range_arm":True
      },
      "firewalls":{
        "heavy_execution_authorized":False,
        "artifact_production_authorized":False,
        "full_row_census_claimed":False,
        "full178_census_claimed":False,
        "main_credit_changed":False,
        "theorem_credit_changed":False,
        "endpoint_credit_changed":False,
        "merge":False
      }
    }
    print("SELECTIVE_PICARD_PILOT_SELECTOR_SUMMARY="+json.dumps({
      "expected_workunits":len(expected),"max_static_key_count":maximum,
      "candidate_count":len(candidates),"chosen_workunit_id":chosen},sort_keys=True))
    print(json.dumps(proposal,indent=2,sort_keys=True))

if __name__=="__main__": main()
