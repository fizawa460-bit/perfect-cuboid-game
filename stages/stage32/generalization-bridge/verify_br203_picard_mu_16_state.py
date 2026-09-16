#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PAIRING = ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py"
BUNDLE = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
BR202 = HERE / "BR202-P1-K8-FULL-QA-BOUNDED-RESULT.json"

LOCKS = {
    PAIRING: "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    BUNDLE: "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    BR202: "06d0d21e5543cd5b5195c93ae431fbc186edd6ba",
}
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_DEN = 8
EXPECTED_B_ORIGINAL_SHA256 = "00bb173ee80c8cd347fe8f378dffe1e89c88107fecca7cb1d5b62e3b04d63472"
EXPECTED_NORMAL_HNF_SHA256 = "9c9ed6c47e8e67bae0b37222b9bd8f99be69045e9ef65baafa7ea8de7683c495"
EXPECTED_NORMAL_COEFFICIENTS_SHA256 = "bd4a45435c101d76c8f8a75c97da4dd1f46fc79e37a4e4bfe6414133fe00056f"
EXPECTED_NORMAL_QUOTIENT = 2**169
EXPECTED_NORMAL_PLUS_FREE_QUOTIENT = 2**165
EXPECTED_ACTIVE_ROWS = 46
EXPECTED_FREE_IMAGE = 16
EXPECTED_MU_MAX = 8
NORMAL_COUNT = 92
X4_LABEL = 49
ASSIGNMENT_LABELS = [95,99,103,102,49,97,94,101,93,98,96]
TERMINAL_EXCEPTIONAL_LABELS = [v for v in ASSIGNMENT_LABELS if v != X4_LABEL]
A_LABELS = [103,102,101]
BC_LABELS = [95,99,97,94,93,98,96]


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def matrix_list(m) -> list[list[int]]:
    return [[int(m[i,j]) for j in range(m.cols)] for i in range(m.rows)]


def lcm_denominator(m, sympy) -> int:
    den = 1
    for q in m:
        den = math.lcm(den, int(sympy.denom(q)))
    return den


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def hnf_lattice(B, den: int, generator_positions: list[int], Matrix, hermite_normal_form):
    suffix = B[:, generator_positions] if generator_positions else Matrix.zeros(B.rows, 0)
    lattice = suffix.row_join(den * Matrix.eye(B.rows))
    hnf = hermite_normal_form(lattice)
    req(hnf.shape == (B.rows, B.rows) and hnf.det() != 0, "HNF lattice regression")
    return hnf


def extension_check(B, den: int, assigned: list[int], unassigned: list[int], *, Matrix, sympy, hermite_normal_form):
    req(not (set(assigned) & set(unassigned)), "assigned/unassigned overlap")
    req(sorted(assigned + unassigned) == list(range(B.cols)), "coordinate partition regression")
    hnf = hnf_lattice(B, den, unassigned, Matrix, hermite_normal_form)
    inv = hnf.inv()
    modulus = lcm_denominator(inv, sympy)
    inv_int_q = inv * modulus
    req(all(sympy.denom(v) == 1 for v in inv_int_q), "scaled HNF inverse nonintegral")
    inv_int = Matrix([[int(inv_int_q[i,j]) for j in range(inv_int_q.cols)] for i in range(inv_int_q.rows)])
    coeff = inv_int * B[:, assigned]
    rows = []
    if modulus != 1:
        for i in range(coeff.rows):
            row = [int(coeff[i,j]) % modulus for j in range(coeff.cols)]
            if any(row):
                rows.append(row)
    return {
        "hnf": hnf,
        "modulus": modulus,
        "coefficients": rows,
        "active_congruence_rows": len(rows),
        "quotient_index": abs(int(hnf.det())),
        "hnf_sha256": csha(matrix_list(hnf)),
        "coefficients_sha256": csha(rows),
    }


def add_state(a: tuple[int,...], b: tuple[int,...], q: int) -> tuple[int,...]:
    return tuple((x+y) % q for x,y in zip(a,b))


def neg_state(a: tuple[int,...], q: int) -> tuple[int,...]:
    return tuple((-x) % q for x in a)


