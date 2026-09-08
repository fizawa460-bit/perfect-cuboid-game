#!/usr/bin/env python3
"""Verify permanent repo transport of the Goal4AK degree-31 denominator."""
from __future__ import annotations

import base64
import gzip
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "stages/stage35-ex/35ex-35/goal4ak-degree31-denominator-transport.json"
MANIFEST_BLOB = "586a37bfe90a5fd3773c7d3525dde7c873ddedca"
EXPECTED_SCHEMA = "STAGE35_EX_GOAL4AK_DEGREE31_DENOMINATOR_PERMANENT_TRANSPORT_V1"
EXPECTED_CANONICAL = "f0e1187b89c3c7ea577e6404c75d3459a3d343d9b4bf56cdc4053a50f40a2522"
EXPECTED_TRANSPORT_BLOB = "5e25d4db44249f6eba0c03863e49f2522c8e54c8"
EXPECTED_B64_SHA = "ef7d9c7a360807a85b10a45b150a1636f01ed78bfc0f3b5ca05584eaf2749e1e"
EXPECTED_GZIP_SHA = "43b1ef891c21e3ec4279c70da0661d7987051b3eaaaf418db2158ede481a822d"
EXPECTED_RAW_SHA = "28d738a7a23df1ace371cabe3a476c270a54c6b7798e8172bd7111b14e25fc29"
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical_without_field(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parse_term(body: str) -> tuple[int, tuple[int, ...]]:
    factors = body.split("*")
    coeff = 1
    if factors and factors[0].isdigit():
        coeff = int(factors.pop(0))
    ex = [0] * len(NAMES)
    for f in factors:
        if "^" in f:
            name, power = f.split("^", 1)
            e = int(power)
        else:
            name, e = f, 1
        assert name in NAMES and e > 0
        ex[NAMES.index(name)] += e
    return coeff, tuple(ex)


def main() -> None:
    assert git_blob(MANIFEST) == MANIFEST_BLOB
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert m["schema"] == EXPECTED_SCHEMA
    assert m["canonical_sha256"] == EXPECTED_CANONICAL
    assert canonical_without_field(m) == EXPECTED_CANONICAL

    t = m["transport"]
    p = ROOT / t["path"]
    assert git_blob(p) == t["git_blob_sha1"] == EXPECTED_TRANSPORT_BLOB
    b64 = p.read_bytes()
    assert len(b64) == t["base64_chars"] == 11128
    assert hashlib.sha256(b64).hexdigest() == t["base64_sha256"] == EXPECTED_B64_SHA
    text = b64.decode("ascii")
    assert not any(ch.isspace() for ch in text)
    gz = base64.b64decode(text, validate=True)
    assert len(gz) == t["gzip_bytes"] == 8346
    assert hashlib.sha256(gz).hexdigest() == t["gzip_sha256"] == EXPECTED_GZIP_SHA
    raw = gzip.decompress(gz)
    assert len(raw) == t["raw_text_bytes"] == 42489
    assert hashlib.sha256(raw).hexdigest() == t["raw_text_sha256"] == EXPECTED_RAW_SHA

    poly = raw.decode("utf-8")
    terms = re.findall(r"[+-]?[^+-]+", poly)
    assert "".join(terms) == poly
    assert len(terms) == m["polynomial"]["term_count"] == 1542
    support = set()
    for term in terms:
        sign = -1 if term.startswith("-") else 1
        body = term[1:] if term[:1] in "+-" else term
        coeff, ex = parse_term(body)
        assert sign * coeff != 0
        assert sum(ex) == m["polynomial"]["homogeneous_degree"] == 31
        assert ex not in support
        support.add(ex)
    assert len(support) == 1542

    print("STAGE35_EX_GOAL4AK_DENOMINATOR_TRANSPORT=PASS")
    print("denominator_sha256=" + EXPECTED_RAW_SHA)


if __name__ == "__main__":
    main()
