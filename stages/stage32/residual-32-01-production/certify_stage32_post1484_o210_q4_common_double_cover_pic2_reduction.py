#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CERT_CANONICAL = "7cd69883433955d3a7c59910c67b3918387fe2a4bc316236c63154f46f759792"
SOURCE_NOTE_BLOB = "83115a5424647e56b3d63c927481e10faa1237a8"
BIDEGREE_BLOB = "072266f2ac5386316adc99e35a6444d2449656c8"
BIDEGREE_CANONICAL = "791870c37681702392e1e59d224f494ed791709d467efa68a20cf49bff4ab420"
LOCAL_BLOB = "dd5fdb8d2553d25a1479c1e5cff68a201c8396e3"
LOCAL_CANONICAL = "318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328"
V4_BLOB = "00eaebc3c57f6b5e3696c7bcd60eac5a53121f72"
V4_CANONICAL = "2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5"
SIX_CUSP_BLOB = "1f1b24eb09f48231a3897423c36f4e03095a6d75"
SIX_CUSP_CANONICAL = "329cf00d5380f515386622f5b18bcf90e36a99c16715e462ef9219abe0d609e1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def locked_json(path: Path, blob: str) -> dict:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return json.loads(raw)


def locked_text(path: Path, blob: str) -> str:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return raw.decode()


def canonical_without_field(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return csha(body)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", required=True, type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[3]
    here = repo / "stages/stage32/residual-32-01-production"

    cert = json.loads(args.check.read_text())
    if canonical_without_field(cert) != CERT_CANONICAL or cert.get("canonical_sha256_without_this_field") != CERT_CANONICAL:
        raise ValueError("Pic2 reduction canonical moved")

    note = locked_text(here / "post1484-o210-q4-common-double-cover-pic2-source-note.md", SOURCE_NOTE_BLOB)
    for needle in (
        "F(w)/F(z)",
        "Pic^0(N)[2] ~= (Z/2)^2",
        "q is a square  <=>  [D]=0",
        "Do not infer zero merely from equality of branch parity",
    ):
        if needle not in note:
            raise ValueError(f"source-note semantics moved: {needle}")

    bidegree = locked_json(here / "post1484-v6-modular-factor-bidegree-boundary.json", BIDEGREE_BLOB)
    if canonical_without_field(bidegree) != BIDEGREE_CANONICAL:
        raise ValueError("audited bidegree canonical moved")
    if bidegree["modular_factor_bidegree"]["first_z"] != 105 or bidegree["modular_factor_bidegree"]["second_w"] != 81:
        raise ValueError("modular factor degrees moved")
    o210 = bidegree["O210_extremal_profile"]
    if o210["forced_contact_histogram"]["m1_odd"] != 210 or o210["forced_contact_histogram"]["m2_even"] != 28:
        raise ValueError("O210 contact histogram moved")
    if o210["descended_projection_ramification_totals"] != [0, 48]:
        raise ValueError("O210 descended ramification moved")

    local = locked_json(here / "post1473-o188-cusp-ramification-budget.json", LOCAL_BLOB)
    if canonical_without_field(local) != LOCAL_CANONICAL:
        raise ValueError("local parity adapter canonical moved")
    adapter = local["local_adapter"]
    if "same parity" not in adapter["parity"] or "parity of m" not in adapter["parity"]:
        raise ValueError("local parity statement moved")

    v4 = locked_json(here / "post1473-x8-v4-cusp-quotient.json", V4_BLOB)
    if canonical_without_field(v4) != V4_CANONICAL:
        raise ValueError("V4 quotient canonical moved")
    qg = v4["quotient_geometry"]
    if qg["C0_to_X4_degree"] != 2 or qg["C0_to_X4_total_fixed_points"] != 6 or qg["genus_C0"] != 2:
        raise ValueError("C0->X4 double-cover geometry moved")

    six = locked_json(here / "post1484-o210-q4-six-cusp-hurwitz-reduction.json", SIX_CUSP_BLOB)
    if canonical_without_field(six) != SIX_CUSP_CANONICAL:
        raise ValueError("six-cusp reduction canonical moved")
    if six["v4_descent"]["Y_to_C0_degrees"] != [105, 81] or six["v4_descent"]["Y_to_C0_ramification"] != [0, 48]:
        raise ValueError("descended simultaneous-map data moved")

    if cert["quadratic_pullback_lemma"]["same_double_cover_iff"] != "F(w)/F(z) is a square in K(N)^*":
        raise ValueError("quadratic pullback criterion moved")
    parity = cert["valuation_parity_reduction"]
    if parity["odd_support"] != "The common odd support is exactly the 210 m=1 exceptional contacts at O=210.":
        raise ValueError("common odd support moved")
    if parity["conclusion"] != "Every valuation of q=F(w)/F(z) is even.":
        raise ValueError("even-valuation conclusion moved")

    pic = cert["pic2_obstruction"]
    if pic["genus_N"] != 1 or pic["Pic0_2_order"] != 4 or pic["current_retained_data_determines_D_class"] is not False:
        raise ValueError("Pic2 obstruction boundary moved")
    if pic["same_double_cover_iff"] != "[D]=0 in Pic^0(N)[2]":
        raise ValueError("Pic2 zero criterion moved")

    verdict = cert["verdict"]
    if verdict != {
        "O210_excluded": False,
        "common_double_cover_condition_reduced_to_four_state_Pic2_check": True,
        "local_parity_alone_is_insufficient": True,
        "next_exact_leaf": "O210_Q4_COMPUTE_COMMON_DOUBLE_COVER_PIC2_CLASS",
    }:
        raise ValueError("Pic2 verdict moved")
    if cert["firewalls"].get("Pic2_class_not_yet_computed") is not True:
        raise ValueError("Pic2 noncomputation firewall missing")

    print("PASS", CERT_CANONICAL)


if __name__ == "__main__":
    main()
