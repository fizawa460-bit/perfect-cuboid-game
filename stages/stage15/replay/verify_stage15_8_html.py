#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S15 = ROOT / "stages" / "stage15"
HTML_PATH = S15 / "stage15-final-self-contained.html"
CTRL_PATH = S15 / "15-8-controller.json"
RESULT_PATH = S15 / "15-8a" / "result.md"


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing marker: {needle}")


html = HTML_PATH.read_text(encoding="utf-8")
ctrl_text = CTRL_PATH.read_text(encoding="utf-8")
result = RESULT_PATH.read_text(encoding="utf-8")
ctrl = json.loads(ctrl_text)

assert ctrl["status"] == "OPEN"
assert ctrl["stage"] == "Stage15-8"
assert ctrl["canonical_commands"] == {
    "main": "Stage15-8-main-batch",
    "audit": "Stage15-8-audit",
}
assert ctrl["main_contract"]["initial_substage"] == "8a"

for path in (
    "stages/stage15/final.md",
    "stages/stage15/manifest-r01.md",
    "stages/stage15/15-2b/result.md",
    "stages/stage15/15-3/result.md",
    "stages/stage15/15-4/result.md",
    "stages/stage14/final.md",
    "stages/stage15/15-5/result.md",
    "stages/stage15/15-6-final.md",
):
    assert (ROOT / path).is_file(), path

# Required human-review sections.
for section_id in (
    "verdict", "scope", "ambient", "normal", "quant", "causal",
    "compare", "data", "provenance", "nonclaims", "perfect", "audit",
):
    require(html, f'id="{section_id}"')

# Frozen mathematical and accounting markers.
for needle in (
    "STAGE15-FINAL-SELF-CONTAINED-20260813-R01",
    "M₂(B) ∼ C<sub>M₂</sub>B(log B)⁵",
    "R∈ℤ  ⇔  AB is a square  ⇔  sf(A)=sf(B)",
    "N₂(B)/M₂(B) → 0",
    "STAGE15_HTML_THEOREM_SPECIES_SEPARATED=true",
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

# Local density transcription and ordered-limit language must be explicit.
require(html, "p⁴+4p³+22p²+4p+1")
require(html, "4/p + O(p<sup>−2</sup>)")
require(html, "まず <code>S</code> を固定して <code>B→∞</code>、その後にのみ <code>S</code> を増やします")

# Perfect-cuboid firewall: exactly-three faces plus integral space diagonal is a different stratum.
require(html, "完全直方体は3つの面対角線すべてと空間対角線が整数")
require(html, "Stage15は完全直方体問題のopen statusを変更しません")

# Self-contained/offline asset policy. Internal fragment hrefs are allowed.
lower = html.lower()
assert "<script" not in lower, "JavaScript is not required for this artifact"
assert not re.search(r"<link\b", lower), "external/link assets are forbidden"
assert "@import" not in lower, "CSS imports are forbidden"
assert "http://" not in lower and "https://" not in lower, "remote URLs are forbidden"
assert not re.search(r"\bsrc\s*=", lower), "external src resources are forbidden"
assert "mathjax" not in lower and "cdn" not in lower, "MathJax/CDN dependencies are forbidden"
assert re.search(r"<style>.*</style>", html, flags=re.I | re.S), "inline CSS missing"
for href in re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.I):
    assert href.startswith("#"), f"non-local navigation link: {href}"

# Handoff markers and no-new-math boundary.
for needle in (
    "STAGE15_8A_HTML_CREATED=true",
    "STAGE15_8A_OFFLINE_SELF_CONTAINED=true",
    "STAGE15_8A_EXTERNAL_REQUIRED_ASSETS=false",
    "STAGE15_8A_NEW_MATHEMATICS=false",
    "STAGE15_8A_STAGE15_6_REOPENED=false",
    "NEXT_GATE=FRESH_AUDIT_OF_SELF_CONTAINED_HTML",
    "AUDIT_REQUIRED=true",
    "MERGE_ALLOWED=false",
):
    require(result, needle)

print("STAGE15_8_HTML_VERIFY=PASS")
