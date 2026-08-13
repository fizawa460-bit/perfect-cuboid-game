#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
S15 = ROOT / "stages" / "stage15"


def read(path: str) -> str:
    p = ROOT / path
    assert p.is_file(), f"missing {path}"
    return p.read_text(encoding="utf-8")


# Preserve dependency replays that remain path-current. Stage15-5's historical
# verifier still points at a pre-archive Stage14 path, so validate its canonical
# result and current Stage14 final source directly below instead of invoking that
# stale historical harness.
for verifier in [
    "stages/stage15/replay/verify_stage15_2b.py",
    "stages/stage15/replay/verify_stage15_3.py",
    "stages/stage15/replay/verify_stage15_4.py",
    "stages/stage15/replay/verify_stage15_6_controller.py",
]:
    run = subprocess.run([sys.executable, str(ROOT / verifier)], cwd=ROOT)
    assert run.returncode == 0, f"dependency verifier failed: {verifier}"

seven_a = read("stages/stage15/15-7a/result.md")
seven_b = read("stages/stage15/15-7b/result.md")
seven_c = read("stages/stage15/15-7c/result.md")
final = read("stages/stage15/final.md")
manifest = read("stages/stage15/manifest-r01.md")
controller = read("stages/stage15/15-7-controller.json")
closed6 = read("stages/stage15/15-6-final.md")
stage5 = read("stages/stage15/15-5/result.md")
stage14 = read("stages/stage14/final.md")

# Current canonical Stage15-5 / Stage14 quantitative contract.
assert "STAGE15_5_SURVIVAL_ZERO_DENSITY=true" in stage5
assert "STAGE15_5_POLYNOMIAL_THINNING_ANY_DELTA_LT_HALF=true" in stage5
assert "STAGE15_5_GAUSSIAN_CAUSAL_DERIVATION_PROVED=false" in stage5
assert "N_2(B)\\ll B^{1/2+o(1)}" in stage14
assert "strict power saving" in stage14

# Stage15-6 must remain closed and no new internal route may appear.
assert "STAGE15_6_STATUS=CLOSED" in closed6
assert not (S15 / "15-6eb").exists()
assert '"non_reopen_rule"' in controller

# Work-unit markers.
for text, marker in [
    (seven_a, "STAGE15_7A_THEOREM_SPECIES_SEPARATED=true"),
    (seven_b, "STAGE15_7B_PROVENANCE_TABLE_FROZEN=true"),
    (seven_c, "STAGE15_7C_FINAL_BUNDLE_R01_CREATED=true"),
]:
    assert marker in text, marker

assert "NEXT_GATE=FRESH_AUDIT_OF_R01_FINAL_BUNDLE_AND_PROVENANCE_LOCK" in seven_c
assert "AUDIT_REQUIRED=true" in seven_c
assert "MERGE_ALLOWED=false" in seven_c

# Final bundle must contain the controller-required sections and explicit theorem-species firewall.
required_sections = [
    "## 1. Scope, physical objects, and common cutoff",
    "## 2. Ambient exactly-two theorem",
    "## 3. Exact survivor normal form",
    "## 4. Strongest quantitative survival theorem",
    "## 5. Independent causal zero-density theorem",
    "## 6. Quantitative versus causal comparison",
    "## 7. Matched finite evidence",
    "## 8. Provenance and theorem firewalls",
    "## 9. Negative knowledge and future gates",
    "## 10. Relation to the perfect cuboid problem",
    "## 11. Final causal comparison verdict",
    "## 12. R01 audit boundary",
]
for heading in required_sections:
    assert heading in final, heading

for needle in [
    "STAGE15-FINAL-SELF-CONTAINED-20260813-R01",
    "M_2(B)\\sim C_{M_2}B(\\log B)^5",
    "B^{-1/2+\\varepsilon}(\\log B)^{-5}",
    "\\operatorname{sf}(A)=\\operatorname{sf}(B)",
    "1-\\rho_p=",
    "This proof is independent of the Stage15-5 ratio bound",
    "the half-power input is Stage14's theorem",
    "does not imply that perfect cuboids do not exist",
    "candidate, not a closed Stage15 final",
]:
    assert needle in final, needle

# Provenance lock must resolve every load-bearing path.
for path in [
    "stages/stage15/15-2b/result.md",
    "stages/stage15/15-3/result.md",
    "stages/stage15/15-4/result.md",
    "stages/stage14/final.md",
    "stages/stage15/15-5/result.md",
    "stages/stage15/15-6-final.md",
    "stages/stage15/15-7-controller.json",
]:
    assert path in manifest, path
    assert (ROOT / path).exists(), path

assert "attribute the Stage14 half-power numerator saving to the Stage15-6 local parity sieve" in manifest
assert "infer perfect-cuboid existence or nonexistence" in manifest

print("STAGE15_7A_C_VERIFY=PASS")
