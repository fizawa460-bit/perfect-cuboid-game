#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import subprocess
from pathlib import Path

BUNDLE_ID = "PC-N1-2J-2P-PROOF-CHAIN-20260807-R01"
SOURCE_SNAPSHOT_COMMIT = "2958c330139904bd57c6d2b404dc8f74dd30f75f"
OUTPUT = Path("review/PC-N1-2J-2P-PROOF-CHAIN-20260807-R01.html")

SOURCES = [
    (
        "Stage12-N1-2j",
        Path("docs/archive/stage12-n1-2/stage12-n1-2j-boundary-layers.md"),
        "111107ce0346606cb8a73b4c50e1841386f4cf23",
    ),
    (
        "Stage12-N1-2k",
        Path("docs/archive/stage12-n1-2/stage12-n1-2k-final-remainder.md"),
        "48b28e84034c17e242998ab313775b0894908515",
    ),
    (
        "Stage12-N1-2l",
        Path("docs/archive/stage12-n1-2/stage12-n1-2l-dlb-hypotheses.md"),
        "68935cf95fa0a6fd8fca2fc57d508eb364215d12",
    ),
    (
        "Stage12-N1-2m",
        Path("docs/archive/stage12-n1-2/stage12-n1-2m-iterated-selberg-delange.md"),
        "6e6a4a59af88c8f39c570d0277708b0831b806b8",
    ),
    (
        "Stage12-N1-2n",
        Path("docs/archive/stage12-n1-2/stage12-n1-2n-coupled-region.md"),
        "1d5d95f46c45a9c8d417c1bb6e87e7c6b77a8779",
    ),
    (
        "Stage12-N1-2o",
        Path("docs/archive/stage12-n1-2/stage12-n1-2o-analytic-closure.md"),
        "5f42b4d45242649c69271fe44abbe7d6cc9aca55",
    ),
    (
        "Stage12-N1-2p",
        Path("docs/archive/stage12-n1-2/stage12-n1-2p-final-bookkeeping.md"),
        "b368b432d743b79e0641c2be6eb6d97f436a1bd7",
    ),
]


def git_blob_sha(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def main() -> None:
    source_texts: list[tuple[str, Path, str, str]] = []
    payload_parts: list[str] = []

    for label, path, expected_blob in SOURCES:
        if not path.is_file():
            raise SystemExit(f"missing source: {path}")
        actual_blob = git_blob_sha(path)
        if actual_blob != expected_blob:
            raise SystemExit(
                f"source blob mismatch for {path}: expected {expected_blob}, got {actual_blob}"
            )
        text = path.read_text(encoding="utf-8")
        source_texts.append((label, path, actual_blob, text))
        payload_parts.append(f"===== {label} | {path} | {actual_blob} =====\n{text}")

    payload = "\n\n".join(payload_parts)
    content_sha256 = hashlib.sha256(payload.encode("utf-8")).hexdigest()

    sections: list[str] = []
    for index, (label, path, blob_sha, text) in enumerate(source_texts, start=1):
        sections.append(
            f"""
<section class="source" id="source-{index}">
  <h2>SOURCE {index} / {len(source_texts)} — {html.escape(label)}</h2>
  <p class="path">{html.escape(path.as_posix())}<br>Git blob SHA: <code>{blob_sha}</code></p>
  <pre>{html.escape(text)}</pre>
</section>
"""
        )

    document = f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stage12-N1-2j through 2p proof-chain review</title>
<style>
:root {{ color-scheme: light dark; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
body {{ max-width: 1120px; margin: 0 auto; padding: 24px 18px 80px; line-height: 1.55; }}
h1, h2 {{ line-height: 1.25; }}
.meta, .protocol {{ border: 1px solid #8887; border-radius: 10px; padding: 14px 16px; margin: 18px 0; }}
.source {{ border-top: 4px solid #8887; margin-top: 56px; padding-top: 24px; }}
.path {{ opacity: .8; }}
pre {{ white-space: pre-wrap; overflow-wrap: anywhere; border: 1px solid #8885; border-radius: 8px; padding: 16px; background: #8881; }}
code {{ overflow-wrap: anywhere; }}
</style>
</head>
<body>
<main id="review-bundle-main">
<div class="meta"><pre>BUNDLE_ID={BUNDLE_ID}
COMPLETED_THROUGH=Stage12-N1-2p
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
SOURCE_COUNT={len(source_texts)}
SOURCE_RANGE=Stage12-N1-2j..Stage12-N1-2p
CONTENT_SHA256={content_sha256}
FIRST_SOURCE_DOCUMENT={source_texts[0][1].as_posix()}
LAST_SOURCE_DOCUMENT={source_texts[-1][1].as_posix()}
CHECKPOINT=START_OF_MAIN</pre></div>

<h1>Stage12-N1-2j〜2p 証明鎖・自己完結レビューHTML</h1>
<p>このHTMLは、Stage12-N1-2jから2pまでの原文7本を一つのファイルへ埋め込んだ外部レビュー用資料です。数学的内容は変更していません。通常の主文書は <code>docs/stage12-n1-2-final.md</code> です。</p>

<div class="protocol">
<h2>レビュープロトコル</h2>
<p>レビュー開始前に、BUNDLE_ID、SOURCE_SNAPSHOT_COMMIT、CONTENT_SHA256、先頭・末尾文書名、START/END checkpointを復唱してください。末尾まで読めない場合は <code>UNREADABLE_SOURCE</code> としてください。</p>
<p>各指摘を <code>FATAL / MAJOR / MINOR / CLARIFICATION</code> に分類し、最終判定を <code>CLOSED / REPAIRABLE / OPEN / UNREADABLE_SOURCE</code> のいずれかで返してください。</p>
</div>

{''.join(sections)}

<div class="meta"><pre>CHECKPOINT=END_OF_MAIN
CONTENT_SHA256={content_sha256}
END_OF_BUNDLE={BUNDLE_ID}</pre></div>
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
