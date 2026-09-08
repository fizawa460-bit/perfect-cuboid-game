#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas

HERE = Path(__file__).resolve().parent
E5A = HERE / "e3-v91c1x-r5b3b3c4b1e5a-rees-gauge-factor-carrier-binding.json"
E3 = HERE / "e3-v91c1x-r5b3b3c4b1e3-hilbert90-divisor-rees-attachment.json"
EXC = HERE.parent / "33-07" / "exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5b-rees-gauge-cross-action-divisor-transport.json"

E5A_SHA = "a294f594ab15230f09c8dd3e595f8b343ec88eded5e117600c5fb6181f2eac99"
E3_SHA = "cad7a3493b3215a1988058a26ddf00d3da45109212caa19df9f439d9cb5143ea"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
PERM = atlas.PERM
I = sp.I


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


def clean(x: sp.Expr) -> sp.Expr:
    return atlas.clean(x)


def ambient_lift_from_rees_direction(poly: sp.Expr, meta: dict, H: list[sp.Symbol], X: list[sp.Symbol]) -> sp.Expr:
    P = sp.Poly(sp.expand(poly), *H, extension=I)
    degree = int(P.total_degree())
    if degree <= 0:
        raise SystemExit("expected positive-degree Rees factor")
    if any(sum(mon) != degree for mon, coeff in P.terms() if coeff != 0):
        raise SystemExit("E5A factor ceased to be homogeneous")
    pivot = int(meta["pivot"])
    q = meta["q"]
    nonpivot = [int(j) for j in meta["nonpivot"]]
    if len(nonpivot) != len(H):
        raise SystemExit("Rees direction dimension moved")
    linear_displacements = [clean(X[j] - q[j] * X[pivot]) for j in nonpivot]
    out = clean(poly.subs({H[k]: linear_displacements[k] for k in range(len(H))}, simultaneous=True))
    OP = sp.Poly(sp.expand(out), *X, extension=I)
    if int(OP.total_degree()) != degree or any(sum(mon) != degree for mon, coeff in OP.terms() if coeff != 0):
        raise SystemExit("ambient lift lost homogeneous degree")
    p = meta["point"]
    if clean(out.subs({X[j]: p[j] for j in range(7)}, simultaneous=True)) != 0:
        raise SystemExit(f"ambient lifted factor missed source node {meta['exceptional_id']}")
    return out


def sig(poly: sp.Expr, X: list[sp.Symbol]) -> str:
    return atlas.projective_poly_signature(poly, X)[0]


def pullback_tau(poly: sp.Expr, X: list[sp.Symbol]) -> sp.Expr:
    return clean(poly.subs({X[j]: X[PERM[j]] for j in range(7)}, simultaneous=True))


