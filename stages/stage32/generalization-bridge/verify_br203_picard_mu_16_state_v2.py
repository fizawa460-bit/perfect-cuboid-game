#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib
import importlib.util
import json
import math
import sys
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
PAIRING = RESIDUAL / "pairing_prefix_engine.py"
ADAPTER = RESIDUAL / "hperp_integral_adapter.py"
BUNDLE = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
BR202 = HERE / "BR202-P1-K8-FULL-QA-BOUNDED-RESULT.json"

LOCKS = {
    PAIRING: "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ADAPTER: "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    BUNDLE: "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    MARKING: "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    BR202: "06d0d21e5543cd5b5195c93ae431fbc186edd6ba",
}
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_DEN = 8
EXPECTED_B_ORIGINAL_SHA256 = "00bb173ee80c8cd347fe8f378dffe1e89c88107fecca7cb1d5b62e3b04d63472"
EXPECTED_NORMAL_HNF_SHA256 = "9c9ed6c47e8e67bae0b37222b9bd8f99be69045e9ef65baafa7ea8de7683c495"
EXPECTED_NORMAL_COEFFICIENTS_SHA256 = "bd4a45435c101d76c8f8a75c97da4dd1f46fc79e37a4e4bfe6414133fe00056f"
EXPECTED_NORMAL_QUOTIENT = 2**169
EXPECTED_ACTIVE_ROWS = 46
EXPECTED_FREE_IMAGE = 16
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
    sys.modules[name] = mod
    try:
        spec.loader.exec_module(mod)
    except BaseException:
        sys.modules.pop(name, None)
        raise
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
    req(bool(generators), "empty generator set")
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

    # Fail closed before executing any retained or adapter Python payload.
    for path, expected in LOCKS.items():
        req(path.is_file(), f"missing source {path.relative_to(ROOT)}")
        req(git_blob(path) == expected, f"source blob drift {path.relative_to(ROOT)}")

    import sympy
    from sympy import Matrix
    from sympy.matrices.normalforms import hermite_normal_form

    sys.path.insert(0, str(RESIDUAL))
    pairing = importlib.import_module("pairing_prefix_engine")
    hpadj = importlib.import_module("hperp_integral_adapter")
    retained = load_module(BUNDLE, "stage32_br203_v2_retained")
    marking_mod = load_module(MARKING, "stage32_br203_v2_marking")
    bundle = retained.load()
    marking = marking_mod.load()
    req(bundle.get("canonical_sha256") == EXPECTED_BUNDLE_CANONICAL, "retained bundle canonical drift")
    req(marking.get("canonical_sha256") == EXPECTED_MARKING_CANONICAL, "retained marking canonical drift")

    # Historical BC2-18 did not use the retained Gram rows as the selected64
    # pairing coordinates.  It reconstructed the all140-to-retained-basis
    # pairing matrix and selected the actual INDLIST curve rows.  Replay that
    # exact coordinate model here before taking the inverse.
    adapter = hpadj.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    req(P.shape == (140, 64), "all140 pairing matrix shape drift")
    original_labels = [int(v) for v in pairing.INDLIST]
    selected_indices = [label - 1 for label in original_labels]
    Psel = P.extract(selected_indices, list(range(64)))
    req(Psel.det() != 0, "historical selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = lcm_denominator(Pinv, sympy)
    req(den == EXPECTED_DEN, "historical selected64 denominator drift")
    Bq = Pinv * den
    req(all(sympy.denom(v) == 1 for v in Bq), "historical selected64 scaled inverse nonintegral")
    B = Matrix([[int(Bq[i,j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    req(Psel * B == den * Matrix.eye(64), "historical selected64 inverse reconstruction drift")
    req(csha(matrix_list(B)) == EXPECTED_B_ORIGINAL_SHA256, "BC2 selected64 inverse replay drift")

    normal_pos = [j for j,label in enumerate(original_labels) if label <= NORMAL_COUNT]
    exceptional_pos = [j for j,label in enumerate(original_labels) if label > NORMAL_COUNT]
    req(len(normal_pos) == 35 and len(exceptional_pos) == 29, "35/29 selected partition drift")
    exceptional_labels = [original_labels[j] for j in exceptional_pos]
    req(all(label in exceptional_labels for label in TERMINAL_EXCEPTIONAL_LABELS), "terminal exceptional label drift")

    full = extension_check(
        B, den, exceptional_pos, normal_pos,
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

    normal_index = full["quotient_index"]
    normal_plus_free_hnf = hnf_lattice(B, den, normal_pos + free_pos, Matrix, hermite_normal_form)
    normal_plus_free_index = abs(int(normal_plus_free_hnf.det()))
    req(normal_index % normal_plus_free_index == 0, "normal/free quotient divisibility regression")
    free_image_size = normal_index // normal_plus_free_index
    req(free_image_size == EXPECTED_FREE_IMAGE, f"free exceptional image-size drift: {free_image_size}")

    def image_size(extra_labels: list[int]) -> tuple[int,int]:
        h = hnf_lattice(B, den, normal_pos + [pos_by_label[v] for v in extra_labels], Matrix, hermite_normal_form)
        idx = abs(int(h.det()))
        req(normal_index % idx == 0, "image index divisibility regression")
        return normal_index // idx, idx

    A_image, A_quotient = image_size(A_LABELS)
    BC_image, BC_quotient = image_size(BC_LABELS)
    terminal_image, terminal_quotient = image_size(TERMINAL_EXCEPTIONAL_LABELS)
    free_A_image, free_A_quotient = image_size(free_labels + A_LABELS)
    free_BC_image, free_BC_quotient = image_size(free_labels + BC_LABELS)
    free_terminal_image, free_terminal_quotient = image_size(free_labels + TERMINAL_EXCEPTIONAL_LABELS)

    # The 46 active HNF congruence rows give the exact exceptional syndrome
    # modulo the normal lattice.  Compute the shortest nonnegative unit mass
    # needed to realize every state in the image of the 19 free exceptional
    # coordinates.  This is the mu table consumed by the bounded BR202 replay.
    coeff = full["coefficients"]
    exc_col = {label:i for i,label in enumerate(exceptional_labels)}

    def syndrome_column(label: int) -> tuple[int,...]:
        j = exc_col[label]
        return tuple(int(row[j]) % den for row in coeff)

    free_generators = [syndrome_column(label) for label in free_labels]
    mu = subgroup_shortest(free_generators, den)
    req(len(mu) == free_image_size, "free syndrome closure/image-size disagreement")

    states = sorted(mu)
    state_id = {state:i for i,state in enumerate(states)}
    mu_table = [{"id": state_id[state], "mu": int(mu[state]), "syndrome": list(state)} for state in states]
    mu_hist = Counter(int(v) for v in mu.values())

    terminal_columns = {label: syndrome_column(label) for label in TERMINAL_EXCEPTIONAL_LABELS}
    A_columns = {label: terminal_columns[label] for label in A_LABELS}
    BC_columns = {label: terminal_columns[label] for label in BC_LABELS}

    for gen in free_generators:
        req(gen in mu, "free generator missing from syndrome closure")
    for state in states:
        req(neg_state(state, den) in mu, "free syndrome group inverse missing")

    result = {
        "schema": "STAGE32_BR203_PICARD_MU_16_STATE_V2",
        "status": "PASS_SOURCE_LOCKED_HISTORICAL_BC2_COORDINATES_16_STATE_MU_ZERO_CREDIT",
        "source_locks": {
            "pairing_prefix_engine_git_blob_sha1": LOCKS[PAIRING],
            "hperp_integral_adapter_git_blob_sha1": LOCKS[ADAPTER],
            "picard_base_rows_retained_git_blob_sha1": LOCKS[BUNDLE],
            "stage32_picard_marking_retained_git_blob_sha1": LOCKS[MARKING],
            "br202_result_git_blob_sha1": LOCKS[BR202],
            "retained_bundle_canonical": EXPECTED_BUNDLE_CANONICAL,
            "retained_marking_canonical": EXPECTED_MARKING_CANONICAL,
            "bc2_18_historical_generator_git_blob_sha1": "1e2ed93cae3c5b446c8d90c1ae2250be83289c79",
            "bc2_18_historical_checkpoint_git_blob_sha1": "0e269d5ec6da24b9b887b6dd40f4b4f33242e154"
        },
        "selected64_replay": {
            "coordinate_source": "HperpIntegralPairingAdapter all140 pairing rows at pairing_prefix_engine.INDLIST",
            "selected_labels_1based": original_labels,
            "inverse_denominator": den,
            "inverse_integer_sha256": csha(matrix_list(B)),
            "historical_bc2_18_exact_match": True
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
            "free_exceptional_image_size": free_image_size
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
            "sha256": csha({
                "A": {str(k):list(v) for k,v in A_columns.items()},
                "BC": {str(k):list(v) for k,v in BC_columns.items()}
            })
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
