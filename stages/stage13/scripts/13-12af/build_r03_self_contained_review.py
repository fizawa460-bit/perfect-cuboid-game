#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import json
import subprocess
from pathlib import Path

BUNDLE_ID = "STAGE13-FINAL-SELF-CONTAINED-20260809-R03"
COMPLETED_THROUGH = "Stage13-12af"
DOCUMENT_STATUS = "POST_R02_REPAIRED_STAGE13_R03_CANDIDATE_PENDING_EXTERNAL_VERDICT"
OUTPUT_HTML = Path("review/STAGE13-FINAL-SELF-CONTAINED-20260809-R03.html")
OUTPUT_MANIFEST = Path("stages/stage13/data/13-12af/review_bundle_manifest.json")
GENERATED_PATHS = {OUTPUT_HTML.as_posix(), OUTPUT_MANIFEST.as_posix()}

PRIORITY_SOURCES = [
    Path("stages/stage13/13-12af/current-proof.md"),
    Path("stages/stage13/13-12ad/result.md"),
    Path("stages/stage13/13-12ae/result.md"),
    Path("stages/stage13/13-12aa/result.md"),
    Path("stages/stage13/13-12ab/result.md"),
    Path("stages/stage13/13-12ac/current-proof.md"),
    Path("stages/stage13/13-12af/result.md"),
    Path("stages/stage13/README.md"),
    Path("stages/stage13/roadmap.md"),
    Path("stages/stage13/policy.md"),
    Path("stages/stage13/main.md"),
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def git_blob_sha(path: Path) -> str:
    return git("hash-object", str(path))


def changed_paths(commit: str) -> set[str]:
    output = git("show", "--pretty=format:", "--name-only", commit)
    return {line.strip() for line in output.splitlines() if line.strip()}


def source_snapshot_commit() -> str:
    commit = git("rev-parse", "HEAD")
    while True:
        paths = changed_paths(commit)
        if paths and paths.issubset(GENERATED_PATHS):
            commit = git("rev-parse", f"{commit}^")
            continue
        return commit


def source_paths() -> list[Path]:
    paths = list(PRIORITY_SOURCES)
    paths.extend(sorted(Path("stages/stage13/initial").glob("*.md")))

    packaging_dirs = {"13-11", "13-12ac", "13-12af"}
    for root in (Path("stages/stage13/scripts"), Path("stages/stage13/data")):
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(root)
            if rel.parts and rel.parts[0] in packaging_dirs:
                continue
            if path.suffix not in {".py", ".json", ".md", ".txt"}:
                continue
            paths.append(path)

    # The R03 builder itself is reviewable. Generated R03 outputs are excluded.
    paths.append(Path(__file__).resolve().relative_to(Path.cwd().resolve()))

    seen: set[str] = set()
    out: list[Path] = []
    for path in paths:
        key = path.as_posix()
        if key in seen:
            continue
        seen.add(key)
        out.append(path)
    return out


def read_sources(paths: list[Path]) -> tuple[list[dict], str]:
    rows: list[dict] = []
    ledger_lines: list[str] = []
    for path in paths:
        if not path.is_file():
            raise SystemExit(f"missing source: {path}")
        blob = git_blob_sha(path)
        text = path.read_text(encoding="utf-8")
        rows.append({
            "path": path.as_posix(),
            "blob_sha": blob,
            "bytes": len(text.encode("utf-8")),
            "text": text,
        })
        ledger_lines.append(f"{path.as_posix()}|{blob}")
    ledger = "\n".join(ledger_lines)
    return rows, hashlib.sha256(ledger.encode("utf-8")).hexdigest()


def build_payload(rows: list[dict], snapshot: str, ledger_sha: str) -> str:
    preamble = f"""# Stage13 post-R02 repaired self-contained review bundle R03

BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={snapshot}
SOURCE_LEDGER_SHA256={ledger_sha}
DOCUMENT_STATUS={DOCUMENT_STATUS}
CHECKPOINT=START_OF_MAIN

## What this bundle is

This is a new Stage13-only external-review candidate after the R02 adversarial
reviews returned Grok=OPEN, Claude=REPAIRABLE and Qwen=REPAIRABLE.  R03 embeds
the subsequent Stage13-12ad quantitative analytic repair and Stage13-12ae exact
p-adic/local-state repair.  The authoritative current proof entrypoint is
`stages/stage13/13-12af/current-proof.md`.

R01 and R02 are immutable historical review snapshots and are not mutated by
this bundle.  Their verdicts identify previous objections but do not constrain
the R03 verdict.

Stage12 source text is not embedded.  The frozen Stage12 R09 primitive oriented
asymptotic is a declared prior theorem-level input.  Review whether Stage13
states and uses that input correctly, including the factor-2 bridge, but do not
infer correctness of Stage12 from this bundle.

## Evidence neutrality

The following are NOT mathematical evidence and must not influence the verdict:

PREVIOUS_R01_R02_VERDICTS_BINDING=false
INTERNAL_PASS_FLAGS_ARE_EVIDENCE=false
INTERNAL_COMPLETE_FLAGS_ARE_EVIDENCE=false
GIT_HASHES_ARE_MATHEMATICAL_EVIDENCE=false
CI_SUCCESS_IS_MATHEMATICAL_EVIDENCE=false
NEGATIVE_VERDICT_REQUIRES_EXTRA_BURDEN=false

Hashes, manifests and CI establish source identity and deterministic
regeneration only.  A reviewer should freely return a negative verdict whenever
the mathematics warrants it.

## Required R03 questions

1. Are primitive canonical definitions, projection factor 2 and exactly-one
   inclusion-exclusion correct?
2. Are the Gelfand--Leray weights and chamber integrals I_q correct?
3. Is the analytic change of variables proving J_q=(2/pi)I_q correct, rather
   than merely numerically verified?
4. Does the raw j=0 coefficient system derive the common form
   A_q(B)~Theta J_q B(log B)^3 without seeding categorywise constants?
5. Is the explicit weighted-Wiener estimate
   ||C_{{ell,p}}-1||_{{5/8}} <= 529 p^(-5/4) valid uniformly over split primes
   and retained harmonics?
6. Do the logarithmic moments rigorously show that convolution shifts and
   anisotropic scaled regions alter only lower logarithmic degrees, leaving a
   direction-independent leading arithmetic scalar?
7. Are the small-height, small-coordinate, rectangle-tail, curved-boundary,
   Vaaler and retained-harmonic errors all o(B(log B)^3) with the concrete
   parameter choices in Stage13-12ad?
8. Is OE/EE parity handled correctly as finite 2-adic branch data without
   introducing a directional odd-prime factor?
9. Is Stage12 total calibration used only after commonness of Theta is proved?
   Is any earlier use of Stage12 confined to an error majorant rather than the
   leading directional proportion?
10. For inert p=3 mod 4, does primitivity force v_p(h)=0 and does gcd(r,s)=1
    leave exactly the U, R_b and S_c valuation states?
11. Is the exact unrestricted inert local factor
    L_p=(p+1)/(p-1) and positive-valuation fraction 2/(p+1) correct?
12. Is the unit-state finite-field acceptance (p+1)/(2(p-1)) correct and does
    it yield lambda_p=(p+5)/(2(p+1))?
13. Does the fixed-conductor residue-character refinement justify using that
    finite local acceptance as the principal leading local density with p fixed
    before B->infinity?
14. Does every genuine pair overlap inject into the constrained tagged union,
    and is the tag factor 2 only a safe upper multiplicity?
15. Is the order fixed k -> B->infinity -> k->infinity legitimate and enough
    to prove pair/triple overlap lower order?
16. Does exact inclusion-exclusion then establish the claimed exactly-one
    directional theorem and normalized vector?
17. Are all non-claims respected, including no perfect-cuboid existence result,
    no effective convergence rate, no monotonicity theorem and no claim of
    publication-grade independent peer review?

## R02 objection crosswalk to inspect, not to trust

Grok R02:
- zero-mode curved transfer -> Stage13-12ad
- mixed correction / harmonic uniformity -> Stage13-12ad
- positive-valuation tail -> Stage13-12ae
- local-state completeness -> Stage13-12ae

Claude R02:
- weighted-l1 uniformity -> Stage13-12ad
- nonzero harmonic lower order -> Stage13-12ad

Qwen R02:
- MAJOR-1 inert positive-valuation tail -> Stage13-12ae
- MAJOR-2 convolution / curved transfer -> Stage13-12ad and R03 current proof
- MINOR-1 tagged factor 2 -> Stage13-12ae / R03 current proof
- MINOR-2 limited Stage12 use in Vaaler error -> R03 current proof
- MINOR-3 OE/EE branch summary -> R03 current proof
- MINOR-4 analytic J_q=(2/pi)I_q bridge -> R03 current proof

The crosswalk is navigation only.  The reviewer should independently decide
whether the repairs are correct and complete.

## Verdict protocol

Return one top-level classification.  There is no preferred outcome.

CLOSED
  No fatal or major Stage13 mathematical gap is found at the declared Stage12
  R09 input boundary.

REPAIRABLE
  The central route appears potentially valid but one or more material local
  gaps require repair before acceptance.

OPEN
  A fatal gap, invalid central implication or unsupported theorem-level step
  prevents acceptance of the Stage13 theorem candidate.

UNREADABLE_SOURCE
  The physical bundle cannot be read or reconstructed well enough to perform
  the mathematical review.

For REPAIRABLE or OPEN, identify each material finding and cite the embedded
source path plus nearest section/function.  MINOR observations may also be
reported.  A negative verdict carries no extra burden.

## Scope locks

REVIEW_SCOPE=STAGE13_ONLY
STAGE12_SOURCE_EMBEDDED=false
STAGE12_REVIEW_IN_SCOPE=false
STAGE12_R09_DECLARED_PRIOR_INPUT=true
R03_CURRENT_PROOF=stages/stage13/13-12af/current-proof.md
OLD_7JB_PROOF_STATUS=SUPERSEDED_BY_13_12AA_13_12AD
OLD_7JF_PROOF_STATUS=SUPERSEDED_BY_13_12AB_13_12AE
R01_R02_ARTIFACTS_MUTATED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
EXPLICIT_CONVERGENCE_RATE_CLAIM=false
MONOTONICITY_CLAIM=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
R03_SELF_DECLARED_CLOSED=false

CHECKPOINT=BEFORE_EMBEDDED_SOURCES

## Stage13 source ledger

| # | path | Git blob SHA | bytes |
|---:|---|---|---:|
"""
    table = "\n".join(
        f"| {i} | `{row['path']}` | `{row['blob_sha']}` | {row['bytes']} |"
        for i, row in enumerate(rows, start=1)
    )

    sections: list[str] = []
    for i, row in enumerate(rows, start=1):
        sections.append(
            f"\n\n---\n\n# EMBEDDED SOURCE {i}/{len(rows)}\n\n"
            f"PATH={row['path']}\nGIT_BLOB_SHA={row['blob_sha']}\n\n"
            f"{row['text'].rstrip()}\n"
        )

    end = f"""\n\n---\n\nCHECKPOINT=AFTER_EMBEDDED_SOURCES\n
## Final candidate state

STAGE13_12AA=COMPLETE_NONCIRCULAR_STRUCTURE
STAGE13_12AB=COMPLETE_FIXED_LOCAL_STRUCTURE
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE
STAGE13_12AE=COMPLETE_EXACT_PADIC_LOCAL_CLOSURE
STAGE13_12AF=R03_REVIEW_RESYNTHESIS
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=R03_CANDIDATE
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
R03_SELF_DECLARED_CLOSED=false
CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE={BUNDLE_ID}
"""
    return preamble + table + "".join(sections) + end


def build_html(payload: str, snapshot: str, ledger_sha: str, content_sha: str) -> str:
    escaped = html.escape(payload)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{BUNDLE_ID}</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ max-width: 1240px; margin: 0 auto; padding: 24px 18px 80px; font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.5; }}
