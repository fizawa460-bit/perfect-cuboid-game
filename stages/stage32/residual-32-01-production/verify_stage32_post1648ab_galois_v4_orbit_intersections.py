#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
GALOIS_DIR = ROOT / "stages/stage33/33-07"
GALOIS_SCRIPT = GALOIS_DIR / "certify_actual_galois_at2_actions.py"
V6_PATH = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
INCIDENCE_PATH = HERE / "post1473-x8-marked-exceptional-incidence.json"
AA_PATH = HERE / "post1648aa-galois-ccpic-intersection.json"
CERT_PATH = HERE / "post1648ab-galois-v4-orbit-intersections.json"

EXPECTED_CERT = "7b36625f61fd1c2d7868f2f5b5a7deaeb6dc50835cba77b0189e2b676e0cbcf1"
EXPECTED_AA = "5d86c63e9e457152b1adeb3f8f4724f91301a23a63d57a0c5db3fba68f7a8339"
EXPECTED_GALOIS_BLOB = "3d17da12a6b612ae3dd7a748d7880394ee2c226d"
EXPECTED_V6_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
EXPECTED_V6 = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_INCIDENCE = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
EXPECTED_PERM = "e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"
EXPECTED_STOLL_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def verify_without(doc: dict, expected: str) -> None:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {claimed}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    verify_without(cert, EXPECTED_CERT)
    aa = json.loads(AA_PATH.read_text(encoding="utf-8"))
    verify_without(aa, EXPECTED_AA)
    v6 = json.loads(V6_PATH.read_text(encoding="utf-8"))
    verify_without(v6, EXPECTED_V6)
    incidence = json.loads(INCIDENCE_PATH.read_text(encoding="utf-8"))
    verify_without(incidence, EXPECTED_INCIDENCE)
    if git_blob_sha1(GALOIS_SCRIPT) != EXPECTED_GALOIS_BLOB:
        raise SystemExit("Galois adapter blob moved")
    if git_blob_sha1(V6_PATH) != EXPECTED_V6_BLOB:
        raise SystemExit("V6 blob moved")

    b = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(b) != 140 or int(v6["witness"]["self_intersection"]) != 758:
        raise SystemExit("V6 witness shape moved")

    sys.path.insert(0, str(GALOIS_DIR))
    g = runpy.run_path(str(GALOIS_SCRIPT))
    if g["EXPECTED_PERM"] != EXPECTED_PERM or g["SOURCE_BLOB"] != EXPECTED_STOLL_BLOB:
        raise SystemExit("retained Galois source lock moved")
    pic = g["pic"]
    known = g["known"]
    gram = g["gram"]
    indlist = [int(x) for x in g["indlist"]]
    cc = g["cc_pic"]
    ct = g["ct_pic"]

    d = pic["integral_row"](
        pic["row_times_fraction_matrix"](
            [b[j - 1] for j in indlist], pic["invert_matrix"](gram)
        ),
        "V6 D",
    )
    dcc = pic["row_times_matrix"](d, cc)
    dct = pic["row_times_matrix"](d, ct)
    dcct = pic["row_times_matrix"](dcc, ct)
    if pic["row_times_matrix"](dct, cc) != dcct:
        raise SystemExit("cc/ct commute replay failed")

    orbit = {"D": d, "ccD": dcc, "ctD": dct, "ccctD": dcct}
    if len({tuple(x) for x in orbit.values()}) != 4:
        raise SystemExit("Galois orbit size is not four")
    if any(pic["pairing"](x, x, gram) != 758 for x in orbit.values()):
        raise SystemExit("Galois orbit square preservation failed")

    expected_pairs = {
        "D.ccD": 1116,
        "D.ctD": 1026,
        "D.ccctD": 1348,
        "ccD.ctD": 1348,
        "ccD.ccctD": 1026,
        "ctD.ccctD": 1116,
    }
    for key, want in expected_pairs.items():
        a, bname = key.split(".")
        got = pic["pairing"](orbit[a], orbit[bname], gram)
        if got != want:
            raise SystemExit(f"pairing {key} moved: {got}")
        if got < 0:
            raise SystemExit(f"unexpected negative distinct pair {key}: {got}")

    first: dict[int, list[int]] = {}
    second: dict[int, list[int]] = {}
    for row in incidence["rows"]:
        e = int(row["exceptional_label"])
        first.setdefault(int(row["first_factor_boundary_label"]), []).append(e)
        second.setdefault(int(row["second_factor_boundary_label"]), []).append(e)

    def all140(coords: list[int]) -> list[int]:
        return [pic["pairing"](coords, known[j], gram) for j in range(140)]

    def degree_set(vals: list[int], table: dict[int, list[int]]) -> list[int]:
        return sorted({
            2 * vals[label - 1] + sum(vals[e - 1] for e in es)
            for label, es in table.items()
        })

    expected_bidegrees = {
        "D": [105, 81],
        "ccD": [81, 105],
        "ctD": [105, 81],
        "ccctD": [81, 105],
    }
    for name, coords in orbit.items():
        vals = all140(coords)
        fd = degree_set(vals, first)
        sd = degree_set(vals, second)
        if len(fd) != 1 or len(sd) != 1 or [fd[0], sd[0]] != expected_bidegrees[name]:
            raise SystemExit(f"bidegree {name} moved: {fd}, {sd}")

    exact = cert["exact_galois_v4_orbit"]
    if exact["pairwise_intersections"] != expected_pairs:
        raise SystemExit("certificate pair table mismatch")
    if exact["modular_bidegrees"] != expected_bidegrees:
        raise SystemExit("certificate bidegree table mismatch")
    if not exact["all_four_classes_pairwise_distinct"]:
        raise SystemExit("certificate distinctness regressed")
    if exact["negative_distinct_pair_obstruction_found"]:
        raise SystemExit("certificate falsely claims negative obstruction")

    consequence = cert["conditional_geometric_consequence"]
    if consequence["smallest_pairwise_intersection_length"] != 1026:
        raise SystemExit("support bound moved")
    if consequence["rational_support_identified"] or consequence["isolated_rational_intersection_point_excluded"]:
        raise SystemExit("support firewall regressed")
    decision = cert["decision"]
    if decision["Q602_excluded"] or decision["O210_excluded"] or decision["O212_plus_advance_allowed"]:
        raise SystemExit("credit firewall regressed")
    if cert["fixed_target"]["surviving_residues_decimal"] != [73, 97, 235]:
        raise SystemExit("survivors moved")

    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1648AB_EXACT_GALOIS_V4_INTERSECTIONS_NONEXCLUSION",
        "certificate_canonical_sha256": EXPECTED_CERT,
        "orbit_size": 4,
        "pairwise_intersections": expected_pairs,
        "smallest_pairwise_intersection_length": 1026,
        "support_improved_from_AA": 1116,
        "rational_support_identified": False,
        "Q602_excluded": False,
        "O210_excluded": False,
        "survivors_current_credit": [73, 97, 235],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
