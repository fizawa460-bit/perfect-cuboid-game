#!/usr/bin/env python3
"""Stage14-num-alpha2 diagonal-first reference enumerator and overlap audit.

This is intentionally an auditable reference implementation, not the optimized
num-alpha engine.  It reconstructs >=2-face cuboids from collisions among
opposite-edge representations of a fixed space diagonal and compares the
result against the independent ordinary Stage14-num3 enumerator on small
cutoffs plus the frozen Stage14-num1 B=2,000,000 ledger hashes.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from collections import defaultdict
from hashlib import sha256
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
NUM3_SCRIPT = ROOT / "stages/stage14/scripts/14-num3/extended_exact_census.py"
NUM1_MANIFEST = ROOT / "stages/stage14/data/14-num1/baseline_manifest.json"
SMALL_CUTOFFS = (1_000, 5_000, 20_000, 100_000)
FROZEN_BOUND = 2_000_000


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def primitive_pythagorean_triples(bound: int):
    """Generate primitive positive triples with sorted legs and hypotenuse <= bound."""
    m = 2
    while m * m + 1 <= bound:
        for n in range(1, m):
            if ((m - n) & 1) == 0 or gcd(m, n) != 1:
                continue
            u = m * m - n * n
            v = 2 * m * n
            w = m * m + n * n
            if w > bound:
                continue
            if u > v:
                u, v = v, u
            yield u, v, w
        m += 1


def representation_table(bound: int):
    """Map d to all unordered positive nontrivial pairs u<v with u^2+v^2=d^2."""
    reps = defaultdict(set)
    for u, v, w in primitive_pythagorean_triples(bound):
        for k in range(1, bound // w + 1):
            a, b = k * u, k * v
            reps[k * w].add((a, b) if a < b else (b, a))
    return reps


def face_mask(a: int, b: int, c: int):
    mask = 0
    diagonals = []
    for i, value in enumerate((a*a+b*b, a*a+c*c, b*b+c*c)):
        r = isqrt(value)
        if r * r == value:
            mask |= 1 << i
            diagonals.append(r)
        else:
            diagonals.append(0)
    return mask, tuple(diagonals)


def enumerate_alpha(bound: int):
    """Exact alpha1 ordered-role collision enumerator for the frozen >=2-face population."""
    table = representation_table(bound)
    objects = set()
    profile = {
        "diagonals_with_representations": len(table),
        "unordered_representation_count": sum(len(v) for v in table.values()),
        "diagonals_with_two_or_more_representations": 0,
        "ordered_role_pair_tests": 0,
        "positive_square_residual_hits": 0,
        "canonical_generation_hits": 0,
        "deduplicated_objects": 0,
    }

    for d, reps in table.items():
        if len(reps) < 2:
            continue
        profile["diagonals_with_two_or_more_representations"] += 1
        roles = []
        for u, v in sorted(reps):
            roles.append((u, v))
            roles.append((v, u))

        for (a, fa), (b, fb) in combinations(roles, 2):
            profile["ordered_role_pair_tests"] += 1
            if a == b:
                continue
            # Since both are representations of d^2, the two displayed residual
            # expressions agree identically; keeping the check makes the alpha1
            # dictionary executable rather than implicit.
            c2 = d*d - a*a - b*b
            if c2 <= 0 or not is_square(c2):
                continue
            if fa*fa - b*b != c2 or fb*fb - a*a != c2:
                raise ArithmeticError("ordered-role collision identity failed")
            profile["positive_square_residual_hits"] += 1
            c = isqrt(c2)
            aa, bb, cc = sorted((a, b, c))
            if not (0 < aa < bb < cc):
                continue
            if gcd(aa, gcd(bb, cc)) != 1:
                continue
            if aa*aa + bb*bb + cc*cc != d*d:
                raise ArithmeticError("space-diagonal reconstruction failed")
            mask, _ = face_mask(aa, bb, cc)
            if mask.bit_count() < 2:
                raise ArithmeticError("alpha collision produced fewer than two faces")
            profile["canonical_generation_hits"] += 1
            objects.add((aa, bb, cc, d, mask))

    profile["deduplicated_objects"] = len(objects)
    return objects, profile


def primitive_face(shared: int, other: int, hyp: int):
    g = gcd(shared, other)
    if hyp % g:
        raise ArithmeticError("face primitive reduction failed")
    return shared // g, other // g, hyp // g


def object_edges(rec):
    a, b, c, _, mask = rec
    _, (dab, dac, dbc) = face_mask(a, b, c)
    out = []
    if mask & 1 and mask & 2:
        out.append(tuple(sorted((primitive_face(a,b,dab), primitive_face(a,c,dac)))))
    if mask & 1 and mask & 4:
        out.append(tuple(sorted((primitive_face(b,a,dab), primitive_face(b,c,dbc)))))
    if mask & 2 and mask & 4:
        out.append(tuple(sorted((primitive_face(c,a,dac), primitive_face(c,b,dbc)))))
    return out


def digest_rows(rows) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in sorted(rows))
    return sha256(payload.encode("ascii")).hexdigest()


def summarize(objects):
    counts = {"a": 0, "b": 0, "c": 0, "total": 0, "triple": 0}
    edges = set()
    vertices = set()
    degree = defaultdict(int)
    for rec in sorted(objects):
        a, b, c, d, mask = rec
        if mask == 0b011:
            counts["a"] += 1; counts["total"] += 1
        elif mask == 0b101:
            counts["b"] += 1; counts["total"] += 1
        elif mask == 0b110:
            counts["c"] += 1; counts["total"] += 1
        elif mask == 0b111:
            counts["triple"] += 1
        else:
            raise ArithmeticError(f"unexpected mask {mask}")
        for edge in object_edges(rec):
            if edge in edges:
                continue
            edges.add(edge)
            u, v = edge
            vertices.add(u); vertices.add(v)
            degree[u] += 1; degree[v] += 1
    return {
        "counts": counts,
        "distinct_physical_cuboids": len(objects),
        "object_key_sha256": digest_rows(r[:4] for r in objects),
        "object_key_mask_sha256": digest_rows(objects),
        "graph": {
            "raw_pair_edges": len(edges),
            "active_oriented_face_vertices": len(vertices),
            "max_degree": max(degree.values(), default=0),
            "vertex_ledger_sha256": digest_rows(vertices),
            "edge_ledger_sha256": digest_rows((u + v) for u, v in edges),
        },
    }


def load_num3_module():
    spec = importlib.util.spec_from_file_location("stage14_num3", NUM3_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Stage14-num3 reference module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compare_small_cutoffs():
    num3 = load_num3_module()
    rows = []
    for bound in SMALL_CUTOFFS:
        alpha, profile = enumerate_alpha(bound)
        ordinary, _, _ = num3.enumerate_chunk(bound, 0, 1)
        if alpha != ordinary:
            missing = sorted(ordinary - alpha)[:10]
            extra = sorted(alpha - ordinary)[:10]
            raise ArithmeticError(
                f"alpha/main mismatch B={bound}; missing={missing}; extra={extra}"
            )
        rows.append({
            "bound": bound,
            "objects": len(alpha),
            "canonical_object_sets_equal": True,
            "object_mask_sets_equal": True,
            "summary": summarize(alpha),
            "alpha_profile": profile,
        })
    return rows


def compare_frozen_b2m():
    manifest = json.loads(NUM1_MANIFEST.read_text(encoding="utf-8"))
    alpha, profile = enumerate_alpha(FROZEN_BOUND)
    got = summarize(alpha)
    want_hashes = manifest["hashes"]
    hash_checks = {
        "object_key_sha256": got["object_key_sha256"] == want_hashes["object_key_sha256"],
        "object_key_mask_sha256": got["object_key_mask_sha256"] == want_hashes["object_key_mask_sha256"],
        "vertex_ledger_sha256": got["graph"]["vertex_ledger_sha256"] == want_hashes["vertex_ledger_sha256"],
        "edge_ledger_sha256": got["graph"]["edge_ledger_sha256"] == want_hashes["edge_ledger_sha256"],
    }
    counts_equal = got["counts"] == manifest["counts"]
    graph_equal = all(
        got["graph"][k] == manifest["graph"][k]
        for k in ("raw_pair_edges", "active_oriented_face_vertices", "max_degree")
    )
    if not (all(hash_checks.values()) and counts_equal and graph_equal):
        raise ArithmeticError("alpha failed frozen B=2m Stage14-num1 ledger")
    return {
        "bound": FROZEN_BOUND,
        "counts_equal": counts_equal,
        "graph_counts_equal": graph_equal,
        "hash_checks": hash_checks,
        "summary": got,
        "alpha_profile": profile,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    report = {
        "stage": "14-num-alpha2",
        "classification": "FINITE_EXACT_REFERENCE_OVERLAP_AUDIT",
        "small_cutoff_crosschecks": compare_small_cutoffs(),
        "frozen_b2m_crosscheck": compare_frozen_b2m(),
        "decision": {
            "STAGE14_NUM_ALPHA2": "COMPLETE_REFERENCE_IMPLEMENTATION_AND_EXACT_OVERLAP",
            "ALPHA_REFERENCE_EQUALS_EXISTING_NUM_OBJECT_KEYS": True,
            "ALPHA_REFERENCE_EQUALS_EXISTING_FACE_MASKS": True,
            "ALPHA_REFERENCE_EQUALS_EXISTING_RAW_EDGES": True,
            "ALPHA_REFERENCE_EQUALS_EXISTING_ACTIVE_FACES": True,
            "ALPHA_REFERENCE_B2M_FOUR_HASH_LOCKS_MATCH": True,
            "MEANINGFUL_SPEEDUP_PROVED": False,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "NEXT": "Stage14-num-alpha3 sum-of-two-squares generation audit",
        },
    }
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
