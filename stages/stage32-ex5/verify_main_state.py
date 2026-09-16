#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCH = HERE / "archive" / "startup-surface-20260914"
ARCH_VERIFIER = ARCH / "verify_main_state_v5_pre_startup_collapse.py"
TMP_VERIFIER = HERE / ".verify_main_state_v5_pre_startup_collapse.py"
HPADJ15 = HERE / "hpadj-15_ex5" / "derive_b_shard_row_exact_grf04_picard_capacity_bound.py"
HPADJ16 = HERE / "hpadj-16_ex5" / "derive_q_quadratic_b_shard_mass_lp_bound.py"
HPADJ17 = HERE / "hpadj-17_ex5" / "derive_q_quadratic_b_shard_e_capacity_lp_bound.py"

ARCH_VERIFIER_BLOB = "fa20238eb372100520a2ca76523ca63d3b3f9c5f"
HPADJ15_BLOB = "99ac15d18c83da050107ac7e8b113ae795ff0629"
HPADJ16_BLOB = "61805f8b6d661c29805b6966e2453ed411d73189"
HPADJ17_BLOB = "10c1a836136f66b716ad39f6ca74250e32f386a9"
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


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def run_json_script(path: Path) -> dict:
    proc = subprocess.run([sys.executable, str(path)], text=True, capture_output=True)
    if proc.returncode != 0:
        if proc.stdout:
            print(proc.stdout, end="")
        if proc.stderr:
            print(proc.stderr, end="", file=sys.stderr)
        raise SystemExit(proc.returncode)
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    req(lines, f"{path.name} produced no output")
    return json.loads(lines[-1])


def replay_hpadj15_if_present() -> bool:
    if not HPADJ15.exists():
        return False
    req(blob(HPADJ15) == HPADJ15_BLOB, "HPADJ15 live verifier blob drift")
    data = run_json_script(HPADJ15)
    req(data["status"] == "B_SHARD_ROW_EXACT_GRF04_PICARD_CAPACITY_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "HPADJ15 status drift")
    req(data["candidate_bound"]["hpadj15_candidate_upper_bound"] <= 463577241806597722598,
        "HPADJ15 weakened HPADJ14")
    req(data["semantics"]["statistical_independence_assumed"] is False,
        "HPADJ15 independence firewall")
    req(data["semantics"]["new_heavy_run_used"] is False,
        "HPADJ15 heavy-run firewall")
    req(data["firewalls"]["stage32_main_pruning_credit"] is False,
        "HPADJ15 MAIN-credit firewall")
    print("HPADJ15_CANONICAL=" + data["canonical_sha256_without_this_field"])
    print("HPADJ15_UPPER=" + str(data["candidate_bound"]["hpadj15_candidate_upper_bound"]))
    return True


def replay_hpadj16_if_present() -> bool:
    if not HPADJ16.exists():
        return False
    req(blob(HPADJ16) == HPADJ16_BLOB, "HPADJ16 live verifier blob drift")
    data = run_json_script(HPADJ16)
    req(data["status"] == "Q_QUADRATIC_B_SHARD_EXACT_MASS_LP_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "HPADJ16 status drift")
    req(data["candidate_bound"]["hpadj16_candidate_upper_bound"] <= 195603649074545538415,
        "HPADJ16 weakened MAIN q-quadratic candidate")
    req(data["semantics"]["statistical_independence_assumed"] is False,
        "HPADJ16 independence firewall")
    req(data["semantics"]["q_quadratic_candidate_credit_inherited"] is False,
        "HPADJ16 source-credit firewall")
    req(data["firewalls"]["stage32_main_pruning_credit"] is False,
        "HPADJ16 MAIN-credit firewall")
    print("HPADJ16_CANONICAL=" + data["canonical_sha256_without_this_field"])
    print("HPADJ16_UPPER=" + str(data["candidate_bound"]["hpadj16_candidate_upper_bound"]))
    return True


def replay_hpadj17_if_present() -> bool:
    if not HPADJ17.exists():
        return False
    req(blob(HPADJ17) == HPADJ17_BLOB, "HPADJ17 live verifier blob drift")
    data = run_json_script(HPADJ17)
    req(data["status"] == "Q_QUADRATIC_B_SHARD_EXACT_MASS_AND_E_CAPACITY_LP_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "HPADJ17 status drift")
    req(data["candidate_bound"]["hpadj17_candidate_upper_bound"] <= 195603649074545538415,
        "HPADJ17 weakened MAIN q-quadratic candidate")
    req(data["candidate_bound"]["hpadj17_candidate_upper_bound"] <= 426398981823116026011,
        "HPADJ17 weakened HPADJ15")
    req(data["semantics"]["statistical_independence_assumed"] is False,
        "HPADJ17 independence firewall")
    req(data["semantics"]["q_quadratic_source_credit_inherited"] is False,
        "HPADJ17 source-credit firewall")
    req(data["semantics"]["new_heavy_run_used"] is False,
        "HPADJ17 heavy-run firewall")
    req(data["firewalls"]["stage32_main_pruning_credit"] is False,
        "HPADJ17 MAIN-credit firewall")
    print("HPADJ17_CANONICAL=" + data["canonical_sha256_without_this_field"])
    print("HPADJ17_UPPER=" + str(data["candidate_bound"]["hpadj17_candidate_upper_bound"]))
    print("HPADJ17_IMPROVEMENT_VS_MAIN_Q=" + str(data["candidate_bound"]["improvement_vs_main_q_quadratic_global"]))
    return True


def main() -> None:
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
    if not replay_hpadj17_if_present():
        if not replay_hpadj16_if_present():
            replay_hpadj15_if_present()
    print("PASS: retained EX5 V5 mathematical state replayed against archived startup projection only")
    print("live_startup=LANE-ADAPTERS -> stages/stage32-ex5/MAIN-STATE.json")


if __name__ == "__main__":
    main()
