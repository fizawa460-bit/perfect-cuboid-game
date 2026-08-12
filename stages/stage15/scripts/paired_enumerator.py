#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Iterable

FACE_BITS = {"ab": 0b001, "ac": 0b010, "bc": 0b100}
FACE_LEGS = {"ab": (0, 1), "ac": (0, 2), "bc": (1, 2)}
MASK_TO_DIRECTION = {0b011: "a", 0b101: "b", 0b110: "c"}
DIRECTION_ORDER = ("a", "b", "c")


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def face_mask(a: int, b: int, c: int) -> int:
    values = (a * a + b * b, a * a + c * c, b * b + c * c)
    return sum((1 << i) for i, value in enumerate(values) if is_square(value))


def pythagorean_certificate(x: int, y: int) -> dict[str, int]:
    """Return the unique scale-times-primitive Euclid certificate for a square face."""
    g = math.gcd(x, y)
    u, v = x // g, y // g
    h2 = u * u + v * v
    h = math.isqrt(h2)
    if h * h != h2:
        raise ArithmeticError(f"non-Pythagorean face: {(x, y)}")
    if u % 2 == 0 and v % 2 == 1:
        even, odd = u, v
    elif v % 2 == 0 and u % 2 == 1:
        even, odd = v, u
    else:
        raise ArithmeticError(f"primitive parity failure: {(x, y, u, v)}")
    m2 = (h + odd) // 2
    n2 = (h - odd) // 2
    m, n = math.isqrt(m2), math.isqrt(n2)
    if not (m * m == m2 and n * n == n2 and m > n > 0):
        raise ArithmeticError(f"Euclid recovery failure: {(x, y)}")
    if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
        raise ArithmeticError(f"primitive Euclid failure: {(m, n)}")
    if {m * m - n * n, 2 * m * n} != {u, v}:
        raise ArithmeticError(f"Euclid reconstruction failure: {(x, y, m, n)}")
    return {"m": m, "n": n, "scale": g, "hypotenuse": g * h}


