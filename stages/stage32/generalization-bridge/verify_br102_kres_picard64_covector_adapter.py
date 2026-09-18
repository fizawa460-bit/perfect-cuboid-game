#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(BUNDLE_DIR))

from pairing_prefix_engine import (  # noqa: E402
    CURVE_BASIS_POSITIONS,
    EXCEPTIONAL_BASIS_POSITIONS,
    INDLIST,
)
import picard_base_rows_retained as retained_base  # noqa: E402
import stage32_picard_marking_retained as retained_marking  # noqa: E402

SCHEMA = "STAGE32_BRIDGE_BR102_KRES_PICARD64_COVECTOR_ADAPTER_V2"
PAIRING_PREFIX = RESIDUAL / "pairing_prefix_engine.py"
BASE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"
STAGE33_RECONSTRUCTOR = BUNDLE_DIR / "certify_two_coordinate_swap_picard_rows.py"
SOURCE_LOCKS = {
    "pairing_prefix_engine_blob_sha1": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    "picard_base_rows_retained_blob_sha1": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    "stage33_known_class_reconstructor_blob_sha1": "296e2005f822ae89c1aa085161553fe9ef76d077",
    "picard_base_bundle_canonical_sha256": "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c",
    "stage32_picard_core_sha256": "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870",
    "upstream_git_blob_sha1": "0422b69847f2afb97cb7b3ed02ebef91279f61b1",
}
MAGIC = "S32_D16_AUT_CANON_HPERP_V1"
RANK = 64
HPERP_RANK = 63
KNOWN_COUNT = 140
CURVE_COUNT = 92
FIXED_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
KRES_TERMS = {24: -1, 25: 1, 26: -1, 27: 1, 32: -1, 33: 1, 34: -1, 35: 1}


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def parse_hperp(text: str) -> dict:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) != 5 + HPERP_RANK + KNOWN_COUNT:
        raise SystemExit(f"retained Hperp line-count regression: {len(lines)}")
    if lines[0] != MAGIC:
        raise SystemExit("retained Hperp magic moved")
    if lines[1] != SOURCE_LOCKS["stage32_picard_core_sha256"]:
        raise SystemExit("retained Hperp core lock moved")
    if lines[2] != SOURCE_LOCKS["upstream_git_blob_sha1"]:
        raise SystemExit("retained Hperp upstream source lock moved")
    prepared_sha = lines[3]
    r, m = map(int, lines[4].split())
    if (r, m) != (HPERP_RANK, KNOWN_COUNT):
        raise SystemExit("retained Hperp shape regression")
    q = [list(map(int, lines[5 + i].split())) for i in range(HPERP_RANK)]
    if any(len(row) != HPERP_RANK for row in q):
        raise SystemExit("retained Hperp Gram width regression")
    p0, caps, lin = [], [], []
    off = 5 + HPERP_RANK
    for i in range(KNOWN_COUNT):
        row = list(map(int, lines[off + i].split()))
        if len(row) != 2 + HPERP_RANK:
            raise SystemExit(f"retained Hperp class-row width regression at {i + 1}")
        p0.append(row[0])
        caps.append(row[1])
        lin.append(row[2:])
    payload = {
        "core_sha": SOURCE_LOCKS["stage32_picard_core_sha256"],
        "source_blob": SOURCE_LOCKS["upstream_git_blob_sha1"],
        "q": q,
        "p0": p0,
        "caps": caps,
        "lin": lin,
    }
    if csha(payload) != prepared_sha:
        raise SystemExit("retained Hperp prepared-input hash regression")
    return {
        "prepared_sha": prepared_sha,
        "q": q,
        "p0": p0,
        "pairing_rows": [[p0[i]] + lin[i] for i in range(KNOWN_COUNT)],
    }


def invert_matrix(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise SystemExit("attempted to invert a non-square matrix")
    m = [
        [Fraction(x) for x in a[i]]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col]), None)
        if pivot is None:
            raise SystemExit("exact marking matrix is singular")
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]
        m[col] = [x / p for x in m[col]]
        for r in range(n):
            if r == col:
                continue
            f = m[r][col]
            if f:
                m[r] = [m[r][j] - f * m[col][j] for j in range(2 * n)]
    return [row[n:] for row in m]


def row_times_fraction_matrix(
    row: list[int], matrix: list[list[Fraction]]
) -> list[Fraction]:
    return [
        sum(Fraction(row[k]) * matrix[k][j] for k in range(len(row)))
        for j in range(len(matrix[0]))
    ]


