#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent

EXPECTED_N385_BLOB = "bcfa753493237cae7a2ea487c0483fe556ada6dd"
EXPECTED_N385_CANONICAL = "0af1a4deaa1924f6785e2adb259b03bdd64ed6a78e09efd1d16bfde2d6fa5a2f"
EXPECTED_N386_CANONICAL = "66f100b8bcfb8008afd3f59817268ff3d2293001b8746035ac75ffb25b871885"

EXPECTED_N372_BLOB = "e73af40e1433e6ab7227791c9501e51dfca1406c"
EXPECTED_N372_CANONICAL = "ce99f0f14445a2b48c7024bde853470291f604378709fcc7747104efdcd5c6b2"
EXPECTED_N372_REVIEW = 5187357950
EXPECTED_N372_TERMINAL = "g1-d008|e=8|rank=128820"

EXPECTED_V22_HEAD = "f8039b4ce479a4b91f2f0547e7049f629e9be5f5"
EXPECTED_V23_HEAD = "fba76454a49132f752dc93deb20214970b314d89"
EXPECTED_V23_REVIEW = 5189031846
EXPECTED_V23_BLOB = "bead809db3a008dd35d664a8923f06fecb7de5bb"
EXPECTED_V23_CANONICAL = "460b04ecb09d41c1082aee46795acf5da79454df42cc6126a7b92925977855aa"
EXPECTED_V23_TERMINALS = 47589703313957134649501

EXPECTED_HPADJ01_BLOB = "520b6b0f230e23fb5ea34b80fef591cfa5f9be4b"
EXPECTED_HPADJ01_CANONICAL = "9773c11e87de149b5b56438fd1c86929aa54a971601bf8306855fd0f8a303506"
EXPECTED_HPADJ01_CHARGED = 27104321327305699275487


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode() + b"\0" + raw
    ).hexdigest()


def head(root: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
    ).strip()


