#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = HERE / "post1500-common-cover-marked-branch-geometry-certificate.json"
SOURCE_NOTE_PATH = HERE / "post1500-hostile-audit-rosati-trace-repair-source-note.md"
CONTROLLER_PATH = ROOT / "stages/stage32/controller.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))

    require(cert["schema_version"] == 1, "schema_version")
    require(cert["stage"] == 32, "stage")
    require(cert["base_pr"] == 1500, "base_pr")
    require(cert["status"] == "AUDITED_NEGATIVE", "status")
    require(SOURCE_NOTE_PATH.is_file(), "missing admitted source note")
    require(CONTROLLER_PATH.is_file(), "missing Stage32 controller")

    before = cert["authority_before"]
    after = cert["authority_after"]
    expected_authority = {
        "checkpoint": "O211",
        "sigma_gamma": 1204,
        "q_total": 602,
        "o212_plus_authorized": False,
    }
    require(before == after, "negative audit must not promote authority")
    require(after == expected_authority, "unexpected authority state")
    require(
        cert["target"] == {"sigma_gamma": "<1204", "q_total": "<602"},
        "unexpected strict-improvement target",
    )

    result = cert["result"]
    require(
        result["strict_sigma_improvement_certified"] is False,
        "sigma authority was promoted",
    )
    require(
        result["strict_q_improvement_certified"] is False,
        "Q authority was promoted",
    )

    constraints = cert["already_audited_compatible_constraints"]
    pair = constraints["pair_operator_bound"]
    require(pair["degrees"] == [105, 81], "pair degrees")
    require(pair["combined_upper_bound"] == 376, "pair operator upper bound")
    require(
        constraints["weierstrass"] == {"W": 128, "p_lower_bound": 32},
        "Weierstrass record",
    )
    require(len(cert["required_new_evidence"]) == 3, "re-entry evidence count")
    require(len(cert["anti_loop"]) >= 2, "anti-loop rules")

    print(
        "PASS: post1500 common-cover/marked-branch geometry is "
        "AUDITED_NEGATIVE; O211 authority unchanged"
    )


if __name__ == "__main__":
    main()
