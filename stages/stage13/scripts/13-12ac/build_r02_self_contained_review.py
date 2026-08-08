#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import json
import subprocess
from pathlib import Path

BUNDLE_ID = "STAGE13-FINAL-SELF-CONTAINED-20260808-R02"
COMPLETED_THROUGH = "Stage13-12ac"
DOCUMENT_STATUS = "REPAIRED_STAGE13_R02_CANDIDATE_PENDING_EXTERNAL_VERDICT"
OUTPUT_HTML = Path("review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html")
OUTPUT_MANIFEST = Path("stages/stage13/data/13-12ac/review_bundle_manifest.json")
GENERATED_PATHS = {OUTPUT_HTML.as_posix(), OUTPUT_MANIFEST.as_posix()}

PRIORITY_SOURCES = [
    Path("stages/stage13/13-12ac/current-proof.md"),
    Path("stages/stage13/13-12aa/result.md"),
    Path("stages/stage13/13-12ab/result.md"),
    Path("stages/stage13/13-12ac/result.md"),
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

    for root in (Path("stages/stage13/scripts"), Path("stages/stage13/data")):
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(root)
            if rel.parts and rel.parts[0] in {"13-11", "13-12ac"}:
                continue
            if path.suffix not in {".py", ".json", ".md", ".txt"}:
                continue
            paths.append(path)

    # R02 builder itself is reviewable; its generated outputs are excluded.
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
    preamble = f"""# Stage13 repaired self-contained review bundle R02

BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={snapshot}
SOURCE_LEDGER_SHA256={ledger_sha}
DOCUMENT_STATUS={DOCUMENT_STATUS}
CHECKPOINT=START_OF_MAIN

## What this bundle is

This is a fresh Stage13-only external-review candidate after the R01 review
returned OPEN and the project added Stage13-12aa and Stage13-12ab repairs.
R01 is not a precedent for the verdict. The current proof entrypoint is
`stages/stage13/13-12ac/current-proof.md`.

The historical `stages/stage13/main.md` is embedded for evidence and context,
but its old Stage13-7jb and Stage13-7jf proof steps are superseded where the
13-12 repair files explicitly say so.

Stage12 source text is not embedded. The frozen Stage12 R09 primitive oriented
asymptotic is a declared prior theorem-level input. Review whether Stage13 uses
that input correctly; do not infer correctness of Stage12 from this bundle.

## Evidence neutrality

The following are NOT mathematical evidence and must not influence the verdict:

PREVIOUS_R01_VERDICT_BINDING=false
INTERNAL_PASS_FLAGS_ARE_EVIDENCE=false
INTERNAL_COMPLETE_FLAGS_ARE_EVIDENCE=false
GIT_HASHES_ARE_MATHEMATICAL_EVIDENCE=false
CI_SUCCESS_IS_MATHEMATICAL_EVIDENCE=false
NEGATIVE_VERDICT_REQUIRES_EXTRA_BURDEN=false

Hashes, manifests and CI establish source identity and deterministic
regeneration only. A reviewer should freely return a negative verdict whenever
the mathematics warrants it.

## Required R02 questions

1. Are the primitive canonical definitions, projection factor 2 and exactly-one
   inclusion-exclusion identities correct?
2. Are the chamber/Gelfand--Leray directional weights, I_q integrals and
   J_q=2 I_q/pi bridge correct?
3. Does Stage13-12aa derive the raw j=0 primitive local coefficients without
   seeding categorywise asymptotic constants?
4. Are the zero/nonzero pure Dirichlet factors and the three-variable mixed
   correction correct, including the weighted-l1 bound and its uniformity?
5. Does the zero-mode curved-region transfer really produce
   A_q(B) ~ Theta J_q B(log B)^3 with one common unknown Theta?
6. Are nonzero harmonics, Selberg--Vaaler bracketing and all boundary channels
   lower order at the raw B(log B)^3 scale?
7. Is Stage12 total calibration used only after commonness of Theta is proved,
   so the recovered D_q=kappa I_q/(3 pi^3) is non-circular?
8. Does Stage13-12ab correctly implement a fixed prime condition by finite
   local-state refinement and exact replacement of that prime's Euler factor?
9. Is the inert-prime unit acceptance (p+1)/(2(p-1)) correct, and is the
   positive-valuation local tail uniformly O(1/p) strongly enough to imply
   lambda_p<=3/4 for all sufficiently large inert primes?
10. Is the order of limits fixed k -> B->infinity -> k->infinity legitimate,
    with no hidden growing-modulus uniformity assumption?
11. Do pair/triple lower order and exact inclusion-exclusion restore the claimed
    exactly-one directional asymptotic and normalized vector?
12. Are all non-claims respected, including no perfect-cuboid existence result,
    no effective convergence rate and no monotonicity theorem?

## Verdict protocol

Return one top-level classification. There is no preferred outcome.

CLOSED
  The reviewer finds no fatal or major Stage13 mathematical gap at the declared
  Stage12 R09 input boundary.

REPAIRABLE
  The central route appears potentially valid but one or more material local
  gaps require repair before the theorem should be accepted.

OPEN
  A fatal gap, invalid central implication or unsupported theorem-level step
  prevents acceptance of the repaired Stage13 theorem.

UNREADABLE_SOURCE
  The physical bundle cannot be fully read or reconstructed well enough to
  perform the mathematical review.

For REPAIRABLE or OPEN, identify each material finding and cite the embedded
source path plus the nearest section/function. MINOR observations may also be
reported. No extra burden of proof applies to a negative verdict.

## Scope locks

REVIEW_SCOPE=STAGE13_ONLY
STAGE12_SOURCE_EMBEDDED=false
STAGE12_REVIEW_IN_SCOPE=false
STAGE12_R09_DECLARED_PRIOR_INPUT=true
R02_CURRENT_PROOF=stages/stage13/13-12ac/current-proof.md
OLD_7JB_PROOF_STATUS=SUPERSEDED_BY_13_12AA
OLD_7JF_PROOF_STATUS=SUPERSEDED_BY_13_12AB
PERFECT_CUBOID_EXISTENCE_CLAIM=false
EXPLICIT_CONVERGENCE_RATE_CLAIM=false
MONOTONICITY_CLAIM=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02

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

STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
STAGE13_12AB=COMPLETE_FIXED_LOCAL_OVERLAP_REPAIR
STAGE13_12AC=R02_REVIEW_RESYNTHESIS
STAGE13_REPAIR_CHAIN=COMPLETE
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
R02_SELF_DECLARED_CLOSED=false
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
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
CHECKPOINT=START_OF_MAIN</pre></div>
<h1>Stage13 repaired self-contained review bundle R02</h1>
<p>This page is a review candidate, not a mathematical verdict. Stage13 sources only are physically embedded below.</p>
<pre>{escaped}</pre>
<div class="meta"><pre>CHECKPOINT=END_OF_MAIN
CONTENT_SHA256={content_sha}
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
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
            "previous_r01_verdict_binding": False,
            "internal_pass_flags_are_mathematical_evidence": False,
            "git_hashes_are_mathematical_evidence": False,
            "ci_success_is_mathematical_evidence": False,
            "negative_verdict_requires_extra_burden": False,
        },
        "precedence": {
            "r02_current_proof": "stages/stage13/13-12ac/current-proof.md",
            "old_7jb": "superseded_by_13-12aa",
            "old_7jf": "superseded_by_13-12ab",
        },
        "status": {
            "STAGE13_12ac_complete": True,
            "mathematics_changed_by_12ac": False,
            "physical_single_html": True,
            "external_runtime_dependencies": False,
            "stage13_only_bundle": True,
            "stage13_global_review_status": "PENDING_EXTERNAL_R02",
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