def checked(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing file: {path}")
    req(git_blob(path) == expected_blob, f"blob drift: {path}")
    obj = load(path)
    req(
        obj.get("canonical_sha256_without_this_field") == expected_canonical,
        f"stored canonical drift: {path}",
    )
    req(canonical(obj) == expected_canonical, f"canonical drift: {path}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main-v23-root", required=True)
    args = ap.parse_args()
    main_v23 = Path(args.main_v23_root).resolve()

    n385 = checked(
        HERE.parent / "N385" / "STATE.json",
        EXPECTED_N385_BLOB,
        EXPECTED_N385_CANONICAL,
    )
    n372 = checked(
        HERE.parent / "N372" / "STATE.json",
        EXPECTED_N372_BLOB,
        EXPECTED_N372_CANONICAL,
    )

    n386_path = HERE / "STATE.json"
    n386 = load(n386_path)
    req(
        n386["canonical_sha256_without_this_field"] == EXPECTED_N386_CANONICAL,
        "N386 stored canonical drift",
    )
    req(canonical(n386) == EXPECTED_N386_CANONICAL, "N386 canonical drift")

    req(head(main_v23) == EXPECTED_V23_HEAD, "V23 exact head drift")
    v23 = checked(
        main_v23 / "stages/stage32/MAIN-STATE.json",
        EXPECTED_V23_BLOB,
        EXPECTED_V23_CANONICAL,
    )
    hp1 = checked(
        main_v23 / "stages/stage32/management/hpadj-01/RESULT.json",
        EXPECTED_HPADJ01_BLOB,
        EXPECTED_HPADJ01_CANONICAL,
    )

    req(
        n385["status"]
        == "CERTLIFT03_V23_HOSTILE_AUDITED_MAIN_AUTHORITY_SYNC_NO_NEW_LOCAL_CREDIT",
        "N385 status drift",
    )
    req(
        n385["main_v23_authority"]["exact_head"] == EXPECTED_V23_HEAD,
        "N385 V23 head drift",
    )
    req(
        n385["main_v23_authority"]["hostile_audit_review_id"] == EXPECTED_V23_REVIEW,
        "N385 V23 hostile audit review drift",
    )
    req(
        n385["authority_sync"]["latest_hostile_audited_main_authority_visible_to_178"]
        is True,
        "N385 authority visibility drift",
    )
    req(n385["n101_contract"]["remains_stopped"] is True, "N101 stop drift")

    req(n372["target"]["terminal_identity"] == EXPECTED_N372_TERMINAL, "N372 terminal drift")
    req(n372["target"]["row_id"] == "g1-d008", "N372 row drift")
    req(n372["target"]["g"] == 1, "N372 genus drift")
    req(n372["target"]["d"] == 8 and n372["target"]["e"] == 8, "N372 d/e drift")
    req(n372["target"]["terminal_rank"] == 128820, "N372 rank drift")
    req(n372["witness_summary"]["self_square"] == -4, "N372 self-square drift")
    req(
        n372["witness_summary"]["negative_hperp_square_N"] == 32,
        "N372 Hperp N drift",
    )

    frontier = v23["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == 17128, "V23 strata drift")
    req(
        frontier["authoritative_remaining_terminals"] == EXPECTED_V23_TERMINALS,
        "V23 terminal authority drift",
    )
    req(frontier["n372_terminal_identity"] == EXPECTED_N372_TERMINAL, "V23 N372 identity drift")
    req(frontier["n372_candidate_hostile_audit_review_id"] == EXPECTED_N372_REVIEW, "V23 N372 review drift")
    req(frontier["n372_candidate_hostile_audited"] is True, "V23 N372 audit drift")
    req(frontier["n372_current_authority_witness"] is True, "V23 N372 witness drift")
    req(
        frontier["n372_survives_batch_cut193_cut197_cut198"] is True,
        "V23 N372 batch-cut survival drift",
    )
    req(frontier["n372_survives_certlift03"] is True, "V23 N372 CERTLIFT survival drift")
    req(frontier["n372_main_pruning_credit"] is False, "V23 N372 pruning credit drift")
    req(frontier["n372_full178_credit"] is False, "V23 N372 FULL178 credit drift")
    req(
        frontier["n372_effectivity_final_credit"] is False,
        "V23 N372 effectivity credit drift",
    )
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")
    req(frontier["stage32_closed"] is False, "Stage32 unexpectedly closed")

    req(
        hp1["status"]
        == "RETAINED_CURRENT_V22_ENDPOINT_NECESSARY_FILTER_CANDIDATE_NO_MAIN_CREDIT",
        "HPADJ-01 status drift",
    )
    req(hp1["authority_input"]["main_v22_exact_head"] == EXPECTED_V22_HEAD, "HPADJ-01 V22 basis drift")
    req(
        hp1["current_v22_intersection_lower_bound"]["affected_rows"] == 178,
        "HPADJ-01 row coverage drift",
    )
    req(
        hp1["current_v22_intersection_lower_bound"]["candidate_endpoint_rejected_terminals_lower_bound"]
        == EXPECTED_HPADJ01_CHARGED,
        "HPADJ-01 charged lower bound drift",
    )
    req(
        hp1["composition_firewall"]["all_g1_d008_e8_conservatively_excluded"] is True,
        "HPADJ-01 g1-d008/e8 exclusion firewall drift",
    )
    method = hp1["current_v22_intersection_lower_bound"]["method"]
    req(
        "conservatively exclude entire g1-d008/e8 stratum" in method,
        "HPADJ-01 method lost g1-d008/e8 exclusion",
    )
    req(
        hp1["necessary_condition"]["irreducible_k3_adjunction"] == "C^2 >= -2",
        "HPADJ-01 adjunction condition drift",
    )
    req(
        hp1["necessary_condition"]["exact_terminal_necessary_condition"]
        == "8*sum(y_i^2) <= d^2 + 32",
        "HPADJ-01 terminal condition drift",
    )
    req(
        "irreducible K3 carrier" in hp1["promotion_gap"]["missing_adapter"],
        "HPADJ-01 carrier adapter gap drift",
    )
    req(
        "do not subtract from FULL178 numerical authority" in hp1["promotion_gap"]["until_adapter"],
        "HPADJ-01 no-credit gap drift",
    )
    for key, value in hp1["firewalls"].items():
        req(value is False, f"HPADJ-01 firewall unexpectedly opened: {key}")

    req(
        n386["status"]
        == "HPADJ01_EXPLICITLY_EXCLUDES_N372_G1D008_E8_FROM_CHARGED_LOWER_BOUND_NO_TRANSFER_NO_CREDIT",
        "N386 status drift",
    )
    req(
        n386["hpadj01_scope"]["all_g1_d008_e8_conservatively_excluded"] is True,
        "N386 exclusion mirror drift",
    )
    req(
        n386["hpadj01_scope"]["n372_is_in_hpadj01_charged_lower_bound_population"] is False,
        "N386 illegally places N372 in HPADJ charged population",
    )
    req(
        n386["hpadj01_scope"]["n372_pruning_transfer_permitted"] is False,
        "N386 pruning transfer firewall opened",
    )
    req(
        n386["hpadj01_scope"]["self_square_minus4_alone_proves_hpadj_terminal_rejection"] is False,
        "N386 self-square overclaim opened",
    )
    req(
        n386["semantic_firewall"]["population_measure_transfer_without_explicit_adapter_forbidden"] is True,
        "N386 population adapter firewall drift",
    )
    req(n386["semantic_firewall"]["double_charge_forbidden"] is True, "N386 double-charge firewall drift")
    req(
        n386["routing"]["duplicate_ex5_hpadj_terminal_to_picard64_producer_work"] is False,
        "N386 duplicates external HPADJ producer work",
    )
    req(n386["routing"]["n101_remains_stopped"] is True, "N386 illegally reopens N101")
    req(n386["routing"]["heavy_compute_authorized"] is False, "N386 heavy compute drift")
    for key, value in n386["credit"].items():
        req(value is False, f"N386 credit unexpectedly opened: {key}")

    print(json.dumps({
        "verdict": "PASS_N386_HPADJ01_N372_G1D008_E8_NONTRANSFER_FIREWALL",
        "main_v23_exact_head": EXPECTED_V23_HEAD,
        "main_v23_audit_review": EXPECTED_V23_REVIEW,
        "n372_terminal_identity": EXPECTED_N372_TERMINAL,
        "n372_self_square": -4,
        "n372_in_hpadj01_charged_lower_bound_population": False,
        "hpadj01_g1_d008_e8_conservatively_excluded": True,
        "hpadj01_charged_lower_bound": EXPECTED_HPADJ01_CHARGED,
        "n386_additional_pruning_terminals": 0,
        "n101_reopened": False,
        "full178_complete": False,
        "stage32_closed": False,
        "merge_authorized": False,
        "next_gate": n386["next_gate"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
