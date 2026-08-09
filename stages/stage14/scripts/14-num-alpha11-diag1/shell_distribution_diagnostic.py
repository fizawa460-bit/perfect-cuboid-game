#!/usr/bin/env python3
from __future__ import annotations

import base64
import bz2
import csv
import io
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"
OUT = ROOT / "stages/stage14/data/14-num-alpha11-diag1/shell_distribution.json"
SHELLS = [(0,100_000_000),(100_000_000,200_000_000),(200_000_000,300_000_000),(300_000_000,400_000_000),(400_000_000,500_000_000)]


def load_rows():
    encoded = "".join(SOURCE.read_text(encoding="ascii").split())
    raw = bz2.decompress(base64.b64decode(encoded)).decode("utf-8")
    return [tuple(int(r[k]) for k in ("a","b","c","d","mask")) for r in csv.DictReader(io.StringIO(raw))]


def label(mask):
    return {0b011:"a",0b101:"b",0b110:"c",0b111:"triple"}.get(mask)


def shell(rows, lo, hi):
    counts = {"a":0,"b":0,"c":0,"triple":0}
    for row in rows:
        if lo < row[3] <= hi:
            q = label(row[4])
            if q is None:
                raise ArithmeticError(f"unexpected mask {row[4]}")
            counts[q] += 1
    n2 = counts["a"]+counts["b"]+counts["c"]
    ratios = {q:(counts[q]/n2 if n2 else None) for q in ("a","b","c")}
    # Binomial marginal standard errors are descriptive only; categories are multinomial.
    se = {q:(math.sqrt(ratios[q]*(1-ratios[q])/n2) if n2 else None) for q in ratios}
    return {"lo_exclusive":lo,"hi_inclusive":hi,"counts":counts,"N2":n2,"ratios":ratios,"marginal_binomial_se":se}


def main():
    rows = load_rows()
    if len(rows) != 3495 or len(set(rows)) != 3495:
        raise ArithmeticError(f"B500 source regression failed: rows={len(rows)} unique={len(set(rows))}")
    shells = [shell(rows,*bounds) for bounds in SHELLS]
    total = {q:sum(s["counts"][q] for s in shells) for q in ("a","b","c","triple")}
    if (total["a"],total["b"],total["c"],total["triple"]) != (1374,1371,750,0):
        raise ArithmeticError(f"alpha11 count regression failed: {total}")
    global_n = total["a"]+total["b"]+total["c"]
    global_ratio = {q:total[q]/global_n for q in ("a","b","c")}
    for s in shells:
        s["deviation_from_B500_cumulative"] = {q:s["ratios"][q]-global_ratio[q] for q in global_ratio}
        s["z_vs_B500_cumulative_descriptive"] = {
            q:(s["deviation_from_B500_cumulative"][q]/s["marginal_binomial_se"][q] if s["marginal_binomial_se"][q] else None)
            for q in global_ratio
        }
    adjacent = []
    for x,y in zip(shells,shells[1:]):
        adjacent.append({
            "from":x["hi_inclusive"],"to":y["hi_inclusive"],
            "absolute_ratio_shift":{q:abs(y["ratios"][q]-x["ratios"][q]) for q in ("a","b","c")},
        })
    report = {
        "stage":"14-num-alpha11-diag1",
        "classification":"B500M_NONOVERLAPPING_100M_SHELL_DIRECTION_DIAGNOSTIC",
        "source":"merged Stage14-num-alpha11 frozen B500m exact census",
        "source_rows":len(rows),
        "global_counts":total,
        "global_ratios":global_ratio,
        "shells":shells,
        "adjacent_shell_shifts":adjacent,
        "interpretation_boundary":{
            "descriptive_only":True,
            "cumulative_2pct_gate_not_reused_as_statistical_significance":True,
            "z_scores_not_independent_tests_because_global_ratio_contains_each_shell":True,
            "purpose":"expose whether cumulative ratios hide shell-local movement before finer shells/statistical modeling"
        },
        "next":"Stage14-num-alpha11-diag2 refine to 50m shells if shell-local movement is material"
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
