#!/usr/bin/env python3
"""Fail-closed applicability verifier for provisional Arsenal workflow LIT-WF02.

A package PASS is allowed only after immutable repository provenance is resolved to the
claimed Git objects, source/global-class/place evidence is bound, method-specific
mathematical verifiers are executed from their exact committed head, and literature
bindings match the Phase-3-frozen theorem locators/hypotheses in the contract.

`--self-check` validates only the workflow implementation/contract and adversarial
fail-close behavior. It is deliberately not an applicability PASS.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
CONTRACT_PATH = HERE / "lit-wf02-global-h1-localization-reciprocity-contract.json"
PACKAGE_SCHEMA = "LIT-WF02-GLOBAL-H1-LOCALIZATION-PACKAGE-V2"
PASS_EVIDENCE_SCHEMA = "LIT-WF02-IMMUTABLE-MATHEMATICAL-PASS-EVIDENCE-V1"
HEX40 = re.compile(r"^[0-9a-f]{40}$")


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: Path):
    return json.loads(path.read_text())


def require_hex40(value, label: str) -> str:
    if not isinstance(value, str) or not HEX40.fullmatch(value):
        fail(f"{label} must be a full lowercase 40-hex SHA")
    return value


def require_repo_relpath(value, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be a nonempty repo-relative path")
    p = Path(value)
    if p.is_absolute() or ".." in p.parts:
        fail(f"{label} must stay inside the repository")
    return p.as_posix()


def git(*args: str, cwd: Path | None = None) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=str(cwd or REPO_ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        fail(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout.strip()


def require_git_checkout() -> None:
    top = Path(git("rev-parse", "--show-toplevel")).resolve()
    if top != REPO_ROOT.resolve():
        fail(f"verifier must run in repository checkout {REPO_ROOT}; got {top}")


def verify_commit(head: str, label: str) -> None:
    require_hex40(head, label)
    kind = git("cat-file", "-t", head)
    if kind != "commit":
        fail(f"{label} does not resolve to a commit")


def git_blob_at(head: str, path: str) -> str:
    verify_commit(head, "exact_head")
    path = require_repo_relpath(path, "path")
    blob = git("rev-parse", f"{head}:{path}")
    require_hex40(blob, f"blob at {head}:{path}")
    if git("cat-file", "-t", blob) != "blob":
        fail(f"{head}:{path} does not resolve to a blob")
    return blob


def verify_bound_blob(binding: dict, label: str) -> dict:
    if not isinstance(binding, dict):
        fail(f"{label} must be an object")
    path = require_repo_relpath(binding.get("path"), f"{label}.path")
    blob_sha = require_hex40(binding.get("blob_sha"), f"{label}.blob_sha")
    exact_head = require_hex40(binding.get("exact_head"), f"{label}.exact_head")
    actual = git_blob_at(exact_head, path)
    if actual != blob_sha:
        fail(f"{label} blob mismatch: claimed {blob_sha}, actual {actual} at {exact_head}:{path}")
    return {"path": path, "blob_sha": blob_sha, "exact_head": exact_head}


def load_json_from_git(head: str, path: str):
    path = require_repo_relpath(path, "git_json.path")
    actual_blob = git_blob_at(head, path)
    proc = subprocess.run(
        ["git", "show", f"{head}:{path}"],
        cwd=str(REPO_ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        fail(f"cannot read {head}:{path}: {proc.stderr.strip()}")
    try:
        return json.loads(proc.stdout), actual_blob
    except Exception as exc:
        fail(f"invalid JSON at {head}:{path}: {exc}")


def materialize_blob(head: str, path: str, destination: Path) -> None:
    proc = subprocess.run(
        ["git", "show", f"{head}:{path}"],
        cwd=str(REPO_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        fail(f"cannot materialize {head}:{path}: {proc.stderr.decode(errors='replace').strip()}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(proc.stdout)


def verify_evidence_binding(binding: dict, label: str) -> dict:
    b = verify_bound_blob(binding, label)
    if not b["path"].endswith(".json"):
        fail(f"{label}.path must be immutable JSON evidence")
    return b


def run_mathematical_verifier(verifier_binding: dict, evidence_binding: dict, subject: str, label: str) -> dict:
    v = verify_bound_blob(verifier_binding, f"{label}.verifier")
    e = verify_evidence_binding(evidence_binding, f"{label}.evidence")
    if v["exact_head"] != e["exact_head"]:
        fail(f"{label} verifier/evidence exact_head mismatch")
    if not v["path"].endswith(".py"):
        fail(f"{label} verifier must be a Python verifier")
    if not isinstance(subject, str) or not subject.strip():
        fail(f"{label}.subject must be nonempty")

    with tempfile.TemporaryDirectory(prefix="lit-wf02-") as td:
        root = Path(td)
        verifier_path = root / "verifier.py"
        evidence_path = root / "evidence.json"
        materialize_blob(v["exact_head"], v["path"], verifier_path)
        materialize_blob(e["exact_head"], e["path"], evidence_path)
        proc = subprocess.run(
            [sys.executable, str(verifier_path), "--verify-evidence", str(evidence_path), "--json"],
            cwd=str(root),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120,
        )
        if proc.returncode != 0:
            fail(f"{label} mathematical verifier failed: {proc.stderr.strip() or proc.stdout.strip()}")
        lines = [line for line in proc.stdout.splitlines() if line.strip()]
        if not lines:
            fail(f"{label} mathematical verifier emitted no JSON PASS evidence")
        try:
            out = json.loads(lines[-1])
        except Exception as exc:
            fail(f"{label} mathematical verifier final line is not JSON: {exc}")
        expected = {
            "schema": PASS_EVIDENCE_SCHEMA,
            "status": "PASS",
            "subject": subject,
            "verifier_path": v["path"],
            "verifier_blob_sha": v["blob_sha"],
            "evidence_path": e["path"],
            "evidence_blob_sha": e["blob_sha"],
            "exact_head": v["exact_head"],
        }
        for key, value in expected.items():
            if out.get(key) != value:
                fail(f"{label} PASS evidence mismatch for {key}: expected {value!r}, got {out.get(key)!r}")
        return out


def frozen_literature_key(paper: dict) -> tuple[str, str, str]:
    return (paper["title"], paper["theorem_identifier"], paper["canonical_url"])


def verify_contract() -> dict:
    require_git_checkout()
    c = load_json(CONTRACT_PATH)
    assert c["schema"] == "LIT-WF02-GLOBAL-H1-LOCALIZATION-RECIPROCITY-CONTRACT-V2"
    assert c["package_schema"] == PACKAGE_SCHEMA
    assert c["immutable_pass_evidence_schema"] == PASS_EVIDENCE_SCHEMA
    assert c["stable_id"] == "LIT-WF02"
    assert c["candidate_id"] == "GLOBAL-H1-LOCALIZATION-RECIPROCITY-AUDIT"
    assert c["role"] == "GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW"
    assert c["kind"] == "workflow" and c["maturity"] == "PROVISIONAL"
    assert c["discovery_pr"] == 1690
    assert c["discovery_exact_head"] == "f1a2d3074e802b0fd4555cb827e165c3de2bdfc9"
    assert c["phase3_freeze_path"] == "docs/arsenal/literature-stage36-hostile-freeze.json"
    assert c["phase3_freeze_blob_sha"] == "d3f90093c0a6655da9874c9141b15ab4682c4409"
    freeze, freeze_blob = load_json_from_git(c["discovery_exact_head"], c["phase3_freeze_path"])
    if freeze_blob != c["phase3_freeze_blob_sha"]:
        fail("Phase3 freeze blob does not match the frozen discovery head")
    workflow_rows = [
        row for row in freeze.get("accepted_item_metadata", [])
        if row.get("candidate_id") == "GLOBAL-H1-LOCALIZATION-RECIPROCITY-AUDIT"
    ]
    if len(workflow_rows) != 1:
        fail("Phase3 freeze must contain exactly one GLOBAL-H1 workflow candidate")
    frozen_workflow = workflow_rows[0]
    if frozen_workflow.get("proposed_role") != c["role"]:
        fail("contract role differs from Phase3 freeze")
    if frozen_workflow.get("exact_reusable_contract") != c["phase3_exact_reusable_contract"]:
        fail("contract semantics differ from Phase3 freeze")
    freeze_lit = {
        (x.get("title"), x.get("theorem"), x.get("doi"))
        for x in frozen_workflow.get("literature", [])
    }
    contract_lit = {
        (x.get("title"), x.get("theorem_identifier"), x.get("doi"))
        for x in c["literature"]
    }
    if contract_lit != freeze_lit:
        fail("Serre/Milne theorem locators differ from Phase3 freeze")
    assert c["arsenal_base_main"] == "386b6a52d7bfec2e8903412c7ca56976b46c288b"
    assert c["stage36_arsenal_source_head"] == "2fc3f4b8afb28bb23765bd861cbd7c52aafd6563"
    assert c["verifier"] == "docs/arsenal/verify_lit_wf02_global_h1_localization_reciprocity.py"
    assert c["self_check_is_applicability_pass"] is False
    assert c["current_stage36_applicability_status"] == "FAIL_CLOSED_MISSING_GLOBAL_CLASS_AND_LOCALIZATION_ADAPTER_EVIDENCE"
    assert len(c["literature"]) == 2
    keys = set()
    for paper in c["literature"]:
        for key in (
            "authors", "title", "publisher", "year", "canonical_url", "theorem_identifier",
            "conclusion_summary", "source_type", "exact_hypotheses_summary", "conditional_assumptions",
        ):
            if paper.get(key) in (None, ""):
                fail(f"literature metadata missing: {key}")
        if not (paper.get("doi") or paper.get("canonical_url")):
            fail("literature locator missing DOI/URL")
        keys.add(frozen_literature_key(paper))
    if len(keys) != 2:
        fail("frozen literature bindings must be unique")
    firewall = c["credit_firewall"]
    assert firewall["repo_theorem_credit"] is False
    for key in (
        "stage36_progress_increment", "stage36_theorem_credit_increment",
        "receiver_closure_increment", "mw_closure_increment",
        "local_global_obstruction_increment", "endpoint_credit_increment",
    ):
        assert firewall[key] == 0
    return c


def verify_literature_bindings(bindings: list, contract: dict) -> None:
    if not isinstance(bindings, list) or not bindings:
        fail("literature_bindings must be nonempty")
    frozen = {frozen_literature_key(p): p for p in contract["literature"]}
    seen = set()
    for i, binding in enumerate(bindings):
        if not isinstance(binding, dict):
            fail(f"literature_binding[{i}] must be an object")
        for key in (
            "title", "theorem_identifier", "canonical_url", "exact_hypotheses_summary",
            "conditional_assumptions", "hypotheses_evidence", "hypotheses_verifier", "subject",
        ):
            if binding.get(key) in (None, ""):
                fail(f"literature_binding[{i}] missing {key}")
        key = (binding["title"], binding["theorem_identifier"], binding["canonical_url"])
        paper = frozen.get(key)
        if paper is None:
            fail(f"literature_binding[{i}] is not one of the Phase-3-frozen theorem locators")
        if binding["exact_hypotheses_summary"] != paper["exact_hypotheses_summary"]:
            fail(f"literature_binding[{i}] hypotheses summary does not match frozen contract")
        if binding["conditional_assumptions"] != paper["conditional_assumptions"]:
            fail(f"literature_binding[{i}] conditional assumptions do not match frozen contract")
        if paper.get("doi") != binding.get("doi"):
            fail(f"literature_binding[{i}] DOI does not match frozen contract")
        run_mathematical_verifier(
            binding["hypotheses_verifier"],
            binding["hypotheses_evidence"],
            binding["subject"],
            f"literature_binding[{i}]",
        )
        seen.add(key)
    if seen != set(frozen):
        fail("PASS requires bindings for both Phase-3-frozen Serre and Milne theorem entries")


def verify_package(package_path: Path, contract: dict) -> None:
    p = load_json(package_path)
    if p.get("schema") != PACKAGE_SCHEMA:
        fail(f"schema must be {PACKAGE_SCHEMA}")
    for key in contract["pass_package_required_fields"]:
        if key not in p:
            fail(f"missing required field: {key}")

    if not isinstance(p["global_field"], str) or not p["global_field"].strip():
        fail("global_field must be a fixed named global field")

    gm = p["global_module_or_class"]
    if not isinstance(gm, dict):
        fail("global_module_or_class must be an object")
    for key in ("name", "construction_evidence", "construction_verifier", "subject"):
        if gm.get(key) in (None, ""):
            fail(f"global_module_or_class missing {key}")
    run_mathematical_verifier(
        gm["construction_verifier"], gm["construction_evidence"], gm["subject"], "global_module_or_class"
    )

    verify_bound_blob(p["source_binding"], "source_binding")

    inventory = p["required_place_inventory"]
    if not isinstance(inventory, dict):
        fail("required_place_inventory must be an object")
    for key in ("places", "evidence", "verifier", "subject"):
        if inventory.get(key) in (None, ""):
            fail(f"required_place_inventory missing {key}")
    if not isinstance(inventory["places"], list) or not inventory["places"]:
        fail("required_place_inventory.places must be a nonempty exact list")
    expected_places = [str(x) for x in inventory["places"]]
    if len(expected_places) != len(set(expected_places)):
        fail("required_place_inventory contains duplicate places")
    run_mathematical_verifier(
        inventory["verifier"], inventory["evidence"], inventory["subject"], "required_place_inventory"
    )

    locs = p["localizations"]
    if not isinstance(locs, list) or not locs:
        fail("localizations must be a nonempty complete list")
    seen_places = set()
    for i, loc in enumerate(locs):
        if not isinstance(loc, dict):
            fail(f"localization[{i}] must be an object")
        for key in ("place", "source_row_or_chart", "localized_class", "verifier", "evidence", "subject"):
            if loc.get(key) in (None, ""):
                fail(f"localization[{i}] missing {key}")
        place = str(loc["place"])
        if place in seen_places:
            fail(f"duplicate place: {place}")
        seen_places.add(place)
        run_mathematical_verifier(loc["verifier"], loc["evidence"], loc["subject"], f"localization[{i}]")
    if seen_places != set(expected_places):
        fail("localization places do not exactly equal the independently verified required-place inventory")

    for key in ("required_places_complete", "dyadic_handled", "real_places_handled"):
        if p[key] is not True:
            fail(f"{key} must be true for PASS")
    if "2" not in {x.lower() for x in expected_places} and "dyadic" not in {x.lower() for x in expected_places}:
        fail("required-place inventory must explicitly name the dyadic place(s)")
    if not any(x.lower() in {"infinity", "real", "real_places", "archimedean"} or x.lower().startswith("real:") for x in expected_places):
        fail("required-place inventory must explicitly name the real/archimedean place(s)")

    if not isinstance(p["field_change_semantics"], str) or not p["field_change_semantics"].strip():
        fail("field_change_semantics must be explicit")

    fs = p.get("finite_support_assumption")
    if fs is not None:
        if not isinstance(fs, dict) or fs.get("used") not in (True, False):
            fail("finite_support_assumption must state used=true/false")
        if fs["used"]:
            for key in ("evidence", "verifier", "subject"):
                if fs.get(key) in (None, ""):
                    fail(f"finite-support use requires {key}")
            run_mathematical_verifier(fs["verifier"], fs["evidence"], fs["subject"], "finite_support_assumption")

    verify_literature_bindings(p["literature_bindings"], contract)

    av = p["adapter_mathematical_verifier"]
    ae = p["adapter_mathematical_evidence"]
    if not isinstance(av, dict) or not isinstance(ae, dict):
        fail("PASS requires separately bound adapter mathematical verifier and evidence")
    subject = p.get("adapter_subject")
    if not isinstance(subject, str) or not subject.strip():
        fail("adapter_subject must be explicit")
    run_mathematical_verifier(av, ae, subject, "adapter")

    if p.get("claims", {}) != {
        "literature_theorem_proved_by_repo": False,
        "local_global_obstruction": False,
        "receiver_closure": False,
        "endpoint_credit": False,
    }:
        fail("claims firewall must be exactly false for theorem/obstruction/receiver/endpoint")


def adversarial_self_check(contract: dict) -> None:
    head = git("rev-parse", "HEAD")
    require_hex40(head, "HEAD")
    good_blob = git_blob_at(head, contract["verifier"])
    fake = "0" * 40
    if good_blob == fake:
        fake = "f" * 40
    try:
        verify_bound_blob(
            {"path": contract["verifier"], "blob_sha": fake, "exact_head": head},
            "adversarial_fake_sha",
        )
    except AssertionError:
        pass
    else:
        fail("adversarial self-check failed: fake 40-hex blob was accepted")

    if contract["self_check_is_applicability_pass"] is not False:
        fail("self-check/applicability semantics regressed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", nargs="?", help="typed LIT-WF02 package to verify")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    try:
        contract = verify_contract()
        if args.package:
            verify_package(Path(args.package), contract)
            print("PASS: LIT-WF02 immutable global-H1/localization applicability package verified; mathematical credit remains zero")
        else:
            adversarial_self_check(contract)
            print("SELF_CHECK_OK: contract, frozen literature metadata, Git-object provenance checks, and fake-SHA rejection are intact; no applicability PASS is inferred")
        return 0
    except Exception as exc:
        print(f"FAIL_CLOSED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
