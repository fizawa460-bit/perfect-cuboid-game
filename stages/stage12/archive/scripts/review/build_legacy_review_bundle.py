#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_SOURCES = (
    Path("docs/stage12-n1-2m-iterated-selberg-delange.md"),
    Path("docs/stage12-n1-2n-coupled-region.md"),
    Path("docs/stage12-n1-2o-analytic-closure.md"),
)

REVIEW_PROMPT = """# Review instructions

Conduct an adversarial final review of the repair chain through Stage12-N1-2o.
Do not infer omitted text. Verify the following points explicitly:

1. The Euler-product proof that J(s) is regular and nonvanishing on Re(s)>1/2+epsilon.
2. Whether the stated one-variable Selberg-Delange/Perron input is sufficient and used uniformly.
3. Whether weighted absolute convergence of the coprime cross correction yields the stated uniform rectangle estimate.
4. Whether the dyadic/Abel transfer, arc, diagonal, parity and floor errors are o(B(log B)^3).
5. Whether the conclusion applies only to the defined primitive oriented count C_prim(B).

Classify every issue as FATAL, MAJOR, MINOR or CLARIFICATION and finish with exactly one verdict:
CLOSED, REPAIRABLE or FATAL.
"""


def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNKNOWN"


def build_payload(paths: tuple[Path, ...]) -> str:
    sections: list[str] = []
    for index, path in enumerate(paths, start=1):
        text = path.read_text(encoding="utf-8")
        sections.append(
            f"\n---\n\n## EMBEDDED_SOURCE_{index}\n"
            f"PATH={path.as_posix()}\n"
            f"FILE_SHA256={hashlib.sha256(text.encode('utf-8')).hexdigest()}\n\n"
            f"{text.rstrip()}\n"
        )
    return "".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("review/stage12-n1-2-proof-review-r04.md"),
    )
    parser.add_argument(
        "--bundle-id",
        default="PC-N1-2-PROOF-REVIEW-R04",
    )
    parser.add_argument("sources", nargs="*", type=Path)
    args = parser.parse_args()

    paths = tuple(args.sources) if args.sources else DEFAULT_SOURCES
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise SystemExit(f"missing source files: {', '.join(missing)}")

    payload = build_payload(paths)
    content_sha = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    created = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    header = f"""# Stage12-N1-2 final review bundle R04

BUNDLE_ID={args.bundle_id}
COMPLETED_THROUGH=Stage12-N1-2o
SOURCE_SNAPSHOT_COMMIT={git_head()}
CONTENT_SHA256={content_sha}
LAST_SOURCE_DOCUMENT={paths[-1].as_posix()}
SOURCE_COUNT={len(paths)}
CREATED_UTC={created}
END_OF_BUNDLE={args.bundle_id}

CHECKPOINT=START_OF_MAIN

{REVIEW_PROMPT.rstrip()}
"""
    footer = f"""

---

CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE={args.bundle_id}
"""
    rendered = header + payload + footer

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(args.output)
    print(f"CONTENT_SHA256={content_sha}")


if __name__ == "__main__":
    main()
