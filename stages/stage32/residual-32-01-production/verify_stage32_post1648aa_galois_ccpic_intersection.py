#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
GALOIS_DIR = ROOT / "stages/stage33/33-07"
CERT_PATH = HERE / "post1648aa-galois-ccpic-intersection.json"
V6_PATH = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
INCIDENCE_PATH = HERE / "post1473-x8-marked-exceptional-incidence.json"
BIDEGREE_NOTE = HERE / "post1484-v6-modular-factor-bidegree-source-note.md"
GALOIS_PERM_PATH = GALOIS_DIR / "galois-known-class-permutations.json"
GALOIS_ADAPTER = GALOIS_DIR / "certify_actual_galois_at2_actions.py"
COORD_ADAPTER = GALOIS_DIR / "certify_actual_coordinate_swap_at2_actions.py"
PRIMITIVE_RECOVERY = GALOIS_DIR / "certify_two_coordinate_swap_picard_rows.py"

EXPECTED_CERT = "5d86c63e9e457152b1adeb3f8f4724f91301a23a63d57a0c5db3fba68f7a8339"
EXPECTED_V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_V6_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
EXPECTED_INCIDENCE = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
EXPECTED_INCIDENCE_BLOB = "b3f673aa73324ee731356eec2c0448592fd1e59b"
EXPECTED_BIDEGREE_BLOB = "deeecac5599f3b542b445cd87c2070dae488bc85"
EXPECTED_GALOIS_PERM = "e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"
EXPECTED_GALOIS_PERM_BLOB = "f277939b7f258928f484d2b970d4dfb2ec6133a8"
EXPECTED_GALOIS_ADAPTER_BLOB = "3d17da12a6b612ae3dd7a748d7880394ee2c226d"
EXPECTED_COORD_ADAPTER_BLOB = "b5adaed9249346ed519d9269382161da115c21b1"
EXPECTED_PRIMITIVE_RECOVERY_BLOB = "296e2005f822ae89c1aa085161553fe9ef76d077"
EXPECTED_UPSTREAM_STOLL_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_SELF_SQUARE = 758
EXPECTED_CROSS = 1116
EXPECTED_MINUS_SQUARE = -716
EXPECTED_PLUS_SQUARE = 3748
EXPECTED_D_COORDS_SHA = "63ce55e33cf6d078b60bc71531a87819bce7fe0f74dddd19eeea737006a6d41e"
EXPECTED_SIGMA_COORDS_SHA = "a8a5b1bc5fbe3018c87b591178ab921583be22212cfba11c6d16ccdda6d72850"
EXPECTED_SIGMA_PAIRINGS_SHA = "84be4569007a5fe55c533855534defc7d89a05c9fadfc231fd2988adc78fc046"
EXPECTED_SURVIVORS = [73, 97, 235]


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def check_canonical(doc: dict, expected: str, field: str) -> None:
    body = dict(doc)
    claimed = body.pop(field)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical mismatch for {field}: {claimed}")