def build_certificate() -> dict:
    e5a = load_locked(E5A, E5A_SHA)
    e3 = load_locked(E3, E3_SHA)
    exc = load_locked(EXC, EXC_SHA)

    target_map = {
        row["source_exceptional_id"]: row["target_exceptional_id"]
        for row in e3["p1_to_rees_embedding"]["rows"]
    }
    if set(target_map) != {"EXC_003", "EXC_004", "EXC_011", "EXC_012"}:
        raise SystemExit("E3 four-source action map moved")
    if any(target_map.get(target_map[eid]) != eid for eid in target_map):
        raise SystemExit("E3 source-target map ceased to be involutive")

    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    metas = {eid: atlas.node_meta(er_by_eid[eid]) for eid in target_map}
    X = list(sp.symbols("a1 a2 a3 b1 b2 b3 c"))
    H = list(sp.symbols("H0:6"))

    raw_rows = e5a["factorization"]["rows"]
    lifted = []
    for idx, row in enumerate(raw_rows):
        eid = row["source_exceptional_id"]
        poly = atlas.decode_poly(row["normalized_factor_Qi_H"], H)
        F = ambient_lift_from_rees_direction(poly, metas[eid], H, X)
        lifted.append({
            "index": idx,
            "source_exceptional_id": eid,
            "equation_kind": row["equation_kind"],
            "factor_exponent": int(row["factor_exponent"]),
            "factor_total_degree": int(row["factor_total_degree"]),
            "ambient_factor_Qi_X": atlas.encode_poly(F, X),
            "ambient_factor_projective_signature_sha256": sig(F, X),
            "_poly": F,
        })

    by_source_kind: dict[tuple[str, str], list[dict]] = {}
    for row in lifted:
        by_source_kind.setdefault((row["source_exceptional_id"], row["equation_kind"]), []).append(row)

    factor_transport_rows = []
    transported_factor_count = 0
    factor_occurrence_count = 0
    for source in sorted(target_map):
        target = target_map[source]
        for kind in ("zero", "pole"):
            srcrows = by_source_kind.get((source, kind), [])
            tgtrows = by_source_kind.get((target, kind), [])
            target_pull_sigs = {}
            for tr in tgtrows:
                ps = sig(pullback_tau(tr["_poly"], X), X)
                target_pull_sigs.setdefault(ps, []).append(tr)
            for sr in srcrows:
                ss = sr["ambient_factor_projective_signature_sha256"]
                matches = target_pull_sigs.get(ss, [])
                exponent_match = any(int(tr["factor_exponent"]) == int(sr["factor_exponent"]) for tr in matches)
                if exponent_match:
                    transported_factor_count += 1
                factor_occurrence_count += 1
                factor_transport_rows.append({
                    "source_exceptional_id": source,
                    "target_exceptional_id": target,
                    "equation_kind": kind,
                    "source_factor_projective_signature_sha256": ss,
                    "source_factor_degree": int(sr["factor_total_degree"]),
                    "source_factor_exponent": int(sr["factor_exponent"]),
                    "pulled_target_matching_factor_signature_count": len(matches),
                    "pulled_target_factor_with_same_multiplicity_exists": exponent_match,
                    "factor_support_and_multiplicity_transport_exact": exponent_match,
                })

    divisor_rows = []
    exact_divisor_transport_count = 0
    for source in sorted(target_map):
        target = target_map[source]
        for kind in ("zero", "pole"):
            srcrows = by_source_kind.get((source, kind), [])
            tgtrows = by_source_kind.get((target, kind), [])
            if not srcrows or not tgtrows:
                raise SystemExit(f"missing factor rows for {source}->{target}/{kind}")
            src_total = sp.Integer(1)
            tgt_total = sp.Integer(1)
            for row in srcrows:
                src_total *= row["_poly"] ** int(row["factor_exponent"])
            for row in tgtrows:
                tgt_total *= row["_poly"] ** int(row["factor_exponent"])
            src_total = clean(src_total)
            pulled_target_total = pullback_tau(clean(tgt_total), X)
            src_sig = sig(src_total, X)
            pull_sig = sig(pulled_target_total, X)
            exact = src_sig == pull_sig
            if exact:
                exact_divisor_transport_count += 1
            divisor_rows.append({
                "source_exceptional_id": source,
                "target_exceptional_id": target,
                "equation_kind": kind,
                "source_total_degree_with_multiplicity": int(sp.Poly(sp.expand(src_total), *X, extension=I).total_degree()),
                "source_total_projective_polynomial_signature_sha256": src_sig,
                "pulled_target_total_projective_polynomial_signature_sha256": pull_sig,
                "total_zero_or_pole_divisor_equation_transports_projectively_exact": exact,
            })

    nonlinear_rows = [row for row in lifted if int(row["factor_total_degree"]) > 1]
    nonlinear_transport_rows = [
        row for row in factor_transport_rows
        if int(row["source_factor_degree"]) > 1
    ]
    nonlinear_exact = all(row["factor_support_and_multiplicity_transport_exact"] for row in nonlinear_transport_rows)
    all_factor_exact = transported_factor_count == factor_occurrence_count
    all_divisor_exact = exact_divisor_transport_count == len(divisor_rows)

    # Build action-orbit representatives only where literal factor transport is exact.
    exact_keys = {
        (row["source_exceptional_id"], row["equation_kind"], row["source_factor_projective_signature_sha256"])
        for row in factor_transport_rows if row["factor_support_and_multiplicity_transport_exact"]
    }
    orbit_rows = []
    seen = set()
    lookup = {
        (row["source_exceptional_id"], row["equation_kind"], row["ambient_factor_projective_signature_sha256"]): row
        for row in lifted
    }
    for key in sorted(exact_keys):
        if key in seen:
            continue
        source, kind, ss = key
        sr = lookup[key]
        target = target_map[source]
        candidates = by_source_kind[(target, kind)]
        target_match = next(
            tr for tr in candidates
            if sig(pullback_tau(tr["_poly"], X), X) == ss
            and int(tr["factor_exponent"]) == int(sr["factor_exponent"])
        )
        tkey = (target, kind, target_match["ambient_factor_projective_signature_sha256"])
        members = sorted({key, tkey})
        seen.update(members)
        orbit_rows.append({
            "orbit_id": csha([list(x) for x in members]),
            "equation_kind": kind,
            "factor_degree": int(sr["factor_total_degree"]),
            "factor_exponent": int(sr["factor_exponent"]),
            "member_count": len(members),
            "members": [
                {"source_exceptional_id": x[0], "factor_projective_signature_sha256": x[2]}
                for x in members
            ],
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5b.rees_gauge_cross_action_divisor_transport.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5B_REES_GAUGE_CROSS_ACTION_DIVISOR_TRANSPORT",
        "role": "EXACT_NONCREDIT_TEST_OF_WHETHER_THE_DETERMINISTIC_E4_REES_EXTENSIONS_OF_THE_EXCEPTIONAL_HILBERT90_GAUGES_HAVE_SWAP23_COMPATIBLE_ZERO_AND_POLE_SUPPORT_OFF_THE_EXCEPTIONAL_FIBER",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "c4b1e5a_sha256": E5A_SHA,
            "c4b1e3_sha256": E3_SHA,
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
            "source_bound_swap23_coordinate_permutation_zero_based": PERM,
        },
        "ambient_factor_lifts": {
            "row_count": len(lifted),
            "nonlinear_factor_row_count": len(nonlinear_rows),
            "rows": [
                {k: v for k, v in row.items() if k != "_poly" and k != "index"}
                for row in lifted
            ],
        },
        "factor_transport": {
            "directed_factor_row_count": factor_occurrence_count,
            "directed_exact_factor_transport_count": transported_factor_count,
            "all_factor_support_and_multiplicity_transport_exact": all_factor_exact,
            "all_nonlinear_factor_support_and_multiplicity_transport_exact": nonlinear_exact,
            "rows": factor_transport_rows,
        },
        "whole_zero_pole_divisor_transport": {
            "directed_divisor_row_count": len(divisor_rows),
            "directed_exact_divisor_transport_count": exact_divisor_transport_count,
            "all_zero_and_pole_divisor_equations_transport_projectively_exact": all_divisor_exact,
            "rows": divisor_rows,
        },
        "exact_factor_action_orbits": {
            "orbit_count": len(orbit_rows),
            "rows": orbit_rows,
        },
        "exact_consequence": {
            "deterministic_e4_extension_is_swap23_equivariant_at_factor_divisor_level": all_factor_exact and all_divisor_exact,
            "nonlinear_zero_carriers_reduce_to_swap23_factor_orbits": nonlinear_exact,
            "same_representative_full_surface_gauge_correction_verified": False,
            "e5_cartier_nonzerodivisor_saturation_completed": False,
            "off_exceptional_height_one_prime_inventory_complete": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "if_transport_fails": "the fiberwise Hilbert90 correction does not extend through this deterministic Rees rational lift as a swap23-compatible divisor datum; replace or modify the off-fiber extension rather than spending prime-decomposition effort on a non-equivariant choice",
            "if_transport_passes": "only then is it efficient to refine the finitely many transported ambient carriers into height-one primes and compute their residue changes",
        },
        "next_exact_step": "if any zero/pole transport fails, compute the rational mismatch tau^*q_target/q_source on the Rees neighborhood and solve for an additional rational correction whose restriction to the exceptional P1 is 1; otherwise prime-refine the exact transported factor orbits",
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
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
        raise SystemExit("materialized C4B1E5B certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
