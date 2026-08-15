#!/usr/bin/env python3
"""Stage25-20 reuse-only matched finite grid.

Projects the audited Stage14 NUM-R01 exact object ledger onto the frozen
Stage16-20 thresholds. No new cuboid enumeration is performed.
"""
from __future__ import annotations

import base64
import bz2
import csv
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "stages/stage16/16-20/counts.csv"
TARGET_B64 = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"
TARGET_FROZEN = ROOT / "stages/stage19/19-20/counts.csv"


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def decode_target_rows():
    payload = base64.b64decode(TARGET_B64.read_text(encoding="utf-8").strip())
    raw = bz2.decompress(payload).decode("utf-8")
    reader = csv.DictReader(io.StringIO(raw))
    rows = list(reader)
    if not rows:
        raise SystemExit("empty NUM-R01 object ledger")
    return reader.fieldnames or [], rows


def int_value(row, name):
    return int(row[name])


def find_geometry_columns(fields, rows):
    lower = {f.lower(): f for f in fields}
    if not all(k in lower for k in ("a", "b", "c")):
        raise SystemExit(f"cannot locate a,b,c columns in {fields}")
    a, b, c = lower["a"], lower["b"], lower["c"]

    preferred = ["d", "space_diagonal", "body_diagonal", "diagonal", "r"]
    candidates = [lower[x] for x in preferred if x in lower]
    # Fall back to every integer-looking column and identify d by the exact identity.
    if not candidates:
        candidates = list(fields)

    sample = rows[: min(50, len(rows))]
    for d in candidates:
        ok = True
        try:
            for row in sample:
                aa, bb, cc, dd = map(int, (row[a], row[b], row[c], row[d]))
                if aa * aa + bb * bb + cc * cc != dd * dd:
                    ok = False
                    break
        except (ValueError, KeyError):
            ok = False
        if ok:
            return a, b, c, d
    raise SystemExit(f"cannot infer space-diagonal column from {fields}")


def main():
    source = read_csv(SOURCE)
    fields, target = decode_target_rows()
    a, b, c, d = find_geometry_columns(fields, target)

    # NUM-R01 terminal manifest freezes 3495 exactly-two objects and triple=0 at 500m.
    if len(target) != 3495:
        raise SystemExit(f"NUM-R01 row-count mismatch: {len(target)} != 3495")

    # Strong adapter checks: canonical order, primitive gcd and exact body diagonal.
    from math import gcd
    for row in target:
        aa, bb, cc, dd = map(int, (row[a], row[b], row[c], row[d]))
        if not (0 < aa < bb < cc):
            raise SystemExit(f"noncanonical NUM-R01 row: {(aa,bb,cc,dd)}")
        if gcd(gcd(aa, bb), cc) != 1:
            raise SystemExit(f"nonprimitive NUM-R01 row: {(aa,bb,cc,dd)}")
        if aa * aa + bb * bb + cc * cc != dd * dd:
            raise SystemExit(f"space identity fail: {(aa,bb,cc,dd)}")

    frozen_n2 = {int(r["B"]): int(r["N2"]) for r in read_csv(TARGET_FROZEN)}
    def n2_at(B):
        return sum(1 for row in target if int(row[d]) <= B)

    # Cross-oracle lock at all Stage19-20 cutoffs covered by the 500m object ledger.
    for B, expected in frozen_n2.items():
        got = n2_at(B)
        if got != expected:
            raise SystemExit(f"Stage19 cross-oracle mismatch B={B}: {got}!={expected}")

    print(f"NUM_R01_FIELDS={fields}")
    print(f"GEOMETRY_COLUMNS={a},{b},{c},{d}")
    print("B,M1,N2,N2_over_M1")
    ratios = []
    for r in source:
        B = int(r["B"])
        m1 = int(r["M1"])
        n2 = n2_at(B)
        ratio = n2 / m1
        ratios.append(ratio)
        print(f"{B},{m1},{n2},{ratio:.15g}")

    print("STAGE19_CROSS_ORACLE=PASS")
    print("NUM_R01_ADAPTER=PASS")
    print("FINITE_DATA_USED_AS_PROOF=false")
    print("STAGE25_20_REPLAY=PASS")


if __name__ == "__main__":
    main()