def integral_row(row: list[Fraction], label: str) -> list[int]:
    if any(x.denominator != 1 for x in row):
        bad = next(x for x in row if x.denominator != 1)
        raise SystemExit(f"non-integral recovered Picard coordinate in {label}: {bad}")
    return [int(x) for x in row]


def intersection_from_marking(
    a: list[int], b: list[int], qinv: list[list[Fraction]]
) -> Fraction:
    hpart = Fraction(a[0] * b[0], 16)
    lin_a, lin_b = a[1:], b[1:]
    perp = sum(
        Fraction(lin_a[i]) * qinv[i][j] * Fraction(lin_b[j])
        for i in range(HPERP_RANK)
        for j in range(HPERP_RANK)
    )
    return hpart - perp


def pairing(u: list[int], v: list[int], gram: list[list[int]]) -> int:
    return sum(
        u[i] * gram[i][j] * v[j]
        for i in range(RANK)
        for j in range(RANK)
    )


def dot_basis(u: list[int], basis_index: int, gram: list[list[int]]) -> int:
    return sum(u[i] * gram[i][basis_index] for i in range(RANK))


G = tuple[int, int]
ZERO: G = (0, 0)
ONE: G = (1, 0)
II: G = (0, 1)
Coeff = tuple[G, G]
R1: Coeff = (ONE, ZERO)
RI: Coeff = (II, ZERO)
S1: Coeff = (ZERO, ONE)
SI: Coeff = (ZERO, II)


def gadd(a: G, b: G) -> G:
    return (a[0] + b[0], a[1] + b[1])


def gscale(a: G, q: int) -> G:
    return (q * a[0], q * a[1])


def gmul(a: G, b: G) -> G:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cscale(c: Coeff, q: int) -> Coeff:
    return (gscale(c[0], q), gscale(c[1], q))


def form(*terms: tuple[Coeff, int]) -> list[tuple[Coeff, int]]:
    return list(terms)


def eval_form(node: tuple[G, ...], terms: list[tuple[Coeff, int]]) -> tuple[G, G]:
    a = ZERO
    b = ZERO
    for coeff, pos in terms:
        z = node[pos]
        a = gadd(a, gmul(coeff[0], z))
        b = gadd(b, gmul(coeff[1], z))
    return a, b


def node_model() -> list[tuple[G, ...]]:
    out: list[tuple[G, ...]] = []
    for j in range(3):
        for sa, s1, s2 in product((1, -1), repeat=3):
            z = [ZERO] * 7
            z[j] = (sa, 0)
            other = [t for t in range(3) if t != j]
            z[3 + other[0]] = (s1, 0)
            z[3 + other[1]] = (s2, 0)
            z[6] = ONE
            out.append(tuple(z))
    for j in range(3):
        other = [t for t in range(3) if t != j]
        a, b = other
        for sr, ep, eq in product((1, -1), repeat=3):
            z = [ZERO] * 7
            z[a] = ONE
            z[b] = (0, sr)
            z[3 + a] = (0, ep)
            z[3 + b] = (-eq * sr, 0)
            out.append(tuple(z))
    if len(out) != 48:
        raise SystemExit("MB104 node model cardinality regression")
    return out


