#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
CHECKPOINT = HERE / "bc2-17-n354-survivor-picard64-solver-wall-checkpoint.json"
RUNKEY = HERE.parent / "runkeys" / "bc2-17-n354-authority-picard64-retarget-v2.json"

EVIDENCE_CANONICAL = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
CHECKPOINT_CANONICAL = "2119ffb4ff888c0f2f55ec1ea287df38f486a2608cec4d1cda90fe5a67f748ef"
N354_AUDIT_CANONICAL = "e329916a74eea4471e00f109964afdaa871d4f8614237efed7f0f6e5d9b9c808"
N354_RESULT_CANONICAL = "9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4"
BC2_16_CLAIM_SYNC = "ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd"


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_without(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def verify_canonical(path: Path, expected: str, label: str) -> dict:
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == expected, f"{label} canonical field drift")
    req(canonical_without(obj) == expected, f"{label} canonical replay drift")
    return obj


def main() -> None:
    e = verify_canonical(EVIDENCE, EVIDENCE_CANONICAL, "BC2-17 evidence")
    c = verify_canonical(CHECKPOINT, CHECKPOINT_CANONICAL, "BC2-17 checkpoint")
    r = load(RUNKEY)

    req(e["schema"] == "STAGE32EX5_BC2_17_N354_AUTHORITY_PICARD64_RETARGET_V2", "evidence schema drift")
    a = e["main_authority"]
    req(a["n354_hostile_audit_review_id"] == 5164850548, "N354 audit review drift")
    req(a["n354_audited_exact_head"] == "e82a1d2ae6ed3693e5e5e81adfd95b83a6c317b6", "N354 audited head drift")
    req(a["n354_audit_receipt_canonical_sha256"] == N354_AUDIT_CANONICAL, "N354 audit canonical drift")
    req(a["n354_result_canonical_sha256"] == N354_RESULT_CANONICAL, "N354 result canonical drift")
    req(a["n354_survivor_strata"] == 17128 and a["survivor_strata_replayed_from_manifest"] == 17128, "N354 survivor replay drift")
    req(a["n354_survivor_terminals"] == 38560956534397137634780102, "N354 survivor terminal count drift")

    t = e["retarget"]
    req(t["prior_e4_target"] == {"d": 8, "e": 4, "g": 1, "survives_n354": False}, "old e4 target status drift")
    req(t["selected_target"] == {"d": 8, "e": 8, "g": 1, "row_id": "g1-d008", "survives_n354": True}, "e8 retarget drift")
    req(t["first_block"] == [0,112] and t["first_block_width"] == 113, "e8 first-block drift")
    req(t["base_terminal"] == [0,1,0,0,0,0,0,0,0,0,1], "e8 base terminal drift")
    req(t["fixed_exceptional_mass"] == 2 and t["residual_exceptional_mass"] == 6, "e8 mass split drift")
    req(t["rank_unrank_replay_count"] == 113, "e8 replay count drift")
    req(t["replay_stream_sha256"] == "c7ba2038f06494cdcd02c9906ddcdecb938ff82c29eb1af3fce60a5ff79f409c", "e8 replay hash drift")

    q = e["picard64_probe"]
    req(q["result"] == "UNKNOWN" and q["reason_unknown"] == "timeout", "solver wall result drift")
    req(q["timeout_ms"] == 60000 and q["z3_version"] == "4.15.4", "solver provenance drift")
    req(q["whole_first_block_picard64_unsat"] is False and q["sat_witness"] is None, "UNKNOWN promoted to mathematical result")
    req(q["remaining_exceptional_distribution_free_subject_to_integral_picard64_constraints"] is True, "probe scope narrowed")

    req(c["probe"]["evidence_canonical_sha256"] == EVIDENCE_CANONICAL, "checkpoint evidence lock drift")
    req(c["probe"]["result"] == "UNKNOWN" and c["probe"]["reason_unknown"] == "timeout", "checkpoint solver wall drift")
    req(c["workflow"]["run_id"] == 34458170090, "workflow run provenance drift")
    req(c["workflow"]["authorize_job_id"] == 102809392982 and c["workflow"]["compute_job_id"] == 102809456734, "workflow job provenance drift")
    req(c["workflow"]["artifact_id"] == 10144438884, "artifact id drift")
    req(c["workflow"]["artifact_zip_bytes"] == 4062, "artifact byte drift")
    req(c["workflow"]["artifact_zip_sha256"] == "2691a963a1b552126be4283a976785ece4efc06a0c82c6eb76b7155db2d81544", "artifact digest drift")
    req(c["discarded_attempt"]["solver_invoked"] is False and c["discarded_attempt"]["mathematical_credit"] is False, "invalid v1 attempt gained credit")
    req(c["claim_sync"]["claim_dag_sync_triggered_by_bc2_17"] is False, "solver wall falsely claim-synchronized")
    req(c["claim_sync"]["existing_active_claim"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "active claim drift")
    req(c["claim_sync"]["bc2_16_last_claim_sync_receipt_canonical"] == BC2_16_CLAIM_SYNC, "prior claim-sync provenance drift")
    req(c["next_exact_unit"]["id"] == "BC2_18_DECOMPOSE_N354_SURVIVOR_PICARD64_PROBE", "BC2-18 route drift")

    req(r["schema"] == "STAGE32EX5_BC2_17_N354_AUTHORITY_PICARD64_RETARGET_V2_RUNKEY_V1", "run-key schema drift")
    req(r["generation"] == 1 and r["armed"] is True, "run-key generation/arm drift")
    req(r["source_commit"] == "73148a652e5eeac075c2cd81c9323c247653368f", "run-key source commit drift")
    req(r["target"] == {"row_id":"g1-d008","g":1,"d":8,"e":8}, "run-key target drift")
    req(r["symbolic_x4_rank_block"] == [0,112], "run-key block drift")
    req(r["effective_heavy_concurrency"] == 1 and r["artifact_retention_days"] == 1, "heavy safety drift")

    for key, val in c["firewalls"].items():
        req(val is False, f"firewall violated: {key}")
    for key, val in e["firewalls"].items():
        req(val is False, f"evidence firewall violated: {key}")

    print("PASS: BC2-17 N354-survivor Picard64 solver wall retained exactly")
    print("target=g1-d008/e8 first_block=0..112 width=113")
    print("fixed_residual_exceptional_mass=2/6")
    print("solver=UNKNOWN reason=timeout 60s")
    print("next=BC2_18_DECOMPOSE_N354_SURVIVOR_PICARD64_PROBE")
    print("main_credit=NO")


if __name__ == "__main__":
    main()
