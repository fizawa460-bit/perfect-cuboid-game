#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "V48-FULL-SUPPORT-384-EQUIV-DERIVED-BOUND-RETAINED.json"
PRIOR = HERE / "V48-FULL-SUPPORT-384-MIN-BOUND-RETAINED.json"
EQ = HERE / "V48-LEGACY-B47-WORKER-EQUIVALENCE-PREFLIGHT.json"
EQ_VERIFY = HERE / "verify_v48_legacy_b47_worker_equivalence_preflight.py"
LEGACY_RECEIPT = HERE / "local-support-qbc/row022-b047.json"
PREPARED_AGG = HERE / "aggregate_v48_full_support_384_equiv_min_bound.py"

CERT_BLOB = "3acb9551db9fda6be8fde0194b23ddb41ca634d0"
CERT_CANON = "da7eb532daf2b775a49524fe45e5b7bf7851719f19a6926a227f5fa745258aba"
PRIOR_BLOB = "4d6d811015b6b1cdf660ab337864f8c19aab07aa"
PRIOR_CANON = "35b21eebce181747ad4b0511873fa09009b4258f3f9e408bbca4e2c3cecf88e8"
EQ_BLOB = "9c62b906aaa74af8838752f952190ca416c9bbc7"
EQ_CANON = "4cf78a12cbaab9efc11309aaf055e526d4c53322614ee421662d7cbe33ce01f2"
EQ_VERIFY_BLOB = "242389044b916a98ab81f2817a2390ad9b33b01e"
LEGACY_RECEIPT_BLOB = "0f161fa0df18966a8bc38f0160edd76f4f9cc1fe"
LEGACY_RECEIPT_CANON = "2bbc6957864fcb439dc991a26a3ea223d6f3169af7352df8b28966a058a8b47b"
PREPARED_AGG_BLOB = "d2008f43d8a1c718a7466c3913086cd65dbb965e"

