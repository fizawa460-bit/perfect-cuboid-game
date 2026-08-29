#!/usr/bin/env python3
"""Materialize the exact named J2 half-divisor input for the missing Kummer glue.

This is a MAIN progress certificate.  It does not guess a Kc discriminant
coordinate.  It source-locks the explicit J2 function/divisor representative,
the full-surface zero-defect contract, and the pinned Stoll marked-Picard
interface, then states the smallest remaining coordinate bridge exactly.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
J2SRC = S33 / "33-05" / "j2_arithmetic_descent.py"
J2ZERO = HERE / "j2-full-surface-mu2-zero-defect-contract.json"
MARKED = S33 / "33-09" / "marked-picard-basis-source.json"
OUT = HERE / "j2-named-kummer-glue-input.json"

EXPECTED_J2SRC_BLOB = "a63be5592c793c3812da99275478f14dd0d2687b"
EXPECTED_J2ZERO = "ac2999b2e684c534b90c9f6c8a68261b33b3d549b4d4162d107c0509a6082b6a"
EXPECTED_MARKED = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
EXPECTED_STOLL_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical source lock moved: {path}")
    return obj


if git_blob_sha1(J2SRC) != EXPECTED_J2SRC_BLOB:
    raise SystemExit("J2 arithmetic descent source moved")
text = J2SRC.read_text(encoding="utf-8")
for marker in [
    "f2 = sp.cancel((t-r2)/(t-r4))",
    "div(ell)=4*infinity_minus-2*P1-2*P2",
    '"geometric_divisor":"4*infinity_minus - 2*P_root(Dplus,1) - 2*P_root(Dplus,2)"',
    '"Q_defined_arithmetic_representative_materialized":True',
]:
    if marker not in text:
        raise SystemExit(f"named J2 marker moved: {marker}")

j2zero = load_canonical(J2ZERO, EXPECTED_J2ZERO)
marked = load_canonical(MARKED, EXPECTED_MARKED)
if j2zero["finite_v4_consequence"]["delta_Kum_V4_of_J2"] != "EXACT_ZERO":
    raise SystemExit("J2 zero-defect contract regressed")
if marked["source"]["git_blob_sha1"] != EXPECTED_STOLL_BLOB:
    raise SystemExit("pinned Stoll source moved")

cert = {
    "schema": "STAGE33_12_J2_NAMED_KUMMER_GLUE_INPUT_V1",
    "source_locks": {
        "j2_arithmetic_descent_script_git_blob_sha1": EXPECTED_J2SRC_BLOB,
        "j2_full_surface_mu2_zero_defect_contract_sha256": EXPECTED_J2ZERO,
        "marked_picard_basis_source_sha256": EXPECTED_MARKED,
        "stoll_upstream_git_blob_sha1": EXPECTED_STOLL_BLOB,
    },
    "named_J2_geometric_anchor": {
        "normalization": "z^2=t^4-6*t^2+1",
        "squareclass": "f2=(t-r2)/(t-r4), r2=-(1+sqrt(2)), r4=1-sqrt(2)",
        "Q_defined_branch_representative": "ell_J2=4*(alpha^2*t^2+t^4-4*t^2+2)/((t^2-1)*(t^2-2*t-1))",
        "geometric_divisor": "4*infinity_minus - 2*P_root(Dplus,1) - 2*P_root(Dplus,2)",
        "half_divisor_E": "2*infinity_minus - P_root(Dplus,1) - P_root(Dplus,2)",
        "div_ell_equals_2E": True,
        "Q_defined_arithmetic_representative": True,
        "full_surface_delta_Kum_V4": "EXACT_ZERO",
    },
    "stoll_marked_picard_interface": {
        "pinned_repository": "MichaelStollBayreuth/Verification",
        "pinned_commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "pinned_path": "Cuboids/cuboids.magma",
        "PicK_rank": 20,
        "known_curve_index_basis_length": 20,
        "available_exact_routine": "imageinPicK(C): intersection vector against indlistK -> PicK coordinates",
        "MatStoK_and_MatKtoS_present": True,
    },
    "exact_gap": {
        "J2_named_half_divisor_materialized": True,
        "normalization_support_to_stoll_marked_divisor_map_materialized": False,
        "J2_mu2_lift_to_picard_transcendental_glue_coordinate_materialized": False,
        "J2_kc_discriminant_coordinate_materialized": False,
        "J2_full_surface_proper14_coordinate_materialized": False,
        "reason": "The named function/divisor representative and the marked Picard lattice are both exact, but no committed map identifies infinity_minus and the two Dplus support points with Stoll marked divisor classes, nor a Kummer glue map taking that named half-divisor data to the discriminant/Brauer coordinate.",
    },
    "minimal_next_data": {
        "step1": "Materialize the images of infinity_minus and P_root(Dplus,1/2), or directly E, in the pinned marked PicK/divisor presentation.",
        "step2": "Apply an exact Kummer/Picard-transcendental glue map to E and the Q-defined corestriction representative.",
        "step3": "Read the resulting nonzero line in Kc Br[2] discriminant coordinates and filter the six GL(2,2) adapters.",
        "orientation_after_kernel_line_warning": "Even after the J2 line is known, q1 versus q1+J2 needs one further named invariant unless the same glue construction computes q1 as well.",
    },
    "matrix_consequence": {
        "finite_v4_kummer_defect_matrix_shape": [75, 10],
        "columns_materialized": 0,
        "named_J2_kernel_relation_in_P10_materialized": False,
    },
    "promotion_firewall": {
        "adapter_unique": False,
        "proper_d2_map_computed": False,
        "arithmetic_hs_d2_computed": False,
        "global_q_residue_lifts_complete": False,
        "stage33_12_closed": False,
        "stage33_07_closed": False,
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
    "next_exact_leaf": "MATERIALIZE_J2_HALF_DIVISOR_E_IN_STOLL_MARKED_KC_PRESENTATION_AND_KUMMER_GLUE",
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "named_J2_half_divisor_materialized": True,
    "J2_kc_discriminant_coordinate_materialized": False,
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