h1 {{ line-height: 1.2; }}
.meta {{ border: 2px solid currentColor; border-radius: 10px; padding: 14px; margin: 18px 0 24px; }}
pre {{ white-space: pre-wrap; overflow-wrap: anywhere; border: 1px solid #8888; border-radius: 8px; padding: 16px; background: #8881; }}
</style>
</head>
<body>
<main id="review-bundle-main">
<div class="meta"><pre>BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={snapshot}
SOURCE_LEDGER_SHA256={ledger_sha}
CONTENT_SHA256={content_sha}
DOCUMENT_STATUS={DOCUMENT_STATUS}
REVIEW_SCOPE=STAGE13_ONLY
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
CHECKPOINT=START_OF_MAIN</pre></div>
<h1>Stage13 post-R02 repaired self-contained review bundle R03</h1>
<p>This page is a review candidate, not a mathematical verdict. Stage13 sources only are physically embedded below.</p>
<pre>{escaped}</pre>
<div class="meta"><pre>CHECKPOINT=END_OF_MAIN
CONTENT_SHA256={content_sha}
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
R03_SELF_DECLARED_CLOSED=false
END_OF_BUNDLE={BUNDLE_ID}</pre></div>
</main>
</body>
</html>
"""


def main() -> None:
    snapshot = source_snapshot_commit()
    rows, ledger_sha = read_sources(source_paths())
    payload = build_payload(rows, snapshot, ledger_sha)
    content_sha = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    page = build_html(payload, snapshot, ledger_sha, content_sha)

    OUTPUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(page, encoding="utf-8")

    manifest = {
        "bundle_id": BUNDLE_ID,
        "completed_through": COMPLETED_THROUGH,
        "document_status": DOCUMENT_STATUS,
        "source_snapshot_commit": snapshot,
        "source_ledger_sha256": ledger_sha,
        "content_sha256": content_sha,
        "html_path": OUTPUT_HTML.as_posix(),
        "html_bytes": len(page.encode("utf-8")),
        "source_count": len(rows),
        "sources": [{k: row[k] for k in ("path", "blob_sha", "bytes")} for row in rows],
        "review_protocol": {
            "allowed_verdicts": ["CLOSED", "REPAIRABLE", "OPEN", "UNREADABLE_SOURCE"],
            "preferred_verdict": None,
            "review_scope": "stage13_only",
            "stage12_source_embedded": False,
            "stage12_review_in_scope": False,
            "stage12_r09_declared_prior_input": True,
            "previous_r01_r02_verdicts_binding": False,
            "internal_pass_flags_are_mathematical_evidence": False,
            "git_hashes_are_mathematical_evidence": False,
            "ci_success_is_mathematical_evidence": False,
            "negative_verdict_requires_extra_burden": False,
        },
        "precedence": {
            "r03_current_proof": "stages/stage13/13-12af/current-proof.md",
            "quantitative_j0_repair": "stages/stage13/13-12ad/result.md",
            "exact_padic_repair": "stages/stage13/13-12ae/result.md",
            "old_7jb": "superseded_by_13-12aa_and_13-12ad",
            "old_7jf": "superseded_by_13-12ab_and_13-12ae",
        },
        "prior_review_state": {
            "r01": "OPEN",
            "r02_grok": "OPEN",
            "r02_claude": "REPAIRABLE",
            "r02_qwen": "REPAIRABLE",
        },
        "status": {
            "STAGE13_12af_complete": True,
            "mathematics_changed_by_12af": False,
            "physical_single_html": True,
            "external_runtime_dependencies": False,
            "stage13_only_bundle": True,
            "r01_r02_artifacts_mutated": False,
            "stage13_global_review_status": "PENDING_EXTERNAL_R03",
            "self_declared_closed": False,
        },
    }
    OUTPUT_MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"BUNDLE_ID={BUNDLE_ID}")
    print(f"SOURCE_SNAPSHOT_COMMIT={snapshot}")
    print(f"SOURCE_LEDGER_SHA256={ledger_sha}")
    print(f"CONTENT_SHA256={content_sha}")
    print(f"SOURCE_COUNT={len(rows)}")
    print(f"HTML_BYTES={len(page.encode('utf-8'))}")
    print(f"WROTE={OUTPUT_HTML}")
    print(f"WROTE={OUTPUT_MANIFEST}")


if __name__ == "__main__":
    main()
