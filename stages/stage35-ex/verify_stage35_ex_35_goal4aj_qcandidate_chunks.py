#!/usr/bin/env python3
"""Verify the permanent repo transport of the Goal4AJ degree-31 Q candidate."""
from __future__ import annotations

import base64
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24-gzip-chunks.json"
MANIFEST_BLOB = "85b52e921f36fc445fd243db1a3b3f65bb298966"
EXPECTED_SCHEMA = "STAGE35_EX_GOAL4AJ_GEN24_QCANDIDATE_PERMANENT_GZIP_CHUNKS_V1"
EXPECTED_B64_SHA = "4658939e4be602c9e609f2b7ac6e73265627674ddca2a1dda4c00a16a82cd1d1"
EXPECTED_GZIP_SHA = "4758734a80f4ec5c0444acf9b97d0edcbb00a6ee26f1b59c622c711a5d20be8b"
EXPECTED_Q_SHA = "358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb"
EXPECTED_PART_BLOBS = [
    "d7e4af81079f03d2f80b030e18f267ef69f7c95b",
    "fae024acdc3f9b85d8662a8aacc14a94c87c3efb",
    "06578c207b1aa38dd57781b7cbb6ff5c364764bd",
    "b1a2a250b438ef567c0fa39d0d3a6289aacaa025",
]
EXPECTED_PART_SHA256 = [
    "866f651d97122b67c5b4eb980a4914f220602b6a6fe52ac92fcc01069a1987fc",
    "6e0731b85bc07e14553c1a69ddcbb92e912b15b6f8f0636126e8dac78b95f87a",
    "86a2efecba5486a0c9aea576b3a3df036a6f03ae65cdf773c3b52d9ce201efbf",
    "f804c18c7814e4a7ea5bb00be61d2219e9561f794b45b2557fada4ebc3d6c2e3",
]


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def main() -> None:
    assert git_blob(MANIFEST) == MANIFEST_BLOB
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert m["schema"] == EXPECTED_SCHEMA
    assert m["concatenated_base64_chars"] == 60032
    assert m["concatenated_base64_sha256"] == EXPECTED_B64_SHA
    assert m["gzip_bytes"] == 45022 and m["gzip_sha256"] == EXPECTED_GZIP_SHA
    assert m["q_candidate_text_bytes"] == 208802 and m["q_candidate_sha256"] == EXPECTED_Q_SHA
    assert len(m["parts"]) == 4

    texts = []
    for i, row in enumerate(m["parts"]):
        p = ROOT / row["path"]
        b = p.read_bytes()
        assert len(b) == row["text_bytes"] == 15008
        assert hashlib.sha256(b).hexdigest() == row["text_sha256"] == EXPECTED_PART_SHA256[i]
        assert git_blob(p) == row["git_blob_sha1"] == EXPECTED_PART_BLOBS[i]
        texts.append(b.decode("ascii"))

    joined = "".join(texts)
    assert len(joined) == 60032
    assert hashlib.sha256(joined.encode("ascii")).hexdigest() == EXPECTED_B64_SHA
    gz = base64.b64decode(joined, validate=True)
    assert len(gz) == 45022 and hashlib.sha256(gz).hexdigest() == EXPECTED_GZIP_SHA
    raw = gzip.decompress(gz)
    assert len(raw) == 208802 and hashlib.sha256(raw).hexdigest() == EXPECTED_Q_SHA
    assert raw.decode("utf-8")
    print("STAGE35_EX_GOAL4AJ_QCANDIDATE_CHUNKS=PASS")
    print("q_candidate_sha256=" + EXPECTED_Q_SHA)


if __name__ == "__main__":
    main()
