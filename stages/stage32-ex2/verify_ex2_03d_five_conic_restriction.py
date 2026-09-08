#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "EX2-03" / "remaining-five-conic-restriction-preflight.json"
DIAG = HERE / "diagnose_ex2_03d_zero_curve_geometry.py"

EXPECTED_ART_BLOB = "32e19797812f35ad15fc5cad7559be76140480ef"
EXPECTED_ART_CANONICAL = "3f8ef39f3bd52804394b704fc2d6c2d810843d9f9f94530796c8c12c75d6f120"
EXPECTED_DIAG_BLOB = "9df4d917332610e68a48641c58805a541111b5ff"
EXPECTED_DIAG_CANONICAL = "4e66a7b4c2ffed5b1a106b0ed01f415b3c28501260380d837f02db8d7b1015cb"
LABELS = [21, 24, 25, 30, 31]
GRAM = [[-4,0,0,0,0],[0,-4,0,0,0],[0,0,-4,0,0],[0,0,0,-4,0],[0,0,0,0,-4]]


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True).strip()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    if blob(ART) != EXPECTED_ART_BLOB:
        raise SystemExit("EX2-03D artifact blob moved")
    if blob(DIAG) != EXPECTED_DIAG_BLOB:
        raise SystemExit("EX2-03D diagnostic blob moved")

    art = json.loads(ART.read_text())
    if canonical(art) != EXPECTED_ART_CANONICAL or art["canonical_sha256_without_this_field"] != EXPECTED_ART_CANONICAL:
        raise SystemExit("EX2-03D artifact canonical mismatch")

    raw = subprocess.check_output([sys.executable, "-B", str(DIAG)], cwd=ROOT, text=True)
    diag = json.loads(raw)
    if diag["canonical_sha256_without_this_field"] != EXPECTED_DIAG_CANONICAL:
        raise SystemExit("EX2-03D diagnostic replay moved")
    if diag["remaining_unresolved_labels_1based"] != LABELS:
        raise SystemExit("remaining labels moved")
    if diag["remaining5_genus0_labels_1based"] != LABELS or diag["remaining5_genus1_labels_1based"] != []:
        raise SystemExit("remaining curve genera moved")
    if diag["remaining5_intersection_matrix"] != GRAM:
        raise SystemExit("remaining conic intersection matrix moved")
    if not diag["remaining5_negative_definite_by_sylvester"]:
        raise SystemExit("negative definiteness moved")

    geom = art["exact_geometry"]
    assert geom["intersection_matrix"] == GRAM
    assert geom["pairwise_disjoint"] is True
    assert geom["all_five_canonical_degree"] == 2
    assert geom["all_five_self_intersection"] == -4
    assert geom["all_five_arithmetic_and_geometric_genus"] == 0
    assert geom["all_five_are_smooth_rational_conic_strict_transforms_over_Qbar"] is True
    assert geom["V6_dot_each_curve"] == 0

    rr = art["restriction_reduction"]["riemann_roch"]
    assert rr["chi_O_S"] == 8
    assert rr["V6_square"] == 758 and rr["K_dot_V6"] == 186
    assert rr["chi_O_V6"] == 8 + (758 - 186) // 2 == 294
    c = rr["for_each_C"]
    assert c == {
        "C_square": -4,
        "K_dot_C": 2,
        "K_dot_V6_minus_C": 184,
        "V6_dot_C": 0,
        "V6_minus_C_square": 754,
        "chi_O_V6_minus_C": 293,
    }
    assert 8 + (754 - 184) // 2 == 293
    assert 16 - 186 + 2 == -168
    assert rr["h2_O_V6_minus_C"] == 0
    assert art["restriction_reduction"]["target_space_dimension"] == 1
    assert art["restriction_reduction"]["missing_interface"] == "H0_V6_TO_TRIVIAL_CONIC_RESTRICTION_EVALUATION_OR_EQUIVALENT_H1_JUMP_CONTROL"

    dec = art["decision"]
    assert dec["remaining_five_fixedness_classified"] is False
    assert dec["remaining_five_nonfixedness_classified"] is False
    assert dec["known140_unsat_used_as_fixedness"] is False
    assert dec["next_leaf"] == "EX2-03E_FIVE_CONIC_RESTRICTION_EVALUATION_OR_H1_JUMP_PREFLIGHT"

    for key, value in art["credit_firewall"].items():
        if value:
            raise SystemExit(f"credit firewall moved: {key}")

    print("PASS Stage32EX2 EX2-03D five-conic restriction reduction")
    print("remaining_conics=21,24,25,30,31 pairwise_disjoint=true gram=-4I5")
    print("restriction_bundle_each=O_P1 target_H0_dimension=1")
    print("chi_V6=294 chi_V6_minus_C=293 h2_V6_minus_C=0")
    print("fixedness_unresolved=true next=EX2-03E")


if __name__ == "__main__":
    main()
