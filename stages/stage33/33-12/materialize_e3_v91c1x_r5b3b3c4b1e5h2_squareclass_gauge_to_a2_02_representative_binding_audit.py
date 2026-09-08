#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
H1 = HERE / "e3-v91c1x-r5b3b3c4b1e5h1-stable-square-transition-rees-unit-attachment.json"
B3A = HERE / "e3-v91c1x-r5b3a-a2-02-317-1757-literal-package-pullbacks.json"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
V1D = HERE / "e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
V1D_VERIFY = HERE / "verify_e3_v91c1d_a2_02_purity_cech_cartier_assembly.py"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5h2-squareclass-gauge-to-a2-02-representative-binding-audit.json"

H1_SHA = "8ac2745d2847896cc5b32ea91e9f14bbe62aa91d32be74acd57b598366e77a88"
B3A_SHA = "b694cd2aee502e13186cbe68e65ddce7a845e54e546c8cf548c1386ac5a71d31"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
V1D_SHA = "fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
V1D_VERIFY_BLOB_SHA1 = "21827a085c0f3039ab3cd6786483de4bb13d5db9"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
NEXT = "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def build_certificate() -> dict:
    h1 = load_locked(H1, H1_SHA)
    b3a = load_locked(B3A, B3A_SHA)
    b3b2 = load_locked(B3B2, B3B2_SHA)
    v1d = load_locked(V1D, V1D_SHA)
    if blob_sha(V1D_VERIFY.read_bytes()) != V1D_VERIFY_BLOB_SHA1:
        raise SystemExit("V91C1D verifier blob moved")
    verifier_text = V1D_VERIFY.read_text(encoding="utf-8")

    ha = h1["stable_square_transition_rees_unit_attachment"]
    if not ha["all_13_transitions_are_nonzero_Qi_constants"]:
        raise SystemExit("H1 no longer has 13 constant transitions")
    if ha["nonzero_Qi_constant_transition_piece_count"] != 468:
        raise SystemExit("H1 468-piece gauge-unit count moved")
    if h1["coverage_accounting"]["genuine_pole_line_action_unit_piece_count_remains"] != 173:
        raise SystemExit("H1 pole-line firewall moved")

    b3a_status = b3a["construction_status"]
    if b3a_status["single_global_a2_02_kummer_representative_assembled_from_the_eight_component_packages"]:
        raise SystemExit("B3A global Kummer representative unexpectedly materialized")
    if b3a_status["same_representative_swap23_transport_materialized"]:
        raise SystemExit("B3A same-representative transport unexpectedly materialized")

    b3b2_status = b3b2["construction_status"]
    required_false = [
        "all_linear_hyperplane_carriers_prime_decomposed_on_the_resolved_surface",
        "combined_residue_field_squareclass_computed_on_every_prime_above_each_carrier",
        "offboundary_codimension_one_residue_cancellation_verified",
        "single_global_a2_02_kummer_or_brauer_representative_materialized",
        "same_representative_swap23_transport_materialized",
    ]
    for key in required_false:
        if b3b2_status[key] is not False:
            raise SystemExit(f"B3B2 prerequisite unexpectedly closed: {key}")

    reuse = b3b2["v91c1d_reuse_audit"]
    if not reuse["v91c1d_verifier_contains_no_squareclass_computation_path"]:
        raise SystemExit("B3B2 V91C1D squareclass-replay diagnosis moved")
    if not reuse["v91c1d_zero_exact_label_is_not_a_source_bound_all_codimension_one_residue_witness_for_the_new_symbol_sum"]:
        raise SystemExit("B3B2 V91C1D reuse firewall moved")
    if "squareclass" in verifier_text.lower():
        raise SystemExit("V91C1D verifier gained a squareclass path; H2 audit must be redone")

    v1d_exact = v1d["exact_consequence"]
    if not v1d_exact["a2_02_full_surface_cech_cartier_seed_assembly_materialized"]:
        raise SystemExit("V91C1D seed assembly moved")
    if v1d_exact["genuine_full_surface_h2_mu2_lift_for_e3"]:
        raise SystemExit("V91C1D unexpectedly gained genuine H2 lift credit")

    bridge_available = (
        b3a_status["single_global_a2_02_kummer_representative_assembled_from_the_eight_component_packages"]
        and b3b2_status["combined_residue_field_squareclass_computed_on_every_prime_above_each_carrier"]
        and b3b2_status["offboundary_codimension_one_residue_cancellation_verified"]
        and b3b2_status["single_global_a2_02_kummer_or_brauer_representative_materialized"]
        and b3b2_status["same_representative_swap23_transport_materialized"]
    )
    if bridge_available:
        raise SystemExit("H2 expected a negative bridge checkpoint but prerequisites now close")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5h2.squareclass_gauge_to_a2_02_representative_binding_audit.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5H2_SQUARECLASS_GAUGE_TO_A2_02_REPRESENTATIVE_BINDING_AUDIT",
        "role": "EXACT_NONCREDIT_NEGATIVE_BRIDGE_CHECKPOINT_PREVENTING_THE_468_H1_SQUARECLASS_GAUGE_UNITS_FROM_BEING_RELABELED_AS_ACTUAL_A2_02_SAME_REPRESENTATIVE_POLE_LINE_ACTION_UNITS",
        "entry": {"authority": AUTHORITY, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "c4b1e5h1_sha256": H1_SHA,
            "r5b3a_sha256": B3A_SHA,
            "r5b3b2_sha256": B3B2_SHA,
            "v91c1d_sha256": V1D_SHA,
            "v91c1d_verifier_blob_sha1": V1D_VERIFY_BLOB_SHA1,
        },
        "bridge_audit": {
            "h1_regular_invertible_squareclass_gauge_piece_count": 468,
            "h1_actual_a2_02_pole_line_piece_credit": 0,
            "b3a_has_all_eight_literal_packages_on_1757_pieces": True,
            "b3a_has_single_global_a2_02_kummer_representative": False,
            "b3b2_has_exact_eight_term_formal_symbol_sum": True,
            "b3b2_has_all_carrier_prime_decompositions": False,
            "b3b2_has_combined_residue_squareclass_on_every_prime": False,
            "b3b2_has_offboundary_codimension_one_cancellation": False,
            "b3b2_has_single_global_a2_02_kummer_or_brauer_representative": False,
            "v91c1d_has_legacy_full_surface_cech_cartier_seed": True,
            "v91c1d_verifier_replays_new_symbol_sum_residue_squareclasses": False,
            "v91c1d_zero_exact_is_source_bound_witness_for_new_symbol_sum": False,
            "exact_bridge_from_h1_squareclass_gauge_to_actual_a2_02_same_representative": False,
        },
        "coverage_accounting": {
            "genuine_pole_line_action_unit_piece_count_remains": 173,
            "regular_squareclass_gauge_piece_count_held_behind_binding_firewall": 468,
            "remaining_exceptional_pole_line_same_representative_debt_piece_count_remains": 1584,
        },
        "exact_consequence": {
            "the_468_h1_units_are_real_regular_units_but_only_for_the_c4b1_residue_squareclass_gauge": True,
            "promoting_the_468_to_a2_02_pole_line_same_representative_action_units_would_be_unsupported": True,
            "legacy_v91c1d_zero_exact_cannot_close_the_missing_new_symbol_sum_squareclass_replay": True,
            "strict_prime_cross_carrier_incidence_and_residue_field_squareclasses_are_a_required_next_input": True,
            "h2_fixedness_verified": False,
        },
        "next_exact_leaf": NEXT,
        "next_exact_step": "materialize strict-prime decomposition/cross-carrier incidence and exact combined residue-field squareclasses for the B3B2 finite linear-carrier inventory; use that to decide offboundary cancellation before attempting a source-bound single A2-02 representative binding",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "source_bound_single_representative_credit": False,
            "whole_cover_ell_ij_credit": False,
            "whole_cover_r_ij_credit": False,
            "literal_mu2_2_cocycle_credit": False,
            "exceptional_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "bridge_available": cert["bridge_audit"]["exact_bridge_from_h1_squareclass_gauge_to_actual_a2_02_same_representative"],
            "held_gauge_pieces": cert["coverage_accounting"]["regular_squareclass_gauge_piece_count_held_behind_binding_firewall"],
            "pole_line_coverage_remains": cert["coverage_accounting"]["genuine_pole_line_action_unit_piece_count_remains"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E5H2 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
