#!/usr/bin/env python3
"""Stage14-num3 memory-bounded exact census beyond B=2,000,000.

Finite numerical observatory only; this script makes no asymptotic claim.

Architecture:
* partition the shared face hypotenuse p by p mod C;
* retain only that chunk's Pythagorean faces in memory;
* stream outer Pythagorean triples p^2+z^2=d^2;
* apply exact primitive and second-face gates;
* canonical-union deterministic chunk ledgers;
* recheck the frozen B=2m num1 hashes and every frozen num3 milestone.
"""
from __future__ import annotations

import argparse
import json
import time
from collections import defaultdict
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
NUM1_MANIFEST = ROOT / "stages/stage14/data/14-num1/baseline_manifest.json"
NUM3_MANIFEST = ROOT / "stages/stage14/data/14-num3/census_manifest.json"
DEFAULT_BOUND = 5_000_000
DEFAULT_CHUNKS = 8
REGRESSION_BOUND = 2_000_000
MILESTONE_CUTS = (2_000_000, 5_000_000, 10_000_000, 20_000_000, 50_000_000)


def is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def primitive_pythagorean_triples(bound: int):
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


def build_hypotenuse_chunk(bound: int, chunk_index: int, chunk_count: int):
    hyp = defaultdict(list)
    primitive_count = scaled_seen = retained = 0
    t0 = time.perf_counter()
    for u, v, w in primitive_pythagorean_triples(bound):
        primitive_count += 1
        max_k = bound // w
        scaled_seen += max_k
        for k in range(1, max_k + 1):
            p = k * w
            if p % chunk_count == chunk_index:
                hyp[p].append((k * u, k * v, k))
                retained += 1
    return hyp, {
        "primitive_pythagorean_triples": primitive_count,
        "all_scaled_triples_seen": scaled_seen,
        "chunk_hypotenuse_keys": len(hyp),
        "chunk_face_entries": retained,
        "build_seconds": time.perf_counter() - t0,
    }


def face_mask(a: int, b: int, c: int):
    mask = 0
    ds = []
    for i, value in enumerate((a*a+b*b, a*a+c*c, b*b+c*c)):
        r = isqrt(value)
        if r * r == value:
            mask |= 1 << i
            ds.append(r)
        else:
            ds.append(0)
    return mask, tuple(ds)


def primitive_face(S: int, X: int, H: int):
    g = gcd(S, X)
    if H % g:
        raise ArithmeticError("face reduction does not divide hypotenuse")
    return S // g, X // g, H // g


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


