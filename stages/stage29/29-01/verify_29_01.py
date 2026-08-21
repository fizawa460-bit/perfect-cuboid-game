#!/usr/bin/env python3
"""Consistency verifier for audited Stage29-01."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def main() -> None:
    result = read("stages/stage29/29-01/result.md")
    audit = read("stages/stage29/29-01/audit.md")
    controller = json.loads(read("stages/stage29/controller.json"))
    roadmap = read("docs/stage16-29-population-roadmap.md")
    num_md = read("docs/stage14-num-reuse-index.md")
    num_json = json.loads(read("docs/stage14-num-reuse-index.json"))
    stage28 = json.loads(read("stages/stage28/28-controller.json"))

    require(result, "AUDIT_VERDICT=PASS", "result")
    require(result, "P(B)=0 for B<=500000000", "result")
    require(result, "EVIDENCE=EXACT_FINITE_CENSUS", "result")
    require(result, "does not imply perfect-cuboid nonexistence", "result")
    require(result, "NEXT_EXPECTED_COMMAND=Stage29-main-batch", "result")

    require(audit, "AUDIT_VERDICT=PASS", "audit")
    require(audit, "Shared-roadmap backward compatibility", "audit")
    require(audit, "Numerical reuse routing", "audit")

    assert controller["stage"] == "Stage29"
    assert controller["status"] == "29_01_AUDITED_PASS"
    assert controller["audit_status"] == "PASS"
    assert controller["merge_allowed"] is True
    assert controller["advance_allowed"] is True
    assert controller["certified_population_surface"]["P_finite_zero_through_B"] == 500000000
    assert controller["certified_population_surface"]["P_global_zero_theorem"] is False
    assert controller["next_expected_command"] == "Stage29-main-batch"

    require(roadmap, "Stage16-28 Stage70 policy remains active", "roadmap")
    require(roadmap, "## Stage20 literature reuse rule", "roadmap")
    require(roadmap, "## Stage19 carry-over", "roadmap")
    require(roadmap, "Stage29 is the explicit exception", "roadmap")

    require(num_md, "| 29 | Endpoint finite regression / negative control only", "num-md")
    require(num_md, "`T=0` through `B=500,000,000` is bounded evidence only", "num-md")
    assert "Stage29" in next(a for a in num_json["assets"] if a["id"] == "NUM-R01")["targets"]
    assert num_json["stage29_policy"]["finite_zero_global_nonexistence_forbidden"] is True

    assert stage28["status"] == "CLOSED_AUDITED_PASS_MERGED"
    assert stage28["checkpoint_status"]["70"] == "AUDITED_PASS_MERGED"

    print("Stage29-01 audited consistency: PASS")


if __name__ == "__main__":
    main()
