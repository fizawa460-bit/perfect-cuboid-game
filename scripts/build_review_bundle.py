#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="docs/stage12-n1-2-final.md")
    parser.add_argument("--output", default="review/stage12-n1-2-final-review.md")
    parser.add_argument("--bundle-id", default="PC-N1-2-FINAL-REVIEW")
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)
    text = source.read_text(encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    commit = os.environ.get("GITHUB_SHA", "LOCAL_OR_UNSPECIFIED")

    header = f"""BUNDLE_ID={args.bundle_id}
COMPLETED_THROUGH=Stage12-N1-2-final
SOURCE_SNAPSHOT_COMMIT={commit}
CONTENT_SHA256={digest}
LAST_SOURCE_DOCUMENT={source.as_posix()}
END_OF_BUNDLE={args.bundle_id}
CHECKPOINT=START_OF_MAIN

# Adversarial review protocol

Review the integrated proof as a single document. Do not infer missing arguments. Classify each issue as FATAL, MAJOR, MINOR, or CLARIFICATION. Final verdict must be exactly CLOSED, REPAIRABLE, OPEN, or UNREADABLE_SOURCE.

---

"""
    footer = f"""

---
CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE={args.bundle_id}
"""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(header + text + footer, encoding="utf-8")


if __name__ == "__main__":
    main()
