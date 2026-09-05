#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1577-mod2-fiber-divisor-identity.json"
CONTROLLER = ROOT / "stages/stage32/controller.json"

EXPECTED_SCHEMA = "STAGE32_POST1577_DIRECT_MOD2_FIBER_DIVISOR_IDENTITY_V1"
EXPECTED_STATUS = "EXACT_DIRECT_MOD2_FIBER_DIVISOR_IDENTITY_PENDING_HOSTILE_AUDIT"
EXPECTED_CANONICAL = "1f81266f3361ca797d0caf321136c53e5d717d8f8abb434737f2ec933ee3b228"
EXPECTED_TARGET = {"row_id":"g1-d186","O":210,"qprime":4,"Q":602,"surviving_residues_decimal":[73,97,235]}
EXPECTED_FIRST = [34,35,38,39,42,43]
EXPECTED_SECOND = [33,36,37,40,41,44]


def fail(msg: str) -> None:
    raise SystemExit(msg)


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canonical_sha(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def assert_blob(lock: dict) -> Path:
    path = ROOT / lock["path"]
    if not path.is_file():
        fail(f"missing locked file: {lock['path']}")
    got = git_blob_sha(path)
    if got != lock["blob_sha1"]:
        fail(f"blob moved: {lock['path']} got={got} expected={lock['blob_sha1']}")
    return path


def main() -> None:
    cert = json.loads(CERT.read_text())
    if cert["schema"] != EXPECTED_SCHEMA or cert["status"] != EXPECTED_STATUS:
        fail("certificate schema/status moved")
    if cert["fixed_target"] != EXPECTED_TARGET:
        fail("fixed target moved")
    if cert.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        fail("recorded canonical moved")
    got_canonical = canonical_sha(cert)
    if got_canonical != EXPECTED_CANONICAL:
        fail(f"certificate canonical mismatch: {got_canonical}")

    expected_base = os.environ.get("STAGE32_EXPECTED_BASE_SHA")
    if not expected_base:
        fail("STAGE32_EXPECTED_BASE_SHA is required")
    if cert["base_main_sha"] != expected_base:
        fail(f"stale base_main_sha: cert={cert['base_main_sha']} expected={expected_base}")

    controller = json.loads(CONTROLLER.read_text())
    if controller.get("stage32_closed") is not False:
        fail("controller stage32_closed moved")
    ctarget = controller.get("fixed_target", {})
    for key, value in {"row_id":"g1-d186","O":210,"qprime":4,"Q":602}.items():
        if ctarget.get(key) != value:
            fail(f"controller target moved at {key}")

    locks = cert["source_locks"]
    source_path = assert_blob(locks["post1484_modular_factor_bidegree_source_note"])
    terminal_path = assert_blob(locks["post1577_terminal_negative"])

    source = source_path.read_text()
    required_source_fragments = [
        "F_z(L) = 2 L + sum_{E_j incident to L} E_j",
        "F_w(L) = 2 L + sum_{E_j incident to L} E_j",
        "every retained boundary label 33..44 has exactly eight incident exceptional curves",
        "first factor labels `34,35,38,39,42,43`: `C.F_z = 105`",
        "second factor labels `33,36,37,40,41,44`: `C.F_w = 81`",
    ]
    for fragment in required_source_fragments:
        if fragment not in source:
            fail(f"locked divisor source statement missing: {fragment}")

    terminal = json.loads(terminal_path.read_text())
    if canonical_sha(terminal) != locks["post1577_terminal_negative"]["canonical_sha256"]:
        fail("post1577 terminal canonical moved")
    reentry = terminal["lane_closure"]["reentry_requires"]
    if "DIRECT_MOD2_DIVISOR_OR_CORRESPONDENCE_IDENTITY" not in reentry:
        fail("post1577 direct-divisor reentry condition moved")
    if terminal["decision"]["Q602_excluded"] is not False:
        fail("post1577 Q602 firewall moved")

    direct = cert["direct_identity"]
    if direct["first_factor_boundary_labels"] != EXPECTED_FIRST or direct["second_factor_boundary_labels"] != EXPECTED_SECOND:
        fail("factor boundary-label split moved")
    if sorted(EXPECTED_FIRST + EXPECTED_SECOND) != list(range(33,45)):
        fail("retained boundary partition regression")
    if direct["incident_exceptional_count_each"] != 8:
        fail("incident exceptional count moved")
    if direct["integral_templates"] != {
        "first_factor":"F_z(L) = 2 L + sum_{E_j incident to L} E_j",
        "second_factor":"F_w(L) = 2 L + sum_{E_j incident to L} E_j",
    }:
        fail("integral fiber-divisor identity moved")
    if direct["mod2_templates"] != {
        "first_factor":"F_z(L) = sum_{E_j incident to L} E_j (mod 2)",
        "second_factor":"F_w(L) = sum_{E_j incident to L} E_j (mod 2)",
    }:
        fail("mod2 fiber-divisor identity moved")
    if direct["direct_mod2_divisor_identity_obtained"] is not True:
        fail("direct mod2 divisor identity credit moved")

    quotient = cert["exceptional_quotient_preflight"]
    if quotient != {
        "mod2_fiber_class_lies_in_exceptional_span":True,
        "image_in_mod2_quotient_by_exceptional_span":"0",
        "nonexceptional_mod2_class_obtained":False,
        "q602_residue_specific_commutator_obtained":False,
    }:
        fail("exceptional-quotient preflight moved")

    decision = cert["decision"]
    if decision != {
        "result":"PASS_EXACT_DIRECT_MOD2_FIBER_IDENTITY_EXCEPTIONAL_SUPPORTED_ONLY",
        "Q602_excluded":False,
        "O210_excluded":False,
        "O212_plus_advance_allowed":False,
        "controller_change_authorized":False,
        "next_exact_route":"DIRECT_MOD2_CORRESPONDENCE_OR_DIVISOR_CLASS_WITH_NONEXCEPTIONAL_COMPONENT_OR_INDEPENDENT_ODD_COMMUTATOR",
    }:
        fail("decision/firewall moved")
    if any(cert["firewalls"].values()):
        fail("credit firewall promoted unexpectedly")

    print("PASS Stage32 post1577 direct mod2 fiber-divisor identity preflight")
    print(f"certificate_canonical={got_canonical}")
    print("direct_mod2_divisor_identity=true")
    print("mod2_fiber_class_in_exceptional_span=true quotient_image=0")
    print("Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")


if __name__ == "__main__":
    main()
