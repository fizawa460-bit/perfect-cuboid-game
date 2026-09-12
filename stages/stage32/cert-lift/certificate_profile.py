#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE_ROOT = Path(os.environ.get("CERTLIFT_EX5_SOURCE_ROOT", str(ROOT))).resolve()
EX5_HANDOFF = SOURCE_ROOT / "stages/stage32-ex5/cut-handoff"
EX5_ADAPTER = EX5_HANDOFF / "e8_terminal_population_adapter.py"
if not EX5_ADAPTER.is_file():
    raise RuntimeError(
        "locked EX5 adapter checkout missing; set CERTLIFT_EX5_SOURCE_ROOT to the exact producer checkout"
    )
sys.path.insert(0, str(EX5_HANDOFF))

import e8_terminal_population_adapter as e8

LEDGER = HERE / "CERTIFICATE-LEDGER.json"
SOURCE_MANIFEST = ROOT / "stages/stage32/cut-cert-lift/SOURCE-LOCKS.json"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def load_ledger() -> dict:
    ledger = json.loads(LEDGER.read_text())
    body = dict(ledger)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(
        ledger.get("schema") == "STAGE32_CERTLIFT_CERTIFICATE_LEDGER_V1"
        and claimed == csha(body),
        "certificate ledger canonical/schema drift",
    )
    return ledger


def verify_source_manifest(ledger: dict) -> None:
    manifest = json.loads(SOURCE_MANIFEST.read_text())
    req(
        manifest.get("schema") == "STAGE32_CUT_CERT_LIFT_SOURCE_LOCKS_V1",
        "CERT-LIFT source manifest schema drift",
    )
    shared = manifest.get("shared_inputs", {})
    expected_head = shared.get("ex5_e8_terminal_producer_exact_head")
    req(isinstance(expected_head, str) and len(expected_head) == 40, "EX5 producer head lock missing")
    req(
        shared.get("adapter_path") == "stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py",
        "EX5 adapter path lock drift",
    )
    actual_head = subprocess.check_output(
        ["git", "-C", str(SOURCE_ROOT), "rev-parse", "HEAD"], text=True
    ).strip()
    req(actual_head == expected_head, f"EX5 source checkout head drift: {actual_head}")

    locked = {w["id"]: w for w in manifest["waves"]}
    for wave in ledger["waves"]:
        src = locked.get(wave["id"])
        req(src is not None, f"missing source lock for {wave['id']}")
        req(src["pr"] == wave["pr"], f"PR drift for {wave['id']}")
        req(src["exact_head"] == wave["exact_head"], f"exact-head drift for {wave['id']}")
        req(
            [src["offset_start"], src["offset_end"]] == wave["offsets"],
            f"offset drift for {wave['id']}",
        )
        req(src["blocks"] == 255 and src["terminals"] == 28815, f"scope drift for {wave['id']}")
        req(
            src["candidate_closed_blocks"] == wave["closed"],
            f"closed-count drift for {wave['id']}",
        )
    agg = manifest["aggregate"]
    req(
        agg["blocks"] == ledger["scope"]["blocks"]
        and agg["terminals"] == ledger["scope"]["terminals"],
        "aggregate scope drift",
    )


def build_profile(ledger: dict) -> dict:
    verify_source_manifest(ledger)
    survivors = e8.current_main_survivor_block_indices()
    idx = e8.indexer()

    mass_bins: dict[str, dict[str, int]] = {}
    per_wave = []
    selected_closed = 0
    selected_residual = 0
    threshold6_residual = 0
    closed_total = 0
    residual_total = 0
    seen_blocks: set[int] = set()

    for wave in ledger["waves"]:
        start, end = map(int, wave["offsets"])
        blocks = list(map(int, survivors[start : end + 1]))
        req(len(blocks) == 255, f"{wave['id']} reconstructed block-count drift")
        req(seen_blocks.isdisjoint(blocks), f"{wave['id']} overlaps prior wave")
        seen_blocks.update(blocks)

        residual = set(map(int, wave["residual_blocks"]))
        req(residual.issubset(blocks), f"{wave['id']} residual outside reconstructed scope")
        req(len(residual) == wave["residual"], f"{wave['id']} residual-count drift")
        req(len(blocks) - len(residual) == wave["closed"], f"{wave['id']} closed-count drift")

        wave_selected_closed = 0
        wave_selected_residual = 0
        for block in blocks:
            sig = e8.block_signature(block, idx)
            req(sig["current_main_audited_prefix_survivor"] is True, f"prefix survivor drift at block {block}")
            mass = int(sig["fixed_exceptional_mass"])
            label = "residual" if block in residual else "closed"
            slot = mass_bins.setdefault(str(mass), {"closed": 0, "residual": 0})
            slot[label] += 1

            if block in residual:
                residual_total += 1
                if mass >= 6:
                    threshold6_residual += 1
                if mass >= 7:
                    selected_residual += 1
                    wave_selected_residual += 1
            else:
                closed_total += 1
                if mass >= 7:
                    selected_closed += 1
                    wave_selected_closed += 1

        req(
            wave_selected_closed == wave["mass_ge_7_closed"]
            and wave_selected_residual == 0,
            f"MASS7 replay drift for {wave['id']}",
        )
        per_wave.append(
            {
                "id": wave["id"],
                "offsets": wave["offsets"],
                "closed": wave["closed"],
                "residual": wave["residual"],
                "mass_ge_7_closed": wave_selected_closed,
                "mass_ge_7_residual": wave_selected_residual,
            }
        )

    expected_bins = ledger["profile"]["mass_bins"]
    req(mass_bins == expected_bins, "fixed-exceptional-mass profile drift")
    req(closed_total == ledger["profile"]["closed_total"] == 1433, "closed total drift")
    req(residual_total == ledger["profile"]["residual_total"] == 97, "residual total drift")

    rule = ledger["candidate_rule"]
    req(selected_closed == rule["selected_closed_blocks"] == 1049, "MASS7 closed coverage drift")
    req(selected_residual == rule["selected_residual_blocks"] == 0, "MASS7 residual counterexample")
    req(
        threshold6_residual == rule["threshold_6_residual_counterexamples"] == 13,
        "MASS6 minimality-control drift",
    )

    out = {
        "schema": "STAGE32_CERTLIFT_CERTIFICATE_PROFILE_V1",
        "stage": "32",
        "node": "CERTLIFT-01",
        "status": "PASS_AUDITED_SEPARATOR_L1_ONLY",
        "scope": ledger["scope"],
        "signature": ledger["signature"],
        "candidate_rule": rule,
        "mass_bins": mass_bins,
        "per_wave": per_wave,
        "checks": {
            "source_manifest_locked": True,
            "ex5_source_checkout_exact_head_locked": True,
            "all_six_wave_scopes_reconstructed_from_current_main_prefix_adapter": True,
            "residual_controls_replayed": True,
            "cp_sat_or_z3_rerun": False,
            "mass_ge_7_residual_counterexamples": selected_residual,
            "mass_ge_6_residual_counterexamples": threshold6_residual,
        },
        "firewalls": ledger["firewalls"],
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-check", action="store_true")
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    profile = build_profile(load_ledger())
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(profile, sort_keys=True, indent=2) + "\n")
    if args.self_check:
        print(
            json.dumps(
                {
                    "status": "PASS",
                    "closed": profile["candidate_rule"]["selected_closed_blocks"],
                    "residual_counterexamples": profile["candidate_rule"]["selected_residual_blocks"],
                    "canonical": profile["canonical_sha256_without_this_field"],
                },
                sort_keys=True,
            )
        )
    elif not args.output:
        print(json.dumps(profile, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
