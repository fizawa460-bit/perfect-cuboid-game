#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
ROUTING = HERE / "GRF04-V37-FULL178-INTEGER-LATTICE-ROUTING.json"
V36 = HERE / "GRF04-V36-Q-QUADRATIC-AUDIT-SYNC.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

STATE_BLOB = "3abc129c319b48d90ff42be2e1e4a23e552bf4a4"
STATE_CANON = "3b75bf45e1129667345f41ccaedbc92847ac215b352722dffb30502aa9fc8f98"
ROUTING_BLOB = "5e46668259fd6b162c7da43ee4dc21ede81ea158"
ROUTING_CANON = "33a5053eea96c9ed9aa3e66b82b6c0a5f596cc2f1731cb34442f2f1dd898540b"
V36_BLOB = "c5418f9ed2813f0a38b2342fd31e4f3ce23a017a"
V36_CANON = "b30400705423b2c3c060f58ae9085d9442fc07c88dddad10ffa27e1f41c0ff59"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

BOUND = 195603649074545538415
BOUNDED_AUDIT_REVIEW = 5217996434
BOUNDED_178_HEAD = "23e53bfd145b722640481e34458fb689326e486a"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(p: Path) -> str:
    b = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def lock_json(p: Path, b: str, c: str, label: str) -> dict:
    req(p.is_file(), f"missing {label}")
    req(blob(p) == b, f"{label} blob drift")
    o = json.loads(p.read_text(encoding="utf-8"))
    req(o.get("canonical_sha256_without_this_field") == c, f"{label} stored canonical drift")
    req(canon(o) == c, f"{label} canonical drift")
    return o

def main() -> None:
    st = lock_json(STATE, STATE_BLOB, STATE_CANON, "V37 MAIN state")
    route = lock_json(ROUTING, ROUTING_BLOB, ROUTING_CANON, "V37 routing receipt")
    v36 = lock_json(V36, V36_BLOB, V36_CANON, "V36 audit sync receipt")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    req(v36["sync"]["authoritative_remaining_terminals"] == BOUND, "V36 predecessor authority")
    req(v36["sync"]["additional_pruning"] == 0, "V36 sync pruning")

    req(route["status"] == "AUDITED_BOUNDED_SIGNAL_ROUTED__FULL178_SCALEOUT_PENDING__ZERO_NEW_MAIN_CREDIT",
        "routing status")
    p = route["producer_178"]
    req(p["live_head"] == BOUNDED_178_HEAD, "178 audited bounded head")
    req(p["bounded_scope"] == "d<=32", "bounded scope")
    req(p["bounded_capacity_hostile_audit_status"] == "PASS", "bounded audit status")
    req(p["bounded_capacity_hostile_audit_review_id"] == BOUNDED_AUDIT_REVIEW, "bounded audit review")
    req(p["bounded_real_lp_floor"] == 398251814964, "bounded real LP")
    req(p["bounded_integer_lattice_lp_floor"] == 394813297087, "bounded integer LP")
    req(p["bounded_floor_improvement"] == 3438517877, "bounded improvement")
    req(p["pointwise_weakened_cells"] == 0, "bounded pointwise weakening")
    req(p["full178_integer_lattice_capacity_scaleout_run"] is False, "FULL178 scaleout silently run")
    req(p["full178_integer_lattice_capacity_audited"] is False, "FULL178 scaleout silently audited")
    req(p["main_handoff_ready"] is False and p["main_credit"] is False, "178 bounded result silently promoted")

    r = route["routing"]
    req(r["owner"] == "32-01-178", "route owner")
    req(r["next_specialist_route"] == "TD02-INTEGER-LATTICE-CAPACITY-FULL178-SCALEOUT", "next 178 route")
    req(r["main_same_route_duplicate_census_forbidden"] is True, "duplicate census firewall")
    req(r["bounded_ratio_global_extrapolation_forbidden"] is True, "bounded/global firewall")
    req(r["current_main_authority_unchanged_until_audited_full178_handoff"] is True, "authority hold")
    req(route["informational_only"]["hypothetical_scaling_is_not_credit_and_not_a_prediction"] is True,
        "hypothetical scaling firewall")

    ex = route["ex5_observation"]
    req(ex["live_head"] == "dbd3a191bfdd33c3413a2abc41331feb651f0830", "EX5 live head")
    req(ex["hpadj18_retained_numeric_result_frozen"] is False, "HPADJ18 result silently frozen")
    req(ex["hpadj18_hostile_audited"] is False, "HPADJ18 silently audited")
    req(ex["hpadj18_main_handoff_ready"] is False and ex["main_credit"] is False, "HPADJ18 silently promoted")
    req(ex["latest_audited_hpadj13_is_stronger_than_current_main"] is False, "HPADJ13 dominance")

    req(st["schema"] == "STAGE32_MAIN_COMPACT_STATE_V37_FULL178_INTEGER_LATTICE_ROUTED_WAIT", "state schema")
    req(st["authority_sync"]["v37_routing_additional_pruning"] == 0, "routing added pruning")
    req(st["current_exact_frontier"]["authoritative_remaining_terminals"] == BOUND, "MAIN authority changed")
    req(st["current_exact_frontier"]["live_178_td02_bounded_capacity_hostile_audited"] is True,
        "bounded audit not synchronized")
    req(st["current_exact_frontier"]["live_178_td02_bounded_capacity_audit_review_id"] == BOUNDED_AUDIT_REVIEW,
        "bounded audit review state")
    req(st["current_exact_frontier"]["live_178_td02_main_handoff_ready"] is False, "178 handoff silently ready")
    req(st["current_exact_frontier"]["live_ex5_q_quadratic_refinement_main_handoff_ready"] is False,
        "EX5 handoff silently ready")
    req(st["current"]["mainbatch_stop_gate"] == "SPECIALIST_178_FULL178_INTEGER_LATTICE_SCALEOUT_PENDING",
        "MAIN routing gate")
    req(st["current"]["next_exact_route"] == "178_TD02_INTEGER_LATTICE_FULL178_SCALEOUT_THEN_AUDITED_MAIN_HANDOFF",
        "MAIN next route")

    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(st["firewalls"][key] is False, f"firewall {key}")

    cs = route["claim_sync"]
    req(cs["logical_claim_statement_changed"] is False, "logical claim changed")
    req(cs["claim_registry_mutated"] is False and cs["active_frontier_mutated"] is False
        and cs["lane_adapters_mutated"] is False, "claim routing mutation")

    print("PASS: Stage32 V37 routes the hostile-audited d<=32 integer-lattice signal to the 178 FULL178 owner")
    print("PASS: numerical MAIN authority unchanged; bounded/global extrapolation and same-route duplicate census remain forbidden")

if __name__ == "__main__":
    main()
