#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCH = HERE / "archive" / "startup-surface-20260914"
ARCH_VERIFIER = ARCH / "verify_main_state_v5_pre_startup_collapse.py"
ARCH_STATE = ARCH / "MAIN-STATE-v5-post-1765.json"
TMP_VERIFIER = HERE / ".verify_main_state_v5_pre_startup_collapse.py"
MAIN_STATE = HERE / "MAIN-STATE.json"
HPADJ20_HANDOFF = HERE / "hpadj-20_ex5" / "MAIN-HANDOFF.json"
HPADJ20_HANDOFF_VERIFIER = HERE / "hpadj-20_ex5" / "verify_main_handoff.py"
HPADJ23_PREFLIGHT = HERE / "hpadj-23_ex5" / "HPADJ23-EXACT-T-HOLE-PREFLIGHT.json"
HPADJ23_VERIFIER = HERE / "hpadj-23_ex5" / "verify_hpadj23_exact_t_hole_preflight.py"
HPADJ23_BUILDER = HERE / "hpadj-23_ex5" / "build_exact_t_joint_histogram.py"
HPADJ23_BUILDER_RESULT = HERE / "hpadj-23_ex5" / "HPADJ23-EXACT-T-BUILDER-BOUNDED-RESULT.json"
HPADJ23_SERIALIZER = HERE / "hpadj-23_ex5" / "serialize_exact_t_histogram.py"
HPADJ23_SERIALIZATION_RESULT = HERE / "hpadj-23_ex5" / "HPADJ23-COMPACT-SERIALIZATION-BOUNDED-RESULT.json"
HPADJ23_HANDOFF = HERE / "hpadj-23_ex5" / "HPADJ23-BOUNDED-PRODUCER-HANDOFF.json"
HPADJ23_HANDOFF_VERIFIER = HERE / "hpadj-23_ex5" / "verify_hpadj23_bounded_producer_handoff.py"
HPADJ23_SHARD_BUILDER = HERE / "hpadj-23_ex5" / "build_exact_t_joint_histogram_shard.py"
HPADJ23_SHARD_EQ = HERE / "hpadj-23_ex5" / "HPADJ23-SHARD-BOUNDED-EQUIVALENCE.json"
HPADJ23_SHARD_EQ_VERIFIER = HERE / "hpadj-23_ex5" / "verify_hpadj23_shard_bounded_equivalence.py"
HPADJ23_SCALEOUT_PREFLIGHT = HERE / "hpadj-23_ex5" / "HPADJ23-FULL178-SCALEOUT-PREFLIGHT.json"
HPADJ23_SCALEOUT_RUNKEY = HERE / "runkeys" / "hpadj23-scaleout-measurement.json"
HPADJ23_SCALEOUT_VERIFIER = HERE / "hpadj-23_ex5" / "verify_hpadj23_scaleout_preflight.py"
HPADJ23_MEASUREMENT_RUNNER = HERE / "hpadj-23_ex5" / "measure_scaleout_shard.py"
HPADJ23_MEASUREMENT_CONTRACT = HERE / "hpadj-23_ex5" / "HPADJ23-MEASUREMENT-EXECUTION-CONTRACT.json"
HPADJ23_MEASUREMENT_AUTH = HERE / "hpadj-23_ex5" / "verify_hpadj23_measurement_authorization.py"
HPADJ23_MEASUREMENT_WORKFLOW = HERE.parents[1] / ".github" / "workflows" / "stage32-ex5-hpadj23-measurement.yml"

