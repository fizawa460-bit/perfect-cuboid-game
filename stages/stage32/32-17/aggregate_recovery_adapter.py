#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
import tempfile

AUDIT_SCHEMA = "STAGE32_16_E20_A0_LE65536_EXECUTION_STATE_V1"
EXPECTED_AUDIT_VERDICT = "PASS_EXACT_E20_A0_DELTA_AND_CUMULATIVE_LE65536_ZERO_TIER"
EXPECTED_PROFILE_SHA = "e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5"
LEGACY_RECORDED_PROFILE_SHA = "e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384d53fa1fee67c5"
EXPECTED_PREDECESSOR_SHA = "5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c"
AGGREGATOR = pathlib.Path("stages/stage32/32-17-recovery/aggregate_recovered_e20_tier114186.py")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Isolate the legacy Stage32-16 profile-SHA transcription typo while preserving its audited state verbatim."
    )
    ap.add_argument("--profile", type=pathlib.Path, required=True)
    ap.add_argument("--predecessor-audit-state", type=pathlib.Path, required=True)
    ap.add_argument("--plan", type=pathlib.Path, required=True)
    ap.add_argument("--input-dir", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    profile = json.loads(args.profile.read_text())
    audit = json.loads(args.predecessor_audit_state.read_text())
    plan = json.loads(args.plan.read_text())

    # The regenerated profile and the Stage32-17 plan independently lock the
    # actual 64-hex profile digest. Stage32-16's committed execution-state has
    # a known 61-character transcription typo in that metadata field only.
    assert profile["canonical_sha256_without_this_field"] == EXPECTED_PROFILE_SHA
    assert plan["profile_sha256"] == EXPECTED_PROFILE_SHA
    assert len(EXPECTED_PROFILE_SHA) == 64
    assert len(LEGACY_RECORDED_PROFILE_SHA) == 61
    assert EXPECTED_PROFILE_SHA != LEGACY_RECORDED_PROFILE_SHA

    # Do not edit or silently reinterpret the historical audit state. Accept
    # exactly the already-committed typo, and independently re-lock every
    # predecessor fact that grants imported exact credit.
    assert audit["schema"] == AUDIT_SCHEMA
    assert audit["execution_verdict"] == EXPECTED_AUDIT_VERDICT
    assert audit["audit_final_verdict"] == EXPECTED_AUDIT_VERDICT
    assert audit["hostile_audit_required"] is False
    assert audit["profile_sha256"] == LEGACY_RECORDED_PROFILE_SHA

    prev = audit["cumulative_tier"]
    assert int(prev["threshold"]) == 65_536
    assert int(prev["cells"]) == 301
    assert int(prev["materialized_branches"]) == 6_834_114
    assert int(prev["search_nodes"]) == 1_881_870
    assert int(prev["unknown_branches"]) == 0
    assert int(prev["numerical_survivors"]) == 0
    assert prev["all_selected_cells_unsat"] is True
    assert prev["canonical_sha256"] == EXPECTED_PREDECESSOR_SHA

    independent = audit["independent_reaggregation"]
    assert int(independent["all_bundle_artifacts_downloaded"]) == 48
    assert int(independent["all_compact_certificates_verified"]) == 287
    assert independent["parsed_aggregate_equal"] is True
    assert independent["canonical_sha256"] == EXPECTED_PREDECESSOR_SHA

    # The existing recovery aggregator intentionally insists on the correct
    # profile SHA. Feed it an ephemeral adapter copy only; the repository
    # history and the final preserved predecessor audit file remain unchanged.
    patched = dict(audit)
    patched["profile_sha256"] = EXPECTED_PROFILE_SHA

    with tempfile.TemporaryDirectory(prefix="stage32-17-audit-adapter-") as td:
        adapted = pathlib.Path(td) / "stage32-16-execution-state-adapted.json"
        adapted.write_text(json.dumps(patched, indent=2, sort_keys=True) + "\n")
        subprocess.run(
            [
                sys.executable,
                str(AGGREGATOR),
                "--profile",
                str(args.profile),
                "--predecessor-audit-state",
                str(adapted),
                "--plan",
                str(args.plan),
                "--input-dir",
                str(args.input_dir),
                "--output",
                str(args.output),
            ],
            check=True,
        )

    print(
        json.dumps(
            {
                "adapter": "LEGACY_STAGE32_16_PROFILE_SHA_TRANSCRIPTION_ONLY",
                "legacy_recorded_profile_sha256": LEGACY_RECORDED_PROFILE_SHA,
                "correct_profile_sha256": EXPECTED_PROFILE_SHA,
                "historical_audit_state_modified": False,
                "predecessor_canonical_sha256": EXPECTED_PREDECESSOR_SHA,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
