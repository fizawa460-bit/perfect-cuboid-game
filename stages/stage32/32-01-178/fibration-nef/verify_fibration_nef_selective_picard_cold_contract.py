#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "SELECTIVE-PICARD-RESUME-CONTRACT.json"
CONTRACT_BLOB = "9faa2792f0e507ebeb6ce9af3597a43e31236d16"
RUNKEY = HERE / "SELECTIVE-PICARD-RUNKEY.json"
RUNKEY_BLOB = "c73b15a9ac5be6af15890b9d3db89c3de6f39f28"
WORKER = HERE / "run_fibration_nef_selective_picard_workunit.py"
WORKER_BLOB = "3bbc4ba84f7ba5bf7188929d56c4a273ca0532f5"
RESUME = HERE / "verify_fibration_nef_selective_picard_resume.py"
RESUME_BLOB = "f6fe66583bf81a68563bbbf7f7b8c22531db98ba"\nSELECTOR = HERE / "verify_fibration_nef_selective_picard_pilot_selector.py"\nSELECTOR_BLOB = "e29abd7c8d653fa1cc2809fca99307f9beeda372"

def req(v, m):
    if not v: raise SystemExit("FAIL: " + m)

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def csha(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec); sys.modules[name] = mod; spec.loader.exec_module(mod)
    return mod

def main():
    for path, expected, label in (
        (CONTRACT, CONTRACT_BLOB, "contract"), (RUNKEY, RUNKEY_BLOB, "cold runkey"),
        (WORKER, WORKER_BLOB, "worker"), (RESUME, RESUME_BLOB, "resume verifier"),\n        (SELECTOR, SELECTOR_BLOB, "pilot selector")):
        req(path.is_file(), f"missing {label}")
        req(git_blob(path) == expected, f"{label} source drift")

    contract = json.loads(CONTRACT.read_text())
    canon = contract.pop("canonical_sha256_without_this_field", None)
    req(canon == csha(contract), "contract canonical digest mismatch")
    contract["canonical_sha256_without_this_field"] = canon
    runkey = json.loads(RUNKEY.read_text())

    worker = load_module(WORKER, "s32_178_cold_contract_worker")
    resume = load_module(RESUME, "s32_178_cold_contract_resume")
    req(worker.RUNKEY.resolve() == RUNKEY.resolve(), "worker runkey path drift")
    req(worker.RUNKEY_SCHEMA == runkey["schema"], "worker/runkey schema drift")
    req(tuple(contract["target"]["selected_x4_slices"]) == tuple(worker.SELECTED_X4), "selected x4 drift")
    req(int(contract["partition"]["workunit_size_ceiling"]) == int(worker.WORKUNIT_SIZE), "workunit size drift")
    req(resume.WORKER_BLOB == WORKER_BLOB, "resume verifier worker lock drift")
    req(resume.PLAN_BLOB == worker.PLAN_BLOB, "resume verifier plan lock drift")

    locks = contract["source_locks"]
    req(locks["worker_blob_sha1"] == WORKER_BLOB, "contract worker lock mismatch")
    req(locks["resume_verifier_blob_sha1"] == RESUME_BLOB, "contract resume lock mismatch")
    req(locks["workunit_preflight_blob_sha1"] == worker.WORKUNIT_BLOB, "contract workunit lock mismatch")
    req(locks["plan_certificate_producer_blob_sha1"] == worker.PLAN_BLOB, "contract plan lock mismatch")\n    req(locks["pilot_selector_blob_sha1"] == SELECTOR_BLOB, "contract pilot selector lock mismatch")\n    req(contract["authorization"].get("pilot_selector") == SELECTOR.name, "contract pilot selector path mismatch")

    auth = contract["authorization"]
    req(auth["current_generation"] == 0 and auth["current_armed"] is False, "contract is not cold")
    req(runkey["generation"] == 0 and runkey["armed"] is False, "runkey is not cold")\n    req(runkey.get("mode") == "COLD", "runkey mode is not COLD")\n    req(auth.get("current_mode") == "COLD", "contract mode is not COLD")
    req(runkey["authorized_workunit_ids"] == [], "cold runkey authorizes work")
    req(runkey["planned_effective_heavy_concurrency"] == 0, "cold runkey has heavy concurrency")
    req(runkey["representative_receipt_bytes"] == 0, "cold runkey claims measured receipt")
    req(runkey["projected_peak_storage_bytes"] == 0, "cold runkey claims projected storage")
    req(runkey["firewalls"]["heavy_execution_authorized"] is False, "cold runkey authorizes heavy execution")
    req(contract["storage_and_concurrency"]["planned_effective_heavy_concurrency"] is None,
        "cold contract preselects heavy concurrency")
    req(contract["storage_and_concurrency"]["representative_receipt_bytes"] is None,
        "cold contract claims representative measurement")
    req(contract["workflow_lifecycle"]["workflow_retained_now"] is False, "contract claims retained workflow")
    req(contract["firewalls"]["heavy_execution_authorized"] is False, "contract authorizes heavy execution")

    out = {
      "schema":"STAGE32_32_01_178_SELECTIVE_PICARD_COLD_CONTRACT_CHECK_V1",
      "contract_blob_sha1":CONTRACT_BLOB,
      "contract_canonical_sha256":canon,
      "runkey_blob_sha1":RUNKEY_BLOB,
      "worker_blob_sha1":WORKER_BLOB,
      "resume_verifier_blob_sha1":RESUME_BLOB,\n      "pilot_selector_blob_sha1":SELECTOR_BLOB,
      "selected_x4_slices":list(worker.SELECTED_X4),
      "workunit_size_ceiling":worker.WORKUNIT_SIZE,
      "cold_runkey_generation":0,\n      "cold_runkey_mode":"COLD",\n      "measurement_pilot_defined":True,\n      "production_wave_requires_prior_measurement":True,
      "heavy_execution_authorized":False,
      "workflow_retained":False,
      "ready_for_future_measure_then_arm":True,
      "main_credit_changed":False,
      "theorem_credit_changed":False,
      "endpoint_credit_changed":False,
      "merge":False
    }
    print("SELECTIVE_PICARD_COLD_CONTRACT_SUMMARY=" + json.dumps(out, sort_keys=True))
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__": main()
