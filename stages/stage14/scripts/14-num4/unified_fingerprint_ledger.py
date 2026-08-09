#!/usr/bin/env python3
"""Stage14-num4 unified finite cross-track fingerprint ledger.

This stage is deliberately proof-independent.  It imports the frozen B=100m
Stage14-num3 physical object ledger, validates all num3 hash locks, and attaches
only deterministic cross-track fields whose normalizations are already fixed by
merged stages.  Theorem-sensitive row fields that are not frozen per face stay
null; they are never silently recomputed under a new normalization.
"""
from __future__ import annotations

import argparse
import base64
import bz2
import csv
import io
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

PROVENANCE = {
    "num3": {
        "stage": "14-num3",
        "role": "frozen B=100m physical object and active-face census",
        "path": "stages/stage14/scripts/14-num3/extended_exact_census.py",
        "blob_sha": "abb40f7e6084f8589771cb7b10461d701a478f9a",
        "pr": 215,
        "merge_commit": "18f34e428e464ef57dd7cd0d84aed6ace9e5e1d5",
        "actions_run": 31293771440,
        "actions_head_sha": "a4f1c286e7942335ca97fa91693315dfe64d175a",
    },
    "e9": {
        "stage": "14-e9",
        "role": "exact gcd/lcm inverse and six-state local fingerprints",
        "path": "stages/stage14/scripts/14-e9/gcd_lcm_local_statistics.py",
        "blob_sha": "96fbab0ecbda21c7a1fb84081187df000ccaac86",
        "pr": 166,
        "merge_commit": "01fd93d97b547aff2cd4363651606f9c6449ca24",
    },
    "s1": {
        "stage": "14-s1",
        "role": "elliptic full-2-torsion normalization and sampled rank/Selmer audit",
        "path": "stages/stage14/scripts/14-s1/selmer_interface_audit.py",
        "blob_sha": "4b8ce6c4b56ce5bd02016256e4de0912bfd90304",
        "pr": 169,
        "merge_commit": "c15d71013c8cbf213983002692be3caab5d239a5",
        "row_level_import": "unavailable_in_frozen_compact_json",
    },
    "s3": {
        "stage": "14-s3",
        "role": "canonical-height small-point normalization and sampled audit",
        "path": "stages/stage14/scripts/14-s3/small_point_gate_audit.py",
        "blob_sha": "119c0bb78278c1984a7b72f38b7a55063d7b95d1",
        "pr": 177,
        "merge_commit": "46e5b7cf383d2455ac9b51c35c2452a662beb532",
        "row_level_import": "unavailable_in_frozen_compact_json",
    },
    "kummer_main": {
        "stage": "14-4ag",
        "role": "level-4 modular/Kummer identification and active rank-jump graph interface",
        "pr": 160,
        "merge_commit": "da73b1fe8f0b26c12e812a0800faab85f725f859",
        "row_level_square_class_import": "not_frozen_per_face",
    },
}


def is_square(n: int) -> tuple[bool, int]:
    r = isqrt(n)
    return r * r == n, r


def face_mask(a: int, b: int, c: int):
    mask = 0
    ds = []
    for i, value in enumerate((a*a+b*b, a*a+c*c, b*b+c*c)):
        ok, r = is_square(value)
        if ok:
            mask |= 1 << i
            ds.append(r)
        else:
            ds.append(0)
    return mask, tuple(ds)


