#!/usr/bin/env python3
"""Build and verify the closed Stage14 R04 self-contained review bundle."""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import subprocess
import sys
from pathlib import Path


BUNDLE_ID = "STAGE14-FINAL-SELF-CONTAINED-20260812-R04"
SOURCE_SNAPSHOT_COMMIT = "81bc12bc28f159e3af2b26e4b41ef406a4f98339"
SOURCE = Path("docs/stage14-final-self-contained.md")
LEDGER = Path("docs/review/stage14-final-self-contained-provenance-20260812-r01.md")
BUNDLE = Path("review/STAGE14-FINAL-SELF-CONTAINED-20260812-R04.html")
MANIFEST = Path("docs/review/stage14-final-self-contained-manifest-20260812-r04.md")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def slugify(value: str, used: set[str]) -> str:
    plain = re.sub(r"[`*_\\]", "", value).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", plain).strip("-") or "section"
    base = slug
    n = 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


def inline_markup(value: str) -> str:
    code_parts: list[str] = []

    def keep_code(match: re.Match[str]) -> str:
        code_parts.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"\x00CODE{len(code_parts) - 1}\x00"

    value = re.sub(r"`([^`]+)`", keep_code, value)
    value = html.escape(value, quote=False)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", value)
    value = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        value,
    )
    for i, code in enumerate(code_parts):
        value = value.replace(f"\x00CODE{i}\x00", code)
    return value


def render_markdown(text: str, id_prefix: str = "") -> tuple[str, list[tuple[int, str, str]]]:
    lines = text.splitlines()
    out: list[str] = []
    toc: list[tuple[int, str, str]] = []
    used: set[str] = set()
    paragraph: list[str] = []
    list_kind: str | None = None
    in_code = False
    code_lines: list[str] = []
    in_math = False
    math_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{inline_markup(' '.join(s.strip() for s in paragraph))}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            out.append(f"</{list_kind}>")
            list_kind = None

    i = 0
    while i < len(lines):
        line = lines[i]

        if in_code:
            if line.startswith("```"):
                out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                code_lines.append(line)
            i += 1
            continue

        if in_math:
            if line.strip() == r"\]":
                out.append(f'<div class="math" role="math">{html.escape(chr(10).join(math_lines))}</div>')
                math_lines = []
                in_math = False
            else:
                math_lines.append(line)
            i += 1
            continue

        if line.startswith("```"):
            flush_paragraph()
            close_list()
            in_code = True
            i += 1
            continue

        if line.strip() == r"\[":
            flush_paragraph()
            close_list()
            in_math = True
            i += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            title = heading.group(2).strip()
            sid = id_prefix + slugify(title, used)
            out.append(f'<h{level} id="{sid}">{inline_markup(title)}<a class="anchor" href="#{sid}" aria-label="Link to section">#</a></h{level}>')
            if level <= 3:
                toc.append((level, title, sid))
            i += 1
            continue

        if re.match(r"^\s*\|.*\|\s*$", line) and i + 1 < len(lines) and re.match(
            r"^\s*\|?\s*:?-+", lines[i + 1]
        ):
            flush_paragraph()
            close_list()
            rows: list[list[str]] = []
            while i < len(lines) and re.match(r"^\s*\|.*\|\s*$", lines[i]):
                cells = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            if len(rows) >= 2:
                headers = rows[0]
                body = rows[2:]
                out.append('<div class="table-wrap"><table><thead><tr>')
                out.extend(f"<th>{inline_markup(cell)}</th>" for cell in headers)
                out.append("</tr></thead><tbody>")
                for row in body:
                    out.append("<tr>")
                    row = row + [""] * (len(headers) - len(row))
                    out.extend(f"<td>{inline_markup(cell)}</td>" for cell in row[: len(headers)])
                    out.append("</tr>")
                out.append("</tbody></table></div>")
            continue

        item = re.match(r"^\s*([-*])\s+(.+)$", line)
        numbered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if item or numbered:
            flush_paragraph()
            kind = "ul" if item else "ol"
            if list_kind != kind:
                close_list()
                out.append(f"<{kind}>")
                list_kind = kind
            value = item.group(2) if item else numbered.group(1)
            out.append(f"<li>{inline_markup(value)}</li>")
            i += 1
            continue

        if line.startswith(">"):
            flush_paragraph()
            close_list()
            quotes: list[str] = []
            while i < len(lines) and lines[i].startswith(">"):
                quotes.append(lines[i].lstrip("> "))
                i += 1
            out.append(f"<blockquote>{inline_markup(' '.join(quotes))}</blockquote>")
            continue

        if re.match(r"^\s*---+\s*$", line):
            flush_paragraph()
            close_list()
            out.append("<hr>")
            i += 1
            continue

        if not line.strip():
            flush_paragraph()
            close_list()
        else:
            paragraph.append(line)
        i += 1

    flush_paragraph()
    close_list()
    if in_code:
        raise ValueError("unclosed code fence")
    if in_math:
        raise ValueError("unclosed display math block")
    return "\n".join(out), toc