def generate_leg_index(bound: int) -> tuple[dict[int, list[int]], int]:
    """All integer Pythagorean triangles with hypotenuse <= bound, indexed by either leg."""
    by_leg: dict[int, list[int]] = defaultdict(list)
    triangle_count = 0
    for m in range(2, math.isqrt(bound) + 2):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            u0, v0, h0 = m * m - n * n, 2 * m * n, m * m + n * n
            if h0 > bound:
                continue
            for k in range(1, bound // h0 + 1):
                u, v = k * u0, k * v0
                by_leg[u].append(v)
                by_leg[v].append(u)
                triangle_count += 1
    for shared, entries in by_leg.items():
        entries.sort()
        if len(entries) != len(set(entries)):
            raise ArithmeticError(f"duplicate triangle record at shared leg {shared}")
    return by_leg, triangle_count


def integral_face_names(mask: int) -> list[str]:
    return [name for name, bit in FACE_BITS.items() if mask & bit]


def shared_edge_for_exact_two(a: int, b: int, c: int, mask: int) -> tuple[str, int]:
    direction = MASK_TO_DIRECTION[mask]
    return direction, {"a": a, "b": b, "c": c}[direction]


def third_face_data(a: int, b: int, c: int, mask: int) -> dict[str, int | str]:
    missing = [name for name, bit in FACE_BITS.items() if not (mask & bit)]
    if len(missing) != 1:
        raise ArithmeticError(f"expected one missing face, mask={mask:03b}")
    name = missing[0]
    i, j = FACE_LEGS[name]
    edges = (a, b, c)
    s = edges[i] * edges[i] + edges[j] * edges[j]
    q = math.isqrt(s)
    if q * q == s:
        raise ArithmeticError("third face unexpectedly square")
    return {
        "third_face": name,
        "third_face_sum": s,
        "third_face_floor_root": q,
        "third_face_defect_lower": s - q * q,
        "third_face_defect_upper": (q + 1) * (q + 1) - s,
    }


def build_exact_two_row(a: int, b: int, c: int, mask: int, r2: int, source_count: int) -> dict:
    direction, shared_edge = shared_edge_for_exact_two(a, b, c, mask)
    faces = integral_face_names(mask)
    certs = {}
    edges = (a, b, c)
    for name in faces:
        i, j = FACE_LEGS[name]
        certs[name] = pythagorean_certificate(edges[i], edges[j])
    d = math.isqrt(r2)
    space_integral = d * d == r2
    row = {
        "a": a,
        "b": b,
        "c": c,
        "R2": r2,
        "space_integral": space_integral,
        "d": d if space_integral else None,
        "face_mask": f"{mask:03b}",
        "integral_faces": ",".join(faces),
        "direction": direction,
        "shared_edge": shared_edge,
        "primitive": True,
        "canonical": True,
        "glue_source_count": source_count,
        "face_certificates": certs,
    }
    row.update(third_face_data(a, b, c, mask))
    return row


def enumerate_paired(bound: int, materialize_rows: bool = True) -> tuple[list[dict], list[dict], dict]:
    """Enumerate B_2 and B_3 exactly under 0<a<b<c, gcd=1, R<=bound."""
    if bound < 1:
        raise ValueError("bound must be positive")
    by_leg, triangle_count = generate_leg_index(bound)
    objects: dict[tuple[int, int, int], dict[str, int]] = {}
    glued_pairs_inside_r = 0

    for shared, entries in by_leg.items():
        for i, x in enumerate(entries):
            for y in entries[i + 1 :]:
                if x == y:
                    continue
                r2 = shared * shared + x * x + y * y
                if r2 > bound * bound:
                    continue
                glued_pairs_inside_r += 1
                a, b, c = sorted((shared, x, y))
                if not (a < b < c):
                    continue
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                mask = face_mask(a, b, c)
                if mask.bit_count() < 2:
                    raise ArithmeticError(f"glued pair lost a square face: {(a, b, c, mask)}")
                if mask.bit_count() == 2:
                    _, expected_shared = shared_edge_for_exact_two(a, b, c, mask)
                    if shared != expected_shared:
                        raise ArithmeticError(
                            f"exact-two object glued through wrong shared edge: {(a, b, c, shared, mask)}"
                        )
                key = (a, b, c)
                previous = objects.get(key)
                if previous is None:
                    objects[key] = {"mask": mask, "R2": r2, "source_count": 1}
                else:
                    if previous["mask"] != mask or previous["R2"] != r2:
                        raise ArithmeticError(f"inconsistent duplicate provenance: {key}")
                    previous["source_count"] += 1

    exact_two: list[dict] = []
    triples: list[dict] = []
    m2_dir = {direction: 0 for direction in DIRECTION_ORDER}
    n2_dir = {direction: 0 for direction in DIRECTION_ORDER}
    m2_total = 0
    m3_total = 0
    n3 = 0
    exact2_mult_ok = True
    triple_mult_ok = True

    for (a, b, c), info in sorted(objects.items()):
        mask, r2, source_count = info["mask"], info["R2"], info["source_count"]
        d = math.isqrt(r2)
        space_integral = d * d == r2
        if mask.bit_count() == 2:
            exact2_mult_ok = exact2_mult_ok and source_count == 1
            if source_count != 1:
                raise ArithmeticError(f"exact-two multiplicity is not one: {(a, b, c, source_count)}")
            direction = MASK_TO_DIRECTION[mask]
            m2_total += 1
            m2_dir[direction] += 1
            if space_integral:
                n2_dir[direction] += 1
            if materialize_rows:
                exact_two.append(build_exact_two_row(a, b, c, mask, r2, source_count))
        elif mask == 0b111:
            triple_mult_ok = triple_mult_ok and source_count == 3
            if source_count != 3:
                raise ArithmeticError(f"triple multiplicity is not three: {(a, b, c, source_count)}")
            m3_total += 1
            if space_integral:
                n3 += 1
            if materialize_rows:
                triples.append(
                    {
                        "a": a,
                        "b": b,
                        "c": c,
                        "R2": r2,
                        "space_integral": space_integral,
                        "d": d if space_integral else None,
                        "face_mask": "111",
                        "primitive": True,
                        "canonical": True,
                        "glue_source_count": source_count,
                    }
                )
        else:
            raise ArithmeticError(f"unexpected mask after gluing: {(a, b, c, mask)}")

    summary = {
        "stage": "Stage15-1",
        "classification": "EXACT_PAIRED_ENUMERATOR",
        "bound_R": bound,
        "M2_total": m2_total,
        "M2_direction_a_b_c": [m2_dir[d] for d in DIRECTION_ORDER],
        "M3_total": m3_total,
        "N2_total": sum(n2_dir.values()),
        "N2_direction_a_b_c": [n2_dir[d] for d in DIRECTION_ORDER],
        "N3_total": n3,
        "diagnostics": {
            "integer_pythagorean_triangles_hyp_le_B": triangle_count,
            "glued_pairs_inside_R_before_physical_filters": glued_pairs_inside_r,
            "distinct_primitive_canonical_objects_with_at_least_two_faces": len(objects),
            "exact_two_glue_multiplicity_one": exact2_mult_ok,
            "triple_glue_multiplicity_three": triple_mult_ok,
        },
        "claims": {
            "enumeration_is_exact": True,
            "numerical_asymptotic_claim": False,
            "stage15_3_comparison_inference": False,
        },
    }
    return exact_two, triples, summary


TSV_FIELDS = [
    "a", "b", "c", "R2", "space_integral", "d", "face_mask", "integral_faces",
    "direction", "shared_edge", "third_face", "third_face_sum", "third_face_floor_root",
    "third_face_defect_lower", "third_face_defect_upper", "primitive", "canonical",
    "glue_source_count", "face_certificates",
]


def write_tsv(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TSV_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            out = dict(row)
            out["space_integral"] = str(bool(out["space_integral"])).lower()
            out["primitive"] = str(bool(out["primitive"])).lower()
            out["canonical"] = str(bool(out["canonical"])).lower()
            out["d"] = "" if out["d"] is None else out["d"]
            out["face_certificates"] = json.dumps(out["face_certificates"], sort_keys=True, separators=(",", ":"))
            writer.writerow({field: out[field] for field in TSV_FIELDS})


def main() -> None:
    parser = argparse.ArgumentParser(description="Exact Stage15 paired B2/A2 enumerator")
    parser.add_argument("--bound", type=int, required=True, help="common geometric cutoff R<=B")
    parser.add_argument("--tsv", type=Path, help="write exact-two B2 rows as TSV")
    parser.add_argument("--triples-json", type=Path, help="write B3 rows separately as JSON")
    parser.add_argument("--summary-json", type=Path, help="write summary JSON")
    args = parser.parse_args()

    materialize = bool(args.tsv or args.triples_json)
    exact_two, triples, summary = enumerate_paired(args.bound, materialize_rows=materialize)
    if args.tsv:
        write_tsv(args.tsv, exact_two)
    if args.triples_json:
        args.triples_json.parent.mkdir(parents=True, exist_ok=True)
        args.triples_json.write_text(json.dumps(triples, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.summary_json:
        args.summary_json.parent.mkdir(parents=True, exist_ok=True)
        args.summary_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
