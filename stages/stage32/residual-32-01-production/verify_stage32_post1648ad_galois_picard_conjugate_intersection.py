#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGES = HERE.parents[1]
STAGE33_07 = STAGES / "stage33" / "33-07"
sys.path.insert(0, str(STAGE33_07))

from picard_base_rows_retained import load as load_picard  # noqa: E402

CERT = HERE / "post1648ad-galois-picard-conjugate-intersection.json"
NOTE = HERE / "post1648ad-galois-picard-conjugate-intersection-source-note.md"
PARENT = HERE / "post1648z-galois-factor-swap-asymmetric-bidegree-descent-gate.json"
V6 = STAGES / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
PERM = STAGE33_07 / "galois-known-class-permutations.json"
EXPECTED_CERT = "a35e600decfa7bc5bc6e3f4e835f28ed902950314c8eb5152219e494c0b85747"
EXPECTED_NOTE_BLOB = "3d0fb5243d4b2309ca1d80ec4dacecb7e2e98281"
EXPECTED_PARENT = "cc2fc48738e35d62883e7cf94f6b75c8153d066346b72a0b9ce05deaae1eb36b"
EXPECTED_V6 = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_V6_COORDS = "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726"
EXPECTED_RETAINED = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_PERM = "e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_SIGMA_COORDS = "e6f28415018f0e159101537f2cafbaf99280f9ab8c0b4f4566609e2a27313da9"
EXPECTED_SIGMA_PAIRINGS = "84be4569007a5fe55c533855534defc7d89a05c9fadfc231fd2988adc78fc046"
RANK = 64


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def canonical(path: Path, field: str, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get(field)
    body = dict(obj)
    body.pop(field, None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical regression for {path.name}: claimed={claimed} actual={actual}")
    return obj


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def mm(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    BT = list(zip(*B))
    return [[sum(int(a) * int(b) for a, b in zip(row, col)) for col in BT] for row in A]


def mv(A: list[list[int]], x: list[int]) -> list[int]:
    return [sum(int(a) * int(b) for a, b in zip(row, x)) for row in A]


def transpose(A: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*A)]


def dot(x: list[int], G: list[list[int]], y: list[int]) -> int:
    return sum(int(a) * int(b) for a, b in zip(x, mv(G, y)))


def main() -> None:
    cert = canonical(CERT, "canonical_sha256_without_this_field", EXPECTED_CERT)
    parent = canonical(PARENT, "canonical_sha256_without_this_field", EXPECTED_PARENT)
    v6 = canonical(V6, "canonical_sha256_without_this_field", EXPECTED_V6)
    perm = canonical(PERM, "canonical_sha256", EXPECTED_PERM)

    note_blob = git_blob_sha1(NOTE.read_bytes())
    if note_blob != EXPECTED_NOTE_BLOB:
        raise SystemExit(f"source-note blob regression: {note_blob}")

    retained = load_picard()
    if retained["canonical_sha256"] != EXPECTED_RETAINED:
        raise SystemExit("retained Picard bundle canonical regression")
    if retained["upstream_git_blob_sha1"] != EXPECTED_SOURCE_BLOB:
        raise SystemExit("retained upstream Stoll blob regression")
    if perm["source"]["git_blob_sha1"] != EXPECTED_SOURCE_BLOB:
        raise SystemExit("known-class Galois source blob regression")

    x = [int(v) for v in v6["witness"]["picard_coordinates"]]
    if len(x) != RANK or csha(x) != EXPECTED_V6_COORDS:
        raise SystemExit("V6 Picard coordinate regression")
    G = [[int(v) for v in row] for row in retained["picard_gram_64x64"]]
    A = [[int(v) for v in row] for row in retained["picard_action_cc_64x64"]]
    if len(G) != RANK or len(A) != RANK or any(len(row) != RANK for row in G + A):
        raise SystemExit("Picard matrix shape regression")
    I = [[int(i == j) for j in range(RANK)] for i in range(RANK)]
    AT = transpose(A)
    if mm(A, A) != I:
        raise SystemExit("complex conjugation ceased to be involutive")
    if mm(mm(A, G), AT) != G:
        raise SystemExit("complex conjugation ceased to preserve Picard Gram")

    sx = mv(AT, x)
    if mv(AT, sx) != x:
        raise SystemExit("coordinate conjugation ceased to be involutive")
    if csha(sx) != EXPECTED_SIGMA_COORDS:
        raise SystemExit("sigma(D) coordinate hash regression")

    d2 = dot(x, G, x)
    sd2 = dot(sx, G, sx)
    cross = dot(x, G, sx)
    summ = [a + b for a, b in zip(x, sx)]
    diff = [a - b for a, b in zip(x, sx)]
    sumsq = dot(summ, G, summ)
    diffsq = dot(diff, G, diff)
    if (d2, sd2, cross, sumsq, diffsq) != (758, 758, 1288, 4092, -1060):
        raise SystemExit(f"Picard intersection regression: {(d2, sd2, cross, sumsq, diffsq)}")
    if sx == x:
        raise SystemExit("sigma(D) unexpectedly equals D")

    # Independent 140-class Galois transport check at the pairing-vector level.
    pairings = [int(v) for v in v6["witness"]["all140_pairings"]]
    cc = [int(v) for v in perm["cc_permutation_1based"]]
    if len(pairings) != 140 or sorted(cc) != list(range(1, 141)):
        raise SystemExit("140-class payload regression")
    sigma_pairings = [pairings[j - 1] for j in cc]
    if csha(sigma_pairings) != EXPECTED_SIGMA_PAIRINGS:
        raise SystemExit("sigma(D) all-140 pairing transport regression")

    e = cert["exact_picard_computation"]
    if [e["D_self_intersection"], e["sigma_D_self_intersection"], e["D_dot_sigma_D"], e["D_plus_sigma_D_square"], e["D_minus_sigma_D_square"]] != [d2, sd2, cross, sumsq, diffsq]:
        raise SystemExit("certificate arithmetic mismatch")
    if e["sigma_D_picard_coordinates"] != sx or e["sigma_D_picard_coordinates_sha256"] != EXPECTED_SIGMA_COORDS:
        raise SystemExit("certificate sigma(D) mismatch")
    if parent["exact_derivation"]["sigma_D_equals_D"] is not False:
        raise SystemExit("parent asymmetric-bidegree gate regression")

    g = cert["geometric_consequence"]
    if not (g["conditional_on_geometrically_irreducible_carrier_C_in_class_D"] and g["C_intersect_sigma_C_zero_dimensional"]):
        raise SystemExit("geometric conditional contract regression")
    if g["C_intersect_sigma_C_total_geometric_degree_with_multiplicity"] != 1288:
        raise SystemExit("geometric intersection degree regression")
    if g["intersection_support_identified"] or g["intersection_residue_fields_identified"] or g["Q_rational_support_excluded"]:
        raise SystemExit("support/Q-rational firewall regression")

    d = cert["decision"]
    f = cert["firewalls"]
    if d["survivors_current_credit"] != [73, 97, 235] or d["Q602_excluded"] or d["O210_excluded"] or d["O212_plus_advance_allowed"]:
        raise SystemExit("Stage32 current-credit firewall regression")
    if any(f[k] for k in ["scratch_result_promoted_to_MAIN_authority", "scratch_result_promoted_to_current_credit", "intersection_number_promoted_to_support_identification", "intersection_number_promoted_to_Q_rational_point_exclusion", "Q602_excluded", "O210_excluded", "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit", "perfect_cuboid_credit"]):
        raise SystemExit("promotion firewall regression")

    print("STAGE32_POST1648AD_GALOIS_PICARD_CONJUGATE_INTERSECTION=PASS_EXACT")
    print("D_DOT_SIGMA_D=1288")
    print("D_MINUS_SIGMA_D_SQUARE=-1060")
    print("SIGMA_D_PAIRINGS_SHA256=" + EXPECTED_SIGMA_PAIRINGS)
    print("CERTIFICATE_SHA256=" + EXPECTED_CERT)
    print("NEXT=" + cert["next_interface"]["next_exact_route"])


if __name__ == "__main__":
    main()
