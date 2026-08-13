#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S15 = ROOT / "stages" / "stage15"
HTML_PATH = S15 / "stage15-final-self-contained.html"
CTRL_PATH = S15 / "15-8-controller.json"
RESULT_PATH = S15 / "15-8a" / "result.md"
MANIFEST_PATH = S15 / "15-8-manifest-r02.md"
STANDARD_PATH = ROOT / "docs" / "self-contained-review-standard.md"


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing marker: {needle}")


html = HTML_PATH.read_text(encoding="utf-8")
ctrl_text = CTRL_PATH.read_text(encoding="utf-8")
result = RESULT_PATH.read_text(encoding="utf-8")
manifest = MANIFEST_PATH.read_text(encoding="utf-8")
standard = STANDARD_PATH.read_text(encoding="utf-8")
ctrl = json.loads(ctrl_text)

assert ctrl["status"] == "OPEN"
assert ctrl["stage"] == "Stage15-8"
assert ctrl["schema_version"] >= 2
assert ctrl["self_containment_standard"]["id"] == "SELF_CONTAINED_REVIEW_STANDARD_V1"
assert ctrl["self_containment_standard"]["path"] == "docs/self-contained-review-standard.md"
assert ctrl["self_containment_standard"]["summary_only_is_self_contained"] is False
assert ctrl["canonical_commands"] == {
    "main": "Stage15-8-main-batch",
    "audit": "Stage15-8-audit",
}

for path in (
    "docs/self-contained-review-standard.md",
    "stages/stage15/final.md",
    "stages/stage15/manifest-r01.md",
    "stages/stage15/15-2a/result.md",
    "stages/stage15/15-2b/result.md",
    "stages/stage15/15-3/result.md",
    "stages/stage15/15-4/result.md",
    "stages/stage14/final.md",
    "stages/stage15/15-5/result.md",
    "stages/stage15/15-6dy/result.md",
    "stages/stage15/15-6dz/result.md",
    "stages/stage15/15-6-final.md",
    "stages/stage15/15-8-manifest-r02.md",
):
    assert (ROOT / path).is_file(), path
    assert path in ctrl["source_of_truth"], f"controller provenance missing: {path}"

for needle in (
    "STANDARD_ID=SELF_CONTAINED_REVIEW_STANDARD_V1",
    "SUMMARY_ONLY_IS_SELF_CONTAINED=false",
    "Internal load-bearing mathematics is physically present",
    "Published external theorems may remain external",
    "Repository paths are provenance, not proof",
    "The top-level `review/` directory is reserved for **active rendered review artifacts**",
):
    require(standard, needle)

for section_id in (
    "verdict", "scope", "upstream", "ambient", "normal", "quant", "local",
    "fixeds", "compare", "data", "external", "nonclaims", "perfect",
    "provenance", "audit",
):
    require(html, f'id="{section_id}"')

for needle in (
    "STAGE15-FINAL-SELF-CONTAINED-20260813-R02",
    "SELF_CONTAINED_REVIEW_STANDARD_V1",
    "STAGE15_HTML_SUMMARY_ONLY=false",
    "STAGE15_HTML_INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true",
    "STAGE15_HTML_EXTERNAL_THEOREM_WORKING_FORMS_STATED=true",
    "STAGE15_HTML_EXTERNAL_HYPOTHESES_MAPPED=true",
    "STAGE15_HTML_LOCAL_DENSITY_DERIVATION_EMBEDDED=true",
    "STAGE15_HTML_FIXED_S_ADAPTER_EMBEDDED=true",
):
    require(html, needle)

for needle in (
    "Y=Bl₄(P¹×P¹)",
    "−K_Y = 2F₁+2F₂−E₁−E₂−E₃−E₄",
    "ρ(Y)=2+4=6",
    "A(B)=M₂(B)+3M₃(B)",
    "geometrically integral",
    "M₃(B)=o(B(log B)^5)",
    "M₂(B) ∼ C_M₂ B(log B)^5",
):
    require(html, needle)

for needle in (
    "G=gcd(E,X,Y)=gcd(E,X,Y,U,V)",
    "m/n=(u+x)/e",
    "r/s=(v+y)/e",
    "G²R²=4AB",
    "R∈ℤ  ⇔  AB is a square",
    "AB square  ⇔  sf(A)=sf(B)",
    "A=kP²,   B=kQ²",
):
    require(html, needle)

