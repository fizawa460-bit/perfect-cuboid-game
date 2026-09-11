#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import z3
from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N345_PATH = HERE.parent / "N345/verify_n345_kernel14_integral_self_square.py"
AO_NOTE = ROOT / "stages/stage32/residual-32-01-production/post1648ao-special-fibre-hurwitz-budget-source-note.md"
CONTRACT = HERE / "GENERAL_FACTOR_HURWITZ_MASS_CAP_CONTRACT.md"

EXPECTED_AO_BLOB = "242088adab5c86292154a6de9bc3563ba73b4f43"
EXPECTED_CONTRACT_BLOB = "377c2c43b3c80644c5913586cee42e9a6ec1138d"
EXPECTED_BUNDLE = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
BOUNDARY_PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
TARGETS = [
    {"row_id": "g0-d174", "genus": 0, "degree": 174, "e": 48, "normal_mass": 3066},
    {"row_id": "g0-d176", "genus": 0, "degree": 176, "e": 48, "normal_mass": 3104},
    {"row_id": "g1-d190", "genus": 1, "degree": 190, "e": 48, "normal_mass": 3370},
    {"row_id": "g1-d192", "genus": 1, "degree": 192, "e": 48, "normal_mass": 3408},
]
TIMEOUT_MS = 30000


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def linear_expr(P: Matrix, label: int, xs):
    terms = [int(P[label - 1, i]) * xs[i] for i in range(64) if int(P[label - 1, i])]
    return z3.Sum(terms) if terms else z3.IntVal(0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if git_blob_sha1(AO_NOTE) != EXPECTED_AO_BLOB:
        raise ValueError("AO source-note blob regression")
    if git_blob_sha1(CONTRACT) != EXPECTED_CONTRACT_BLOB:
        raise ValueError("N351 contract blob regression")

    n345 = load_module(N345_PATH, "s32_n351_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n351_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n351_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise ValueError("retained marking canonical regression")

    adapter = n345.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    # Exact retained geometry check: each pack consists of six linearly equivalent
    # special fibres and its exceptional 8-sets partition labels 93..140.
    fibre_checks = []
    for pack in BOUNDARY_PACKS:
        fibre_rows = []
        seen = []
        incidence_sizes = []
        for label in pack:
            inc = [j for j in range(93, 141) if int(full[label - 1, j - 1]) == 1]
            incidence_sizes.append(len(inc))
            if len(inc) != 8:
                raise ValueError(f"boundary incidence regression label={label}")
            seen.extend(inc)
            F = 2 * coords.row(label - 1)
            for j in inc:
                F += coords.row(j - 1)
            fibre_rows.append(F)
        if sorted(seen) != list(range(93, 141)):
            raise ValueError("six-fibre exceptional partition regression")
        if any(F != fibre_rows[0] for F in fibre_rows[1:]):
            raise ValueError("six special fibres are not linearly equivalent")
        fibre_checks.append({"pack": pack, "incidence_sizes": incidence_sizes, "partition_all48": True})

    rows = []
    sat = unsat = unknown = 0
    for target in TARGETS:
        xs = [z3.Int(f"x_{target['row_id']}_{i}") for i in range(64)]
        pair = {label: linear_expr(P, label, xs) for label in range(1, 141)}
        s = z3.SolverFor("QF_LIA")
        s.set(timeout=TIMEOUT_MS)

        s.add(z3.Sum([pair[i] for i in range(1, 93)]) == target["normal_mass"])
        s.add(z3.Sum([pair[i] for i in range(93, 141)]) == target["e"])
        for i in range(1, 141):
            s.add(pair[i] >= 0)

        q_cap = target["e"] + 6 * target["genus"] - 6
        q_exprs = [z3.Sum([pair[i] for i in pack]) for pack in BOUNDARY_PACKS]
        for q in q_exprs:
            s.add(q <= q_cap)

        # Deliberately no exceptional-vector fixation, no x4 equality, no self-square.
        status = s.check()
        row = dict(target)
        row["q_cap_each_factor_pack"] = q_cap
        if status == z3.unsat:
            unsat += 1
            row["verdict"] = "UNSAT_MASS_ONLY_RELAXED_QF_LIA"
            row["entire_gde_stratum_candidate_obstructed_if_audited"] = True
        elif status == z3.unknown:
            unknown += 1
            row["verdict"] = "UNKNOWN_ZERO_CREDIT"
            row["reason_unknown"] = s.reason_unknown()
        else:
            sat += 1
            row["verdict"] = "SAT_MASS_ONLY_RELAXED_QF_LIA"
            model = s.model()
            xvals = [int(model.eval(v, model_completion=True).as_long()) for v in xs]
            pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
            row["witness_sha256"] = csha({"picard_coordinates": xvals, "all140_pairings": pairings})
            row["witness_exceptional_mass"] = sum(pairings[92:140])
            row["witness_x4"] = pairings[48]
            row["witness_q_packs"] = [sum(pairings[i - 1] for i in pack) for pack in BOUNDARY_PACKS]
        rows.append(row)

    body = {
        "schema": "STAGE32_32_01_178_N351_GENERAL_FACTOR_HURWITZ_MASS_CAP_V1",
        "node_id": "N351",
        "status": "AUDIT_CANDIDATE_NO_MAIN_CREDIT",
        "source_locks": {
            "ao_source_note_blob_sha1": EXPECTED_AO_BLOB,
            "contract_blob_sha1": EXPECTED_CONTRACT_BLOB,
            "retained_bundle_canonical": EXPECTED_BUNDLE,
            "retained_marking_canonical": EXPECTED_MARKING,
        },
        "necessary_condition": {
            "local_hurwitz": "R >= e-B+q",
            "branch_mass_bound": "B <= e",
            "weakened_hurwitz": "R >= q",
            "six_fibre_identity": "6n = 2q+e",
            "riemann_hurwitz": "R = 2g-2+2n",
            "degree_cap": "n <= e/2+2g-2",
            "pack_sum_cap": "q <= e+6g-6",
            "applied_in_both_factor_directions": True,
        },
        "fibre_geometry_checks": fibre_checks,
        "relaxation": {
            "picard_coordinates_integral": True,
            "all140_pairings_nonnegative": True,
            "exceptional_total_fixed_only": True,
            "individual_exceptional_pairings_fixed": False,
            "normal_total_fixed": True,
            "x4_fixed": False,
            "self_square_used": False,
            "n349_local44_used": False,
            "n260_allones_used": False,
            "solver_logic": "QF_LIA",
            "timeout_ms_per_row": TIMEOUT_MS,
        },
        "aggregate": {
            "row_count": len(TARGETS),
            "sat_row_count": sat,
            "unsat_row_count": unsat,
            "unknown_row_count": unknown,
        },
        "rows": rows,
        "semantics": {
            "unsat_is_candidate_whole_gde_stratum_necessary_obstruction": True,
            "sat_is_not_member_or_existence_credit": True,
            "unknown_zero_credit": True,
            "hostile_audit_required": True,
            "main_pruning_credit": False,
            "production_leaf_credit": False,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N351_GENERAL_HURWITZ_LEDGER",
        "sat_rows": sat,
        "unsat_rows": unsat,
        "unknown_rows": unknown,
        "canonical": body["canonical_sha256_without_this_field"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
