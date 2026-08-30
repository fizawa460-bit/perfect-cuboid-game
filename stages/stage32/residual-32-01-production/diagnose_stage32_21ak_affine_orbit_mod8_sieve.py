#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from sympy import Matrix, ZZ, eye
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from z3 import Int, Mod, Solver, sat, unsat, unknown, get_version_string

from diagnose_stage32_21aj_2adic_pairing_saturation import (
    build_certificate as build_21aj_certificate,
    integer_coordinate_matrix,
)
from direct_picard_reynolds_lattice_diagnostic import (
    EXPECTED_FIXED_RANK,
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    exact_column_lattice_basis_lowrank,
)
from direct_picard_reynolds_rank2_antifixed_coset_bound import (
    ReynoldsRank2AntiFixedCosetBound,
)
from direct_picard_reynolds_rank2_integral_projection_bound import (
    build_reynolds_numerator,
)
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_ANTI_RANK = PICARD_RANK - EXPECTED_FIXED_RANK
EXPECTED_CURVE_COUNT = 140
EXPECTED_ORBIT_COUNT = 14
EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_21AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_21AJ_CERTIFICATE_SHA256 = "e360d4277135c5191c23e7f422ab669eb20d3363f0ff054073796c12e65598d0"
MODULUS = 8
SCHEMA = "STAGE32_21AK_AFFINE_ORBIT_MOD8_MEMBERSHIP_SIEVE_V1"


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


def nonzero_smith_diagonal(d: Matrix) -> tuple[int, ...]:
    out = []
    for i in range(min(d.rows, d.cols)):
        v = int(d[i, i])
        if v:
            out.append(v)
    return tuple(out)


def deterministic_sample(
    row_id: str,
    e: int,
    a: int,
    u: int,
    v: int,
    sample_modulus: int,
    sample_remainder: int,
) -> bool:
    raw = f"{row_id}|{e}|{a}|{u}|{v}".encode()
    value = int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")
    return value % sample_modulus == sample_remainder