for needle in (
    "N00=p²+2p+5",
    "N10=N01=2p−6",
    "N11=8",
    "Pr(v_p(A) even | A≡0 mod p)=1/(p+1)",
    "Pr(v_p(A)≡v_p(B) mod 2)=(p²+1)/(p+1)²",
    "p⁴+4p³+22p²+4p+1",
    "4/p + O(p<sup>−2</sup>)",
):
    require(html, needle)

for needle in (
    "M₂,p(B)=ρ_p C_M₂ B(log B)^5 + o_p(B(log B)^5)",
    "ρ_S=∏_{p∈S}ρ_p",
    "M₂,S(B)=C_M₂ (∏_{p∈S}ρ_p) B(log B)^5",
    "o_S",
    "N₂(B) ≤ M₂,S(B)",
    "limsup_{B→∞} N₂(B)/M₂(B) ≤ ∏_{p∈S}ρ_p",
    "STAGE15_HTML_GROWING_MODULUS_USED=false",
):
    require(html, needle)

for needle in (
    "STAGE15_HTML_QUANTITATIVE_SOURCE=STAGE14_NUMERATOR_PLUS_STAGE15_2B_DENOMINATOR",
    "STAGE15_HTML_CAUSAL_SOURCE=STAGE15_4_SQUARECLASS_PLUS_STAGE15_6_FIXED_PRIME_SIEVE",
    "STAGE15_HTML_STAGE15_6_INTERNAL_FIXED_DELTA=false",
    "STAGE15_HTML_STAGE15_6_INTERNAL_SIGMA=false",
    "STAGE15_HTML_FINITE_DATA_PROMOTED=false",
    "STAGE15_HTML_PERFECT_CUBOID_VERDICT=OPEN_UNCHANGED",
    "796,698",
    "(33,33,23)",
):
    require(html, needle)

for needle in (
    "Batyrev–Tschinkel toric anticanonical counting",
    "Huang Manin–Peyre equidistribution / adelic neighbourhood counting",
    "Browning–Loughran thin-set zero density",
    "UNIFORMITY_NOT_CLAIMED=GROWING_MODULUS",
    "K3_COUNTING_THEOREM_USED=false",
):
    require(html, needle)

html_sha = hashlib.sha256(html.encode("utf-8")).hexdigest()
standard_sha = hashlib.sha256(standard.encode("utf-8")).hexdigest()
require(manifest, f"HTML_SHA256={html_sha}")
require(manifest, f"SELF_CONTAINMENT_STANDARD_SHA256={standard_sha}")
require(manifest, "STATUS=AUDIT_CANDIDATE")
require(manifest, "NEW_MATHEMATICS=false")
require(manifest, "SUMMARY_ONLY=false")

lower = html.lower()
assert "<script" not in lower, "JavaScript is not required for this artifact"
assert not re.search(r"<link\b", lower), "external/link assets are forbidden"
assert "@import" not in lower, "CSS imports are forbidden"
assert "http://" not in lower and "https://" not in lower, "remote URLs are forbidden"
assert not re.search(r"\bsrc\s*=", lower), "external src resources are forbidden"
assert re.search(r"<style>.*</style>", html, flags=re.I | re.S), "inline CSS missing"
for href in re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.I):
    assert href.startswith("#"), f"non-local navigation link: {href}"

for needle in (
    "STAGE15_8A_REVIEW_BUNDLE=STAGE15-FINAL-SELF-CONTAINED-20260813-R02",
    "STAGE15_8A_R01_SELF_CONTAINMENT_DEFECT_REPAIRED=true",
    "STAGE15_8A_SELF_CONTAINMENT_STANDARD_APPLIED=true",
    "STAGE15_8A_INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true",
    "STAGE15_8A_EXTERNAL_THEOREM_CONTRACTS_MAPPED=true",
    "STAGE15_8A_NEW_MATHEMATICS=false",
    "STAGE15_8A_STAGE15_6_REOPENED=false",
    "NEXT_GATE=FRESH_AUDIT_OF_R02_SELF_CONTAINED_HTML",
    "AUDIT_REQUIRED=true",
    "MERGE_ALLOWED=false",
):
    require(result, needle)

print("STAGE15_8_HTML_VERIFY=PASS")
