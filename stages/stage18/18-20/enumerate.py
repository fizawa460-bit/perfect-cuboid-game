#!/usr/bin/env python3
"""Stage18-20 deterministic exactly-two-face census."""

import argparse
import csv
from collections import defaultdict
from math import gcd, isqrt
from pathlib import Path

DEFAULT = (50, 100, 200, 400, 800, 1200, 1600, 2000)

def square(n):
    r = isqrt(n)
    return r * r == n

def face_count(a, b, c):
    return sum((square(a*a + b*b), square(a*a + c*c), square(b*b + c*c)))

def pythagorean_adjacency(B):
    adj = defaultdict(set)
    m = 2
    while m*m + 1 <= B:
        for n in range(1, m):
            if ((m - n) & 1) == 0 or gcd(m, n) != 1:
                continue
            h = m*m + n*n
            if h > B:
                break
            u = m*m - n*n
            v = 2*m*n
            for k in range(1, B // h + 1):
                x, y = k*u, k*v
                adj[x].add(y)
                adj[y].add(x)
        m += 1
    return adj

def enumerate_fast(B):
    adj = pythagorean_adjacency(B)
    out = {}
    B2 = B * B
    for e, partners in adj.items():
        ps = sorted(partners)
        for i, x in enumerate(ps):
            for y in ps[i+1:]:
                a, b, c = sorted((e, x, y))
                if a == b or b == c:
                    continue
                if gcd(gcd(a, b), c) != 1:
                    continue
                r2 = a*a + b*b + c*c
                if r2 > B2:
                    continue
                if face_count(a, b, c) == 2:
                    out[(a, b, c)] = r2
    return out

def enumerate_brute(B):
    out = {}
    B2 = B * B
    for a in range(1, B):
        for b in range(a+1, B):
            ab = a*a + b*b
            if ab + (b+1)*(b+1) > B2:
                break
            cmax = isqrt(B2 - ab)
            for c in range(b+1, cmax+1):
                if gcd(gcd(a, b), c) != 1:
                    continue
                if face_count(a, b, c) == 2:
                    out[(a, b, c)] = ab + c*c
    return out

def rows(records, thresholds):
    return [{"B": B, "M2": sum(r2 <= B*B for r2 in records.values())} for B in thresholds]

def read_counts(path):
    with path.open(newline="", encoding="utf-8") as f:
        return [{"B": int(r["B"]), "M2": int(r["M2"])} for r in csv.DictReader(f)]

def write_counts(path, data):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=("B", "M2"))
        w.writeheader(); w.writerows(data)

def verify(path, small):
    frozen = read_counts(path)
    thresholds = tuple(r["B"] for r in frozen)
    if not thresholds or thresholds != tuple(sorted(set(thresholds))):
        raise SystemExit("thresholds must be strictly increasing")
    regen = rows(enumerate_fast(max(thresholds)), thresholds)
    if regen != frozen:
        raise SystemExit(f"frozen census mismatch: {regen}")
    fast_small = enumerate_fast(small)
    brute_small = enumerate_brute(small)
    if fast_small != brute_small:
        raise SystemExit(f"small-cutoff set mismatch: fast={len(fast_small)} brute={len(brute_small)}")
    print(f"SMALL_CUTOFF_CROSSCHECK_B={small}:PASS")
    print(f"FROZEN_CENSUS_MAX_B={max(thresholds)}:PASS")
    print("STAGE18_20_VERIFY=PASS")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path)
    p.add_argument("--verify", type=Path)
    p.add_argument("--self-check-b", type=int, default=200)
    p.add_argument("--thresholds", default=",".join(map(str, DEFAULT)))
    a = p.parse_args()
    if a.verify:
        verify(a.verify, a.self_check_b); return
    thresholds = tuple(int(x) for x in a.thresholds.split(",") if x)
    if not thresholds or thresholds != tuple(sorted(set(thresholds))) or thresholds[0] <= 0:
        raise SystemExit("thresholds must be positive and strictly increasing")
    data = rows(enumerate_fast(max(thresholds)), thresholds)
    if a.output:
        write_counts(a.output, data)
    else:
        w = csv.DictWriter(__import__("sys").stdout, fieldnames=("B", "M2"))
        w.writeheader(); w.writerows(data)

if __name__ == "__main__":
    main()
