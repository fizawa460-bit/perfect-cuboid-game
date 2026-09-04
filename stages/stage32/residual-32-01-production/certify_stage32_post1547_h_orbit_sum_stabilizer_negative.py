#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1547-h-orbit-sum-stabilizer-negative.json"
DIAG = HERE / "diagnose_stage32_post1536_h_orbit_sum_stabilizer.py"
CONTROLLER = ROOT / "stages/stage32/controller.json"

EXPECTED_CANONICAL = "501fe974c75e85cfa8ccc3a1f2f01fee100ee5a7fffd91cc7987c75cc6b3c28b"
EXPECTED_FINITE = {
    "retained_stoll_group_order": 1536,
    "h_deck_group_order": 4,
    "h_orbit_sum_stabilizer_count": 4,
    "h_orbit_sum_stabilizer_outside_h_count": 0,
    "h_orbit_sum_stabilizer_elements": [
        {"word": "1", "is_H_deck_element": True},
        {"word": "g7*g8", "is_H_deck_element": True},
        {"word": "g7*g9", "is_H_deck_element": True},
        {"word": "g8*g9", "is_H_deck_element": True},
    ],
    "second_boundary_set_stabilizer_count": 768,
    "second_boundary_cycle_type_3_3_count": 256,
    "cycle_type_3_3_and_h_orbit_sum_fixed_count": 0,
    "cycle_type_3_3_and_h_orbit_sum_fixed_elements": [],
}


def fail(msg: str) -> None:
    raise SystemExit(msg)


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def canonical_sha(obj: dict) -> str:
    core = dict(obj)
    got = core.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if got != calc:
        fail(f"canonical mismatch: field={got} calc={calc}")
    return calc


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def assert_source_locks(cert: dict) -> None:
    for name, lock in cert["source_locks"].items():
        path = ROOT / lock["path"]
        if not path.is_file():
            fail(f"missing source lock {name}: {path}")
        got_blob = git_blob_sha(path)
        if got_blob != lock["blob_sha1"]:
            fail(f"source blob moved for {name}: {got_blob} != {lock['blob_sha1']}")
        if "canonical_sha256" in lock:
            obj = load_json(path)
            if canonical_sha(obj) != lock["canonical_sha256"]:
                fail(f"source canonical moved for {name}")


def run_diagnostic() -> dict:
    raw = subprocess.check_output([sys.executable, str(DIAG)], text=True)
    return json.loads(raw)


