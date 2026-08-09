#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
MASTER = ROOT / "docs/stage14-toolbox/variable-dictionary.md"

EXPECTED = {
    "TB-DICTIONARY-euclid-five-columns": {
        "type": "DICTIONARY",
        "status": "CURRENT",
        "source_pr": 345,
        "source_merge_sha": "86b91ffcd8bae79452ef75f187c8570a3819d386",
    },
    "TB-DICTIONARY-witness-kernel-two-quadrics": {
        "type": "DICTIONARY",
        "status": "CURRENT",
        "source_pr": 345,
        "source_merge_sha": "86b91ffcd8bae79452ef75f187c8570a3819d386",
    },
    "TB-DICTIONARY-denominator-selectors": {
        "type": "DICTIONARY",
        "status": "CURRENT",
        "source_pr": 356,
        "source_merge_sha": "c2273d0388b48f8fb51d9dc69d8977efbc83db37",
    },
    "TB-DICTIONARY-physical-pair-compact-half-angle": {
        "type": "DICTIONARY",
        "status": "CURRENT",
        "source_pr": 360,
        "source_merge_sha": "42f4315b0659bd402a94adeb8822588ea153305a",
    },
    "TB-WARNING-cross-route-symbol-collisions": {
        "type": "WARNING",
        "status": "CURRENT",
        "source_pr": 360,
        "source_merge_sha": "42f4315b0659bd402a94adeb8822588ea153305a",
    },
}

REQUIRED_CARD_SECTIONS = [
    "## INPUT",
    "## OUTPUT",
    "## VARIABLE DICTIONARY",
    "## USED BY",
    "## DO NOT USE FOR",
    "## PROVENANCE NOTES",
]

MASTER_LOCKS = [
    "S = 2mn",
    "X = m^2-n^2 = (m-n)(m+n)",
    "Z=A/D^2",
    "G0=A",
    "d0=tau0*a*b",
    "d1=tau1*a*c",
    "d2=tau2*b*c",
    "D_min <= D_T",
    "G=g*d",
    "Z_T=-Nminus/R=-U*V/X2^2",
    "D_T^2=R/gcd(Nminus,R)",
    "R=H2-S2=kappa*t^2",
    "gcd(Nminus,R)=kappa*k^2",
    "Open Stage14-4bk is intentionally not used as canonical provenance",
]

CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")


def fail(msg: str) -> None:
    raise AssertionError(msg)


def main() -> None:
    data = json.loads(INDEX.read_text())
    cards = {c["id"]: c for c in data["cards"]}

    # Forward-compatible: ab established the dictionary and originally handed
    # off to ac, but later toolbox stages must be allowed to advance the index.
    next_stage = data.get("next_stage", "")
    match = CODE.fullmatch(next_stage)
    if not match or match.group(1) < "ac":
        fail(f"toolbox next_stage must be ac or later, got {next_stage!r}")
    if not str(data.get("next_theme", "")).strip():
        fail("toolbox next_theme must remain nonempty")

    for card_id, expected in EXPECTED.items():
        if card_id not in cards:
            fail(f"missing index card {card_id}")
        row = cards[card_id]
        for key, value in expected.items():
            if row.get(key) != value:
                fail(f"{card_id}: {key}={row.get(key)!r}, expected {value!r}")
        sha = row["source_merge_sha"]
        if not re.fullmatch(r"[0-9a-f]{40}", sha):
            fail(f"{card_id}: invalid source merge SHA")
        path = ROOT / row["path"]
        if not path.is_file():
            fail(f"{card_id}: card path missing: {row['path']}")
        text = path.read_text()
        for section in REQUIRED_CARD_SECTIONS:
            if section not in text:
                fail(f"{card_id}: missing section {section}")
        for header in [
            f"ID: {card_id}",
            f"TYPE: {row['type']}",
            f"STATUS: {row['status']}",
            f"SOURCE_PR: {row['source_pr']}",
            f"SOURCE_MERGE_SHA: {sha}",
        ]:
            if header not in text:
                fail(f"{card_id}: header/index mismatch for {header}")

    master = MASTER.read_text()
    for lock in MASTER_LOCKS:
        if lock not in master:
            fail(f"master dictionary missing lock: {lock}")

    # The central normalization chain must distinguish all three denominator notions.
    for token in ["D      =", "D_min  =", "D_T    ="]:
        if token not in master:
            fail(f"denominator selector separation missing: {token}")

    # Canonical cards may not depend on the open 4bk source.
    for card_id in EXPECTED:
        text = (ROOT / cards[card_id]["path"]).read_text()
        if "SOURCE_PR: 359" in text:
            fail(f"{card_id}: open PR #359 used as canonical source")

    print("Stage14-toolbox-ab variable dictionary audit: OK")
    print(f"cards={len(EXPECTED)} next={data['next_stage']}")


if __name__ == "__main__":
    main()
