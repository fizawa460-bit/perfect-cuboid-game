#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S15 = ROOT / "stages" / "stage15"
HTML_PATH = S15 / "stage15-final-self-contained.html"
REVIEW_PATH = ROOT / "review" / "STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html"
CTRL_PATH = S15 / "15-8-controller.json"
MANIFEST_PATH = S15 / "15-8-manifest-r02.md"
CLOSEOUT_PATH = S15 / "15-8-closeout.md"
STANDARD_PATH = ROOT / "docs" / "self-contained-review-standard.md"
STATUS_PATH = ROOT / "docs" / "00_CURRENT_RESEARCH_STATUS.md"
R01_FINAL_PATH = S15 / "final.md"
R01_MANIFEST_PATH = S15 / "manifest-r01.md"


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing marker: {needle}")


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


html_bytes = HTML_PATH.read_bytes()
review_bytes = REVIEW_PATH.read_bytes()
html = html_bytes.decode("utf-8")
review = review_bytes.decode("utf-8")
ctrl = json.loads(CTRL_PATH.read_text(encoding="utf-8"))
manifest = MANIFEST_PATH.read_text(encoding="utf-8")
closeout = CLOSEOUT_PATH.read_text(encoding="utf-8")
standard = STANDARD_PATH.read_text(encoding="utf-8")
status = STATUS_PATH.read_text(encoding="utf-8")
r01_final = R01_FINAL_PATH.read_text(encoding="utf-8")
r01_manifest = R01_MANIFEST_PATH.read_text(encoding="utf-8")

# Closed controller and immutable review identity.
assert ctrl["schema_version"] >= 3
assert ctrl["stage"] == "Stage15-8"
assert ctrl["status"] == "CLOSED"
assert ctrl["self_containment_standard"]["id"] == "SELF_CONTAINED_REVIEW_STANDARD_V1"
assert ctrl["stage15_r01_provenance_status"]["canonical_stage15_7_audit_record_present"] is False
assert ctrl["stage15_r01_provenance_status"]["stage15_7_closed_r01_assumed"] is False
assert ctrl["stage15_8_audit"]["verdict"] == "PASS"
assert ctrl["stage15_8_audit"]["internal_route_remains"] is False
assert ctrl["stage15_8_audit"]["merge_allowed"] is True
assert ctrl["merged_review_pr"]["number"] == 888
assert ctrl["merged_review_pr"]["merge_commit"] == "b83dd74be283dc58b3ce5c6862d21e105a9fa3f9"
assert ctrl["final_review_artifact"]["active_review_path"] == "review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html"

expected_blob = "5ebfd8e9e3b37c91a5cce509bfca708c1c34c618"
assert html_bytes == review_bytes, "review/ freeze is not byte-identical to stage-local HTML"
assert git_blob_sha(html_bytes) == expected_blob
assert ctrl["final_review_artifact"]["html_blob_sha"] == expected_blob

# Project-wide self-containment standard remains locked.
for needle in (
    "STANDARD_ID=SELF_CONTAINED_REVIEW_STANDARD_V1",
    "SUMMARY_ONLY_IS_SELF_CONTAINED=false",
    "Internal load-bearing mathematics is physically present",
    "Published external theorems may remain external",
    "Repository paths are provenance, not proof",
):
    require(standard, needle)

# Frozen R02 proof-facing sections and theorem firewalls.
for section_id in (
    "verdict", "scope", "upstream", "ambient", "normal", "quant", "local",
    "fixeds", "compare", "data", "external", "nonclaims", "perfect",
    "provenance", "audit",
):
    require(html, f'id="{section_id}"')

for needle in (
    "STAGE15-FINAL-SELF-CONTAINED-20260813-R02",
    "SELF_CONTAINED_REVIEW_STANDARD_V1",
    "Y=Bl₄(P¹×P¹)",
    "G²R²=4AB",
    "R∈ℤ  ⇔  AB is a square",
    "AB square  ⇔  sf(A)=sf(B)",
    "p⁴+4p³+22p²+4p+1",
    "ρ_S=∏_{p∈S}ρ_p",
    "N₂(B) ≤ M₂,S(B)",
    "STAGE15_HTML_QUANTITATIVE_SOURCE=STAGE14_NUMERATOR_PLUS_STAGE15_2B_DENOMINATOR",
    "STAGE15_HTML_CAUSAL_SOURCE=STAGE15_4_SQUARECLASS_PLUS_STAGE15_6_FIXED_PRIME_SIEVE",
    "STAGE15_HTML_STAGE15_6_INTERNAL_FIXED_DELTA=false",
    "STAGE15_HTML_STAGE15_6_INTERNAL_SIGMA=false",
    "STAGE15_HTML_FINITE_DATA_PROMOTED=false",
    "STAGE15_HTML_PERFECT_CUBOID_VERDICT=OPEN_UNCHANGED",
):
    require(html, needle)

# Offline freeze: no remote runtime dependencies.
lower = html.lower()
assert "<script" not in lower
assert not re.search(r"<link\b", lower)
assert "@import" not in lower
assert "http://" not in lower and "https://" not in lower
assert not re.search(r"\bsrc\s*=", lower)
assert re.search(r"<style>.*</style>", html, flags=re.I | re.S)
for href in re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.I):
    assert href.startswith("#"), f"non-local navigation link: {href}"

# Frozen manifest and closeout audit provenance.
for needle in (
    "STATUS=FROZEN_AUDITED",
    "STAGE15_8_AUDIT_VERDICT=PASS",
    "STAGE15_8_INTERNAL_ROUTE_REMAINS=false",
    "MERGED_REVIEW_PR=888",
    "MERGED_REVIEW_COMMIT=b83dd74be283dc58b3ce5c6862d21e105a9fa3f9",
    f"HTML_GIT_BLOB_SHA={expected_blob}",
    "ACTIVE_REVIEW_PATH=review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html",
    "RETROSPECTIVE_STAGE15_7_CLOSURE_INVENTED=false",
):
    require(manifest, needle)

for needle in (
    "STAGE15_8_STATUS=CLOSED",
    "STAGE15_8_FRESH_AUDIT=PASS",
    "STAGE15_8_INTERNAL_ROUTE_REMAINS=false",
    "STAGE15_8_STAGE15_6_REOPENED=false",
    "STAGE15_8_STAGE15_7_REOPENED=false",
    "STAGE15_8_RETROSPECTIVE_STAGE15_7_CLOSURE_INVENTED=false",
    "STAGE15_8_EXIT=CLOSED_R02_FROZEN",
):
    require(closeout, needle)

# Historical Stage15-7 provenance must remain literal, not retroactively repaired.
require(r01_final, "Status:** fresh-audit candidate")
require(r01_manifest, "Status: candidate pending fresh `Stage15-7-audit`.")
for needle in (
    "STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN",
    "STAGE15_7_STATUS=R01_MERGED_AUDIT_STATUS_NOT_CANONICALLY_RECORDED",
    "STAGE15_8_STATUS=CLOSED_R02",
    "STAGE15_FINAL_REVIEW=review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html",
    "NEXT_RESEARCH_PROGRAM=UNDEFINED",
):
    require(status, needle)

print("STAGE15_8_R02_CLOSEOUT_VERIFY=PASS")
