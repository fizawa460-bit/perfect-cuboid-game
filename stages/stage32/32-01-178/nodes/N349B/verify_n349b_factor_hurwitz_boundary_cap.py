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
N349A = HERE.parent / "N349A/RESULT.json"
AO_NOTE = ROOT / "stages/stage32/residual-32-01-production/post1648ao-special-fibre-hurwitz-budget-source-note.md"
CONTRACT = HERE / "FACTOR_HURWITZ_BOUNDARY_CAP_CONTRACT.md"

EXPECTED_N349 = "10bdf80d8e9755455133226ac1166da254fec8b956658a53fde769f33c5cd12b"
EXPECTED_N349A = "a98044bfe45cb7fd2190061c073e7b442d6556ec8a795b79195f5c374bb2d938"
EXPECTED_BUNDLE = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
BOUNDARY_PACKS = [
    [33, 36, 37, 40, 41, 44],
    [34, 35, 38, 39, 42, 43],
]
PER_TERMINAL_TIMEOUT_MS = 5000


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    data = json.loads(path.read_text())
    claimed = data.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(data) != expected:
        raise ValueError(f"canonical regression: {path}")
    data["canonical_sha256_without_this_field"] = claimed
    return data


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def linear_expr(P: Matrix, label_1based: int, xs: list[z3.IntNumRef]):
    terms = [int(P[label_1based - 1, i]) * xs[i] for i in range(64) if int(P[label_1based - 1, i])]
    return z3.Sum(terms) if terms else z3.IntVal(0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    n349 = load_canonical(N349, EXPECTED_N349)
    n349a = load_canonical(N349A, EXPECTED_N349A)
    if n349["aggregate"]["required_local_pair_at_every_node"] != [4, 4]:
        raise ValueError("N349 pair regression")
    if n349["aggregate"]["boundary_terminal_count"] != 21:
        raise ValueError("N349 terminal regression")
    if n349a["aggregate"]["mapped_exceptional_count"] != 48:
        raise ValueError("N349A exceptional-map regression")
    if n349a["aggregate"]["forbidden_fixed_landing_count_per_member"] != 96:
        raise ValueError("N349A fixed-landing regression")
    if n349a["semantics"]["n349_hostile_audit_still_required"] is not True:
        raise ValueError("N349A audit firewall regression")

    contract = CONTRACT.read_text()
    for required in [
        "6n = 2q + 48",
        "n <= 22 + 2g",
        "g=0: 0 <= C.E <= 7",
        "g=1: 0 <= C.E <= 8",
        "N349_HOSTILE_AUDIT_CONSUMED=false",
    ]:
        if required not in contract:
            raise ValueError(f"N349B contract regression: {required}")

    ao = AO_NOTE.read_text()
    for required in [
        "F_E = 2E + sum(8 incident exceptional curves)",
        "Their exceptional components partition the 48 exceptional curves",
        "R_i >= e - B + q_i",
        "g(Z)=1+mu/12-c/2=1+2-3=0",
    ]:
        if required not in ao:
            raise ValueError(f"AO source-lock regression: {required}")

    n345 = load_module(N345_PATH, "s32_n349b_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n349b_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n349b_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise ValueError("retained marking canonical regression")

    adapter = n345.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    if P.shape != (140, 64) or coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("retained Picard shape regression")
    full = coords * gram * coords.T

    boundary_union = sorted(x for pack in BOUNDARY_PACKS for x in pack)
    if boundary_union != list(range(33, 45)):
        raise ValueError("boundary label partition regression")

    incidence: dict[int, list[int]] = {}
    fibre_rows: list[Matrix] = []
    for pack in BOUNDARY_PACKS:
        pack_incidence = []
        pack_fibres = []
        for label in pack:
            inc = [j for j in range(93, 141) if int(full[label - 1, j - 1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"boundary label {label} exceptional incidence regression")
            incidence[label] = inc
            pack_incidence.extend(inc)
            F = 2 * coords.row(label - 1)
            for exc_label in inc:
                F += coords.row(exc_label - 1)
            pack_fibres.append(F)
        if sorted(pack_incidence) != list(range(93, 141)):
            raise ValueError(f"special-fibre exceptional partition regression: {pack}")
        if any(F != pack_fibres[0] for F in pack_fibres[1:]):
            raise ValueError(f"six fibres do not share one Picard class: {pack}")
        fibre_rows.append(pack_fibres[0])
    if fibre_rows[0] == fibre_rows[1]:
        raise ValueError("two factor fibre classes unexpectedly equal")

    rows = []
    sat = unsat = unknown = 0
    sat_partition = {"g0-d176": [], "g1-d192": []}
    unsat_partition = {"g0-d176": [], "g1-d192": []}
    unknown_partition = {"g0-d176": [], "g1-d192": []}

    for target in n345.TARGETS:
        row_id = str(target["row_id"])
        genus = int(target["genus"])
        mass = int(target["normal_mass"])
        cap_b = 7 + genus
        cap_n = 22 + 2 * genus
        for x4 in target["x4_values"]:
            xs = [z3.Int(f"x_{row_id}_{x4}_{i}") for i in range(64)]
            pair = {label: linear_expr(P, label, xs) for label in range(1, 141)}
            solver = z3.SolverFor("QF_LIA")
            solver.set(timeout=PER_TERMINAL_TIMEOUT_MS)
            solver.add(z3.Sum([pair[label] for label in range(1, 93)]) == mass)
            for label in range(93, 141):
                solver.add(pair[label] == 1)
            solver.add(pair[n345.X4_LABEL] == int(x4))
            for label in range(1, 93):
                solver.add(pair[label] >= 0)
            for label in boundary_union:
                solver.add(pair[label] <= cap_b)

            status = solver.check()
            out = {
                "row_id": row_id,
                "genus": genus,
                "degree": int(target["degree"]),
                "x4": int(x4),
                "boundary_pairing_cap": cap_b,
                "factor_degree_cap": cap_n,
            }
            if status == z3.unsat:
                unsat += 1
                unsat_partition[row_id].append(int(x4))
                out["verdict"] = "UNSAT_RELAXED_LINEAR_FACTOR_HURWITZ_CAP"
            elif status == z3.unknown:
                unknown += 1
                unknown_partition[row_id].append(int(x4))
                out["verdict"] = "UNKNOWN_ZERO_CREDIT"
                out["reason_unknown"] = solver.reason_unknown()
            else:
                sat += 1
                sat_partition[row_id].append(int(x4))
                model = solver.model()
                xvals = [int(model.eval(v, model_completion=True).as_long()) for v in xs]
                pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
                if pairings[92:] != [1] * 48:
                    raise ValueError("SAT exceptional replay regression")
                if min(pairings[:92]) < 0 or sum(pairings[:92]) != mass:
                    raise ValueError("SAT normal replay regression")
                if pairings[n345.X4_LABEL - 1] != int(x4):
                    raise ValueError("SAT x4 replay regression")
                factor_rows = []
                for pack in BOUNDARY_PACKS:
                    bvals = [pairings[label - 1] for label in pack]
                    nvals = [2 * pairings[label - 1] + sum(pairings[e - 1] for e in incidence[label]) for label in pack]
                    if len(set(nvals)) != 1:
                        raise ValueError("SAT fibre-degree replay regression")
                    n = nvals[0]
                    q = sum(bvals)
                    if 6 * n != 2 * q + 48:
                        raise ValueError("SAT six-fibre identity regression")
                    if n > cap_n or max(bvals) > cap_b:
                        raise ValueError("SAT Hurwitz-cap replay regression")
                    factor_rows.append({"boundary_pairings": bvals, "factor_degree": n, "q_boundary": q})
                witness = {
                    "picard_coordinates": xvals,
                    "boundary_pairings_33_to_44": pairings[32:44],
                    "factor_rows": factor_rows,
                }
                out.update({
                    "verdict": "SAT_RELAXED_LINEAR_FACTOR_HURWITZ_CAP",
                    "factor_rows": factor_rows,
                    "witness_sha256": csha(witness),
                })
            rows.append(out)

    body = {
        "schema": "STAGE32_32_01_178_N349B_FACTOR_HURWITZ_BOUNDARY_CAP_V1",
        "node_id": "N349B",
        "source_locks": {
            "n349_checkpoint_canonical": EXPECTED_N349,
            "n349a_checkpoint_canonical": EXPECTED_N349A,
            "n349_hostile_audit_consumed": False,
            "retained_bundle_canonical": EXPECTED_BUNDLE,
            "retained_marking_canonical": EXPECTED_MARKING,
            "ao_source_note_blob_sha1": "242088adab5c86292154a6de9bc3563ba73b4f43",
        },
        "exact_reduction": {
            "factor_base_genus": 0,
            "exceptional_mass": 48,
            "node_preimage_count_under_n349": 48,
            "six_fibre_identity": "6n=2q+48",
            "hurwitz_necessary_inequality_under_n349": "2g-2+2n >= q",
            "derived_factor_degree_cap": "n<=22+2g",
            "derived_boundary_pairing_cap": "C.E<=7+g on all 12 boundary elliptics",
            "solver_logic": "QF_LIA",
            "self_square_used": False,
            "per_terminal_timeout_ms": PER_TERMINAL_TIMEOUT_MS,
            "normal_nonnegativity_used": True,
        },
        "aggregate": {
            "terminal_count": len(rows),
            "sat_count": sat,
            "unsat_count": unsat,
            "unknown_count": unknown,
            "sat_partition": sat_partition,
            "unsat_partition": unsat_partition,
            "unknown_partition": unknown_partition,
        },
        "rows": rows,
        "semantics": {
            "unsat_is_exact_for_the_relaxed_integer_picard_problem": True,
            "unsat_is_conditional_on_n349_boundary_equality_input": True,
            "n349_hostile_audit_still_required": True,
            "sat_is_only_relaxed_numerical_picard_feasibility": True,
            "unknown_receives_zero_credit": True,
            "self_square_omission_makes_unsat_safe": True,
            "actual_integral_irreducible_member_not_constructed": True,
            "production_leaf_credit": False,
            "n350_producer_registry_unchanged": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "hostile_audit_required_before_main_credit": True,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N349B_EXACT_RELAXED_FACTOR_HURWITZ_CAP_LEDGER",
        "sat": sat,
        "unsat": unsat,
        "unknown": unknown,
        "sat_g0": sat_partition["g0-d176"],
        "sat_g1": sat_partition["g1-d192"],
        "unsat_g0": unsat_partition["g0-d176"],
        "unsat_g1": unsat_partition["g1-d192"],
        "canonical": body["canonical_sha256_without_this_field"],
        "n349_audit_consumed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
