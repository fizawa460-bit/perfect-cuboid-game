#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
from typing import Any

SCHEMA = "STAGE32_17_ACTIONS_RETAINED_STORAGE_GATE_V1"
CONSERVATIVE_INCREMENTAL_CEILING_BYTES = 100_000_000
NEW_COMPACT_CERTIFICATE_BOUND_BYTES = 364 * 20_000
NEW_BUNDLE_RECEIPT_BOUND_BYTES = 80 * 100_000
NEW_FINAL_AGGREGATE_BOUND_BYTES = 10_000_000
NEW_PLAN_AND_GATE_BOUND_BYTES = 2_000_000
NEW_RUN_OWN_BOUND_BYTES = (
    NEW_COMPACT_CERTIFICATE_BOUND_BYTES
    + NEW_BUNDLE_RECEIPT_BOUND_BYTES
    + NEW_FINAL_AGGREGATE_BOUND_BYTES
    + NEW_PLAN_AND_GATE_BOUND_BYTES
)
REQUIRED = {
    (32624596141, "stage32-01-low-degree-verified-prefix"),
    (32725113188, "stage32-14-e20-profile-plan"),
    (32733420941, "stage32-16-e20-a0-le65536-exact-tier"),
}


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--enforce", action="store_true")
    args = ap.parse_args()

    pages = json.loads(args.inventory.read_text(encoding="utf-8-sig"))
    assert isinstance(pages, list) and pages
    all_rows = [row for page in pages for row in page["artifacts"]]
    assert len(all_rows) == int(pages[0]["total_count"])
    retained = [row for row in all_rows if not bool(row["expired"])]
    retained_bytes = sum(int(row["size_in_bytes"]) for row in retained)
    stage32_rows = [row for row in retained if str(row["name"]).startswith("stage32-")]

    required_rows: list[dict[str, Any]] = []
    for run_id, name in sorted(REQUIRED):
        matches = [
            row for row in retained
            if int(row["workflow_run"]["id"]) == run_id and str(row["name"]) == name
        ]
        assert len(matches) == 1, (run_id, name, len(matches))
        row = matches[0]
        required_rows.append({
            "workflow_run_id": run_id,
            "artifact_id": int(row["id"]),
            "name": name,
            "retained_bytes": int(row["size_in_bytes"]),
            "expires_at": row["expires_at"],
        })

    safe = NEW_RUN_OWN_BOUND_BYTES < CONSERVATIVE_INCREMENTAL_CEILING_BYTES
    report = {
        "schema": SCHEMA,
        "measured_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "inventory_source": "GET_REPOSITORY_ACTIONS_ARTIFACTS_ALL_PAGES",
        "inventory_complete": True,
        "retained_artifact_count": len(retained),
        "retained_artifact_bytes": retained_bytes,
        "retained_stage32_artifact_count": len(stage32_rows),
        "retained_stage32_artifact_bytes": sum(int(row["size_in_bytes"]) for row in stage32_rows),
        "required_predecessor_artifacts": required_rows,
        "historical_retained_inventory_is_background_only": True,
        "conservative_new_run_incremental_ceiling_bytes": CONSERVATIVE_INCREMENTAL_CEILING_BYTES,
        "new_run_worst_case": {
            "compact_certificates_bytes": NEW_COMPACT_CERTIFICATE_BOUND_BYTES,
            "bundle_receipts_bytes": NEW_BUNDLE_RECEIPT_BOUND_BYTES,
            "final_aggregate_bytes": NEW_FINAL_AGGREGATE_BOUND_BYTES,
            "plan_and_gate_bytes": NEW_PLAN_AND_GATE_BOUND_BYTES,
            "total_bytes": NEW_RUN_OWN_BOUND_BYTES,
            "below_100mb_fallback_requirement": NEW_RUN_OWN_BOUND_BYTES < 100_000_000,
            "does_not_depend_on_deletion": True,
        },
        "projected_simultaneous_retained_peak_bytes": retained_bytes + NEW_RUN_OWN_BOUND_BYTES,
        "new_run_incremental_headroom_bytes": CONSERVATIVE_INCREMENTAL_CEILING_BYTES - NEW_RUN_OWN_BOUND_BYTES,
        "safe_to_launch_pilot_or_fanout": safe,
        "stop_reason": None if safe else "NEW_RUN_WORST_CASE_INCREMENTAL_STORAGE_EXCEEDS_100MB_GATE",
        "theorem_credit": False,
        "receiver_credit": False,
    }
    deterministic = {k: v for k, v in report.items() if k != "measured_at_utc"}
    report["deterministic_sha256_without_measurement_time"] = csha(deterministic)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "retained_artifacts": len(retained),
        "retained_bytes": retained_bytes,
        "new_run_bound_bytes": NEW_RUN_OWN_BOUND_BYTES,
        "safe_to_launch": safe,
    }, sort_keys=True))
    if args.enforce and not safe:
        raise SystemExit("STOP: new-run incremental Actions storage violates the conservative 100 MB gate")


if __name__ == "__main__":
    main()