def primitive_face(S: int, X: int, H: int):
    g = gcd(S, X)
    assert H % g == 0
    return (S // g, X // g, H // g)


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


def object_edge_details(rec):
    """Return e9-canonical raw pair data with x<y for each square-face pair."""
    a,b,c,_,mask = rec
    _, (dab,dac,dbc) = face_mask(a,b,c)
    out=[]
    if mask & 1 and mask & 2:
        out.append((a,b,c,primitive_face(a,b,dab),primitive_face(a,c,dac)))
    if mask & 1 and mask & 4:
        out.append((b,a,c,primitive_face(b,a,dab),primitive_face(b,c,dbc)))
    if mask & 2 and mask & 4:
        out.append((c,a,b,primitive_face(c,a,dac),primitive_face(c,b,dbc)))
    return out


def digest_rows(rows) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in sorted(rows))
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def canonical_json_sha(obj) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def read_objects(path: Path):
    rows = []
    if path.is_dir():
        parts = sorted(path.glob("part-*.b64"))
        if not parts:
            raise ArithmeticError("empty num4 bzip2/base64 object-source directory")
        encoded = "".join(p.read_text(encoding="ascii").strip() for p in parts)
        raw = bz2.decompress(base64.b64decode(encoded))
        stream = io.StringIO(raw.decode("utf-8"), newline="")
        for row in csv.DictReader(stream):
            rows.append(tuple(int(row[k]) for k in ("a", "b", "c", "d", "mask")))
    else:
        with path.open(newline="", encoding="utf-8") as stream:
            for row in csv.DictReader(stream):
                rows.append(tuple(int(row[k]) for k in ("a", "b", "c", "d", "mask")))
    if len(rows) != len(set(rows)):
        raise ArithmeticError("duplicate object rows in num4 source")
    return set(rows)


def direction_from_mask(mask: int):
    return {0b011: "a", 0b101: "b", 0b110: "c", 0b111: "triple"}[mask]


def local_state(g: int, u: int, v: int, p: int) -> str:
    G = g % p == 0
    U = u % p == 0
    V = v % p == 0
    assert not (U and V)
    return (("G" if G else "") + ("U" if U else "") + ("V" if V else "")) or "none"


def validate_base(objects):
    counts = Counter()
    edges = set()
    vertices = set()
    degree = defaultdict(int)
    for rec in sorted(objects):
        a,b,c,d,mask = rec
        assert 0 < a < b < c and gcd(a, gcd(b,c)) == 1 and d <= BOUND
        assert a*a+b*b+c*c == d*d
        check,_ = face_mask(a,b,c)
        assert check == mask and mask.bit_count() >= 2
        q = direction_from_mask(mask)
        if q == "triple":
            counts["triple"] += 1
        else:
            counts[q] += 1
            counts["total"] += 1
        for edge in object_edges(rec):
            if edge in edges:
                continue
            edges.add(edge)
            u,v = edge
            vertices.add(u); vertices.add(v)
            degree[u] += 1; degree[v] += 1
    got = {
        "object_count": len(objects),
        "active_face_count": len(vertices),
        "edge_count": len(edges),
        "max_degree": max(degree.values(), default=0),
        "counts": {k: counts[k] for k in ("a","b","c","total","triple")},
        "object_key_sha256": digest_rows(r[:4] for r in objects),
        "object_key_mask_sha256": digest_rows(objects),
        "vertex_ledger_sha256": digest_rows(vertices),
        "edge_ledger_sha256": digest_rows(u+v for u,v in edges),
    }
    if got != EXPECTED:
        raise ArithmeticError(f"num3 B=100m regression failed: {got}")
    return got


