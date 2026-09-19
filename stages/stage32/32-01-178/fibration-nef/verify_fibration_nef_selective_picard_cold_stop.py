#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STOP = HERE / "SELECTIVE-PICARD-COLD-STOP.json"
STOP_BLOB = "5b92371e5f147b96ade73ff9e5ea0d0a9f90f98e"
STOP_CANON = "0cc8f4733e909a2b0c44aa3edc1f83ec07d8b7cedbc30b5e8fea4e484a1c40d2"

LOCKS = {
    "resume_contract": (HERE / "SELECTIVE-PICARD-RESUME-CONTRACT.json", "59454ea4b3f3766145753705f62cfeec25b1cba9"),
    "runkey": (HERE / "SELECTIVE-PICARD-RUNKEY.json", "c73b15a9ac5be6af15890b9d3db89c3de6f39f28"),
    "worker": (HERE / "run_fibration_nef_selective_picard_workunit.py", "3bbc4ba84f7ba5bf7188929d56c4a273ca0532f5"),
    "resume_verifier": (HERE / "verify_fibration_nef_selective_picard_resume.py", "bf17305df21a1da966decf4e5689df0789757cc6"),
    "pilot_selector": (HERE / "verify_fibration_nef_selective_picard_pilot_selector.py", "5bfea1e78161ea7810d777d253607c48baf1852b"),
    "cold_contract_verifier": (HERE / "verify_fibration_nef_selective_picard_cold_contract.py", "d927edff870f2ebe50832d08c1dea94675592335"),
}

def req(v, m):
    if not v:
        raise SystemExit("FAIL: " + m)

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj):
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def main():
    req(STOP.is_file(), "missing cold-stop checkpoint")
    req(git_blob(STOP) == STOP_BLOB, "cold-stop checkpoint blob drift")
    stop = json.loads(STOP.read_text())
    req(stop.get("canonical_sha256_without_this_field") == STOP_CANON, "stored cold-stop canonical drift")
    req(canon(stop) == STOP_CANON, "cold-stop canonical drift")

    for label, (path, expected) in LOCKS.items():
        req(path.is_file(), "missing " + label)
        req(git_blob(path) == expected, label + " blob drift")

    contract = json.loads(LOCKS["resume_contract"][0].read_text())
    req(contract["canonical_sha256_without_this_field"] ==
        stop["locked_execution_contract"]["resume_contract_canonical_sha256"],
        "resume contract canonical identity drift")
    req(contract["status"] == "COLD_NOT_ARMED__RESUME_ARCHITECTURE_READY",
        "resume contract status drift")
    req(contract["firewalls"]["heavy_execution_authorized"] is False,
        "resume contract unexpectedly authorizes heavy execution")

    runkey = json.loads(LOCKS["runkey"][0].read_text())
    req(runkey["generation"] == 0, "cold runkey generation drift")
    req(runkey["mode"] == "COLD", "cold runkey mode drift")
    req(runkey["armed"] is False, "cold runkey unexpectedly armed")
    req(runkey["authorized_workunit_ids"] == [], "cold runkey authorizes units")
    req(runkey["planned_effective_heavy_concurrency"] == 0,
        "cold runkey has nonzero heavy concurrency")
    req(runkey["firewalls"]["heavy_execution_authorized"] is False,
        "cold runkey heavy firewall drift")

    req(stop["status"] == "BLOCKED_EXECUTION_AUTHORIZATION_REQUIRED",
        "cold-stop status drift")
    req(stop["blocker"]["heavy_or_artifact_execution_currently_authorized"] is False,
        "cold-stop authorization drift")
    req(stop["blocker"]["additional_representation_rewrite_required"] is False,
        "cold-stop representation boundary drift")
    req(stop["observed_live_main"]["authority_version"] == "V43",
        "observed MAIN authority version drift in checkpoint")
    req(stop["observed_live_main"]["full178_complete"] is False,
        "FULL178 completion overclaim")
    req(stop["fixed_main_btva_source_boundary"]["lane178_source_head"] ==
        "e60f03cf5105bc6e26cb4615acabd6fe0c07625c",
        "fixed MAIN BTVA lane178 source drift")

    reopen_ids = [r["id"] for r in stop["reopen_conditions"]]
    req(reopen_ids == [
        "PILOT_MEASURE_AUTHORIZED",
        "MAIN_REASSIGNS_178",
        "NEW_NONHEAVY_MATHEMATICAL_WEAPON",
    ], "reopen-condition order/content drift")

    fw = stop["firewalls"]
    for key in ("full_row_census_claimed", "full178_census_claimed",
                "main_credit_changed", "theorem_credit_changed",
                "endpoint_credit_changed", "stage32_closed",
                "perfect_cuboid_claim", "merge"):
        req(fw[key] is False, "cold-stop firewall " + key)

    print("PASS: selective Picard non-heavy boundary is frozen at cold execution blocker")
    print("PASS: runkey generation=0 mode=COLD armed=false; no heavy/artifact execution authorized")
    print("PASS: resume/worker/selector/cold-contract source locks match")
    print("PASS: MAIN V43 BTVA source remains fixed at historical lane178 head e60f03cf...")
    print("PASS: next numerical step requires explicit PILOT_MEASURE authorization; zero MAIN/theorem/endpoint credit")

if __name__ == "__main__":
    main()
