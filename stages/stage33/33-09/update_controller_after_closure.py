#!/usr/bin/env python3
"""Apply the deterministic controller transition after exact Stage33-09 closure."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTROLLER = HERE.parent / "controller.json"
CLOSURE = HERE / "stage33-09-closure.json"

ctl = json.loads(CONTROLLER.read_text(encoding="utf-8"))
close = json.loads(CLOSURE.read_text(encoding="utf-8"))
if ctl["schema"] != "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V22_PARALLEL_ADAPTIVE_REPAIR_MINIMAPS":
    raise SystemExit("controller schema moved")
if not all(close["exit_condition"].values()) or not close["stage33_10_released"]:
    raise SystemExit("Stage33-09 closure certificate is not releasing Stage33-10")
if ctl["stage33_progress"] != "6/11" or ctl["stage33_07"]["unit_closed"] or ctl["stage33_08_released"]:
    raise SystemExit("parent/downstream firewall moved before Stage33-09 controller transition")

children = {x["id"]: x for x in ctl["repair_children"]}
if children["33-09"]["name"] != "PICARD-EQUIVARIANT-TRANSPORT":
    raise SystemExit("33-09 repair-child identity moved")
if children["33-10"]["name"] != "ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER":
    raise SystemExit("33-10 repair-child identity moved")

children["33-09"].update({
    "status": "CLOSED_EXACT",
    "closure_certificate": "stages/stage33/33-09/stage33-09-closure.json",
    "closure_certificate_sha256": close["canonical_sha256"],
    "historical_retained_picard_marking_bridge_certified": True,
    "named_integral_and_two_torsion_actions_source_locked": True,
    "picard_equivariant_transport_closed": True,
})
children["33-10"]["status"] = "OPEN_RELEASED_BY_33_09"
ctl["stage33_07"]["historical_q256_marked_bridge_certified"] = True
ctl["stage33_07"]["picard_equivariant_transport_closed"] = True
ctl["stage33_07"]["stage33_09_closure_certificate_sha256"] = close["canonical_sha256"]
ctl["status"] = "STAGE33_01_TO_06_AUDITED_CLOSED_33_07_REPAIR_33_09_CLOSED_33_10_OPEN_33_08_BLOCKED"
ctl["current_item"] = "Stage33-10_ABSOLUTE_H1_AND_GALOIS_DESCENT_ADAPTER"
ctl["next_item"] = "Stage33-10_ABSOLUTE_H1_AND_GALOIS_DESCENT_ADAPTER"
ctl["advance_scope"] = "STAGE33_10_REPAIR_CHILD_MAY_ADVANCE_MULTIPLE_SAFE_LIVE_MINIMAP_BRANCHES_IN_PARALLEL_WITH_STRICT_CHILD_EXIT_GATE_NOT_33_11_33_08_OR_33_40_PLUS"
ctl["main_batch_semantics"] = "ADVANCE_MULTIPLE_AUTHORIZED_33_10_LIVE_BRANCHES_UNTIL_BLOCKED_OR_CLOSED_PRESERVE_PARTIAL_EXACT_PROGRESS_STOP_UNNEEDED_SIBLINGS_AFTER_33_10E_EXACT_CLOSURE"
ctl["next_expected_command"] = "Stage33-main-batch"

# Firewalls remain unchanged by this child closure.
assert ctl["stage33_progress"] == "6/11"
assert not ctl["stage33_07"]["unit_closed"] and ctl["stage33_07"]["connecting_matrix_columns_explicitly_materialized"] == 0
assert not ctl["stage33_07"]["absolute_h1_identified_with_finite_v4_h1"]
assert not ctl["stage33_07"]["arithmetic_localization_connecting_map_computed"]
assert not ctl["stage33_07"]["arithmetic_hs_d2_computed"]
assert not ctl["stage33_08_released"] and not ctl["stage33_40_released"]
assert not ctl["theorem_credit"] and not ctl["endpoint_credit"]

CONTROLLER.write_text(json.dumps(ctl, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("STAGE33_09_CONTROLLER_TRANSITION=PASS_EXACT")
print("NEXT=" + ctl["next_item"])