ARCH_VERIFIER_BLOB = "fa20238eb372100520a2ca76523ca63d3b3f9c5f"
ARCH_STATE_BLOB = "a26f19cb01d86174aef49495be16e946a429ddcb"
HPADJ20_HANDOFF_BLOB = "52ca73eeb52b7d930f905c42a85b62f044bda269"
HPADJ20_HANDOFF_VERIFIER_BLOB = "404a7d2c362ca15db4bd655eb6022ebbade219d1"
HPADJ23_PREFLIGHT_BLOB = "eb6ec8e7ea2e1bc87ef3222603f0f9c026cfb78e"
HPADJ23_VERIFIER_BLOB = "60f9585ef049daeb49f0b918f4e90e962713abed"
HPADJ23_BUILDER_BLOB = "c02973cb9d7fdea7584661a9c5935a43e12efe92"
HPADJ23_BUILDER_RESULT_BLOB = "7e919c28f3c259cc1db2743c8deb7c82a5c11612"
HPADJ23_SERIALIZER_BLOB = "91be480f62de7c8cac63c4ddc37a372cc3fed33d"
HPADJ23_SERIALIZATION_RESULT_BLOB = "30eb5b36f357c0474454189c8ff52549d943f277"
HPADJ23_HANDOFF_BLOB = "f2c1d998cd1d2cf032bf1e56c94e710dbc80eddb"
HPADJ23_HANDOFF_VERIFIER_BLOB = "f764a06716e90e0b4788e756cb1dd7a03e7b968f"
HPADJ23_SHARD_BUILDER_BLOB = "25284ea56c0746912318ce3c0d0e75d50cf60458"
HPADJ23_SHARD_EQ_BLOB = "b1a0248926c176a31a57da0fbb97807c3bb0eeba"
HPADJ23_SHARD_EQ_VERIFIER_BLOB = "6aea0f8c39ea0865fb3926aec55ba25582a31697"
HPADJ23_SCALEOUT_PREFLIGHT_BLOB = "0b71f07f3bfbb0497ddb0be9a0b5ad28681780b6"
HPADJ23_SCALEOUT_VERIFIER_BLOB = "663f7f12edf4eed15336f3e5fc26f9d48c3f8bd0"
HPADJ23_MEASUREMENT_RUNNER_BLOB = "2fe44f3ccc97ef051cfdbbd42124ecad3a45b623"
HPADJ23_MEASUREMENT_CONTRACT_BLOB = "b7472b77268f9ab628c4d486d0687490340f0f97"
HPADJ23_MEASUREMENT_AUTH_BLOB = "8042bdc63d636fd74e41fb7681e53c2ab8c76686"
HPADJ23_MEASUREMENT_WORKFLOW_BLOB = "f864d59964b06700112eaece7b033433389bf079"
RESTORE = {
    "README.md": "62ec5465089fffe316c64a179162bdd337ae8305",
    "MAIN-START-HERE.md": "47581a734da21dac3d2cabc4dc520d5be1310a49",
    "CURRENT-ROADMAP.md": "b733127cc0c17d45ad9f03525d04fecf46b29bbb",
    "CURRENT-AUDIT-CONTRACT.md": "ea133bb1a43bb417f049afe7d28eafcee702e0c4",
}
RETIRED = (
    "README.md",
    "MAIN-START-HERE.md",
    "MAINBATCH-OPERATIONS.md",
    "CROSS-LANE-STATE.json",
    "CURRENT-ROADMAP.md",
    "CURRENT-AUDIT-CONTRACT.md",
    "AUDIT-CONTRACT.md",
)

