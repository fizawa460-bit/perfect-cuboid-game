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
from sympy import Matrix, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound
from direct_picard_reynolds_rank2_integer_qp import OBJECTIVE_DENOMINATOR, dot, quad
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter

GROUP_ORDER = 64
PICARD_RANK = 64
EXPECTED_SLICE_RANK = 3
EXPECTED_SLICE_KERNEL_RANK = 61
EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
SCHEMA = "STAGE32_21AF_PAIR_PENALTY_WITNESS_RECONNAISSANCE_V1"


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


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def pair_modular_lower_bound(
    q11: Fraction,
    q12: Fraction,
    q22: Fraction,
    residue1: int,
    residue2: int,
) -> Fraction:
    """Exact minimum anti-fixed norm from two coordinate congruences.

    Q=[[q11,q12],[q12,q22]] is the dual Gram of two coordinate
    functionals on the positive slice-kernel norm. For exact coordinate values
    y, the minimum norm is y^T Q^{-1} y. The anti-fixed coordinates are fixed
    only modulo Z by the projection residue, so minimize this quadratic over
    y=(r1/64+n, r2/64+m), n,m in Z. The 2D CVP is solved exactly by reducing
    the second coordinate for each first-coordinate integer and using the
    one-coordinate bound x^2/q11 to terminate the finite search.
    """
    det = q11 * q22 - q12 * q12
    if q11 <= 0 or q22 <= 0 or det <= 0:
        raise ValueError("pair dual Gram must be positive definite")

    d1 = Fraction(int(residue1), GROUP_ORDER)
    d2 = Fraction(int(residue2), GROUP_ORDER)

    # Inverse-Q numerator form:
    # norm = (q22*x^2 - 2*q12*x*y + q11*y^2) / det.
    def evaluate_n(n: int) -> Fraction:
        x = Fraction(n, 1) + d1
        target_m = (q12 * x / q11) - d2
        mf = floor_fraction(target_m)
        best_local: Fraction | None = None
        for m in (mf, mf + 1):
            y = Fraction(m, 1) + d2
            numerator = q22 * x * x - 2 * q12 * x * y + q11 * y * y
            value = numerator / det
            if best_local is None or value < best_local:
                best_local = value
        if best_local is None:
            raise RuntimeError("pair CVP local candidate set unexpectedly empty")
        return best_local

    target_n = -d1
    nf = floor_fraction(target_n)
    best = min(evaluate_n(nf), evaluate_n(nf + 1))

    left = nf - 1
    right = nf + 2
    while True:
        left_x = Fraction(left, 1) + d1
        right_x = Fraction(right, 1) + d1
        left_can_improve = left_x * left_x / q11 < best
        right_can_improve = right_x * right_x / q11 < best
        if not left_can_improve and not right_can_improve:
            break
        if left_can_improve:
            best = min(best, evaluate_n(left))
            left -= 1
        if right_can_improve:
            best = min(best, evaluate_n(right))
            right += 1
    return best


