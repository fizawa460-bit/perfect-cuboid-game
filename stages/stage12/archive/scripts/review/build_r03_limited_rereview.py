#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import subprocess
from pathlib import Path

BUNDLE_ID = "PC-N1-2-LIMITED-REREVIEW-20260807-R03"
COMPLETED_THROUGH = "Stage12-N1-3e"
SOURCE_SNAPSHOT_COMMIT = "bd8fe51b4466ddc91276f9f7699f3a8bdb490f4c"
SOURCE_LEDGER_SHA256 = "a752f5f42c17944c09d2d8ebff6432f74d772b88d5463d2aa3af0fbd5069b774"
PARENT_BUNDLE = "PC-N1-2-REPAIRED-PROOF-20260807-R02"
THEOREM_STATUS = "REPAIRED_CANDIDATE_PENDING_LIMITED_REAUDIT"
LAST_SOURCE_DOCUMENT = "docs/stage12-n1-3e-local-gap-closure.md"

PARENT_PAGE = Path("review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html")
SUPPLEMENT = Path("docs/stage12-n1-3e-local-gap-closure.md")
OUTPUT = Path("review/PC-N1-2-LIMITED-REREVIEW-20260807-R03.html")

EXPECTED_BLOBS = {
    PARENT_PAGE: "da7e937b195cc2c4fd43eb4bd2235217bc65f770",
    SUPPLEMENT: "a61ba1fe84f49c92e4ccbcd5755ea1e3e0bf5ae5",
}


def git_blob_sha(path: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path)], text=True
    ).strip()


def verify_sources() -> None:
    ledger_lines: list[str] = []
    for path, expected in EXPECTED_BLOBS.items():
        if not path.is_file():
            raise SystemExit(f"missing source: {path}")
        actual = git_blob_sha(path)
        if actual != expected:
            raise SystemExit(
                f"source blob mismatch for {path}: expected {expected}, got {actual}"
            )
        ledger_lines.append(f"{path.as_posix()}\t{expected}")

    ledger = "\n".join(ledger_lines) + "\n"
    actual_ledger = hashlib.sha256(ledger.encode("utf-8")).hexdigest()
    if actual_ledger != SOURCE_LEDGER_SHA256:
        raise SystemExit(
            "source ledger mismatch: "
            f"expected {SOURCE_LEDGER_SHA256}, got {actual_ledger}"
        )


def extract_parent_main(page: str) -> str:
    marker = '<main id="review-bundle-main">'
    start = page.index(marker) + len(marker)
    end = page.index("</main>", start)
    return page[start:end]


def handshake(checkpoint: str, content_sha256: str) -> str:
    return f"""
<section class="handshake" data-checkpoint="{checkpoint}">
<h2>Machine-readable handshake — {checkpoint}</h2>
<pre>BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH={COMPLETED_THROUGH}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
SOURCE_LEDGER_SHA256={SOURCE_LEDGER_SHA256}
PARENT_BUNDLE={PARENT_BUNDLE}
LAST_SOURCE_DOCUMENT={LAST_SOURCE_DOCUMENT}
THEOREM_STATUS={THEOREM_STATUS}
CONTENT_SHA256={content_sha256}
END_OF_BUNDLE={BUNDLE_ID}
CHECKPOINT={checkpoint}</pre>
</section>
"""


def main() -> None:
    verify_sources()

    parent_page = PARENT_PAGE.read_text(encoding="utf-8")
    supplement = SUPPLEMENT.read_text(encoding="utf-8")
    if "\x0c" in parent_page or "\x0c" in supplement:
        raise SystemExit("form-feed control character found in R03 source")

    parent_main = extract_parent_main(parent_page)
    payload = parent_page + "\n===== STAGE12-N1-3E =====\n" + supplement
    content_sha256 = hashlib.sha256(payload.encode("utf-8")).hexdigest()

    document = f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{BUNDLE_ID}</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ max-width: 1160px; margin: 0 auto; padding: 24px; font-family: system-ui, -apple-system, sans-serif; line-height: 1.55; }}
h1, h2, h3 {{ line-height: 1.25; }}
pre {{ white-space: pre-wrap; overflow-wrap: anywhere; border: 1px solid #8888; border-radius: 8px; padding: 16px; background: #8881; }}
.handshake, .scope, .source-ledger {{ border: 2px solid currentColor; border-radius: 10px; padding: 16px; margin: 20px 0; }}
.parent {{ border-top: 6px solid #8888; margin-top: 30px; padding-top: 24px; }}
.supplement {{ border-top: 6px solid #8888; margin-top: 42px; padding-top: 24px; }}
code {{ overflow-wrap: anywhere; }}
</style>
</head>
<body>
<main id="review-bundle-main">
{handshake("START_OF_MAIN", content_sha256)}
<header>
<h1>Stage12-N1-2 limited re-review R03</h1>
<p>This page embeds the complete parent R02 proof bundle and the complete Stage12-N1-3e local-gap supplement.</p>
</header>
<section class="scope">
<h2>Review scope</h2>
<pre>LIMITED_REVIEW=true
REVIEW_ONLY=OUTER_AVERAGE_LEMMA,PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY
PARENT_R02_VERDICT=REPAIRABLE
NEW_CENTRAL_ROUTE=false
FIXED_BC_KERNEL_USED=false
EXPECTED_OUTPUT=CLOSED|REPAIRABLE|OPEN|STALE_SOURCE|UNREADABLE_SOURCE</pre>
</section>
<section class="source-ledger">
<h2>Immutable source ledger</h2>
<pre>review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html\tda7e937b195cc2c4fd43eb4bd2235217bc65f770
docs/stage12-n1-3e-local-gap-closure.md\ta61ba1fe84f49c92e4ccbcd5755ea1e3e0bf5ae5
SOURCE_LEDGER_SHA256={SOURCE_LEDGER_SHA256}</pre>
</section>
{handshake("BEFORE_PARENT_R02", content_sha256)}
<section class="parent">
<h1>Embedded parent R02 bundle</h1>
{parent_main}
</section>
{handshake("AFTER_PARENT_BEFORE_3E", content_sha256)}
<section class="supplement">
<h1>Embedded Stage12-N1-3e supplement</h1>
<p><code>{SUPPLEMENT.as_posix()}</code> — Git blob <code>{EXPECTED_BLOBS[SUPPLEMENT]}</code></p>
<pre>{html.escape(supplement)}</pre>
</section>
<section class="scope">
<h2>Required machine-readable review result</h2>
<pre>VERDICT=
OUTER_AVERAGE_LEMMA=
PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY=
NEW_CENTRAL_GAP=</pre>
</section>
{handshake("END_OF_MAIN", content_sha256)}
</main>
</body>
</html>
"""

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(document, encoding="utf-8")
    print(f"wrote {OUTPUT} ({len(document.encode('utf-8'))} bytes)")
    print(f"CONTENT_SHA256={content_sha256}")


if __name__ == "__main__":
    main()
