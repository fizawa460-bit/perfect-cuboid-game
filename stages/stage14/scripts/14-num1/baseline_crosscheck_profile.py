#!/usr/bin/env python3
"""Stage14-num1 exact B=2m baseline cross-check and deterministic workload profile.

Two logically different exact generation routes are implemented locally so the
numerical observatory does not depend on row-order or summaries from old stages:

A. hypotenuse -> space-diagonal gluing:
       x^2+y^2=p^2, p^2+z^2=d^2;
B. shared-leg face pairing:
       e^2+x^2=u^2, e^2+y^2=v^2, then test e^2+x^2+y^2=d^2.

Both routes recompute primitiveness, canonical order and all three face-square
flags with integer arithmetic.  Only objects with at least two integral faces
are retained.  The output includes the full small B=2m object ledger and stable
SHA-256 digests.  Runtime/RSS are intentionally left to /usr/bin/time in CI;
the JSON profile contains deterministic workload counters only.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import argparse
import json

DEFAULT_B = 2_000_000
DEFAULT_OUTPUT = Path("stages/stage14/data/14-num1/baseline_crosscheck_profile.json")
EXPECTED_COUNTS = {"a": 142, "b": 134, "c": 80, "total": 356, "triple": 0}
EXPECTED_GRAPH = {"raw_pair_edges": 356, "active_oriented_face_vertices": 490, "max_degree": 9}


def is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def face_mask_and_diagonals(a: int, b: int, c: int) -> tuple[int, tuple[int, int, int]]:
    vals = (a*a+b*b, a*a+c*c, b*b+c*c)
    mask = 0
    ds = []
    for i, value in enumerate(vals):
        r = isqrt(value)
        if r*r == value:
            mask |= 1 << i
            ds.append(r)
        else:
            ds.append(0)
    return mask, (ds[0], ds[1], ds[2])


def generate_pythagorean_indexes(bound: int):
    hyp: dict[int, list[tuple[int, int]]] = defaultdict(list)
    leg: dict[int, list[tuple[int, int]]] = defaultdict(list)
    ntrip = 0
    m = 2
    while m*m + 1 <= bound:
        for n in range(1, m):
            if ((m-n) & 1) == 0 or gcd(m, n) != 1:
                continue
            u = m*m - n*n
            v = 2*m*n
            w = m*m + n*n
            if w > bound:
                continue
            if u > v:
                u, v = v, u
            k = 1
            while k*w <= bound:
                x, y, h = k*u, k*v, k*w
                hyp[h].append((x, y))
                leg[x].append((y, h))
                leg[y].append((x, h))
                ntrip += 1
                k += 1
        m += 1
    common = {
        "integer_pythagorean_triples": ntrip,
        "hypotenuse_index_keys": len(hyp),
        "hypotenuse_index_entries": sum(len(v) for v in hyp.values()),
        "leg_index_keys": len(leg),
        "leg_index_entries": sum(len(v) for v in leg.values()),
    }
    return hyp, leg, common


def route_hypotenuse_glue(bound: int):
    hyp, leg, common = generate_pythagorean_indexes(bound)
    objects: set[tuple[int, int, int, int, int]] = set()
    candidate_glues = 0
    reject_non_strict = 0
    reject_nonprimitive = 0
    face_mask_tests = 0
    reject_less_than_two = 0
    duplicate_two_plus = 0

    for p, face_pairs in hyp.items():
        extensions = leg.get(p)
        if not extensions:
            continue
        for x, y in face_pairs:
            for z, d in extensions:
                candidate_glues += 1
                a, b, c = sorted((x, y, z))
                if not (0 < a < b < c):
                    reject_non_strict += 1
                    continue
                if gcd(a, gcd(b, c)) != 1:
                    reject_nonprimitive += 1
                    continue
                if a*a + b*b + c*c != d*d:
                    raise ArithmeticError("route A space-diagonal identity failure")
                mask, _ = face_mask_and_diagonals(a, b, c)
                face_mask_tests += 1
                if mask.bit_count() < 2:
                    reject_less_than_two += 1
                    continue
                rec = (a, b, c, d, mask)
                if rec in objects:
                    duplicate_two_plus += 1
                objects.add(rec)

    profile = dict(common)
    profile.update({
        "candidate_glues": candidate_glues,
        "reject_non_strict": reject_non_strict,
        "reject_nonprimitive": reject_nonprimitive,
        "face_mask_tests": face_mask_tests,
        "reject_less_than_two_integral_faces": reject_less_than_two,
        "duplicate_two_plus_records_suppressed": duplicate_two_plus,
        "distinct_two_plus_objects": len(objects),
    })
    return objects, profile


def route_shared_leg(bound: int):
    _, leg, common = generate_pythagorean_indexes(bound)
    objects: set[tuple[int, int, int, int, int]] = set()
    candidate_face_pairs = 0
    reject_same_other_leg = 0
    reject_non_strict = 0
    reject_nonprimitive = 0
    reject_space_nonsquare = 0
    reject_space_over_bound = 0
    duplicate_two_plus = 0

    for shared, faces in leg.items():
        L = len(faces)
        for i in range(L):
            x, _ = faces[i]
            for j in range(i+1, L):
                y, _ = faces[j]
                candidate_face_pairs += 1
                if x == y:
                    reject_same_other_leg += 1
                    continue
                a, b, c = sorted((shared, x, y))
                if not (0 < a < b < c):
                    reject_non_strict += 1
                    continue
                if gcd(a, gcd(b, c)) != 1:
                    reject_nonprimitive += 1
                    continue
                d2 = a*a + b*b + c*c
                d = isqrt(d2)
                if d*d != d2:
                    reject_space_nonsquare += 1
                    continue
                if d > bound:
                    reject_space_over_bound += 1
                    continue
                mask, _ = face_mask_and_diagonals(a, b, c)
                if mask.bit_count() < 2:
                    raise ArithmeticError("route B lost its two-face construction")
                rec = (a, b, c, d, mask)
                if rec in objects:
                    duplicate_two_plus += 1
                objects.add(rec)

    profile = dict(common)
    profile.update({
        "candidate_shared_leg_face_pairs": candidate_face_pairs,
        "reject_same_other_leg": reject_same_other_leg,
        "reject_non_strict": reject_non_strict,
        "reject_nonprimitive": reject_nonprimitive,
        "reject_space_nonsquare": reject_space_nonsquare,
        "reject_space_over_bound": reject_space_over_bound,
        "duplicate_two_plus_records_suppressed": duplicate_two_plus,
        "distinct_two_plus_objects": len(objects),
    })
    return objects, profile


def primitive_oriented_face(S: int, X: int, H: int) -> tuple[int, int, int]:
    g = gcd(S, X)
    if H % g:
        raise ArithmeticError("face reduction does not divide hypotenuse")
    return S//g, X//g, H//g


def object_edges(rec: tuple[int, int, int, int, int]):
    a, b, c, _, mask = rec
    _, (dab, dac, dbc) = face_mask_and_diagonals(a, b, c)
    edges = []
    if mask & 1 and mask & 2:
        edges.append(tuple(sorted((primitive_oriented_face(a,b,dab), primitive_oriented_face(a,c,dac)))))
    if mask & 1 and mask & 4:
        edges.append(tuple(sorted((primitive_oriented_face(b,a,dab), primitive_oriented_face(b,c,dbc)))))
    if mask & 2 and mask & 4:
        edges.append(tuple(sorted((primitive_oriented_face(c,a,dac), primitive_oriented_face(c,b,dbc)))))
    return edges


def ledger_digest(rows) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in sorted(rows))
    return sha256(payload.encode("ascii")).hexdigest()


def summarize(objects):
    counts = {"a": 0, "b": 0, "c": 0, "total": 0, "triple": 0}
    ledger = []
    edge_set = set()
    vertices = set()
    degree = defaultdict(int)

    for rec in sorted(objects):
        a, b, c, d, mask = rec
        if not (0 < a < b < c and gcd(a, gcd(b,c)) == 1):
            raise ArithmeticError("canonical/primitiveness failure in retained ledger")
        if a*a+b*b+c*c != d*d:
            raise ArithmeticError("space square failure in retained ledger")
        check_mask, ds = face_mask_and_diagonals(a,b,c)
        if check_mask != mask or mask.bit_count() < 2:
            raise ArithmeticError("mask failure in retained ledger")
        if mask == 0b011:
            direction = "a"; counts["a"] += 1; counts["total"] += 1
        elif mask == 0b101:
            direction = "b"; counts["b"] += 1; counts["total"] += 1
        elif mask == 0b110:
            direction = "c"; counts["c"] += 1; counts["total"] += 1
        elif mask == 0b111:
            direction = "triple"; counts["triple"] += 1
        else:
            raise ArithmeticError("unexpected two-plus mask")

        ledger.append({
            "key": [a,b,c,d],
            "mask": mask,
            "direction": direction,
            "face_diagonals": {"ab": ds[0], "ac": ds[1], "bc": ds[2]},
        })
        for edge in object_edges(rec):
            if edge in edge_set:
                raise ArithmeticError("duplicate raw-pair graph edge")
            edge_set.add(edge)
            u, v = edge
            vertices.add(u); vertices.add(v)
            degree[u] += 1; degree[v] += 1

    graph = {
        "raw_pair_edges": len(edge_set),
        "active_oriented_face_vertices": len(vertices),
        "max_degree": max(degree.values(), default=0),
        "vertex_ledger_sha256": ledger_digest(vertices),
        "edge_ledger_sha256": ledger_digest((u+v) for u,v in edge_set),
    }
    return counts, ledger, graph


def build_report(bound: int):
    if bound != DEFAULT_B:
        raise SystemExit("num1 is a frozen B=2,000,000 baseline stage")

    route_a, prof_a = route_hypotenuse_glue(bound)
    route_b, prof_b = route_shared_leg(bound)
    if route_a != route_b:
        only_a = sorted(route_a-route_b)[:20]
        only_b = sorted(route_b-route_a)[:20]
        raise ArithmeticError(f"route ledger mismatch; onlyA={only_a}; onlyB={only_b}")

    counts, ledger, graph = summarize(route_a)
    if counts != EXPECTED_COUNTS:
        raise ArithmeticError(f"B=2m count lock failed: {counts}")
    for k,v in EXPECTED_GRAPH.items():
        if graph[k] != v:
            raise ArithmeticError(f"B=2m graph lock failed: {k}={graph[k]} expected {v}")

    object_rows = [(r["key"][0],r["key"][1],r["key"][2],r["key"][3],r["mask"]) for r in ledger]
    object_hash = ledger_digest(object_rows)
    key_hash = ledger_digest(tuple(r["key"]) for r in ledger)

    bottleneck_a = max(
        (("candidate_glues", prof_a["candidate_glues"]),
         ("face_mask_tests", prof_a["face_mask_tests"])), key=lambda kv: kv[1]
    )[0]
    bottleneck_b = "candidate_shared_leg_face_pairs"

    return {
        "metadata": {
            "stage": "14-num1",
            "bound": bound,
            "classification": "FINITE_EXACT_CENSUS_BASELINE",
            "routes": [
                "hypotenuse_to_space_diagonal_gluing",
                "shared_leg_two_face_pairing_then_space_square_test",
            ],
        },
        "baseline": {
            "exactly_two": counts,
            "graph": graph,
            "object_count_two_plus": len(ledger),
            "object_key_sha256": key_hash,
            "object_key_mask_sha256": object_hash,
            "ledger": ledger,
        },
        "crosscheck": {
            "route_object_sets_equal": True,
            "canonical_order_rechecked": True,
            "primitiveness_rechecked": True,
            "direction_labels_recomputed_from_face_masks": True,
            "triple_handling_recomputed": True,
            "duplicate_suppression_by_canonical_key_and_mask": True,
            "integer_square_tests_only": True,
        },
        "deterministic_workload_profile": {
            "route_A_hypotenuse_glue": prof_a,
            "route_B_shared_leg": prof_b,
            "dominant_loop_A": bottleneck_a,
            "dominant_loop_B": bottleneck_b,
            "interpretation": "num2 must benchmark optimizations against these deterministic candidate/rejection volumes; wall time and peak RSS are CI-environment measurements, not frozen mathematical data.",
        },
        "decision": {
            "STAGE14_NUM1": "COMPLETE_BASELINE_CROSSCHECK_AND_PROFILE",
            "B2M_MAIN_COUNTS_REPRODUCED": True,
            "B2M_OBJECT_LEDGER_HASH_LOCKED": True,
            "DIRECTION_LABELS_CROSSCHECKED": True,
            "TRIPLE_HANDLING_CROSSCHECKED": True,
            "DUPLICATE_SUPPRESSION_CROSSCHECKED": True,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "ASYMPTOTIC_CLAIM": False,
            "NEXT": "Stage14-num2 enumerator acceleration and incremental architecture",
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bound", type=int, default=DEFAULT_B)
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = ap.parse_args()
    report = build_report(args.bound)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({
        "counts": report["baseline"]["exactly_two"],
        "object_key_mask_sha256": report["baseline"]["object_key_mask_sha256"],
        "graph": report["baseline"]["graph"],
        "route_A": report["deterministic_workload_profile"]["route_A_hypotenuse_glue"],
        "route_B": report["deterministic_workload_profile"]["route_B_shared_leg"],
        "decision": report["decision"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
