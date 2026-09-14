#!/usr/bin/env python3
from __future__ import annotations

import ast
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
HANDOFF = ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
GRF01 = HERE / "GRF-01-CONTRACT.json"
PREFIX = RESIDUAL / "pairing_prefix_engine.py"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"

sys.path.insert(0, str(BUNDLE_DIR))
import picard_base_rows_retained as retained_bundle

SOURCE_LOCKS = {
    HANDOFF: "8a30e3aa30777460f344eb19836dc725dd442329",
    GRF01: "a81ebccfa0e235fe33926e16a0bd67bfcb29cbc0",
    PREFIX: "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    BUNDLE_SOURCE: "82e4d450a1d852e34f6615440fb88a029c6e54eb",
}
EXPECTED_GRF01_CANONICAL = "18ce801f45bd95fec8e0a2f6001eff9fd80a9b6f6b416ccc9190d3b37adc3c43"
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(
        json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def parse_indlist(path: Path) -> list[int]:
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(t, ast.Name) and t.id == "INDLIST" for t in targets):
                value = ast.literal_eval(node.value)
                return [int(v) for v in value]
    raise RuntimeError("INDLIST not found in source-locked pairing_prefix_engine.py")


def invert_fraction_matrix(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    req(n > 0 and all(len(row) == n for row in a), "selected matrix is not square")
    aug = [
        [Fraction(v) for v in a[i]]
        + [Fraction(1 if i == j else 0) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col]), None)
        req(pivot is not None, "selected matrix is singular")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [v / p for v in aug[col]]
        for r in range(n):
            if r == col or not aug[r][col]:
                continue
            f = aug[r][col]
            aug[r] = [x - f * y for x, y in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def matmul_int(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    m = len(a)
    k = len(a[0])
    req(k == len(b), "matrix multiply shape mismatch")
    n = len(b[0])
    return [
        [sum(a[i][t] * b[t][j] for t in range(k)) for j in range(n)]
        for i in range(m)
    ]


def select_columns(a: list[list[int]], cols: list[int]) -> list[list[int]]:
    return [[row[j] for j in cols] for row in a]


def v2_mod8(v: int) -> int:
    v %= 8
    if v == 0:
        return 99
    if v & 1:
        return 0
    if v & 2:
        return 1
    return 2


def diagonalize_mod8(a: list[list[int]]) -> tuple[list[int], list[list[int]], list[list[int]]]:
    """Diagonalize over Z/8 by invertible row/column operations; return D and left U."""
    m = len(a)
    n = len(a[0]) if m else 0
    M = [[int(v) % 8 for v in row] for row in a]
    U = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    diag: list[int] = []
    k = 0
    while k < m and k < n:
        best = None
        best_v = 100
        for i in range(k, m):
            for j in range(k, n):
                vv = v2_mod8(M[i][j])
                if vv < best_v:
                    best_v = vv
                    best = (i, j)
        if best is None or best_v == 99:
            break
        i0, j0 = best
        if i0 != k:
            M[k], M[i0] = M[i0], M[k]
            U[k], U[i0] = U[i0], U[k]
        if j0 != k:
            for row in M:
                row[k], row[j0] = row[j0], row[k]

        d = 1 << best_v
        pivot = M[k][k] % 8
        unit = next(u for u in (1, 3, 5, 7) if (u * pivot) % 8 == d)
        M[k] = [(unit * v) % 8 for v in M[k]]
        U[k] = [(unit * v) % 8 for v in U[k]]
        req(M[k][k] == d, "failed to normalize Z/8 pivot")

        for i in range(k + 1, m):
            v = M[i][k] % 8
            req(v % d == 0, "nondivisible entry below minimal Z/8 pivot")
            q = v // d
            if q:
                M[i] = [(x - q * y) % 8 for x, y in zip(M[i], M[k])]
                U[i] = [(x - q * y) % 8 for x, y in zip(U[i], U[k])]
            req(M[i][k] == 0, "failed to clear Z/8 pivot column")

        for j in range(k + 1, n):
            v = M[k][j] % 8
            req(v % d == 0, "nondivisible entry right of minimal Z/8 pivot")
            q = v // d
            if q:
                for i in range(m):
                    M[i][j] = (M[i][j] - q * M[i][k]) % 8
            req(M[k][j] == 0, "failed to clear Z/8 pivot row")

        diag.append(d)
        k += 1

    rank = len(diag)
    for i in range(m):
        for j in range(n):
            expected = diag[i] if i == j and i < rank else 0
            req(M[i][j] == expected, "Z/8 diagonalization residual is not diagonal")
    req(
        all(diag[i] <= diag[i + 1] for i in range(len(diag) - 1)),
        "Z/8 diagonal factors are not valuation ordered",
    )
    return diag, U, M


def row_times_matrix_mod(
    row: list[int], matrix: list[list[int]], modulus: int
) -> tuple[int, ...]:
    cols = len(matrix[0])
    return tuple(
        sum(row[i] * matrix[i][j] for i in range(len(row))) % modulus
        for j in range(cols)
    )


def primitive_row(row: tuple[int, ...], modulus: int) -> tuple[int, tuple[int, ...]]:
    g = modulus
    for v in row:
        g = math.gcd(g, int(v))
    q = modulus // g
    vals = tuple((int(v) // g) % q for v in row)
    if q == 1:
        return 1, tuple(0 for _ in row)
    units = [u for u in range(1, q) if math.gcd(u, q) == 1]
    reps = [tuple((u * v) % q for v in vals) for u in units]
    return q, min(reps)


def image_invariants_mod8(encoded_rows: list[list[int]], domain_cols: int) -> list[int]:
    """Invariant factors of an image subgroup after embedding its 2-group target in (Z/8)^m."""
    if not encoded_rows:
        return []
    diag, _, _ = diagonalize_mod8(encoded_rows)
    req(len(diag) <= domain_cols, "image diagonal rank exceeds domain rank")
    invariants = sorted(8 // d for d in diag if d)
    req(all(v in (2, 4, 8) for v in invariants), "unexpected projected image invariant")
    return invariants


def main() -> None:
    for path, expected in SOURCE_LOCKS.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    grf01 = json.loads(GRF01.read_text())
    stored = grf01.pop("canonical_sha256_without_this_field", None)
    req(
        stored == EXPECTED_GRF01_CANONICAL and csha(grf01) == EXPECTED_GRF01_CANONICAL,
        "GRF-01 canonical drift",
    )
    req(
        grf01["status"] == "FAMILY_LEVEL_OBSTRUCTION_DESIGN_ONLY_HANDOFF_TO_178_NO_CREDIT",
        "GRF-01 ownership/status drift",
    )

    handoff = json.loads(HANDOFF.read_text())
    tm = handoff["terminal_to_picard64_map"]
    selected_labels = [int(v) for v in tm["selected_pairing_coordinate_order_1based"]]
    assignment_labels = [int(v) for v in tm["terminal_assignment_labels_1based"]]
    fixed_positions = [int(v) for v in tm["terminal_fixed_selected_positions_0based"]]
    free_positions = [int(v) for v in tm["free_selected_positions_0based"]]
    req(len(selected_labels) == 64 and len(set(selected_labels)) == 64, "selected64 label drift")
    req(len(assignment_labels) == 11 and len(set(assignment_labels)) == 11, "terminal fixed-label identity drift")
    req(fixed_positions == [selected_labels.index(v) for v in assignment_labels], "fixed selected-position drift")
    req(sorted(fixed_positions + free_positions) == list(range(64)), "selected64 fixed/free partition drift")
    req(len(free_positions) == 53, "selected64 free-coordinate count drift")
    req(int(tm["inverse_denominator"]) == 8, "selected64 denominator drift")

    indlist = parse_indlist(PREFIX)
    req(len(indlist) == 64 and len(set(indlist)) == 64, "source-locked INDLIST drift")
    expected_selected = [v for v in indlist if v > 92] + [v for v in indlist if v <= 92]
    req(selected_labels == expected_selected, "handoff selected64 order disagrees with source-locked prefix engine")

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == EXPECTED_BUNDLE_CANONICAL, "Picard bundle canonical drift")
    gram = [[int(v) for v in row] for row in bundle["picard_gram_64x64"]]
    req(len(gram) == 64 and all(len(row) == 64 for row in gram), "Picard Gram shape drift")
    req(all(gram[i][j] == gram[j][i] for i in range(64) for j in range(64)), "Picard Gram symmetry drift")
    source_row_by_label = {label: i for i, label in enumerate(indlist)}
    selected = [gram[source_row_by_label[label]][:] for label in selected_labels]

    inv = invert_fraction_matrix(selected)
    den = 1
    for row in inv:
        for v in row:
            den = math.lcm(den, v.denominator)
    req(den == 8, "selected64 inverse denominator is not 8")
    B: list[list[int]] = []
    for row in inv:
        out = []
        for v in row:
            w = v * den
            req(w.denominator == 1, "scaled inverse entry is not integral")
            out.append(int(w))
        B.append(out)

    ident8 = [[8 if i == j else 0 for j in range(64)] for i in range(64)]
    req(matmul_int(selected, B) == ident8, "selected64 inverse identity failed")
    req(csha(B) == tm["inverse_integer_matrix_sha256"], "selected64 inverse matrix hash drift")
    req(
        csha(B) == handoff["reconstructed_picard64_coordinate_identity"]["selected64_inverse_integer_matrix_sha256"],
        "reconstructed Picard64 inverse hash drift",
    )

    Bfixed = select_columns(B, fixed_positions)
    Bfree = select_columns(B, free_positions)
    req(csha(Bfixed) == tm["terminal_fixed_coefficient_matrix_sha256"], "fixed coefficient matrix hash drift")
    req(csha(Bfree) == tm["free_completion_coefficient_matrix_sha256"], "free coefficient matrix hash drift")

    diag, U, _ = diagonalize_mod8(Bfree)
    pivot_count = len(diag)
    zero_row_count = 64 - pivot_count
    quotient_invariants = sorted([d for d in diag if d > 1] + [8] * zero_row_count)
    quotient_order = math.prod(quotient_invariants) if quotient_invariants else 1

    raw_components: list[tuple[int, tuple[int, ...]]] = []
    for i, d in enumerate(diag):
        if d == 1:
            continue
        raw_components.append((d, row_times_matrix_mod(U[i], Bfixed, d)))
    for i in range(pivot_count, 64):
        raw_components.append((8, row_times_matrix_mod(U[i], Bfixed, 8)))

    active_raw = [(q, row) for q, row in raw_components if any(row)]
    primitive = sorted(set(primitive_row(row, q) for q, row in active_raw))
    primitive_rows = [
        {"modulus": int(q), "coefficients": list(row)}
        for q, row in primitive
        if q != 1
    ]
    req(primitive_rows, "projected completion kernel unexpectedly trivial")

    embedded_rows = [
        [((8 // q) * int(v)) % 8 for v in row]
        for q, row in raw_components
    ]
    projected_image_invariants = image_invariants_mod8(embedded_rows, 11)
    projected_image_order = math.prod(projected_image_invariants) if projected_image_invariants else 1
    req(8 ** 11 % projected_image_order == 0, "projected image order does not divide fixed residue domain")
    kernel_cardinality_mod8 = 8 ** 11 // projected_image_order

    signatures: dict[int, tuple[int, ...]] = {}
    orders: dict[int, int] = {}
    for j, label in enumerate(assignment_labels):
        sig = tuple(row[j] for row in embedded_rows)
        signatures[label] = sig
        orders[label] = next(
            t for t in (1, 2, 4, 8)
            if all((t * v) % 8 == 0 for v in sig)
        )

    classes: dict[tuple[int, ...], list[int]] = {}
    for label in assignment_labels:
        classes.setdefault(signatures[label], []).append(label)
    equivalence_classes = sorted(
        (sorted(v) for v in classes.values()), key=lambda x: (x[0], len(x), x)
    )

    groups = handoff["stored_10_exceptional_coordinate_identity"]["groups"]
    group_sum_collapse = {}
    for name in ("a", "b", "c"):
        labels = [int(v) for v in groups[name]]
        group_sum_collapse[name] = len({signatures[label] for label in labels}) == 1

    body = {
        "schema": "STAGE32_MAIN_GRF02_SELECTED64_PROJECTED_KERNEL_DERIVATION_V2",
        "stage": 32,
        "surface": "MAIN",
        "status": "EXACT_SYMBOLIC_PROJECTED_KERNEL_ONLY_NO_CONCRETE_178_TARGET_NO_CREDIT",
        "source": {
            "grf01_contract_blob_sha1": SOURCE_LOCKS[GRF01],
            "grf01_canonical_sha256": EXPECTED_GRF01_CANONICAL,
            "hpadj_picard64_interface_blob_sha1": SOURCE_LOCKS[HANDOFF],
            "pairing_prefix_engine_blob_sha1": SOURCE_LOCKS[PREFIX],
            "picard_bundle_source_blob_sha1": SOURCE_LOCKS[BUNDLE_SOURCE],
            "picard_bundle_canonical_sha256": EXPECTED_BUNDLE_CANONICAL,
        },
        "hermetic_derivation": {
            "external_python_packages_required": [],
            "integer_normal_form_dependency": False,
            "method": "Fraction Gauss-Jordan for B=8*S^-1; invertible row/column diagonalization over Z/8",
            "source_locked_prefix_engine_imported": False,
            "full178_population_materialized": False,
        },
        "fixed_selected64": {
            "assignment_labels_1based": assignment_labels,
            "selected_positions_0based": fixed_positions,
            "free_selected_positions_0based": free_positions,
            "free_coordinate_count": 53,
            "inverse_denominator": den,
            "inverse_integer_matrix_sha256": csha(B),
            "fixed_coefficient_matrix_sha256": csha(Bfixed),
            "free_coefficient_matrix_sha256": csha(Bfree),
        },
        "free_completion_quotient": {
            "ambient": "(Z/8Z)^64 / image(B_free mod 8)",
            "nonzero_diagonal_factors_mod8": diag,
            "nonzero_diagonal_count": pivot_count,
            "unit_pivot_count": sum(d == 1 for d in diag),
            "two_pivot_count": sum(d == 2 for d in diag),
            "four_pivot_count": sum(d == 4 for d in diag),
            "zero_row_count": zero_row_count,
            "nontrivial_invariant_factors": quotient_invariants,
            "order": int(quotient_order),
        },
        "projected_fixed_image": {
            "meaning": "image of the 11 fixed selected64 coordinate directions in the free-completion quotient",
            "nontrivial_invariant_factors": projected_image_invariants,
            "order": int(projected_image_order),
            "kernel_cardinality_in_mod8_fixed_domain": int(kernel_cardinality_mod8),
            "fixed_domain_cardinality": int(8 ** 11),
        },
        "exact_completion_kernel": {
            "theorem": "A fixed x11 extends to some z53 iff every listed modular linear form vanishes.",
            "raw_quotient_component_count": len(raw_components),
            "active_raw_component_count": len(active_raw),
            "primitive_equation_rows": primitive_rows,
            "primitive_equation_rows_sha256": csha(primitive_rows),
        },
        "fixed_coordinate_classes": {
            "equivalence_classes_by_projected_quotient_signature": equivalence_classes,
            "individual_class_orders": {str(k): int(orders[k]) for k in assignment_labels},
            "embedded_signature_stream_sha256": csha(
                {str(k): list(signatures[k]) for k in assignment_labels}
            ),
            "hpadj_group_collapses_to_group_sum": group_sum_collapse,
        },
        "ownership": {
            "main_scope": "fixed symbolic lattice kernel only",
            "concrete_row_or_stratum_selected": False,
            "population_replay_performed": False,
            "bounded_leaf_search_performed": False,
            "exact_subset_certificate_generated": False,
            "concrete_application_owner": "stage32-01-178-mainbatch",
        },
        "credit_firewall": {
            "main_pruning_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    print(json.dumps(body, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
