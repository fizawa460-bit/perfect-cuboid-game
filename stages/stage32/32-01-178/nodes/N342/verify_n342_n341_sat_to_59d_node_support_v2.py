#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import z3
from sympy import Matrix, Rational

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
N230_DIR = HERE.parent / "N230"
EX5_CONSUMER = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_02_exact_witness_to_node_support.py"
NODE_BRIDGE = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-01b-runtime-node-coordinate-bridge.json"

sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(N230_DIR))
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from hperp_integral_adapter import HperpIntegralPairingAdapter
from pairing_prefix_engine import RetainedBasisPairingTransform
from n220_filtered_terminal_indexer import N220FilteredTerminalIndexer

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
N341_RUN = 34424019499
N341_JOB = 102705288033
N341_CANONICAL = "672ca52e1b71e7bde2b14de6320ae57dddcbf6f0d3817f3244f27eec20cce315"
N341_VERIFIER_BLOB = "70d17967f7a965de4994dce1bc70a398468ef42e"
EX5_AUDITED_HEAD = "a5e59bab3f7fe5a31e356c5a78edcbd741b093a6"
EX5_CONSUMER_BLOB = "5941a6270def08a614797be84b3242aaa83def72"
NODE_BRIDGE_BLOB = "2a14a683e8ec38ec993eb711841c466f2be6eb06"
EXCEPTIONAL_LABELS = list(range(93, 141))
NORMAL_LABELS = list(range(1, 93))
X4_LABEL = 49
TARGETS = [
    ("g0-d176", 0, 176, 48, 3104, [3,7,11,15,19,23,27,31,35,39]),
    ("g1-d192", 1, 192, 48, 3408, [3,7,11,15,19,23,27,31,35,39,43]),
]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module(path: Path, name: str):
    if not path.exists():
        raise FileNotFoundError(f"required integration source missing: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_retained(path: Path, name: str) -> dict:
    payload = load_module(path, name).load()
    if not isinstance(payload, dict):
        raise ValueError("retained payload must be dict")
    return payload


def zsum(coeffs, vars_):
    return z3.Sum([int(a) * v for a, v in zip(coeffs, vars_)])


def ints(v: Matrix) -> list[int]:
    out = []
    for i in range(v.rows):
        q = Rational(v[i, 0])
        if q.q != 1:
            raise ValueError(f"nonintegral coordinate {i}: {q}")
        out.append(int(q))
    return out


def main() -> None:
    bundle = load_retained(RETAINED, "s32_n342v2_bundle")
    marking = load_retained(MARKING, "s32_n342v2_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("bundle canonical drift")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("marking canonical drift")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    if transform.den != 8:
        raise ValueError("selected64 denominator drift")
    selected_labels = list(transform.certificate["selected_known_indices_1based"])
    if len(selected_labels) != 64 or sum(v > 92 for v in selected_labels) != 29:
        raise ValueError("selected64 partition drift")

    data = reconstruct_translation_data(marking, bundle)
    M = data["M"]
    pivots = [int(v) for v in data["pivot_rows"]]
    selected_M = M.extract(pivots, list(range(59)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform drift")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("reduced transform is not unimodular")
    kernel_reduced = data["K"] * U
    Mred = M * U

    # Cache one exact left solve for every later 59D witness.
    _, pivot_rows = kernel_reduced.T.rref()
    pivot_rows = list(pivot_rows)
    if len(pivot_rows) != 59:
        raise ValueError("kernel rank drift")
    square_inv = kernel_reduced.extract(pivot_rows, list(range(59))).inv()

    ex5 = load_module(EX5_CONSUMER, "s32_n342v2_ex5")
    bridge_rows, bridge_claimed = ex5.load_node_bridge(NODE_BRIDGE)
    bridge_raw = json.loads(NODE_BRIDGE.read_text())
    raw_claimed = bridge_raw.get("canonical_sha256_without_this_field")
    if raw_claimed != bridge_claimed:
        raise ValueError("node bridge claimed canonical disagreement")
    if raw_claimed is not None:
        body = dict(bridge_raw)
        body.pop("canonical_sha256_without_this_field", None)
        if csha(body) != raw_claimed:
            raise ValueError("node bridge canonical drift")
        node_bridge_canonical = raw_claimed
    else:
        node_bridge_canonical = csha(bridge_raw)

    yn = [z3.Int(f"yn_{j}") for j in range(35)]
    yexpr = [z3.IntVal(1) for _ in range(29)] + yn
    B = transform.inverse_integer
    P = adapter.pairing_matrix
    num_expr = [zsum([B[i, j] for j in range(64)], yexpr) for i in range(64)]
    pairing_num = [zsum([P[r, i] for i in range(64)], num_expr) for r in range(140)]
    solver = z3.SolverFor("QF_LIA")
    for expr in num_expr:
        solver.add(expr % 8 == 0)
    for label in EXCEPTIONAL_LABELS:
        solver.add(pairing_num[label - 1] == 8)
    for label in NORMAL_LABELS:
        solver.add(pairing_num[label - 1] >= 0)
    normal_total_num = z3.Sum([pairing_num[label - 1] for label in NORMAL_LABELS])
    x4_num = pairing_num[X4_LABEL - 1]

    gram = Matrix(bundle["picard_gram_64x64"])
    phi = Matrix([
        list(data["bridge"].degree_functional),
        list(data["bridge"].exceptional_mass_functional),
        list(data["bridge"].first_normal_half_functional),
    ])

    rows = []
    for row_id, genus, degree, e, normal_mass, sat_x4s in TARGETS:
        indexer = N220FilteredTerminalIndexer(genus, degree, e)
        if indexer.accepted_exceptional_count != 1:
            raise ValueError("N260 one-exceptional-block drift")
        solver.push()
        for v in yn:
            solver.add(v >= 0, v <= normal_mass)
        solver.add(normal_total_num == 8 * normal_mass)
        for x4 in sat_x4s:
            solver.push()
            solver.add(x4_num == 8 * x4)
            if solver.check() != z3.sat:
                raise ValueError(f"source-locked N341 SAT terminal did not rematerialize: {row_id}/x4={x4}")
            model = solver.model()
            yvals = [1] * 29 + [int(model.eval(v, model_completion=True).as_long()) for v in yn]
            if not transform.full_membership(yvals):
                raise ValueError("selected64 membership replay failed")
            xvals = transform.reconstruct_picard_basis(yvals)
            pairings = [sum(int(P[r, i]) * xvals[i] for i in range(64)) for r in range(140)]
            if pairings[92:] != [1] * 48:
                raise ValueError("exceptional [1]^48 replay failed")
            if min(pairings[:92]) < 0 or sum(pairings[:92]) != normal_mass or pairings[48] != x4:
                raise ValueError("normal pairing replay failed")

            x = Matrix(xvals)
            z = data["C"] * x
            x0 = data["x0_map"] * z
            q = x - x0
            if data["C"] * q != Matrix.zeros(5, 1):
                raise ValueError("affine kernel replay failed")
            qsel = q.extract(pivot_rows, [0])
            r = square_inv * qsel
            if kernel_reduced * r != q:
                raise ValueError("59D witness solve failed")
            zvals = ints(z)
            rvals = ints(r)
            if data["N"] * x != data["B"] * z:
                raise ValueError("Reynolds numerator identity failed")
            if data["pairing_x0_map"] * z + Mred * r != Matrix(pairings):
                raise ValueError("59D all140 replay failed")

            slice_values = ints(phi * x)
            if slice_values[0] != degree or slice_values[1] != e:
                raise ValueError("degree/exceptional slice replay failed")
            a = slice_values[2]
            terminal_pairings = list(indexer.unrank(x4))
            old_rank = int(indexer.old_rank_of_filtered(x4))
            disp = indexer.disposition_of_old(old_rank)
            if terminal_pairings[4] != x4 or disp.get("disposition") != "N220_SURVIVOR" or int(disp["filtered_rank"]) != x4:
                raise ValueError("canonical old-rank handoff failed")

            evidence = {
                "target": {"row_id": row_id, "e": e, "a": a, "z": zvals},
                "result": {"status": "SAT", "witness_r_reduced": rvals},
            }
            support = ex5.reconstruct(evidence, bundle, marking, bridge_rows)
            if support.get("status") != "PASS_EXACT_WITNESS_TO_NODE_SUPPORT":
                raise ValueError("EX5 consumer replay failed")
            exceptional = support["exceptional_support"]
            if exceptional["pairings_last48"] != [1] * 48 or int(exceptional["support_count"]) != 48:
                raise ValueError("labelled support replay failed")
            if not bool(exceptional["spans_p6"]):
                raise ValueError("full labelled support unexpectedly fails P6 span")

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
                "picard_coordinates_sha256": csha(xvals),
                "z": zvals,
                "a": a,
                "witness_r_reduced": rvals,
                "witness_r_reduced_sha256": csha(rvals),
                "all140_pairings_sha256": csha(pairings),
                "self_square": self_square,
                "required_self_square_lower": required_lower,
                "chosen_picard_model_self_square_pass": self_square >= required_lower,
                "node_support": {
                    "consumer_status": support["status"],
                    "pairings_last48_sha256": exceptional["pairings_last48_sha256"],
                    "support_count": int(exceptional["support_count"]),
                    "canonical_node_vector_rank": int(exceptional["canonical_node_vector_rank"]),
                    "projective_span_dimension": int(exceptional["projective_span_dimension"]),
                    "spans_p6": bool(exceptional["spans_p6"]),
                },
            })
            solver.pop()
        solver.pop()

    if len(rows) != 21:
        raise ValueError("N341 SAT terminal count drift")
    self_square_pass_count = sum(bool(r["chosen_picard_model_self_square_pass"]) for r in rows)
    body = {
        "schema": "STAGE32_32_01_178_N342_N341_SAT_TO_59D_NODE_SUPPORT_V2",
        "source_locks": {
            "n341_run_id": N341_RUN,
            "n341_job_id": N341_JOB,
            "n341_canonical_sha256": N341_CANONICAL,
            "n341_verifier_blob_sha1": N341_VERIFIER_BLOB,
            "n341_source_ledger": "157 UNSAT / 21 SAT / 0 unknown",
            "n341_sat_terminal_sets": {"g0-d176": TARGETS[0][5], "g1-d192": TARGETS[1][5]},
            "retained_bundle_canonical_sha256": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical_sha256": EXPECTED_MARKING_CANONICAL,
            "ex5_audited_head": EX5_AUDITED_HEAD,
            "ex5_exact_witness_consumer_blob_sha1": EX5_CONSUMER_BLOB,
            "node_bridge_blob_sha1": NODE_BRIDGE_BLOB,
            "node_bridge_canonical_sha256": node_bridge_canonical,
        },
        "result": {
            "sat_terminal_count": 21,
            "all_21_rematerialized_exact_picard64": True,
            "all_21_exact_reynolds59d_witness": True,
            "all_21_exact_old_rank_locator": True,
            "all_21_exact_labelled_support48": True,
            "all_21_support_span_p6": True,
            "chosen_picard_models_meeting_self_square_threshold": self_square_pass_count,
            "rows": rows,
        },
        "firewalls": {
            "n341_157_unsat_not_recomputed_here": True,
            "n341_sat_terminal_set_is_source_locked_not_promoted_by_shape": True,
            "labelled_support_not_inferred_from_scalar_e": True,
            "chosen_model_self_square_failure_if_any_is_not_terminal_unsat": True,
            "picard_numerical_class_is_not_effective_curve_existence": True,
            "n350_producer_registration_not_modified": True,
            "n350_hostile_audit_still_required_before_registration": True,
            "n260_n280_n310_n341_n342_audit_boundaries_preserved": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
