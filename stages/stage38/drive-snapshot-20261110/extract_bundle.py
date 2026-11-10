#!/usr/bin/env python3
"""Restore the verbatim text and archived ZIP bytes from Stage38 Drive mirror.

Read-only source bundles remain untouched. Python standard library only.
Run: python stages/stage38/drive-snapshot-20261110/extract_bundle.py --output /tmp/stage38-drive
"""
from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def safe_name(name: str) -> str:
    if not name or Path(name).name != name or name in (".", ".."):
        raise ValueError(f"Unsafe Drive filename: {name!r}")
    return name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((HERE / "MANIFEST.json").read_text(encoding="utf-8"))
    written = 0
    files_cache: dict[Path, dict] = {}

    for rec in manifest["records"]:
        target_scope = rec["storage"].removeprefix(
            "stages/stage38/drive-snapshot-20261110/"
        ).split("/")[0]
        target = args.output / target_scope / safe_name(rec["name"])
        target.parent.mkdir(parents=True, exist_ok=True)
        status = rec["status"]
        src = REPO / rec["storage"]

        if status == "CONTENT_IN_JSON_BUNDLE":
            if src not in files_cache:
                files_cache[src] = {
                    f["id"]: f for f in json.loads(src.read_text(encoding="utf-8"))["files"]
                }
            original = files_cache[src][rec["file_id"]]
            if original["title"] != rec["name"]:
                raise AssertionError("Manifest title mismatch")
            payload = original["content"].encode("utf-8")
        elif status == "EXACT_ZIP_BYTES_BASE64_RECONSTRUCTABLE":
            payload = base64.b64decode(src.read_text(encoding="ascii"), validate=False)
        elif status == "NATIVE_DOC_PARAGRAPH_TEXT_SNAPSHOT_NOT_FORMAT_IDENTICAL":
            data = json.loads(src.read_text(encoding="utf-8"))
            payload = "".join(p["text"] for p in data["paragraphs"]).encode("utf-8")
            target = target.with_suffix(target.suffix + ".txt")
        else:
            raise ValueError(f"Unknown status {status!r}")

        if rec.get("bytes") is not None and status == "EXACT_ZIP_BYTES_BASE64_RECONSTRUCTABLE":
            if len(payload) != rec["bytes"]:
                raise AssertionError(f"ZIP length mismatch: {rec['name']}")
        target.write_bytes(payload)
        written += 1

    assert written == manifest["counts"]["total"], written
    print(f"restored {written} Stage38 files to {args.output}")


if __name__ == "__main__":
    main()
