#!/usr/bin/env python3
"""Certify the exact information boundary after the 26 purity lifts exist.

Purity/Gersten exactness proves that every one of the 26 prescribed boundary
tuples has at least one global geometric preimage.  It does not choose a
Galois-equivariant section of those nonempty fibres, nor does it provide the
cc/ct differences between chosen lifts.  The independently checked endpoint
module calculation classifies the still-unfixed finite V4 extension datum as

    Ext^1_F2[V4](F2^26, Br(Sbar)[2]) ~= F2^416.

This certificate joins those two exact facts without promoting the abstract
endpoint-compatible extensions to geometrically realised ones.  Its positive
claim is an information claim: the locked purity output supplies no datum that
selects an entry of the 16 x 26 connecting matrix.  A genuine equivariant
middle module, equivariant section, or the 26 cc/ct lift-difference cocycles is
still required.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PURITY = HERE / "mixed-order-global-gersten-lift-existence-by-purity.json"
AMBIGUITY = HERE / "order2-ambient-extension-ambiguity.json"
OUTPUT = HERE / "post-purity-gersten-torsor-ambiguity.json"

EXPECTED_PURITY = "c97cf3df4c69bc859765b6844dc12e1ad24bdf0da0457446f1e5e11846c6660a"
EXPECTED_AMBIGUITY = "428b980afb01ca1a84c4657cb6d1e278d0c1ddf777a157a4e58b426a269cbdbb"


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.pop("canonical_sha256", None)
    actual = canonical_sha256(obj)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock failed for {path.name}")
    obj["canonical_sha256"] = claimed
    return obj


def main():
    purity = load_locked(PURITY, EXPECTED_PURITY)
    ambiguity = load_locked(AMBIGUITY, EXPECTED_AMBIGUITY)

    counts = purity["exact_counts"]
    progress = purity["constructive_progress"]
    classification = ambiguity["extension_classification"]
    exhaustive = ambiguity["exhaustive_basis_adapter_check"]
    consequence = ambiguity["exact_consequence"]

    if counts["source_count"] != 26:
        raise SystemExit("purity source count regression")
    if progress["global_geometric_Gersten_lift_existence_certified_count"] != 26:
        raise SystemExit("global Gersten existence regression")
    if progress["global_geometric_Gersten_explicit_representatives_materialized_count"] != 0:
        raise SystemExit("unexpected explicit representative promotion")
    if classification["connecting_matrix_shape"] != [16, 26]:
        raise SystemExit("connecting matrix shape regression")
    if classification["extension_equivalence_space_dimension_f2"] != 416:
        raise SystemExit("extension ambiguity dimension regression")
    if exhaustive["elementary_extensions_checked"] != 416:
        raise SystemExit("elementary extension census regression")
    if not exhaustive["all_416_elementary_16x26_matrices_recovered_exactly"]:
        raise SystemExit("elementary extension adapter check incomplete")
    if consequence["endpoint_dimensions_and_v4_actions_determine_any_delta_loc_entry"]:
        raise SystemExit("endpoint data unexpectedly determine delta_loc")

    certificate = {
        "schema": "STAGE33_07_POST_PURITY_GERSTEN_TORSOR_AMBIGUITY_V1",
        "source_locks": {
            "gersten_existence_by_purity_sha256": EXPECTED_PURITY,
            "ambient_extension_ambiguity_sha256": EXPECTED_AMBIGUITY,
        },
        "locked_positive_prefix": {
            "global_geometric_Gersten_lift_existence_certified": 26,
            "source_count": 26,
            "raw_order2_sources": 17,
            "raw_order4_sources": 9,
            "boundary_tuples_in_full_codimension2_Gersten_kernel": 26,
        },
        "exact_information_boundary": {
            "purity_proves_each_lift_fibre_nonempty": True,
            "purity_chooses_a_representative_in_each_fibre": False,
            "purity_supplies_a_galois_equivariant_section": False,
            "purity_supplies_cc_ct_differences_in_proper_Br2": False,
            "nonempty_fibres_alone_determine_any_connecting_matrix_entry": False,
            "endpoint_compatible_extension_space_dimension_f2": 416,
            "endpoint_compatible_extension_class_count": "2^416",
            "connecting_matrix_shape": [16, 26],
            "connecting_matrix_columns_materialized": 0,
            "geometric_realizability_of_all_abstract_extension_classes_claimed": False,
        },
        "independent_exact_checks": {
            "all_416_elementary_endpoint_compatible_extensions_recovered_by_adapter": True,
            "elementary_extension_aggregate_sha256": exhaustive[
                "elementary_test_aggregate_sha256"
            ],
            "purity_and_ambiguity_source_hashes_locked": True,
            "existence_data_do_not_contain_middle_module_actions_or_lift_differences": True,
        },
        "required_new_input": {
            "one_of": [
                "the genuine Galois-equivariant middle Gersten module",
                "a Galois-equivariant section of the 26 lift fibres",
                "the 26 cc/ct chosen-lift difference cocycles in proper Br(Sbar)[2] coordinates",
            ],
            "endpoint_dimensions_or_non-equivariant_existence_alone_suffice": False,
        },
        "project_status": {
            "finite_v4_delta_loc_matrix_computed": False,
            "project_14x26_L_squareclass_tensor_materialized": False,
            "actual_index512_glue_identified": False,
            "absolute_delta_loc_computed": False,
            "arithmetic_HS_closed": False,
            "stage33_progress": "6/11",
            "stage33_08_released": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "new_smallest_exact_kernel": "R33-BR2A-GENUINE-GALOIS-EQUIVARIANT-GERSTEN-MIDDLE-MODULE-OR-26-LIFT-DIFFERENCE-COCYCLES",
        "next_exact_leaf": "L33-07-MATERIALIZE-GALOIS-EQUIVARIANT-GERSTEN-MIDDLE-MODULE-OR-26-CC-CT-LIFT-DIFFERENCES",
    }
    certificate["canonical_sha256"] = canonical_sha256(certificate)
    OUTPUT.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "success": True,
        "global_Gersten_lift_existence": "26/26",
        "explicit_representatives": "0/26",
        "endpoint_compatible_extension_dimension_f2": 416,
        "connecting_matrix_columns_materialized": "0/26",
        "certificate_sha256": certificate["canonical_sha256"],
        "next": certificate["next_exact_leaf"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