def main() -> None:
    cert = load_json(CERT)
    if cert["schema"] != "STAGE32_POST1547_H_ORBIT_SUM_STABILIZER_NEGATIVE_V1":
        fail("certificate schema moved")
    if cert["status"] != "EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT":
        fail("certificate status moved")
    if canonical_sha(cert) != EXPECTED_CANONICAL:
        fail("certificate canonical moved")

    assert_source_locks(cert)

    if cert["fixed_target"] != {"row_id": "g1-d186", "O": 210, "qprime": 4, "Q": 602}:
        fail("fixed target moved")

    anchor = cert["semantic_anchor"]
    if anchor["q_pullback_relation"] != "q^*Gamma = D + uD + vD + uvD":
        fail("q-pullback relation moved")
    if anchor["h_deck_words"] != {"id": "1", "u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"}:
        fail("H-deck words moved")
    if anchor["second_factor_boundary_labels"] != [33, 36, 37, 40, 41, 44]:
        fail("second-factor boundary labels moved")
    if anchor["required_nontrivial_order3_branch_cycle_type"] != [3, 3]:
        fail("order-three branch cycle type moved")
    if anchor["orbit_sum_is_retained_numerical_pairing_class_only"] is not True:
        fail("orbit-sum scope firewall moved")

    repaired_note = (ROOT / cert["source_locks"]["post1500_rosati_repair_source_note"]["path"]).read_text()
    if "q^*Gamma=D+uD+vD+uvD" not in repaired_note:
        fail("post1500 source note no longer states exact q-pullback relation")

    post1532 = load_json(ROOT / cert["source_locks"]["post1532_setwise_predecessor"]["path"])
    if post1532["finite_result"]["setwise_h_orbit_stabilizer_count"] != 4:
        fail("post1532 setwise predecessor moved")
    if post1532["finite_result"]["setwise_h_orbit_stabilizer_outside_h_count"] != 0:
        fail("post1532 setwise predecessor outside-H result moved")

    post1536 = load_json(ROOT / cert["source_locks"]["post1536_branch_predecessor"]["path"])
    if post1536["finite_result"]["second_factor_boundary_labels"] != [33, 36, 37, 40, 41, 44]:
        fail("post1536 boundary labels moved")
    if post1536["bolza_order3_input"]["required_branch_permutation_cycle_type"] != [3, 3]:
        fail("post1536 order-three branch condition moved")
    if post1536["semantic_anchor"]["bijection_verified"] is not True:
        fail("post1536 Weierstrass semantic anchor moved")

    diag = run_diagnostic()
    if diag["schema"] != "STAGE32_POST1536_H_ORBIT_SUM_STABILIZER_DIAGNOSTIC_V1":
        fail("diagnostic schema moved")
    diag_finite = {key: diag[key] for key in EXPECTED_FINITE}
    if diag_finite != EXPECTED_FINITE:
        fail(f"diagnostic finite result moved: {json.dumps(diag_finite, sort_keys=True)}")
    if cert["finite_result"] != EXPECTED_FINITE:
        fail("certificate finite result does not match recomputed diagnostic")
    if diag["scope"] != "EXACT_RETAINED_NUMERICAL_PICARD_ORBIT_SUM_ONLY_NO_ACTUAL_T_COMMUTATOR_CREDIT":
        fail("diagnostic scope firewall moved")

    decision = cert["decision"]
    required_false = [
        "actual_T_commutation_proved",
        "actual_T_noncommutation_proved",
        "Q602_excluded",
        "O210_excluded",
        "O212_plus_advance_allowed",
        "controller_change_authorized",
    ]
    if decision["result"] != "EXACT_BOUNDED_NEGATIVE":
        fail("decision result moved")
    if decision["closed_subroute"] != "RETAINED_AMBIENT_STOLL_B3_ORBIT_SUM_INVARIANCE_FOR_Q_PULLBACK_GAMMA":
        fail("closed subroute moved")
    if decision["closed_subroute_only"] is not True:
        fail("closed-subroute-only firewall moved")
    if decision["strictly_weaker_test_than_post1532_setwise_orbit_stabilization"] is not True:
        fail("post1532 distinction moved")
    if any(decision[key] is not False for key in required_false):
        fail("decision credit firewall moved")

    fw = cert["firewalls"]
    for key in [
        "b3_lift_to_retained_X_proved",
        "correspondence_equivariance_credit",
        "effectivity_credit",
        "full178_closed",
        "receiver_credit",
        "route_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_credit",
    ]:
        if fw[key] is not False:
            fail(f"firewall moved: {key}")

    source_note = (ROOT / cert["source_locks"]["source_note"]["path"]).read_text()
    for phrase in [
        "RETAINED_AMBIENT_STOLL_B3_ORBIT_SUM_INVARIANCE_FOR_Q_PULLBACK_GAMMA",
        "does **not** prove `[T,b3]=0` or `[T,b3]!=0`",
        "does not exclude `Q(T)=602` or `O=210`",
        "O212+ remains blocked",
    ]:
        if phrase not in source_note:
            fail(f"source-note semantic firewall missing: {phrase}")

    controller = load_json(CONTROLLER)
    if controller.get("stage32_closed") is not False:
        fail("Stage32 unexpectedly closed")
    target = controller.get("fixed_target", {})
    for key, value in {"row_id": "g1-d186", "O": 210, "qprime": 4, "Q": 602}.items():
        if target.get(key) != value:
            fail(f"controller fixed target moved at {key}: {target.get(key)} != {value}")

    print("PASS post1547 H-orbit-sum bounded negative")
    print(f"canonical={EXPECTED_CANONICAL}")
    print("retained_stoll_group_order=1536")
    print("h_orbit_sum_stabilizer=4 exactly_H=true outside_H=0")
    print("second_boundary_set_stabilizer=768 cycle_type_3_3=256 intersection_with_sum_fixed=0")
    print("actual_[T,b3]_status=UNRESOLVED Q602_O210=OPEN O212_plus=BLOCKED")


if __name__ == "__main__":
    main()
