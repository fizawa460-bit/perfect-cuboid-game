#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1570-three-involution-q602-exclusion-batch.json"
DIAG = HERE / "diagnose_stage32_post1570_three_involution_q602.py"
CONTROLLER = ROOT / "stages/stage32/controller.json"
EXPECTED_SCHEMA = "STAGE32_POST1570_THREE_INVOLUTION_Q602_TERMINAL_NEGATIVE_V1"
EXPECTED_STATUS = "EXACT_MULTI_ROUTE_SYMMETRY_PARITY_TERMINAL_NEGATIVE_PENDING_HOSTILE_AUDIT"
EXPECTED_CANONICAL = "8af12197316f8d23b7fa94fa7d064fded355a59d5c0cd5adef47e13826643538"
EXPECTED_TABLE = {"73":["A0=b4"],"97":["A2=b3^2*b4*b3^-2"],"235":["A1=b3*b4*b3^-1"]}


def fail(msg: str) -> None:
    raise SystemExit(msg)


def canonical_sha(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    data = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(data).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def assert_blob(lock: dict) -> None:
    path = ROOT / lock["path"]
    if not path.is_file():
        fail(f"missing locked file: {lock['path']}")
    got = git_blob_sha(path)
    if got != lock["blob_sha1"]:
        fail(f"blob moved: {lock['path']} got={got} expected={lock['blob_sha1']}")


def main() -> None:
    cert = json.loads(CERT.read_text())
    if cert["schema"] != EXPECTED_SCHEMA or cert["status"] != EXPECTED_STATUS:
        fail("certificate schema/status moved")
    if cert.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        fail("recorded certificate canonical moved")
    got_canonical = canonical_sha(cert)
    if got_canonical != EXPECTED_CANONICAL:
        fail(f"certificate canonical mismatch: {got_canonical}")

    expected_base = os.environ.get("STAGE32_EXPECTED_BASE_SHA")
    if not expected_base:
        fail("STAGE32_EXPECTED_BASE_SHA is required")
    if cert["base_main_sha"] != expected_base:
        fail(f"stale base_main_sha: cert={cert['base_main_sha']} expected={expected_base}")

    if cert["fixed_target"] != {"row_id":"g1-d186","O":210,"qprime":4,"Q":602,"surviving_residues_decimal":[73,97,235]}:
        fail("fixed target moved")
    controller = json.loads(CONTROLLER.read_text())
    if controller.get("stage32_closed") is not False:
        fail("controller stage32_closed moved")
    ctarget = controller.get("fixed_target", {})
    for key, value in {"row_id":"g1-d186","O":210,"qprime":4,"Q":602}.items():
        if ctarget.get(key) != value:
            fail(f"controller fixed target moved at {key}")

    proc = subprocess.run([sys.executable, str(DIAG)], cwd=ROOT, text=True, capture_output=True, check=True)
    diag = json.loads(proc.stdout)
    if diag["schema"] != "STAGE32_POST1570_THREE_INVOLUTION_Q602_DIAGNOSTIC_V1":
        fail("diagnostic schema moved")
    if diag["q602_residue_commuting_involution_table"] != EXPECTED_TABLE:
        fail("residue/involution table moved")
    if diag["retained_stoll_group_order"] != 1536:
        fail("Stoll group order moved")
    if diag["blowdown_mod2_orbit_sum_stabilizer_count"] != 384 or diag["blowdown_mod2_orbit_sum_stabilizer_outside_h_count"] != 380:
        fail(
            "mod2 orbit-sum stabilizer moved: "
            f"count={diag['blowdown_mod2_orbit_sum_stabilizer_count']} "
            f"outside_H={diag['blowdown_mod2_orbit_sum_stabilizer_outside_h_count']}"
        )
    if diag["blowdown_mod2_stabilizer_exactly_H"] is not False:
        fail("mod2 detector unexpectedly recovered exact-H stabilizer")

    route_a = cert["routes"]["A_three_involution_residue_table"]
    if route_a["table"] != EXPECTED_TABLE or route_a["exclusion_credit"] is not False:
        fail("Route A firewall moved")
    route_b = cert["routes"]["B_blowdown_orbit_sum_mod2"]
    expected_b = {"retained_stoll_group_order":1536,"blowdown_mod2_orbit_sum_stabilizer_count":384,"blowdown_mod2_orbit_sum_stabilizer_outside_h_count":380,"blowdown_mod2_stabilizer_exactly_H":False,"full_stoll_group_stabilizes_mod2_blowdown_orbit_sum":False,"q602_residue_exclusion_obtained":False}
    for key, value in expected_b.items():
        if route_b.get(key) != value:
            fail(f"Route B moved at {key}")

    route_c = cert["routes"]["C_degree2_pushpull_mod2"]
    if route_c != {"result":"NO_INJECTIVITY_CREDIT_FROM_STANDARD_DEGREE2_PUSH_PULL","retained_degree2_geometry_source_locked":True,"formal_identity":"push_* pull^* = 2 id","mod2_composite":"0","kernel_nonzero_claimed":False,"mod2_pullback_injective_proved":False,"rescue_of_route_B_obtained":False}:
        fail("Route C push-pull firewall moved")

    route_d = cert["routes"]["D_arsenal"]
    if not (route_d["S30_W01_requires_source_common_model_semantic_anchor"] and route_d["S32_PW05_requires_proved_action_and_invariance"] and route_d["S32_PW05_semantic_geometric_identification_forbidden"]):
        fail("Arsenal semantic firewall moved")

    for name in ("source_note","common_double_cover_degree2","post1566_orbit_sum_diagnostic","arsenal_index","arsenal_S30_W01","arsenal_S32_PW05"):
        assert_blob(cert["source_locks"][name])
    common = json.loads((ROOT / cert["source_locks"]["common_double_cover_degree2"]["path"]).read_text())
    if canonical_sha(common) != cert["source_locks"]["common_double_cover_degree2"]["canonical_sha256"]:
        fail("common double-cover canonical moved")
    square = common.get("group_quotient_square", {})
    if "degree-two" not in square.get("generic_fiber_argument", "") and "degree two" not in square.get("generic_fiber_argument", ""):
        fail("common double-cover degree-two statement missing")

    decision = cert["decision"]
    if decision != {"result":"PASS_EXACT_TERMINAL_NEGATIVE_SYMMETRY_PARITY_BATCH","Q602_excluded":False,"O210_excluded":False,"O212_plus_advance_allowed":False,"controller_change_authorized":False,"next_exact_route":"NEW_NON_AUTOMORPHISM_MOD2_GEOMETRIC_INPUT_ONLY"}:
        fail("decision/firewall moved")
    closure = cert["lane_closure"]
    if closure["symmetry_parity_orbit_sum_lane_exhausted"] is not True or closure["no_further_same_detector_gap_localization_only"] is not True:
        fail("lane closure moved")
    if any(cert["firewalls"].values()):
        fail("credit firewall promoted unexpectedly")

    print("PASS Stage32 post1570 terminal symmetry-parity negative batch")
    print(f"certificate_canonical={got_canonical}")
    print("residue_table=73:b4,97:b3^2b4b3^-2,235:b3b4b3^-1")
    print("mod2_orbit_sum_stabilizer=384 outside_H=380")
    print("degree2_common_cover_source_locked=true mod2_injectivity_credit=false")
    print("Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")


if __name__ == "__main__":
    main()