def enumerate_chunk(bound: int, chunk_index: int, chunk_count: int):
    hyp, index_profile = build_hypotenuse_chunk(bound, chunk_index, chunk_count)
    objects = set()
    profile = {
        "outer_primitive_triples": 0,
        "outer_scaled_triples": 0,
        "outer_leg_events_in_chunk": 0,
        "candidate_glues": 0,
        "early_nonprimitive_rejects": 0,
        "second_face_square_tests": 0,
        "second_face_gate_rejects": 0,
        "post_gate_sorts": 0,
        "strict_order_rejects": 0,
        "full_face_mask_validations": 0,
        "retained_generation_records": 0,
        "duplicates_suppressed_within_chunk": 0,
    }
    t0 = time.perf_counter()
    for u, v, w in primitive_pythagorean_triples(bound):
        profile["outer_primitive_triples"] += 1
        for k_outer in range(1, bound // w + 1):
            l1 = k_outer * u
            l2 = k_outer * v
            d = k_outer * w
            profile["outer_scaled_triples"] += 1
            for p, z in ((l1, l2), (l2, l1)):
                if p % chunk_count != chunk_index:
                    continue
                profile["outer_leg_events_in_chunk"] += 1
                faces = hyp.get(p)
                if not faces:
                    continue
                for x, y, face_scale in faces:
                    profile["candidate_glues"] += 1
                    if gcd(face_scale, z) != 1:
                        profile["early_nonprimitive_rejects"] += 1
                        continue
                    profile["second_face_square_tests"] += 1
                    xz = is_square(x*x + z*z)
                    yz = False
                    if not xz:
                        profile["second_face_square_tests"] += 1
                        yz = is_square(y*y + z*z)
                    if not xz and not yz:
                        profile["second_face_gate_rejects"] += 1
                        continue
                    profile["post_gate_sorts"] += 1
                    a, b, c = sorted((x, y, z))
                    if not (0 < a < b < c):
                        profile["strict_order_rejects"] += 1
                        continue
                    if gcd(a, gcd(b, c)) != 1:
                        raise ArithmeticError("early primitive gate disagrees after canonicalization")
                    if a*a + b*b + c*c != d*d:
                        raise ArithmeticError("space diagonal identity failure")
                    mask, _ = face_mask(a, b, c)
                    profile["full_face_mask_validations"] += 1
                    if mask.bit_count() < 2:
                        raise ArithmeticError("second-face gate disagrees with face-mask validation")
                    rec = (a, b, c, d, mask)
                    profile["retained_generation_records"] += 1
                    if rec in objects:
                        profile["duplicates_suppressed_within_chunk"] += 1
                    objects.add(rec)
    profile["kernel_seconds"] = time.perf_counter() - t0
    return objects, index_profile, profile


def summarize(objects):
    counts = {"a":0, "b":0, "c":0, "total":0, "triple":0}
    edges = set(); vertices = set(); degree = defaultdict(int)
    for rec in sorted(objects):
        a, b, c, d, mask = rec
        if not (0 < a < b < c and gcd(a, gcd(b, c)) == 1):
            raise ArithmeticError("canonical primitive check failed")
        if a*a + b*b + c*c != d*d:
            raise ArithmeticError("space-square check failed")
        check, _ = face_mask(a, b, c)
        if check != mask or mask.bit_count() < 2:
            raise ArithmeticError("face-mask check failed")
        if mask == 0b011:
            counts["a"] += 1; counts["total"] += 1
        elif mask == 0b101:
            counts["b"] += 1; counts["total"] += 1
        elif mask == 0b110:
            counts["c"] += 1; counts["total"] += 1
        elif mask == 0b111:
            counts["triple"] += 1
        else:
            raise ArithmeticError(f"unexpected retained mask {mask}")
        for edge in object_edges(rec):
            if edge in edges:
                continue
            edges.add(edge)
            u, v = edge
            vertices.add(u); vertices.add(v)
            degree[u] += 1; degree[v] += 1
    endpoint_incidences = 2 * len(edges)
    return {
        "counts": counts,
        "distinct_physical_cuboids": len(objects),
        "object_key_sha256": digest_rows(r[:4] for r in objects),
        "object_key_mask_sha256": digest_rows(objects),
        "graph": {
            "raw_pair_edges": len(edges),
            "active_oriented_face_vertices": len(vertices),
            "max_degree": max(degree.values(), default=0),
            "vertex_first_hit_events": len(vertices),
            "vertex_repeat_incidence_events": endpoint_incidences - len(vertices),
            "vertex_ledger_sha256": digest_rows(vertices),
            "edge_ledger_sha256": digest_rows((u+v) for u,v in edges),
        },
    }


def load_num1():
    return json.loads(NUM1_MANIFEST.read_text(encoding="utf-8"))


def load_num3():
    if not NUM3_MANIFEST.exists():
        return {"completed_cutoffs": {}}
    return json.loads(NUM3_MANIFEST.read_text(encoding="utf-8"))


def chunk_report(bound: int, chunk_index: int, chunk_count: int):
    objects, index_profile, kernel_profile = enumerate_chunk(bound, chunk_index, chunk_count)
    return {
        "metadata": {
            "stage": "14-num3",
            "classification": "FINITE_EXACT_CENSUS_CHUNK",
            "bound": bound,
            "chunk_index": chunk_index,
            "chunk_count": chunk_count,
            "partition": "shared face hypotenuse p modulo chunk_count",
        },
        "objects": [list(r) for r in sorted(objects)],
        "index_profile": index_profile,
        "kernel_profile": kernel_profile,
        "decision": {
            "FINITE_DIAGNOSTIC_ONLY": True,
            "ASYMPTOTIC_CLAIM": False,
            "SQRT_B_ASYMPTOTIC_CLAIM": False,
        },
    }


def verify_num1(objects):
    num1 = load_num1()
    baseline = summarize({r for r in objects if r[3] <= REGRESSION_BOUND})
    h = num1["hashes"]
    hashes_ok = (
        baseline["object_key_sha256"] == h["object_key_sha256"] and
        baseline["object_key_mask_sha256"] == h["object_key_mask_sha256"] and
        baseline["graph"]["vertex_ledger_sha256"] == h["vertex_ledger_sha256"] and
        baseline["graph"]["edge_ledger_sha256"] == h["edge_ledger_sha256"]
    )
    counts_ok = baseline["counts"] == num1["counts"]
    graph_ok = all(baseline["graph"][k] == num1["graph"][k]
                   for k in ("raw_pair_edges","active_oriented_face_vertices","max_degree"))
    if not (hashes_ok and counts_ok and graph_ok):
        raise ArithmeticError("num3 kernel failed num1 B=2m regression")
    return {
        "bound": REGRESSION_BOUND,
        "all_four_sha256_match": hashes_ok,
        "counts_match": counts_ok,
        "graph_match": graph_ok,
        "hashes": h,
    }


def verify_frozen_num3_milestones(checkpoints):
    manifest = load_num3()
    verified = []
    for key, want in manifest.get("completed_cutoffs", {}).items():
        if key not in checkpoints:
            continue
        got = checkpoints[key]
        if got["counts"] != want["counts"]:
            raise ArithmeticError(f"num3 frozen count mismatch at B={key}")
        if got["distinct_physical_cuboids"] != want["distinct_physical_cuboids"]:
            raise ArithmeticError(f"num3 object-count mismatch at B={key}")
        if got["object_key_sha256"] != want["object_key_sha256"]:
            raise ArithmeticError(f"num3 object-key hash mismatch at B={key}")
        if got["object_key_mask_sha256"] != want["object_key_mask_sha256"]:
            raise ArithmeticError(f"num3 object+mask hash mismatch at B={key}")
        if got["graph"] != want["graph"]:
            raise ArithmeticError(f"num3 graph mismatch at B={key}")
        verified.append(int(key))
    return sorted(verified)


def merge_reports(bound: int, paths):
    reports = [json.loads(Path(p).read_text(encoding="utf-8")) for p in paths]
    if not reports:
        raise SystemExit("no chunk reports found")
    chunk_count = reports[0]["metadata"]["chunk_count"]
    seen_chunks = sorted(r["metadata"]["chunk_index"] for r in reports)
    if seen_chunks != list(range(chunk_count)):
        raise ArithmeticError(f"missing/duplicate chunks: {seen_chunks}")
    if any(r["metadata"]["bound"] != bound for r in reports):
        raise ArithmeticError("chunk bound mismatch")

    objects = set(); pre_union_records = 0
    for r in reports:
        rows = {tuple(row) for row in r["objects"]}
        pre_union_records += len(rows)
        objects.update(rows)

    num1_regression = verify_num1(objects)
    checkpoints = {
        str(B): summarize({r for r in objects if r[3] <= B})
        for B in MILESTONE_CUTS if B <= bound
    }
    verified_num3 = verify_frozen_num3_milestones(checkpoints)
    full = summarize(objects)
    triples = [list(r) for r in sorted(objects) if r[4] == 0b111]
    emergency = bool(triples)

    ordered = sorted(reports, key=lambda x: x["metadata"]["chunk_index"])
    combined_profile = {
        "chunk_count": chunk_count,
        "pre_union_distinct_chunk_records": pre_union_records,
        "post_union_distinct_objects": len(objects),
        "sum_chunk_face_entries": sum(r["index_profile"]["chunk_face_entries"] for r in reports),
        "sum_candidate_glues": sum(r["kernel_profile"]["candidate_glues"] for r in reports),
        "sum_early_nonprimitive_rejects": sum(r["kernel_profile"]["early_nonprimitive_rejects"] for r in reports),
        "sum_second_face_square_tests": sum(r["kernel_profile"]["second_face_square_tests"] for r in reports),
        "sum_full_face_mask_validations": sum(r["kernel_profile"]["full_face_mask_validations"] for r in reports),
        "max_chunk_face_entries": max(r["index_profile"]["chunk_face_entries"] for r in reports),
        "chunk_build_seconds": [r["index_profile"]["build_seconds"] for r in ordered],
        "chunk_kernel_seconds": [r["kernel_profile"]["kernel_seconds"] for r in ordered],
    }
    return {
        "metadata": {
            "stage": "14-num3",
            "classification": "FINITE_EXACT_EXTENDED_CENSUS",
            "bound": bound,
            "chunk_count": chunk_count,
            "method": "memory-bounded hypotenuse-residue chunks + streamed outer Pythagorean triples",
        },
        "num1_regression": num1_regression,
        "frozen_num3_milestone_regression": {
            "verified_cutoffs": verified_num3,
            "all_available_frozen_milestones_match": True,
        },
        "cutoff_summaries": checkpoints,
        "extended_census": full,
        "resource_workload": combined_profile,
        "perfect_cuboid_emergency": {
            "triggered": emergency,
            "unverified_candidates": triples,
            "second_generation_route_reproduction_required_before_verified_candidate_report": True,
        },
        "decision": {
            "STAGE14_NUM3": "COMPLETE_EXTENDED_EXACT_CENSUS" if not emergency else "PAUSED_PERFECT_CUBOID_EMERGENCY_PROTOCOL",
            "EXTENDED_BEYOND_B2M": bound > REGRESSION_BOUND,
            "B2M_BASELINE_LEDGER_UNCHANGED": True,
            "FROZEN_NUM3_MILESTONES_UNCHANGED": True,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "ASYMPTOTIC_CLAIM": False,
            "SQRT_B_ASYMPTOTIC_CLAIM": False,
            "PERFECT_CUBOID_EXISTENCE_CLAIM": False,
            "PERFECT_CUBOID_NONEXISTENCE_CLAIM": False,
            "NEXT": "Stage14-num4 unified cross-track fingerprint ledger" if not emergency else "independent perfect-cuboid candidate reproduction",
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bound", type=int, default=DEFAULT_BOUND)
    ap.add_argument("--chunk-count", type=int, default=DEFAULT_CHUNKS)
    ap.add_argument("--chunk-index", type=int)
    ap.add_argument("--merge-dir", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.chunk_index is not None and args.merge_dir is not None:
        raise SystemExit("choose chunk mode or merge mode")
    if args.chunk_index is not None:
        if not (0 <= args.chunk_index < args.chunk_count):
            raise SystemExit("invalid chunk index")
        report = chunk_report(args.bound, args.chunk_index, args.chunk_count)
    elif args.merge_dir is not None:
        report = merge_reports(args.bound, sorted(args.merge_dir.rglob("chunk-*.json")))
    else:
        raise SystemExit("provide --chunk-index or --merge-dir")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.chunk_index is not None:
        visible = {
            "metadata": report["metadata"],
            "object_count": len(report["objects"]),
            "index_profile": report["index_profile"],
            "kernel_profile": report["kernel_profile"],
        }
    else:
        visible = {
            "metadata": report["metadata"],
            "num1_regression": report["num1_regression"],
            "frozen_num3_milestone_regression": report["frozen_num3_milestone_regression"],
            "cutoff_summaries": report["cutoff_summaries"],
            "extended_census": report["extended_census"],
            "resource_workload": report["resource_workload"],
            "perfect_cuboid_emergency": report["perfect_cuboid_emergency"],
            "decision": report["decision"],
        }
    print(json.dumps(visible, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
