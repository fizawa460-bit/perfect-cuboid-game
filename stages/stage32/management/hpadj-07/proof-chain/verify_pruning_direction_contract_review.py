#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESULT = HERE / "PRUNING-DIRECTION-CONTRACT-REVIEW.json"
ROADMAP = ROOT / "stages/stage32/ROADMAP.md"
ROUTE = ROOT / "stages/stage29/29-02c-LG2/route-contract.json"
CORRECTED = HERE / "GENERAL-TYPE-ADJUNCTION-CORRECTION.json"

EXPECTED_RESULT_CANON = "3c6ace29e475f781e6db5a5859578b88b91179a46637c97551391782e85d3e87"
EXPECTED_ROADMAP_BLOB = "15526ac6012b2dc383dcfc186784340fe1569be7"
EXPECTED_ROUTE_BLOB = "99752985fd705ee993d052e5bcc622181c7a4cbc"
EXPECTED_CORRECTED_BLOB = "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e"
EXPECTED_CORRECTED_CANON = "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa"


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    req(git_blob(ROADMAP) == EXPECTED_ROADMAP_BLOB, "Stage32 ROADMAP blob drift")
    req(git_blob(ROUTE) == EXPECTED_ROUTE_BLOB, "Stage29 route-contract blob drift")
    req(git_blob(CORRECTED) == EXPECTED_CORRECTED_BLOB, "corrected HPADJ blob drift")

    roadmap = ROADMAP.read_text(encoding="utf-8")
    req("R29-LG2" in roadmap, "R29-LG2 roadmap target missing")
    req(
        "produce a complete orbit list of every numerical Picard class satisfying the audited necessary conditions"
        in roadmap,
        "32-01 close criterion drift",
    )
    req("Effectivity is intentionally **not** credited here." in roadmap, "32-01 effectivity firewall drift")

    route = json.loads(ROUTE.read_text(encoding="utf-8"))
    req(any(x.startswith("R29-LG2 ") for x in route["receivers"]), "R29-LG2 receiver missing")
    req(any(x.startswith("R29-LG2-EFF ") for x in route["receivers"]), "R29-LG2-EFF receiver missing")
    req(route["verdicts"]["effectivity_certified"] is False, "effectivity receiver already closed unexpectedly")

    corrected = json.loads(CORRECTED.read_text(encoding="utf-8"))
    req(corrected["canonical_sha256_without_this_field"] == EXPECTED_CORRECTED_CANON, "corrected stored canonical")
    req(canonical(corrected) == EXPECTED_CORRECTED_CANON, "corrected canonical drift")
    req(corrected["firewalls"]["main_pruning_credit"] is False, "corrected result prematurely promoted")

    result = json.loads(RESULT.read_text(encoding="utf-8"))
    req(result["canonical_sha256_without_this_field"] == EXPECTED_RESULT_CANON, "result stored canonical")
    req(canonical(result) == EXPECTED_RESULT_CANON, "result canonical drift")
    req(
        result["status"]
        == "CANDIDATE_CONTRACT_CORRECTION_REVERSE_REALIZATION_NOT_REQUIRED_FOR_32_01_NECESSARY_FILTER_PRUNING",
        "result status",
    )
    logic = result["logic"]
    req(
        logic["necessary_condition_direction"] == "ACTUAL_TARGET_CARRIER -> CORRECTED_HPADJ_CONDITION",
        "necessary-condition direction",
    )
    req(
        logic["contrapositive"]
        == "CORRECTED_HPADJ_REJECTED_TERMINAL -> NO_ACTUAL_TARGET_CARRIER_WITH_THAT_TERMINAL",
        "contrapositive",
    )
    req(
        logic["reverse_realization_role"]
        == "A/B/C reverse realization is relevant to positive existence/effectivity claims or R29-LG2-EFF, not to a one-way necessary-condition pruning of R29-LG2.",
        "reverse-realization role",
    )
    req(result["does_not_claim"]["effectivity"] is True, "effectivity nonclaim")
    req(result["does_not_claim"]["integral_irreducible_existence"] is True, "existence nonclaim")
    req(result["does_not_claim"]["receiver_discharge"] is True, "receiver nonclaim")
    for key, value in result["firewalls"].items():
        req(value is False, f"credit/firewall unexpectedly true: {key}")

    print(
        "PASS hpadj07 pruning-direction contract; R29-LG2 necessary-filter pruning "
        "does not require reverse A/B/C realization; no MAIN/effectivity/receiver credit"
    )


if __name__ == "__main__":
    main()
