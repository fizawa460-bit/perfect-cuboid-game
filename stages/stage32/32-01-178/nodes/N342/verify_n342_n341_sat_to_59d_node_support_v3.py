#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import z3
from sympy import Matrix

import verify_n342_n341_sat_to_59d_node_support_v2 as v2


def main() -> None:
    bundle = v2.load_retained(v2.RETAINED, "s32_n342v3_bundle")
    marking = v2.load_retained(v2.MARKING, "s32_n342v3_marking")
    if bundle.get("canonical_sha256") != v2.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("bundle canonical drift")
    if marking.get("canonical_sha256") != v2.EXPECTED_MARKING_CANONICAL:
        raise ValueError("marking canonical drift")

    adapter = v2.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    transform = v2.RetainedBasisPairingTransform.from_bundle(bundle)
    if transform.den != 8:
        raise ValueError("selected64 denominator drift")
    selected_labels = list(transform.certificate["selected_known_indices_1based"])
    if len(selected_labels) != 64 or sum(label > 92 for label in selected_labels) != 29:
        raise ValueError("selected64 partition drift")

    # Expensive retained translation reconstruction is executed exactly once.
    data = v2.reconstruct_translation_data(marking, bundle)
    M = data["M"]
    pivots = [int(x) for x in data["pivot_rows"]]
    selected_M = M.extract(pivots, list(range(59)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform drift")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("reduced transform is not unimodular")
    kernel_reduced = data["K"] * U
    Mred = M * U

    # One exact 59x59 left inverse is reused for all 21 witnesses.
    _, pivot_rows = kernel_reduced.T.rref()
    pivot_rows = list(pivot_rows)
    if len(pivot_rows) != 59:
        raise ValueError("kernel rank drift")
    square_inv = kernel_reduced.extract(pivot_rows, list(range(59))).inv()

    # Reuse the audited EX5 bridge loader and coordinate parser, but do not
    # rerun its expensive Picard reconstruction 21 times. Support is computed
    # from each witness's exact labelled all140 pairings, never from scalar e.
    ex5 = v2.load_module(v2.EX5_CONSUMER, "s32_n342v3_ex5")
    bridge_rows, bridge_claimed = ex5.load_node_bridge(v2.NODE_BRIDGE)
    bridge_raw = json.loads(v2.NODE_BRIDGE.read_text())
    raw_claimed = bridge_raw.get("canonical_sha256_without_this_field")
    if raw_claimed != bridge_claimed:
        raise ValueError("node bridge canonical disagreement")
    if raw_claimed is not None:
        bridge_body = dict(bridge_raw)
        bridge_body.pop("canonical_sha256_without_this_field", None)
        if v2.csha(bridge_body) != raw_claimed:
            raise ValueError("node bridge canonical drift")
        bridge_lock = raw_claimed
    else:
        bridge_lock = v2.csha(bridge_raw)

    full_support_coord_matrix = Matrix([
        [ex5.parse_qi(x) for x in row["canonical_stoll_coordinates"]]
        for row in bridge_rows
    ])
    full_support_rank = int(full_support_coord_matrix.rank())
    if full_support_rank != 7:
        raise ValueError("retained 48-node bridge no longer spans P6")

    yn = [z3.Int(f"yn_{j}") for j in range(35)]
    yexpr = [z3.IntVal(1) for _ in range(29)] + yn
    B = transform.inverse_integer
    P = adapter.pairing_matrix
    num_expr = [v2.zsum([B[i, j] for j in range(64)], yexpr) for i in range(64)]
    pairing_num = [v2.zsum([P[r, i] for i in range(64)], num_expr) for r in range(140)]
    solver = z3.SolverFor("QF_LIA")
    for expr in num_expr:
        solver.add(expr % 8 == 0)
    for label in v2.EXCEPTIONAL_LABELS:
        solver.add(pairing_num[label - 1] == 8)
    for label in v2.NORMAL_LABELS:
        solver.add(pairing_num[label - 1] >= 0)
    normal_total_num = z3.Sum([pairing_num[label - 1] for label in v2.NORMAL_LABELS])
    x4_num = pairing_num[v2.X4_LABEL - 1]

    phi = Matrix([
        list(data["bridge"].degree_functional),
        list(data["bridge"].exceptional_mass_functional),
        list(data["bridge"].first_normal_half_functional),
    ])
    gram = Matrix(bundle["picard_gram_64x64"])
    rows = []

    for row_id, genus, degree, e, normal_mass, sat_x4s in v2.TARGETS:
        indexer = v2.N220FilteredTerminalIndexer(genus, degree, e)
        if indexer.accepted_exceptional_count != 1:
            raise ValueError("N260 one-exceptional-block drift")
        solver.push()
        for var in yn:
            solver.add(var >= 0, var <= normal_mass)
        solver.add(normal_total_num == 8 * normal_mass)

        for x4 in sat_x4s:
            solver.push()
            solver.add(x4_num == 8 * x4)
            if solver.check() != z3.sat:
                raise ValueError(f"N341 SAT terminal failed rematerialization: {row_id}/x4={x4}")
            model = solver.model()
            yvals = [1] * 29 + [int(model.eval(var, model_completion=True).as_long()) for var in yn]
            if not transform.full_membership(yvals):
                raise ValueError("selected64 membership replay failed")
            xvals = transform.reconstruct_picard_basis(yvals)
            pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
            if pairings[92:] != [1] * 48:
                raise ValueError("exact labelled exceptional vector is not [1]^48")
            if min(pairings[:92]) < 0 or sum(pairings[:92]) != normal_mass or pairings[48] != x4:
                raise ValueError("normal pairing replay failed")

            x = Matrix(xvals)
            z = data["C"] * x
            q = x - data["x0_map"] * z
            if data["C"] * q != Matrix.zeros(5, 1):
                raise ValueError("affine kernel replay failed")
            r = square_inv * q.extract(pivot_rows, [0])
            if kernel_reduced * r != q:
                raise ValueError("59D witness solve failed")
            zvals = v2.ints(z)
            rvals = v2.ints(r)
            if data["N"] * x != data["B"] * z:
                raise ValueError("Reynolds numerator identity failed")
            if data["pairing_x0_map"] * z + Mred * r != Matrix(pairings):
                raise ValueError("59D all140 replay failed")

            slice_values = v2.ints(phi * x)
            if slice_values[0] != degree or slice_values[1] != e:
                raise ValueError("degree/e slice replay failed")
            terminal_pairings = list(indexer.unrank(x4))
            old_rank = int(indexer.old_rank_of_filtered(x4))
            disp = indexer.disposition_of_old(old_rank)
            if terminal_pairings[4] != x4 or disp.get("disposition") != "N220_SURVIVOR" or int(disp["filtered_rank"]) != x4:
                raise ValueError("old-rank locator replay failed")

            # Exact EX5 support rule replay from labelled pairings.
            last48 = pairings[92:140]
            support = [k for k, value in enumerate(last48) if value > 0]
            zeros = [k for k, value in enumerate(last48) if value == 0]
            support_rows = [bridge_rows[k] for k in support]
            coord_matrix = Matrix([
                [ex5.parse_qi(x) for x in row["canonical_stoll_coordinates"]]
                for row in support_rows
            ]) if support_rows else Matrix.zeros(0, 7)
            vector_rank = int(coord_matrix.rank()) if support_rows else 0
            if support != list(range(48)) or zeros or vector_rank != 7:
                raise ValueError("exact labelled node-support replay failed")

            self_square = int((x.T * gram * x)[0])
            required_lower = -degree - 2 + 2 * genus
            rows.append({
                "row_id": row_id,
                "g": genus,
                "d": degree,
                "e": e,
                "filtered_rank": x4,
                "old_terminal_rank": old_rank,
                "terminal_pairings": terminal_pairings,
                "x4": x4,
                "picard_coordinates_sha256": v2.csha(xvals),
                "z": zvals,
                "a": slice_values[2],
                "witness_r_reduced": rvals,
                "witness_r_reduced_sha256": v2.csha(rvals),
                "all140_pairings_sha256": v2.csha(pairings),
                "self_square": self_square,
                "required_self_square_lower": required_lower,
                "chosen_picard_model_self_square_pass": self_square >= required_lower,
                "node_support": {
                    "algorithm_source_blob_sha1": v2.EX5_CONSUMER_BLOB,
                    "pairings_last48_sha256": v2.csha(last48),
                    "support_count": len(support),
                    "zero_indices_0based": zeros,
                    "canonical_node_vector_rank": vector_rank,
                    "projective_span_dimension": vector_rank - 1,
                    "spans_p6": vector_rank == 7,
                },
            })
            solver.pop()
        solver.pop()

    if len(rows) != 21:
        raise ValueError("SAT handoff count drift")
    self_square_pass_count = sum(bool(row["chosen_picard_model_self_square_pass"]) for row in rows)
    body = {
        "schema": "STAGE32_32_01_178_N342_N341_SAT_TO_59D_NODE_SUPPORT_V3",
        "source_locks": {
            "n341_run_id": v2.N341_RUN,
            "n341_job_id": v2.N341_JOB,
            "n341_canonical_sha256": v2.N341_CANONICAL,
            "n341_verifier_blob_sha1": v2.N341_VERIFIER_BLOB,
            "n341_source_ledger": "157 UNSAT / 21 SAT / 0 unknown",
            "n341_sat_terminal_sets": {"g0-d176": v2.TARGETS[0][5], "g1-d192": v2.TARGETS[1][5]},
            "retained_bundle_canonical_sha256": v2.EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical_sha256": v2.EXPECTED_MARKING_CANONICAL,
            "ex5_audited_head": v2.EX5_AUDITED_HEAD,
            "ex5_support_algorithm_blob_sha1": v2.EX5_CONSUMER_BLOB,
            "node_bridge_blob_sha1": v2.NODE_BRIDGE_BLOB,
            "node_bridge_canonical_sha256": bridge_lock,
        },
        "result": {
            "sat_terminal_count": 21,
            "all_21_rematerialized_exact_picard64": True,
            "all_21_have_exact_reynolds59d_witness": True,
            "all_21_have_exact_old_rank_locator": True,
            "all_21_exact_labelled_support48": True,
            "all_21_support_span_p6": True,
            "chosen_picard_models_meeting_self_square_threshold": self_square_pass_count,
            "rows": rows,
        },
        "firewalls": {
            "n341_157_unsat_not_recomputed_here": True,
            "support_replayed_from_labelled_all140_not_scalar_e": True,
            "ex5_support_algorithm_reused_without_repeating_21_expensive_picard_reconstructions": True,
            "chosen_model_self_square_failure_if_any_is_not_terminal_unsat": True,
            "picard_numerical_class_is_not_effective_curve_existence": True,
            "n350_producer_registry_unchanged": True,
            "n350_hostile_audit_required_before_registration": True,
            "n260_n280_n310_n341_n342_audit_boundaries_preserved": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": v2.csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
