#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
WALL = HERE / "CARRIER-REALIZATION-WALL.json"
EXPECTED_WALL_CANON = "79598cf3649be2d86771ea9f90d748a51028d348c672dc258424db025a39b303"

LOCKS = {
    "historical_hpadj06": (
        "stages/stage32/management/hpadj-06/CARRIER-ADAPTER.json",
        "2f8d51dd4c52cf9189b829d0cd42679ef110cef9",
        "72144be89761ba82f93fd33ca7647c90a4ba12646d5f63e70537a955d93f106d",
    ),
    "general_type_correction": (
        "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json",
        "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e",
        "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa",
    ),
    "pruning_direction": (
        "stages/stage32/management/hpadj-07/proof-chain/PRUNING-DIRECTION-CONTRACT-REVIEW.json",
        "bd1beddf25b505c9f6c7e163606e6156dca10346",
        "3c6ace29e475f781e6db5a5859578b88b91179a46637c97551391782e85d3e87",
    ),
    "current_v23_rebase": (
        "stages/stage32/management/hpadj-07/proof-chain/CURRENT-V23-CONSERVATIVE-REBASE.json",
        "8883cfc59a6d48e34d7e256fad15e69714dc02d1",
        "9ae15dd70a3ba84fe83d2d11dfa8e1081c44a8b06e68b78dda4f871aa0f00e01",
    ),
}
ROUTE_PATH = "stages/stage29/29-02c-LG2/route-contract.json"
ROUTE_BLOB = "99752985fd705ee993d052e5bcc622181c7a4cbc"


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


