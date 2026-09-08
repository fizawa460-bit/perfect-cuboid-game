#!/usr/bin/env python3
"""Exact loader/evaluator for the provisional Goal4AK class-B rational function F_B.

The fixed representative is F_B=A31/B31 in Q(S)^*, where A31 is the audited
Goal4AJ numerator and B31 is the audited/materialized Goal4AJ denominator.
Both are homogeneous degree 31 in (a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w).
No local-evaluation or Brauer-Manin credit is granted by this loader.
"""
from __future__ import annotations

import base64
import gzip
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
NUM_MANIFEST = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24-gzip-chunks.json"
DEN_MANIFEST = ROOT / "stages/stage35-ex/35ex-35/goal4ak-degree31-denominator-transport.json"
NUM_MANIFEST_BLOB = "85b52e921f36fc445fd243db1a3b3f65bb298966"
DEN_MANIFEST_BLOB = "586a37bfe90a5fd3773c7d3525dde7c873ddedca"
NUM_SHA = "358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb"
DEN_SHA = "28d738a7a23df1ace371cabe3a476c270a54c6b7798e8172bd7111b14e25fc29"


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_numerator_text() -> str:
    assert git_blob(NUM_MANIFEST) == NUM_MANIFEST_BLOB
    m = json.loads(NUM_MANIFEST.read_text(encoding="utf-8"))
    parts = []
    for row in m["parts"]:
        p = ROOT / row["path"]
        b = p.read_bytes()
        assert len(b) == row["text_bytes"]
        assert hashlib.sha256(b).hexdigest() == row["text_sha256"]
        assert git_blob(p) == row["git_blob_sha1"]
        parts.append(b.decode("ascii"))
    joined = "".join(parts)
    assert len(joined) == m["concatenated_base64_chars"]
    assert hashlib.sha256(joined.encode("ascii")).hexdigest() == m["concatenated_base64_sha256"]
    gz = base64.b64decode(joined, validate=True)
    assert len(gz) == m["gzip_bytes"] and hashlib.sha256(gz).hexdigest() == m["gzip_sha256"]
    raw = gzip.decompress(gz)
    assert len(raw) == m["q_candidate_text_bytes"]
    assert hashlib.sha256(raw).hexdigest() == m["q_candidate_sha256"] == NUM_SHA
    return raw.decode("utf-8")


def load_denominator_text() -> str:
    assert git_blob(DEN_MANIFEST) == DEN_MANIFEST_BLOB
    m = json.loads(DEN_MANIFEST.read_text(encoding="utf-8"))
    t = m["transport"]
    p = ROOT / t["path"]
    assert git_blob(p) == t["git_blob_sha1"]
    b64 = p.read_bytes()
    assert len(b64) == t["base64_chars"]
    assert hashlib.sha256(b64).hexdigest() == t["base64_sha256"]
    text = b64.decode("ascii")
    assert not any(ch.isspace() for ch in text)
    gz = base64.b64decode(text, validate=True)
    assert len(gz) == t["gzip_bytes"] and hashlib.sha256(gz).hexdigest() == t["gzip_sha256"]
    raw = gzip.decompress(gz)
    assert len(raw) == t["raw_text_bytes"]
    assert hashlib.sha256(raw).hexdigest() == t["raw_text_sha256"] == DEN_SHA
    return raw.decode("utf-8")


def _monomial(mon: str) -> tuple[int, ...]:
    ex = [0] * len(NAMES)
    for f in mon.split("*"):
        if "^" in f:
            name, power = f.split("^", 1)
            e = int(power)
        else:
            name, e = f, 1
        if name not in NAMES or e <= 0:
            raise ValueError(f"bad monomial factor: {f}")
        ex[NAMES.index(name)] += e
    return tuple(ex)


def parse_polynomial(text: str) -> list[tuple[Fraction, tuple[int, ...]]]:
    signed = re.findall(r"[+-]?[^+-]+", text)
    if "".join(signed) != text:
        raise ValueError("polynomial tokenization mismatch")
    out = []
    seen = set()
    for t in signed:
        sign = -1 if t.startswith("-") else 1
        body = t[1:] if t[:1] in "+-" else t
        coeff = Fraction(sign, 1)
        mon = body
        m = re.fullmatch(r"\(\((\d+)/(\d+)\)\)\*(.+)", body)
        if m:
            coeff *= Fraction(int(m.group(1)), int(m.group(2)))
            mon = m.group(3)
        else:
            m = re.fullmatch(r"\((\d+)\)\*(.+)", body)
            if m:
                coeff *= int(m.group(1))
                mon = m.group(2)
            else:
                factors = body.split("*", 1)
                if factors[0].isdigit() and len(factors) == 2:
                    coeff *= int(factors[0])
                    mon = factors[1]
        ex = _monomial(mon)
        if ex in seen:
            raise ValueError("duplicate monomial")
        seen.add(ex)
        out.append((coeff, ex))
    return out


def load_terms() -> tuple[list[tuple[Fraction, tuple[int, ...]]], list[tuple[Fraction, tuple[int, ...]]]]:
    num = parse_polynomial(load_numerator_text())
    den = parse_polynomial(load_denominator_text())
    if len(num) != 5924 or len(den) != 1542:
        raise ValueError("support count mismatch")
    if any(sum(ex) != 31 for _, ex in num + den):
        raise ValueError("homogeneous degree mismatch")
    return num, den


def evaluate_terms(terms, coords) -> Fraction:
    q = tuple(Fraction(x) for x in coords)
    if len(q) != 7:
        raise ValueError("expected seven homogeneous coordinates")
    total = Fraction(0, 1)
    for coeff, ex in terms:
        term = coeff
        for x, e in zip(q, ex):
            if e:
                term *= x ** e
        total += term
    return total


def evaluate_FB(coords) -> Fraction:
    num, den = load_terms()
    a = evaluate_terms(num, coords)
    b = evaluate_terms(den, coords)
    if b == 0:
        raise ZeroDivisionError("F_B denominator vanishes at this point")
    return a / b


def evaluate_FB_affine(x, y, z, q, p, w) -> Fraction:
    # (a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w), h=1.
    return evaluate_FB((1, x, y, z, q, p, w))