# Normal EX5 integrity is deliberately source-lock-only for these research
# producers. Their exact mathematical replay is audit/on-demand work, not a
# per-commit routing firewall. In particular HPADJ20 is a large nested exact
# LP replay and must not turn this lightweight integrity step into a heavy job.
LOCKED_PRODUCERS = {
    "hpadj-15_ex5/derive_b_shard_row_exact_grf04_picard_capacity_bound.py": "99ac15d18c83da050107ac7e8b113ae795ff0629",
    "hpadj-16_ex5/derive_q_quadratic_b_shard_mass_lp_bound.py": "61805f8b6d661c29805b6966e2453ed411d73189",
    "hpadj-17_ex5/derive_q_quadratic_b_shard_e_capacity_lp_bound.py": "10c1a836136f66b716ad39f6ca74250e32f386a9",
    "hpadj-18_ex5/derive_q_quadratic_exact_predomain_picard_parity_lp_bound.py": "09c3a97ca47f2602b547efc572a3ddfee1d3437f",
    "hpadj-19_ex5/derive_exact_support_qa_predomain_picard_lp_bound.py": "fdf5c721121d549361b08a92694373f3df7d02c8",
    "hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py": "837d647cfcbc96bbe384e564f449cd7042a46d48",
}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def verify_archived_v5_projection() -> None:
    req(all(not (HERE / name).exists() for name in RETIRED),
        "retired EX5 startup surface leaked into live root before V5 replay")
    req(ARCH_VERIFIER.is_file() and blob(ARCH_VERIFIER) == ARCH_VERIFIER_BLOB,
        "archived V5 verifier drift")
    req(ARCH_STATE.is_file() and blob(ARCH_STATE) == ARCH_STATE_BLOB,
        "archived V5 state drift")
    for name, expected in RESTORE.items():
        p = ARCH / name
        req(p.is_file() and blob(p) == expected, f"archived V5 startup input drift: {name}")

    old_tmp = TMP_VERIFIER.read_bytes() if TMP_VERIFIER.exists() else None
    old_state = MAIN_STATE.read_bytes()
    old_live = {name: (HERE / name).read_bytes() if (HERE / name).exists() else None for name in RESTORE}
    try:
        for name in RESTORE:
            (HERE / name).write_bytes((ARCH / name).read_bytes())
        MAIN_STATE.write_bytes(ARCH_STATE.read_bytes())
        TMP_VERIFIER.write_bytes(ARCH_VERIFIER.read_bytes())
        runpy.run_path(str(TMP_VERIFIER), run_name="__main__")
    finally:
        MAIN_STATE.write_bytes(old_state)
        for name, raw in old_live.items():
            p = HERE / name
            if raw is None:
                if p.exists():
                    p.unlink()
            else:
                p.write_bytes(raw)
        if old_tmp is None:
            if TMP_VERIFIER.exists():
                TMP_VERIFIER.unlink()
        else:
            TMP_VERIFIER.write_bytes(old_tmp)

    req(all(not (HERE / name).exists() for name in RETIRED),
        "retired EX5 startup surface leaked after V5 compatibility replay")


