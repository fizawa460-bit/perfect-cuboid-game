#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
EFF_AFFINE01 = HERE / "effectivity-affine" / "eff_affine01_base4_kernel_preflight.py"
EFF_FP58 = HERE / "effectivity-affine" / "eff_affine01_fp58_engine.py"
EFF_FP58_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"
EFF_FP58_AGG = HERE / "effectivity-affine" / "aggregate_eff_affine01_fp58_shards.py"
EFF_FP58_AGG_BLOB = "39d957f2638cbf39217d27f4c1ee49ba3675811d"
ARCH = HERE / "archive" / "startup-surface-20260914"
ARCH_VERIFIER = ARCH / "verify_main_state_v5_pre_startup_collapse.py"
TMP_VERIFIER = HERE / ".verify_main_state_v5_pre_startup_collapse.py"

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


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


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

    live = json.loads((HERE / "MAIN-STATE.json").read_text(encoding="utf-8"))["live_current"]
    req(live["authority"] == "SUPERSEDES_LEGACY_V5_CURRENT_AND_STAGE32_MAIN_AUTHORITY_FIELDS_FOR_ORDINARY_STARTUP",
        "live V48 override authority missing")
    req(live["observed_repository_main"] == "e7fd29d24dd21e8529dbdb45b221a53f2cc21ed3",
        "live repository-main observation drift")
    req(live["stage32_main_state_blob_sha1"] == "070847c669120aef1ab3777239d45878937b41f3",
        "live Stage32 MAIN state lock drift")
    req(live["stage32_primary_incomplete_id"] == "32-02" and
        live["stage32_primary_incomplete_name"] == "EFFECTIVITY_SURVIVOR_DISPOSAL",
        "EX5 did not advance from completed 32-01 to 32-02")
    req(live["full178_numerical_census_complete"] is True,
        "completed FULL178 census regressed in EX5 startup")
    req(live["authoritative_remaining_terminals"] == "128470212118313474449",
        "V48 certified upper bound drift")
    req(live["active_leaf"] == "EFF-AFFINE01_BASE4_HPERP_EXACT_CHECKER_PREFLIGHT",
        "EX5 effectivity producer leaf drift")
    req(live["open_cross_lane_demands_for_ex5"] == 0,
        "unexpected EX5 demand count in live override")
    req(live["heavy_scaleout_authorized"] is False and
        live["effectivity_credit"] is False and live["main_credit"] is False and
        live["merge_authorized"] is False,
        "EX5 live override leaked unauthorized credit")

    req(EFF_AFFINE01.is_file(), "missing EFF-AFFINE01 structural preflight")
    req(EFF_FP58.is_file() and blob(EFF_FP58) == EFF_FP58_BLOB, "EFF-AFFINE01 FP58 engine drift")
    req(EFF_FP58_AGG.is_file() and blob(EFF_FP58_AGG) == EFF_FP58_AGG_BLOB, "EFF-AFFINE01 FP58 aggregator drift")
    fp58_text = EFF_FP58.read_text(encoding="utf-8")
    req('N=58' in fp58_text and '"BAD_SHELL_UNSAT_EXACT"' in fp58_text and
        'all140_pruning' in fp58_text and 'two_sided_pairing_pruning' in fp58_text,
        "EFF-AFFINE01 FP58 completeness/two-sided-pruning markers missing")
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "eff-affine01.json"
        subprocess.run(
            [sys.executable, str(EFF_AFFINE01), "--output", str(out)],
            cwd=ROOT,
            check=True,
        )
        result = json.loads(out.read_text(encoding="utf-8"))
    req(result["status"] ==
        "STRUCTURAL_PASS_HNF_SATURATED_KERNEL58_NEGATIVE_DEFINITE_GRAM_LLL_READY",
        "EFF-AFFINE01 structural status drift")
    req(result["fixed_fiber"]["fixed_map_rank"] == 6 and
        result["fixed_fiber"]["saturated_integer_kernel_dimension"] == 58,
        "EFF-AFFINE01 rank/kernel regression")
    req(result["fixed_fiber"]["restricted_negative_gram_positive_definite"] is True,
        "EFF-AFFINE01 H-perp definiteness regression")
    req(result["firewalls"]["integer_affine_kernel_and_image_basis_certified"] is True and
        result["firewalls"]["fincke_pohst_bad_shell_checker_complete"] is False and
        result["firewalls"]["effectivity_credit"] is False and
        result["firewalls"]["main_pruning_credit"] is False,
        "EFF-AFFINE01 structural preflight overclaimed credit")

    print("PASS: retained EX5 V5 mathematical state replayed against archived startup projection only")
    print("live_startup=LANE-ADAPTERS -> stages/stage32-ex5/MAIN-STATE.json")


if __name__ == "__main__":
    main()