V48_TOTAL = 128470212118313474449
COVERED_TOTAL = 37911631052805557219
SUM_383 = 37735096385453088954
B47_V48_CURRENT = 176534667352468265
B47_FULL_SUPPORT = 176436593457463322
B47_EXTRA = 98073895004943
PRIOR_TIGHTENING = 26892956458889546
TOTAL_TIGHTENING = 26991030353894489
CANDIDATE = 128443221087959579960


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    for path, expected, label in (
        (CERT, CERT_BLOB, "derived certificate"),
        (PRIOR, PRIOR_BLOB, "prior 383 certificate"),
        (EQ, EQ_BLOB, "b47 equivalence preflight"),
        (EQ_VERIFY, EQ_VERIFY_BLOB, "b47 equivalence verifier"),
        (LEGACY_RECEIPT, LEGACY_RECEIPT_BLOB, "legacy b47 receipt"),
        (PREPARED_AGG, PREPARED_AGG_BLOB, "prepared 384 equivalence aggregator"),
    ):
        req(path.is_file() and blob(path) == expected, label + " blob drift")

    cert = json.loads(CERT.read_text())
    prior = json.loads(PRIOR.read_text())
    eq = json.loads(EQ.read_text())
    legacy = json.loads(LEGACY_RECEIPT.read_text())

    req(canon(cert) == CERT_CANON == cert["canonical_sha256_without_this_field"], "derived certificate canonical drift")
    req(canon(prior) == PRIOR_CANON == prior["canonical_sha256_without_this_field"], "prior certificate canonical drift")
    req(canon(eq) == EQ_CANON == eq["canonical_sha256_without_this_field"], "equivalence preflight canonical drift")
    req(canon(legacy) == LEGACY_RECEIPT_CANON == legacy["canonical_sha256_without_this_field"], "legacy receipt canonical drift")

    subprocess.run([sys.executable, str(EQ_VERIFY)], check=True)

    cov = prior["coverage"]
    req(int(cov["expected_coordinates"]) == 384, "prior expected coordinate count drift")
    req(int(cov["eligible_current_worker_coordinates"]) == 383, "prior eligible coordinate count drift")
    req(int(cov["strict_replacement_coordinates"]) == 383, "prior strict coordinate count drift")
    req(int(cov["source_ineligible_coordinates"]) == 1, "prior source-ineligible count drift")
    req(int(cov["unchanged_coordinates"]) == 1, "prior unchanged count drift")

    ineligible = prior["source_ineligible_coordinates"]
    req(len(ineligible) == 1, "prior ineligible list size drift")
    req((int(ineligible[0]["row_index"]), int(ineligible[0]["b"])) == (22, 47), "prior ineligible coordinate drift")

    strict = prior["strict_coordinates"]
    req(len(strict) == 383, "prior strict list size drift")
    keys = [(int(x["row_index"]), int(x["b"])) for x in strict]
    req(len(set(keys)) == 383, "prior strict coordinate duplicate")
    req((22, 47) not in set(keys), "b47 unexpectedly present in prior strict list")
    sum383 = sum(int(x["v48_current"]) for x in strict)
    req(sum383 == SUM_383, f"prior strict V48 current sum drift {sum383}")

    covered = int(prior["result"]["covered_v48_current"])
    req(covered == COVERED_TOTAL, "prior covered V48 total drift")
    b47_current = covered - sum383
    req(b47_current == B47_V48_CURRENT, f"derived b47 V48 current drift {b47_current}")

    req(eq["semantics"]["legacy_worker_numerical_kernel_equivalent_to_current_worker_on_row022_b47"] is True, "b47 kernel equivalence missing")
    req(eq["semantics"]["eligible_as_current_worker_equivalent_source_for_future_v48_pointwise_min_replay"] is True, "b47 replacement eligibility missing")
    b47_bound = int(legacy["result"]["support_qbc_refined_survivors"])
    req(b47_bound == B47_FULL_SUPPORT, "legacy b47 full-support bound drift")
    req(b47_bound < b47_current, "b47 is not strict")
    extra = b47_current - b47_bound
    req(extra == B47_EXTRA, f"b47 additional tightening drift {extra}")

    prior_tightening = int(prior["result"]["certified_tightening_vs_v48"])
    req(prior_tightening == PRIOR_TIGHTENING, "prior tightening drift")
    total_tightening = prior_tightening + extra
    req(total_tightening == TOTAL_TIGHTENING, "total tightening drift")
    candidate = V48_TOTAL - total_tightening
    req(candidate == CANDIDATE, "candidate global bound drift")

    req(cert["status"] == "EXACT_DERIVED_384_COORDINATE_UPPER_BOUND_CANDIDATE__ZERO_MAIN_CREDIT", "derived status drift")
    dc = cert["coverage"]
    req(dc == {
        "current_worker_coordinates": 383,
        "eligible_replacement_coordinates": 384,
        "expected_coordinates": 384,
        "gaps": 0,
        "legacy_current_equivalent_coordinates": 1,
        "overlaps": 0,
        "source_ineligible_coordinates": 0,
        "strict_replacement_coordinates": 384,
        "unchanged_coordinates": 0,
    }, "derived coverage drift")
    d = cert["derivation"]
    req(int(d["sum_prior_383_v48_current"]) == SUM_383, "certificate sum383 drift")
    req(int(d["derived_row022_b47_v48_current"]) == B47_V48_CURRENT, "certificate b47 current drift")
    req(int(d["row022_b47_equivalent_full_support_upper_bound"]) == B47_FULL_SUPPORT, "certificate b47 bound drift")
    req(d["row022_b47_strict"] is True, "certificate b47 strict flag drift")
    req(int(d["row022_b47_additional_tightening"]) == B47_EXTRA, "certificate b47 extra drift")
    req(int(d["prior_certified_tightening_vs_v48"]) == PRIOR_TIGHTENING, "certificate prior tightening drift")
    req(int(d["certified_tightening_vs_v48"]) == TOTAL_TIGHTENING, "certificate total tightening drift")
    req(int(d["candidate_global_upper_bound_if_promoted"]) == CANDIDATE, "certificate candidate drift")

    comp = cert["composition"]
    req(comp["additive_subtraction"] is False, "additive subtraction forbidden")
    req(comp["statistical_independence"] is False, "independence assumption forbidden")
    req(comp["exact_intersection_identity_set_claimed"] is False, "identity-set overclaim")
    req(comp["uncovered_v48_population_unchanged"] is True, "uncovered V48 population drift")
    req(cert["semantics"]["main_consumption_performed"] is False, "producer self-consumed")

    for k, v in cert["firewalls"].items():
        if k == "hostile_audit_required_before_promotion":
            req(v is True, "hostile audit firewall drift")
        else:
            req(v is False, "credit firewall drift " + k)

    print("V48_FULL_SUPPORT_384_EQUIV_DERIVED_BOUND_RETAINED=PASS")
    print("ROW022_B47_V48_CURRENT=176534667352468265")
    print("ROW022_B47_FULL_SUPPORT=176436593457463322")
    print("ROW022_B47_ADDITIONAL_TIGHTENING=98073895004943")
    print("CERTIFIED_TIGHTENING_VS_V48=26991030353894489")
    print("CANDIDATE_GLOBAL_UPPER_BOUND=128443221087959579960")
    print("MAIN_CREDIT_CHANGED=false")
    print("HOSTILE_AUDIT_REQUIRED=true")


if __name__ == "__main__":
    main()
