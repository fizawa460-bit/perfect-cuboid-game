#!/usr/bin/env python3
"""Verify the bounded V91A type obstruction and direct-Cech route narrowing."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
MARKED = STAGE / "33-09"
CERT = HERE / "e3-v91a-literal-integral-divisor-type-obstruction.json"
V91 = HERE / "e3-retained-at-marked-picard-dual-source-v91.json"
V89 = HERE / "e3-proper14-dual-to-discriminant-quotient-bridge-v89.json"
V88 = HERE / "e3-direct-cech-seed-contract-v88.json"
SOURCE = MARKED / "marked-picard-basis-source.json"

CERT_SHA = "1da7e6c26939a80ec5dec24c19cd04615084982d4fc4f29086273796cef102d9"
V91_SHA = "729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9"
V89_SHA = "26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639"
V88_SHA = "1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7"
SOURCE_SHA = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
TARGET = [1,0,0,0,0,0,0,1,0,1,0,0,0,0]


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path}")
    return obj


cert = load_locked(CERT, CERT_SHA)
v91 = load_locked(V91, V91_SHA)
v89 = load_locked(V89, V89_SHA)
v88 = load_locked(V88, V88_SHA)
source = load_locked(SOURCE, SOURCE_SHA)

if cert["schema"] != "stage33.e3.v91a.literal_integral_divisor_type_obstruction.v1":
    raise SystemExit("V91A schema moved")
locks = cert["source_locks"]
if locks != {
    "marked_picard_basis_source_canonical_sha256": SOURCE_SHA,
    "v88_canonical_sha256": V88_SHA,
    "v89_canonical_sha256": V89_SHA,
    "v91_canonical_sha256": V91_SHA,
}:
    raise SystemExit("V91A source locks moved")

# V91 is an exact nonzero discriminant/dual class, not an integral divisor.
bind = v91["e3_source_binding"]
if bind["object_type"] != "marked Picard dual-lattice/discriminant class, not an integral Picard divisor":
    raise SystemExit("V91 object type moved")
if bind["retained_at_mod2_quotient_coordinate_f2"] != TARGET:
    raise SystemExit("V91 mixed target moved")
if bind["retained_at_mod2_quotient_support_one_based"] != [1, 8, 10]:
    raise SystemExit("V91 support moved")
if not bind["source_bound_to_actual_140_class_marking"] or not bind["mixed_coordinate_roundtrip_exact"]:
    raise SystemExit("V91 source binding/roundtrip moved")
if not any(TARGET):
    raise SystemExit("target unexpectedly zero")

# Independently retain the V89 proper-Brauer image witness.
t = v89["e3_transport"]
if t["retained_at_mod2_quotient_coordinate_f2"] != TARGET or not t["solution_unique"]:
    raise SystemExit("V89 target bridge moved")
if t["proper14_mask_decimal"] != 20 or t["proper14_support_one_based"] != [3, 5]:
    raise SystemExit("V89 proper14 image moved")

checks = cert["input_type_checks"]
if checks["v91_object_type"] != bind["object_type"]:
    raise SystemExit("V91A type witness mismatch")
if checks["retained_at_mod2_quotient_coordinate_f2"] != TARGET:
    raise SystemExit("V91A target witness mismatch")
if checks["retained_at_mod2_quotient_support_one_based"] != [1, 8, 10]:
    raise SystemExit("V91A support witness mismatch")
if checks["proper14_mask_decimal"] != 20 or checks["proper14_support_one_based"] != [3, 5]:
    raise SystemExit("V91A proper14 witness mismatch")
if not checks["e3_discriminant_class_nonzero"]:
    raise SystemExit("V91A nonzero witness lost")

# The source-bound 64-dimensional marking is a known-class Picard basis, but
# its dual-functional coordinates must not be reinterpreted as divisor coefficients.
if source["basis_from"] != "upstream primitive INDLIST known-class basis":
    raise SystemExit("marked source semantics moved")
if len(source["indlist_1based"]) != 64 or len(set(source["indlist_1based"])) != 64:
    raise SystemExit("marked INDLIST basis moved")
dist = cert["literal_geometry_distinction"]
for key in (
    "marked_indlist_basis_generators_are_source_bound_known_curve_or_exceptional_divisor_classes",
    "dual_numerator_coordinates_are_not_integral_divisor_coefficients",
    "smith_support_1_8_10_are_not_literal_indlist_divisor_labels",
    "integral_divisor_relations_may_still_participate_in_a_cech_or_gysin_seed",
    "no_claim_that_all_divisor_based_cech_constructions_are_impossible",
):
    if not dist[key]:
        raise SystemExit(f"V91A distinction firewall moved: {key}")

# Exact type argument: Pic is the zero subgroup in its own quotient Pic^vee/Pic.
arg = cert["exact_argument"]
if arg["ambient_quotient"] != "A_Pic = Pic^vee / Pic":
    raise SystemExit("V91A quotient definition moved")
if "zero image" not in arg["integral_picard_divisor_image"]:
    raise SystemExit("V91A integral-divisor quotient fact moved")
if not arg["type_obstruction_not_repository_absence"]:
    raise SystemExit("V91A must remain a type obstruction, not an absence claim")
if cert["route_decision"]["literal_integral_divisor_as_same_discriminant_class"] != "BLOCKED_BY_NONZERO_DISCRIMINANT_QUOTIENT_TYPE":
    raise SystemExit("V91A blocked branch moved")

# V88 still leaves two literal seed shapes open; V91A closes neither.
accepted = v88["v88_construction_contract"]["accepted_seed_types"]
if len(accepted) != 2 or not accepted[0].startswith("BRANCH_GYSIN_SEED:") or not accepted[1].startswith("GENERAL_CECH_SEED:"):
    raise SystemExit("V88 accepted seed contract moved")
route = cert["route_decision"]
if route["direct_source_bound_cech_kummer_datum"] != "LIVE_UNMATERIALIZED":
    raise SystemExit("direct Cech/Kummer route must remain live")
if route["accepted_live_seed_types_from_v88"] != [
    "BRANCH_GYSIN_SEED_WITH_CONCRETE_SUPPORT_AND_KUMMER_FUNCTION",
    "GENERAL_CECH_SEED_WITH_EXPLICIT_SOURCE_BOUND_TRANSITION_DATA",
]:
    raise SystemExit("V91A live seed summary moved")

cons = cert["exact_consequence"]
if not cons["literal_integral_picard_divisor_representative_branch_closed"]:
    raise SystemExit("V91A type-obstruction conclusion moved")
for key in (
    "literal_picard_divisor_materialized",
    "literal_kummer_function_materialized",
    "literal_cech_seed_materialized",
    "complete_residue_audit_materialized",
    "genuine_full_surface_h2_mu2_lift_for_e3",
    "global_h2_mu2_nonexistence_claim",
):
    if cons[key]:
        raise SystemExit(f"V91A credit firewall violated: {key}")

f = cert["credit_firewall"]
if f["stage33_progress"] != "6/11":
    raise SystemExit("Stage33 progress moved")
for key in (
    "stage33_12_closed_exact", "stage33_13_released", "receiver_credit",
    "theorem_credit", "endpoint_credit", "merge_allowed",
):
    if f[key]:
        raise SystemExit(f"V91A credit firewall violated: {key}")

if cert["next_exact_leaf"] != "V91B_CONSTRUCT_SOURCE_BOUND_DIRECT_CECH_KUMMER_DATUM_FOR_E3_MASK20":
    raise SystemExit("V91A successor moved")
if cert["status"] != "PASS_EXACT_V91A_INTEGRAL_DIVISOR_AS_SAME_DISCRIMINANT_CLASS_BLOCKED_DIRECT_CECH_KUMMER_REMAINS_OPEN":
    raise SystemExit("V91A status moved")

print(json.dumps({
    "success": True,
    "marker": "V91A_E3_LITERAL_INTEGRAL_DIVISOR_TYPE_OBSTRUCTION_COMPLETE",
    "certificate_sha256": CERT_SHA,
    "proper14_mask_decimal": 20,
    "retained_support_one_based": [1, 8, 10],
    "integral_divisor_same_class_branch": "BLOCKED_BY_TYPE",
    "direct_cech_kummer_route": "LIVE_UNMATERIALIZED",
    "stage33_progress": "6/11",
    "merge_allowed": False,
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
