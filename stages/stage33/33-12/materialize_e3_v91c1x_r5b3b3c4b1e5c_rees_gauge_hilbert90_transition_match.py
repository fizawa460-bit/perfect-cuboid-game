#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c4b1d_swap23_tangent_pullback_comparison as c4b1d
import materialize_e3_v91c1x_r5b3b3c4b1e1_literal_swap23_orbit_difference_cocycle as e1
import materialize_e3_v91c1x_r5b3b3c4b1e5b_rees_gauge_cross_action_divisor_transport as e5b

HERE = Path(__file__).resolve().parent
E1 = HERE / "e3-v91c1x-r5b3b3c4b1e1-literal-swap23-orbit-difference-cocycle.json"
E2 = HERE / "e3-v91c1x-r5b3b3c4b1e2-hilbert90-swap23-residue-gauge.json"
E3 = HERE / "e3-v91c1x-r5b3b3c4b1e3-hilbert90-divisor-rees-attachment.json"
E4 = HERE / "e3-v91c1x-r5b3b3c4b1e4-rees-cartier-rational-gauge-lift.json"
E5B = HERE / "e3-v91c1x-r5b3b3c4b1e5b-rees-gauge-cross-action-divisor-transport.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5c-rees-gauge-hilbert90-transition-match.json"

E1_SHA = "e84f0222007b8b404d4651198fb74cb325e394848063ba74a6105e692cd9d442"
E2_SHA = "65793b939058c8ebe28cd5829d12c1c3d00bfbc0ca21bfd830513f990a767b9b"
E3_SHA = "cad7a3493b3215a1988058a26ddf00d3da45109212caa19df9f439d9cb5143ea"
E4_SHA = "6a31839c0ef50439d6a0e5a7b4d6b452ae8caf2f68d0419aa1dbc4d339c27d07"
E5B_SHA = "5d60f94503a863800d4ca67265728a9e3b55cdd9d8d08f5203b8734316a9616d"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
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


def decode_rational(encoded: dict, variables: list[sp.Symbol]) -> sp.Expr:
    num = atlas.decode_poly(encoded["numerator"], variables)
    den = atlas.decode_poly(encoded["denominator"], variables)
    if clean(den) == 0:
        raise SystemExit("zero rational denominator")
    return clean(num / den)


def encode_rational(expr: sp.Expr, variables: list[sp.Symbol]) -> dict:
    num, den = sp.fraction(sp.cancel(expr))
    return {
        "numerator": atlas.encode_poly(sp.expand(num), variables),
        "denominator": atlas.encode_poly(sp.expand(den), variables),
    }


