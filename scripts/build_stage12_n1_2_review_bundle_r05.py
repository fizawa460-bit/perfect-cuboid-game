#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import subprocess
from pathlib import Path

BUNDLE_ID = "PC-N1-2-PROOF-REVIEW-R05"
SOURCE_PATHS = [
    Path("docs/stage12-n1-2o-analytic-closure.md"),
    Path("docs/stage12-n1-2p-final-bookkeeping.md"),
]
OUTPUT_PATH = Path("review/stage12-n1-2-proof-review-r05.md")


def git_head() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNKNOWN"


def build_bundle() -> str:
    missing = [str(path) for path in SOURCE_PATHS if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))

    sources = [(path, path.read_text(encoding="utf-8")) for path in SOURCE_PATHS]
    canonical = "\n\n".join(
        f"SOURCE={path.as_posix()}\n{text.rstrip()}" for path, text in sources
    ) + "\n"
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    snapshot = git_head()

    handshake = "\n".join(
        [
            f"BUNDLE_ID={BUNDLE_ID}",
            "COMPLETED_THROUGH=Stage12-N1-2p",
            f"SOURCE_SNAPSHOT_COMMIT={snapshot}",
            f"CONTENT_SHA256={digest}",
            "LAST_SOURCE_DOCUMENT=docs/stage12-n1-2p-final-bookkeeping.md",
            f"END_OF_BUNDLE={BUNDLE_ID}",
        ]
    )

    sections = [
        "# Stage12-N1-2 final bookkeeping review bundle — R05",
        "",
        "This is an incremental patch bundle. Read the previously supplied R03 full-chain bundle first, then R04, then this R05 bundle. Where statements conflict, the later bundle prevails.",
        "",
        "## Machine-readable handshake — START_OF_MAIN",
        "",
        "```text",
        handshake,
        "CHECKPOINT=START_OF_MAIN",
        "```",
        "",
        "## Mandatory adversarial review protocol",
        "",
        "Review the final route `2j -> 2k -> 2l -> 2m -> 2n -> 2o -> 2p` and focus on the two remaining Round-2 MINOR items:",
        "",
        "1. Verify that the cited Selberg–Delange reference, edition, chapter and theorem number actually support the stated `z=1` input and error term.",
        "2. Verify every inequality in the four-region rectangle bookkeeping (`R00`, `R10`, `R01`, `R11`), including the powers of `R,S`, logarithmic absorption, uniformity in `R,S`, and summation over retained dyadic boxes.",
        "3. Check that R05 introduces no new FATAL or MAJOR gap and that the safe arc/diagonal/floor bounds remain `o(B(log B)^3)`.",
        "4. Return exactly one final verdict: `CLOSED`, `REPAIRABLE`, `OPEN`, or `UNREADABLE_SOURCE`.",
        "",
        "For every issue report severity, exact location, missing argument, and repairability. Do not infer unavailable text.",
        "",
        "## Embedded patch documents",
    ]

    for path, text in sources:
        sections.extend(
            [
                "",
                f"### `{path.as_posix()}`",
                "",
                "```markdown",
                text.rstrip(),
                "```",
            ]
        )

    sections.extend(
        [
            "",
            "## Machine-readable handshake — END_OF_MAIN",
            "",
            "```text",
            handshake,
            "CHECKPOINT=END_OF_MAIN",
            "```",
            "",
        ]
    )
    return "\n".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    rendered = build_bundle()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
