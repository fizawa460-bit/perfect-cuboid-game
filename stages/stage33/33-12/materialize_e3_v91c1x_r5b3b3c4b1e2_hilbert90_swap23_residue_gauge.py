#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b3c4b1d_swap23_tangent_pullback_comparison as c4b1d
import materialize_e3_v91c1x_r5b3b3c4b1e1_literal_swap23_orbit_difference_cocycle as e1

HERE = Path(__file__).resolve().parent
E1 = HERE / "e3-v91c1x-r5b3b3c4b1e1-literal-swap23-orbit-difference-cocycle.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e2-hilbert90-swap23-residue-gauge.json"

E1_SHA = "e84f0222007b8b404d4651198fb74cb325e394848063ba74a6105e692cd9d442"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
I = sp.I


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved: {path.name}: "
            f"claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def normalized_factor(fac: sp.Expr, t: sp.Symbol) -> tuple[str, sp.Expr]:
    p = sp.Poly(sp.expand(fac), t, extension=I)
    lc = c4b1d.clean(p.LC())
    monic = sp.Poly(sp.expand(p.as_expr() / lc), t, extension=I).as_expr()
    return csha(c4b1d.atlas.encode_poly(monic, [t])), monic


def divisor_of_rational(expr: sp.Expr, t: sp.Symbol) -> dict:
    expr = c4b1d.clean(expr)
    num, den = sp.fraction(expr)
    num = sp.expand(num)
    den = sp.expand(den)
    cn, nf = sp.factor_list(num, t, extension=I)
    cd, df = sp.factor_list(den, t, extension=I)
    rows = []
    finite_degree = 0
    for side, factors, sign in (("zero", nf, 1), ("pole", df, -1)):
        for fac, exponent in factors:
            sig, monic = normalized_factor(fac, t)
            deg = int(sp.Poly(monic, t, extension=I).degree())
            order = sign * int(exponent)
            finite_degree += order * deg
            rows.append({
                "kind": side,
                "order": order,
                "degree": deg,
                "projective_factor_sha256": sig,
                "monic_factor_Qi_t": c4b1d.atlas.encode_poly(monic, [t]),
            })
    infinity_order = -finite_degree
    rows.sort(key=lambda r: (r["kind"], r["degree"], r["projective_factor_sha256"]))
    return {
        "finite_rows": rows,
        "infinity_order": infinity_order,
        "total_divisor_degree": finite_degree + infinity_order,
        "numerator_degree": int(sp.Poly(num, t, extension=I).degree()),
        "denominator_degree": int(sp.Poly(den, t, extension=I).degree()),
        "numerator_scalar_Qi": c4b1d.atlas.encode_element(c4b1d.clean(cn)),
        "denominator_scalar_Qi": c4b1d.atlas.encode_element(c4b1d.clean(cd)),
    }


