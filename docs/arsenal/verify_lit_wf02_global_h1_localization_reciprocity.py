#!/usr/bin/env python3
"""Fail-closed structural verifier for provisional Arsenal workflow LIT-WF02.

This verifies typed provenance/readiness only. It does not verify the mathematics of a
proposed global H1/Kummer adapter or prove any literature theorem/obstruction.
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT_PATH = HERE / "lit-wf02-global-h1-localization-reciprocity-contract.json"
PACKAGE_SCHEMA = "LIT-WF02-GLOBAL-H1-LOCALIZATION-PACKAGE-V1"


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: Path):
    return json.loads(path.read_text())


def verify_contract() -> dict:
    c = load_json(CONTRACT_PATH)
    assert c["schema"] == "LIT-WF02-GLOBAL-H1-LOCALIZATION-RECIPROCITY-CONTRACT-V1"
    assert c["stable_id"] == "LIT-WF02"
    assert c["candidate_id"] == "GLOBAL-H1-LOCALIZATION-RECIPROCITY-AUDIT"
    assert c["role"] == "GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW"
    assert c["kind"] == "workflow" and c["maturity"] == "PROVISIONAL"
    assert c["discovery_pr"] == 1690
    assert c["discovery_exact_head"] == "f1a2d3074e802b0fd4555cb827e165c3de2bdfc9"
    assert c["arsenal_base_main"] == "386b6a52d7bfec2e8903412c7ca56976b46c288b"
    assert c["stage36_arsenal_source_head"] == "2fc3f4b8afb28bb23765bd861cbd7c52aafd6563"
    assert c["verifier"] == "docs/arsenal/verify_lit_wf02_global_h1_localization_reciprocity.py"
    assert len(c["literature"]) == 2
    for paper in c["literature"]:
        for key in ("authors", "title", "publisher", "year", "canonical_url", "theorem_identifier", "conclusion_summary", "source_type"):
            if paper.get(key) in (None, ""):
                fail(f"literature metadata missing: {key}")
        if not (paper.get("doi") or paper.get("canonical_url")):
            fail("literature locator missing DOI/URL")
    firewall = c["credit_firewall"]
    assert firewall["repo_theorem_credit"] is False
    for key in (
        "stage36_progress_increment", "stage36_theorem_credit_increment",
        "receiver_closure_increment", "mw_closure_increment",
        "local_global_obstruction_increment", "endpoint_credit_increment",
    ):
        assert firewall[key] == 0
    return c


def verify_package(package_path: Path, contract: dict) -> None:
    p = load_json(package_path)
    if p.get("schema") != PACKAGE_SCHEMA:
        fail(f"schema must be {PACKAGE_SCHEMA}")
    for key in contract["pass_package_required_fields"]:
        if key not in p:
            fail(f"missing required field: {key}")

    if not isinstance(p["global_field"], str) or not p["global_field"].strip():
        fail("global_field must be a fixed named global field")
    if not isinstance(p["global_module_or_class"], dict) or not p["global_module_or_class"]:
        fail("global_module_or_class must be a nonempty named object")

    sb = p["source_binding"]
    if not isinstance(sb, dict):
        fail("source_binding must be an object")
    for key in ("path", "blob_sha", "exact_head"):
        if not sb.get(key):
            fail(f"source_binding missing {key}")
    if len(sb["blob_sha"]) != 40 or len(sb["exact_head"]) != 40:
        fail("source_binding blob/head must be full 40-hex provenance")

    locs = p["localizations"]
    if not isinstance(locs, list) or not locs:
        fail("localizations must be a nonempty complete list")
    seen_places = set()
    for i, loc in enumerate(locs):
        if not isinstance(loc, dict):
            fail(f"localization[{i}] must be an object")
        for key in ("place", "source_row_or_chart", "localized_class", "localization_verifier"):
            if not loc.get(key):
                fail(f"localization[{i}] missing {key}")
        place = str(loc["place"])
        if place in seen_places:
            fail(f"duplicate place: {place}")
        seen_places.add(place)
        lv = loc["localization_verifier"]
        if not isinstance(lv, dict) or not lv.get("path") or not lv.get("blob_sha"):
            fail(f"localization[{i}] lacks exact mathematical verifier provenance")
        if len(lv["blob_sha"]) != 40:
            fail(f"localization[{i}] verifier blob is not full SHA")

    for key in ("required_places_complete", "dyadic_handled", "real_places_handled"):
        if p[key] is not True:
            fail(f"{key} must be true for PASS")

    if not isinstance(p["field_change_semantics"], str) or not p["field_change_semantics"].strip():
        fail("field_change_semantics must be explicit")

    fs = p.get("finite_support_assumption")
    if fs is not None:
        if not isinstance(fs, dict) or fs.get("used") not in (True, False):
            fail("finite_support_assumption must state used=true/false")
        if fs["used"] and not (fs.get("proof_path") and fs.get("proof_blob_sha")):
            fail("finite-support use requires exact proof provenance")
        if fs.get("proof_blob_sha") and len(fs["proof_blob_sha"]) != 40:
            fail("finite-support proof blob must be full SHA")

    lbs = p["literature_bindings"]
    if not isinstance(lbs, list) or not lbs:
        fail("literature_bindings must be nonempty")
    for i, binding in enumerate(lbs):
        if not isinstance(binding, dict):
            fail(f"literature_binding[{i}] must be an object")
        for key in ("source", "theorem_identifier", "hypotheses_checked"):
            if key not in binding:
                fail(f"literature_binding[{i}] missing {key}")
        if binding["hypotheses_checked"] is not True:
            fail(f"literature_binding[{i}] hypotheses are not certified")

    av = p["adapter_mathematical_verifier"]
    if not isinstance(av, dict) or not av.get("path") or not av.get("blob_sha") or not av.get("exact_head"):
        fail("PASS requires a separately proved adapter_mathematical_verifier")
    if len(av["blob_sha"]) != 40 or len(av["exact_head"]) != 40:
        fail("adapter mathematical verifier provenance must use full SHAs")

    if p.get("claims", {}) != {
        "literature_theorem_proved_by_repo": False,
        "local_global_obstruction": False,
        "receiver_closure": False,
        "endpoint_credit": False,
    }:
        fail("claims firewall must be exactly false for theorem/obstruction/receiver/endpoint")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", nargs="?", help="typed LIT-WF02 package to verify")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        contract = verify_contract()
        if args.package:
            verify_package(Path(args.package), contract)
            print("PASS: LIT-WF02 typed global-H1/localization package is structurally ready for separately cited literature theorem use; mathematical credit remains zero")
        else:
            print("PASS: LIT-WF02 contract/source metadata self-check; no mathematical adapter or obstruction is inferred")
        return 0
    except Exception as exc:
        print(f"FAIL_CLOSED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
