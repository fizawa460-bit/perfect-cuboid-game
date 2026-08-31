#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Int, Solver, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from diagnose_stage32_21al_nonnegative_orbit_composition import deterministic_sample, parse_row_id
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained
from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_21AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_21AK_CONSTRAINT_ROWS_SHA256 = "1c8ea0443dcf80dcaec80964618eac97385d85bfa7d009e60d471cd70f3a5169"
EXPECTED_ANTI_RANK = 59
EXPECTED_PAIRING_COUNT = 140
EXPECTED_ORBIT_COUNT = 14
EXPECTED_RELATION_RANK = 81
EXPECTED_ADDITIONAL_RELATION_RANK = 67
EXPECTED_SAMPLE_COUNT = 56
SCHEMA = "STAGE32_21AP_SELECTED_PAIRING_BOUNDED_INTEGER_FIBER_V1"


def as_fraction(v) -> Fraction:
    return Fraction(int(v.p), int(v.q)) if hasattr(v, "p") else Fraction(int(v), 1)


def relation_row_payload(row) -> list[list[int]]:
    return [[as_fraction(v).numerator, as_fraction(v).denominator] for v in row]


def lcm_denominators(values) -> int:
    d = 1
    for v in values:
        d = math.lcm(d, as_fraction(v).denominator)
    return d