def build_ledger(objects):
    face_info = {}
    edge_rows = []
    seen_edges = set()
    local_counts = {str(p): Counter() for p in PRIMES}
    blocker_counts = Counter()
    g_counts = Counter()

    def ensure_face(face):
        if face not in face_info:
            S,X,H = face
            face_info[face] = {
                "face_key": list(face),
                "first_physical_hit_d": None,
                "partner_count_le_B": 0,
                "first_hit_object_key": None,
                "first_hit_partner_face": None,
                "first_hit_direction": None,
                "directions_seen": set(),
                "elliptic_specialization": {
                    "a2": X*X-S*S,
                    "a4": -(S*S)*(X*X),
                    "model": "W^2=Z(Z-S^2)(Z+X^2)",
                    "source_stage": "14-s1",
                },
                "certified_rank_interval": None,
                "selmer_2_summary": None,
                "canonical_height_of_actual_first_hit": None,
                "kummer_square_class_fingerprint": None,
                "low_degree_bisection_class": None,
            }
        return face_info[face]

    for rec in sorted(objects):
        a,b,c,d,mask = rec
        direction = direction_from_mask(mask)
        for e,x,y,face_x,face_y in object_edge_details(rec):
            edge = tuple(sorted((face_x, face_y)))
            if edge in seen_edges:
                continue
            seen_edges.add(edge)
            u = gcd(e,x)
            v = gcd(e,y)
            assert gcd(u,v) == 1 and e % (u*v) == 0
            g = e // (u*v)
            S1 = e // u
            S2 = e // v
            assert S1 == face_x[0] and S2 == face_y[0]
            assert S1 == g*v and S2 == g*u and lcm(S1,S2) == e
            states = {str(p): local_state(g,u,v,p) for p in PRIMES}
            f1,f2 = face_x,face_y
            for p,s in states.items():
                local_counts[p][s] += 1
            g_counts[g] += 1
            blocker2 = states["2"] == "G"
            blocker3 = states["3"] == "G"
            blocker_counts["p2_G"] += int(blocker2)
            blocker_counts["p3_G"] += int(blocker3)
            blocker_counts["p2_or_p3_G"] += int(blocker2 or blocker3)
            edge_rows.append({
                "object_key": [a,b,c,d],
                "mask": mask,
                "direction": direction,
                "faces": [list(f1), list(f2)],
                "ambient_pair": {"e": e, "x": x, "y": y},
                "gcd_lcm": {"g": g, "u": u, "v": v, "e": e},
                "local_six_state": states,
                "source_stage": "14-e9",
            })
            for face,partner in ((f1,f2),(f2,f1)):
                r = ensure_face(face)
                r["partner_count_le_B"] += 1
                r["directions_seen"].add(direction)
                candidate = (d, (a,b,c,d), partner)
                current = None if r["first_physical_hit_d"] is None else (
                    r["first_physical_hit_d"], tuple(r["first_hit_object_key"]), tuple(r["first_hit_partner_face"])
                )
                if current is None or candidate < current:
                    r["first_physical_hit_d"] = d
                    r["first_hit_object_key"] = [a,b,c,d]
                    r["first_hit_partner_face"] = list(partner)
                    r["first_hit_direction"] = direction

    face_rows = []
    for face in sorted(face_info):
        r = face_info[face]
        r["directions_seen"] = sorted(r["directions_seen"])
        face_rows.append(r)
    edge_rows.sort(key=lambda r: (r["object_key"], r["faces"]))
    assert len(face_rows) == EXPECTED["active_face_count"]
    assert len(edge_rows) == EXPECTED["edge_count"]
    assert max(r["partner_count_le_B"] for r in face_rows) == EXPECTED["max_degree"]

    null_policy = {
        "certified_rank_interval": "null unless a row-level frozen source artifact exists for this exact face; 14-s1 committed only aggregate/sample digest",
        "selmer_2_summary": "null unless a row-level frozen source artifact exists for this exact face; 14-s1 committed only aggregate/sample digest",
        "canonical_height_of_actual_first_hit": "null because 14-s3 frozen JSON intentionally omits sampled rows; num4 does not rerun theorem-sensitive PARI height calculations",
        "kummer_square_class_fingerprint": "null because no merged per-face frozen square-class ledger was identified",
        "low_degree_bisection_class": "null because no merged per-face frozen bisection-class ledger was identified",
    }
    object_rows = [
        {"object_key": [a,b,c,d], "mask": mask, "direction": direction_from_mask(mask)}
        for a,b,c,d,mask in sorted(objects)
    ]
    ledger = {
        "metadata": {
            "stage": "14-num4",
            "classification": "FINITE_EXACT_DERIVED_CROSS_TRACK_LEDGER",
            "bound": BOUND,
            "schema_version": 1,
            "finite_diagnostic_only": True,
            "asymptotic_claim": False,
        },
        "provenance": PROVENANCE,
        "null_policy": null_policy,
        "objects": object_rows,
        "faces": face_rows,
        "edges": edge_rows,
    }
    diagnostics = {
        "local_state_counts": {p: dict(sorted(c.items())) for p,c in local_counts.items()},
        "rigorous_e9_blocker_counts_on_exact_two_objects": dict(blocker_counts),
        "g_eq_1_edges": g_counts[1],
        "distinct_g_values": len(g_counts),
        "top_g": [[g,n] for g,n in g_counts.most_common(12)],
        "face_degree_histogram": dict(sorted(Counter(r["partner_count_le_B"] for r in face_rows).items())),
        "first_hit_d_min": min(r["first_physical_hit_d"] for r in face_rows),
        "first_hit_d_max": max(r["first_physical_hit_d"] for r in face_rows),
    }
    return ledger, diagnostics


