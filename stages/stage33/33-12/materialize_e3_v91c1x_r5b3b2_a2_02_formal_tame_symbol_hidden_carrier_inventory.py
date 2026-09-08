#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
B3A = HERE / "e3-v91c1x-r5b3a-a2-02-317-1757-literal-package-pullbacks.json"
B3B1 = HERE / "e3-v91c1x-r5b3b1-a2-02-317-1757-boundary-uniformizers.json"
BF = HERE / "boundary-function-generator-source-lock.json"
V1D = HERE / "e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
V1D_VERIFY = HERE / "verify_e3_v91c1d_a2_02_purity_cech_cartier_assembly.py"
UNI_PRODUCER = S07 / "certify_72_boundary_weak_approximation_uniformizers.py"
OUT = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"

B3A_SHA = "b694cd2aee502e13186cbe68e65ddce7a845e54e546c8cf548c1386ac5a71d31"
B3B1_SHA = "8a5dcb751b312a846a06fac88298166efe8c1fd91ed0988b3cb04a408cfc2654"
BF_SHA = "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96"
V1D_SHA = "fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
V1D_VERIFY_BLOB_SHA1 = "21827a085c0f3039ab3cd6786483de4bb13d5db9"
UNI_PRODUCER_BLOB_SHA1 = "b108921184eb45dbd416035839371984bd6ef738"
SOURCE = "A2_02"
COMPONENTS = ["EXC_003", "EXC_004", "EXC_011", "EXC_012", "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path.name}")
    return obj


def projective_key(coeffs):
    vals = [atlas.decode_element(z) for z in coeffs]
    pivot = next((q for q in vals if q != 0), None)
    if pivot is None:
        raise SystemExit("zero linear factor")
    enc = [atlas.encode_element(atlas.clean(q / pivot)) for q in vals]
    return csha(enc), enc


def add_carrier(carriers, coeffs, component, member, role, exponent):
    key, normalized = projective_key(coeffs)
    if key not in carriers:
        carriers[key] = {
            "carrier_id": f"LIN_{len(carriers)+1:03d}",
            "projective_linear_form_Qi_sha256": key,
            "normalized_coefficients_Qi": normalized,
            "appearances": [],
        }
    carriers[key]["appearances"].append({
        "symbol_component": component,
        "member": member,
        "role": role,
        "exponent": int(exponent),
    })
    return key