def source_curves() -> list[list[list[tuple[Coeff, int]]]]:
    curves: list[list[list[tuple[Coeff, int]]]] = []

    def add(eqs: list[list[tuple[Coeff, int]]]) -> None:
        curves.append(eqs)

    def r(q: int, pos: int) -> tuple[Coeff, int]:
        return cscale(R1, q), pos

    def im(q: int, pos: int) -> tuple[Coeff, int]:
        return cscale(RI, q), pos

    def sq(q: int, pos: int) -> tuple[Coeff, int]:
        return cscale(S1, q), pos

    def isq(q: int, pos: int) -> tuple[Coeff, int]:
        return cscale(SI, q), pos

    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1, 0)), form(r(1, 1), r(e1, 5)), form(r(1, 2), r(e2, 4)), form(r(1, 3), r(e3, 6))])
    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1, 1)), form(r(1, 2), r(e1, 3)), form(r(1, 0), r(e2, 5)), form(r(1, 4), r(e3, 6))])
    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1, 2)), form(r(1, 0), r(e1, 4)), form(r(1, 1), r(e2, 3)), form(r(1, 5), r(e3, 6))])
    for e3, e2, e1 in product((1, -1), repeat=3):
        add([form(r(1, 6)), form(im(1, 0), r(e1, 3)), form(im(1, 1), r(e2, 4)), form(im(1, 2), r(e3, 5))])
    if len(curves) != 32:
        raise SystemExit("C1 curve count regression")

    for e1, e2 in product((1, -1), repeat=2):
        add([form(r(1, 3)), form(im(1, 1), r(e1, 2)), form(r(1, 0), r(e2, 6))])
    for e1, e2 in product((1, -1), repeat=2):
        add([form(r(1, 4)), form(im(1, 2), r(e1, 0)), form(r(1, 1), r(e2, 6))])
    for e1, e2 in product((1, -1), repeat=2):
        add([form(r(1, 5)), form(im(1, 0), r(e1, 1)), form(r(1, 2), r(e2, 6))])
    if len(curves) != 44:
        raise SystemExit("C2 curve count regression")

    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1, 0), r(e1, 1)), form(sq(1, 0), r(e2, 5)), form(r(1, 3), r(e3, 4))])
    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1, 1), r(e1, 2)), form(sq(1, 1), r(e2, 3)), form(r(1, 4), r(e3, 5))])
    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1, 2), r(e1, 0)), form(sq(1, 2), r(e2, 4)), form(r(1, 5), r(e3, 3))])
    for e3, e2, e1 in product((1, -1), repeat=3):
        add([form(im(1, 0), r(e1, 6)), form(im(1, 4), r(e2, 5)), form(isq(1, 0), r(e3, 3))])
    for e3, e2, e1 in product((1, -1), repeat=3):
        add([form(im(1, 1), r(e1, 6)), form(im(1, 5), r(e2, 3)), form(isq(1, 1), r(e3, 4))])
    for e3, e2, e1 in product((1, -1), repeat=3):
        add([form(im(1, 2), r(e1, 6)), form(im(1, 3), r(e2, 4)), form(isq(1, 2), r(e3, 5))])
    if len(curves) != CURVE_COUNT:
        raise SystemExit("C3/all curve count regression")
    return curves


def on_curve(node: tuple[G, ...], curve: list[list[tuple[Coeff, int]]]) -> int:
    return int(all(eval_form(node, eq) == (ZERO, ZERO) for eq in curve))