def build_certificate() -> dict:
    frozen = load_locked(E1, E1_SHA)
    expected_map, residues, directed_maps = e1.reconstruct_exact_data()
    t = sp.Symbol("t")

    frozen_rows = {
        row["source_exceptional_id"]: row
        for row in frozen["literal_orbit_difference"]["rows"]
    }
    if set(frozen_rows) != set(c4b1d.TARGETS):
        raise SystemExit("C4B1E1 source set moved")

    differences: dict[str, sp.Expr] = {}
    gauges: dict[str, sp.Expr] = {}
    target_parameters: dict[str, sp.Expr] = {}
    target_residue_pullbacks: dict[str, sp.Expr] = {}

    for source in c4b1d.TARGETS:
        target = expected_map[source]
        _t, target_parameter, target_pullback, difference = e1.ratio_for(
            source, target, residues, directed_maps
        )
        encoded_difference = c4b1d.atlas.encode_rational(difference, [t])
        expected_hash = frozen_rows[source]["literal_difference_rational_Qi_t_sha256"]
        if csha(encoded_difference) != expected_hash:
            raise SystemExit(f"C4B1E1 literal difference replay moved for {source}")
        q = c4b1d.clean(1 + difference)
        if q == 0:
            raise SystemExit(f"deterministic Hilbert-90 gauge 1+d vanished for {source}")
        differences[source] = difference
        gauges[source] = q
        target_parameters[source] = target_parameter
        target_residue_pullbacks[source] = target_pullback

    rows = []
    unique_divisor_support = set()
    nonconstant_gauge_count = 0
    for source in c4b1d.TARGETS:
        target = expected_map[source]
        q_source = gauges[source]
        q_target_pullback = c4b1d.clean(
            gauges[target].subs({t: target_parameters[source]}, simultaneous=True)
        )
        if q_target_pullback == 0:
            raise SystemExit(f"pulled target Hilbert-90 gauge vanished identically for {source}")

        coboundary = c4b1d.clean(q_source / q_target_pullback)
        if c4b1d.clean(coboundary - differences[source]) != 0:
            raise SystemExit(f"Hilbert-90 coboundary identity failed for {source}->{target}")

        corrected_source = c4b1d.clean(residues[source] / q_source)
        corrected_target_pullback = c4b1d.clean(
            target_residue_pullbacks[source] / q_target_pullback
        )
        if c4b1d.clean(corrected_source - corrected_target_pullback) != 0:
            raise SystemExit(f"gauge-corrected residue transport failed for {source}->{target}")

        div = divisor_of_rational(q_source, t)
        if div["total_divisor_degree"] != 0:
            raise SystemExit(f"principal divisor degree check failed for {source}")
        if div["finite_rows"] or div["infinity_order"]:
            nonconstant_gauge_count += 1
        for dr in div["finite_rows"]:
            unique_divisor_support.add((dr["kind"], dr["projective_factor_sha256"]))
        if div["infinity_order"]:
            unique_divisor_support.add(("infinity", str(div["infinity_order"])))

        encoded_q = c4b1d.atlas.encode_rational(q_source, [t])
        encoded_qtp = c4b1d.atlas.encode_rational(q_target_pullback, [t])
        encoded_corrected = c4b1d.atlas.encode_rational(corrected_source, [t])
        rows.append({
            "source_exceptional_id": source,
            "target_exceptional_id": target,
            "difference_rational_Qi_t_sha256": frozen_rows[source]["literal_difference_rational_Qi_t_sha256"],
            "hilbert90_gauge_rule": "q_source=1+d_source",
            "q_source_rational_Qi_t": encoded_q,
            "q_source_rational_Qi_t_sha256": csha(encoded_q),
            "pulled_q_target_rational_Qi_t": encoded_qtp,
            "pulled_q_target_rational_Qi_t_sha256": csha(encoded_qtp),
            "q_source_over_pulled_q_target_equals_difference": True,
            "q_source_principal_divisor": div,
            "corrected_residue_rational_Qi_t": encoded_corrected,
            "corrected_residue_rational_Qi_t_sha256": csha(encoded_corrected),
            "corrected_source_equals_pulled_corrected_target": True,
        })

    if nonconstant_gauge_count != 4:
        raise SystemExit(
            f"expected four nonconstant Hilbert-90 gauges, got {nonconstant_gauge_count}"
        )

    orbit_rows = []
    seen = set()
    for source in c4b1d.TARGETS:
        target = expected_map[source]
        orbit = tuple(sorted((source, target)))
        if orbit in seen:
            continue
        seen.add(orbit)
        orbit_rows.append({
            "orbit_members": list(orbit),
            "explicit_function_field_hilbert90_coboundary_materialized": True,
            "gauge_corrected_residue_transport_exact_in_both_directions": True,
        })
    if len(orbit_rows) != 2:
        raise SystemExit("expected two swap23 nonconstant orbits")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e2.hilbert90_swap23_residue_gauge.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E2_EXPLICIT_HILBERT90_SWAP23_RESIDUE_GAUGE",
        "role": "EXACT_NONCREDIT_FUNCTION_FIELD_HILBERT90_COBoundary_KILLING_THE_FOUR_C4B1D_SWAP23_RESIDUE_DIFFERENCES",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "c4b1e1_literal_orbit_difference_sha256": E1_SHA,
            "c4b1d_sha256": c4b1d.C4B1D_SHA if hasattr(c4b1d, "C4B1D_SHA") else "0b63663ce9e4eda381e7665dbf7722969898ebf931806b5eec3687579882c11e",
            "r5b2d2_sha256": c4b1d.D2_SHA,
            "exceptional_p1_tangent_coordinates_sha256": c4b1d.EXC_SHA,
        },
        "hilbert90_gauge": {
            "directed_row_count": len(rows),
            "nonconstant_gauge_count": nonconstant_gauge_count,
            "unique_principal_divisor_support_entry_count": len(unique_divisor_support),
            "rows": sorted(rows, key=lambda row: row["source_exceptional_id"]),
            "orbit_rows": sorted(orbit_rows, key=lambda row: row["orbit_members"]),
        },
        "exact_consequence": {
            "all_four_swap23_difference_rational_cocycles_are_explicit_function_field_coboundaries": True,
            "deterministic_q_equals_1_plus_d_gauge_works_for_all_four_directed_differences": True,
            "all_four_gauge_corrected_exceptional_residue_representatives_are_swap23_transport_equal": True,
            "the_c4b1d_nonsquare_difference_is_not_a_function_field_action_obstruction_after_rational_gauge": True,
            "all_four_q_gauges_are_nonconstant_and_have_principal_divisor_support_to_resolve": True,
            "q_gauges_materialized_as_global_regular_units_on_the_whole_exceptional_p1": False,
            "q_divisor_support_attached_to_the_1757_rees_cover": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_changed": "C4B1D's four nonsquare residue differences are now exact multiplicative swap23 coboundaries in the exceptional function fields, with an explicit q=1+d gauge that makes the corrected residue representatives transport identically",
            "what_did_not_change": "the q gauges are nonconstant rational functions, not global regular units; their zero/pole divisors must be attached to the resolved-surface cover and absorbed by genuine Cartier/Cech transition data before any H2-fixedness credit",
            "hilbert90_does_not_itself_supply_cover_indexed_r_ij": True,
            "function_field_gauge_is_not_full_surface_cech_glue": True,
        },
        "next_exact_step": "embed each q_source principal divisor into the corresponding exceptional P1 inside the D2 36-piece Rees refinement, refine/Cartier-bind its zero-pole support, and then test whether the resulting transition units admit the required square-root cochain and triple-overlap identity",
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT}")
        print(cert["canonical_sha256"])
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E2 certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
