#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER65536_WORK_BALANCED_PLAN_V1"
CERT_SCHEMA = "STAGE32_D8_E20_A0_DYNAMIC_SHARD_COMPACT_CERT_V1"
OUT_SCHEMA = "STAGE32_16_PREDECESSOR_NEIGHBOR_EXACT_REGRESSION_V1"


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=pathlib.Path, required=True)
    ap.add_argument("--compact", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    plan = json.loads(args.plan.read_text())
    cert = json.loads(args.compact.read_text())
    assert plan["schema"] == PLAN_SCHEMA
    plan_unsigned = dict(plan)
    plan_claimed = plan_unsigned.pop("canonical_sha256_without_this_field")
    assert csha(plan_unsigned) == plan_claimed
    assert cert["schema"] == CERT_SCHEMA
    cert_unsigned = dict(cert)
    cert_claimed = cert_unsigned.pop("canonical_sha256_without_this_field")
    assert csha(cert_unsigned) == cert_claimed

    regression = plan["representative_predecessor_regression"]
    item = regression["item"]
    p = cert["parameters"]
    for key in ("cell_index", "cell_id", "shard_index", "shard_count"):
        assert p[key] == item[key]
    assert int(cert["parent_cell_total_branch_count"]) == int(item["total_branches"])
    assert int(cert["executed_shard_branch_count"]) == int(
        item["expected_shard_branches"]
    )
    assert cert["all_branches_complete"] is True
    assert int(cert["unknown_branch_count"]) == 0
    assert cert["branch_exact_evidence_stream_sha256"] == regression[
        "expected_branch_exact_evidence_stream_sha256"
    ]
    assert int(cert["exact_numerical_survivor_count_in_shard"]) == int(
        regression["expected_exact_numerical_survivor_count"]
    )
    assert cert["signature_cell_sha256"] == regression[
        "expected_signature_cell_sha256"
    ]
    assert cert["shared_context_certificate_sha256"] == regression[
        "expected_shared_context_certificate_sha256"
    ]

    report = {
        "schema": OUT_SCHEMA,
        "plan_sha256": plan_claimed,
        "new_compact_certificate_sha256": cert_claimed,
        "cell_index": int(item["cell_index"]),
        "cell_id": item["cell_id"],
        "shard_index": int(item["shard_index"]),
        "shard_count": int(item["shard_count"]),
        "executed_branches": int(cert["executed_shard_branch_count"]),
        "branch_exact_evidence_stream_sha256": cert[
            "branch_exact_evidence_stream_sha256"
        ],
        "exact_numerical_survivor_count": int(
            cert["exact_numerical_survivor_count_in_shard"]
        ),
        "predecessor_regression_complete": True,
        "predecessor_regression_match": True,
        "theorem_credit": False,
        "receiver_credit": False,
    }
    report["canonical_sha256_without_this_field"] = csha(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