def build_relation_interface(data: dict) -> dict:
    S = data["Sfinal"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    square = data["square"]
    if square != S.extract(list(pivots), list(range(EXPECTED_ANTI_RANK))):
        raise ValueError("21ap selected saturated square regression")
    inv = square.inv()
    rel = S * inv
    selected_rel = rel.extract(list(pivots), list(range(EXPECTED_ANTI_RANK)))
    if selected_rel != Matrix.eye(EXPECTED_ANTI_RANK):
        raise ValueError("21ap selected relation identity regression")
    denominators = []
    for i in range(rel.rows):
        denominators.append(lcm_denominators(rel.row(i)))
    omitted = [i for i in range(EXPECTED_PAIRING_COUNT) if i not in set(pivots)]
    if len(omitted) != EXPECTED_RELATION_RANK:
        raise ValueError("21ap omitted relation count regression")
    return {
        "relation_matrix": rel,
        "square_inverse": inv,
        "pivots": pivots,
        "omitted": tuple(omitted),
        "row_denominators": tuple(denominators),
    }


def solve_selected_integer_fiber(
    *,
    z: tuple[int, ...],
    data: dict,
    relif: dict,
    timeout_ms: int,
) -> tuple[str, tuple[int, ...] | None, tuple[int, ...] | None, tuple[int, ...] | None]:
    pivots = relif["pivots"]
    rel = relif["relation_matrix"]
    y0_map = data["pairing_x0_map"]
    y0 = y0_map * Matrix(z)
    selected_y0 = Matrix([int(y0[i, 0]) for i in pivots])
    svars = [Int(f"s_{j}") for j in range(EXPECTED_ANTI_RANK)]
    solver = Solver()
    solver.set(timeout=timeout_ms)
    for v in svars:
        solver.add(v >= 0)

    # Exact fixed orbit totals give small natural bounds to the selected coordinates.
    orbit_totals = []
    selected_positions_by_orbit = [[] for _ in range(EXPECTED_ORBIT_COUNT)]
    curve_to_orbit = {}
    for oid, orbit in enumerate(data["orbits"]):
        for idx in orbit:
            curve_to_orbit[int(idx)] = oid
        total = sum(int(y0[int(idx), 0]) for idx in orbit)
        if total < 0:
            raise ValueError("21ap negative fixed orbit total")
        orbit_totals.append(total)
    for j, curve_idx in enumerate(pivots):
        selected_positions_by_orbit[curve_to_orbit[int(curve_idx)]].append(j)
    for oid, positions in enumerate(selected_positions_by_orbit):
        if positions:
            solver.add(sum((svars[j] for j in positions), 0) <= orbit_totals[oid])

    # Exact 14 congruences distinguish the original pairing lattice inside its 2-saturation.
    for row in data["constraint_rows"]:
        modulus = int(row["modulus"])
        coeffs = tuple(int(v) for v in row["selected_pairing_coefficients"])
        offsets = tuple(int(v) for v in row["projection_z_offset_coefficients"])
        lhs = sum(coeffs[j] * svars[j] for j in range(EXPECTED_ANTI_RANK))
        offset = sum(offsets[k] * int(z[k]) for k in range(len(z)))
        solver.add((lhs - offset) % modulus == 0)

    # Recover every omitted pairing through the 81 exact rational relations.
    # Clearing denominators and requiring divisibility enforces that all 140 pairings are integral.
    relation_specs = []
    for i in relif["omitted"]:
        coeff = [as_fraction(rel[i, j]) for j in range(EXPECTED_ANTI_RANK)]
        const = Fraction(int(y0[i, 0]), 1) - sum(coeff[j] * Fraction(int(selected_y0[j, 0]), 1) for j in range(EXPECTED_ANTI_RANK))
        D = lcm_denominators(coeff + [const])
        nums = [int(c * D) for c in coeff]
        c0 = int(const * D)
        numexpr = c0 + sum(nums[j] * svars[j] for j in range(EXPECTED_ANTI_RANK))
        solver.add(numexpr >= 0)
        if D != 1:
            solver.add(numexpr % D == 0)
        relation_specs.append((i, D, tuple(nums), c0))

    result = solver.check()
    if result == unknown:
        return "UNKNOWN", None, None, tuple(orbit_totals)
    if result == unsat:
        return "UNSAT", None, None, tuple(orbit_totals)
    if result != sat:
        raise ValueError(f"unexpected z3 result: {result}")
    m = solver.model()
    s = tuple(int(m.eval(v, model_completion=True).as_long()) for v in svars)

    pairings = [None] * EXPECTED_PAIRING_COUNT
    for j, idx in enumerate(pivots):
        pairings[idx] = s[j]
    for i, D, nums, c0 in relation_specs:
        num = c0 + sum(nums[j] * s[j] for j in range(EXPECTED_ANTI_RANK))
        if num < 0 or num % D:
            raise ValueError("21ap SAT relation reconstruction regression")
        pairings[i] = num // D
    if any(v is None or int(v) < 0 for v in pairings):
        raise ValueError("21ap SAT all140 nonnegative reconstruction regression")
    pairings_t = tuple(int(v) for v in pairings)

    # Strong independent lift check: recover saturated coordinates w and then original t.
    ds = Matrix([s[j] - int(selected_y0[j, 0]) for j in range(EXPECTED_ANTI_RANK)])
    w = relif["square_inverse"] * ds
    if any(v.q != 1 for v in w):
        raise ValueError("21ap SAT candidate was integral in all140 pairings but not in saturated coordinates")
    wint = Matrix([int(v) for v in w])
    F = data["F"]
    t = F.inv() * wint
    if any(v.q != 1 for v in t):
        raise ValueError("21ap SAT candidate passed published congruences but failed original-lattice lift")
    tint = tuple(int(v) for v in t)
    exact_pairings = data["pairing_x0_map"] * Matrix(z) + data["M"] * Matrix(tint)
    if tuple(int(exact_pairings[i, 0]) for i in range(EXPECTED_PAIRING_COUNT)) != pairings_t:
        raise ValueError("21ap original-lattice lift did not reconstruct all140 pairings")
    return "SAT", tint, pairings_t, tuple(orbit_totals)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--row-shards", type=int, default=16)
    ap.add_argument("--shard-index", type=int, default=0)
    ap.add_argument("--sample-modulus", type=int, default=1024)
    ap.add_argument("--sample-remainder", type=int, default=0)
    ap.add_argument("--solver-timeout-ms", type=int, default=5000)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed or claimed != EXPECTED_MANIFEST_SHA256:
        raise ValueError("manifest regression")
    bundle = load_retained(args.retained, "s32_21ap_picard")
    marking = load_retained(args.marking, "s32_21ap_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_21AC_CERTIFICATE_SHA256:
        raise ValueError("21ac certificate regression")
    data = reconstruct_translation_data(marking, bundle)
    if csha(list(data["constraint_rows"])) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("21ak constraint regression")
    relif = build_relation_interface(data)
    relation_denominators = relif["row_denominators"]

    all_rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    selected_rows = [r for i, r in enumerate(all_rows) if i % args.row_shards == args.shard_index]
    rank2 = model.rank2
    kkt = rank2.orbit_qp
    bound = rank2.bound
    bridge = rank2.bridge
    k0, k1 = rank2.kernel_columns

    sampled = satc = unsatc = unknownc = 0
    cache = {}
    stream = hashlib.sha256()
    states = []
    min_pairing = None
    max_pairing = None

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            if interval is None:
                continue
            lo, hi = interval
            for a in range(lo, hi + 1):
                if not deterministic_sample(row_id, e, a, args.sample_modulus, args.sample_remainder):
                    continue
                if not bridge.target_in_image(d, e, a):
                    continue
                if kkt.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
                    continue
                cand = kkt.solve_candidate(d, e, a)
                if cand is None or not cand.can_reach_selfsq(d, e, a, lower):
                    continue
                survives, _, _, uv, _ = model.can_reach_selfsq(d, e, a, lower)
                if not survives or uv is None:
                    raise ValueError("21ad representative witness regression")
                u, v = uv
                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("rank2 affine origin missing")
                z = tuple(int(z0[i] + k0[i] * u + k1[i] * v) for i in range(len(z0)))
                sampled += 1
                ans = cache.get(z)
                if ans is None:
                    ans = solve_selected_integer_fiber(z=z, data=data, relif=relif, timeout_ms=args.solver_timeout_ms)
                    cache[z] = ans
                status, t, pairings, totals = ans
                if status == "SAT":
                    satc += 1
                    if t is None or pairings is None:
                        raise ValueError("21ap SAT witness missing")
                    pmin, pmax = min(pairings), max(pairings)
                    min_pairing = pmin if min_pairing is None else min(min_pairing, pmin)
                    max_pairing = pmax if max_pairing is None else max(max_pairing, pmax)
                    witness_sha = csha(list(t))
                    pairings_sha = csha(list(pairings))
                elif status == "UNSAT":
                    unsatc += 1; witness_sha = None; pairings_sha = None
                elif status == "UNKNOWN":
                    unknownc += 1; witness_sha = None; pairings_sha = None
                else:
                    raise ValueError(status)
                state = {"row_id": row_id, "e": e, "a": a, "u": u, "v": v, "z": list(z), "status": status, "orbit_totals": list(totals), "translation_witness_sha256": witness_sha, "all140_pairings_sha256": pairings_sha}
                states.append(state)
                stream.update(f"{row_id}|{e}|{a}|{u}|{v}|{','.join(map(str,z))}|{status}\n".encode())

    if sampled != EXPECTED_SAMPLE_COUNT or len(cache) != EXPECTED_SAMPLE_COUNT:
        raise ValueError(f"21ap sample regression sampled={sampled} unique={len(cache)}")
    if sampled != satc + unsatc + unknownc:
        raise ValueError("21ap accounting regression")
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ap",
        "mode": "EXACT_BOUNDED_SELECTED59_INTEGER_PAIRINGS_PLUS_81_RATIONAL_RELATIONS_PLUS_14_LATTICE_CONGRUENCES",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_21AC_CERTIFICATE_SHA256,
        "upstream_32_21ak_constraint_rows_sha256": EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
        "z3_version": get_version_string(),
        "interface": {
            "selected_integer_pairing_count": EXPECTED_ANTI_RANK,
            "all_pairing_count": EXPECTED_PAIRING_COUNT,
            "omitted_exact_rational_relation_count": EXPECTED_RELATION_RANK,
            "additional_relation_rank_beyond_orbit_sums": EXPECTED_ADDITIONAL_RELATION_RANK,
            "two_adic_lattice_congruence_count": len(data["constraint_rows"]),
            "relation_matrix_sha256": csha([relation_row_payload(relif["relation_matrix"].row(i)) for i in range(EXPECTED_PAIRING_COUNT)]),
            "relation_row_denominator_max": max(relation_denominators),
            "relation_row_denominator_distinct": sorted(set(relation_denominators)),
            "selected_pairings_nonnegative_and_orbit_bounded": True,
            "omitted_pairings_nonnegative_and_integral_by_cleared_denominator_constraints": True,
            "sat_witness_independently_lifted_back_to_original_t_in_Z59": True,
            "unsat_is_safe_for_fixed_projection": True,
        },
        "sampling": {"row_shards": args.row_shards, "shard_index": args.shard_index, "selected_rows": selected_rows, "sample_modulus": args.sample_modulus, "sample_remainder": args.sample_remainder, "sampled_projection_states": sampled, "unique_projection_states": len(cache), "solver_timeout_ms": args.solver_timeout_ms, "representative_not_full178_credit": True},
        "result": {"sat_projection_states": satc, "unsat_projection_states": unsatc, "unknown_projection_states": unknownc, "minimum_pairing_on_sat_witnesses": min_pairing, "maximum_pairing_on_sat_witnesses": max_pairing, "decision_stream_sha256": stream.hexdigest(), "complete_projection_state_frontier": states},
        "interpretation": {
            "unsat_is_not_yet_slice_prune": True,
            "slice_prune_requires_exhausting_all_relevant_rank2_projection_states": True,
            "next_if_any_unsat": "32-21aq: exhaust rank2 integer projection states only for candidate slices and promote only all-projection UNSAT",
            "next_if_all_sat": "32-21aq: all140 integer nonnegative fibers exist on representative projections; add exact self-intersection/norm threshold on those explicit fibers before any FULL178 pass",
            "next_if_unknown": "32-21aq: use the source-locked complete 56-state frontier and decompose bounded congruence/semigroup feasibility; UNKNOWN has no credit",
        },
        "safety": {"heavy_run_key_used": False, "full178_production_run": False, "59d_cvp_run": False, "terminal_family_materialization_run": False, "numerical_row_complete": False, "theorem_credit": False, "receiver_credit": False, "route_credit": False, "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False, "unknown_is_not_unsat": True, "planned_effective_heavy_concurrency": 0, "artifact_storage_preflight": "single compact complete-56-state JSON, expected <<100 KB, 3-day retention"},
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": "PASS_STAGE32_21AP_SELECTED_PAIRING_BOUNDED_INTEGER_FIBER", "sampled": sampled, "sat": satc, "unsat": unsatc, "unknown": unknownc, "relation_denominator_max": max(relation_denominators), "canonical_sha256": payload["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
