#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage32-ex2/EX2-01/section-source-inventory.json"
EX200 = ROOT / "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json"
PW05 = ROOT / "docs/arsenal/cards/provisional/S32-PW05.md"

LOCKS = {
    EX200: "b72b7582339d3933ac4485a1cf92c7be07809dc9",
    PW05: "18988010867b5bd6278e4431b9f0efe81186c381",
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    for path, expected in LOCKS.items():
        actual = blob(path)
        assert actual == expected, (path, actual, expected)

    c = json.loads(CERT.read_text())
    ex0 = json.loads(EX200.read_text())
    pw05 = PW05.read_text()

    assert c["schema"] == "STAGE32EX2_EX2_01_SECTION_SOURCE_INVENTORY_V1"
    assert c["status"] == "PASS_CERTIFIED_ABSTRACT_SECTION_LINE_COORDINATE_LANES_TYPED_BLOCKED"
    assert c["target"]["base_field_context"] == "QBAR_GEOMETRIC"
    assert c["target"]["divisor_class"] == "V6"
    assert c["target"]["h0_lower_bound"] == ex0["riemann_roch_scope"]["h0_lower_bound"] == 294

    src = ex0["known140_scope"]
    bridge = c["known140_effective_divisor_section_bridge"]
    inp = bridge["input"]
    assert src["exact_nonnegative_integer_decomposition_exists"] is True
    assert inp["nonzero_term_count"] == src["nonzero_term_count"] == 61
    assert inp["total_multiplicity"] == src["total_multiplicity"] == 155
    assert inp["normal_curve_multiplicity"] == src["normal_curve_multiplicity"] == 73
    assert inp["exceptional_curve_multiplicity"] == src["exceptional_curve_multiplicity"] == 82
    assert inp["effective"] is True

    lemma = bridge["geometric_lemma"]
    assert lemma["S_is_connected_projective_integral_over_Qbar"] is True
    assert lemma["E_known140_is_effective_Cartier_on_smooth_S"] is True
    assert lemma["projective_section_line_independent_of_chosen_isomorphism"] is True

    out = bridge["output"]
    assert out["object_type"] == "PROJECTIVE_SECTION_LINE_IN_P_H0_L"
    assert out["certified_nonzero_section_line"] is True
    assert out["certified_subspace_dimension"] == 1
    assert out["spans_complete_H0"] is False
    assert out["ambient_coefficients_materialized"] is False
    assert out["Q_descent_certified"] is False
    assert out["positive_EX2_terminal"] is False

    lanes = {item["lane"]: item for item in c["lane_inventory"]}
    assert set(lanes) == {
        "KNOWN_CURVE_EFFECTIVE_DIVISOR",
        "KNOWN_CURVE_EQUATION_PRODUCTS",
        "AMBIENT_PROJECTIVE_RESTRICTIONS",
        "MODULAR_OR_THETA_FORMS",
        "COX_GRADED_IDEAL_SYZYGY",
        "PULLBACK_OR_NORM_FROM_COVERS_QUOTIENTS",
        "SYMMETRY_OR_GALOIS_SECTION_ORBITS",
    }
    assert lanes["KNOWN_CURVE_EFFECTIVE_DIVISOR"]["status"] == "EXECUTABLE_AT_ABSTRACT_DIVISOR_AND_PROJECTIVE_SECTION_LEVEL"
    assert lanes["KNOWN_CURVE_EFFECTIVE_DIVISOR"]["coverage"] == "CERTIFIED_1D_SUBSPACE_ONLY"
    assert lanes["KNOWN_CURVE_EFFECTIVE_DIVISOR"]["complete_H0"] is False
    for key in [
        "KNOWN_CURVE_EQUATION_PRODUCTS",
        "AMBIENT_PROJECTIVE_RESTRICTIONS",
        "MODULAR_OR_THETA_FORMS",
        "COX_GRADED_IDEAL_SYZYGY",
        "PULLBACK_OR_NORM_FROM_COVERS_QUOTIENTS",
        "SYMMETRY_OR_GALOIS_SECTION_ORBITS",
    ]:
        assert lanes[key]["status"].startswith("BLOCKED_")
        assert lanes[key]["complete_H0"] is False

    assert "FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION" in pw05
    assert "semantic/geometric identification merely from reconstructed algebra" in pw05
    symmetry_lane = lanes["SYMMETRY_OR_GALOIS_SECTION_ORBITS"]
    assert symmetry_lane["status"] == "BLOCKED_LINE_BUNDLE_LINEARIZATION"
    missing = symmetry_lane["missing_object"]
    assert "linearization" in missing and "H0" in missing

    discovery = c["bounded_discovery"]
    assert discovery["direct_reusable_coordinate_section_asset_found"] is False
    assert discovery["search_miss_is_repository_wide_absence_claim"] is False
    assert discovery["arsenal_catalog_checked"] is True

    exit_ = c["exit"]
    assert exit_["EX2_01_complete"] is True
    assert exit_["abstract_divisor_representative_line_bundle_realization"] is True
    assert exit_["coordinate_line_bundle_presentation"] is False
    assert exit_["certified_section_subspace_obtained"] is True
    assert exit_["certified_section_subspace_dimension"] == 1
    assert exit_["complete_section_space_basis_obtained"] is False
    assert exit_["explicit_coordinate_section_obtained"] is False
    assert exit_["next_leaf"] == "EX2-02_EXACT_FIXED_COMPONENT_EXTRACTION"

    for key, value in c["credit_firewall"].items():
        assert value is False, (key, value)

    print(
        "Stage32EX2 EX2-01 section inventory: PASS; one exact abstract projective section line comes from the retained known-140 effective divisor, while coordinate/H0-complete lanes remain typed-blocked and no terminal or Stage32 credit is granted."
    )


if __name__ == "__main__":
    main()
