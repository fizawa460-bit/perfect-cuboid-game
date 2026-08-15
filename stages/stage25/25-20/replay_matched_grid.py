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
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "stages/stage16/16-20/counts.csv"
TARGET_B64 = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"
TARGET_FROZEN = ROOT / "stages/stage19/19-20/counts.csv"
MATCHED = ROOT / "stages/stage25/25-20/matched-counts.csv"


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


def find_geometry_columns(fields, rows):
    lower = {f.lower(): f for f in fields}
    if not all(k in lower for k in ("a", "b", "c")):
        raise SystemExit(f"cannot locate a,b,c columns in {fields}")
    a, b, c = lower["a"], lower["b"], lower["c"]
    preferred = ["d", "space_diagonal", "body_diagonal", "diagonal", "r"]
    candidates = [lower[x] for x in preferred if x in lower] or list(fields)
    sample = rows[: min(50, len(rows))]
    for d in candidates:
        try:
            if all(
                int(row[a]) ** 2 + int(row[b]) ** 2 + int(row[c]) ** 2 == int(row[d]) ** 2
                for row in sample
            ):
                return a, b, c, d
        except (ValueError, KeyError):
            pass
    raise SystemExit(f"cannot infer space-diagonal column from {fields}")


def main():
    source = read_csv(SOURCE)
    fields, target = decode_target_rows()
    a, b, c, d = find_geometry_columns(fields, target)

    if len(target) != 3495:
        raise SystemExit(f"NUM-R01 row-count mismatch: {len(target)} != 3495")

    for row in target:
        aa, bb, cc, dd = map(int, (row[a], row[b], row[c], row[d]))
        if not (0 < aa < bb < cc):
            raise SystemExit(f"noncanonical NUM-R01 row: {(aa,bb,cc,dd)}")
        if gcd(gcd(aa, bb), cc) != 1:
            raise SystemExit(f"nonprimitive NUM-R01 row: {(aa,bb,cc,dd)}")
        if aa * aa + bb * bb + cc * cc != dd * dd:
            raise SystemExit(f"space identity fail: {(aa,bb,cc,dd)}")

    def n2_at(B):
        return sum(1 for row in target if int(row[d]) <= B)

    frozen_n2 = {int(r["B"]): int(r["N2"]) for r in read_csv(TARGET_FROZEN)}
    for B, expected in frozen_n2.items():
        got = n2_at(B)
        if got != expected:
            raise SystemExit(f"Stage19 cross-oracle mismatch B={B}: {got}!={expected}")

    generated = []
    print(f"NUM_R01_FIELDS={fields}")
    print(f"GEOMETRY_COLUMNS={a},{b},{c},{d}")
    print("B,M1,N2,N2_over_M1")
    for r in source:
        B = int(r["B"])
        m1 = int(r["M1"])
        n2 = n2_at(B)
        ratio = n2 / m1
        generated.append((B, m1, n2, ratio))
        print(f"{B},{m1},{n2},{ratio:.15g}")

    committed = read_csv(MATCHED)
    if len(committed) != len(generated):
        raise SystemExit("matched-counts.csv row-count mismatch")
    for row, (B, m1, n2, ratio) in zip(committed, generated):
        if int(row["B"]) != B or int(row["M1"]) != m1 or int(row["N2"]) != n2:
            raise SystemExit(f"matched-counts.csv exact mismatch at B={B}")
        if abs(float(row["N2_over_M1"]) - ratio) > 1e-18:
            raise SystemExit(f"matched-counts.csv ratio mismatch at B={B}")

    print("STAGE19_CROSS_ORACLE=PASS")
    print("NUM_R01_ADAPTER=PASS")
    print("COMMITTED_MATCHED_GRID=PASS")
    print("FINITE_DATA_USED_AS_PROOF=false")
    print("STAGE25_20_REPLAY=PASS")


if __name__ == "__main__":
    main()
