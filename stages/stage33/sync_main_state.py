#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at the exact V77 x-alpha repair frontier."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
R05 = H / "33-05"
OUT = H / "MAIN-STATE.json"
CONTROLLER = H / "controller.json"
V77 = D / "e3-b1-c22-j1-xalpha-kernel-correction-v77.json"
XALPHA = R05 / "xalpha_pair_galois_repair.py"

CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
CONTROLLER_SHA = "18d8aa4e0ab7a946f5ae5205de2cfddc4b55f867338e92242e5db7cac6f87554"
STATE_SHA = "f13dca2b0e254eb1b8e5a4c72b495886718e019167b87bf4d5a2a7452f3cee37"
V77_SHA = "d2f803ab0cb394389c1fedf8f94e237ce82702743d0240a4f4b2fe73a44d5e98"
V77_BLOB = "bfc54650fdc7885664cdfcb1533cb9a1e711c5a5"
XALPHA_BLOB = "b7f37df50a123ef6c972aa210e7efb5f16535f76"


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
    cb = dict(controller)
    claimed_controller = cb.pop("projection_canonical_sha256")
    assert controller["schema"] == CONTROLLER_SCHEMA
    assert claimed_controller == CONTROLLER_SHA == hashlib.sha256(
        json.dumps(cb, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert controller["merge_allowed"] is False
    assert controller["execution"]["merge_allowed"] is False

    assert blob_sha(V77) == V77_BLOB
    assert blob_sha(XALPHA) == XALPHA_BLOB
    v77 = json.loads(V77.read_text(encoding="utf-8"))
    assert v77["canonical_sha256"] == V77_SHA == csha(v77)
    assert v77["cohomological_correction"]["J1_geometric_brauer_class"] == "ZERO"
    assert v77["supersession"]["v65_J1_candidates_u2_u1plusu2_valid_for_actual_Brauer_OS_class"] is False
    assert v77["proper14_boundary"]["column3_marked_coordinate_materialized"] is False

    state = json.loads(OUT.read_text(encoding="utf-8"))
    assert state["canonical_sha256"] == STATE_SHA == csha(state)
    assert state["controller_projection_canonical_sha256"] == CONTROLLER_SHA
    assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V25_V77_J1_XALPHA_ZERO_COLUMN3_REPAIR_ACTIVE"
    assert state["authority_sync"]["frontier_authority"] == "V77_J1_XALPHA_KERNEL_CORRECTION"
    assert state["branch_exact_frontier_authority"].endswith("e3-b1-c22-j1-xalpha-kernel-correction-v77.json")
    assert state["current"]["active_missing_interface"] == "LAMBDA_A_LITERAL_TO_PROPER14_BRAUER_BINDING_AFTER_J1_XALPHA_ZERO"
    assert state["current_exact_frontier"]["j1_E2_cocycle_nonzero"] is True
    assert state["current_exact_frontier"]["j1_H1_E_class"] == "ZERO"
    assert state["current_exact_frontier"]["j1_geometric_brauer_os_class"] == "ZERO"
    assert state["current_exact_frontier"]["j1_twisted_kernel_minimum_norm"] == 4
    assert state["current_exact_frontier"]["j1_minimum_norm_4_selects_u2"] is False
    assert state["current_exact_frontier"]["J1_marked_kc_candidate_gate_applicable"] is False
    assert state["current_exact_frontier"]["e3_b1_column3_marked_coordinate_materialized"] is False
    assert state["resolved_investigations"]["j1_xalpha_kernel"].startswith("CLOSED_EXACT_V77")
    assert state["execution_gate"]["advance_allowed"] is True
    assert state["firewalls"]["merge_allowed"] is False
    assert state["stage33_progress"] == "6/11"

    if not args.check:
        # Normalize formatting without changing the exact state payload.
        OUT.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")

    print(json.dumps({
        "success": True,
        "mode": "check" if args.check else "write",
        "canonical_sha256": STATE_SHA,
        "frontier": state["authority_sync"]["frontier_authority"],
        "current_leaf": state["current"]["active_missing_interface"],
        "j1_geometric_brauer_os_class": "ZERO",
        "advance_allowed": True,
        "merge_allowed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
