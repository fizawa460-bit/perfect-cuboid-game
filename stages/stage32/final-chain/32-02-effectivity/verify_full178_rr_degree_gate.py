#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
GATE = HERE / "FULL178-RR-DEGREE-GATE.json"
MANIFEST = REPO / "stages/stage32/residual-32-01-production/full178-manifest.json"
EXPECTED_MANIFEST_BLOB = "0a46b34e278688240656b4977e9cb7f589e90e06"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(f"FAIL: {message}")


def canonical_without_self(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def main() -> None:
    gate = json.loads(GATE.read_text(encoding="utf-8"))
    req(gate["schema"] == "STAGE32_FINAL_CHAIN_32_02_FULL178_RR_DEGREE_GATE_V1", "gate schema drift")
    req(canonical_without_self(gate) == gate["canonical_sha256_without_this_field"], "gate canonical drift")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lock = gate["manifest"]
    req(manifest["schema"] == lock["schema"], "FULL178 manifest schema drift")
    req(manifest["residual_row_count"] == lock["residual_row_count"] == 178, "FULL178 row-count drift")
    req(
        canonical_without_self(manifest) == lock["canonical_sha256_without_this_field"],
        "FULL178 manifest canonical drift",
    )
    blob = subprocess.check_output(["git", "hash-object", str(MANIFEST)], text=True).strip()
    req(blob == EXPECTED_MANIFEST_BLOB, "FULL178 manifest blob drift")

    rows: list[str] = []
    for class_rows in manifest["m_class_rows"].values():
        rows.extend(class_rows)
    req(len(rows) == 178, "FULL178 manifest row materialization is not 178")
    req(len(set(rows)) == 178, "FULL178 manifest contains duplicate row ids")

    parsed: list[tuple[str, int, int]] = []
    for row in rows:
        match = re.fullmatch(r"g([01])-d(\d{3})", row)
        req(match is not None, f"invalid FULL178 row id: {row}")
        parsed.append((row, int(match.group(1)), int(match.group(2))))

    high = sorted(row for row, _, degree in parsed if degree > 16)
    low = sorted(row for row, _, degree in parsed if degree <= 16)
    expected = gate["rr_degree_gate"]
    req(len(high) == expected["degree_gt_16_row_count"] == 168, "degree>16 count drift")
    req(len(low) == expected["degree_le_16_row_count"] == 10, "degree<=16 count drift")
    req(low == sorted(expected["degree_le_16_rows"]), "degree<=16 row set drift")
    req(set(high).isdisjoint(low) and len(high) + len(low) == 178, "degree gate is not an exact partition")

    semantics = gate["semantics"]
    for key in (
        "degree_gate_is_not_effectivity_certification",
        "degree_gate_is_not_survivor_count",
        "degree_gate_does_not_assume_all_rows_survive_full178",
    ):
        req(semantics[key] is True, f"degree-gate semantic firewall missing: {key}")
    req(semantics["rr_surface_assumptions_source_locked_here"] is False, "surface assumptions falsely source-locked")
    req(semantics["final_survivor_picard_ledger_available"] is False, "survivor ledger falsely declared available")

    firewall = gate["credit_firewall"]
    req(firewall["effectivity_preparation_credit"] is True, "preparation credit missing")
    for key in (
        "effectivity_final_execution_released",
        "full178_pruning_credit",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "merge_authorized",
    ):
        req(firewall[key] is False, f"credit firewall opened: {key}")

    print("PASS: FULL178 RR degree gate source-locked to retained manifest")
    print("degree>16 rows=168; degree<=16 rows=10")
    print("credit: 32-02 preparation only; no effectivity/survivor/FULL178 closure credit")


if __name__ == "__main__":
    main()
