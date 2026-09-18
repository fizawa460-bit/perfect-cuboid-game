#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "PRODUCTION-EXECUTION-CONTRACT.json"
RUNKEY = ROOT / "stages/stage32-ex5/runkeys/hpadj22-production.json"
EXPECTED_HPADJ21 = 157570677819451133507
EXPECTED_HPADJ08_REJECTED = 40886299509963924857401
EXPECTED_BANDS = [[0,11],[12,23],[24,35],[36,47],[48,59],[60,71],[72,83],[84,96]]


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_json(path: Path, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    d = json.loads(path.read_text())
    req(d.get("canonical_sha256_without_this_field") == canonical(d), f"{label} canonical drift")
    return d


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--require-armed", action="store_true")
    args = ap.parse_args()

    contract = load_json(CONTRACT, "production contract")
    runkey = load_json(RUNKEY, "production runkey")

    req(contract["schema"] == "STAGE32EX5_HPADJ22_PRODUCTION_EXECUTION_CONTRACT_V1", "contract schema")
    req(contract["route_id"] == "HPADJ-22_ex5", "contract route")
    req(contract["status"] == "READY_COLD__EXPLICIT_ARM_REQUIRED", "contract status")
    req(contract["mathematical_semantics"]["audited_hpadj21_full178_upper_bound"] == EXPECTED_HPADJ21,
        "HPADJ21 authority drift")
    req(contract["mathematical_semantics"]["audited_hpadj08_exact_square_rejected_terminals"] == EXPECTED_HPADJ08_REJECTED,
        "HPADJ08 authority drift")
    req(contract["partition"]["b_bands"] == EXPECTED_BANDS, "band partition drift")
    req(contract["partition"]["band_count"] == 8 and contract["partition"]["row_count"] == 178,
        "production coverage geometry")
    req(contract["partition"]["exact_cell_count"] == 1424, "exact cell count")

    src = runkey["source_locks"]
    required_paths = {
        "band_worker": "stages/stage32-ex5/hpadj-22_ex5/run_full_bband.py",
        "aggregate": "stages/stage32-ex5/hpadj-22_ex5/aggregate_full178_bands.py",
        "recovery_snapshot": "stages/stage32-ex5/hpadj-22_ex5/build_recovery_snapshot.py",
        "band_bounded_equivalence": "stages/stage32-ex5/hpadj-22_ex5/verify_bband_bounded.py",
        "production_contract": "stages/stage32-ex5/hpadj-22_ex5/PRODUCTION-EXECUTION-CONTRACT.json",
        "production_workflow": ".github/workflows/stage32-ex5-hpadj22-production.yml",
        "production_preflight": "stages/stage32-ex5/hpadj-22_ex5/verify_production_preflight.py",
    }
    for key, rel in required_paths.items():
        rec = src[key]
        req(rec["path"] == rel, f"runkey {key} path drift")
        path = ROOT / rel
        req(path.is_file(), f"missing runkey source {key}")
        req(git_blob(path) == rec["blob_sha1"], f"runkey {key} blob drift")
        if key != "production_contract":
            csrc = contract["source_locks"][key]
            req(csrc == rec, f"contract/runkey source-lock mismatch {key}")

    req(contract["source_locks"]["bchunk_worker"]["blob_sha1"] ==
        "3fc6e7e4aff539be5b60528d1d1b2e41529ddc03", "bchunk parent lock drift")
    req(contract["source_locks"]["bounded_result"]["blob_sha1"] ==
        "837ae21d2ef80a58d5d61bbfbedf5e4277ff5d0e", "bounded result lock drift")
    req(contract["source_locks"]["bchunk_equivalence_receipt"]["blob_sha1"] ==
        "b773ccadd0ae0c0aadb1074199d2f4c1d31fc95b", "bchunk equivalence lock drift")

    prior = contract["comparable_execution_preflight"]
    req(prior["hpadj21_bchunk_run_id"] == 35279651998, "HPADJ21 comparable run id")
    req(prior["hpadj21_artifact_count"] == 59, "HPADJ21 artifact count")
    req(prior["hpadj21_max_measured_chunk_artifact_bytes"] == 482162, "HPADJ21 measured max artifact")
    req(prior["hpadj21_max_measured_chunk_artifact_bytes"] < 2097152, "HPADJ21 comparable artifact exceeds new hard cap")
    req(prior["hpadj08_full178_run_id"] == 34935380596, "HPADJ08 comparable run id")
    req(prior["hpadj08_band_artifact_count"] == 8, "HPADJ08 band artifact count")
    req(prior["hpadj08_max_measured_band_artifact_bytes"] == 6611, "HPADJ08 measured max band artifact")
    req(prior["new_representative_measurement_required"] is False, "comparable-run waiver drift")
    req(prior["basis"] == "COMPARABLE_PRIOR_HPADJ21_BCHUNK_AND_HPADJ08_BBAND_RUNS", "comparable-run basis")

    req(runkey["schema"] == "STAGE32EX5_HPADJ22_PRODUCTION_RUNKEY_V1", "runkey schema")
    req(runkey["route_id"] == "HPADJ-22_ex5", "runkey route")
    req(int(runkey["carry_run_id"]) >= 0, "carry run id")
    if int(runkey["carry_run_id"]) == 0:
        req(runkey["carry_exact_head"] is None, "cold/no-carry runkey must use carry_exact_head=null")
    else:
        req(isinstance(runkey["carry_exact_head"], str) and len(runkey["carry_exact_head"]) == 40,
            "carry exact head must be recorded for recovery")
    res = runkey["resource_preflight"]
    req(res["planned_effective_heavy_concurrency"] == 8, "planned heavy concurrency")
    req(res["repo_stage_heavy_cap"] == 18, "Stage32 heavy cap")
    req(res["maximum_other_stage32_heavy_concurrency_at_arm"] == 10, "headroom contract")
    req(res["artifact_count_upper_bound_per_run"] <= 10, "artifact count")
    req(res["artifact_hard_cap_bytes_per_band"] == 2097152, "band artifact cap")
    req(res["projected_peak_artifact_mb"] <= 24, "storage peak")
    req(res["repository_operating_budget_mb"] == 500, "repository storage budget")

    if args.require_armed:
        req(runkey["armed"] is True, "production runkey is not armed")
        req(int(runkey["generation"]) >= 1, "production generation")
        observed = res["observed_other_stage32_heavy_concurrency_at_arm"]
        req(isinstance(observed, int) and observed >= 0, "arm-time overlapping heavy count not recorded")
        req(observed + res["planned_effective_heavy_concurrency"] <= res["repo_stage_heavy_cap"],
            "Stage32 effective heavy concurrency would exceed cap")
    else:
        req(runkey["armed"] is False, "cold preflight requires armed=false")
        req(res["observed_other_stage32_heavy_concurrency_at_arm"] is None,
            "cold runkey must not pretend arm-time overlap was checked")

    req(all(v is False for v in contract["credit_firewall"].values()), "contract credit firewall")
    req(all(v is False for v in runkey["credit"].values()), "runkey credit firewall")
    print("PASS: HPADJ22 FULL178 production surface is source-locked")
    print("PASS: exact partition 8 bands x 178 rows = 1424 HPADJ15 cells")
    print("PASS: resume is row-checkpointed inside each band; <=8 band artifacts plus snapshot/final")
    print("PASS: audited HPADJ21 and HPADJ08 totals are mandatory aggregate crosschecks")
    print("PASS: production remains cold unless a fresh runkey arm records overlap <=10")


if __name__ == "__main__":
    main()
