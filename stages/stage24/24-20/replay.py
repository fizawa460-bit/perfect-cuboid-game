#!/usr/bin/env python3
"""Reproduce Stage24 checkpoint20 matched Stage18/19 finite table.

Reuses the audited Stage18 exactly-two enumerator and the frozen Stage19 N2 CSV.
No new Stage19 enumerator is introduced.
"""
from __future__ import annotations
import csv
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
STAGE18_ENUM = ROOT / "stages/stage18/18-20/enumerate.py"
STAGE18_FROZEN = ROOT / "stages/stage18/18-20/counts.csv"
STAGE19_COUNTS = ROOT / "stages/stage19/19-20/counts.csv"
OUT = HERE.parent / "matched-counts.csv"

spec = importlib.util.spec_from_file_location("stage18_enum", STAGE18_ENUM)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

with STAGE19_COUNTS.open(newline="", encoding="utf-8") as f:
    target = [(int(r["B"]), int(r["N2"])) for r in csv.DictReader(f)]
thresholds = [b for b, _ in target]
records = mod.enumerate_fast(max(thresholds))
source = {row["B"]: row["M2"] for row in mod.rows(records, thresholds)}

# Recheck every threshold already frozen by Stage18 that lies in the replay window.
with STAGE18_FROZEN.open(newline="", encoding="utf-8") as f:
    frozen18 = {int(r["B"]): int(r["M2"]) for r in csv.DictReader(f)}
for b, m2 in frozen18.items():
    if b in source:
        assert source[b] == m2, (b, source[b], m2)

rows = []
for b, n2 in target:
    m2 = source[b]
    assert 0 <= n2 <= m2
    rows.append((b, m2, n2, n2 / m2))

with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(("B", "M2", "N2", "survivor_ratio"))
    w.writerows(rows)

print("STAGE24_20_MATCHED_REPLAY=PASS")
print(f"MAX_B={max(thresholds)}")
print(f"ROWS={len(rows)}")
