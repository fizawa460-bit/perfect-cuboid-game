#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas

HERE = Path(__file__).resolve().parent
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
E5H = HERE / "e3-v91c1x-r5b3b3c4b1e5h-square17-swap23-square-root-transition-preflight.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5h1-stable-square-transition-rees-unit-attachment.json"

D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
E5H_SHA = "eb719b7efecd3503ce40c1064bde6f0347d7229780629053dead63d72f0f7c21"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I


def clean(x: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.expand(x))


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def decode_rational(obj: dict, t: sp.Symbol) -> sp.Expr:
    num = atlas.decode_poly(obj["numerator"], [t])
    den = atlas.decode_poly(obj["denominator"], [t])
    if den == 0:
        raise SystemExit("encoded transition denominator is zero")
    return clean(num / den)


def build_certificate() -> dict:
    d2 = load_locked(D2, D2_SHA)
    e5h = load_locked(E5H, E5H_SHA)

    pre = e5h["square17_transition_preflight"]
    if pre["source_block_count"] != 17:
        raise SystemExit("E5H square17 source count moved")
    if pre["function_field_square_root_transition_materialized_source_block_count"] != 13:
        raise SystemExit("E5H stable source count moved")
    if pre["function_field_square_root_transition_materialized_piece_count_before_cartier_attachment"] != 468:
        raise SystemExit("E5H stable piece count moved")
    if e5h["coverage_accounting"]["genuine_pole_line_action_unit_piece_count_remains"] != 173:
        raise SystemExit("E5H pole-line firewall boundary moved")

    d2_rows = {
        row["source_node"]: row
        for row in d2["exceptional_common_refinement"]["node_rows"]
    }
    stable = [
        row for row in pre["rows"]
        if row["same_representative_function_field_square_root_transition_materialized"]
    ]
    if len(stable) != 13:
        raise SystemExit("E5H stable row count moved")
    stable_by_source = {row["source_exceptional_id"]: row for row in stable}
    if len(stable_by_source) != 13:
        raise SystemExit("duplicate E5H stable source")

    t = sp.Symbol("t")
    rows = []
    constant_source_count = 0
    constant_piece_count = 0
    nonconstant_sources = []
    constants: dict[str, sp.Expr] = {}

    for row in sorted(stable, key=lambda r: r["source_exceptional_id"]):
        source = row["source_exceptional_id"]
        target = row["target_exceptional_id"]
        d2row = d2_rows[source]
        if d2row["acted_target_node"] != target:
            raise SystemExit(f"D2 target moved for {source}")
        if d2row["common_refinement_piece_count"] != 36:
            raise SystemExit(f"D2 piece count moved for {source}")
        if d2row["36_piece_descriptors_sha256"] != row["d2_36_piece_descriptors_sha256"]:
            raise SystemExit(f"D2 piece commitment moved for {source}")

        transition = decode_rational(row["explicit_square_root_transition_Qi_t"], t)
        if transition == 0:
            raise SystemExit(f"zero square-root transition at {source}")
        num, den = sp.fraction(transition)
        num_degree = int(sp.Poly(num, t, extension=I).degree())
        den_degree = int(sp.Poly(den, t, extension=I).degree())
        is_constant = (not transition.has(t))
        if is_constant:
            constant_source_count += 1
            constant_piece_count += 36
            constants[source] = transition
        else:
            nonconstant_sources.append(source)

        rows.append({
            "source_exceptional_id": source,
            "target_exceptional_id": target,
            "d2_piece_count": 36,
            "d2_36_piece_descriptors_sha256": row["d2_36_piece_descriptors_sha256"],
            "transition_Qi_t_sha256": row["explicit_square_root_transition_Qi_t_sha256"],
            "reduced_numerator_degree_t": num_degree,
            "reduced_denominator_degree_t": den_degree,
            "transition_is_nonzero_Qi_constant": is_constant,
            "regular_invertible_on_source_Rees_chart_before_any_localization": is_constant,
            "regular_invertible_on_all_36_D2_common_refinement_pieces": is_constant,
            "attachment_kind": (
                "GLOBAL_NONZERO_QI_CONSTANT_UNIT_PULLS_BACK_TO_EVERY_D2_REES_PIECE"
                if is_constant else
                "NONCONSTANT_FUNCTION_FIELD_UNIT_REQUIRES_EXPLICIT_REES_DIVISOR_LOCALIZATION_TEST"
            ),
        })

    involution_checks = []
    for source in sorted(constants):
        target = stable_by_source[source]["target_exceptional_id"]
        if target not in constants:
            raise SystemExit(f"constant stable source target lacks reverse stable row: {source}->{target}")
        product = clean(constants[source] * constants[target])
        ok = product == 1
        if not ok:
            raise SystemExit(f"constant transition involution failed: {source}<->{target}: {product}")
        involution_checks.append({
            "source_exceptional_id": source,
            "target_exceptional_id": target,
            "forward_times_reverse_constant_equals_one_exact": True,
        })

    all_constant = constant_source_count == 13
    if all_constant and constant_piece_count != 468:
        raise SystemExit("E5H1 expected 468 constant-unit pieces")

    if all_constant:
        next_leaf = "V91C1X_R5B3B3C4B1E5H2_SQUARECLASS_GAUGE_TO_A2_02_ACTUAL_PACKAGE_REPRESENTATIVE_BINDING"
        next_step = (
            "bind these 13 source-bound nonzero-constant square-root gauge transitions back to the actual A2-02 package/line representative; "
            "only after that bridge may any of the 468 pieces be counted as genuine pole-line same-representative action transport"
        )
    else:
        next_leaf = "V91C1X_R5B3B3C4B1E5H1A_NONCONSTANT_STABLE_SQUARE_REES_DIVISOR_LOCALIZATION"
        next_step = (
            "for each nonconstant stable-square transition, homogenize its numerator and denominator in the source exceptional tangent coordinates and test whether their divisors are removed by the D2 piece localizers"
        )

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5h1.stable_square_transition_rees_unit_attachment.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5H1_STABLE_SQUARE_TRANSITION_REES_UNIT_ATTACHMENT",
        "role": "EXACT_NONCREDIT_REGULAR_UNIT_ATTACHMENT_TEST_FOR_THE_13_E5H_FUNCTION_FIELD_SQUARE_ROOT_TRANSITIONS_WITH_STRICT_FIREWALL_AGAINST_RELABELLING_THEM_AS_A2_02_POLE_LINE_ACTION_UNITS",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "r5b2d2_sha256": D2_SHA,
            "c4b1e5h_sha256": E5H_SHA,
        },
        "stable_square_transition_rees_unit_attachment": {
            "tested_source_block_count": 13,
            "tested_piece_count": 468,
            "nonzero_Qi_constant_transition_source_block_count": constant_source_count,
            "nonzero_Qi_constant_transition_piece_count": constant_piece_count,
            "nonconstant_transition_source_blocks": nonconstant_sources,
            "all_13_transitions_are_nonzero_Qi_constants": all_constant,
            "all_468_D2_pieces_have_regular_invertible_squareclass_gauge_transition": all_constant,
            "rows": rows,
            "constant_transition_involution_checks": involution_checks,
        },
        "coverage_accounting": {
            "genuine_pole_line_action_unit_piece_count_remains": 173,
            "new_regular_invertible_squareclass_gauge_piece_count": constant_piece_count,
            "these_468_are_not_added_to_pole_line_coverage_without_A2_02_representative_binding": True,
            "remaining_exceptional_pole_line_same_representative_debt_piece_count_remains": 1584,
        },
        "exact_consequence": {
            "squareclass_gauge_transition_regular_invertibility_is_exact_on_all_constant_rows": True,
            "nonzero_constant_units_need_no_additional_Rees_Cartier_localization": True,
            "this_is_not_yet_an_A2_02_line_representative_action_unit": True,
            "this_does_not_assemble_the_eight_A2_02_packages_into_one_global_Kummer_or_Cech_representative": True,
            "whole_cover_ell_ij_materialized": False,
            "whole_cover_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_is_now_exact_if_all_constant": "all 13 target-stable square/trivial source blocks carry an explicit source-bound nonzero Q(i)-constant square-root gauge transition, hence a regular invertible gauge unit on each of their 36 D2 common-refinement pieces",
            "what_is_still_missing": "an exact bridge from the C4B1 residue squareclass gauge to the actual A2-02 package/line representative; without that bridge the 468 pieces cannot receive E5D-style pole-line same-representative action-unit credit",
        },
        "next_exact_leaf": next_leaf,
        "next_exact_step": next_step,
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
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
            "source_bound_dim5_credit": False,
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
        a = cert["stable_square_transition_rees_unit_attachment"]
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "constant_source_blocks": a["nonzero_Qi_constant_transition_source_block_count"],
            "constant_unit_pieces": a["nonzero_Qi_constant_transition_piece_count"],
            "nonconstant_sources": a["nonconstant_transition_source_blocks"],
            "pole_line_coverage_remains": cert["coverage_accounting"]["genuine_pole_line_action_unit_piece_count_remains"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E5H1 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