def verify_live_firewalls() -> None:
    for rel, expected in LOCKED_PRODUCERS.items():
        p = HERE / rel
        req(p.is_file(), f"missing locked producer: {rel}")
        req(blob(p) == expected, f"locked producer drift: {rel}")

    state = json.loads(MAIN_STATE.read_text())
    req(state.get("stage") == "32EX5", "MAIN-STATE stage drift")
    req(state.get("schema") == "STAGE32EX5_MAIN_COMPACT_STATE_V6_HPADJ23_EXACT_T_PRODUCER_PREFLIGHT",
        "MAIN-STATE schema/current-leaf drift")
    current = state.get("current", {})
    req(current.get("route_id") == "HPADJ-23_ex5", "current EX5 route drift")
    req(current.get("leaf") == "HPADJ23_EXACT_T_HOLE_HISTOGRAM_PRODUCER", "current EX5 leaf drift")
    next_step = state.get("next_step", {})
    req(next_step.get("id") == "HPADJ23_SCALEOUT_MEASUREMENT_PILOT", "next-step drift")
    req(next_step.get("heavy_scaleout_authorized") is False, "unexpected HPADJ23 heavy authorization")
    req(next_step.get("consumer_execution_authorized_here") is False, "178 consumer duplication authorized")
    authority = state.get("authority", {})
    req(authority.get("state_itself_grants_mathematical_credit") is False,
        "MAIN-STATE unexpectedly grants mathematical credit")
    main_authority = state.get("stage32_main_authority", {})
    req(main_authority.get("ex5_auto_promotes_to_main") is False,
        "EX5 auto-promotion firewall drift")

    credit = state.get("credit", {})
    for key in (
        "stage32_main_credit",
        "FULL178_complete",
        "effectivity_credit",
        "actual_curve_existence_credit",
        "receiver_credit",
        "final_milestone_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_credit",
    ):
        req(credit.get(key) is False, f"credit firewall drift: {key}")

    firewalls = state.get("firewalls", {})
    for key in (
        "ex5_progress_auto_promoted_to_stage32_main",
        "ex5_registered_into_n350_without_main_audit",
        "sat_witness_promoted_to_effective_curve_existence",
        "stage32_final_milestone_claimed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ):
        req(firewalls.get(key) is False, f"live firewall drift: {key}")


def verify_hpadj20_handoff_surface() -> None:
    req(HPADJ20_HANDOFF.is_file() and blob(HPADJ20_HANDOFF) == HPADJ20_HANDOFF_BLOB,
        "HPADJ20 audited MAIN handoff drift")
    req(HPADJ20_HANDOFF_VERIFIER.is_file() and
        blob(HPADJ20_HANDOFF_VERIFIER) == HPADJ20_HANDOFF_VERIFIER_BLOB,
        "HPADJ20 MAIN handoff verifier drift")

    old_argv = sys.argv[:]
    try:
        sys.argv = [str(HPADJ20_HANDOFF_VERIFIER)]
        runpy.run_path(str(HPADJ20_HANDOFF_VERIFIER), run_name="__main__")
    finally:
        sys.argv = old_argv


def verify_hpadj23_preflight_surface() -> None:
    req(HPADJ23_PREFLIGHT.is_file() and blob(HPADJ23_PREFLIGHT) == HPADJ23_PREFLIGHT_BLOB,
        "HPADJ23 retained preflight drift")
    req(HPADJ23_VERIFIER.is_file() and blob(HPADJ23_VERIFIER) == HPADJ23_VERIFIER_BLOB,
        "HPADJ23 bounded verifier drift")
    old_argv = sys.argv[:]
    try:
        sys.argv = [str(HPADJ23_VERIFIER)]
        runpy.run_path(str(HPADJ23_VERIFIER), run_name="__main__")
    finally:
        sys.argv = old_argv

def main() -> None:
    verify_archived_v5_projection()
    verify_live_firewalls()
    verify_hpadj20_handoff_surface()
    verify_hpadj23_preflight_surface()
    req(HPADJ23_BUILDER.is_file() and blob(HPADJ23_BUILDER) == HPADJ23_BUILDER_BLOB,
        "HPADJ23 exact-t builder drift")
    req(HPADJ23_BUILDER_RESULT.is_file() and blob(HPADJ23_BUILDER_RESULT) == HPADJ23_BUILDER_RESULT_BLOB,
        "HPADJ23 bounded builder result drift")
    old_argv = sys.argv[:]
    try:
        sys.argv = [str(HPADJ23_BUILDER)]
        runpy.run_path(str(HPADJ23_BUILDER), run_name="__main__")
    finally:
        sys.argv = old_argv
    req(HPADJ23_SERIALIZER.is_file() and blob(HPADJ23_SERIALIZER) == HPADJ23_SERIALIZER_BLOB,
        "HPADJ23 serializer drift")
    req(HPADJ23_SERIALIZATION_RESULT.is_file() and
        blob(HPADJ23_SERIALIZATION_RESULT) == HPADJ23_SERIALIZATION_RESULT_BLOB,
        "HPADJ23 serialization result drift")
    old_argv = sys.argv[:]
    try:
        sys.argv = [str(HPADJ23_SERIALIZER)]
        runpy.run_path(str(HPADJ23_SERIALIZER), run_name="__main__")
    finally:
        sys.argv = old_argv
    req(HPADJ23_HANDOFF.is_file() and blob(HPADJ23_HANDOFF) == HPADJ23_HANDOFF_BLOB,
        "HPADJ23 bounded producer handoff drift")
    req(HPADJ23_HANDOFF_VERIFIER.is_file() and
        blob(HPADJ23_HANDOFF_VERIFIER) == HPADJ23_HANDOFF_VERIFIER_BLOB,
        "HPADJ23 bounded handoff verifier drift")
    old_argv = sys.argv[:]
    try:
        sys.argv = [str(HPADJ23_HANDOFF_VERIFIER)]
        runpy.run_path(str(HPADJ23_HANDOFF_VERIFIER), run_name="__main__")
    finally:
        sys.argv = old_argv
    req(HPADJ23_SHARD_BUILDER.is_file() and
        blob(HPADJ23_SHARD_BUILDER) == HPADJ23_SHARD_BUILDER_BLOB,
        "HPADJ23 shard builder drift")
    req(HPADJ23_SHARD_EQ.is_file() and blob(HPADJ23_SHARD_EQ) == HPADJ23_SHARD_EQ_BLOB,
        "HPADJ23 shard equivalence receipt drift")
    req(HPADJ23_SHARD_EQ_VERIFIER.is_file() and
        blob(HPADJ23_SHARD_EQ_VERIFIER) == HPADJ23_SHARD_EQ_VERIFIER_BLOB,
        "HPADJ23 shard equivalence verifier drift")
    req(HPADJ23_SCALEOUT_PREFLIGHT.is_file() and
        blob(HPADJ23_SCALEOUT_PREFLIGHT) == HPADJ23_SCALEOUT_PREFLIGHT_BLOB,
        "HPADJ23 scaleout preflight drift")
    req(HPADJ23_SCALEOUT_RUNKEY.is_file(),
        "HPADJ23 scaleout measurement runkey missing")
    req(HPADJ23_SCALEOUT_VERIFIER.is_file() and
        blob(HPADJ23_SCALEOUT_VERIFIER) == HPADJ23_SCALEOUT_VERIFIER_BLOB,
        "HPADJ23 scaleout preflight verifier drift")
    old_argv = sys.argv[:]
    try:
        sys.argv = [str(HPADJ23_SCALEOUT_VERIFIER)]
        runpy.run_path(str(HPADJ23_SCALEOUT_VERIFIER), run_name="__main__")
    finally:
        sys.argv = old_argv
    req(HPADJ23_MEASUREMENT_RUNNER.is_file() and
        blob(HPADJ23_MEASUREMENT_RUNNER) == HPADJ23_MEASUREMENT_RUNNER_BLOB,
        "HPADJ23 measurement runner drift")
    req(HPADJ23_MEASUREMENT_CONTRACT.is_file() and
        blob(HPADJ23_MEASUREMENT_CONTRACT) == HPADJ23_MEASUREMENT_CONTRACT_BLOB,
        "HPADJ23 measurement execution contract drift")
    req(HPADJ23_MEASUREMENT_AUTH.is_file() and
        blob(HPADJ23_MEASUREMENT_AUTH) == HPADJ23_MEASUREMENT_AUTH_BLOB,
        "HPADJ23 measurement authorization verifier drift")
    req(HPADJ23_MEASUREMENT_WORKFLOW.is_file() and
        blob(HPADJ23_MEASUREMENT_WORKFLOW) == HPADJ23_MEASUREMENT_WORKFLOW_BLOB,
        "HPADJ23 measurement workflow drift")
    old_argv = sys.argv[:]
    try:
        sys.argv = [str(HPADJ23_MEASUREMENT_AUTH)]
        runpy.run_path(str(HPADJ23_MEASUREMENT_AUTH), run_name="__main__")
    finally:
        sys.argv = old_argv
    print("PASS: retained EX5 V5 state and live credit/routing firewalls verified")
    print("producer_policy=SOURCE_LOCK_ONLY_IN_NORMAL_CI")
    print("exact_replay_policy=HOSTILE_AUDIT_OR_ON_DEMAND")
    print("HPADJ23_SHARD_EQ_REPLAY_POLICY=SOURCE_LOCK_ONLY_IN_NORMAL_CI")
    print("HPADJ23_SCALEOUT=UNIVERSAL_H96_COLD_MEASUREMENT_GATE")
    print("HPADJ23_MEASUREMENT_EXECUTION_SURFACE=READY_DYNAMIC_RUNKEY")
    print("HPADJ20_SOURCE_LOCK=" + LOCKED_PRODUCERS[
        "hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py"
    ])
    print("HPADJ20_MAIN_HANDOFF_BLOB=" + HPADJ20_HANDOFF_BLOB)
    print("HPADJ20_MAIN_HANDOFF_VERIFIER_BLOB=" + HPADJ20_HANDOFF_VERIFIER_BLOB)
    print("live_startup=LANE-ADAPTERS -> stages/stage32-ex5/MAIN-STATE.json")


if __name__ == "__main__":
    main()