def build_coordinate_dual_gram(marking: dict, bundle: dict, expected_diagonal: tuple[Fraction, ...]) -> tuple[tuple[Fraction, ...], ...]:
    # Rebuild independently from the retained slice functionals rather than
    # extending the audited 32-21aa object with un-audited hidden state.
    _ = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])
    if phi.shape != (EXPECTED_SLICE_RANK, PICARD_RANK) or int(phi.rank()) != EXPECTED_SLICE_RANK:
        raise ValueError("slice functional rank regression")

    phi_dm = DomainMatrix.from_Matrix(phi).convert_to(ZZ)
    D_dm, S_dm, T_dm = smith_normal_decomp(phi_dm)
    if S_dm * phi_dm * T_dm != D_dm:
        raise ValueError("slice Smith reconstruction regression")
    T = T_dm.to_Matrix()
    kernel = T[:, EXPECTED_SLICE_RANK:]
    if kernel.shape != (PICARD_RANK, EXPECTED_SLICE_KERNEL_RANK):
        raise ValueError("slice kernel shape regression")
    if phi * kernel != Matrix.zeros(EXPECTED_SLICE_RANK, EXPECTED_SLICE_KERNEL_RANK):
        raise ValueError("slice kernel functional regression")

    positive_gram = -(kernel.T * gram * kernel)
    if positive_gram != positive_gram.T:
        raise ValueError("slice kernel positive Gram symmetry regression")
    inverse = positive_gram.inv()
    dual = kernel * inverse * kernel.T
    result = tuple(
        tuple(as_fraction(dual[i, j]) for j in range(PICARD_RANK))
        for i in range(PICARD_RANK)
    )
    diagonal = tuple(result[i][i] for i in range(PICARD_RANK))
    if diagonal != expected_diagonal:
        raise ValueError("independently rebuilt coordinate dual Gram diagonal disagrees with audited 32-21aa")
    return result


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
    ap.add_argument("--top-coordinates", type=int, default=12)
    ap.add_argument("--example-limit", type=int, default=24)
    args = ap.parse_args()

    if args.row_shards <= 0 or not 0 <= args.shard_index < args.row_shards:
        raise ValueError("invalid deterministic row shard")
    if not 2 <= args.top_coordinates <= PICARD_RANK:
        raise ValueError("--top-coordinates must be in [2,64]")

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed or claimed != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    bundle = load_module_payload(args.retained, "stage32_21af_picard")
    marking = load_module_payload(args.marking, "stage32_21af_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("32-21ac audited evaluator certificate regression")
    mapping = model.mapping
    aa = mapping.penalty
    rank2 = model.rank2

    dual = build_coordinate_dual_gram(marking, bundle, aa.coordinate_dual_norms)

    aa_penalties: list[Fraction] = []
    active_counts: Counter[int] = Counter()
    for residue in mapping.sorted_projection_residues:
        p = aa.lower_bound_from_residue(residue)
        aa_penalties.append(p)
        for i, raw in enumerate(residue):
            dist = min(int(raw), GROUP_ORDER - int(raw))
            if dist == 0 or aa.coordinate_dual_norms[i] <= 0:
                continue
            candidate = Fraction(dist * dist, GROUP_ORDER * GROUP_ORDER) / aa.coordinate_dual_norms[i]
            if candidate == p:
                active_counts[i] += 1

    ranked_coordinates = sorted(
        (i for i in range(PICARD_RANK) if aa.coordinate_dual_norms[i] > 0),
        key=lambda i: (-active_counts[i], i),
    )
    selected_coordinates = tuple(ranked_coordinates[: args.top_coordinates])
    pairs: list[tuple[int, int]] = []
    for p, i in enumerate(selected_coordinates):
        for j in selected_coordinates[p + 1 :]:
            det = dual[i][i] * dual[j][j] - dual[i][j] * dual[i][j]
            if det > 0:
                pairs.append((i, j))
    if not pairs:
        raise ValueError("no positive-definite coordinate pairs selected")

    best_pair_penalties: list[Fraction] = []
    classes_strictly_improved = 0
    pair_win_counts: Counter[str] = Counter()
    for class_id, residue in enumerate(mapping.sorted_projection_residues):
        best = aa_penalties[class_id]
        winning_pair: tuple[int, int] | None = None
        for i, j in pairs:
            candidate = pair_modular_lower_bound(
                dual[i][i], dual[i][j], dual[j][j], residue[i], residue[j]
            )
            # Adding coordinate constraints cannot be weaker than either single
            # coordinate bound, hence cannot undercut the audited aa maximum if
            # this pair contains its active coordinate; other pairs may be lower.
            if candidate > best:
                best = candidate
                winning_pair = (i, j)
        best_pair_penalties.append(best)
        if best > aa_penalties[class_id]:
            classes_strictly_improved += 1
            if winning_pair is not None:
                pair_win_counts[f"{winning_pair[0]},{winning_pair[1]}"] += 1

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    selected_rows = [row for idx, row in enumerate(all_rows) if idx % args.row_shards == args.shard_index]
    if len(all_rows) != 178 or not selected_rows:
        raise ValueError("FULL178 row selection regression")

    kkt = rank2.orbit_qp
    bound = rank2.bound
    bridge = rank2.bridge
    continuous = 0
    witness_pair_pass = 0
    witness_pair_fail = 0
    witness_pair_stronger_than_aa = 0
    fail_examples: list[dict] = []
    row_summaries: list[dict] = []
    decision_stream = hashlib.sha256()

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
                if not bridge.target_in_image(d, e, a):
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
                aa_penalty = aa_penalties[class_id]
                pair_penalty = best_pair_penalties[class_id]
                if pair_penalty < aa_penalty:
                    raise ValueError("pair reconnaissance penalty undercut audited aa penalty")
                if pair_penalty > aa_penalty:
                    witness_pair_stronger_than_aa += 1

                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("witness affine origin missing")
                margin_num = projected_margin_numerator(rank2, z0, lower, u, v)
                pair_ok = margin_num * pair_penalty.denominator >= OBJECTIVE_DENOMINATOR * pair_penalty.numerator
                if pair_ok:
                    witness_pair_pass += 1
                    row_pass += 1
                else:
                    witness_pair_fail += 1
                    row_fail += 1
                    if len(fail_examples) < args.example_limit:
                        fail_examples.append({
                            "row_id": row_id,
                            "e": e,
                            "a": a,
                            "u": u,
                            "v": v,
                            "class_id": class_id,
                            "aa_penalty": frac_key(aa_penalty),
                            "best_tested_pair_penalty": frac_key(pair_penalty),
                            "projected_margin": f"{margin_num}/{OBJECTIVE_DENOMINATOR}",
                        })
                decision_stream.update(
                    f"{row_id}|{e}|{a}|{class_id}|{frac_key(aa_penalty)}|{frac_key(pair_penalty)}|{margin_num}|{int(pair_ok)}\n".encode()
                )

        row_summaries.append({
            "row_id": row_id,
            "continuous_kkt_survivors": row_cont,
            "existing_witness_passes_best_tested_pair_penalty": row_pass,
            "existing_witness_fails_best_tested_pair_penalty": row_fail,
        })

    if witness_pair_pass + witness_pair_fail != continuous:
        raise ValueError("pair witness accounting regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21af",
        "mode": "TOP_AA_ACTIVE_COORDINATE_PAIR_EXACT_MODULAR_LOWER_BOUND_RECONNAISSANCE_ON_DETERMINISTIC_ROW_SHARD",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
        "selected_coordinates": list(selected_coordinates),
        "selected_coordinate_active_counts": {str(i): active_counts[i] for i in selected_coordinates},
        "tested_positive_definite_pair_count": len(pairs),
        "tested_pairs": [[i, j] for i, j in pairs],
        "projection_classes": len(mapping.sorted_projection_residues),
        "projection_classes_strictly_improved_over_aa_coordinate_max": classes_strictly_improved,
        "pair_winner_counts_on_improved_classes": dict(sorted(pair_win_counts.items())),
        "row_shards": args.row_shards,
        "shard_index": args.shard_index,
        "selected_rows": selected_rows,
        "continuous_kkt_survivors": continuous,
        "existing_witness_pair_penalty_strictly_stronger_than_aa": witness_pair_stronger_than_aa,
        "existing_witness_passes_best_tested_pair_penalty": witness_pair_pass,
        "existing_witness_fails_best_tested_pair_penalty": witness_pair_fail,
        "witness_fail_examples": fail_examples,
        "decision_stream_sha256": decision_stream.hexdigest(),
        "row_summaries": row_summaries,
        "interpretation": {
            "pair_bound_exact_for_each_tested_coordinate_pair_and_residue": True,
            "coordinate_pair_search_is_reconnaissance_not_exhaustive_over_all_pairs": True,
            "existing_witness_pair_pass_proves_slice_survives_tested_pair_strengthening": True,
            "existing_witness_pair_fail_does_not_prove_slice_prunable": True,
            "witness_fail_requires_exact_search_over_other_rank2_integer_pairs": True,
            "not_full178_numerical_credit": True,
            "no_59d_antifixed_CVP_run": True,
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
        "verdict": "PASS_STAGE32_21AF_PAIR_PENALTY_WITNESS_RECONNAISSANCE",
        "tested_pairs": len(pairs),
        "classes_improved": classes_strictly_improved,
        "continuous_survivors": continuous,
        "witness_pair_stronger": witness_pair_stronger_than_aa,
        "witness_pair_pass": witness_pair_pass,
        "witness_pair_fail": witness_pair_fail,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
