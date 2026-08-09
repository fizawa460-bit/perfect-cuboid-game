#!/usr/bin/env python3
"""Build the immutable Stage13 R07 self-contained review bundle.

All embedded proof-facing sources are read from the fixed merged 13-13fu
snapshot. The builder is deterministic: rerunning it on the same repository
state reproduces the exact same R07 HTML bytes and SHA-256.
"""
from __future__ import annotations

import hashlib
import html
import subprocess
from pathlib import Path

BUNDLE_ID = "STAGE13-FINAL-SELF-CONTAINED-20260810-R07"
SOURCE_SNAPSHOT_COMMIT = "a2bb16304e02fe8d6f9b0454188fe410e16b9afb"
BUNDLE_PATH = Path("review/STAGE13-FINAL-SELF-CONTAINED-20260810-R07.html")
BASE = Path("stages/stage13/13-13fv")
MANIFEST_PATH = BASE / "review-manifest.md"
RESULT_PATH = BASE / "result.md"
LOCKS_PATH = BASE / "locks.txt"
POLICY_PATH = BASE / "review-policy.md"
SNAPSHOT_PATH = BASE / "source-snapshot.txt"

SOURCES = [
    ("R07 canonical proof", "stages/stage13/13-13fu/stage13-r07-canonical-proof.md"),
    ("R07 Gate A — fixed finite Hecke/ray-class twist contract", "stages/stage13/13-13fq/fixed-twist-hecke-contract.md"),
    ("R07 Gate B — concrete fixed-S residue model", "stages/stage13/13-13fr/concrete-fixed-s-residue-model.md"),
    ("R07 Gate C — curved-region self-contained closure", "stages/stage13/13-13fs/curved-region-self-contained-closure.md"),
    ("R07 Gate D — exact arithmetic and quantifier hardening", "stages/stage13/13-13ft/r07-hardening-lemma.md"),
    ("Explicit split-prime Wiener lemma", "stages/stage13/13-13fb/wiener-bound-lemma.md"),
    ("Frozen Stage12 counting/factor-two interface", "stages/stage13/13-13fe/stage12-counting-interface.md"),
    ("R07 repair plan", "stages/stage13/13-13fp/r07-repair-plan.md"),
    ("R07 synthesis source map", "stages/stage13/13-13fu/source-map.md"),
    ("R07 synthesis result", "stages/stage13/13-13fu/result.md"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{SOURCE_SNAPSHOT_COMMIT}:{path}"], text=True
    )


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    sections: list[str] = []
    nav: list[str] = []
    source_hashes: list[tuple[str, str]] = []

    for i, (title, path) in enumerate(SOURCES, 1):
        text = git_show(path)
        sha = sha256_text(text)
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
lambda_p=(p+5)/(2(p+1)) for inert p
lambda_3=1; contraction starts at inert p>=7"""

    focus = """1. Recheck the positive-octant proof of sum I_q=pi^2/8 and the non-circular common-Theta calibration.
2. Verify the exact fixed finite Hecke/ray-class twist family, Xi_{2 ell}=xi_{8 ell}, nonzero infinity type, holomorphy at s=1, and fixed-S strip-growth quantifiers.
3. Verify the concrete U/R_b/S_c residue model, the actual second-face square predicate W_p, lambda_p, effective-character quotient, principal residue product, and tagged fixed-S injection.
4. Verify the full curved-region transfer: Vaaler only on the angular interval, physical cutoff handled separately, box count Lambda^27, all-box Lambda^-35, boundary/mesh Lambda^-5, and retained-harmonic ledger.
5. Verify exact Wiener integer inequalities, ell-uniform logarithmic moments, epsilon-form overlap squeeze, and the Stage12 oriented-record factor-two interface.
6. Treat deterministic audits and finite numerical data only as reproducibility/diagnostic evidence, never as proof."""

    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{BUNDLE_ID}</title><style>
body{{font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45;max-width:1180px;margin:0 auto;padding:28px;color:#171717;background:#fff}}
header{{border-bottom:2px solid #222;padding-bottom:18px;margin-bottom:24px}}code,pre{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#f6f7f8;border:1px solid #ddd;padding:18px;border-radius:8px;font-size:13px;line-height:1.42}}
section{{margin:40px 0}}nav{{background:#f6f7f8;border:1px solid #ddd;padding:12px 20px;border-radius:8px}}dt{{font-weight:700;margin-top:8px}}dd{{margin-left:0}}.source{{font-size:13px;color:#555}}.lock{{background:#fff8dc;border-left:4px solid #9a7b00;padding:12px 16px}}.warn{{background:#f6f7f8;border-left:4px solid #555;padding:12px 16px}}
</style></head><body>
<header><h1>Stage13 final self-contained review bundle — R07</h1>
<dl><dt>Bundle ID</dt><dd><code>{BUNDLE_ID}</code></dd><dt>Source snapshot commit</dt><dd><code>{SOURCE_SNAPSHOT_COMMIT}</code></dd>
<dt>Canonical proof</dt><dd><code>stages/stage13/13-13fu/stage13-r07-canonical-proof.md</code></dd>
<dt>Theorem status entering review</dt><dd>R07 repair Gates A–D complete; theorem/counting contract unchanged.</dd>
<dt>Deterministic audit meaning</dt><dd>Reproducibility and consistency only; never a substitute for mathematical review.</dd></dl>
<p class="lock"><strong>Immutability rule:</strong> this exact HTML byte sequence is the R07 review target. Any substantive repair creates R08 or later.</p>
<p class="warn"><strong>Fresh-review rule:</strong> R07 starts with zero independent CLOSED verdicts. No R06 verdict carries forward.</p></header>
<section><h2>Frozen theorem contract under review</h2><pre>{html.escape(theorem)}</pre></section>
<section><h2>Scope and non-claims</h2><ul>
<li>No perfect-cuboid existence or nonexistence claim is made.</li>
<li>No effective convergence rate or finite-range directional monotonicity is claimed.</li>
<li>Finite data are neither proof nor positive convergence evidence.</li>
<li>No growing modulus is used: every inert set S is fixed before B tends to infinity.</li>
<li>The Stage12 total theorem is a frozen external interface; its proof is not reopened in Stage13.</li>
<li>Vaaler approximates only the angular chamber interval, never the physical cutoff d&lt;=B.</li>
</ul></section>
<section><h2>Adversarial review focus</h2><pre>{html.escape(focus)}</pre></section>
<nav><h2>Bundle contents</h2><ol>{''.join(nav)}</ol></nav>{''.join(sections)}</body></html>"""

    write(BUNDLE_PATH, document)
    bundle_sha = sha256_text(document)
    source_lines = "\n".join(f"- `{p}` — SHA-256 `{s}`" for p, s in source_hashes)

    locks = f"""BUNDLE_ID={BUNDLE_ID}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
CONTENT_SHA256={bundle_sha}
BUNDLE_PATH={BUNDLE_PATH.as_posix()}
R07_IMMUTABLE=true
R06_IMMUTABLE=true
R07_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R06_VERDICTS_CARRY_FORWARD_TO_R07=false
R07_INDEPENDENT_CLOSED_VERDICTS=0
R07_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
R07_RECORDED_THEOREM_LEVEL_OBJECTIONS=0
R07_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
R07_REPAIR_BLOCKERS_OPEN=0
R07_HARDENING_OBLIGATIONS_OPEN=0
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
PROMOTE_TO_13_13G=false
NEXT=13-13fw"""

    manifest = f"""# Stage13-13fv — R07 review manifest

```text
STAGE13_13FV=COMPLETE_R07_REVIEW_BUNDLE
{locks}
```

## Review target

The byte-for-byte review target is `{BUNDLE_PATH.as_posix()}` with SHA-256 `{bundle_sha}`.
Every embedded source is read from the fixed merged R07 synthesis snapshot `{SOURCE_SNAPSHOT_COMMIT}`.
R07 is never edited in place; any substantive repair creates R08 or later.

## Included fixed-snapshot sources

{source_lines}

## Review policy

R07 begins from zero independent `CLOSED` verdicts. Every R06 verdict is provenance only and does not count toward R07.
Final Stage13 freeze remains blocked until the immutable current review bundle obtains at least two independent `CLOSED` verdicts and zero unresolved theorem-level objections.
"""
    result = f"""# Stage13-13fv — result

The immutable R07 self-contained review bundle has been generated from merged R07 canonical-synthesis snapshot `{SOURCE_SNAPSHOT_COMMIT}`.

```text
STAGE13_13FV=COMPLETE_R07_REVIEW_BUNDLE
{locks}
```

The R07 external-review ledger starts from zero. No R06 CLOSED/OPEN verdict is inferred, copied, or carried forward.
"""
    policy = f"""# Stage13-13fv — R07 external review policy

- Review exactly `{BUNDLE_PATH.as_posix()}` with SHA-256 `{bundle_sha}`.
- Start from zero. Do not inherit any R06 verdict.
- Record each independent reviewer verdict as `CLOSED` or `OPEN` with explicit theorem-level objections.
- Documentation suggestions may be recorded without becoming theorem-level blockers.
- Promotion remains forbidden until at least two independent `CLOSED` verdicts and zero unresolved theorem-level objections are present.
- Any substantive mathematical repair produces R08 or later; R07 remains byte-for-byte immutable.
"""

    write(MANIFEST_PATH, manifest)
    write(RESULT_PATH, result)
    write(LOCKS_PATH, locks + "\n")
    write(POLICY_PATH, policy)
    write(SNAPSHOT_PATH, SOURCE_SNAPSHOT_COMMIT + "\n")

    # Deterministic self-checks.
    assert sha256_text(BUNDLE_PATH.read_text(encoding="utf-8")) == bundle_sha
    assert "R07_INDEPENDENT_CLOSED_VERDICTS=0" in locks
    assert "R06_VERDICTS_CARRY_FORWARD_TO_R07=false" in locks
    assert "R07_REPAIR_BLOCKERS_OPEN=0" in locks
    assert "R07_HARDENING_OBLIGATIONS_OPEN=0" in locks
    assert "NEXT=13-13fw" in locks

    print(f"BUNDLE_ID={BUNDLE_ID}")
    print(f"SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}")
    print(f"CONTENT_SHA256={bundle_sha}")
    print(f"BUNDLE_PATH={BUNDLE_PATH.as_posix()}")


if __name__ == "__main__":
    main()
