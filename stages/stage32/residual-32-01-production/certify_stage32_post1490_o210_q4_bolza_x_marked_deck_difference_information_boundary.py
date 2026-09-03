#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXPECTED = "c19c6b2aec02276d555d751505cdb2b20d4c3f1712c8edfed63046802f8b0150"
LOCKS = {
    "stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json": (
        "def8b60b726c02aa7ee97c0cc25b34f43525ec34",
        "eb31183bf519fec4ad5bb2d0799b3f0a64b7af893308e09ce0c33119b63440a1",
    ),
    "stages/stage32/residual-32-01-production/post1473-x8-marked-exceptional-incidence.json": (
        "b3f673aa73324ee731356eec2c0448592fd1e59b",
        "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143",
    ),
    "stages/stage32/residual-32-01-production/post1473-x8-v4-cusp-quotient.json": (
        "00eaebc3c57f6b5e3696c7bcd60eac5a53121f72",
        "2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5",
    ),
    "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-weierstrass-collision-delta-bound.json": (
        "b357c1df85231cad05a2dbdffc9a60541ab32c3d",
        "7ccddb53c2f4b32979e5f728f974dfa58cf346c730fe7fe040f35cc31f0f4d5f",
    ),
    "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-v4-deck-translate-defect-decomposition.json": (
        "d7ac0791f7d2eadf6ee5b9780b1f89ef9a16b502",
        "cdc186f8da6eff760a79f98b50106de19d565ebf806dc58b00cc105e4d983af2",
    ),
}


def csha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load(rel: str) -> dict:
    path = ROOT / rel
    expected_blob, expected_canon = LOCKS[rel]
    if blob(path) != expected_blob:
        raise SystemExit(f"source blob moved: {rel}")
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != expected_canon:
        raise SystemExit(f"source canonical moved: {rel}")
    return obj


