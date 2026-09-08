#!/usr/bin/env python3
"""Goal4AJ gen26: exact numerator exceptional-incidence bridge preflight.

This is the numerator analogue of the already source-locked degree-19 denominator
exceptional bridge.  It checks, for every one of the 48 retained A1 exceptional
curves E_j, the exact resolution identity

    sum_i m_i (C_i . E_j) = 2 e_j,

using the active degree-31 numerator strict multiplicities m_i, active exceptional
targets e_j, and the retained 0/1 strict-to-node incidence from the exact locator.

If all identities hold, then any effective degree-31 section divisor D ~ 31H that
satisfies all 27 strict lower-bound conditions automatically has exceptional
orders >= e_j.  Combined with the source-locked fact that the full active numerator
target divisor has class 31H, there can be no additional effective divisor:
D-target is effective and linearly equivalent to zero, hence zero on the projective
integral surface.

This diagnostic does NOT assert that all 27 strict conditions passed; that is a
separate gen25-g4 exact computation.  Therefore it grants no literal numerator,
F_B, local, Brauer-Manin, E1, Stage35, theorem, receiver, endpoint, or perfect-
cuboid credit by itself.
"""
from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"
ACTIVE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py"
QPEEL = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_q_hyperplane_factor_peel.py"

LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
ACTIVE_BLOB = "20da16902171b267294acee0f3b80997d8fd5246"
ACTIVE_CANONICAL = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
QPEEL_BLOB = "e5b41410e570d5e442afe985dd5b7f3355d5d653"
QPEEL_CANONICAL = "c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba"
QPEEL_RUN = 34092066114
QPEEL_JOB = 101647794285
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def csha(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


assert git_blob(LOCATOR) == LOCATOR_BLOB
assert git_blob(ACTIVE) == ACTIVE_BLOB
assert git_blob(QPEEL) == QPEEL_BLOB

buf = io.StringIO()
with redirect_stdout(buf):
    lns = runpy.run_path(str(LOCATOR))
loc = lns["out"]
node_map = lns["node_map"]
assert loc["canonical_sha256"] == LOCATOR_CANONICAL
assert loc["strict_curve_packet_sha256"] == STRICT_PACKET
assert len(node_map) == 48

buf = io.StringIO()
with redirect_stdout(buf):
    ans = runpy.run_path(str(ACTIVE))
active = ans["out"]
assert active["canonical_sha256"] == ACTIVE_CANONICAL
num = active["numerator"]
strict = {int(k): int(v) for k, v in num["strict_multiplicities_1based"].items()}
exc = {int(k): int(v) for k, v in num["exceptional_multiplicities_1based"].items()}
assert num["homogeneous_degree_after_q_peel"] == 31
assert len(strict) == 27 and len(exc) == 48
assert sum(strict.values()) == 202
assert sorted(exc) == list(range(93, 141))

rows = {}
for j in range(93, 141):
    incident = [int(i) for i in node_map[str(j)]["incident_strict_curve_indices_1based"]]
    inc_sum = sum(strict.get(i, 0) for i in incident)
    target = exc[j]
    rows[str(j)] = {
        "exceptional_index_1based": j,
        "target_order": target,
        "active_strict_incidence_multiplicity_sum": inc_sum,
        "twice_target_order": 2 * target,
        "relation_holds": inc_sum == 2 * target,
    }

all_rel = all(r["relation_holds"] for r in rows.values())
route = (
    "NUMERATOR_ALL48_EXCEPTIONAL_TARGETS_FORCED_FROM_STRICT_IF_ALL27_EXACT_PASS"
    if all_rel else
    "NUMERATOR_EXCEPTIONAL_INCIDENCE_BRIDGE_FAIL"
)
out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_EXCEPTIONAL_FORCED_BRIDGE_GEN26_DIAGNOSTIC_V1",
    "source_locks": {
        "locator_blob_sha1": LOCATOR_BLOB,
        "locator_canonical_sha256": LOCATOR_CANONICAL,
        "active_packet_blob_sha1": ACTIVE_BLOB,
        "active_packet_canonical_sha256": ACTIVE_CANONICAL,
        "strict_curve_packet_sha256": STRICT_PACKET,
        "q_hyperplane_peel_blob_sha1": QPEEL_BLOB,
        "q_hyperplane_peel_canonical_sha256": QPEEL_CANONICAL,
        "q_hyperplane_peel_run": QPEEL_RUN,
        "q_hyperplane_peel_job": QPEEL_JOB,
    },
    "homogeneous_degree": 31,
    "strict_condition_count": len(strict),
    "strict_total_multiplicity": sum(strict.values()),
    "exceptional_condition_count": len(exc),
    "all_48_incidence_relations_hold": all_rel,
    "incidence_rows": rows,
    "source_locked_full_numerator_target_class": "31H",
    "bridge_statement": "all27 exact strict lower bounds + all48 incidence identities + target class 31H imply all exceptional lower bounds and exact full target divisor equality",
    "route_result": route,
    "all_27_strict_exact_pass_consumed": False,
    "literal_q_numerator_materialized": False,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
print("GOAL4AJ_GEN26_NUMERATOR_EXCEPTIONAL_BRIDGE_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_GEN26_NUMERATOR_EXCEPTIONAL_BRIDGE=" + ("PASS" if all_rel else "FAIL"))
if not all_rel:
    raise SystemExit("numerator exceptional incidence bridge failed")