def build_certificate():
    b3a = load(B3A, B3A_SHA)
    b3b1 = load(B3B1, B3B1_SHA)
    bf = load(BF, BF_SHA)
    v1d = load(V1D, V1D_SHA)
    if blob_sha(V1D_VERIFY.read_bytes()) != V1D_VERIFY_BLOB_SHA1:
        raise SystemExit("V91C1D verifier blob moved")
    if blob_sha(UNI_PRODUCER.read_bytes()) != UNI_PRODUCER_BLOB_SHA1:
        raise SystemExit("boundary uniformizer producer blob moved")

    verifier = V1D_VERIFY.read_text(encoding="utf-8")
    producer = UNI_PRODUCER.read_text(encoding="utf-8")
    if 'p["offboundary_height_one_residue_discrepancy"]=="ZERO_EXACT"' not in verifier:
        raise SystemExit("V91C1D ZERO_EXACT assertion moved")
    if "squareclass" in verifier.lower():
        raise SystemExit("V91C1D verifier gained squareclass replay; diagnostic must be revisited")
    disclaimer = "This leaf does not compute their squareclasses on those primes and gives no Gersten lift credit."
    if disclaimer not in producer:
        raise SystemExit("uniformizer producer disclaimer moved")

    if b3a["a2_02_source"]["component_ids_in_source_order"] != COMPONENTS:
        raise SystemExit("R5B3A component order moved")
    if b3b1["a2_02_uniformizers"]["component_ids_in_source_order"] != COMPONENTS:
        raise SystemExit("R5B3B1 component order moved")
    source = next(r for r in bf["generator_records"] if r["source_direction"] == SOURCE)
    packages = source["component_packages"]
    if [r["component_id"] for r in packages] != COMPONENTS:
        raise SystemExit("source package order moved")

    arows = {r["component_id"]: r for r in b3a["a2_02_source"]["package_rows"]}
    urows = {r["component_id"]: r for r in b3b1["a2_02_uniformizers"]["uniformizer_rows"]}
    pairs = {r["component_id"]: r for r in b3b1["a2_02_uniformizers"]["paired_residue_function_uniformizer_rows"]}
    package_map = {r["component_id"]: r for r in packages}

    carriers = {}
    terms = []
    supports = []
    for component in COMPONENTS:
        urow = urows[component]
        arow = arows[component]
        pair = pairs[component]
        package = package_map[component]
        fac = urow["source_uniformizer"]["exact_factorized_ambient_rational_function_Qi"]
        pi_keys = []
        f_keys = []
        for coeffs in fac["numerator_linear_factors_Qi"]:
            pi_keys.append(add_carrier(carriers, coeffs, component, "pi_D", "NUMERATOR", 1))
        for coeffs in fac["denominator_linear_factors_Qi"]:
            pi_keys.append(add_carrier(carriers, coeffs, component, "pi_D", "DENOMINATOR", -1))
        for factor in package["numerator_factors"]:
            exp = int(factor.get("exponent", 1))
            f_keys.append(add_carrier(carriers, factor["coefficients_Qi"], component, "f_D", "NUMERATOR", exp))
        dexp = int(package["denominator"]["exponent"])
        f_keys.append(add_carrier(carriers, package["denominator"]["coefficients_Qi"], component, "f_D", "DENOMINATOR", -dexp))

        if pair["residue_function_Qi_sha256"] != arow["source_literal_package"]["ambient_rational_function_Qi_sha256"]:
            raise SystemExit(f"residue-function pair lock moved: {component}")
        if pair["boundary_uniformizer_factorized_Qi_sha256"] != urow["source_uniformizer"]["exact_factorized_ambient_rational_function_Qi_sha256"]:
            raise SystemExit(f"uniformizer pair lock moved: {component}")

        terms.append({
            "component_id": component,
            "symbol": "[pi_D,f_D]_2",
            "uniformizer_factorized_Qi_sha256": pair["boundary_uniformizer_factorized_Qi_sha256"],
            "residue_function_Qi_sha256": pair["residue_function_Qi_sha256"],
            "semantics": "EXACT_FORMAL_BRAUER_2_SYMBOL_TERM_NOT_YET_CERTIFIED_UNRAMIFIED",
        })
        supports.append({
            "component_id": component,
            "pi_D_linear_carriers": sorted(set(pi_keys)),
            "f_D_linear_carriers": sorted(set(f_keys)),
            "candidate_nonexceptional_residue_support_is_contained_in_pullbacks_of_these_linear_hyperplane_carriers": True,
        })

    carrier_rows = sorted(carriers.values(), key=lambda r: r["carrier_id"])
    for row in carrier_rows:
        row["appearances"] = sorted(row["appearances"], key=lambda x: (x["symbol_component"], x["member"], x["role"], x["exponent"]))
        row["appears_in_pi_D"] = any(x["member"] == "pi_D" for x in row["appearances"])
        row["appears_in_f_D"] = any(x["member"] == "f_D" for x in row["appearances"])
    pi_rows = [r for r in carrier_rows if r["appears_in_pi_D"]]
    f_rows = [r for r in carrier_rows if r["appears_in_f_D"]]
    shared_rows = [r for r in carrier_rows if r["appears_in_pi_D"] and r["appears_in_f_D"]]

    if b3b1["construction_status"]["offboundary_codimension_one_residue_cancellation_verified"] is not False:
        raise SystemExit("R5B3B1 offboundary firewall moved")
    if v1d["purity_cartier"]["offboundary_height_one_residue_discrepancy"] != "ZERO_EXACT":
        raise SystemExit("V91C1D recorded ZERO_EXACT moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b2.a2_02_formal_tame_symbol_hidden_carrier_inventory.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B2_A2_02_FORMAL_TAME_SYMBOL_SUM_AND_HIDDEN_LINEAR_CARRIER_INVENTORY",
        "role": "EXACT_NONCREDIT_R5B3B2_FORMAL_EIGHT_SYMBOL_ASSEMBLY_WITH_FINITE_LINEAR_SUPPORT_INVENTORY_AND_V91C1D_REUSE_GAP_DIAGNOSIS",
        "entry": {"pr": 1695, "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT", "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3a_literal_package_pullbacks_sha256": B3A_SHA,
            "r5b3b1_boundary_uniformizers_sha256": B3B1_SHA,
            "boundary_function_generator_source_lock_sha256": BF_SHA,
            "v91c1d_purity_cech_cartier_sha256": V1D_SHA,
            "v91c1d_verifier_blob_sha1": V1D_VERIFY_BLOB_SHA1,
            "boundary_uniformizer_producer_blob_sha1": UNI_PRODUCER_BLOB_SHA1,
        },
        "formal_tame_symbol_sum": {
            "source_direction": SOURCE,
            "term_count": 8,
            "component_ids_in_source_order": COMPONENTS,
            "terms": terms,
            "formal_sum_expression": "SUM_D [pi_D,f_D]_2 FOR D IN A2_02_EIGHT_COMPONENTS",
            "formal_symbol_sum_materialized": True,
            "certified_as_unramified_global_brauer_or_kummer_representative": False,
        },
        "finite_linear_carrier_inventory": {
            "per_symbol_support_rows": supports,
            "unique_projective_linear_carrier_count": len(carrier_rows),
            "uniformizer_pi_unique_linear_carrier_count": len(pi_rows),
            "residue_function_f_unique_linear_carrier_count": len(f_rows),
            "pi_and_f_shared_linear_carrier_count": len(shared_rows),
            "carrier_rows": carrier_rows,
            "all_candidate_nonexceptional_residue_support_is_reduced_to_a_finite_projective_Qi_linear_hyperplane_carrier_inventory": True,
            "exceptional_divisor_orders_already_replayed_by_r5b3b1": True,
            "prime_decomposition_of_every_linear_carrier_on_the_resolved_surface_materialized": False,
            "combined_residue_squareclass_on_every_prime_above_the_carriers_materialized": False,
        },
        "v91c1d_reuse_audit": {
            "recorded_offboundary_height_one_residue_discrepancy": "ZERO_EXACT",
            "v91c1d_verifier_contains_no_squareclass_computation_path": True,
            "v91c1d_verifier_replays_residue_field_squareclasses_for_the_later_r5b3b1_uniformizers": False,
            "boundary_uniformizer_producer_explicitly_disclaims_squareclass_and_gersten_lift_credit": True,
            "v91c1d_zero_exact_label_is_not_a_source_bound_all_codimension_one_residue_witness_for_the_new_symbol_sum": True,
        },
        "construction_status": {
            "eight_term_formal_tame_symbol_sum_assembled": True,
            "finite_linear_carrier_support_inventory_materialized": True,
            "all_linear_hyperplane_carriers_prime_decomposed_on_the_resolved_surface": False,
            "combined_residue_field_squareclass_computed_on_every_prime_above_each_carrier": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "single_global_a2_02_kummer_or_brauer_representative_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "same_representative_swap23_transport_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
        },
        "exact_consequence": {
            "the_candidate_is_now_an_exact_eight_term_formal_symbol_sum_not_merely_eight_unpaired_inputs": True,
            "possible_nonexceptional_residue_support_is_bounded_by_an_explicit_finite_linear_carrier_inventory": True,
            "the_remaining_global_gersten_gap_is_not_closed_by_the_old_v91c1d_zero_exact_label": True,
            "next_computation_is_finite_prime_decomposition_plus_combined_residue_squareclasses_on_the_inventory": True,
        },
        "next_missing_object": "PRIME_DECOMPOSITION_ON_THE_RESOLVED_SURFACE_OF_EACH_DISTINCT_LINEAR_HYPERPLANE_CARRIER_IN_THE_EIGHT_SYMBOL_TERMS_THEN_EXACT_COMBINED_TAME_RESIDUE_SQUARECLASS_ON_EVERY_PRIME_ABOVE_THEM",
        "next_exact_leaf": "V91C1X_R5B3B3_DECOMPOSE_LINEAR_CARRIERS_AND_AUDIT_COMBINED_TAME_RESIDUES",
        "credit_firewall": {
            "authority_promotion": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "hostile_audit_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    inv = cert["finite_linear_carrier_inventory"]
    print(json.dumps({
        "success": True,
        "candidate": cert["candidate"],
        "canonical_sha256": cert["canonical_sha256"],
        "formal_symbol_term_count": cert["formal_tame_symbol_sum"]["term_count"],
        "unique_projective_linear_carrier_count": inv["unique_projective_linear_carrier_count"],
        "uniformizer_pi_unique_linear_carrier_count": inv["uniformizer_pi_unique_linear_carrier_count"],
        "residue_function_f_unique_linear_carrier_count": inv["residue_function_f_unique_linear_carrier_count"],
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
