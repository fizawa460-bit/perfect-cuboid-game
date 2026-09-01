#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

from sympy import Matrix
from z3 import Real, Solver, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from diagnose_stage32_21al_nonnegative_orbit_composition import deterministic_sample, parse_row_id
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained
from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_21AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_ANTI_RANK = 59
EXPECTED_PAIRING_COUNT = 140
EXPECTED_ORBIT_COUNT = 14
EXPECTED_RELATION_RANK = 81
EXPECTED_ADDITIONAL_RELATION_RANK = 67
EXPECTED_SAMPLE_COUNT = 56
SCHEMA = "STAGE32_21AO_ALL140_RATIONAL_POLYHEDRAL_FEASIBILITY_GATE_V1"


def z3_fraction(value) -> Fraction:
    value = value.as_fraction()
    return Fraction(int(value.numerator), int(value.denominator))


def solve_rational_fiber(*, z: tuple[int, ...], M: Matrix, y0_map: Matrix) -> tuple[str, tuple[Fraction, ...] | None, tuple[Fraction, ...] | None]:
    if M.shape != (EXPECTED_PAIRING_COUNT, EXPECTED_ANTI_RANK):
        raise ValueError("21ao translation shape regression")
    if y0_map.shape != (EXPECTED_PAIRING_COUNT, len(z)):
        raise ValueError("21ao affine-offset shape regression")
    q = [Real(f"q_{j}") for j in range(EXPECTED_ANTI_RANK)]
    y0 = y0_map * Matrix(z)
    s = Solver()
    for i in range(EXPECTED_PAIRING_COUNT):
        s.add(int(y0[i, 0]) + sum(int(M[i, j]) * q[j] for j in range(EXPECTED_ANTI_RANK)) >= 0)
    result = s.check()
    if result == unknown:
        return "UNKNOWN", None, None
    if result == unsat:
        return "UNSAT", None, None
    if result != sat:
        raise ValueError(f"unexpected z3 result: {result}")
    model = s.model()
    witness = tuple(z3_fraction(model.eval(v, model_completion=True)) for v in q)
    pairings = tuple(
        Fraction(int(y0[i, 0]), 1)
        + sum(Fraction(int(M[i, j]), 1) * witness[j] for j in range(EXPECTED_ANTI_RANK))
        for i in range(EXPECTED_PAIRING_COUNT)
    )
    if any(v < 0 for v in pairings):
        raise ValueError("21ao rational SAT witness violated nonnegativity")
    return "SAT", witness, pairings