def build_orbits(subgroup: tuple[tuple[int, ...], ...] | list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    unvisited = set(range(EXPECTED_CURVE_COUNT))
    orbits: list[tuple[int, ...]] = []
    while unvisited:
        seed = min(unvisited)
        orbit = tuple(sorted({g[seed] for g in subgroup}))
        if not orbit:
            raise ValueError("empty stabilizer orbit")
        orbits.append(orbit)
        unvisited.difference_update(orbit)
    if len(orbits) != EXPECTED_ORBIT_COUNT:
        raise ValueError(f"stabilizer orbit count regression: {len(orbits)}")
    return orbits


def z3_mod8_orbit_feasible(
    y0: tuple[int, ...],
    translation: Matrix,
    orbits: list[tuple[int, ...]],
    orbit_totals: tuple[int, ...],
    timeout_ms: int,
) -> tuple[str, tuple[int, ...] | None, tuple[int, ...] | None]:
    t = [Int(f"t_{j}") for j in range(translation.cols)]
    solver = Solver()
    solver.set(timeout=timeout_ms)
    for var in t:
        solver.add(var >= 0, var < MODULUS)

    residue_exprs = []
    for i in range(translation.rows):
        expr = y0[i]
        for j in range(translation.cols):
            coeff = int(translation[i, j]) % MODULUS
            if coeff:
                expr += coeff * t[j]
        residue_exprs.append(Mod(expr, MODULUS))

    for oi, orbit in enumerate(orbits):
        total = orbit_totals[oi]
        if total < 0:
            raise ValueError("negative fixed orbit total reached mod8 sieve")
        solver.add(sum(residue_exprs[i] for i in orbit) <= total)

    result = solver.check()
    if result == unknown:
        return "UNKNOWN", None, None
    if result == unsat:
        return "UNSAT", None, None
    if result != sat:
        raise ValueError(f"unexpected z3 result: {result}")

    model = solver.model()
    tvals = tuple(int(model.eval(var, model_completion=True).as_long()) for var in t)
    residues = []
    for i in range(translation.rows):
        raw = y0[i] + sum(int(translation[i, j]) * tvals[j] for j in range(translation.cols))
        residues.append(raw % MODULUS)

    orbit_minimal_sums = tuple(sum(residues[i] for i in orbit) for orbit in orbits)
    for minimal, total in zip(orbit_minimal_sums, orbit_totals):
        if minimal > total or (total - minimal) % MODULUS:
            raise ValueError("SAT model failed exact nonnegative-composition residue reconstruction")
    return "SAT", tvals, orbit_minimal_sums


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--row-shards", type=int, default=16)
    ap.add_argument("--shard-index", type=int, default=0)
    ap.add_argument("--sample-modulus", type=int, default=256)
    ap.add_argument("--sample-remainder", type=int, default=0)
    ap.add_argument("--solver-timeout-ms", type=int, default=750)
    ap.add_argument("--example-limit", type=int, default=24)
    args = ap.parse_args()

    if args.row_shards <= 0 or not 0 <= args.shard_index < args.row_shards:
        raise ValueError("invalid deterministic row shard")
    if args.sample_modulus <= 0 or not 0 <= args.sample_remainder < args.sample_modulus:
        raise ValueError("invalid deterministic sample congruence")
    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    manifest = json.loads(args.manifest.read_text())
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed_manifest or claimed_manifest != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    bundle = load_module_payload(args.retained, "stage32_21ak_picard")
    marking = load_module_payload(args.marking, "stage32_21ak_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_21AC_CERTIFICATE_SHA256:
        raise ValueError("32-21ac audited evaluator certificate regression")

    # Rebuild the exact 32-21aj source-locked 2-primary structure before using
    # modulus 8 as the complete exponent needed for the finite pairing-image sieve.
    cert_21aj = build_21aj_certificate(marking, bundle)
    if cert_21aj["canonical_sha256_without_this_field"] != EXPECTED_21AJ_CERTIFICATE_SHA256:
        raise ValueError("32-21aj certificate regression")
    smith = cert_21aj["exact_smith_structure"]
    if smith["maximum_factor"] != MODULUS or smith["maximum_two_adic_exponent"] != 3:
        raise ValueError("32-21aj modulus lock regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    phi = Matrix(
        [
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ]
    )
    N, subgroup, action_hashes_sha = build_reynolds_numerator(marking, adapter, gram, phi)
    B, module_stats = exact_column_lattice_basis_lowrank(N, EXPECTED_FIXED_RANK)
    C = integer_coordinate_matrix(N, B)
    if B * C != N:
        raise ValueError("N=B*C regression")

    C_dm = DomainMatrix.from_Matrix(C).convert_to(ZZ)
    D_dm, S_dm, T_dm = smith_normal_decomp(C_dm)
    if S_dm * C_dm * T_dm != D_dm:
        raise ValueError("fixed-coordinate Smith reconstruction regression")
    D = D_dm.to_Matrix()
    S = S_dm.to_Matrix()
    T = T_dm.to_Matrix()
    diag = nonzero_smith_diagonal(D)
    if tuple(abs(v) for v in diag) != (1,) * EXPECTED_FIXED_RANK:
        raise ValueError(f"fixed-coordinate map not surjective: {diag}")

    D5 = Matrix.diag(*diag)
    right_inverse = T[:, :EXPECTED_FIXED_RANK] * D5.inv() * S
    if C * right_inverse != eye(EXPECTED_FIXED_RANK):
        raise ValueError("integer right inverse reconstruction regression")
    if any(v.q != 1 for v in right_inverse):
        raise ValueError("fixed-coordinate right inverse is not integral")

    K = T[:, EXPECTED_FIXED_RANK:]
    if K.shape != (PICARD_RANK, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed integer kernel shape regression")
    if N * K != Matrix.zeros(PICARD_RANK, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed integer kernel N-regression")

    pairing = adapter.pairing_matrix
    translation = pairing * K
    if translation.shape != (EXPECTED_CURVE_COUNT, EXPECTED_ANTI_RANK):
        raise ValueError("pairing translation lattice shape regression")
    if csha([[int(translation[i, j]) for j in range(translation.cols)] for i in range(translation.rows)]) != cert_21aj["initial_pairing_translation_lattice"]["sha256"]:
        raise ValueError("32-21aj pairing translation lattice hash regression")

    orbits = build_orbits(subgroup)
    orbit_sum = Matrix.zeros(len(orbits), EXPECTED_CURVE_COUNT)
    for oi, orbit in enumerate(orbits):
        for idx in orbit:
            orbit_sum[oi, idx] = 1
    if orbit_sum * translation != Matrix.zeros(len(orbits), EXPECTED_ANTI_RANK):
        raise ValueError("translation lattice changed a stabilizer orbit total")

    pairing_B = pairing * B
    rank2 = model.rank2
    kkt = rank2.orbit_qp
    bound = rank2.bound
    bridge2 = rank2.bridge
    k0, k1 = rank2.kernel_columns

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    if len(all_rows) != 178 or len(set(all_rows)) != 178:
        raise ValueError("FULL178 row population regression")
    selected_rows = [
        row for idx, row in enumerate(all_rows)
        if idx % args.row_shards == args.shard_index
    ]
    if not selected_rows:
        raise ValueError("selected row shard empty")

    continuous = 0
    sampled = 0
    sat_count = 0
    unsat_count = 0
    unknown_count = 0
    cache: dict[tuple[int, ...], tuple[str, tuple[int, ...] | None, tuple[int, ...] | None]] = {}
    unsat_examples: list[dict] = []
    unknown_examples: list[dict] = []
    sat_examples: list[dict] = []
    row_summaries: list[dict] = []
    decision_stream = hashlib.sha256()
    min_orbit_total: int | None = None
    max_orbit_total = 0
    max_sat_minimal_sum = 0

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_cont = row_sampled = row_sat = row_unsat = row_unknown = 0

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

                if not deterministic_sample(
                    row_id, e, a, u, v, args.sample_modulus, args.sample_remainder
                ):
                    continue

                sampled += 1
                row_sampled += 1
                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("rank2 affine origin missing")
                z = tuple(
                    int(z0[i] + k0[i] * u + k1[i] * v)
                    for i in range(EXPECTED_FIXED_RANK)
                )

                cached = cache.get(z)
                if cached is None:
                    zvec = Matrix(z)
                    x0 = right_inverse * zvec
                    if C * x0 != zvec or N * x0 != B * zvec:
                        raise ValueError("affine integral preimage reconstruction regression")
                    if any(v.q != 1 for v in x0):
                        raise ValueError("affine integral preimage became nonintegral")
                    y0m = pairing * x0
                    if any(v.q != 1 for v in y0m):
                        raise ValueError("integral lift produced nonintegral halfspace pairings")
                    y0 = tuple(int(v) for v in y0m)

                    orbit_totals = []
                    for orbit in orbits:
                        total = sum(y0[i] for i in orbit)
                        seed = orbit[0]
                        numerator = len(orbit) * sum(
                            int(pairing_B[seed, j]) * z[j]
                            for j in range(EXPECTED_FIXED_RANK)
                        )
                        if numerator % GROUP_ORDER:
                            raise ValueError("projected orbit total became nonintegral")
                        projected_total = numerator // GROUP_ORDER
                        if projected_total != total:
                            raise ValueError("integral-preimage and projected orbit totals disagree")
                        if total < 0:
                            raise ValueError("sampled rank2 witness has negative fixed orbit total")
                        orbit_totals.append(total)
                        min_orbit_total = total if min_orbit_total is None else min(min_orbit_total, total)
                        max_orbit_total = max(max_orbit_total, total)

                    cached = z3_mod8_orbit_feasible(
                        y0=y0,
                        translation=translation,
                        orbits=orbits,
                        orbit_totals=tuple(orbit_totals),
                        timeout_ms=args.solver_timeout_ms,
                    )
                    cache[z] = cached
                status, tvals, minimal_sums = cached

                if status == "SAT":
                    sat_count += 1
                    row_sat += 1
                    if minimal_sums is None:
                        raise ValueError("SAT status missing exact residue reconstruction")
                    max_sat_minimal_sum = max(max_sat_minimal_sum, max(minimal_sums, default=0))
                    if len(sat_examples) < args.example_limit:
                        sat_examples.append(
                            {
                                "row_id": row_id,
                                "e": e,
                                "a": a,
                                "u": u,
                                "v": v,
                                "z": list(z),
                                "mod8_translation_witness_sha256": csha(list(tvals or ())),
                                "orbit_minimal_residue_sums": list(minimal_sums),
                            }
                        )
                elif status == "UNSAT":
                    unsat_count += 1
                    row_unsat += 1
                    if len(unsat_examples) < args.example_limit:
                        unsat_examples.append(
                            {
                                "row_id": row_id,
                                "e": e,
                                "a": a,
                                "u": u,
                                "v": v,
                                "z": list(z),
                            }
                        )
                elif status == "UNKNOWN":
                    unknown_count += 1
                    row_unknown += 1
                    if len(unknown_examples) < args.example_limit:
                        unknown_examples.append(
                            {
                                "row_id": row_id,
                                "e": e,
                                "a": a,
                                "u": u,
                                "v": v,
                                "z": list(z),
                            }
                        )
                else:
                    raise ValueError(f"unexpected cached status: {status}")

                decision_stream.update(
                    f"{row_id}|{e}|{a}|{u}|{v}|{','.join(map(str, z))}|{status}\n".encode()
                )

        row_summaries.append(
            {
                "row_id": row_id,
                "continuous_kkt_survivors": row_cont,
                "deterministically_sampled_existing_witnesses": row_sampled,
                "mod8_affine_orbit_sat": row_sat,
                "mod8_affine_orbit_unsat": row_unsat,
                "mod8_affine_orbit_unknown": row_unknown,
            }
        )

    if sampled != sat_count + unsat_count + unknown_count:
        raise ValueError("21ak sampled decision accounting regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ak",
        "mode": "EXACT_MOD8_AFFINE_PAIRING_IMAGE_NECESSARY_SIEVE_WITH_NONNEGATIVE_ORBIT_COMPOSITIONS",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_21AC_CERTIFICATE_SHA256,
        "upstream_32_21aj_certificate_sha256": EXPECTED_21AJ_CERTIFICATE_SHA256,
        "z3_version": get_version_string(),
        "modulus": MODULUS,
        "modulus_justification": {
            "maximum_21aj_smith_factor": smith["maximum_factor"],
            "maximum_21aj_two_adic_exponent": smith["maximum_two_adic_exponent"],
            "pairing_saturation_quotient_is_2_primary": cert_21aj["two_primary_proof"]["pairing_saturation_quotient_is_2_primary"],
            "test_is_only_a_necessary_modular_filter": True,
        },
        "fixed_image_column_module_stats": module_stats,
        "action_hashes_sha256": action_hashes_sha,
        "anti_fixed_integer_kernel_sha256": cert_21aj["anti_fixed_integer_kernel_sha256"],
        "pairing_translation_lattice_sha256": cert_21aj["initial_pairing_translation_lattice"]["sha256"],
        "orbit_decomposition": {
            "count": len(orbits),
            "sizes": sorted(len(o) for o in orbits),
            "translation_preserves_orbit_totals_exactly": True,
            "nonnegative_composition_residue_criterion": (
                "for residue vector r in [0,7]^orbit, a nonnegative composition of fixed "
                "total S exists with those residues iff sum(r)<=S; congruence mod 8 is "
                "automatic because the translation lattice preserves the exact orbit sum"
            ),
        },
        "sampling": {
            "row_shards": args.row_shards,
            "shard_index": args.shard_index,
            "selected_row_count": len(selected_rows),
            "selected_rows": selected_rows,
            "continuous_kkt_survivors": continuous,
            "sample_modulus": args.sample_modulus,
            "sample_remainder": args.sample_remainder,
            "selection_rule": "sha256(row|e|a|u|v)[0:8]_big_endian mod sample_modulus == sample_remainder",
            "sampled_existing_witnesses": sampled,
            "unique_sampled_projection_states": len(cache),
            "solver_timeout_ms_per_unique_projection_state": args.solver_timeout_ms,
        },
        "result": {
            "sat_existing_witness_projection_states": sat_count,
            "unsat_existing_witness_projection_states": unsat_count,
            "unknown_existing_witness_projection_states": unknown_count,
            "unsat_is_exact_for_the_mod8_orbit_composition_sieve": True,
            "unsat_is_not_yet_a_slice_prune": True,
            "slice_prune_requires_exhausting_all_relevant_rank2_integer_pairs": True,
            "unknown_is_not_unsat": True,
            "minimum_observed_fixed_orbit_total": min_orbit_total,
            "maximum_observed_fixed_orbit_total": max_orbit_total,
            "maximum_sat_minimal_residue_orbit_sum": max_sat_minimal_sum,
            "decision_stream_sha256": decision_stream.hexdigest(),
            "row_summaries": row_summaries,
            "sat_examples": sat_examples,
            "unsat_examples": unsat_examples,
            "unknown_examples": unknown_examples,
        },
        "interpretation": {
            "affine_projection_offset_restored": True,
            "exact_mod8_pairing_image_filter_implemented": True,
            "full_affine_lattice_membership_solved": False,
            "simultaneous_nonnegative_affine_fiber_feasibility_solved": False,
            "next_if_unsat_found": (
                "32-21al: exhaust the rank2 integer (u,v) search only on mod8-UNSAT "
                "candidate slices and promote a prune only if every relevant projection state fails"
            ),
            "next_if_zero_unsat_and_zero_unknown": (
                "32-21al: the pure 2-adic orbit-composition sieve is empirically dominated on "
                "this representative sample; move to the 67 additional rational affine-fiber "
                "relations before considering a full 59D affine solver"
            ),
            "next_if_unknown": (
                "tighten or decompose the exact mod8 feasibility solver; UNKNOWN receives no prune credit"
            ),
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "terminal_family_materialization_run": False,
            "59d_cvp_run": False,
            "full_59d_affine_integer_solver_run": False,
            "representative_row_shard_only": True,
            "deterministic_sample_only": True,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "unknown_is_not_unsat": True,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
