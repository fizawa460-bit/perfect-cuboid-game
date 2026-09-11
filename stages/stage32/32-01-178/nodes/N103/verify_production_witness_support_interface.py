#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

INTERFACE_SCHEMA = "STAGE32_32_01_178_N103_PRODUCTION_WITNESS_SUPPORT_INTERFACE_V1"
HANDOFF_SCHEMA = "STAGE32_32_01_178_N103_PRODUCTION_WITNESS_SUPPORT_HANDOFF_V1"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def fail(message: str) -> None:
    raise ValueError(message)


def sha256_json(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def parse_degree(row_id: object) -> int:
    match = re.fullmatch(r"g\d+-d(\d+)", str(row_id))
    if match is None:
        fail("row_id must have form g<genus>-d<degree>")
    return int(match.group(1))


def require_int_list(value: object, count: int, name: str) -> list[int]:
    if not isinstance(value, list) or len(value) != count:
        fail(f"{name} must contain exactly {count} entries")
    if any(type(v) is not int for v in value):
        fail(f"{name} must contain only integers")
    return value


def require_sha256(value: object, name: str) -> str:
    text = str(value)
    if HEX64.fullmatch(text) is None:
        fail(f"{name} must be a lowercase 64-hex sha256")
    return text


def verify_interface(raw: dict) -> None:
    if raw.get("schema") != INTERFACE_SCHEMA:
        fail("interface schema regression")
    if raw.get("node_id") != "N103":
        fail("node id regression")
    if raw.get("credit_ceiling") != "PRODUCTION_INTERFACE_ONLY_NO_BTVA_OR_FULL178_CREDIT":
        fail("credit ceiling regression")

    seam = raw["external_ex5_seam"]
    ci = seam["consumer_input_contract"]
    if ci.get("z_length") != 5 or ci.get("witness_r_reduced_length") != 59:
        fail("EX5 consumer input dimensions regression")
    if seam.get("consumer_does_not_find_witness") is not True:
        fail("consumer/producer responsibility regression")

    handoff = raw["minimal_stage32_handoff"]
    if handoff.get("handoff_schema") != HANDOFF_SCHEMA:
        fail("handoff schema regression")
    locator = handoff["required_production_locator"]
    if locator["terminal_pairings"].get("count") != 11:
        fail("terminal prefix dimension regression")
    support = handoff["required_support_packet_after_replay"]
    if support.get("picard_rank") != 64 or support.get("all140_pairing_count") != 140:
        fail("Picard/all140 dimension regression")
    if support.get("exceptional_all140_indices_0based") != [92, 139]:
        fail("exceptional all140 slice regression")
    if support.get("pairings_last48_count") != 48:
        fail("last48 dimension regression")

    anti = raw["anti_loop"]
    forbidden_false = (
        "duplicate_ex5_target_to_59d_adapter",
        "infer_z_from_row_id_d_e_or_terminal_rank_without_exact_completion",
        "infer_support_from_exceptional_mass_e",
        "materialize_27_digit_terminal_family",
        "promote_representative_sat_or_unsat_to_full178",
    )
    if any(anti.get(key) is not False for key in forbidden_false):
        fail("anti-loop firewall regression")

    firewalls = raw["firewalls"]
    forbidden_credit = (
        "FULL178_complete",
        "receiver_credit",
        "stage32_main_credit",
        "Q602_excluded",
        "O210_excluded",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    )
    if any(firewalls.get(key) is not False for key in forbidden_credit):
        fail("credit firewall regression")


def verify_handoff(raw: dict) -> None:
    if raw.get("schema") != HANDOFF_SCHEMA:
        fail("handoff schema mismatch")

    locator = raw.get("production_locator")
    witness = raw.get("exact_witness")
    support = raw.get("support_replay")
    if not isinstance(locator, dict) or not isinstance(witness, dict) or not isinstance(support, dict):
        fail("handoff must contain production_locator, exact_witness, support_replay")

    row_id = str(locator.get("row_id"))
    degree = parse_degree(row_id)
    if locator.get("degree_d") != degree:
        fail("production locator degree does not match row_id")
    if type(locator.get("exceptional_mass_e")) is not int:
        fail("production locator e must be integral")
    if type(locator.get("terminal_rank")) is not int or locator["terminal_rank"] < 0:
        fail("terminal_rank must be a nonnegative integer")
    terminal_pairings = require_int_list(locator.get("terminal_pairings"), 11, "terminal_pairings")

    equal_fields = ("row_id", "degree_d", "exceptional_mass_e", "terminal_rank")
    for key in equal_fields:
        if witness.get(key) != locator.get(key):
            fail(f"witness {key} does not match production locator")
    if witness.get("terminal_pairings") != terminal_pairings:
        fail("witness terminal_pairings do not match production locator")
    require_int_list(witness.get("z"), 5, "z")
    r59 = require_int_list(witness.get("witness_r_reduced"), 59, "witness_r_reduced")
    require_sha256(witness.get("producer_evidence_canonical_sha256"), "producer evidence hash")
    if HEX40.fullmatch(str(witness.get("producer_exact_head"))) is None:
        fail("producer_exact_head must be a lowercase 40-hex commit")

    if support.get("consumer_status") != "PASS_EXACT_WITNESS_TO_NODE_SUPPORT":
        fail("support replay is not exact-consumer PASS")
    if support.get("picard_rank") != 64 or support.get("all140_pairing_count") != 140:
        fail("support replay Picard/all140 dimensions regression")
    if support.get("exceptional_all140_indices_0based") != [92, 139]:
        fail("support replay exceptional slice regression")
    last48 = require_int_list(support.get("pairings_last48"), 48, "pairings_last48")
    if min(last48) < 0:
        fail("pairings_last48 must be nonnegative before support extraction")
    if sum(last48) != locator["exceptional_mass_e"]:
        fail("sum(last48) does not equal exact exceptional mass e")
    expected_support = [k for k, value in enumerate(last48) if value > 0]
    expected_zeros = [k for k, value in enumerate(last48) if value == 0]
    if support.get("support_indices_0based") != expected_support:
        fail("support indices are not exactly the positive last48 entries")
    if support.get("zero_indices_0based") != expected_zeros:
        fail("zero indices are not exactly the zero last48 entries")
    if require_sha256(support.get("pairings_last48_sha256"), "last48 hash") != sha256_json(last48):
        fail("last48 sha256 mismatch")
    if support.get("witness_r_reduced_sha256") is not None:
        if require_sha256(support["witness_r_reduced_sha256"], "r59 hash") != sha256_json(r59):
            fail("witness_r_reduced sha256 mismatch")
    require_sha256(support.get("node_bridge_canonical_sha256"), "node bridge hash")
    require_sha256(support.get("consumer_output_canonical_sha256"), "consumer output hash")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--interface",
        type=Path,
        default=Path(__file__).with_name("production-witness-support-interface.json"),
    )
    ap.add_argument("--handoff", type=Path)
    args = ap.parse_args()

    interface = json.loads(args.interface.read_text())
    verify_interface(interface)
    result = {"interface": "PASS"}
    if args.handoff is not None:
        verify_handoff(json.loads(args.handoff.read_text()))
        result["handoff"] = "PASS"
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
