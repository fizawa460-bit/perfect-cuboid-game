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

ROUTING_BLOB = "5e46668259fd6b162c7da43ee4dc21ede81ea158"
ROUTING_CANON = "33a5053eea96c9ed9aa3e66b82b6c0a5f596cc2f1731cb34442f2f1dd898540b"
V36_BLOB = "c5418f9ed2813f0a38b2342fd31e4f3ce23a017a"
V36_CANON = "b30400705423b2c3c060f58ae9085d9442fc07c88dddad10ffa27e1f41c0ff59"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

BOUND = 195603649074545538415
FULL178_CANDIDATE = 195414091250828468192
FULL178_AUDIT_REVIEW = 5218209619
FULL178_AUDITED_HEAD = "640195f158e2fa953ebd669820a794a56cef04fb"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(p: Path) -> str:
    b = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def lock_json(p: Path, b: str, c: str, label: str) -> dict:
    req(p.is_file(), f"missing {label}")
    req(blob(p) == b, f"{label} blob drift")
    o = json.loads(p.read_text(encoding="utf-8"))
    req(o.get("canonical_sha256_without_this_field") == c, f"{label} stored canonical drift")
    req(canon(o) == c, f"{label} canonical drift")
    return o


def mutable_state() -> dict:
    req(STATE.is_file(), "missing current MAIN state")
    o = json.loads(STATE.read_text(encoding="utf-8"))
    stored = o.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(o) == stored, "current MAIN state canonical drift")
    return o


def main() -> None:
    st = mutable_state()
    route = lock_json(ROUTING, ROUTING_BLOB, ROUTING_CANON, "historical V37 routing receipt")
    v36 = lock_json(V36, V36_BLOB, V36_CANON, "V36 audit sync receipt")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    # Historical V37 routing receipt remains immutable evidence for the transition
    # that originally routed the bounded signal to 32-01-178.
    req(v36["sync"]["authoritative_remaining_terminals"] == BOUND, "V36 predecessor authority")
    req(v36["sync"]["additional_pruning"] == 0, "V36 sync pruning")
    req(route["status"] == "AUDITED_BOUNDED_SIGNAL_ROUTED__FULL178_SCALEOUT_PENDING__ZERO_NEW_MAIN_CREDIT",
        "historical routing status")
    p = route["producer_178"]
    req(p["bounded_scope"] == "d<=32", "historical bounded scope")
    req(p["bounded_capacity_hostile_audit_status"] == "PASS", "historical bounded audit")
    req(p["main_handoff_ready"] is False and p["main_credit"] is False,
        "historical bounded result silently promoted")

    # MAIN-STATE is intentionally mutable operational projection. Do not freeze its
    # whole-file blob: live specialist observations are refreshed by stage32mainbatch.
    # Fail closed on the mathematical authority/firewalls instead.
    req(st["schema"] == "STAGE32_MAIN_COMPACT_STATE_V37_FULL178_INTEGER_LATTICE_ROUTED_WAIT",
        "state schema")
    req(st["authority_sync"]["q_quadratic_consumption_rule"] ==
        "MIN_OF_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING", "composition rule")
    req(st["authority_sync"]["v37_routing_additional_pruning"] == 0, "routing added pruning")
    f = st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata authority changed")
    req(f["authoritative_remaining_terminals"] == BOUND, "MAIN numerical authority changed")
    req(f["live_178_td02_full178_capacity_hostile_audited"] is True, "FULL178 audit observation missing")
    req(f["live_178_td02_full178_capacity_audit_review_id"] == FULL178_AUDIT_REVIEW,
        "FULL178 audit review drift")
    req(f["live_178_td02_full178_capacity_audited_exact_head"] == FULL178_AUDITED_HEAD,
        "FULL178 audited head drift")
    req(f["live_178_td02_full178_candidate_upper_bound"] == FULL178_CANDIDATE,
        "FULL178 candidate drift")
    req(f["live_178_td02_v37_sync_complete"] is True, "V37 specialist sync not recorded")
    req(f["live_178_td02_postsync_replay_success"] is True, "post-sync replay not recorded")
    req(f["live_178_td02_producer_ready_for_main_reentry"] is True, "MAIN re-entry not recorded")
    req(f["live_178_td02_main_handoff_ready"] is True, "handoff-ready observation missing")
    req(f["live_178_td02_main_credit_consumed"] is False, "FULL178 candidate silently consumed")

    req(st["current"]["mainbatch_stop_gate"] ==
        "SPECIALIST_178_FULL178_V37_SYNCED_REPLAY_PASS__MAIN_MIN_COMPOSITION_DECISION_PENDING",
        "MAIN stop gate")
    req(st["current"]["next_exact_route"] ==
        "MAIN_EVALUATE_178_TD02_FULL178_V37_SYNC_HANDOFF_UNDER_MIN_COMPOSITION",
        "MAIN next route")

    for key in ("effectivity_released", "endpoint_credit", "full178_complete", "merge_authorized",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "receiver_credit", "route_credit", "stage32_closed", "theorem_credit"):
        req(st["firewalls"][key] is False, f"firewall {key}")

    sweep = st["source_locks"]["live_specialist_sweep"]
    for key in ("lane_178_head", "lane_178_handoff", "ex5_head", "ex5_handoff",
                "cut_handoff", "mb_head", "mb_handoff"):
        req(key in sweep, f"missing live specialist observation {key}")

    cs = route["claim_sync"]
    req(cs["logical_claim_statement_changed"] is False, "historical logical claim changed")
    req(cs["claim_registry_mutated"] is False and cs["active_frontier_mutated"] is False
        and cs["lane_adapters_mutated"] is False, "historical claim routing mutation")

    print("PASS: historical V37 routing evidence retained and current MAIN projection canonical")
    print("PASS: FULL178 V37-synced handoff observed; MAIN authority unchanged pending MIN-composition decision")


if __name__ == "__main__":
    main()