def pairings_sha(values: list[int]) -> str:
    return hashlib.sha256(json.dumps(values, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    check_canonical(cert, EXPECTED_CERT, "canonical_sha256_without_this_field")
    if cert["fixed_target"]["surviving_residues_decimal"] != EXPECTED_SURVIVORS:
        raise SystemExit("certificate survivor set moved")

    locked_blobs = {
        V6_PATH: EXPECTED_V6_BLOB,
        INCIDENCE_PATH: EXPECTED_INCIDENCE_BLOB,
        BIDEGREE_NOTE: EXPECTED_BIDEGREE_BLOB,
        GALOIS_PERM_PATH: EXPECTED_GALOIS_PERM_BLOB,
        GALOIS_ADAPTER: EXPECTED_GALOIS_ADAPTER_BLOB,
        COORD_ADAPTER: EXPECTED_COORD_ADAPTER_BLOB,
        PRIMITIVE_RECOVERY: EXPECTED_PRIMITIVE_RECOVERY_BLOB,
    }
    for path, expected in locked_blobs.items():
        if git_blob_sha1(path) != expected:
            raise SystemExit(f"source blob moved: {path}")

    v6 = json.loads(V6_PATH.read_text(encoding="utf-8"))
    check_canonical(v6, EXPECTED_V6_CANONICAL, "canonical_sha256_without_this_field")
    b = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(b) != 140 or int(v6["witness"]["self_intersection"]) != EXPECTED_SELF_SQUARE:
        raise SystemExit("V6 witness moved")

    incidence = json.loads(INCIDENCE_PATH.read_text(encoding="utf-8"))
    check_canonical(incidence, EXPECTED_INCIDENCE, "canonical_sha256_without_this_field")

    perm = json.loads(GALOIS_PERM_PATH.read_text(encoding="utf-8"))
    check_canonical(perm, EXPECTED_GALOIS_PERM, "canonical_sha256")
    if perm["source"]["git_blob_sha1"] != EXPECTED_UPSTREAM_STOLL_BLOB:
        raise SystemExit("upstream Stoll Galois source moved")
    cc_perm = [int(x) for x in perm["cc_permutation_1based"]]
    if len(cc_perm) != 140:
        raise SystemExit("cc permutation length moved")

    # Execute the already-retained compact adapters runner-side.  They may
    # decode the retained payload internally, but this verifier never prints
    # or copies either permanently denylisted retained object.
    sys.path.insert(0, str(GALOIS_DIR))
    with contextlib.redirect_stdout(io.StringIO()):
        g = runpy.run_path(str(GALOIS_ADAPTER))

    if g["EXPECTED_PERM"] != EXPECTED_GALOIS_PERM or g["SOURCE_BLOB"] != EXPECTED_UPSTREAM_STOLL_BLOB:
        raise SystemExit("Galois adapter constants moved")
    pic = g["pic"]
    known = g["known"]
    gram = g["gram"]
    indlist = [int(x) for x in g["indlist"]]
    cc_pic = g["cc_pic"]
    if len(known) != 140 or len(gram) != 64 or len(indlist) != 64:
        raise SystemExit("retained Picard shape moved")

    gram_inv = pic["invert_matrix"](gram)
    basis_pairings = [b[j - 1] for j in indlist]
    d_coords = pic["integral_row"](
        pic["row_times_fraction_matrix"](basis_pairings, gram_inv),
        "fixed V6 class in primitive INDLIST basis",
    )
    replay = [pic["pairing"](d_coords, known[j], gram) for j in range(140)]
    if replay != b:
        raise SystemExit("V6 all-140 pairing replay failed")

    d_square = pic["pairing"](d_coords, d_coords, gram)
    sigma = pic["row_times_matrix"](d_coords, cc_pic)
    if pic["row_times_matrix"](sigma, cc_pic) != d_coords:
        raise SystemExit("cc involution failed on V6 class")
    sigma_square = pic["pairing"](sigma, sigma, gram)
    sigma_pairings = [pic["pairing"](sigma, known[j], gram) for j in range(140)]
    if sigma_pairings != [b[cc_perm[j] - 1] for j in range(140)]:
        raise SystemExit("cc all-140 pairing transport failed")

    cross = pic["pairing"](d_coords, sigma, gram)
    minus = [d_coords[j] - sigma[j] for j in range(64)]
    plus = [d_coords[j] + sigma[j] for j in range(64)]
    minus_square = pic["pairing"](minus, minus, gram)
    plus_square = pic["pairing"](plus, plus, gram)

    observed = {
        "D_square": d_square,
        "sigma_D_square": sigma_square,
        "D_equals_sigma_D": d_coords == sigma,
        "D_dot_sigma_D": cross,
        "D_minus_sigma_D_square": minus_square,
        "D_plus_sigma_D_square": plus_square,
        "D_coordinates_sha256": csha(d_coords),
        "sigma_D_coordinates_sha256": csha(sigma),
        "sigma_all140_pairings_sha256": pairings_sha(sigma_pairings),
    }
    expected = {
        "D_square": EXPECTED_SELF_SQUARE,
        "sigma_D_square": EXPECTED_SELF_SQUARE,
        "D_equals_sigma_D": False,
        "D_dot_sigma_D": EXPECTED_CROSS,
        "D_minus_sigma_D_square": EXPECTED_MINUS_SQUARE,
        "D_plus_sigma_D_square": EXPECTED_PLUS_SQUARE,
        "D_coordinates_sha256": EXPECTED_D_COORDS_SHA,
        "sigma_D_coordinates_sha256": EXPECTED_SIGMA_COORDS_SHA,
        "sigma_all140_pairings_sha256": EXPECTED_SIGMA_PAIRINGS_SHA,
    }
    if observed != expected:
        raise SystemExit(f"exact Picard calculation moved: {observed}")

    rows = incidence["rows"]
    first: dict[int, list[int]] = {}
    second: dict[int, list[int]] = {}
    for row in rows:
        e = int(row["exceptional_label"])
        first.setdefault(int(row["first_factor_boundary_label"]), []).append(e)
        second.setdefault(int(row["second_factor_boundary_label"]), []).append(e)

    def fiber_degrees(pairings: list[int], table: dict[int, list[int]]) -> dict[str, int]:
        return {
            str(label): 2 * pairings[label - 1] + sum(pairings[e - 1] for e in es)
            for label, es in sorted(table.items())
        }

    d_first = fiber_degrees(b, first)
    d_second = fiber_degrees(b, second)
    s_first = fiber_degrees(sigma_pairings, first)
    s_second = fiber_degrees(sigma_pairings, second)
    if set(d_first.values()) != {105} or set(d_second.values()) != {81}:
        raise SystemExit("original V6 bidegree replay failed")
    if set(s_first.values()) != {81} or set(s_second.values()) != {105}:
        raise SystemExit("complex-conjugate bidegree swap failed")

    calc = cert["exact_picard_calculation"]
    for key, value in expected.items():
        if calc[key] != value:
            raise SystemExit(f"certificate exact value moved at {key}")
    if cert["modular_factor_replay"] != {
        "D_bidegree": [105, 81],
        "complex_conjugation_swaps_factor_degrees": True,
        "sigma_D_bidegree": [81, 105],
    }:
        raise SystemExit("certificate bidegree replay moved")

    conditional = cert["conditional_geometric_consequence"]
    if conditional["proper_intersection_length_if_integral"] != EXPECTED_CROSS:
        raise SystemExit("conditional proper-intersection length moved")
    if not conditional["C_and_sigmaC_distinct_if_integral"] or not conditional["Q_rational_points_are_cc_fixed"]:
        raise SystemExit("conditional Galois geometry flags moved")
    if conditional["rational_support_identified"] or conditional["isolated_rational_intersection_point_excluded"]:
        raise SystemExit("rational-support firewall violated")

    decision = cert["decision"]
    if not decision["numerical_intersection_computed_exactly"] or not decision["finite_cc_fixed_support_reduction_obtained_conditionally"]:
        raise SystemExit("positive scratch credit missing")
    for forbidden in (
        "Q602_excluded",
        "O210_excluded",
        "O212_plus_advance_allowed",
        "controller_change_authorized",
        "effective_integral_curve_existence_proved",
        "q602_residue_specific_commutator_obtained",
    ):
        if decision[forbidden]:
            raise SystemExit(f"decision firewall violated: {forbidden}")
    for forbidden in ("receiver_credit", "route_credit", "theorem_credit", "endpoint_credit", "perfect_cuboid_credit"):
        if cert["firewalls"][forbidden]:
            raise SystemExit(f"research-credit firewall violated: {forbidden}")

    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1648AA_EXACT_GALOIS_CCPIC_INTERSECTION_NONEXCLUSION",
        "certificate_canonical_sha256": EXPECTED_CERT,
        "D_square": d_square,
        "sigma_D_square": sigma_square,
        "D_dot_sigma_D": cross,
        "D_minus_sigma_D_square": minus_square,
        "D_plus_sigma_D_square": plus_square,
        "D_bidegree": [105, 81],
        "sigma_D_bidegree": [81, 105],
        "conditional_fixed_support_length": cross,
        "rational_support_identified": False,
        "survivors_current_credit": EXPECTED_SURVIVORS,
        "Q602_excluded": False,
        "O210_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
