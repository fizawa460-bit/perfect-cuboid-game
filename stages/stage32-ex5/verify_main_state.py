#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCH = HERE / "archive" / "startup-surface-20260914"
ARCH_VERIFIER = ARCH / "verify_main_state_v5_pre_startup_collapse.py"
TMP_VERIFIER = HERE / ".verify_main_state_v5_pre_startup_collapse.py"
MAIN_STATE = HERE / "MAIN-STATE.json"

ARCH_VERIFIER_BLOB = "fa20238eb372100520a2ca76523ca63d3b3f9c5f"
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
    for name, expected in RESTORE.items():
        p = ARCH / name
        req(p.is_file() and blob(p) == expected, f"archived V5 startup input drift: {name}")

    old_tmp = TMP_VERIFIER.read_bytes() if TMP_VERIFIER.exists() else None
    old_live = {name: (HERE / name).read_bytes() if (HERE / name).exists() else None for name in RESTORE}
    try:
        for name in RESTORE:
            (HERE / name).write_bytes((ARCH / name).read_bytes())
        TMP_VERIFIER.write_bytes(ARCH_VERIFIER.read_bytes())
        runpy.run_path(str(TMP_VERIFIER), run_name="__main__")
    finally:
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


def main() -> None:
    verify_archived_v5_projection()
    verify_live_firewalls()
    print("PASS: retained EX5 V5 state and live credit/routing firewalls verified")
    print("producer_policy=SOURCE_LOCK_ONLY_IN_NORMAL_CI")
    print("exact_replay_policy=HOSTILE_AUDIT_OR_ON_DEMAND")
    print("HPADJ20_SOURCE_LOCK=" + LOCKED_PRODUCERS[
        "hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py"
    ])
    print("live_startup=LANE-ADAPTERS -> stages/stage32-ex5/MAIN-STATE.json")


if __name__ == "__main__":
    main()
