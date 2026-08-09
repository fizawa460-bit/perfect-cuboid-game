#!/usr/bin/env python3
"""Stage14-num4 replay/audit tool.

Input is the canonical Stage14-num3 B=100m object CSV with columns
`a,b,c,d,mask`.  The tool revalidates the frozen num3 population and derives
face/edge fingerprints used by the compact num4 manifest.  It performs no PARI
rank, Selmer, canonical-height, or Kummer recomputation.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from math import gcd, isqrt, lcm
from pathlib import Path

BOUND = 100_000_000
PRIMES = (2, 3, 5, 7, 11, 13)
EXPECTED = {
    "object_count": 1875,
    "active_face_count": 2687,
    "edge_count": 1875,
    "max_degree": 11,
    "counts": {"a": 729, "b": 758, "c": 388, "total": 1875, "triple": 0},
    "object_key_sha256": "b8151aedbf46f33700b213c79a5227fa62653d2279eed954103a2b9e768fff42",
    "object_key_mask_sha256": "2ac9a994f735d2d4f8f3c519145de17d920bdcf9841f32a73793cae3ec94e14f",
    "vertex_ledger_sha256": "99f9cf72d473df19a2fc27e04032095607995ea43d874afd08a15e7fc7e240f0",
    "edge_ledger_sha256": "c54aa6fea7971a44e317a041986ca1197671af2cab97825943ebb9d51cadd97e",
}


def square(n: int):
    r = isqrt(n)
    return r * r == n, r


def face_mask(a: int, b: int, c: int):
    mask = 0
    ds = []
    for i, n in enumerate((a*a+b*b, a*a+c*c, b*b+c*c)):
        ok, r = square(n)
        if ok:
            mask |= 1 << i
            ds.append(r)
        else:
            ds.append(0)
    return mask, tuple(ds)


def primitive_face(s: int, x: int, h: int):
    g = gcd(s, x)
    assert h % g == 0
    return (s // g, x // g, h // g)


def edge_details(row):
    a, b, c, _, mask = row
    _, (dab, dac, dbc) = face_mask(a, b, c)
    out = []
    if mask & 1 and mask & 2:
        out.append((a, b, c, primitive_face(a,b,dab), primitive_face(a,c,dac)))
    if mask & 1 and mask & 4:
        out.append((b, a, c, primitive_face(b,a,dab), primitive_face(b,c,dbc)))
    if mask & 2 and mask & 4:
        out.append((c, a, b, primitive_face(c,a,dac), primitive_face(c,b,dbc)))
    return out


def digest_rows(rows):
    data = "".join(",".join(map(str, r)) + "\n" for r in sorted(rows))
    return hashlib.sha256(data.encode("ascii")).hexdigest()


def local_state(g: int, u: int, v: int, p: int):
    G, U, V = g % p == 0, u % p == 0, v % p == 0
    assert not (U and V)
    return (("G" if G else "") + ("U" if U else "") + ("V" if V else "")) or "none"


def read_rows(path: Path):
    rows = []
    with path.open(newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            rows.append(tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")))
    if len(rows) != len(set(rows)):
        raise ArithmeticError("duplicate object rows")
    return set(rows)


def audit(objects):
    counts = Counter()
    vertices = set()
    edges = set()
    degree = defaultdict(int)
    face_info = {}
    g_counts = Counter()
    local_counts = {str(p): Counter() for p in PRIMES}

    for row in sorted(objects):
        a,b,c,d,mask = row
        assert 0 < a < b < c and gcd(a, gcd(b,c)) == 1 and d <= BOUND
        assert a*a+b*b+c*c == d*d
        check,_ = face_mask(a,b,c)
        assert check == mask and mask.bit_count() >= 2
        direction = {3:"a",5:"b",6:"c",7:"triple"}[mask]
        if direction == "triple":
            counts["triple"] += 1
        else:
            counts[direction] += 1
            counts["total"] += 1

        for e,x,y,f1,f2 in edge_details(row):
            edge = tuple(sorted((f1,f2)))
            if edge in edges:
                continue
            edges.add(edge)
            for f in edge:
                vertices.add(f)
                degree[f] += 1
            u, v = gcd(e,x), gcd(e,y)
            assert gcd(u,v) == 1 and e % (u*v) == 0
            g = e // (u*v)
            assert e // u == f1[0] == g*v
            assert e // v == f2[0] == g*u
            assert lcm(f1[0], f2[0]) == e
            g_counts[g] += 1
            for p in PRIMES:
                local_counts[str(p)][local_state(g,u,v,p)] += 1
            for f, partner in ((f1,f2),(f2,f1)):
                info = face_info.setdefault(f, {"first_d": d, "degree": 0, "first_partner": partner})
                info["degree"] += 1
                if (d, partner) < (info["first_d"], info["first_partner"]):
                    info["first_d"], info["first_partner"] = d, partner

    got = {
        "object_count": len(objects),
        "active_face_count": len(vertices),
        "edge_count": len(edges),
        "max_degree": max(degree.values()),
        "counts": {k: counts[k] for k in ("a","b","c","total","triple")},
        "object_key_sha256": digest_rows(r[:4] for r in objects),
        "object_key_mask_sha256": digest_rows(objects),
        "vertex_ledger_sha256": digest_rows(vertices),
        "edge_ledger_sha256": digest_rows(a+b for a,b in edges),
    }
    if got != EXPECTED:
        raise ArithmeticError(f"num3 regression failed: {got}")

    diagnostics = {
        "distinct_g_values": len(g_counts),
        "g_eq_1_edges": g_counts[1],
        "face_degree_histogram": dict(sorted(Counter(degree.values()).items())),
        "first_hit_d_min": min(v["first_d"] for v in face_info.values()),
        "first_hit_d_max": max(v["first_d"] for v in face_info.values()),
        "local_state_counts": {p: dict(sorted(c.items())) for p,c in local_counts.items()},
    }
    return got, diagnostics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("objects", type=Path, help="canonical num3 B=100m CSV")
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()
    base, diagnostics = audit(read_rows(args.objects))
    payload = {
        "base_num3_regression": base,
        "diagnostics": diagnostics,
        "boundary": {
            "finite_diagnostic_only": True,
            "asymptotic_claim": False,
            "theorem_sensitive_fields_recomputed": False,
        },
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.json_out:
        args.json_out.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