def build_certificate() -> dict:
    frozen_e1 = load_locked(E1, E1_SHA)
    e2 = load_locked(E2, E2_SHA)
    e3 = load_locked(E3, E3_SHA)
    e4 = load_locked(E4, E4_SHA)
    e5b_cert = load_locked(E5B, E5B_SHA)
    exc = c4b1d.load_locked(c4b1d.EXC, c4b1d.EXC_SHA)

    expected_map, residues, directed_maps = e1.reconstruct_exact_data()
    targets = list(c4b1d.TARGETS)
    if set(expected_map) != set(targets):
        raise SystemExit("E1 action map source inventory moved")

    e1_rows = {
        row["source_exceptional_id"]: row
        for row in frozen_e1["literal_orbit_difference"]["rows"]
    }
    e2_rows = {
        row["source_exceptional_id"]: row
        for row in e2["hilbert90_gauge"]["rows"]
    }
    e3_rows = {
        row["source_exceptional_id"]: row
        for row in e3["p1_to_rees_embedding"]["rows"]
    }
    e4_rows = {
        row["source_exceptional_id"]: row
        for row in e4["rees_rational_gauge_lifts"]["rows"]
    }
    if not (set(e1_rows) == set(e2_rows) == set(e3_rows) == set(e4_rows) == set(targets)):
        raise SystemExit("E1/E2/E3/E4 source inventory mismatch")

    er_by_eid = {row["exceptional_id"]: row for row in exc["exceptional_models"]}
    metas = {eid: atlas.node_meta(er_by_eid[eid]) for eid in targets}

    X = list(sp.symbols("a1 a2 a3 b1 b2 b3 c"))
    H = list(sp.symbols("H0:6"))
    t, u, w = sp.symbols("t u w")

    ambient_q: dict[str, sp.Expr] = {}
    restriction_q: dict[str, sp.Expr] = {}
    for source in targets:
        row = e4_rows[source]
        N = atlas.decode_poly(row["homogeneous_q_numerator_Qi_H"], H)
        D = atlas.decode_poly(row["homogeneous_q_denominator_Qi_H"], H)
        if N == 0 or D == 0:
            raise SystemExit(f"zero E4 homogeneous q member at {source}")
        Namb = e5b.ambient_lift_from_rees_direction(N, metas[source], H, X)
        Damb = e5b.ambient_lift_from_rees_direction(D, metas[source], H, X)
        ambient_q[source] = clean(Namb / Damb)

        hsrc = sp.Matrix([
            atlas.decode_poly(enc, [u, w])
            for enc in e3_rows[source]["source_rees_homogeneous_vector_Qi_u_w"]
        ])
        qsrc_p1 = clean(
            N.subs({H[j]: hsrc[j] for j in range(6)}, simultaneous=True)
            / D.subs({H[j]: hsrc[j] for j in range(6)}, simultaneous=True)
        )
        q_e2 = decode_rational(e2_rows[source]["q_source_rational_Qi_t"], [t])
        q_e2_uw = clean(q_e2.subs({t: u / w}, simultaneous=True))
        if clean(qsrc_p1 - q_e2_uw) != 0:
            raise SystemExit(f"E4/E2 exceptional restriction moved at {source}")
        restriction_q[source] = qsrc_p1

    rows = []
    exact_fiber_match_count = 0
    exact_ambient_involution_count = 0
    exact_e2_orientation_count = 0
    zero_transport_by_source = {
        row["source_exceptional_id"]: bool(row["total_zero_or_pole_divisor_equation_transports_projectively_exact"])
        for row in e5b_cert["whole_zero_pole_divisor_transport"]["rows"]
        if row["equation_kind"] == "zero"
    }
    pole_transport_by_source = {
        row["source_exceptional_id"]: bool(row["total_zero_or_pole_divisor_equation_transports_projectively_exact"])
        for row in e5b_cert["whole_zero_pole_divisor_transport"]["rows"]
        if row["equation_kind"] == "pole"
    }

    for source in targets:
        target = expected_map[source]
        if e2_rows[source]["target_exceptional_id"] != target:
            raise SystemExit(f"E2 target map moved at {source}")
        if e3_rows[source]["target_exceptional_id"] != target:
            raise SystemExit(f"E3 target map moved at {source}")
        if e4_rows[source]["target_exceptional_id"] != target:
            raise SystemExit(f"E4 target map moved at {source}")

        Qs = ambient_q[source]
        Qt_pull = e5b.pullback_tau(ambient_q[target], X)
        mismatch = clean(Qs / Qt_pull)
        if mismatch == 0:
            raise SystemExit(f"zero ambient Hilbert90 mismatch at {source}")

        # The same definition in the reverse direction must satisfy the literal involution identity.
        Mt = clean(ambient_q[target] / e5b.pullback_tau(ambient_q[source], X))
        involution = clean(mismatch * e5b.pullback_tau(Mt, X))
        ambient_involution_exact = clean(involution - 1) == 0
        if ambient_involution_exact:
            exact_ambient_involution_count += 1

        # Restrict the pulled target gauge using the exact E3 acted-target Rees tangent vector,
        # still parameterized by the source [u:w].
        target_row = e4_rows[target]
        Nt = atlas.decode_poly(target_row["homogeneous_q_numerator_Qi_H"], H)
        Dt = atlas.decode_poly(target_row["homogeneous_q_denominator_Qi_H"], H)
        htgt = sp.Matrix([
            atlas.decode_poly(enc, [u, w])
            for enc in e3_rows[source]["acted_target_rees_homogeneous_vector_Qi_u_w"]
        ])
        qtp_p1 = clean(
            Nt.subs({H[j]: htgt[j] for j in range(6)}, simultaneous=True)
            / Dt.subs({H[j]: htgt[j] for j in range(6)}, simultaneous=True)
        )
        mismatch_p1 = clean(restriction_q[source] / qtp_p1)

        _tt, _target_parameter, _target_pullback, difference = e1.ratio_for(
            source, target, residues, directed_maps
        )
        encoded_difference = atlas.encode_rational(difference, [t])
        if csha(encoded_difference) != e1_rows[source]["literal_difference_rational_Qi_t_sha256"]:
            raise SystemExit(f"E1 difference lock moved at {source}")
        difference_uw = clean(difference.subs({t: u / w}, simultaneous=True))
        fiber_match = clean(mismatch_p1 - difference_uw) == 0
        if fiber_match:
            exact_fiber_match_count += 1

        # Independent replay of the E2 orientation, using the stored pulled target q.
        stored_q_source = decode_rational(e2_rows[source]["q_source_rational_Qi_t"], [t])
        stored_q_target_pull = decode_rational(e2_rows[source]["pulled_q_target_rational_Qi_t"], [t])
        stored_ratio = clean(stored_q_source / stored_q_target_pull)
        e2_orientation_exact = clean(stored_ratio - difference) == 0
        if e2_orientation_exact:
            exact_e2_orientation_count += 1

        rows.append({
            "source_exceptional_id": source,
            "target_exceptional_id": target,
            "ambient_transition_rule": "m_source = Q_source / swap23^*(Q_target)",
            "ambient_rational_transition_Qi_X": encode_rational(mismatch, X),
            "ambient_rational_transition_sha256": csha(encode_rational(mismatch, X)),
            "ambient_reverse_pullback_product_equals_one_exact": ambient_involution_exact,
            "exceptional_p1_transition_Qi_u_w": encode_rational(mismatch_p1, [u, w]),
            "exceptional_p1_transition_sha256": csha(encode_rational(mismatch_p1, [u, w])),
            "frozen_e1_difference_rational_Qi_t_sha256": e1_rows[source]["literal_difference_rational_Qi_t_sha256"],
            "exceptional_p1_transition_equals_frozen_e1_difference_exact": fiber_match,
            "stored_e2_q_source_over_pulled_q_target_equals_same_difference_exact": e2_orientation_exact,
            "e5b_zero_divisor_transport_projectively_exact": zero_transport_by_source[source],
            "e5b_pole_divisor_transport_projectively_exact": pole_transport_by_source[source],
            "interpretation": "pole transport failure is compatible with, and here measured by, the required Hilbert90 rational transition rather than being treated as a standalone obstruction",
        })

    all_fiber = exact_fiber_match_count == len(targets)
    all_involution = exact_ambient_involution_count == len(targets)
    all_e2_orientation = exact_e2_orientation_count == len(targets)
    all_zero_transport = all(zero_transport_by_source.values())
    all_pole_transport_fail = all(not x for x in pole_transport_by_source.values())

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5c.rees_gauge_hilbert90_transition_match.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5C_REES_GAUGE_HILBERT90_TRANSITION_MATCH",
        "role": "EXACT_NONCREDIT_IDENTIFICATION_OF_THE_E4_REES_GAUGE_CROSS_ACTION_MISMATCH_WITH_THE_FROZEN_E1_HILBERT90_DIFFERENCE_ON_THE_EXCEPTIONAL_P1",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "c4b1e1_sha256": E1_SHA,
            "c4b1e2_sha256": E2_SHA,
            "c4b1e3_sha256": E3_SHA,
            "c4b1e4_sha256": E4_SHA,
            "c4b1e5b_sha256": E5B_SHA,
            "exceptional_p1_tangent_coordinates_sha256": c4b1d.EXC_SHA,
            "source_bound_swap23_coordinate_permutation_zero_based": atlas.PERM,
        },
        "transition_match": {
            "directed_row_count": len(rows),
            "fiber_exact_match_count": exact_fiber_match_count,
            "ambient_involution_identity_count": exact_ambient_involution_count,
            "stored_e2_orientation_replay_count": exact_e2_orientation_count,
            "rows": sorted(rows, key=lambda row: row["source_exceptional_id"]),
        },
        "exact_consequence": {
            "all_four_rees_cross_action_transitions_restrict_to_the_frozen_e1_difference_cocycle": all_fiber,
            "all_four_ambient_rational_transition_pairs_satisfy_swap23_involution_identity": all_involution,
            "e2_orientation_q_source_over_pulled_q_target_equals_difference_replayed_all_four": all_e2_orientation,
            "e5b_zero_divisors_transport_exact_all_four": all_zero_transport,
            "e5b_pole_divisors_transport_nontrivially_all_four": all_pole_transport_fail,
            "e5b_pole_mismatch_is_not_by_itself_an_obstruction": all_fiber and all_e2_orientation,
            "source_bound_rational_transition_candidate_materialized": all_fiber and all_involution,
            "transition_is_regular_gm_unit_on_every_required_cover_overlap": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_is_now_exact": "the deterministic E4 Rees extensions have a source-bound rational cross-action transition m=Q_source/swap23^*Q_target; its restriction to every exceptional P1 is exactly the frozen E1 difference d, and the reverse-pullback product is 1",
            "what_is_still_missing": "localize m on the actual D2/317 cover refinement, determine on which overlap pieces it is a regular Gm unit after accounting for its off-fiber zero/pole support, then test whether those cover-indexed units admit the required square-root cochain and triple-overlap identity",
            "rational_group_action_transition_is_not_yet_a_cech_line_bundle_cocycle": True,
            "fiber_hilbert90_identity_does_not_remove_offfiber_prime_refinement_debt": True,
        },
        "next_exact_step": "pull each ambient rational transition m_source onto the finite source/acted-target D2 refinement pieces from E3, use E5A/E5B support factors to remove pieces meeting its zero or pole support, and materialize the remaining piecewise regular Gm transition units ell before any square-root test",
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
        raise SystemExit("materialized C4B1E5C certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