def locked_json(rel: str, blob: str, canon: str | None = None) -> dict:
    path = ROOT / rel
    req(path.is_file(), f"missing source {rel}")
    req(git_blob(path) == blob, f"blob drift {rel}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == canon, f"stored canonical drift {rel}")
        req(canonical(obj) == canon, f"canonical drift {rel}")
    return obj


def main() -> None:
    wall = json.loads(WALL.read_text(encoding="utf-8"))
    req(
        wall.get("schema") == "STAGE32_MAIN_HPADJ07_CARRIER_REALIZATION_WALL_V2_GENERAL_TYPE_SUPERSESSION",
        "wall schema",
    )
    req(wall.get("canonical_sha256_without_this_field") == EXPECTED_WALL_CANON, "wall stored canonical")
    req(canonical(wall) == EXPECTED_WALL_CANON, "wall canonical")

    audit = wall["audit_repair_boundary"]
    req(audit["failed_exact_head"] == "d7b9b06ad8d162304ac52310cbb20ef8363fc3cd", "failed-head lock")
    req(audit["hostile_audit_review_id"] == 5190972957, "FAIL review lock")
    req(audit["hostile_audit_status"] == "FAIL", "FAIL status lock")
    req(audit["repair_required"] is True, "repair-required lock")
    req(audit["merge_authorized"] is False, "merge firewall")

    src = {name: locked_json(*spec) for name, spec in LOCKS.items()}
    route = locked_json(ROUTE_PATH, ROUTE_BLOB)

    old = src["historical_hpadj06"]
    req(
        old["proved_direction"]["step_5_adjunction_contradiction"]
        == "an integral irreducible curve on the K3 carrier surface satisfies C^2 >= -2, so an HPADJ-rejected matching terminal cannot be realized by such a carrier",
        "historical HPADJ06 claim identity",
    )
    req(
        old["proved_direction"]["contrapositive"]
        == "HPADJ_REJECTED_TERMINAL -> NO_ACTUAL_MATCHING_INTEGRAL_IRREDUCIBLE_K3_CARRIER",
        "historical K3 contrapositive identity",
    )

    corrected = src["general_type_correction"]
    superseded = corrected["supersedes_for_mathematical_use"]
    req(
        "stages/stage32/management/hpadj-06/CARRIER-ADAPTER.json proved_direction.step_5_adjunction_contradiction"
        in superseded,
        "HPADJ06 supersession missing",
    )
    req(
        "stages/stage32/management/hpadj-01/RESULT.json necessary_condition.irreducible_k3_adjunction"
        in superseded,
        "HPADJ01 K3-threshold supersession missing",
    )
    c = corrected["corrected_general_type_adjunction"]
    req(c["g0_lower_bound"] == "C^2>=-d-2", "g0 corrected adjunction")
    req(c["g1_lower_bound"] == "C^2>=-d", "g1 corrected adjunction")
    req(
        c["g0_group_cauchy_rejection"] == "8*a^2+8*b^2+6*c^2>3*d^2+48*d+96",
        "g0 corrected rejection",
    )
    req(
        c["g1_group_cauchy_rejection"] == "8*a^2+8*b^2+6*c^2>3*d^2+48*d",
        "g1 corrected rejection",
    )
    req(corrected["firewalls"]["main_pruning_credit"] is False, "correction premature credit")

    direction = src["pruning_direction"]
    logic = direction["logic"]
    req(
        logic["necessary_condition_direction"] == "ACTUAL_TARGET_CARRIER -> CORRECTED_HPADJ_CONDITION",
        "necessary-condition direction",
    )
    req(
        logic["contrapositive"]
        == "CORRECTED_HPADJ_REJECTED_TERMINAL -> NO_ACTUAL_TARGET_CARRIER_WITH_THAT_TERMINAL",
        "corrected contrapositive",
    )
    req(
        logic["reverse_realization_not_needed"].startswith("It is not necessary to prove"),
        "reverse-realization pruning contract",
    )
    req(direction["firewalls"]["main_pruning_credit"] is False, "direction premature credit")

    rebase = src["current_v23_rebase"]
    rb = rebase["set_theoretic_rebase"]
    req(rb["v22_to_v23_total_removed"] == 154697, "V22->V23 removal")
    req(rb["therefore_current_v23_hpadj_rejected_lower_bound"] == 20713268924714183560113,
        "current V23 corrected lower bound")
    req(rb["candidate_remaining_upper_bound_if_corrected_hpadj_promoted"] == 26876434389242951089388,
        "current V23 remaining upper bound")
    req(rebase["firewalls"]["main_pruning_credit"] is False, "rebase premature credit")

    receivers = route["receivers"]
    req(any(x.startswith("R29-LG2 ") for x in receivers), "R29-LG2 receiver missing")
    req(any(x.startswith("R29-LG2-EFF ") for x in receivers), "R29-LG2-EFF receiver missing")
    req(route["verdicts"]["effectivity_certified"] is False, "effectivity remains separate")

    active = wall["active_path"]
    req(active["terminal_to_picard64_population_identity"] is True, "terminal/Picard64 interface")
    req(active["historical_k3_adjunction_claim_active"] is False, "old K3 claim must be retired")
    req(active["historical_hpadj06_carrier_exclusion_active"] is False, "old HPADJ06 exclusion must be retired")
    req(active["historical_hpadj01_k3_threshold_active"] is False, "old HPADJ01 K3 threshold must be retired")
    req(active["corrected_general_type_adjunction_active"] is True, "corrected adjunction active")
    req(active["corrected_necessary_filter_candidate_active"] is True, "corrected filter active")
    req(active["necessary_condition_direction"] == logic["necessary_condition_direction"], "active direction mismatch")
    req(active["contrapositive"] == logic["contrapositive"], "active contrapositive mismatch")
    req(active["reverse_realization_required_for_32_01_pruning"] is False, "reverse realization wrongly active")

    for claim in wall["superseded_claims"]:
        req(claim["active_credit"] is False, "superseded claim retained active credit")

    cm = wall["corrected_mathematics"]
    req(cm["corrected_v22_candidate_rejected_lower_bound"] == 20713268924714183714810, "V22 corrected count")
    req(cm["current_v23_conservative_rejected_lower_bound"] == 20713268924714183560113, "V23 corrected count")
    req(cm["current_v23_candidate_remaining_upper_bound_if_promoted"] == 26876434389242951089388,
        "V23 remaining upper bound")

    reverse = wall["reverse_realization_chain"]
    req(reverse["status"] == "NOT_A_PREREQUISITE_FOR_32_01_NECESSARY_FILTER_PRUNING", "reverse-chain status")
    req(reverse["retained_for_positive_existence_or_effectivity_routes"] is True, "positive-route retention")
    req(reverse["effectivity_receiver"] == "R29-LG2-EFF", "effectivity receiver")
    req(reverse["no_positive_realization_credit_from_this_repair"] is True, "positive-credit firewall")

    promotion = wall["promotion_gate"]
    req(promotion["corrected_proof_chain_exact_head_ci_required"] is True, "CI gate")
    req(promotion["replacement_head_hostile_reaudit_required"] is True, "reaudit gate")
    req(promotion["explicit_main_consumption_required"] is True, "consumption gate")
    req(promotion["main_authority_mutation_allowed_now"] is False, "authority mutation firewall")

    for key, value in wall["firewalls"].items():
        req(value is False, f"credit/firewall unexpectedly true: {key}")

    print(
        "PASS hpadj07 general-type supersession wall; old K3 HPADJ path retired; "
        "corrected candidate remains zero-credit pending replacement-head hostile re-audit"
    )


if __name__ == "__main__":
    main()
