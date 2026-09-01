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

from direct_picard_reynolds_lattice_diagnostic import exact_column_lattice_basis_lowrank
from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound
from direct_picard_reynolds_rank2_integer_qp import OBJECTIVE_DENOMINATOR, dot, quad
from direct_picard_reynolds_rank2_integral_projection_bound import build_reynolds_numerator
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter

GROUP_ORDER = 64
PICARD_RANK = 64
FIXED_RANK = 5
ANTI_FIXED_RANK = 59
EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
SCHEMA = "STAGE32_21AH_ORIGINAL_HALFSPACE_INTEGRALITY_ANTIFIXED_DIAGNOSTIC_V1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def as_fraction(value: sympy.Expr) -> Fraction:
    return Fraction(int(sympy.numer(value)), int(sympy.denom(value)))


def frac_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


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


def coordinate_penalty(residue: tuple[int, ...], dual_norms: tuple[Fraction, ...]) -> Fraction:
    best = Fraction(0, 1)
    for raw, dn in zip(residue, dual_norms):
        dist = min(int(raw), GROUP_ORDER - int(raw))
        if dist == 0:
            continue
        if dn == 0:
            raise ValueError("nonzero coordinate residue on a functional vanishing on ker(N)")
        candidate = Fraction(dist * dist, GROUP_ORDER * GROUP_ORDER) / dn
        if candidate > best:
            best = candidate
    return best


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
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed_manifest or claimed_manifest != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    bundle = load_module_payload(args.retained, "stage32_21ah_picard")
    marking = load_module_payload(args.marking, "stage32_21ah_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("32-21ac audited evaluator certificate regression")

    rank2 = model.rank2
    mapping = model.mapping
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])
    N, _, _ = build_reynolds_numerator(marking, adapter, gram, phi)
    if N * N != GROUP_ORDER * N or N.T * gram != gram * N or phi * N != GROUP_ORDER * phi:
        raise ValueError("Reynolds structural identity regression")

    null = N.nullspace()
    if len(null) != ANTI_FIXED_RANK:
        raise ValueError(f"anti-fixed nullity regression: {len(null)}")
    K = Matrix.hstack(*null)
    if N * K != Matrix.zeros(PICARD_RANK, ANTI_FIXED_RANK):
        raise ValueError("anti-fixed basis regression")
    if phi * K != Matrix.zeros(3, ANTI_FIXED_RANK):
        raise ValueError("ker(N) not contained in slice kernel")

    positive_gram = -(K.T * gram * K)
    L, D = positive_gram.LDLdecomposition(hermitian=False)
    if L * D * L.T != positive_gram or any(D[i, i] <= 0 for i in range(D.rows)):
        raise ValueError("anti-fixed positive Gram regression")
    inverse = positive_gram.inv()

    true_coordinate_dual_norms = tuple(
        as_fraction((K[i, :] * inverse * K[i, :].T)[0])
        for i in range(PICARD_RANK)
    )
    if any(new > old for new, old in zip(true_coordinate_dual_norms, mapping.penalty.coordinate_dual_norms)):
        raise ValueError("true anti-fixed coordinate dual norm exceeded slice-kernel norm")

    pairing = adapter.pairing_matrix
    if pairing.rows != 140 or pairing.cols != PICARD_RANK:
        raise ValueError(f"original halfspace pairing shape regression: {pairing.shape}")
    halfspace_dual_norms = []
    for i in range(pairing.rows):
        restricted = pairing[i, :] * K
        halfspace_dual_norms.append(as_fraction((restricted * inverse * restricted.T)[0]))
    halfspace_dual_norms_t = tuple(halfspace_dual_norms)

    Bmat, module_stats = exact_column_lattice_basis_lowrank(N, FIXED_RANK)
    if Bmat.shape != (PICARD_RANK, FIXED_RANK):
        raise ValueError("fixed image basis shape regression")
    pairing_B = pairing * Bmat

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    if len(all_rows) != 178 or len(set(all_rows)) != 178:
        raise ValueError("FULL178 row population regression")
    selected_rows = [row for idx, row in enumerate(all_rows) if idx % args.row_shards == args.shard_index]
    if not selected_rows:
        raise ValueError("selected row shard empty")

    kkt = rank2.orbit_qp
    bound = rank2.bound
    bridge2 = rank2.bridge
    k0, k1 = rank2.kernel_columns

    cache: dict[tuple[int, ...], tuple[Fraction, Fraction, Fraction, int | None]] = {}
    continuous = 0
    witness_pass = witness_fail = 0
    halfspace_stronger = combined_stronger_than_aa = 0
    positive_penalty_count = 0
    min_ratio: Fraction | None = None
    min_slack: Fraction | None = None
    ratio_lt_2 = ratio_lt_4 = ratio_lt_8 = ratio_lt_16 = ratio_lt_64 = ratio_lt_128 = ratio_lt_256 = 0
    winning_halfspaces: Counter[int] = Counter()
    combined_penalty_counts: Counter[str] = Counter()
    fail_examples: list[dict] = []
    decision_stream = hashlib.sha256()
    row_summaries: list[dict] = []

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
                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("witness affine origin missing")
                z = tuple(z0[i] + k0[i] * u + k1[i] * v for i in range(FIXED_RANK))
                zmod = tuple(value % GROUP_ORDER for value in z)

                cached = cache.get(zmod)
                if cached is None:
                    residue = mapping.residue(d, e, a, u, v)
                    if residue is None:
                        raise ValueError("witness residue missing")
                    expected_residue = tuple(
                        sum(int(Bmat[i, j]) * zmod[j] for j in range(FIXED_RANK)) % GROUP_ORDER
                        for i in range(PICARD_RANK)
                    )
                    if residue != expected_residue:
                        raise ValueError("fixed-basis residue reconstruction regression")

                    coord_pen = coordinate_penalty(residue, true_coordinate_dual_norms)
                    half_pen = Fraction(0, 1)
                    winner: int | None = None
                    for hi in range(pairing.rows):
                        raw = sum(int(pairing_B[hi, j]) * zmod[j] for j in range(FIXED_RANK)) % GROUP_ORDER
                        dist = min(raw, GROUP_ORDER - raw)
                        if dist == 0:
                            continue
                        dn = halfspace_dual_norms_t[hi]
                        if dn == 0:
                            raise ValueError("nonintegral halfspace fixed pairing on a functional vanishing on ker(N)")
                        cand = Fraction(dist * dist, GROUP_ORDER * GROUP_ORDER) / dn
                        if cand > half_pen:
                            half_pen = cand
                            winner = hi
                    combined = max(coord_pen, half_pen)
                    cache[zmod] = (coord_pen, half_pen, combined, winner)
                    cached = cache[zmod]

                coord_pen, half_pen, combined, winner = cached
                aa_pen = mapping.penalty.lower_bound_from_residue(mapping.residue(d, e, a, u, v))
                if coord_pen < aa_pen or combined < coord_pen:
                    raise ValueError("strengthened penalty ordering regression")
                if half_pen > coord_pen:
                    halfspace_stronger += 1
                    if winner is not None:
                        winning_halfspaces[winner] += 1
                if combined > aa_pen:
                    combined_stronger_than_aa += 1
                combined_penalty_counts[frac_key(combined)] += 1

                # The 12 fixed halfspaces are exact orbit averages of the 140 rows.
                # Recheck nonnegativity on the actual witness z before interpreting
                # halfspace pairing congruences as an original-lift necessary condition.
                if any(sum(int(pairing_B[hi, j]) * z[j] for j in range(FIXED_RANK)) < 0 for hi in range(pairing.rows)):
                    raise ValueError("rank2 witness violated an original fixed-orbit halfspace average")

                margin_num = projected_margin_numerator(rank2, z0, lower, u, v)
                margin = Fraction(margin_num, OBJECTIVE_DENOMINATOR)
                ok = margin >= combined
                if combined > 0:
                    positive_penalty_count += 1
                    ratio = margin / combined
                    slack = margin - combined
                    if min_ratio is None or ratio < min_ratio:
                        min_ratio = ratio
                    if min_slack is None or slack < min_slack:
                        min_slack = slack
                    ratio_lt_2 += ratio < 2
                    ratio_lt_4 += ratio < 4
                    ratio_lt_8 += ratio < 8
                    ratio_lt_16 += ratio < 16
                    ratio_lt_64 += ratio < 64
                    ratio_lt_128 += ratio < 128
                    ratio_lt_256 += ratio < 256

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
                            "true_coordinate_penalty": frac_key(coord_pen),
                            "halfspace_integrality_penalty": frac_key(half_pen),
                            "combined_penalty": frac_key(combined),
                            "projected_margin": frac_key(margin),
                            "winning_halfspace_index": winner,
                        })
                decision_stream.update(
                    f"{row_id}|{e}|{a}|{u}|{v}|{frac_key(coord_pen)}|{frac_key(half_pen)}|{frac_key(combined)}|{margin_num}|{int(ok)}\n".encode()
                )

        row_summaries.append({
            "row_id": row_id,
            "continuous_kkt_survivors": row_cont,
            "existing_witness_passes_combined_halfspace_integrality_penalty": row_pass,
            "existing_witness_fails_combined_halfspace_integrality_penalty": row_fail,
        })

    if witness_pass + witness_fail != continuous:
        raise ValueError("21ah witness accounting regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ah",
        "mode": "ORIGINAL_140_INTEGRAL_HALFSPACE_FUNCTIONAL_MOD1_CAUCHY_BOUND_ON_TRUE_REYNOLDS_ANTIFIXED_KERNEL",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
        "anti_fixed_rank": ANTI_FIXED_RANK,
        "original_halfspace_count": pairing.rows,
        "fixed_image_column_module_stats": module_stats,
        "anti_fixed_positive_gram_sha256": csha([[str(positive_gram[i, j]) for j in range(positive_gram.cols)] for i in range(positive_gram.rows)]),
        "true_coordinate_dual_norm_sha256": csha([[v.numerator, v.denominator] for v in true_coordinate_dual_norms]),
        "halfspace_dual_norm_sha256": csha([[v.numerator, v.denominator] for v in halfspace_dual_norms_t]),
        "halfspace_dual_norm_zero_count": sum(v == 0 for v in halfspace_dual_norms_t),
        "row_shards": args.row_shards,
        "shard_index": args.shard_index,
        "selected_rows": selected_rows,
        "continuous_kkt_survivors": continuous,
        "unique_fixed_z_mod64_states_at_existing_witnesses": len(cache),
        "existing_witness_halfspace_penalty_strictly_stronger_than_true_coordinate_penalty": halfspace_stronger,
        "existing_witness_combined_penalty_strictly_stronger_than_32_21aa": combined_stronger_than_aa,
        "existing_witness_passes_combined_halfspace_integrality_penalty": witness_pass,
        "existing_witness_fails_combined_halfspace_integrality_penalty": witness_fail,
        "positive_witness_penalty_count": positive_penalty_count,
        "minimum_projected_margin_over_combined_penalty_ratio": frac_key(min_ratio) if min_ratio is not None else None,
        "minimum_projected_margin_minus_combined_penalty": frac_key(min_slack) if min_slack is not None else None,
        "witness_ratio_below_threshold_counts": {
            "2": ratio_lt_2,
            "4": ratio_lt_4,
            "8": ratio_lt_8,
            "16": ratio_lt_16,
            "64": ratio_lt_64,
            "128": ratio_lt_128,
            "256": ratio_lt_256,
        },
        "winning_halfspace_indices_when_stronger_than_coordinate": {str(k): v for k, v in sorted(winning_halfspaces.items())},
        "combined_penalty_population_counts": dict(sorted(combined_penalty_counts.items())),
        "witness_fail_examples": fail_examples,
        "decision_stream_sha256": decision_stream.hexdigest(),
        "row_summaries": row_summaries,
        "proof": {
            "P_equals_N_over_64": True,
            "q_equals_x_minus_Px_lies_in_kerN": True,
            "original_halfspace_pairing_of_integral_x_is_integer": True,
            "halfspace_pairing_fractional_class_of_q_determined_by_fixed_projection_mod64": True,
            "dual_norms_restricted_to_true_kerN": True,
            "one_functional_cauchy_bound_safe": True,
            "max_over_140_and_true_coordinate_penalties_safe": True,
        },
        "interpretation": {
            "existing_witness_pass_proves_slice_survives_this_21ah_strengthening": True,
            "existing_witness_fail_does_not_prove_slice_prunable": True,
            "witness_fail_requires_exact_search_over_other_rank2_integer_pairs": True,
            "representative_strategy_diagnostic_not_full178_numerical_credit": True,
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
        "verdict": "PASS_STAGE32_21AH_ORIGINAL_HALFSPACE_INTEGRALITY_ANTIFIXED_DIAGNOSTIC",
        "continuous_survivors": continuous,
        "unique_zmod": len(cache),
        "halfspace_stronger": halfspace_stronger,
        "combined_stronger_than_aa": combined_stronger_than_aa,
        "witness_pass": witness_pass,
        "witness_fail": witness_fail,
        "min_margin_over_penalty": frac_key(min_ratio) if min_ratio is not None else None,
        "ratio_lt_2": ratio_lt_2,
        "ratio_lt_16": ratio_lt_16,
        "ratio_lt_256": ratio_lt_256,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