def frac_payload(values: tuple[Fraction, ...]) -> list[list[int]]:
    return [[v.numerator, v.denominator] for v in values]


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
    ap.add_argument("--example-limit", type=int, default=12)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text())
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed_manifest or claimed_manifest != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")
    bundle = load_retained(args.retained, "s32_21ao_picard")
    marking = load_retained(args.marking, "s32_21ao_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_21AC_CERTIFICATE_SHA256:
        raise ValueError("21ac certificate regression")
    data = reconstruct_translation_data(marking, bundle)
    M = data["M"]
    y0_map = data["pairing_x0_map"]
    orbits = tuple(tuple(int(v) for v in o) for o in data["orbits"])
    if len(orbits) != EXPECTED_ORBIT_COUNT:
        raise ValueError("21ao orbit count regression")
    if EXPECTED_PAIRING_COUNT - EXPECTED_ANTI_RANK != EXPECTED_RELATION_RANK:
        raise ValueError("21ao relation-rank arithmetic regression")
    if EXPECTED_RELATION_RANK - EXPECTED_ORBIT_COUNT != EXPECTED_ADDITIONAL_RELATION_RANK:
        raise ValueError("21ao additional-relation arithmetic regression")
    for orbit in orbits:
        for j in range(M.cols):
            if sum(int(M[i, j]) for i in orbit):
                raise ValueError("21ao orbit-sum relation regression")

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    selected_rows = [r for i, r in enumerate(all_rows) if i % args.row_shards == args.shard_index]
    rank2 = model.rank2
    kkt = rank2.orbit_qp
    bound = rank2.bound
    bridge = rank2.bridge
    k0, k1 = rank2.kernel_columns

    hashed = sampled = sat_count = unsat_count = unknown_count = 0
    cache: dict[tuple[int, ...], tuple[str, tuple[Fraction, ...] | None, tuple[Fraction, ...] | None]] = {}
    decision_stream = hashlib.sha256()
    examples = {"SAT": [], "UNSAT": [], "UNKNOWN": []}
    rows = []
    minimum_pairing: Fraction | None = None

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        rs = {"row_id": row_id, "sampled": 0, "sat": 0, "unsat": 0, "unknown": 0}
        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            if interval is None:
                continue
            lo, hi = interval
            for a in range(lo, hi + 1):
                if not deterministic_sample(row_id, e, a, args.sample_modulus, args.sample_remainder):
                    continue
                hashed += 1
                if not bridge.target_in_image(d, e, a):
                    continue
                if kkt.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
                    continue
                candidate = kkt.solve_candidate(d, e, a)
                if candidate is None or not candidate.can_reach_selfsq(d, e, a, lower):
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
                rs["sampled"] += 1
                answer = cache.get(z)
                if answer is None:
                    answer = solve_rational_fiber(z=z, M=M, y0_map=y0_map)
                    cache[z] = answer
                status, witness, pairings = answer
                if status == "SAT":
                    sat_count += 1; rs["sat"] += 1
                    if witness is None or pairings is None:
                        raise ValueError("21ao SAT witness missing")
                    local_min = min(pairings)
                    minimum_pairing = local_min if minimum_pairing is None else min(minimum_pairing, local_min)
                    if len(examples[status]) < args.example_limit:
                        examples[status].append({"row_id": row_id, "e": e, "a": a, "u": u, "v": v, "z": list(z), "rational_translation_sha256": csha(frac_payload(witness)), "all140_pairings_sha256": csha(frac_payload(pairings)), "minimum_pairing": [local_min.numerator, local_min.denominator]})
                elif status == "UNSAT":
                    unsat_count += 1; rs["unsat"] += 1
                    if len(examples[status]) < args.example_limit:
                        examples[status].append({"row_id": row_id, "e": e, "a": a, "u": u, "v": v, "z": list(z)})
                elif status == "UNKNOWN":
                    unknown_count += 1; rs["unknown"] += 1
                    if len(examples[status]) < args.example_limit:
                        examples[status].append({"row_id": row_id, "e": e, "a": a, "u": u, "v": v, "z": list(z)})
                else:
                    raise ValueError(status)
                decision_stream.update(f"{row_id}|{e}|{a}|{u}|{v}|{','.join(map(str,z))}|{status}\n".encode())
        rows.append(rs)

    if sampled != EXPECTED_SAMPLE_COUNT or len(cache) != EXPECTED_SAMPLE_COUNT:
        raise ValueError(f"21ao sample regression sampled={sampled} unique={len(cache)}")
    if sampled != sat_count + unsat_count + unknown_count:
        raise ValueError("21ao accounting regression")
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ao",
        "mode": "EXACT_Q_RATIONAL_RELAXATION_OF_ALL140_NONNEGATIVE_AFFINE_PAIRING_FIBER",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_21AC_CERTIFICATE_SHA256,
        "z3_version": get_version_string(),
        "interface": {
            "pairing_count": EXPECTED_PAIRING_COUNT,
            "rational_translation_rank": EXPECTED_ANTI_RANK,
            "left_rational_relation_rank": EXPECTED_RELATION_RANK,
            "orbit_sum_relation_rank": EXPECTED_ORBIT_COUNT,
            "additional_relation_rank_beyond_orbit_sums": EXPECTED_ADDITIONAL_RELATION_RANK,
            "all140_nonnegative_constraints_enforced": True,
            "integrality_deliberately_relaxed": True,
            "unsat_over_Q_implies_unsat_over_Z": True,
            "sat_over_Q_does_not_imply_integral_feasibility": True,
        },
        "sampling": {"row_shards": args.row_shards, "shard_index": args.shard_index, "selected_rows": selected_rows, "sample_modulus": args.sample_modulus, "sample_remainder": args.sample_remainder, "hash_selected_feasible_interval_points": hashed, "sampled_continuous_kkt_survivors": sampled, "unique_projection_states": len(cache), "representative_not_full178_credit": True},
        "result": {"sat_rational_projection_states": sat_count, "unsat_rational_projection_states": unsat_count, "unknown_projection_states": unknown_count, "minimum_pairing_on_sat_witnesses": None if minimum_pairing is None else [minimum_pairing.numerator, minimum_pairing.denominator], "decision_stream_sha256": decision_stream.hexdigest(), "row_summaries": rows, "sat_examples": examples["SAT"], "unsat_examples": examples["UNSAT"], "unknown_examples": examples["UNKNOWN"]},
        "interpretation": {
            "next_if_any_rational_unsat": "32-21ap: exhaust rank2 projection states only for the corresponding candidate slices; rational UNSAT is already exact for each tested projection",
            "next_if_all_rational_sat": "32-21ap: rational geometry is feasible on every representative projection; the remaining all140 obstruction is purely integral and/or self-intersection/norm, so derive an exact small quotient/semigroup interface rather than retrying generic 59D integer SMT",
            "next_if_unknown": "decompose exact LRA solver; UNKNOWN receives no credit",
        },
        "safety": {"heavy_run_key_used": False, "full178_production_run": False, "59d_cvp_run": False, "terminal_family_materialization_run": False, "numerical_row_complete": False, "theorem_credit": False, "receiver_credit": False, "route_credit": False, "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False, "unknown_is_not_unsat": True, "planned_effective_heavy_concurrency": 0, "artifact_storage_preflight": "single compact JSON, 3-day retention, expected <<1 MB"},
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": "PASS_STAGE32_21AO_ALL140_RATIONAL_POLYHEDRAL_FEASIBILITY_GATE", "sampled": sampled, "sat": sat_count, "unsat": unsat_count, "unknown": unknown_count, "canonical_sha256": payload["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
