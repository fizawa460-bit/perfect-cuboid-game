#!/usr/bin/env python3
"""Verify the immutable Stage32-02 stopped-run evidence summary."""

from __future__ import annotations

import hashlib
import json
import pathlib


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    path = pathlib.Path(__file__).with_name("local-evidence.json")
    evidence = json.loads(path.read_text(encoding="utf-8"))
    unsigned = dict(evidence)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(unsigned) == claimed
    residuals = evidence["formerly_unresolved_residuals"]
    assert len(residuals) == 28
    assert evidence["closed_residual_count"] == 14
    assert sum(row["disposition"].startswith("CLOSED") for row in residuals) == 14
    assert all(
        row["exact_survivor_count"] == 0
        for row in residuals
        if row["disposition"].startswith("CLOSED")
    )
    terminal = evidence["terminal_unknown"]
    assert evidence["terminal_unknown_count"] == len(terminal) == 44
    assert all(row["solver_result"] == "unknown" for row in terminal)
    assert all(row["unknown_reason"] == "timeout" for row in terminal)
    assert all(row["degree"] == 6 and row["genus"] == 1 for row in terminal)
    assert all(
        row["exceptional_mass"] == 4 and row["curve_group_mass"] == 32
        for row in terminal
    )
    assert evidence["all_28_residuals_exactly_closed"] is False
    assert evidence["predecessor_regression_complete"] is False
    assert evidence["predecessor_regression_match"] is None
    assert evidence["receiver_credit"] is False
    assert evidence["full_d176_d192_numerical_orbit_census"] is False
    print(
        json.dumps(
            {
                "evidence_sha256": claimed,
                "closed_residuals": evidence["closed_residual_count"],
                "terminal_unknown": evidence["terminal_unknown_count"],
                "status": "PASS_RECORDED_BLOCKER_EVIDENCE",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
