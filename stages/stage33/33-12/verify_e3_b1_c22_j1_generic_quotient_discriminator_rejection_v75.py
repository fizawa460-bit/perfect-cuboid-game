#!/usr/bin/env python3
"""Verify V75: the d-independent generic quotient cannot decide J1's 4-vs-12 marked kernel."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
ROOT = STAGE.parents[1]
V75 = HERE / "e3-b1-c22-j1-generic-quotient-discriminator-rejection-v75.json"
V73 = HERE / "e3-b1-c22-j1-translation-torsor-v73.json"
V65 = HERE / "e3-b1-j1-marked-kc-discriminator-gate-v65.json"
J2Q = STAGE / "33-05" / "j2-r4-translation-quotient-lattice.json"
J2QV = STAGE / "33-05" / "certify_j2_r4_translation_quotient_lattice.py"
FINGER = HERE / "j2-brauer-kernel-lattice-fingerprints.json"
ORIENT = HERE / "j2-cv-d2-semantic-orientation.json"

EXPECTED_V75 = "22b166d44d516a5e0cb57bf582a21144d40b0035489a29036f86dc0944ce1192"
LOCKS = {
    V73: "277ec4bfd86a118b25e45632ce4a02fe3af87cc1",
    V65: "e3634d9c8ed0f4f58ff4132f7bd5822f60fa23c3",
    J2Q: "eae02e2c9a5f3df15589a5c86d209c44bc60a7f1",
    J2QV: "67019914d91ec4f82f76421872fbc201404ddfe2",
    FINGER: "ba48b42a2af3afeaf03d031f8ee6e11fa73df832",
    ORIENT: "140acdc9896d1d87a82a1807fd92ce276a620d75",
}


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def main() -> None:
    for path, expected in LOCKS.items():
        require(blob_sha(path) == expected, f"source blob drift: {path}")

    v75 = json.loads(V75.read_text())
    require(v75["canonical_sha256"] == EXPECTED_V75 == csha(v75), "V75 canonical mismatch")
    v73 = json.loads(V73.read_text())
    v65 = json.loads(V65.read_text())
    j2q = json.loads(J2Q.read_text())
    finger = json.loads(FINGER.read_text())
    orient = json.loads(ORIENT.read_text())

    require(v73["canonical_sha256"] == "b6a8dd83cd83547525e8ff328cccc1572791c52bea6061137c2bc59a134fa09d", "V73 canonical moved")
    require(v73["translation_torsor"]["twisting_squareclass"] == "d=f1", "V73 is not J1/f1")
    require(v73["translation_torsor"]["affine_quartic"] == "d*v^2=n^4-2*a*d*n^2+d^2*q^2", "V73 quartic moved")
    require(v73["credit_firewall"]["D2_1_closed"] is True, "D2.1 not closed")
    require(v73["credit_firewall"]["D2_2_closed"] is False, "D2.2 prematurely closed in V73")

    require(j2q["canonical_sha256"] == "89efe817d2689d7533c99ea9b7f7cc753b90bfd3e55377fef8ee22cfc549108d", "J2 quotient canonical moved")
    qmap = j2q["correct_torsor_degree_two_quotient"]["map"]
    require(qmap == {"X": "n^2/d", "Y": "-n*v/d"}, "J2 quotient map moved")
    require(j2q["correct_torsor_degree_two_quotient"]["target"] == "E'_Tr: Y^2=X*(X^2-2*a*X+q^2)", "J2 quotient target moved")

    # Exact d-cancellation. Put X=n^2/d, so n^2=dX. The V73 equation gives
    # v^2=d*(X^2-2aX+q^2). Therefore Y^2=n^2*v^2/d^2
    # = X*(X^2-2aX+q^2). No coefficient involving d remains.
    replay = v75["generic_quotient_replay"]
    require(replay["map"] == qmap, "V75 quotient map moved")
    require(replay["quotient_target"] == j2q["correct_torsor_degree_two_quotient"]["target"], "V75 target not the exact J2 quotient target")
    require(replay["d_survives_in_quotient_equation"] is False, "V75 failed to record d-cancellation")
    require(replay["same_generic_target_as_j2"] is True, "V75 generic target equality lost")

    require(finger["canonical_sha256"] == "572ad201ca859c5970507dbc598ac0489fdd90d10ee74ffc58f5e2f3fba7927e", "fingerprints canonical moved")
    norms = finger["exact_conclusion"]["minimum_norm_to_functional"]
    require(norms == {"4": [0, 1], "8": [1, 0], "12": [1, 1]}, "marked minimum-norm dictionary moved")
    require(orient["canonical_sha256"] == "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e", "semantic orientation moved")
    require(orient["source_locks"]["named_transport_rigidity_git_blob_sha1"] == "2095dbaca6341f65a29690fe6b373f3da1be745a", "historical rigidity lock moved")
    require(orient["kernel_fingerprint_identification"]["observed_minimum_norm"] == 8, "J2 observed norm moved")
    require(orient["kernel_fingerprint_identification"]["selected_functional_f2"] == [1, 0], "J2 marked coordinate moved")

    gate = v65["locked_frontier"]
    require(v65["canonical_sha256"] == "7ebef9a6182522f772f198d8c1572acc48cd8441f6158312d1f3f3f2c7fcc01c", "V65 canonical moved")
    require(gate["J2_marked_kc_coordinate_f2"] == [1, 0], "V65 J2 anchor moved")
    require(gate["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]], "V65 J1 one-bit gate moved")
    require(v65["target_discriminator_fingerprints"]["u2"]["minimum_norm"] == 4, "V65 norm4 target moved")
    require(v65["target_discriminator_fingerprints"]["u1_plus_u2"]["minimum_norm"] == 12, "V65 norm12 target moved")

    nonportable = v75["nonportable_j2_lattice_step"]
    require(nonportable["j2_exact_result"]["minimum_norm"] == 8, "V75 J2 result moved")
    require(nonportable["j2_exact_result"]["marked_coordinate_f2"] == [1, 0], "V75 J2 coordinate moved")
    require(nonportable["v65_exact_j1_gate"]["allowed_minimum_norms"] == [4, 12], "V75 J1 allowed norms moved")
    require(nonportable["v65_exact_j1_gate"]["allowed_marked_coordinates_f2"] == [[0, 1], [1, 1]], "V75 J1 candidates moved")
    require(8 not in nonportable["v65_exact_j1_gate"]["allowed_minimum_norms"], "V75 accidentally admits J2 norm8 for J1")

    missing = v75["exact_missing_interface"]
    require(missing["name"] == "J1_SPECIFIC_COMPACTIFIED_SURFACE_INTEGRAL_KERNEL_OR_PRIMITIVE_PULLBACK_IDENTIFICATION", "missing interface moved")
    require(missing["generic_function_field_quotient_alone_sufficient"] is False, "generic quotient incorrectly promoted")

    nxt = v75["next_kernel_contract"]
    require(nxt["allowed_minimum_norm_outcomes"] == [4, 12], "next J1 outcomes moved")
    require(nxt["minimum_norm_materialized"] is False, "J1 minimum norm prematurely selected")
    require(nxt["marked_kc_coordinate_selected"] is False, "J1 marked coordinate prematurely selected")

    fw = v75["credit_firewall"]
    require(fw["D2_1_closed"] is True and fw["D2_2_closed"] is False, "D2 gate moved")
    require(fw["j1_translation_torsor_materialized"] is True, "V73 torsor credit lost")
    for key in [
        "j1_twisted_kernel_minimum_norm_materialized", "j1_marked_kc_coordinate_selected",
        "identity_vs_shear_selected", "e3_kummer_column_materialized", "e3_mask20_membership_computed",
        "genuine_full_surface_H2_mu2_lift_for_e3", "stage33_12_closed", "stage33_13_released",
        "receiver_credit", "theorem_credit", "endpoint_credit", "perfect_cuboid_credit", "merge_allowed",
    ]:
        require(fw[key] is False, f"firewall leaked: {key}")

    print(json.dumps({
        "success": True,
        "marker": "V75_J1_GENERIC_QUOTIENT_DISCRIMINATOR_REJECTED",
        "canonical_sha256": EXPECTED_V75,
        "generic_quotient": "Eprime_Tr_independent_of_d",
        "j2_transplant_would_force_norm": 8,
        "allowed_j1_norms": [4, 12],
        "next_exact_leaf": nxt["next_exact_leaf"],
        "D2_2_closed": False,
        "merge_allowed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