def compact_face_row(r):
    return (
        *r["face_key"],
        r["first_physical_hit_d"],
        r["partner_count_le_B"],
        r["elliptic_specialization"]["a2"],
        r["elliptic_specialization"]["a4"],
    )


def compact_edge_row(r):
    gl = r["gcd_lcm"]
    return tuple(r["object_key"] + r["faces"][0] + r["faces"][1] + [gl["g"],gl["u"],gl["v"],gl["e"]] + [r["local_six_state"][str(p)] for p in PRIMES])


def make_manifest(base, ledger, diagnostics):
    face_rows = ledger["faces"]
    edge_rows = ledger["edges"]
    coverage = {
        "active_faces": len(face_rows),
        "physical_first_hit_d": sum(r["first_physical_hit_d"] is not None for r in face_rows),
        "partner_count": sum(r["partner_count_le_B"] is not None for r in face_rows),
        "elliptic_specialization_coefficients": sum(r["elliptic_specialization"] is not None for r in face_rows),
        "certified_rank_interval": sum(r["certified_rank_interval"] is not None for r in face_rows),
        "selmer_2_summary": sum(r["selmer_2_summary"] is not None for r in face_rows),
        "canonical_height_of_actual_first_hit": sum(r["canonical_height_of_actual_first_hit"] is not None for r in face_rows),
        "kummer_square_class_fingerprint": sum(r["kummer_square_class_fingerprint"] is not None for r in face_rows),
        "low_degree_bisection_class": sum(r["low_degree_bisection_class"] is not None for r in face_rows),
        "gcd_lcm_edge_fingerprints": len(edge_rows),
        "local_six_state_edge_fingerprints": len(edge_rows),
    }
    top_degree = sorted(face_rows, key=lambda r: (-r["partner_count_le_B"], r["face_key"]))[:12]
    return {
        "metadata": ledger["metadata"],
        "base_num3_regression": base,
        "counts": {
            "physical_objects": base["object_count"],
            "active_faces": len(face_rows),
            "raw_pair_edges": len(edge_rows),
            "max_degree": max(r["partner_count_le_B"] for r in face_rows),
        },
        "coverage": coverage,
        "diagnostics": diagnostics,
        "hashes": {
            "unified_full_ledger_sha256": canonical_json_sha(ledger),
            "unified_face_core_sha256": digest_rows(compact_face_row(r) for r in face_rows),
            "unified_edge_fingerprint_sha256": digest_rows(compact_edge_row(r) for r in edge_rows),
            "provenance_catalog_sha256": canonical_json_sha(PROVENANCE),
        },
        "top_degree_face_sample": [
            {
                "face_key": r["face_key"],
                "degree": r["partner_count_le_B"],
                "first_hit_d": r["first_physical_hit_d"],
            } for r in top_degree
        ],
        "null_policy": ledger["null_policy"],
        "decision": {
            "STAGE14_NUM4": "COMPLETE_UNIFIED_FINITE_FINGERPRINT_LEDGER",
            "CANONICAL_OBJECT_KEYS_STABLE": True,
            "SOURCE_PROVENANCE_RECORDED": True,
            "CROSS_TRACK_JOIN_REPRODUCIBLE": True,
            "THEOREM_SENSITIVE_FIELDS_RECOMPUTED": False,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "ASYMPTOTIC_CLAIM": False,
            "NEXT": "Stage14-num5 scaling and anomaly diagnostics",
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--objects", type=Path, required=True)
    ap.add_argument("--ledger-out", type=Path)
    ap.add_argument("--manifest-out", type=Path, required=True)
    args = ap.parse_args()
    objects = read_objects(args.objects)
    base = validate_base(objects)
    ledger, diagnostics = build_ledger(objects)
    manifest = make_manifest(base, ledger, diagnostics)
    if args.ledger_out:
        args.ledger_out.parent.mkdir(parents=True, exist_ok=True)
        args.ledger_out.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"counts": manifest["counts"], "hashes": manifest["hashes"], "decision": manifest["decision"]}, indent=2))


if __name__ == "__main__":
    main()
