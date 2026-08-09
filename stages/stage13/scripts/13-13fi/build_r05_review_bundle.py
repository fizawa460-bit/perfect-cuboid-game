#!/usr/bin/env python3
"""Build the immutable Stage13 R05 self-contained review bundle.

The bundle is generated from the fixed merged Gate-H source snapshot.  Every
embedded source is read with ``git show`` from that commit so unrelated Stage14
work or later repository changes cannot silently alter the review target.
"""

from __future__ import annotations

import hashlib
import html
import json
import subprocess
from pathlib import Path

BUNDLE_ID = "STAGE13-FINAL-SELF-CONTAINED-20260809-R05"
SOURCE_SNAPSHOT_COMMIT = "79f03341b67dd49a8c128cfbeba3f756c91de6f6"
BUNDLE_PATH = Path("review/STAGE13-FINAL-SELF-CONTAINED-20260809-R05.html")
MANIFEST_PATH = Path("stages/stage13/13-13fi/review-manifest.md")
RESULT_PATH = Path("stages/stage13/13-13fi/result.md")

SOURCES = [
    ("R05 canonical proof", "stages/stage13/13-13fh/stage13-r05-canonical-proof.md"),
    ("Exact external theorem contracts", "stages/stage13/13-13ff/external-theorem-contracts.md"),
    ("Finite discrepancy / q-independence audit result", "stages/stage13/13-13fa/result.md"),
    ("Finite discrepancy audit JSON", "stages/stage13/data/13-13fa/q_independence_finite_audit.json"),
    ("R05 synthesis-readiness result", "stages/stage13/13-13fh/result.md"),
    ("R05 synthesis-readiness audit JSON", "stages/stage13/data/13-13fh/r05_synthesis_readiness_audit.json"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{SOURCE_SNAPSHOT_COMMIT}:{path}"], text=True
    )


def main() -> None:
    sections: list[str] = []
    nav: list[str] = []
    source_hashes: list[tuple[str, str]] = []

    for i, (title, path) in enumerate(SOURCES, start=1):
        text = git_show(path)
        raw_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
        source_hashes.append((path, raw_sha))
        sid = f"section-{i}"
        nav.append(f'<li><a href="#{sid}">{html.escape(title)}</a></li>')
        sections.append(
            f'<section id="{sid}"><h2>{html.escape(title)}</h2>'
            f'<p class="source"><code>{html.escape(path)}</code> · SHA-256 <code>{raw_sha}</code></p>'
            f'<pre>{html.escape(text)}</pre></section>'
        )

    theorem = r"""
N_q(B) ~ kappa I_q/(3 pi^3) B(log B)^3, q in {ab,ac,bc}
N1(B)  ~ kappa/(24 pi) B(log B)^3
P_q    = 8 I_q/pi^2
sum I_q = pi^2/8
J_q    = 2 I_q/pi
O_qr(B)=o(B(log B)^3)
T(B)   =o(B(log B)^3)
lambda_p=(p+5)/(2(p+1)) for inert p
""".strip()

    metadata = f"""
    <dl>
      <dt>Bundle ID</dt><dd><code>{BUNDLE_ID}</code></dd>
      <dt>Source snapshot commit</dt><dd><code>{SOURCE_SNAPSHOT_COMMIT}</code></dd>
      <dt>Canonical proof</dt><dd><code>stages/stage13/13-13fh/stage13-r05-canonical-proof.md</code></dd>
      <dt>Theorem status entering review</dt><dd>Repair Gates A–H complete; theorem/counting contract unchanged; R05 fresh external review required.</dd>
      <dt>Deterministic audit meaning</dt><dd>Reproducibility and consistency only; never a substitute for mathematical review.</dd>
    </dl>
    """

    scope = """
    <ul>
      <li>R05 is a new review target. R03/R04 remain immutable historical artifacts and their verdicts do not automatically carry forward.</li>
      <li>No claim of perfect-cuboid existence or nonexistence is made.</li>
      <li>No effective convergence rate for the finite directional proportions is claimed. The finite 100k→5m trajectory is disclosed only as a consistency diagnostic.</li>
      <li>Stage12 R09 is an upstream frozen theorem interface; its counting object, kappa normalization and exact factor-two projection are fully restated in the R05 canonical proof.</li>
      <li>Hecke/Dirichlet/Vaaler inputs are exposed at the exact proof-facing strength consumed by the argument. No growing-modulus theorem, general Selberg–Delange black box or Gaussian-Hecke zero-free region is a final logical gate.</li>
      <li>Any substantive repair after R05 review must create a new immutable R06 or later bundle. This R05 HTML is never edited in place.</li>
    </ul>
    """

    review_focus = """
    <ol>
      <li>Check that the common arithmetic factor Theta is established before Stage12 total-mass calibration and that no hidden q-dependent leading factor survives.</li>
      <li>Check the explicit Wiener bound, including the derivation of 3465625/6561 &lt; 529 and the separate p=5 bound.</li>
      <li>Check the curved-region accumulation with O((log B)^27) boxes, N=64, boundary and mesh estimates.</li>
      <li>Check the nonzero-harmonic family estimate with explicit conductor dependence and the Riesz/Perron smoothing bridge.</li>
      <li>Check the exact Stage12 counting/factor-two interface and the fixed-S inert-prime character transfer, including principal-pole-sector aliasing and the order fix S → B→∞ → enlarge S.</li>
      <li>Treat deterministic PASS outputs only as byte/constant/reproducibility checks, not as proof validation.</li>
    </ol>
    """

    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{BUNDLE_ID}</title>
<style>
body{{font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45;max-width:1180px;margin:0 auto;padding:28px;color:#171717;background:#fff}}
header{{border-bottom:2px solid #222;padding-bottom:18px;margin-bottom:24px}}
code,pre{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#f6f7f8;border:1px solid #ddd;padding:18px;border-radius:8px;font-size:13px;line-height:1.42}}
section{{margin:40px 0}} nav{{background:#f6f7f8;border:1px solid #ddd;padding:12px 20px;border-radius:8px}}
dt{{font-weight:700;margin-top:8px}} dd{{margin-left:0}} .source{{font-size:13px;color:#555}}
.lock{{background:#fff8dc;border-left:4px solid #9a7b00;padding:12px 16px}}
.warn{{background:#f6f7f8;border-left:4px solid #555;padding:12px 16px}}
</style>
</head>
<body>
<header>
<h1>Stage13 final self-contained review bundle — R05</h1>
{metadata}
<p class="lock"><strong>Immutability rule:</strong> this exact HTML byte sequence is the R05 review target. Reviewer comments or repairs do not alter it.</p>
<p class="warn"><strong>Fresh-review rule:</strong> all R05 verdicts start from zero. R04 CLOSED/OPEN/REPAIRABLE verdicts are provenance, not votes on this bundle.</p>
</header>
<section><h2>Frozen theorem contract under review</h2><pre>{html.escape(theorem)}</pre></section>
<section><h2>Scope and non-claims</h2>{scope}</section>
<section><h2>Adversarial review focus</h2>{review_focus}</section>
<nav><h2>Bundle contents</h2><ol>{''.join(nav)}</ol></nav>
{''.join(sections)}
</body>
</html>
"""

    BUNDLE_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    BUNDLE_PATH.write_text(document, encoding="utf-8")
    bundle_sha = hashlib.sha256(document.encode("utf-8")).hexdigest()

    source_lines = "\n".join(
        f"- `{path}` — SHA-256 `{sha}`" for path, sha in source_hashes
    )

    manifest = f"""# Stage13-13fi — R05 review manifest

```text
BUNDLE_ID={BUNDLE_ID}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
CONTENT_SHA256={bundle_sha}
BUNDLE_PATH={BUNDLE_PATH.as_posix()}
R05_IMMUTABLE=true
R04_IMMUTABLE=true
R03_IMMUTABLE=true
THEOREM_CHANGED=false
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R04_VERDICTS_CARRY_FORWARD_TO_R05=false
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
NEXT=13-13fj
```

## Review target

The byte-for-byte review target is `{BUNDLE_PATH.as_posix()}`. Its SHA-256 is
`{bundle_sha}`. The source snapshot is the merged Gate-H commit
`{SOURCE_SNAPSHOT_COMMIT}`.

Any substantive repair must create an immutable R06 or later bundle; R05 is
never edited in place.

## Included source snapshot

Every embedded source is read with `git show` from the fixed snapshot:

{source_lines}

## Frozen theorem contract

```text
N_q(B) ~ kappa I_q/(3 pi^3) B(log B)^3
N1(B)  ~ kappa/(24 pi) B(log B)^3
P_q    = 8 I_q/pi^2
sum I_q = pi^2/8
J_q    = 2 I_q/pi
O_qr(B)=o(B(log B)^3)
T(B)   =o(B(log B)^3)
lambda_p=(p+5)/(2(p+1))
```

## Review policy

R05 begins a fresh external-review ledger. Final Stage13 freeze remains blocked
until this final bundle (or a later repaired immutable bundle) receives at
least two independent `CLOSED` verdicts and has zero unresolved theorem-level
objections.

```text
STAGE13_13FI=COMPLETE_R05_REVIEW_BUNDLE
R05_IMMUTABLE=true
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fj
```
"""
    MANIFEST_PATH.write_text(manifest, encoding="utf-8")

    result = f"""# Stage13-13fi — result

The immutable R05 self-contained review bundle has been generated from the
merged Gate-H source snapshot `{SOURCE_SNAPSHOT_COMMIT}`.

```text
STAGE13_13FI=COMPLETE_R05_REVIEW_BUNDLE
BUNDLE_ID={BUNDLE_ID}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
CONTENT_SHA256={bundle_sha}
BUNDLE_PATH={BUNDLE_PATH.as_posix()}
R05_IMMUTABLE=true
R04_IMMUTABLE=true
R03_IMMUTABLE=true
THEOREM_CHANGED=false
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R04_VERDICTS_CARRY_FORWARD_TO_R05=false
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
PROMOTE_TO_13_13G=false
NEXT=13-13fj
```

The review bundle embeds the new single-entrypoint R05 canonical proof, exact
external theorem contracts, finite-discrepancy/q-independence audit material,
and Gate-H synthesis-readiness result/audit. Reviewers do not need to browse
the repair chain to reconstruct the final proof.

No external reviewer verdict is created or inferred by this stage. R05 review
starts from zero independent `CLOSED` verdicts.
"""
    RESULT_PATH.write_text(result, encoding="utf-8")

    print(json.dumps({
        "bundle_id": BUNDLE_ID,
        "source_snapshot_commit": SOURCE_SNAPSHOT_COMMIT,
        "content_sha256": bundle_sha,
        "bundle_path": BUNDLE_PATH.as_posix(),
        "manifest_path": MANIFEST_PATH.as_posix(),
        "result_path": RESULT_PATH.as_posix(),
        "source_hashes": dict(source_hashes),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