def subgroup_shortest(generators: list[tuple[int,...]], q: int) -> dict[tuple[int,...], int]:
    zero = (0,) * len(generators[0])
    dist = {zero: 0}
    todo = deque([zero])
    while todo:
        cur = todo.popleft()
        nd = dist[cur] + 1
        for gen in generators:
            nxt = add_state(cur, gen, q)
            if nxt not in dist:
                dist[nxt] = nd
                todo.append(nxt)
    return dist


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=HERE / "BR203-PICARD-MU-16-STATE-RESULT.json")
    args = ap.parse_args()

    # Fail closed before executing retained Python payloads.
    for path, expected in LOCKS.items():
        req(path.is_file(), f"missing source {path.relative_to(ROOT)}")
        req(git_blob(path) == expected, f"source blob drift {path.relative_to(ROOT)}")

    import sympy
    from sympy import Matrix
    from sympy.matrices.normalforms import hermite_normal_form

    pairing = load_module(PAIRING, "stage32_br203_pairing")
    retained = load_module(BUNDLE, "stage32_br203_retained")
    bundle = retained.load()
    req(bundle.get("canonical_sha256") == EXPECTED_BUNDLE_CANONICAL, "retained bundle canonical drift")

    transform = pairing.RetainedBasisPairingTransform.from_bundle(bundle)
    req(int(transform.den) == EXPECTED_DEN, "selected64 denominator drift")

    # pairing_prefix_engine stores the selected64 coordinate model in
    # exceptional-first / curve-second order.  Reorder columns of den*S^-1
    # back to the canonical INDLIST order used by BC2-18 before reproducing
    # its normal-eliminated HNF system.
    reordered_labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    original_labels = [int(v) for v in pairing.INDLIST]
    req(sorted(reordered_labels) == sorted(original_labels), "selected64 label-set drift")
    col_for_label = {label: i for i, label in enumerate(reordered_labels)}
    B_reordered = transform.inverse_integer
    B = B_reordered[:, [col_for_label[label] for label in original_labels]]
    req(csha(matrix_list(B)) == EXPECTED_B_ORIGINAL_SHA256, "BC2 selected64 inverse replay drift")

    normal_pos = [j for j,label in enumerate(original_labels) if label <= NORMAL_COUNT]
    exceptional_pos = [j for j,label in enumerate(original_labels) if label > NORMAL_COUNT]
    req(len(normal_pos) == 35 and len(exceptional_pos) == 29, "35/29 selected partition drift")
    exceptional_labels = [original_labels[j] for j in exceptional_pos]
    req(all(label in exceptional_labels for label in TERMINAL_EXCEPTIONAL_LABELS), "terminal exceptional label drift")

    full = extension_check(
        B, EXPECTED_DEN, exceptional_pos, normal_pos,
        Matrix=Matrix, sympy=sympy, hermite_normal_form=hermite_normal_form,
    )
    req(full["modulus"] == 8, "normal-eliminated modulus drift")
    req(full["active_congruence_rows"] == EXPECTED_ACTIVE_ROWS, "active row count drift")
    req(full["quotient_index"] == EXPECTED_NORMAL_QUOTIENT, "normal quotient drift")
    req(full["hnf_sha256"] == EXPECTED_NORMAL_HNF_SHA256, "normal HNF drift")
    req(full["coefficients_sha256"] == EXPECTED_NORMAL_COEFFICIENTS_SHA256, "normal coefficient drift")

    terminal_set = set(TERMINAL_EXCEPTIONAL_LABELS)
    free_labels = [label for label in exceptional_labels if label not in terminal_set]
    req(len(free_labels) == 19, "free selected exceptional count drift")
    pos_by_label = {label:j for j,label in enumerate(original_labels)}
    free_pos = [pos_by_label[label] for label in free_labels]
    terminal_pos = [pos_by_label[label] for label in TERMINAL_EXCEPTIONAL_LABELS]

    normal_hnf = full["hnf"]
    normal_index = full["quotient_index"]
    normal_plus_free_hnf = hnf_lattice(B, EXPECTED_DEN, normal_pos + free_pos, Matrix, hermite_normal_form)
    normal_plus_free_index = abs(int(normal_plus_free_hnf.det()))
    req(normal_plus_free_index == EXPECTED_NORMAL_PLUS_FREE_QUOTIENT, "normal+free quotient drift")
    req(normal_index // normal_plus_free_index == EXPECTED_FREE_IMAGE, "free exceptional image-size drift")

    def image_size(extra_labels: list[int]) -> tuple[int,int]:
        h = hnf_lattice(B, EXPECTED_DEN, normal_pos + [pos_by_label[v] for v in extra_labels], Matrix, hermite_normal_form)
        idx = abs(int(h.det()))
        req(normal_index % idx == 0, "image index divisibility regression")
        return normal_index // idx, idx

    A_image, A_quotient = image_size(A_LABELS)
    BC_image, BC_quotient = image_size(BC_LABELS)
    terminal_image, terminal_quotient = image_size(TERMINAL_EXCEPTIONAL_LABELS)
    free_A_image, free_A_quotient = image_size(free_labels + A_LABELS)
    free_BC_image, free_BC_quotient = image_size(free_labels + BC_LABELS)
    free_terminal_image, free_terminal_quotient = image_size(free_labels + TERMINAL_EXCEPTIONAL_LABELS)

    # The 46 active congruence rows are a canonical finite syndrome model for
    # exceptional coordinates modulo the normal lattice.  Extract the 29
    # exceptional columns, then compute the exact shortest nonnegative mass in
    # the subgroup generated by the 19 free exceptional columns.
    coeff = full["coefficients"]
    exc_col = {label:i for i,label in enumerate(exceptional_labels)}
    def syndrome_column(label: int) -> tuple[int,...]:
        j = exc_col[label]
        return tuple(int(row[j]) % 8 for row in coeff)

    free_generators = [syndrome_column(label) for label in free_labels]
    mu = subgroup_shortest(free_generators, 8)
    req(len(mu) == EXPECTED_FREE_IMAGE, "free syndrome closure is not 16 states")
    req(max(mu.values()) <= EXPECTED_MU_MAX, "mu universal bound regression")

    # Stable IDs are assigned by lexicographically sorted 46-row syndrome.
    states = sorted(mu)
    state_id = {state:i for i,state in enumerate(states)}
    mu_table = [{"id": state_id[state], "mu": int(mu[state]), "syndrome": list(state)} for state in states]
    mu_hist = Counter(int(v) for v in mu.values())

    terminal_columns = {label: syndrome_column(label) for label in TERMINAL_EXCEPTIONAL_LABELS}
    A_columns = {label: terminal_columns[label] for label in A_LABELS}
    BC_columns = {label: terminal_columns[label] for label in BC_LABELS}

    # A small exact algebraic regression: every free generator is represented
    # in the closure and every closure state has an inverse in the same group.
    for gen in free_generators:
        req(gen in mu, "free generator missing from syndrome closure")
    for state in states:
        req(neg_state(state, 8) in mu, "free syndrome group inverse missing")

    result = {
        "schema": "STAGE32_BR203_PICARD_MU_16_STATE_V1",
        "status": "PASS_SOURCE_LOCKED_16_STATE_MU_ZERO_CREDIT",
        "source_locks": {
            "pairing_prefix_engine_git_blob_sha1": LOCKS[PAIRING],
            "picard_base_rows_retained_git_blob_sha1": LOCKS[BUNDLE],
            "br202_result_git_blob_sha1": LOCKS[BR202],
            "retained_bundle_canonical": EXPECTED_BUNDLE_CANONICAL,
            "bc2_18_historical_generator_git_blob_sha1": "1e2ed93cae3c5b446c8d90c1ae2250be83289c79",
            "bc2_18_historical_checkpoint_git_blob_sha1": "0e269d5ec6da24b9b887b6dd40f4b4f33242e154"
        },
        "normal_eliminated_system": {
            "selected_normal_count": len(normal_pos),
            "selected_exceptional_count": len(exceptional_pos),
            "terminal_exceptional_count": len(TERMINAL_EXCEPTIONAL_LABELS),
            "free_selected_exceptional_count": len(free_labels),
            "modulus": full["modulus"],
            "active_congruence_rows": full["active_congruence_rows"],
            "normal_quotient_index": normal_index,
            "normal_hnf_sha256": full["hnf_sha256"],
            "coefficients_sha256": full["coefficients_sha256"],
            "normal_plus_free_quotient_index": normal_plus_free_index,
            "free_exceptional_image_size": normal_index // normal_plus_free_index
        },
        "image_cardinalities": {
            "A_labels": A_LABELS,
            "A_image_size_mod_normal": A_image,
            "A_residual_quotient_index": A_quotient,
            "BC_labels": BC_LABELS,
            "BC_image_size_mod_normal": BC_image,
            "BC_residual_quotient_index": BC_quotient,
            "terminal10_image_size_mod_normal": terminal_image,
            "terminal10_residual_quotient_index": terminal_quotient,
            "free_plus_A_image_size_mod_normal": free_A_image,
            "free_plus_A_residual_quotient_index": free_A_quotient,
            "free_plus_BC_image_size_mod_normal": free_BC_image,
            "free_plus_BC_residual_quotient_index": free_BC_quotient,
            "free_plus_terminal10_image_size_mod_normal": free_terminal_image,
            "free_plus_terminal10_residual_quotient_index": free_terminal_quotient
        },
        "mu": {
            "state_count": len(states),
            "max_mu": max(mu.values()),
            "histogram": {str(k):int(v) for k,v in sorted(mu_hist.items())},
            "table": mu_table,
            "table_sha256": csha(mu_table),
            "free_labels": free_labels,
            "free_generator_columns_sha256": csha([list(v) for v in free_generators])
        },
        "terminal_syndrome_columns": {
            "A": {str(k):list(v) for k,v in A_columns.items()},
            "BC": {str(k):list(v) for k,v in BC_columns.items()},
            "sha256": csha({"A":{str(k):list(v) for k,v in A_columns.items()}, "BC":{str(k):list(v) for k,v in BC_columns.items()}})
        },
        "next": {
            "id": "BR203_BOUNDED_MU_INTERSECTION",
            "condition": "for each BR202 compact A/BC state, target=-(sigma_A+sigma_BC); reject if target not in the 16-state free image, otherwise require e-a-b-c >= mu[target]",
            "terminal_identity_materialization": False,
            "FULL178_scaleout_authorized": False
        },
        "credit": {
            "stage32_main": False,
            "theorem": False,
            "effectivity": False,
            "receiver": False,
            "endpoint": False,
            "full178_complete": False,
            "perfect_cuboid": False,
            "merge": False
        }
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "A_image_size": A_image,
        "BC_image_size": BC_image,
        "terminal10_image_size": terminal_image,
        "free_image_size": len(states),
        "max_mu": max(mu.values()),
        "mu_histogram": result["mu"]["histogram"],
        "mu_table_sha256": result["mu"]["table_sha256"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
