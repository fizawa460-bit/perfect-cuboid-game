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
N349 = HERE.parent / "N349/RESULT.json"
N349_AUDIT = HERE.parent / "N349/HOSTILE-AUDIT-PASS.json"
N349B_VERIFIER = HERE.parent / "N349B/verify_n349b_factor_hurwitz_boundary_cap.py"
AO_NOTE = ROOT / "stages/stage32/residual-32-01-production/post1648ao-special-fibre-hurwitz-budget-source-note.md"

EXPECTED_N349 = "10bdf80d8e9755455133226ac1166da254fec8b956658a53fde769f33c5cd12b"
EXPECTED_N349_AUDIT = "1752b861d0308cf4663d993c8d8c94b0ff491028ad88157580c64a39949907f3"
EXPECTED_N349_REVIEW = 5162530057
EXPECTED_N349_AUDITED_HEAD = "77e1ea70a93149e1e0d7e3f5add3bfb15beec4c2"
EXPECTED_N349B_VERIFIER_BLOB = "55ed68bf7de0f1975c1cbe8c7484ac40f16444cc"
EXPECTED_BUNDLE = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_AO_BLOB = "242088adab5c86292154a6de9bc3563ba73b4f43"
BOUNDARY_PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
TARGETS = [
    {"row_id": "g0-d176", "genus": 0, "degree": 176, "e": 48, "normal_mass": 3104, "x4_terminal_count": 3105, "boundary_cap": 7},
    {"row_id": "g1-d192", "genus": 1, "degree": 192, "e": 48, "normal_mass": 3408, "x4_terminal_count": 3409, "boundary_cap": 8},
]
TIMEOUT_MS = 30000


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    d = json.loads(path.read_text())
    claimed = d.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(d) != expected:
        raise ValueError(f"canonical regression: {path}")
    d["canonical_sha256_without_this_field"] = claimed
    return d


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def linear_expr(P: Matrix, label: int, xs):
    terms = [int(P[label - 1, i]) * xs[i] for i in range(64) if int(P[label - 1, i])]
    return z3.Sum(terms) if terms else z3.IntVal(0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    n349 = load_canonical(N349, EXPECTED_N349)
    audit = load_canonical(N349_AUDIT, EXPECTED_N349_AUDIT)
    if audit["audit"]["review_id"] != EXPECTED_N349_REVIEW or audit["audit"]["verdict"] != "PASS":
        raise ValueError("N349 hostile-audit receipt regression")
    if audit["audit"]["audited_exact_head"] != EXPECTED_N349_AUDITED_HEAD:
        raise ValueError("N349 audited head regression")
    if audit["consumption"]["local_pair_necessity_may_be_consumed"] is not True:
        raise ValueError("N349 local-pair scope not consumable")
    if n349["aggregate"]["required_local_pair_at_every_node"] != [4, 4]:
        raise ValueError("N349 local-pair regression")
    if git_blob_sha1(N349B_VERIFIER) != EXPECTED_N349B_VERIFIER_BLOB:
        raise ValueError("N349B verifier blob regression")
    if git_blob_sha1(AO_NOTE) != EXPECTED_AO_BLOB:
        raise ValueError("AO source-note blob regression")

    n345 = load_module(N345_PATH, "s32_n349c_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n349c_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n349c_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise ValueError("retained marking canonical regression")

    adapter = n345.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    boundary = sorted(x for pack in BOUNDARY_PACKS for x in pack)
    if boundary != list(range(33, 45)):
        raise ValueError("boundary labels regression")

    # Recheck the six-fibre geometry used to derive the cap.  Within each
    # direction, every boundary elliptic has eight exceptional incidents and
    # the six resolved fibre classes coincide; their exceptional sets partition 48.
    for pack in BOUNDARY_PACKS:
        fibre_rows = []
        seen = []
        for label in pack:
            inc = [j for j in range(93, 141) if int(full[label - 1, j - 1]) == 1]
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

    rows = []
    eliminated = 0
    sat = unsat = unknown = 0
    for target in TARGETS:
        xs = [z3.Int(f"x_{target['row_id']}_{i}") for i in range(64)]
        pair = {label: linear_expr(P, label, xs) for label in range(1, 141)}
        s = z3.SolverFor("QF_LIA")
        s.set(timeout=TIMEOUT_MS)
        s.add(z3.Sum([pair[i] for i in range(1, 93)]) == target["normal_mass"])
        for i in range(93, 141):
            s.add(pair[i] == 1)
        for i in range(1, 93):
            s.add(pair[i] >= 0)
        for i in boundary:
            s.add(pair[i] <= target["boundary_cap"])
        # Deliberately NO x4 equality and NO self-square condition.
        status = s.check()
        row = dict(target)
        if status == z3.unsat:
            row["verdict"] = "UNSAT_ROWLEVEL_RELAXED_QF_LIA"
            row["all_x4_terminals_eliminated_if_audited"] = True
            eliminated += target["x4_terminal_count"]
            unsat += 1
        elif status == z3.unknown:
            row["verdict"] = "UNKNOWN_ZERO_CREDIT"
            row["reason_unknown"] = s.reason_unknown()
            unknown += 1
        else:
            sat += 1
            row["verdict"] = "SAT_ROWLEVEL_RELAXED_QF_LIA"
            model = s.model()
            xvals = [int(model.eval(v, model_completion=True).as_long()) for v in xs]
            pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
            row["witness_sha256"] = csha({"picard_coordinates": xvals, "all140_pairings": pairings})
            row["witness_x4"] = pairings[48]
            row["boundary_pairings_33_to_44"] = pairings[32:44]
        rows.append(row)

    body = {
        "schema": "STAGE32_32_01_178_N349C_ROWLEVEL_FACTOR_HURWITZ_CAP_V1",
        "node_id": "N349C",
        "status": "AUDIT_CANDIDATE_NO_MAIN_CREDIT",
        "source_locks": {
            "n349_checkpoint_canonical": EXPECTED_N349,
            "n349_hostile_audit_receipt_canonical": EXPECTED_N349_AUDIT,
            "n349_hostile_audit_review_id": EXPECTED_N349_REVIEW,
            "n349_hostile_audit_exact_head": EXPECTED_N349_AUDITED_HEAD,
            "n349b_verifier_blob_sha1": EXPECTED_N349B_VERIFIER_BLOB,
            "ao_source_note_blob_sha1": EXPECTED_AO_BLOB,
            "retained_bundle_canonical": EXPECTED_BUNDLE,
            "retained_marking_canonical": EXPECTED_MARKING,
        },
        "relaxation": {
            "all48_exceptional_pairings": 1,
            "all92_normal_pairings_nonnegative": True,
            "normal_mass_fixed": True,
            "boundary_caps": {"g0-d176": 7, "g1-d192": 8},
            "x4_fixed": False,
            "self_square_used": False,
            "solver_logic": "QF_LIA",
            "timeout_ms_per_row": TIMEOUT_MS,
        },
        "aggregate": {
            "row_count": 2,
            "sat_row_count": sat,
            "unsat_row_count": unsat,
            "unknown_row_count": unknown,
            "boundary_terminal_count": sum(t["x4_terminal_count"] for t in TARGETS),
            "candidate_eliminated_terminal_count_if_audited": eliminated,
        },
        "rows": rows,
        "conclusion": {
            "bypasses_n310_n341_if_both_rows_unsat_and_hostile_audited": unsat == 2 and unknown == 0,
            "n260_still_required_for_all48_vector": True,
            "n280_still_required_for_off_boundary_strata_g0d174_g1d190": True,
            "n349_prerequisite_already_hostile_audited": True,
        },
        "semantics": {
            "rowlevel_unsat_is_stronger_than_testing_selected_x4_values": True,
            "sat_does_not_construct_an_integral_irreducible_curve": True,
            "unknown_zero_credit": True,
            "n349c_hostile_audit_required": True,
            "main_pruning_credit": False,
            "production_leaf_credit": False,
            "n350_producer_registry_unchanged": True,
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
        "verdict": "PASS_N349C_ROWLEVEL_LEDGER",
        "sat_rows": sat,
        "unsat_rows": unsat,
        "unknown_rows": unknown,
        "boundary_terminals": body["aggregate"]["boundary_terminal_count"],
        "candidate_eliminated": eliminated,
        "bypasses_n310_n341": body["conclusion"]["bypasses_n310_n341_if_both_rows_unsat_and_hostile_audited"],
        "canonical": body["canonical_sha256_without_this_field"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