def grouped(masses: list[int], labels: list[str]) -> dict[str, int]:
    out = {"g1": 0, "g2": 0, "g1_plus_g2": 0}
    for mass, label in zip(masses, labels, strict=True):
        out[label] += mass
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", type=Path, required=True)
    args = ap.parse_args()

    cert = json.loads(args.check.read_text())
    claimed = cert.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED or csha(cert) != claimed:
        raise SystemExit("information-boundary canonical mismatch")

    cart = load("stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json")
    incidence = load("stages/stage32/residual-32-01-production/post1473-x8-marked-exceptional-incidence.json")
    v4 = load("stages/stage32/residual-32-01-production/post1473-x8-v4-cusp-quotient.json")
    collision = load("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-weierstrass-collision-delta-bound.json")
    defect = load("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-v4-deck-translate-defect-decomposition.json")

    square = cart["group_quotient_square"]
    deck_object = cert["deck_object"]
    if square["P"] != "Z x Z with diagonal G action" or square["X"] != "P/H_diag (Beauville cover surface)" or square["C0"] != "Z/H":
        raise SystemExit("common-cover quotient objects moved")
    if square["H"] != "Gamma'[4]/Gamma[8] ~= V4, order 4, normal index 2":
        raise SystemExit("H quotient moved")
    if deck_object["deck_group"] != "(H x H)/H_diag ~= H ~= V4" or not cert["firewalls"].get("G_diag_over_H_diag_is_not_the_q_deck_group"):
        raise SystemExit("q deck-group correction missing")
    if defect["quotient_geometry"].get("finite_etale_degree") != 4 or defect["quotient_geometry"].get("deck_group") != "V4":
        raise SystemExit("degree-four V4 deck geometry moved")

    rows = incidence["rows"]
    pair_records = collision["weierstrass_support"]["pair_mass_capacity"]
    if len(rows) != 48 or len(pair_records) != 12:
        raise SystemExit("retained marked support cardinality moved")
    if any(set(r) != {"exceptional_label", "first_factor_boundary_label", "second_factor_boundary_label"} for r in rows):
        raise SystemExit("marked-node projected schema moved")
    if any(set(r) != {"first_factor_boundary_label", "second_factor_boundary_label", "exceptional_mass", "m2_capacity"} for r in pair_records):
        raise SystemExit("pair-mass projected schema moved")

    pair_counts = Counter(f"{r['first_factor_boundary_label']}:{r['second_factor_boundary_label']}" for r in rows)
    if len(pair_counts) != 12 or set(pair_counts.values()) != {4}:
        raise SystemExit("48-node / 12-pair incidence moved")

    witness = cert["nonidentifiability_witness"]
    pair_order = [f"{r['first_factor_boundary_label']}:{r['second_factor_boundary_label']}" for r in pair_records]
    masses = [r["exceptional_mass"] for r in pair_records]
    if pair_order != collision["weierstrass_support"]["pair_order"] or pair_order != witness["visible_pair_order"]:
        raise SystemExit("visible pair order moved")
    if masses != witness["visible_pair_masses"] or sum(masses) != 266:
        raise SystemExit("visible pair masses moved")
    if set(pair_counts) != set(pair_order):
        raise SystemExit("incidence/pair-mass support mismatch")

    if not v4["firewalls"].get("abstract_cusp_orbits_not_yet_retained_boundary_label_identification"):
        raise SystemExit("abstract-to-retained label firewall moved")
    arithmetic = defect["intersection_arithmetic"]
    if arithmetic.get("exact_defect_decomposition") != "delta_D+c_g1+c_g2+c_g1_plus_g2=8586":
        raise SystemExit("defect budget moved")
    if defect["decision"].get("three_translate_pairings_individually_decided"):
        raise SystemExit("upstream unexpectedly claims individual deck split")

    labels = witness["deck_labels"]
    if labels != ["g1", "g2", "g1_plus_g2"]:
        raise SystemExit("deck-label order moved")
    A = witness["annotation_A_labels"]
    B = witness["annotation_B_labels"]
    if len(A) != 12 or len(B) != 12 or Counter(A) != Counter(B) or Counter(A) != Counter(witness["each_annotation_label_count"]):
        raise SystemExit("annotation cardinality witness moved")
    if grouped(masses, A) != witness["annotation_A_grouped_visible_mass"]:
        raise SystemExit("annotation A grouped mass mismatch")
    if grouped(masses, B) != witness["annotation_B_grouped_visible_mass"]:
        raise SystemExit("annotation B grouped mass mismatch")
    if grouped(masses, A) == grouped(masses, B):
        raise SystemExit("annotations do not witness non-identifiability")

    visible = list(zip(pair_order, masses, strict=True))
    annotated_A = [(p, m, label) for (p, m), label in zip(visible, A, strict=True)]
    annotated_B = [(p, m, label) for (p, m), label in zip(visible, B, strict=True)]
    if [(p, m) for p, m, _ in annotated_A] != visible or [(p, m) for p, m, _ in annotated_B] != visible:
        raise SystemExit("annotation projection witness failed")

    boundary = cert["exact_boundary"]
    firewalls = cert["firewalls"]
    inventory = cert["retained_projection_inventory"]
    if inventory.get("relative_H_deck_difference_field_present"):
        raise SystemExit("certificate unexpectedly claims retained relative-H label")
    if boundary.get("retained_projected_payload_determines_ordered_deck_split_of_visible_pair_mass"):
        raise SystemExit("certificate overclaims ordered deck split")
    if boundary.get("retained_projected_payload_determines_individual_D_dot_tD"):
        raise SystemExit("certificate overclaims D.t(D)")
    if not firewalls.get("annotation_witness_is_not_geometry") or not firewalls.get("visible_exceptional_mass_is_not_c_t"):
        raise SystemExit("semantic firewall missing")
    if cert["decision"].get("O210_excluded") or cert["decision"].get("individual_deck_pairings_decided"):
        raise SystemExit("certificate overclaims O210 closure")

    print(json.dumps({
        "verdict": "PASS_EXACT_RETAINED_RELATIVE_H_DECK_LABEL_INFORMATION_BOUNDARY",
        "q_deck_group": deck_object["deck_group"],
        "visible_pair_mass_total": sum(masses),
        "annotation_A_grouped_visible_mass": grouped(masses, A),
        "annotation_B_grouped_visible_mass": grouped(masses, B),
        "individual_D_dot_tD_known": False,
        "canonical_sha256": claimed,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
