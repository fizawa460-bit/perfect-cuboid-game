#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "stages" / "stage32" / "residual-32-01-production"
STAGE33_07 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
EX2_03C = ROOT / "stages" / "stage32-ex2" / "EX2-03" / "known140-zero-curve-omission-witnesses.json"
TARGET = [17, 21, 24, 25, 30, 31, 98]
REMAINING = [21, 24, 25, 30, 31]

sys.path.insert(0, str(HERE))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402

EXPECTED_BLOBS = {
    V6_PATH: "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    EX2_03C: "a4b9396790b6c3b026a4a624247a48b1148a6d36",
    HERE / "hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob(path: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True
    ).strip()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def retained_degrees(marking: dict) -> list[int]:
    text = marking.get("hperp_text")
    if not isinstance(text, str):
        raise ValueError("retained marking missing hperp_text")
    lines = text.splitlines()
    if len(lines) < 5:
        raise ValueError("short hperp payload")
    n, m = map(int, lines[4].split())
    if (n, m) != (63, 140):
        raise ValueError(f"unexpected hperp dimensions {(n, m)}")
    records = [list(map(int, lines[5 + n + r].split())) for r in range(m)]
    if any(len(row) != 65 for row in records):
        raise ValueError("unexpected hperp record width")
    return [row[0] for row in records]


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def main() -> None:
    for path, expected in EXPECTED_BLOBS.items():
        actual = git_blob(path)
        if actual != expected:
            raise ValueError(f"source lock regression {path}: {actual} != {expected}")

    v6 = json.loads(V6_PATH.read_text())
    ex2c = json.loads(EX2_03C.read_text())
    if ex2c["certified_nonfixed_zero_labels_1based"] != [17, 98]:
        raise ValueError("EX2-03C nonfixed set regression")
    if ex2c["unresolved_zero_labels_1based"] != REMAINING:
        raise ValueError("EX2-03C unresolved set regression")

    bundle = load_retained(STAGE33_07 / "picard_base_rows_retained.py", "ex203d_picard")
    marking = load_retained(STAGE33_07 / "stage32_picard_marking_retained.py", "ex203d_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    coords = adapter.class_coordinates_in_retained_basis
    if coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("retained geometry shape regression")
    full = coords * gram * coords.T
    if full.shape != (140, 140) or full != full.T:
        raise ValueError("full intersection replay regression")

    degrees = retained_degrees(marking)
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    if [pairings[z - 1] for z in TARGET] != [0] * len(TARGET):
        raise ValueError("target V6-zero pairing regression")

    indices = [z - 1 for z in TARGET]
    target_gram = full.extract(indices, indices)
    remaining_pos = [TARGET.index(z) for z in REMAINING]
    remaining_gram = target_gram.extract(remaining_pos, remaining_pos)

    curves = []
    for z in TARGET:
        i = z - 1
        self_int = int(full[i, i])
        k_dot = int(degrees[i])
        genus_num = self_int + k_dot
        if genus_num % 2:
            raise ValueError(f"adjunction parity regression at label {z}")
        genus = 1 + genus_num // 2
        if z > 92:
            typ = "EXCEPTIONAL_A1_RESOLUTION_CURVE"
        elif (k_dot, self_int, genus) == (2, -4, 0):
            typ = "CANONICAL_DEGREE_2_CONIC_STRICT_TRANSFORM"
        elif (k_dot, self_int, genus) == (4, -4, 1):
            typ = "CANONICAL_DEGREE_4_GENUS_ONE_CURVE"
        else:
            typ = "RETAINED_NORMAL_CURVE_OTHER_TYPE"
        curves.append({
            "known140_label_1based": z,
            "retained_family": "exceptional" if z > 92 else "normal",
            "self_intersection": self_int,
            "K_dot_curve_from_canonical_degree": k_dot,
            "adjunction_geometric_genus": genus,
            "curve_type": typ,
            "V6_dot_curve": pairings[i],
            "degree_O_V6_restricted_to_curve": pairings[i],
            "picard64_coordinates": [int(coords[i, j]) for j in range(64)],
        })

    leading_minors = [int(remaining_gram[:k, :k].det()) for k in range(1, len(REMAINING) + 1)]
    negative_definite = all(((-1) ** k) * leading_minors[k - 1] > 0 for k in range(1, len(REMAINING) + 1))

    rational_zero = [r["known140_label_1based"] for r in curves if r["known140_label_1based"] in REMAINING and r["adjunction_geometric_genus"] == 0]
    elliptic_zero = [r["known140_label_1based"] for r in curves if r["known140_label_1based"] in REMAINING and r["adjunction_geometric_genus"] == 1]

    out = {
        "schema": "STAGE32EX2_EX2_03D_ZERO_CURVE_COMPACT_GEOMETRY_DIAGNOSTIC_V1",
        "stage": "32EX2",
        "unit": "EX2-03D",
        "status": "EXACT_COMPACT_ZERO_CURVE_GEOMETRY_REPLAY_COMPLETE",
        "source_locks": {
            "v6_blob_sha1": EXPECTED_BLOBS[V6_PATH],
            "v6_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "ex2_03c_blob_sha1": EXPECTED_BLOBS[EX2_03C],
            "ex2_03c_canonical_sha256": ex2c["canonical_sha256_without_this_field"],
            "hperp_adapter_blob_sha1": EXPECTED_BLOBS[HERE / "hperp_integral_adapter.py"],
            "hperp_adapter_canonical_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "all140_retained_coordinates_sha256": adapter.certificate["all140_retained_coordinates_sha256"],
            "full_intersection_sha256": adapter.certificate["full_intersection_sha256"],
        },
        "target_zero_labels_1based": TARGET,
        "remaining_unresolved_labels_1based": REMAINING,
        "curves": curves,
        "target_7x7_intersection_matrix": matrix_list(target_gram),
        "target_7x7_intersection_matrix_sha256": csha(matrix_list(target_gram)),
        "remaining5_intersection_matrix": matrix_list(remaining_gram),
        "remaining5_intersection_matrix_sha256": csha(matrix_list(remaining_gram)),
        "remaining5_rank": int(remaining_gram.rank()),
        "remaining5_determinant": int(remaining_gram.det()),
        "remaining5_leading_principal_minors": leading_minors,
        "remaining5_negative_definite_by_sylvester": negative_definite,
        "remaining5_genus0_labels_1based": rational_zero,
        "remaining5_genus1_labels_1based": elliptic_zero,
        "restriction_preflight": {
            "exact_picard64_classes_now_compactly_exposed": True,
            "exact_7x7_intersection_matrix_now_compactly_exposed": True,
            "exact_curve_self_intersections_and_canonical_degrees_exposed": True,
            "degree_O_V6_restriction_is_zero_for_all_seven": True,
            "degree_zero_does_not_determine_restriction_line_bundle_on_genus_one_curve": True,
            "degree_zero_on_genus_zero_curve_determines_abstract_restriction_line_bundle_as_trivial": bool(rational_zero),
            "H0_restriction_or_evaluation_map_computed": False,
            "complete_base_ideal_computed": False,
            "remaining_five_fixedness_classified": False,
        },
        "next_decision": {
            "if_any_remaining_genus0": "For genus-zero labels, the abstract degree-zero restriction bundle is trivial; fixedness still requires proving the H0 restriction map is nonzero/zero, so seek an evaluation or exact-sequence/cohomology adapter.",
            "if_any_remaining_genus1": "For genus-one labels, first identify the degree-zero class O(V6)|C in Pic^0(C), then compute/evaluate restriction; degree alone is insufficient.",
            "fallback": "If neither restriction adapter is source-bound, route to EX2-04 ideal/syzygy or section-coordinate reconstruction outside the known140 monoid.",
        },
        "firewalls": {
            "pairwise_matrix_promoted_to_fixedness": False,
            "negative_definite_null_configuration_promoted_to_fixed_part": False,
            "degree_zero_restriction_promoted_to_nonfixedness": False,
            "degree_zero_restriction_promoted_to_fixedness": False,
            "known140_unsat_promoted_to_fixedness": False,
            "complete_H0_reconstructed": False,
            "integral_irreducible_genus1_member_constructed": False,
            "population_wide_no_genus1_member_proved": False,
            "stage32_main_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