def build_html(source_text: str, ledger_text: str) -> str:
    source_html, source_toc = render_markdown(source_text, "doc-")
    ledger_html, _ = render_markdown(ledger_text, "ledger-")
    nav = []
    for level, title, sid in source_toc:
        if level == 2:
            nav.append(f'<a href="#{sid}">{inline_markup(title)}</a>')

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{BUNDLE_ID}</title>
<style>
:root{{--ink:#15202b;--muted:#5d6975;--line:#d7dde3;--paper:#fff;--soft:#f4f7f9;--accent:#155eef;--accent2:#0c7a5b;--warn:#9a6700;--bad:#b42318;--shadow:0 10px 30px rgba(20,32,43,.08)}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:#eef2f5;color:var(--ink);font:15.5px/1.62 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
a{{color:var(--accent)}}code,pre,.math{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}code{{background:#edf1f5;border-radius:4px;padding:.08em .32em;font-size:.91em}}
.hero{{background:linear-gradient(135deg,#102a43,#155eef 70%,#35a77a);color:white;padding:54px max(24px,calc((100vw - 1240px)/2)) 42px}}.eyebrow{{font-weight:700;letter-spacing:.12em;text-transform:uppercase;font-size:12px;opacity:.85}}h1{{font-size:clamp(30px,5vw,54px);line-height:1.08;margin:12px 0 18px;max-width:950px}}.subtitle{{font-size:19px;max-width:900px;opacity:.9}}
.hero-meta{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin-top:28px}}.meta-card{{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);border-radius:12px;padding:13px 15px}}.meta-card b{{display:block;font-size:11px;letter-spacing:.08em;text-transform:uppercase;opacity:.75}}.meta-card code{{display:block;margin-top:5px;background:transparent;padding:0;color:#fff;overflow-wrap:anywhere}}
.verdict-strip{{max-width:1240px;margin:-22px auto 24px;background:var(--paper);border-radius:14px;box-shadow:var(--shadow);display:grid;grid-template-columns:repeat(4,1fr);overflow:hidden}}.verdict-strip div{{padding:18px 20px;border-right:1px solid var(--line)}}.verdict-strip div:last-child{{border:0}}.verdict-strip span{{display:block;color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.05em}}.verdict-strip strong{{display:block;margin-top:5px;font-size:17px}}.good{{color:var(--accent2)}}.open{{color:var(--warn)}}
.layout{{max-width:1240px;margin:0 auto 60px;display:grid;grid-template-columns:245px minmax(0,1fr);gap:24px;padding:0 18px}}nav{{position:sticky;top:14px;align-self:start;max-height:calc(100vh - 28px);overflow:auto;background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:15px}}nav strong{{display:block;margin:2px 6px 10px;font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}}nav a{{display:block;text-decoration:none;color:var(--ink);padding:7px 8px;border-radius:6px;font-size:13px}}nav a:hover{{background:var(--soft);color:var(--accent)}}
main{{min-width:0;background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:clamp(24px,5vw,58px);box-shadow:var(--shadow)}}article>h1:first-child{{display:none}}h2{{font-size:29px;line-height:1.22;margin:56px 0 18px;padding-top:6px;border-top:1px solid var(--line)}}h3{{font-size:21px;line-height:1.3;margin:34px 0 12px}}h4{{font-size:17px;margin:25px 0 8px}}.anchor{{opacity:0;text-decoration:none;margin-left:8px;font-size:.7em}}h2:hover .anchor,h3:hover .anchor,h4:hover .anchor{{opacity:.45}}p{{margin:10px 0 16px}}li{{margin:5px 0}}hr{{border:0;border-top:1px solid var(--line);margin:34px 0}}blockquote{{margin:18px 0;padding:14px 18px;border-left:4px solid var(--accent);background:var(--soft)}}
.math{{white-space:pre-wrap;overflow:auto;text-align:center;background:#f8fafc;border:1px solid var(--line);border-radius:9px;padding:16px;margin:18px 0;color:#102a43}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#102a43;color:#eaf2f8;border-radius:9px;padding:17px;overflow:auto;font-size:13px;line-height:1.5}}pre code{{background:transparent;color:inherit;padding:0}}
.table-wrap{{overflow:auto;margin:18px 0 28px;border:1px solid var(--line);border-radius:9px}}table{{border-collapse:collapse;width:100%;min-width:650px;font-size:13.5px}}th{{position:sticky;top:0;background:#eaf0f6;text-align:left}}th,td{{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}}tr:last-child td{{border-bottom:0}}tbody tr:nth-child(even){{background:#fafbfd}}
.nonclaims{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:20px 0 40px}}.nonclaims div{{border:1px solid #f0c6c2;background:#fff7f6;border-radius:9px;padding:12px;color:#7a271a;font-size:13px}}.ledger{{margin-top:70px;border-top:5px solid #102a43;padding-top:24px}}.ledger-label{{display:inline-block;background:#102a43;color:#fff;border-radius:999px;padding:5px 10px;font-size:12px;font-weight:700}}
.footer{{max-width:1240px;margin:0 auto 40px;padding:0 20px;color:var(--muted);font-size:12px}}
@media(max-width:900px){{.verdict-strip{{margin:0 18px 20px;grid-template-columns:1fr 1fr}}.verdict-strip div:nth-child(2){{border-right:0}}.layout{{grid-template-columns:1fr}}nav{{position:static;max-height:none}}.nonclaims{{grid-template-columns:1fr}}}}
@media(prefers-color-scheme:dark){{:root{{--ink:#e6edf3;--muted:#9da7b1;--line:#38434d;--paper:#182129;--soft:#202c35;--accent:#75a7ff;--accent2:#66d1ad;--warn:#f4c152}}body{{background:#101820}}code{{background:#283641}}.math{{background:#101820;color:#e6edf3}}th{{background:#26343f}}tbody tr:nth-child(even){{background:#1c2730}}.nonclaims div{{background:#351f20;border-color:#713638;color:#ffb4ac}}}}
@media print{{body{{background:white}}.hero{{padding:25px;color:#000;background:white;border-bottom:2px solid #000}}.hero-meta,.verdict-strip,nav,.footer{{display:none}}.layout{{display:block;padding:0}}main{{border:0;box-shadow:none;padding:0}}a{{color:#000;text-decoration:none}}h2{{break-after:avoid}}.table-wrap{{overflow:visible}}}}
</style>
</head>
<body>
<header class="hero">
  <div class="eyebrow">Frozen mathematical review bundle · 2026-08-12</div>
  <h1>Stage14 final self-contained review</h1>
  <div class="subtitle">Definitions, active proof chain, route-specific stopping gates, S/X accounting audit, literature contracts, open problems, and compact provenance — in one standalone HTML file.</div>
  <div class="hero-meta">
    <div class="meta-card"><b>Bundle ID</b><code>{BUNDLE_ID}</code></div>
    <div class="meta-card"><b>Audited main snapshot</b><code>{SOURCE_SNAPSHOT_COMMIT}</code></div>
    <div class="meta-card"><b>Scope</b><code>primitive canonical exact-two · d ≤ B</code></div>
    <div class="meta-card"><b>Final classification</b><code>SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS</code></div>
  </div>
</header>
<section class="verdict-strip" aria-label="Final theorem status">
  <div><span>Main result</span><strong>N₂(B) ≪ B<sup>1/2+o(1)</sup></strong></div>
  <div><span>Whole-family exponent</span><strong class="good">1/2</strong></div>
  <div><span>Strict sub-sqrt</span><strong class="open">Not proved</strong></div>
  <div><span>Matching lower bound</span><strong class="open">Not proved</strong></div>
</section>
<div class="layout">
  <nav aria-label="Document sections"><strong>Contents</strong>{''.join(nav)}<a href="#provenance-ledger"><b>Appendix · provenance</b></a></nav>
  <main>
    <div class="nonclaims"><div>No asymptotic equivalence or exact constant.</div><div>No proof that square-root is the true order.</div><div>No perfect-cuboid existence or nonexistence result.</div></div>
    <article>{source_html}</article>
    <section class="ledger" id="provenance-ledger"><span class="ledger-label">Appendix</span>{ledger_html}</section>
  </main>
</div>
<footer class="footer">Deterministically generated from the canonical source and compact ledger. No external CSS, JavaScript, fonts, images, or network resources are required.</footer>
</body>
</html>
"""


def build_manifest(content_sha: str, source_sha: str, ledger_sha: str) -> str:
    return f"""# Stage14 final self-contained R04 manifest

```text
BUNDLE_ID={BUNDLE_ID}
SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}
CONTENT_SHA256={content_sha}
SOURCE_LEDGER_SHA256={ledger_sha}
CANONICAL_SOURCE_SHA256={source_sha}
COMPLETED_THROUGH=Stage14-Work-coX53@{SOURCE_SNAPSHOT_COMMIT}
THEOREM_SCOPE=primitive_canonical_integer-space-diagonal_exactly-two-face_whole-family_d_le_B
WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MATCHING_LOWER_BOUND_PROVED=false
TRUE_ORDER_OF_N2_PROVED=false
PERFECT_CUBOID_EXISTENCE_RESULT=NONE
SELF_CONTAINMENT_STATUS=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
FINAL_BUNDLE_STATUS=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
MAIN_ROUTE_STATUS=PARKED_EXTERNAL_GATE:UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
T_ROUTE_STATUS=PARKED_EXTERNAL_GATE:SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
S_ROUTE_STATUS=PARKED_EXTERNAL_GATE:ValuationAveragedReducedModulusTargetClassPrincipalDominationOrMeasurePreservingAdapter
EXTERNAL_REVIEW_P0_COUNT=3
EXTERNAL_REVIEW_P1_COUNT=8
BUNDLE_PATH={BUNDLE.as_posix()}
CANONICAL_SOURCE_PATH={SOURCE.as_posix()}
SOURCE_LEDGER_PATH={LEDGER.as_posix()}
```

## Integrity contract

`CONTENT_SHA256` is the SHA-256 of the standalone HTML bytes. `SOURCE_LEDGER_SHA256` is the SHA-256 of the compact provenance-ledger bytes, and `CANONICAL_SOURCE_SHA256` is the SHA-256 of the canonical Markdown bytes. The HTML embeds both the canonical source and the ledger and has no external runtime assets.

The snapshot is the latest merged `main` inspected before this bundle branch was created. It records the mathematical source state, not the later bundle commit.
"""


def validate_semantics(source_text: str, ledger_text: str, document: str) -> None:
    required = [
        "N_2(B)\\ll B^{1/2+o(1)}",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        "MATCHING_LOWER_BOUND_PROVED=false",
        "TRUE_ORDER_OF_N2_PROVED=false",
        "PERFECT_CUBOID_EXISTENCE_OR_NONEXISTENCE_PROVED=false",
        "MAIN_ROUTE_STATUS=PARKED_EXTERNAL_GATE",
        "T_ROUTE_STATUS=PARKED_EXTERNAL_GATE",
        "S_ROUTE_STATUS=PARKED_EXTERNAL_GATE",
        "EXTERNAL_REVIEW_P0_COUNT=3",
        "EXTERNAL_REVIEW_P1_COUNT=8",
        "UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment",
        "SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio",
        "FINAL_BUNDLE_STATUS=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS",
    ]
    for token in required:
        if token not in source_text:
            raise ValueError(f"required source token missing: {token}")
    if "q26" not in ledger_text or "#819" not in ledger_text:
        raise ValueError("ledger is missing final q/X provenance")
    forbidden = [
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=true",
        "MATCHING_LOWER_BOUND_PROVED=true",
        "TRUE_ORDER_OF_N2_PROVED=true",
        "PERFECT_CUBOID_EXISTENCE_OR_NONEXISTENCE_PROVED=true",
        "N_2(B) ~ B^(1/2)",
    ]
    for token in forbidden:
        if token in source_text or token in ledger_text:
            raise ValueError(f"forbidden claim present: {token}")
    if "http://" in document or "https://" in document:
        # The standalone bundle deliberately renders citations as text rather than links.
        raise ValueError("standalone HTML unexpectedly contains a network URL")


def git_snapshot_check() -> None:
    subprocess.run(["git", "cat-file", "-e", f"{SOURCE_SNAPSHOT_COMMIT}^{{commit}}"], check=True)
    subprocess.run(["git", "merge-base", "--is-ancestor", SOURCE_SNAPSHOT_COMMIT, "HEAD"], check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify generated files without writing")
    args = parser.parse_args()

    git_snapshot_check()
    source_text = SOURCE.read_text(encoding="utf-8")
    ledger_text = LEDGER.read_text(encoding="utf-8")
    document = build_html(source_text, ledger_text)
    validate_semantics(source_text, ledger_text, document)
    document_bytes = document.encode("utf-8")
    content_sha = sha256_bytes(document_bytes)
    source_sha = sha256_bytes(source_text.encode("utf-8"))
    ledger_sha = sha256_bytes(ledger_text.encode("utf-8"))
    manifest = build_manifest(content_sha, source_sha, ledger_sha)

    expected = {BUNDLE: document_bytes, MANIFEST: manifest.encode("utf-8")}
    if args.check:
        failures = []
        for path, data in expected.items():
            if not path.exists():
                failures.append(f"missing: {path}")
            elif path.read_bytes() != data:
                failures.append(f"stale: {path}")
        if failures:
            print("\n".join(failures), file=sys.stderr)
            return 1
    else:
        for path, data in expected.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

    print(f"BUNDLE_ID={BUNDLE_ID}")
    print(f"SOURCE_SNAPSHOT_COMMIT={SOURCE_SNAPSHOT_COMMIT}")
    print(f"CONTENT_SHA256={content_sha}")
    print(f"SOURCE_LEDGER_SHA256={ledger_sha}")
    print("INTEGRITY_STATUS=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
