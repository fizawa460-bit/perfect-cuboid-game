#!/usr/bin/env python3
"""Build extractor-safe R02 from the immutable R01 review bundle.

Some AI readers extract only the HTML <main> element. R01 placed its handshake
in header/footer elements outside <main>, so those readers obtained all source
material but could not see the bundle markers. R02 preserves the embedded
research payload and places the complete handshake inside <main> at the start,
midpoint, and end.
"""
from __future__ import annotations

import argparse
from pathlib import Path

OLD_BUNDLE_ID = "PC-N1-2-PROOF-REVIEW-20260806-1612-R01"
BUNDLE_ID = "PC-N1-2-PROOF-REVIEW-20260806-1645-R02"
COMPLETED_THROUGH = "Stage12-N1-2k"
SOURCE_SNAPSHOT_COMMIT = "8d6910e8e68145e474f92716460a1cc6f384ecf1"
CONTENT_SHA256 = "201cad458d172e0939e5508b78e6e06abe894d908390f0c1b54c51a16e63d586"
LAST_SOURCE_DOCUMENT = "docs/stage12-n1-2k-final-remainder.md"
SOURCE = Path("review/PC-N1-2-PROOF-REVIEW-20260806-R01.html")
DEFAULT_OUTPUT = Path("review/PC-N1-2-PROOF-REVIEW-20260806-R02.html")


def marker_block(label: str) -> str:
    return f"""<section class=\"protocol machine-readable-handshake\" data-checkpoint=\"{label}\">
<h2>Machine-readable bundle handshake — {label}</h2>
<pre>BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
CONTENT_SHA256={CONTENT_SHA256}
LAST_SOURCE_DOCUMENT={LAST_SOURCE_DOCUMENT}
END_OF_BUNDLE={BUNDLE_ID}
PAGE_STRUCTURE=ALL_HANDSHAKES_INSIDE_MAIN_R02
CHECKPOINT={label}</pre>
</section>"""


def build_page() -> str:
    page = SOURCE.read_text(encoding="utf-8")
    required = [
        f"BUNDLE_ID={OLD_BUNDLE_ID}",
        "<body>\n<header>",
        "\n<main>\n<h1>Part I",
        "\n</main>\n<footer>",
        "\n</footer>\n</body>",
    ]
    for needle in required:
        if needle not in page:
            raise SystemExit(f"R01 structure changed; missing {needle!r}")

    page = page.replace(OLD_BUNDLE_ID, BUNDLE_ID)
    page = page.replace(
        "0e8bbc6e745ddf6d1f7c0ba3b21bb328a1fcc4d2",
        SOURCE_SNAPSHOT_COMMIT,
    )

    page = page.replace(
        "<body>\n<header>",
        "<body>\n<main id=\"review-bundle-main\">\n"
        + marker_block("START_OF_MAIN")
        + "\n<header>",
        1,
    )
    page = page.replace(
        "\n<main>\n<h1>Part I",
        "\n" + marker_block("BEFORE_EMBEDDED_SOURCES") + "\n<h1>Part I",
        1,
    )
    page = page.replace(
        "\n</main>\n<footer>",
        "\n" + marker_block("AFTER_EMBEDDED_SOURCES") + "\n<footer>",
        1,
    )
    page = page.replace(
        "\n</footer>\n</body>",
        "\n</footer>\n"
        + marker_block("END_OF_MAIN")
        + "\n</main>\n</body>",
        1,
    )

    main_start = page.index("<main id=\"review-bundle-main\">")
    main_end = page.index("</main>", main_start)
    main_text = page[main_start:main_end]
    markers = [
        f"BUNDLE_ID={BUNDLE_ID}",
        f"COMPLETED_THROUGH={COMPLETED_THROUGH}",
        f"SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}",
        f"CONTENT_SHA256={CONTENT_SHA256}",
        f"LAST_SOURCE_DOCUMENT={LAST_SOURCE_DOCUMENT}",
        f"END_OF_BUNDLE={BUNDLE_ID}",
    ]
    for marker in markers:
        if main_text.count(marker) < 4:
            raise SystemExit(f"marker is not repeated four times inside main: {marker}")
    if "Stage12-N1-2k" not in main_text or "audit_final_remainder_stage12_n1_2k.py" not in main_text:
        raise SystemExit("embedded final sources are missing from main")
    return page


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    page = build_page()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding="utf-8")
    print(f"wrote {args.output} ({len(page.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
