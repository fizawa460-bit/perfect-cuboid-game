#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1556-carrier-invariance-source-gap.json"
CONTROLLER = ROOT / "stages/stage32/controller.json"

EXPECTED_CANONICAL = "256cbd7d1a3f3667d1558e530293392a3068f52cd8dfa1495f14cb3015caa308"
EXPECTED_BASE = "303c66cc4b2744222ee242d52c457948d587e32e"


def fail(msg: str) -> None:
    raise SystemExit(msg)


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def canonical_sha(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if claimed != calc:
        fail(f"canonical mismatch: {claimed} != {calc}")
    return calc


def main() -> None:
    cert = load_json(CERT_PATH)
    if cert["schema"] != "STAGE32_POST1556_CARRIER_INVARIANCE_SOURCE_GAP_V1":
        fail("certificate schema moved")
    if cert["status"] != "EXACT_RETAINED_SOURCE_GAP_PENDING_HOSTILE_AUDIT":
        fail("certificate status moved")
    if cert["base_main_sha"] != EXPECTED_BASE:
        fail("base main moved")
    if canonical_sha(cert) != EXPECTED_CANONICAL:
        fail("certificate canonical moved")

    locked: dict[str, object] = {}
    for name, lock in cert["source_locks"].items():
        path = ROOT / lock["path"]
        if not path.is_file():
            fail(f"missing source lock: {name}")
        got = blob_sha1(path)
        if got != lock["blob_sha1"]:
            fail(f"source blob drift: {name}: {got}")
        if "canonical_sha256" in lock:
            doc = load_json(path)
            if canonical_sha(doc) != lock["canonical_sha256"]:
                fail(f"source canonical drift: {name}")
            locked[name] = doc
        elif path.suffix == ".json":
            locked[name] = load_json(path)
        else:
            locked[name] = path.read_text()

    parent = locked["parent_box_normalizer"]
    common = locked["common_double_cover"]
    bidegree = locked["v6_bidegree_note"]
    arsenal = locked["arsenal_S32_PW05"]
    note = locked["source_note"]

    norm = parent["full_G_normalizer"]
    for key in ("beta_B_exists", "beta_X_exists", "X_to_B_equivariant"):
        if norm[key] is not True:
            fail(f"parent ambient quotient result moved: {key}")
    boundary = parent["carrier_boundary"]
    for key in (
        "beta_B_N_invariance_proved",
        "beta_X_Y_invariance_proved",
        "intrinsic_beta_Y_proved",
        "Gamma_invariance_proved",
    ):
        if boundary[key] is not False:
            fail(f"parent carrier firewall moved: {key}")
    if boundary["conditional_chain"] != "beta_B(N)=N => beta_X(Y)=Y => [T,b3]=0 => Q(T)!=602":
        fail("parent conditional chain moved")

    carrier = common["carrier_consequence"]
    if carrier["hypothesis"] != "N is the normalization of a hypothetical integral carrier mapping to B, and Y is the normalization of its Beauville pullback N x_B X.":
        fail("common-cover carrier definition moved")
    if common["firewalls"]["carrier_existence_proved"] is not False:
        fail("common-cover carrier existence firewall moved")

    for marker in (
        "This note does not claim existence of an integral genus-one carrier.",
        "m_z=105`, `m_w=81`",
        "any integral curve in the exact V6 class",
        "does not prove an integral curve exists in that class",
    ):
        if marker not in bidegree:
            fail(f"V6 bidegree marker missing: {marker}")

    for marker in (
        "Maturity | **PROVISIONAL**",
        "FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION",
        "proved invariance",
        "semantic/geometric identification merely from reconstructed algebra",
    ):
        if marker not in arsenal:
            fail(f"Arsenal S32-PW05 marker missing: {marker}")

    pos = cert["retained_positive_input"]
    if not all((pos["beta_B_exists"], pos["beta_X_exists"], pos["X_to_B_equivariant"])):
        fail("retained positive input moved")
    if (pos["V6_factor_degree_z"], pos["V6_factor_degree_w"]) != (105, 81):
        fail("V6 factor degrees moved")
    if pos["carrier_N_definition"] != "normalization of a hypothetical integral carrier mapping to B":
        fail("N definition moved")
    if pos["carrier_Y_definition"] != "normalization of N x_B X":
        fail("Y definition moved")

    missing = cert["missing_member_level_data"]
    for key, value in missing.items():
        if value is not False:
            fail(f"missing-member datum promoted without source: {key}")

    ac = cert["arsenal_check"]
    if ac["router_used"] is not True or ac["card"] != "S32-PW05":
        fail("Arsenal routing record moved")
    if ac["card_supplies_missing_carrier_identification"] is not False:
        fail("provisional Arsenal card overpromoted")

    decision = cert["decision"]
    if decision["result"] != "PASS_EXACT_RETAINED_SOURCE_GAP_LOCALIZATION":
        fail("decision moved")
    if decision["retained_input_does_not_yet_prove_carrier_or_Gamma_invariance"] is not True:
        fail("source-gap localization lost")
    if decision["next_exact_leaf"] != "SOURCE_LOCK_BETA_B_ACTION_ON_FIXED_V6_CARRIER_MEMBER_OR_DIRECT_GAMMA_IDENTITY":
        fail("next exact leaf moved")
    for key in (
        "carrier_invariance_proved",
        "correspondence_invariance_proved",
        "actual_T_b3_commutation_proved",
        "actual_T_b3_noncommutation_proved",
        "Q602_excluded",
        "O210_excluded",
        "O212_plus_advance_allowed",
        "controller_change_authorized",
    ):
        if decision[key] is not False:
            fail(f"decision firewall leaked: {key}")

    if any(cert["firewalls"].values()):
        fail("credit firewall leaked")

    for marker in (
        "RETAINED_INPUT_DOES_NOT_YET_PROVE_CARRIER_OR_GAMMA_INVARIANCE=true",
        "beta_B(N)=N",
        "Picard class",
        "SOURCE_LOCK_BETA_B_ACTION_ON_FIXED_V6_CARRIER_MEMBER_OR_DIRECT_GAMMA_IDENTITY",
        "The Stage32 controller remains unchanged.",
    ):
        if marker not in note:
            fail(f"source-note marker missing: {marker}")

    ctl = load_json(CONTROLLER)
    if ctl["stage"] != 32 or ctl["stage32_closed"] is not False:
        fail("controller lifecycle moved")
    fixed = ctl["fixed_target"]
    if (fixed["row_id"], fixed["O"], fixed["qprime"], fixed["Q"]) != ("g1-d186", 210, 4, 602):
        fail("controller fixed target moved")

    print("PASS post1556 retained carrier-invariance source-gap localization")
    print(f"canonical={EXPECTED_CANONICAL}")
    print("ambient beta_B/beta_X descent=RETAINED")
    print("carrier member / direct Gamma invariance source=ABSENT_FROM_LOCKED_INPUT")
    print("Picard-class preservation alone cannot identify the same member without uniqueness/fixed section")
    print("Q602/O210=OPEN O212+=BLOCKED controller=UNCHANGED")


if __name__ == "__main__":
    main()
