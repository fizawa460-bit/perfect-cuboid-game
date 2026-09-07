#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
S07 = S33 / "33-07"

R2 = HERE / "e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json"
R4_LOCAL = HERE / "e3-v91c1x-r4-a2-02-local-chart-inventory.json"
R4_NEG = HERE / "e3-v91c1x-r4-retained-boundary-resolution-insufficient-for-cover-indexed-h2.json"
CERT = HERE / "e3-v91c1x-r5a-a2-02-component-p1-atlas-seeds.json"
SIDE = S07 / "materialize_mixed_order_side_ambient_function_lifts.py"
EXC = S07 / "materialize_mixed_order_exceptional_ambient_tangent_function_lifts.py"

R2_SHA = "912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1"
R4_LOCAL_SHA = "68f61b79b07027e97b4822c4f074cd52f65cf05473475fe964fd0b6785e8c53d"
R4_NEG_SHA = "cead57f641b02e8defb8cb614ee1b1acdca1ee6d1e9f7c04514ccfffef5577e0"
CERT_SHA = "76e63baad22a88f7c2b93d31930785c3b4eafe785fdc6de950756b169be7c9ce"
SIDE_FILE_SHA = "00075c19b97260cbfd51d508d5bfe649724e0333d133e0b8d71c0ec8d6cea797"
EXC_FILE_SHA = "3a4d9115845de0d2c43458ca293333befb8de7c69068ff8280d1d70a7a2023e7"

EXC_TARGETS = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]
SIDE_TARGETS = ["SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008"]


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj["canonical_sha256"]
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = csha(body)
    assert claimed == expected == actual, (path, claimed, expected, actual)
    return obj


def fsha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


r2 = load_locked(R2, R2_SHA)
local = load_locked(R4_LOCAL, R4_LOCAL_SHA)
r4 = load_locked(R4_NEG, R4_NEG_SHA)
cert = load_locked(CERT, CERT_SHA)

assert local["components"] == EXC_TARGETS + SIDE_TARGETS
assert r4["next_exact_leaf_after_audit"] == (
    "V91C1X_R5_FIND_OR_CONSTRUCT_SOURCE_BOUND_A2_02_FINITE_COVER_LOCAL_EQUATION_UNIFORMIZER_OVERLAP_GLUE_PACKAGE"
)
assert fsha(SIDE) == SIDE_FILE_SHA
assert fsha(EXC) == EXC_FILE_SHA

side_text = SIDE.read_text(encoding="utf-8")
exc_text = EXC.read_text(encoding="utf-8")
assert 'if 1 <= side <= 8:' in side_text
assert 'N=linear_basis({"b2":1}); D=linear_basis({"c":1,"b3":-1})' in side_text
assert 'A1: t=u/v = b2/(c-b3)' in side_text
assert "boundary-function ambient lift, not yet a global Gersten/Brauer lift" in side_text

assert "deterministic_left_inverse(B)" in exc_text
assert "R=(F*Y).applyfunc(clean)" in exc_text
assert "R*p!=sp.zeros(2,1)" in exc_text
assert "This still is not a global Gersten/Brauer lift" in exc_text
assert "global compatibility across all 72 boundary components remain" in exc_text

for row in local["exceptional_rows"]:
    assert row["component_id"] in EXC_TARGETS
    pair = row["ambient_projection_R0_R1_coefficients_L_basis"]
    assert isinstance(pair, list) and len(pair) == 2
    assert all(isinstance(v, list) and len(v) == 7 for v in pair)

for row in local["side_rows"]:
    assert row["component_id"] in SIDE_TARGETS
    idx = int(row["component_id"].split("_")[1])
    assert 1 <= idx <= 8
    assert row["D_coefficients_L_basis"] is not None

sig = cert["exact_constructive_signal"]
assert sig["side_family_for_all_four_targets"] == "A1"
assert sig["side_component_p1_homogeneous_pair"] == ["N=b2", "D=c-b3"]
assert sig["exceptional_pair_count"] == 4
assert sig["all_eight_target_components_have_source_bound_p1_atlas_seed_pairs"] is True

fw = cert["credit_firewall"]
for key in [
    "finite_surface_cover_materialized",
    "component_uniformizers_materialized",
    "literal_local_surface_equations_materialized",
    "overlap_transitions_materialized",
    "swap23_common_refinement_materialized",
    "literal_mu2_2_cocycle_materialized",
    "equivalent_unimodular_cech_glue_materialized",
    "line_bundle_gm_1_cocycle_ell_ij_materialized",
    "square_root_1_cochain_r_ij_materialized",
    "triple_overlap_identity_verified",
    "h2_fixedness_credit",
    "mask20_credit",
    "source_bound_dim5_credit",
    "marked_brauer_image_credit",
    "stage33_close_credit",
    "stage33_release_credit",
    "theorem_credit",
    "receiver_credit",
    "endpoint_credit",
    "merge_allowed",
]:
    assert fw[key] is False, key

assert cert["next_exact_leaf"] == (
    "V91C1X_R5B_MATERIALIZE_FOUR_TARGET_ODP_BLOWUP_CHARTS_AND_FOUR_SIDE_NEIGHBORHOOD_CHARTS_THEN_VERIFY_COVER_AND_OVERLAPS"
)
assert cert["entry"]["stage33_progress"] == "6/11"
assert r2["current_materialization_status"]["accepted_source_representative_materialized"] is False

print(json.dumps({
    "success": True,
    "marker": "V116_V91C1X_R5A_COMPONENT_P1_ATLAS_SEEDS",
    "certificate_sha256": CERT_SHA,
    "target_component_count": 8,
    "exceptional_seed_pairs": 4,
    "side_seed_pairs": 4,
    "surface_cover_materialized": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "stage33_progress": "6/11",
}, sort_keys=True))