def main() -> int:
    for path, key in [
        (PAIRING_PREFIX, "pairing_prefix_engine_blob_sha1"),
        (BASE_SOURCE, "picard_base_rows_retained_blob_sha1"),
        (STAGE33_RECONSTRUCTOR, "stage33_known_class_reconstructor_blob_sha1"),
    ]:
        if git_blob(path) != SOURCE_LOCKS[key]:
            raise SystemExit(f"source-lock drift: {path.relative_to(ROOT)}")

    base = retained_base.load()
    marking = retained_marking.load()
    if base["canonical_sha256"] != SOURCE_LOCKS["picard_base_bundle_canonical_sha256"]:
        raise SystemExit("retained Picard-base canonical drift")
    if base["upstream_git_blob_sha1"] != SOURCE_LOCKS["upstream_git_blob_sha1"]:
        raise SystemExit("retained Picard-base upstream source moved")
    if marking["stage32_picard_core_sha256"] != SOURCE_LOCKS["stage32_picard_core_sha256"]:
        raise SystemExit("retained Stage32 Picard core moved")

    parsed = parse_hperp(marking["hperp_text"])
    pairing_rows = parsed["pairing_rows"]
    basis_pairing = [pairing_rows[j - 1] for j in INDLIST]
    basis_pairing_inv = invert_matrix(basis_pairing)
    known = [
        integral_row(
            row_times_fraction_matrix(row, basis_pairing_inv),
            f"known class {i + 1}",
        )
        for i, row in enumerate(pairing_rows)
    ]
    for k, j in enumerate(INDLIST):
        expected = [0] * RANK
        expected[k] = 1
        if known[j - 1] != expected:
            raise SystemExit(f"INDLIST class {j} failed primitive-basis reconstruction")

    qinv = invert_matrix(parsed["q"])
    gram_f = [
        [
            intersection_from_marking(pairing_rows[i - 1], pairing_rows[j - 1], qinv)
            for j in INDLIST
        ]
        for i in INDLIST
    ]
    if any(x.denominator != 1 for row in gram_f for x in row):
        bad = next(x for row in gram_f for x in row if x.denominator != 1)
        raise SystemExit(f"reconstructed INDLIST Gram is not integral: {bad}")
    gram = [[int(x) for x in row] for row in gram_f]
    if gram != [list(row) for row in zip(*gram)]:
        raise SystemExit("reconstructed INDLIST Gram is not symmetric")

    nodes = node_model()
    curves = source_curves()
    node_fp = {
        i: tuple(on_curve(node, curves[curve_label - 1]) for curve_label in range(1, CURVE_COUNT + 1))
        for i, node in enumerate(nodes)
    }
    retained_fp = {
        label: tuple(
            pairing(known[label - 1], known[curve_label - 1], gram)
            for curve_label in range(1, CURVE_COUNT + 1)
        )
        for label in range(CURVE_COUNT + 1, KNOWN_COUNT + 1)
    }
    if any(v not in (0, 1) for fp in retained_fp.values() for v in fp):
        raise SystemExit("retained exceptional/curve incidence is not 0/1")

    label_to_node: dict[int, int] = {}
    for label, fp in retained_fp.items():
        matches = [i for i, candidate in node_fp.items() if candidate == fp]
        if len(matches) != 1:
            ranked = sorted(
                (
                    sum(int(a != b) for a, b in zip(fp, candidate)),
                    i,
                    [j + 1 for j, value in enumerate(candidate) if value],
                )
                for i, candidate in node_fp.items()
            )[:8]
            diag = {
                "label": label,
                "retained_incident_curves": [j + 1 for j, value in enumerate(fp) if value],
                "exact_matches": matches,
                "closest_nodes": [
                    {"hamming": h, "node": i, "node_incident_curves": labels}
                    for h, i, labels in ranked
                ],
            }
            raise SystemExit(
                "exceptional fingerprint mismatch diagnostic="
                + json.dumps(diag, sort_keys=True, separators=(",", ":"))
            )
        label_to_node[label] = matches[0]
    if len(label_to_node) != 48 or len(set(label_to_node.values())) != 48:
        raise SystemExit("exceptional fingerprint matching is not bijective")
    node_to_label = {node: label for label, node in label_to_node.items()}

    xk = [0] * RANK
    relevant_map: dict[str, int] = {}
    for node_index, sign in KRES_TERMS.items():
        label = node_to_label[node_index]
        relevant_map[str(node_index)] = label
        row = known[label - 1]
        xk = [a + sign * b for a, b in zip(xk, row)]
    k2 = pairing(xk, xk, gram)
    if k2 != -16:
        raise SystemExit(f"K_res square mismatch: {k2} != -16")

    order = EXCEPTIONAL_BASIS_POSITIONS + CURVE_BASIS_POSITIONS
    selected_labels = [INDLIST[p] for p in order]
    selected_pairings = [dot_basis(xk, p, gram) for p in order]
    ell_selected = [xk[p] for p in order]
    fixed_set = set(FIXED_LABELS)
    fixed_support = {
        str(label): coeff
        for label, coeff in zip(selected_labels, ell_selected)
        if label in fixed_set and coeff
    }
    free_support = {
        str(label): coeff
        for label, coeff in zip(selected_labels, ell_selected)
        if label not in fixed_set and coeff
    }

    result = {
        "schema": SCHEMA,
        "status": "EXACT_REPLAY_PASS_NO_CREDIT",
        "source_locks": SOURCE_LOCKS,
        "prepared_hperp_input_sha256": parsed["prepared_sha"],
        "exceptional_fingerprint_bijection_count": len(label_to_node),
        "exceptional_fingerprint_bijection_sha256": csha(label_to_node),
        "relevant_mb104_node_to_known_class": relevant_map,
        "kres_terms": {str(k): v for k, v in sorted(KRES_TERMS.items())},
        "kres_primitive_indlist_coordinates": xk,
        "kres_selected_pairings": selected_pairings,
        "kres_square": k2,
        "ell_selected_pairing_coefficients": ell_selected,
        "ell_fixed_nonzero": fixed_support,
        "ell_free_nonzero": free_support,
        "terminal_visible_on_hpadj_interface": not free_support,
        "next_route": "BR102_TERMINAL_VISIBLE" if not free_support else "BR103_FREE_COMPLETION_CANCELLATION",
        "firewall": {
            "stage32_main_pruning_credit": False,
            "population_wide_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
