#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
N378 = HERE / "STATE.json"
N377 = HERE.parent / "N377/STATE.json"

N378_BLOB = "5ddd2379750d291a3b77d630479335ff02a159c3"
N378_CANON = "6312c0d2a49b2407c6fb431c5a845010a1eea38c268c6cfe7400685d73a17bca"
N377_BLOB = "ecbba41447f089ebd5100859b62d5d5ab75a16ca"
N377_CANON = "0086b11b55f77ee8cd852ff0557d1a2b1f952f50fb312f72faa747d5423874a4"

CERTLIFT_HEAD = "007e0591e94e475caf348aa82c39837368f3e5c0"
CERTLIFT_STATE_REL = Path("stages/stage32/cut-cert-lift/STATE.json")
CERTLIFT_STATE_BLOB = "176fdcb1c628365bec8613469e00031654283589"
CERTLIFT_METHOD_REL = Path("stages/stage32/cert-lift/CERTLIFT-02-MOD2-EXACT.md")
CERTLIFT_METHOD_BLOB = "ca597d363c5755aed996a31e7cf5f14ae3ede4c4"
CERTLIFT_SCRIPT_REL = Path("stages/stage32/cert-lift/mass7_mod2_obstruction.py")
CERTLIFT_SCRIPT_BLOB = "ca0d55645db71c065185c56442532def5563898e"
CERTLIFT_LEDGER_REL = Path("stages/stage32/cert-lift/CERTIFICATE-LEDGER.json")
CERTLIFT_LEDGER_BLOB = "befce1cd6cd3fe9be9d91cb4b4f176283983bac1"

