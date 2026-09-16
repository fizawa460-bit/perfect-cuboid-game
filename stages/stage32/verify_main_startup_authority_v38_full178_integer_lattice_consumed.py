#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
RECEIPT = HERE / "management/grf04-quadratic-capacity/GRF04-V38-TD02-FULL178-INTEGER-LATTICE-MAIN-BOUND-REPLACEMENT.json"

NEW = 195414091250828468192
TIGHTENING = 189557823717070223
RECEIPT_BLOB = "f959b922129354f58c2fd0e1b182d723bfa174e2"
RECEIPT_CANON = "8adf31a03c6c1fd6538e25c50deb059b843d34cfaf174bc2993f078b4657a08b"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    stored = state.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(state) == stored, "MAIN state canonical drift")

    req(blob(RECEIPT) == RECEIPT_BLOB, "V38 receipt blob drift")
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    req(receipt.get("canonical_sha256_without_this_field") == RECEIPT_CANON and
        canon(receipt) == RECEIPT_CANON, "V38 receipt canonical drift")

    req(state["schema"] ==
        "STAGE32_MAIN_COMPACT_STATE_V38_FULL178_INTEGER_LATTICE_BOUND_CONSUMED_REAUDIT_PENDING",
        "state schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata authority")
    req(f["authoritative_remaining_terminals"] == NEW, "V38 numerical authority")
    req(f["v38_td02_full178_certified_numeric_bound_tightening_vs_v37"] == TIGHTENING,
        "V38 tightening")
    req(f["live_178_td02_main_credit_consumed"] is True, "178 bound not consumed")
    req(f["full178_numerical_census_complete"] is False, "FULL178 census overclaim")
    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED",
        "hostile-reaudit gate")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True,
        "replacement reaudit firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete",
                "merge_authorized", "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "receiver_credit", "route_credit",
                "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall {key}")

    req(receipt["replacement"]["authoritative_remaining_terminals"] == NEW,
        "receipt V38 bound")
    req(receipt["replacement"]["composition_rule"] ==
        "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING",
        "receipt composition")
    req(receipt["firewalls"]["replacement_head_hostile_reaudit_required"] is True,
        "receipt hostile-reaudit gate")

    print("PASS: Stage32 MAIN V38 numerical authority is the consumed TD02 FULL178 integer-lattice upper bound")
    print("PASS: replacement exact head remains fail-closed pending independent hostile reaudit")


if __name__ == "__main__":
    main()
