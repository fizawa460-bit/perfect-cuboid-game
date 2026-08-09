#!/usr/bin/env python3
"""Build the immutable Stage13 R06 self-contained review bundle.

Every embedded proof-facing source is read from the fixed merged 13-13fn
snapshot so later repository work cannot alter the R06 review target.
"""
from __future__ import annotations

import hashlib
import html
import subprocess
from pathlib import Path

BUNDLE_ID = "STAGE13-FINAL-SELF-CONTAINED-20260809-R06"
SOURCE_SNAPSHOT_COMMIT = "103dbc9bf241f8c306befc8dab0175e3ca4fb0f2"
BUNDLE_PATH = Path("review/STAGE13-FINAL-SELF-CONTAINED-20260809-R06.html")
MANIFEST_PATH = Path("stages/stage13/13-13fo/review-manifest.md")
RESULT_PATH = Path("stages/stage13/13-13fo/result.md")

SOURCES = [
    ("R06 canonical proof", "stages/stage13/13-13fn/stage13-r06-canonical-proof.md"),
    ("Explicit Wiener lemma", "stages/stage13/13-13fb/wiener-bound-lemma.md"),
    ("Gaussian-Hecke primary-source normalization", "stages/stage13/13-13fl/gaussian-hecke-normalization.md"),
    ("Fixed-S principal-pole closure", "stages/stage13/13-13fm/principal-pole-sector-closure.md"),
    ("R06 repair plan", "stages/stage13/13-13fj/r06-repair-plan.md"),
    ("R06 synthesis result", "stages/stage13/13-13fn/result.md"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{SOURCE_SNAPSHOT_COMMIT}:{path}"], text=True
    )


def main() -> None:
    sections = []
    nav = []
    source_hashes = []
    for i, (title, path) in enumerate(SOURCES, 1):
        text = git_show(path)
        sha = hashlib.sha256(text.encode()).hexdigest()
        source_hashes.append((path, sha))
        sid = f"section-{i}"
        nav.append(f'<li><a href="#{sid}">{html.escape(title)}</a></li>')
        sections.append(
            f'<section id="{sid}"><h2>{html.escape(title)}</h2>'
            f'<p class="source"><code>{html.escape(path)}</code> · SHA-256 <code>{sha}</code></p>'
            f'<pre>{html.escape(text)}</pre></section>'
        )

    theorem = """N_q(B) ~ kappa I_q/(3 pi^3) B(log B)^3, q in {ab,ac,bc}
N1(B)  ~ kappa/(24 pi) B(log B)^3
P_q    = 8 I_q/pi^2
sum I_q = pi^2/8
J_q    = 2 I_q/pi
O_qr(B)=o(B(log B)^3)
T(B)   =o(B(log B)^3)
lambda_p=(p+5)/(2(p+1)) for inert p"""

    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{BUNDLE_ID}</title><style>
body{{font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45;max-width:1180px;margin:0 auto;padding:28px;color:#171717;background:#fff}}
header{{border-bottom:2px solid #222;padding-bottom:18px;margin-bottom:24px}}code,pre{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#f6f7f8;border:1px solid #ddd;padding:18px;border-radius:8px;font-size:13px;line-height:1.42}}
section{{margin:40px 0}}nav{{background:#f6f7f8;border:1px solid #ddd;padding:12px 20px;border-radius:8px}}dt{{font-weight:700;margin-top:8px}}dd{{margin-left:0}}.source{{font-size:13px;color:#555}}.lock{{background:#fff8dc;border-left:4px solid #9a7b00;padding:12px 16px}}.warn{{background:#f6f7f8;border-left:4px solid #555;padding:12px 16px}}
</style></head><body>
<header><h1>Stage13 final self-contained review bundle — R06</h1>
<dl><dt>Bundle ID</dt><dd><code>{BUNDLE_ID}</code></dd><dt>Source snapshot commit</dt><dd><code>{SOURCE_SNAPSHOT_COMMIT}</code></dd>
<dt>Canonical proof</dt><dd><code>stages/stage13/13-13fn/stage13-r06-canonical-proof.md</code></dd>
<dt>Theorem status entering review</dt><dd>R06 repair Gates A–C complete; explicitness Gate D integrated; theorem/counting contract unchanged.</dd>
<dt>Deterministic audit meaning</dt><dd>Reproducibility and consistency only; never a substitute for mathematical review.</dd></dl>
<p class="lock"><strong>Immutability rule:</strong> this exact HTML byte sequence is the R06 review target. Any substantive repair creates R07 or later.</p>
<p class="warn"><strong>Fresh-review rule:</strong> R06 starts with zero independent CLOSED verdicts. No R05 reviewer verdict carries forward.</p></header>
<section><h2>Frozen theorem contract under review</h2><pre>{html.escape(theorem)}</pre></section>
<section><h2>Scope and non-claims</h2><ul>
<li>No perfect-cuboid existence or nonexistence claim is made.</li><li>No effective convergence rate or finite-range directional monotonicity is claimed.</li>
<li>The analytic identity sum I_q=pi^2/8 is proved in the R06 canonical proof; numerical quadrature is validation only.</li>
<li>The Gaussian-Hecke map is fixed as Fourier exponent m=8 ell to Huang–Liu–Rudnick index k=2 ell, with gamma shift 4 ell.</li>
<li>The fixed-S overlap proof classifies the principal sector only after auxiliary character aliasing on the actual constrained residue set is removed.</li>
<li>No growing-modulus theorem, general Selberg–Delange black box, or Gaussian-Hecke zero-free region is a final logical input.</li></ul></section>
<section><h2>Adversarial review focus</h2><ol>
<li>Verify the analytic positive-octant derivation of sum I_q=pi^2/8 and the common-Theta calibration order.</li>
<li>Verify the exact Gaussian-Hecke normalization, continuation/no-pole statement and fixed-strip growth interface.</li>
<li>Verify the explicit Wiener constants including p=5, curved-region accumulation and retained-harmonic exponent ledger.</li>
<li>Verify the fixed-S pole-signature kernel, exact product lambda_p principal residue, tagged-factor-two injection and nonprincipal pole loss.</li>
<li>Verify the Stage12 counting/factor-two interface and that all finite-data and deterministic audits remain non-proof diagnostics.</li></ol></section>
<nav><h2>Bundle contents</h2><ol>{''.join(nav)}</ol></nav>{''.join(sections)}</body></html>"""

    BUNDLE_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    BUNDLE_PATH.write_text(document, encoding="utf-8")
    bundle_sha = hashlib.sha256(document.encode()).hexdigest()
    source_lines = "\n".join(f"- `{p}` — SHA-256 `{s}`" for p, s in source_hashes)

    locks = f"""BUNDLE_ID={BUNDLE_ID}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
CONTENT_SHA256={bundle_sha}
BUNDLE_PATH={BUNDLE_PATH.as_posix()}
R06_IMMUTABLE=true
R05_IMMUTABLE=true
R06_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R05_VERDICTS_CARRY_FORWARD_TO_R06=false
R06_INDEPENDENT_CLOSED_VERDICTS=0
R06_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
R06_RECORDED_THEOREM_LEVEL_OBJECTIONS=0
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
PROMOTE_TO_13_13G=false
NEXT=13-13fp"""

    manifest = f"""# Stage13-13fo — R06 review manifest

```text
STAGE13_13FO=COMPLETE_R06_REVIEW_BUNDLE
{locks}
```

## Review target

The byte-for-byte review target is `{BUNDLE_PATH.as_posix()}` with SHA-256 `{bundle_sha}`.
Every embedded source is read from the fixed merged R06 synthesis snapshot `{SOURCE_SNAPSHOT_COMMIT}`.
R06 is never edited in place; any substantive repair creates R07 or later.

## Included fixed-snapshot sources

{source_lines}

## Review policy

R06 begins from zero independent `CLOSED` verdicts. R05 verdicts are provenance only and do not count toward R06.
Final Stage13 freeze remains blocked until an immutable final bundle obtains at least two independent `CLOSED` verdicts and zero unresolved theorem-level objections.
"""
    MANIFEST_PATH.write_text(manifest, encoding="utf-8")

    result = f"""# Stage13-13fo — result

The immutable R06 self-contained review bundle has been generated from the merged R06 canonical-synthesis snapshot `{SOURCE_SNAPSHOT_COMMIT}`.

```text
STAGE13_13FO=COMPLETE_R06_REVIEW_BUNDLE
{locks}
```

The R06 external-review ledger starts from zero. No R05 CLOSED/OPEN verdict is inferred, copied, or carried forward.
"""
    RESULT_PATH.write_text(result, encoding="utf-8")
    print(f"BUNDLE_ID={BUNDLE_ID}")
    print(f"SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}")
    print(f"CONTENT_SHA256={bundle_sha}")

if __name__ == "__main__":
    main()