MAIN_V22_HEAD = "f8039b4ce479a4b91f2f0547e7049f629e9be5f5"
MAIN_STATE_REL = Path("stages/stage32/MAIN-STATE.json")
MAIN_STATE_BLOB = "80fb35c79854bfdf775dc5b94c331f5f8a535ced"
MAIN_STATE_CANON = "82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected_blob: str, expected_canon: str | None = None) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
        req(canonical(obj) == expected_canon, f"canonical replay drift: {path}")
    return obj


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certlift-root", type=Path, required=True)
    ap.add_argument("--main-v22-root", type=Path, required=True)
    args = ap.parse_args()

    n377 = checked(N377, N377_BLOB, N377_CANON)
    n378 = checked(N378, N378_BLOB, N378_CANON)

    certroot = args.certlift_root.resolve()
    req(exact_head(certroot) == CERTLIFT_HEAD, "CERT-LIFT exact head drift")
    producer = checked(certroot / CERTLIFT_STATE_REL, CERTLIFT_STATE_BLOB)
    req(blob(certroot / CERTLIFT_METHOD_REL) == CERTLIFT_METHOD_BLOB, "CERTLIFT-02 method-note blob drift")
    req(blob(certroot / CERTLIFT_SCRIPT_REL) == CERTLIFT_SCRIPT_BLOB, "CERTLIFT-02 discriminator blob drift")
    req(blob(certroot / CERTLIFT_LEDGER_REL) == CERTLIFT_LEDGER_BLOB, "CERTLIFT certificate-ledger blob drift")

    mainroot = args.main_v22_root.resolve()
    req(exact_head(mainroot) == MAIN_V22_HEAD, "MAIN V22 audited exact head drift")
    main_state = checked(mainroot / MAIN_STATE_REL, MAIN_STATE_BLOB, MAIN_STATE_CANON)

    req(n377["status"] == "WAITING_ON_CERTLIFT_EXACT_SIGNATURE_NO_CREDIT", "N377 parent status drift")
    req(n378["parent"]["n377_state_blob_sha1"] == N377_BLOB, "N378 parent blob drift")
    req(n378["parent"]["n377_state_canonical_sha256"] == N377_CANON, "N378 parent canonical drift")
    req(n378["status"] == "WAITING_CERTLIFT02_EXECUTION_AND_V22_ADAPTER_NO_CREDIT", "N378 status drift")

    req(producer["schema"] == "STAGE32_CUT_CERT_LIFT_STATE_V1", "CERT-LIFT schema drift")
    req(producer["status"] == "ACTIVE", "CERT-LIFT status drift")
    req(producer["active_node"] == "CERTLIFT-02_INVARIANT_COMPRESSION_AND_COUNTEREXAMPLE_SPLIT", "CERT-LIFT active node drift")
    req(producer["base_main_exact_head"] == "b6c0a1e431ac04de5326a7c42af89a7b92423ed2", "CERT-LIFT base MAIN drift")
    c1 = producer["certlift_01"]
    req(c1["status"] == "L1_AUDITED_SEPARATOR_FOUND", "CERTLIFT-01 status drift")
    req(c1["predicate"] == "fixed_exceptional_mass >= 7", "MASS7 predicate drift")
    req(c1["selected_closed_blocks"] == 1049 and c1["selected_residual_controls"] == 0, "MASS7 audited split drift")
    req("not yet a symbolic lemma" in c1["interpretation"], "MASS7 promotion firewall drift")
    req(producer["current_work"]["exact_discriminator"] == str(CERTLIFT_SCRIPT_REL), "CERTLIFT-02 discriminator path drift")
    req(producer["current_work"]["primary_scope"] == "all current-MAIN e8 prefix-surviving blocks", "CERTLIFT-02 primary scope drift")
    req(producer["current_work"]["challenge_scope"] == "entire 11,318-block compressed e8 terminal universe before N220/N355 filtering", "CERTLIFT-02 challenge scope drift")
    req(producer["credit"]["main_pruning"] is False and producer["credit"]["full178"] is False, "producer credit firewall drift")

    req(main_state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V22_BATCH_CUT193_CUT197_CUT198_CONSUMED", "MAIN V22 schema drift")
    frontier = main_state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == 17128, "MAIN V22 strata drift")
    req(frontier["authoritative_remaining_terminals"] == 47589703313957134804198, "MAIN V22 terminal count drift")
    req(frontier["full178_numerical_census_complete"] is False, "MAIN V22 FULL178 unexpectedly complete")

    req(n378["producer"]["exact_head"] == CERTLIFT_HEAD, "N378 producer head drift")
    req(n378["producer"]["state_blob_sha1"] == CERTLIFT_STATE_BLOB, "N378 producer state blob drift")
    req(n378["producer"]["producer_result_consumable_now"] is False, "N378 prematurely consumes producer")
    req(n378["producer"]["certlift02"]["implementation_ready"] is True, "N378 CERTLIFT-02 implementation observation drift")
    req(n378["producer"]["certlift02"]["execution_result_promoted"] is False, "N378 CERTLIFT-02 promotion observation drift")
    req(n378["producer"]["certlift02"]["required_pass_token"] == "PASS_MASS7_EXACT_MOD2_OBSTRUCTION", "N378 pass token drift")
    req(n378["producer"]["certlift02"]["zero_counterexamples_required"] is True, "N378 zero-counterexample gate drift")

    req(n378["live_authority"]["audited_exact_head"] == MAIN_V22_HEAD, "N378 live authority head drift")
    req(n378["live_authority"]["main_state_blob_sha1"] == MAIN_STATE_BLOB, "N378 live authority blob drift")
    req(n378["authority_gap"]["producer_base_equals_live_audited_authority"] is False, "authority-gap boolean drift")
    req(n378["authority_gap"]["exact_adapter_required_before_live_consumption"] is True, "authority adapter firewall drift")
    req(n378["route_split"]["n101_compression_route"]["remains_stopped"] is True, "N101 route unexpectedly reopened")
    req(n378["route_split"]["n101_compression_route"]["mass7_exact_obstruction_alone_reopens_n101"] is False, "MASS7/N101 firewall drift")

    for key, value in n378["credit"].items():
        req(value is False, f"N378 credit firewall drift: {key}")
    req(all(value is False for value in n378["anti_loop"].values()), "N378 anti-loop/heavy firewall drift")

    print(json.dumps({
        "verdict": "PASS_N378_CERTLIFT02_EXECUTION_AND_V22_ADAPTER_WAIT_BOUNDARY",
        "producer_pr": 1803,
        "producer_exact_head": CERTLIFT_HEAD,
        "producer_active_node": producer["active_node"],
        "mass7_selected_closed_blocks": c1["selected_closed_blocks"],
        "mass7_selected_residual_controls": c1["selected_residual_controls"],
        "certlift02_execution_result_promoted": False,
        "live_main_audited_version": "V22",
        "live_main_audited_exact_head": MAIN_V22_HEAD,
        "authority_adapter_required": True,
        "producer_result_consumable_now": False,
        "n101_compression_route_remains_stopped": True,
        "next_gate": n378["next_gate"],
        "main_pruning_credit": False,
        "full178_complete": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
