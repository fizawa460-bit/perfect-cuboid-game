#!/usr/bin/env python3
"""Build the immutable Stage13 R04 self-contained review bundle.

The bundle is generated from an explicit source snapshot commit rather than the
working tree so parallel work cannot silently change the reviewed mathematics.
"""

from __future__ import annotations

import hashlib
import html
import json
import subprocess
from pathlib import Path

BUNDLE_ID = "STAGE13-FINAL-SELF-CONTAINED-20260809-R04"
SOURCE_SNAPSHOT_COMMIT = "f652833d194bade57794e4c03c184928a54a31b9"
BUNDLE_PATH = Path("review/STAGE13-FINAL-SELF-CONTAINED-20260809-R04.html")
MANIFEST_PATH = Path("stages/stage13/13-13e/review-manifest.md")
RESULT_PATH = Path("stages/stage13/13-13e/result.md")

SOURCES = [
    ("Canonical final proof", "stages/stage13/13-13c/stage13-final-proof.md"),
    ("External theorem / hypothesis crosswalk", "stages/stage13/13-13b/external-theorem-crosswalk.md"),
    ("Claim and dependency ledger result", "stages/stage13/13-13a/result.md"),
    ("Deterministic consistency audit result", "stages/stage13/13-13d/result.md"),
    ("Deterministic consistency audit JSON", "stages/stage13/data/13-13d/final_consistency_audit.json"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{SOURCE_SNAPSHOT_COMMIT}:{path}"], text=True
    )


def section_id(i: int) -> str:
    return f"section-{i}"


def main() -> None:
    sections = []
    nav = []
    source_hashes = []
    for i, (title, path) in enumerate(SOURCES, start=1):
        text = git_show(path)
        raw_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
        source_hashes.append((path, raw_sha))
        sid = section_id(i)
        nav.append(f'<li><a href="#{sid}">{html.escape(title)}</a></li>')
        sections.append(
            f'<section id="{sid}"><h2>{html.escape(title)}</h2>'
            f'<p class="source"><code>{html.escape(path)}</code> · SHA-256 <code>{raw_sha}</code></p>'
            f'<pre>{html.escape(text)}</pre></section>'
        )

    metadata = f"""
    <dl>
      <dt>Bundle ID</dt><dd><code>{BUNDLE_ID}</code></dd>
      <dt>Source snapshot commit</dt><dd><code>{SOURCE_SNAPSHOT_COMMIT}</code></dd>
      <dt>Stage13 theorem status entering review</dt><dd>Canonical proof resynthesized; deterministic audit PASS; theorem unchanged from 13-13a lock.</dd>
      <dt>Review gate</dt><dd>R04 is review evidence only. Final Stage13 freeze requires Stage13-13f and Stage13-13g.</dd>
    </dl>
    """

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

    scope = """
    <ul>
      <li>No claim of perfect-cuboid existence or nonexistence.</li>
      <li>Finite numerical checks are validators, not substitutes for the asymptotic proof.</li>
      <li>Stage12 R09 is imported as a frozen upstream theorem interface and is not reopened here.</li>
      <li>R03 remains immutable historical review evidence; this R04 bundle reviews the canonical 13-13c proof plus the 13-13b/13-13d audit material.</li>
      <li>Any substantive repair after review must create a new immutable R05/R06 bundle; R04 itself is never mutated.</li>
    </ul>
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
</style>
</head>
<body>
<header>
<h1>Stage13 final self-contained review bundle — R04</h1>
{metadata}
<p class="lock"><strong>Immutability rule:</strong> this exact HTML byte sequence is the R04 review target. Reviewer comments or repairs do not alter it.</p>
</header>
<section><h2>Frozen theorem contract</h2><pre>{html.escape(theorem)}</pre></section>
<section><h2>Scope and non-claims</h2>{scope}</section>
<nav><h2>Bundle contents</h2><ol>{''.join(nav)}</ol></nav>
{''.join(sections)}
</body>
</html>
"""

    BUNDLE_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    BUNDLE_PATH.write_text(document, encoding="utf-8")
    bundle_sha = hashlib.sha256(document.encode("utf-8")).hexdigest()

    source_lines = "\n".join(f"- `{path}` — SHA-256 `{sha}`" for path, sha in source_hashes)
    manifest = f"""# Stage13-13e — R04 review manifest

```text
BUNDLE_ID={BUNDLE_ID}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
CONTENT_SHA256={bundle_sha}
BUNDLE_PATH={BUNDLE_PATH.as_posix()}
R04_IMMUTABLE=true
R03_IMMUTABLE=true
THEOREM_CHANGED=false
DETERMINISTIC_AUDIT_STATUS=PASS
NEXT=13-13f
```

## Review target

The byte-for-byte review target is `{BUNDLE_PATH.as_posix()}`. Its SHA-256 is
`{bundle_sha}`. Any substantive repair must create a new R05/R06 bundle; R04 is
never edited in place.

## Included source snapshot

All embedded material is read with `git show` from source snapshot
`{SOURCE_SNAPSHOT_COMMIT}`:

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

R04 is a review snapshot, not the final Stage13 freeze. Stage13-13f targets
independent Grok/Qwen/Claude review when available. Promotion to Stage13-13g
requires at least two independent `CLOSED` verdicts and zero unresolved
received theorem-level objections.

```text
STAGE13_13E=COMPLETE_R04_REVIEW_BUNDLE
R04_IMMUTABLE=true
R03_IMMUTABLE=true
NEXT=13-13f
```
"""
    MANIFEST_PATH.write_text(manifest, encoding="utf-8")

    result = f"""# Stage13-13e — result

The final self-contained R04 review snapshot has been generated from the fixed
Stage13 source commit `{SOURCE_SNAPSHOT_COMMIT}`.

```text
STAGE13_13E=COMPLETE_R04_REVIEW_BUNDLE
BUNDLE_ID={BUNDLE_ID}
CONTENT_SHA256={bundle_sha}
R04_IMMUTABLE=true
R03_IMMUTABLE=true
THEOREM_CHANGED=false
NEXT=13-13f
```

The bundle contains the full canonical proof, the external-theorem crosswalk,
the 13-13a dependency-lock result, and the deterministic 13-13d audit result
plus its machine-readable JSON. It is intentionally self-contained: a reviewer
does not need to browse the repository to reconstruct the proof chain.

No external reviewer verdict is created or inferred by this stage.
"""
    RESULT_PATH.write_text(result, encoding="utf-8")

    print(json.dumps({
        "bundle_id": BUNDLE_ID,
        "source_snapshot_commit": SOURCE_SNAPSHOT_COMMIT,
        "content_sha256": bundle_sha,
        "bundle_path": BUNDLE_PATH.as_posix(),
        "manifest_path": MANIFEST_PATH.as_posix(),
        "result_path": RESULT_PATH.as_posix(),
    }, indent=2))


if __name__ == "__main__":
    main()
