#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import sympy
from sympy import Matrix

from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound
from direct_picard_reynolds_rank2_integer_qp import OBJECTIVE_DENOMINATOR, dot, quad
from direct_picard_reynolds_rank2_integral_projection_bound import build_reynolds_numerator
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter

GROUP_ORDER = 64
PICARD_RANK = 64
EXPECTED_ANTI_FIXED_RANK = 59
EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
SCHEMA = "STAGE32_21AG_TRUE_ANTIFIXED_COORDINATE_PENALTY_DIAGNOSTIC_V1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def as_fraction(value: sympy.Expr) -> Fraction:
    return Fraction(int(sympy.numer(value)), int(sympy.denom(value)))


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def load_module_payload(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def frac_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def matrix_fraction_sha(m: tuple[tuple[Fraction, ...], ...]) -> str:
    return csha([[[v.numerator, v.denominator] for v in row] for row in m])


def projected_margin_numerator(rank2, z0: tuple[int, ...], lower: int, u: int, v: int) -> int:
    dlin = 2 * dot(z0, rank2.kernel_h0)
    elin = 2 * dot(z0, rank2.kernel_h1)
    fconst = quad(rank2.hessian, z0) - int(lower) * OBJECTIVE_DENOMINATOR
    return (
        rank2.objective_uu * u * u
        + rank2.objective_uv_twice * u * v
        + rank2.objective_vv * v * v
        + dlin * u
        + elin * v
        + fconst
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--row-shards", type=int, default=16)
    ap.add_argument("--shard-index", type=int, default=0)
    ap.add_argument("--example-limit", type=int, default=24)
    args = ap.parse_args()

    if args.row_shards <= 0 or not 0 <= args.shard_index < args.row_shards:
        raise ValueError("invalid deterministic row shard")

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed or claimed != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    bundle = load_module_payload(args.retained, "stage32_21ag_picard")
    marking = load_module_payload(args.marking, "stage32_21ag_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("32-21ac audited evaluator certificate regression")

    mapping = model.mapping
    aa = mapping.penalty
    rank2 = model.rank2
    gram = Matrix(bundle["picard_gram_64x64"])
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])

    N, _, _ = build_reynolds_numerator(marking, adapter, gram, phi)
    if N.shape != (PICARD_RANK, PICARD_RANK):
        raise ValueError("Reynolds numerator shape regression")
    if N * N != GROUP_ORDER * N:
        raise ValueError("Reynolds numerator idempotence regression")
    if N.T * gram != gram * N:
        raise ValueError("Reynolds numerator Gram self-adjointness regression")
    if phi * N != GROUP_ORDER * phi:
        raise ValueError("Reynolds numerator slice-preservation regression")

    null = N.nullspace()
    if len(null) != EXPECTED_ANTI_FIXED_RANK:
        raise ValueError(f"anti-fixed nullity regression: {len(null)}")
    K = Matrix.hstack(*null)
    if K.shape != (PICARD_RANK, EXPECTED_ANTI_FIXED_RANK):
        raise ValueError("anti-fixed basis shape regression")
    if N * K != Matrix.zeros(PICARD_RANK, EXPECTED_ANTI_FIXED_RANK):
        raise ValueError("anti-fixed basis is not in ker(N)")
    if phi * K != Matrix.zeros(3, EXPECTED_ANTI_FIXED_RANK):
        raise ValueError("ker(N) did not lie in the slice kernel")

    positive_gram = -(K.T * gram * K)
    if positive_gram != positive_gram.T:
        raise ValueError("anti-fixed positive Gram symmetry regression")
    L, D = positive_gram.LDLdecomposition(hermitian=False)
    if L * D * L.T != positive_gram:
        raise ValueError("anti-fixed LDL reconstruction regression")
    pivots = [D[i, i] for i in range(D.rows)]
    if any(v <= 0 for v in pivots):
        raise ValueError("anti-fixed positive Gram is not positive definite")

    inverse = positive_gram.inv()
    true_dual_norms: list[Fraction] = []
    for i in range(PICARD_RANK):
        row = K[i, :]
        true_dual_norms.append(as_fraction((row * inverse * row.T)[0]))
    true_dual_norms_t = tuple(true_dual_norms)

    strictly_smaller_dual_norms = 0
    equal_dual_norms = 0
    for old, new in zip(aa.coordinate_dual_norms, true_dual_norms_t):
        if new < 0:
            raise ValueError("negative true anti-fixed coordinate dual norm")
        if new > old:
            raise ValueError("restricting from slice kernel to ker(N) increased a coordinate dual norm")
        if new < old:
            strictly_smaller_dual_norms += 1
        else:
            equal_dual_norms += 1

    old_penalties: list[Fraction] = []
    true_penalties: list[Fraction] = []
    zero_norm_nonzero_residue_count = 0
    classes_improved = 0
    improvement_ratios: list[Fraction] = []
    for residue in mapping.sorted_projection_residues:
        old = aa.lower_bound_from_residue(residue)
        best = Fraction(0, 1)
        impossible = False
        for i, raw in enumerate(residue):
            r = int(raw)
            dist = min(r, GROUP_ORDER - r)
            if dist == 0:
                continue
            dn = true_dual_norms_t[i]
            if dn == 0:
                impossible = True
                zero_norm_nonzero_residue_count += 1
                break
            candidate = Fraction(dist * dist, GROUP_ORDER * GROUP_ORDER) / dn
            if candidate > best:
                best = candidate
        if impossible:
            raise ValueError("projection residue incompatible with ker(N); expected every image residue to have an integral source")
        if best < old:
            raise ValueError("true anti-fixed coordinate penalty undercut audited 32-21aa penalty")
        old_penalties.append(old)
        true_penalties.append(best)
        if best > old:
            classes_improved += 1
            if old > 0:
                improvement_ratios.append(best / old)

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    if len(all_rows) != 178 or len(set(all_rows)) != 178:
        raise ValueError("FULL178 row population regression")
    selected_rows = [row for idx, row in enumerate(all_rows) if idx % args.row_shards == args.shard_index]
    if not selected_rows:
        raise ValueError("selected row shard is empty")

    kkt = rank2.orbit_qp
    bound = rank2.bound
    bridge2 = rank2.bridge
    continuous = 0
    witness_pass = 0
    witness_fail = 0
    witness_stronger = 0
    positive_witness_penalties = 0
    ratio_lt_2 = ratio_lt_4 = ratio_lt_8 = ratio_lt_16 = 0
    min_slack_ratio: Fraction | None = None
    min_slack_margin: Fraction | None = None
    fail_examples: list[dict] = []
    decision_stream = hashlib.sha256()
    row_summaries: list[dict] = []
    penalty_counts: Counter[str] = Counter()

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_cont = row_pass = row_fail = 0
        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            if interval is None:
                continue
            lo, hi = interval
            for a in range(lo, hi + 1):
                if not bridge2.target_in_image(d, e, a):
                    continue
                if kkt.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
                    continue
                candidate = kkt.solve_candidate(d, e, a)
                if candidate is None or not candidate.can_reach_selfsq(d, e, a, lower):
                    continue

                continuous += 1
                row_cont += 1
                survives, _, _, witness, _ = model.can_reach_selfsq(d, e, a, lower)
                if not survives or witness is None:
                    raise ValueError("32-21ad zero-prune witness regression")
                u, v = witness
                residue = mapping.residue(d, e, a, u, v)
                if residue is None:
                    raise ValueError("witness residue missing")
                class_id = mapping.residue_to_class_id[residue]
                old_penalty = old_penalties[class_id]
                penalty = true_penalties[class_id]
                if penalty > old_penalty:
                    witness_stronger += 1
                penalty_counts[frac_key(penalty)] += 1

                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("witness affine origin missing")
                margin_num = projected_margin_numerator(rank2, z0, lower, u, v)
                margin = Fraction(margin_num, OBJECTIVE_DENOMINATOR)
                ok = margin >= penalty

                if penalty > 0:
                    positive_witness_penalties += 1
                    ratio = margin / penalty
                    if min_slack_ratio is None or ratio < min_slack_ratio:
                        min_slack_ratio = ratio
                    slack_margin = margin - penalty
                    if min_slack_margin is None or slack_margin < min_slack_margin:
                        min_slack_margin = slack_margin
                    ratio_lt_2 += ratio < 2
                    ratio_lt_4 += ratio < 4
                    ratio_lt_8 += ratio < 8
                    ratio_lt_16 += ratio < 16

                if ok:
                    witness_pass += 1
                    row_pass += 1
                else:
                    witness_fail += 1
                    row_fail += 1
                    if len(fail_examples) < args.example_limit:
                        fail_examples.append({
                            "row_id": row_id,
                            "e": e,
                            "a": a,
                            "u": u,
                            "v": v,
                            "class_id": class_id,
                            "old_aa_penalty": frac_key(old_penalty),
                            "true_antifixed_coordinate_penalty": frac_key(penalty),
                            "projected_margin": frac_key(margin),
                        })
                decision_stream.update(
                    f"{row_id}|{e}|{a}|{class_id}|{frac_key(old_penalty)}|{frac_key(penalty)}|{margin_num}|{int(ok)}\n".encode()
                )

        row_summaries.append({
            "row_id": row_id,
            "continuous_kkt_survivors": row_cont,
            "existing_witness_passes_true_antifixed_coordinate_penalty": row_pass,
            "existing_witness_fails_true_antifixed_coordinate_penalty": row_fail,
        })

    if witness_pass + witness_fail != continuous:
        raise ValueError("true anti-fixed witness accounting regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ag",
        "mode": "EXACT_COORDINATE_CAUCHY_BOUND_RESTRICTED_TO_TRUE_REYNOLDS_ANTI_FIXED_KERNEL_ON_DETERMINISTIC_ROW_SHARD",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
        "reynolds_group_order": GROUP_ORDER,
        "anti_fixed_rank": EXPECTED_ANTI_FIXED_RANK,
        "anti_fixed_basis_sha256": csha([[str(K[i, j]) for j in range(K.cols)] for i in range(K.rows)]),
        "anti_fixed_positive_gram_sha256": csha([[str(positive_gram[i, j]) for j in range(positive_gram.cols)] for i in range(positive_gram.rows)]),
        "anti_fixed_ldl_positive_exact": True,
        "true_coordinate_dual_norm_sha256": csha([[v.numerator, v.denominator] for v in true_dual_norms_t]),
        "old_slice_kernel_coordinate_dual_norm_sha256": csha([[v.numerator, v.denominator] for v in aa.coordinate_dual_norms]),
        "coordinate_dual_norm_strictly_smaller_count": strictly_smaller_dual_norms,
        "coordinate_dual_norm_equal_count": equal_dual_norms,
        "projection_class_count": len(mapping.sorted_projection_residues),
        "projection_classes_strictly_improved_over_32_21aa": classes_improved,
        "zero_norm_nonzero_residue_count": zero_norm_nonzero_residue_count,
        "maximum_class_penalty_improvement_ratio": (
            frac_key(max(improvement_ratios)) if improvement_ratios else "1/1"
        ),
        "row_shards": args.row_shards,
        "shard_index": args.shard_index,
        "selected_rows": selected_rows,
        "continuous_kkt_survivors": continuous,
        "existing_witness_penalty_strictly_stronger_than_32_21aa": witness_stronger,
        "existing_witness_passes_true_antifixed_coordinate_penalty": witness_pass,
        "existing_witness_fails_true_antifixed_coordinate_penalty": witness_fail,
        "positive_witness_penalty_count": positive_witness_penalties,
        "minimum_projected_margin_over_true_penalty_ratio": (
            frac_key(min_slack_ratio) if min_slack_ratio is not None else None
        ),
        "minimum_projected_margin_minus_true_penalty": (
            frac_key(min_slack_margin) if min_slack_margin is not None else None
        ),
        "witness_ratio_below_threshold_counts": {
            "2": ratio_lt_2,
            "4": ratio_lt_4,
            "8": ratio_lt_8,
            "16": ratio_lt_16,
        },
        "true_penalty_population_counts_on_existing_witnesses": dict(sorted(penalty_counts.items())),
        "witness_fail_examples": fail_examples,
        "decision_stream_sha256": decision_stream.hexdigest(),
        "row_summaries": row_summaries,
        "proof": {
            "P_equals_N_over_64": True,
            "N_squared_equals_64N": True,
            "q_equals_x_minus_Px_implies_Nq_zero": True,
            "phiN_equals_64phi_implies_kerN_subset_kerphi": True,
            "anti_fixed_kernel_dimension_exactly_59": True,
            "negative_picard_gram_positive_definite_on_kerN": True,
            "coordinate_dual_norms_computed_exactly_on_kerN": True,
            "kerN_coordinate_dual_norm_no_larger_than_slice_kernel_dual_norm": True,
            "same_fractional_coordinate_congruence_q_i_equals_minus_residue_i_over_64_mod_Z": True,
            "coordinate_cauchy_lower_bound_exact": True,
        },
        "interpretation": {
            "existing_witness_pass_proves_slice_survives_this_true_antifixed_coordinate_strengthening": True,
            "existing_witness_fail_does_not_prove_slice_prunable": True,
            "witness_fail_requires_exact_search_over_other_rank2_integer_pairs": True,
            "diagnostic_is_representative_strategy_reconnaissance_not_full178_numerical_credit": True,
            "no_59d_closest_vector_search_run": True,
            "no_legacy_prefix_DFS_run": True,
            "no_terminal_family_materialization_run": True,
        },
        "firewalls": {
            "unknown_is_unsat": False,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_STAGE32_21AG_TRUE_ANTIFIXED_COORDINATE_PENALTY_DIAGNOSTIC",
        "dual_norms_strictly_smaller": strictly_smaller_dual_norms,
        "classes_improved": classes_improved,
        "continuous_survivors": continuous,
        "witness_stronger": witness_stronger,
        "witness_pass": witness_pass,
        "witness_fail": witness_fail,
        "min_margin_over_penalty": frac_key(min_slack_ratio) if min_slack_ratio is not None else None,
        "ratio_lt_2": ratio_lt_2,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
