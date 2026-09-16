#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "GRF04-V35-Q-QUADRATIC-MAIN-BOUND-REPLACEMENT.json"
CANDIDATE = HERE / "GRF04-MAIN-INDEPENDENT-QUADRATIC-CAPACITY-LP-CANDIDATE.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

LOCKS = {
    "state_blob": "9b460df0b49e70513a13e0ab09aecb8fab375f90",
    "state_canonical": "987e6d33b86170c78a3c9de3bfb0b39875314afb1f129160c8a2dfd97e3eabaa",
    "receipt_blob": "b24731409f33a8e76d3924ee2f651fbfba86b044",
    "receipt_canonical": "c04bf60efdd92f7af245e307167fffffd1d0d4a087a676ded5b01e5110298748",
    "candidate_blob": "1d669114e930951b9d5f9f82a6abb2b59cd43884",
    "candidate_canonical": "3fca63c0d678eb2de2147848a1aa29839618cfd9cb65bdd27d671b28c6e44b01",
    "registry_blob": "f3a884adc1c82aace81cb73d049ff14720ace862",
    "frontier_blob": "4c251be4aa5c355481fe3bcfc71c292fb6389ba4",
    "adapters_blob": "c0ef34e5838e27046a20fed77063593009c56f40",
}
OLD = 3360778813767800658369
NEW = 195603649074545538415
TIGHTENING = 3165175164693255119954
AUDIT_REVIEW = 5217623202
AUDITED_HEAD = "6489e1fb9f35b8ecdc19c982301a816d956711e9"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def locked_json(path: Path, blob: str, canonical: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(git_blob(path) == blob, f"{label} blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == canonical, f"{label} stored canonical drift")
    req(canon(obj) == canonical, f"{label} canonical drift")
    return obj

def main() -> None:
    state = locked_json(STATE, LOCKS["state_blob"], LOCKS["state_canonical"], "MAIN state")
    receipt = locked_json(RECEIPT, LOCKS["receipt_blob"], LOCKS["receipt_canonical"], "replacement receipt")
    candidate = locked_json(CANDIDATE, LOCKS["candidate_blob"], LOCKS["candidate_canonical"], "q candidate")
    req(git_blob(REGISTRY) == LOCKS["registry_blob"], "claim registry drift")
    req(git_blob(FRONTIER) == LOCKS["frontier_blob"], "active frontier drift")
    req(git_blob(ADAPTERS) == LOCKS["adapters_blob"], "lane adapters drift")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V35_Q_QUADRATIC_CONSUMED_REAUDIT_PENDING_FULL178_ACTIVE", "state schema")
    req(state["role"] == "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE", "state role")
    sync = state["authority_sync"]
    req(sync["predecessor_process_head"] == AUDITED_HEAD, "predecessor head")
    req(sync["predecessor_main_state_blob_sha1"] == "ec0243cb998c5c58340100d8151559516c474193", "V34 state blob")
    req(sync["q_quadratic_candidate_hostile_audit_review_id"] == AUDIT_REVIEW, "candidate audit review")
    req(sync["q_quadratic_candidate_hostile_audit_status"] == "PASS", "candidate audit status")
    req(sync["q_quadratic_main_numeric_bound_replacement_consumed"] is True, "candidate not consumed")
    req(sync["q_quadratic_consumption_rule"] == "MIN_OF_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "composition rule")
    req(sync["split_authority"]["orchestration_mode"] == "ROOT_NATIVE_STAGE32_MAIN_ONLY", "orchestration mode")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata authority")
    req(f["predecessor_v34_authoritative_remaining_terminals"] == OLD, "V34 bound")
    req(f["authoritative_remaining_terminals"] == NEW, "V35 bound")
    req(f["v35_q_quadratic_certified_numeric_bound_tightening_vs_v34"] == TIGHTENING, "tightening")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "bound semantics")
    req(f["v35_q_quadratic_exact_incremental_rejected_set_vs_v34_claimed"] is False, "identity-set overclaim")
    req(f["v35_q_quadratic_additive_subtraction_against_v34_performed"] is False, "additive subtraction")
    req(f["v35_q_quadratic_double_charge"] is False, "double charge")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "closure firewall")

    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "replacement audit gate")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "replacement firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall {key}")

    cb = candidate["candidate_bound"]
    req(cb["predecessor_v34_authoritative_upper_bound"] == OLD, "candidate predecessor")
    req(cb["candidate_upper_bound"] == NEW, "candidate bound")
    req(cb["candidate_tightening_vs_v34"] == TIGHTENING, "candidate tightening")
    lp = candidate["capacity_lp_certificate"]
    req(lp["dual_threshold"] == "lambda=29/1357", "dual threshold")
    req(lp["exact_dual_value_numerator"] == 265434151794158295629351, "dual numerator")
    req(lp["exact_dual_value_denominator"] == 1357, "dual denominator")
    req(lp["exact_dual_value_numerator"] // lp["exact_dual_value_denominator"] == NEW, "dual floor")
    req(lp["exact_dual_value_numerator"] % lp["exact_dual_value_denominator"] == 196, "dual remainder")

    req(receipt["status"] == "AUDITED_CANDIDATE_BOUND_CONSUMED__REPLACEMENT_HEAD_PENDING_HOSTILE_REAUDIT", "receipt status")
    req(receipt["consumed_candidate"]["audited_exact_head"] == AUDITED_HEAD, "receipt audited head")
    req(receipt["consumed_candidate"]["hostile_audit_review_id"] == AUDIT_REVIEW, "receipt audit review")
    req(receipt["replacement"]["authority_version"] == "V35", "authority version")
    req(receipt["replacement"]["authoritative_remaining_terminals"] == NEW, "receipt authority")
    req(receipt["replacement"]["tightening_vs_v34"] == TIGHTENING, "receipt tightening")
    req(receipt["replacement"]["composition_rule"] == "MIN_OF_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "receipt composition")
    req(receipt["replacement"]["exact_incremental_rejected_identity_set_claimed"] is False, "receipt identity overclaim")
    req(receipt["replacement"]["additive_subtraction_performed"] is False, "receipt additive subtraction")
    req(receipt["replacement"]["double_charge"] is False, "receipt double charge")
    req(receipt["claim_sync"]["logical_claim_statement_changed"] is False, "claim statement changed")
    req(receipt["claim_sync"]["claim_registry_mutated"] is False, "claim registry mutation")
    req(receipt["claim_sync"]["active_frontier_mutated"] is False, "active frontier mutation")
    req(receipt["claim_sync"]["lane_adapters_mutated"] is False, "lane adapters mutation")
    req(receipt["firewalls"]["replacement_head_hostile_reaudit_required"] is True, "receipt audit gate")
    req(receipt["firewalls"]["merge_authorized"] is False, "merge authorization")

    req(OLD - NEW == TIGHTENING, "authority arithmetic")
    print("PASS: Stage32 V35 consumes hostile-audited q-quadratic bound as numerical MAIN authority")
    print("PASS: replacement head remains fail-closed pending its own hostile reaudit; no additive stacking or identity-set claim")

if __name__ == "__main__":
    main()
