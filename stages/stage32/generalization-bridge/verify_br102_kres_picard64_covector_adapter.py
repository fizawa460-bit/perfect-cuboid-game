#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from itertools import product
from pathlib import Path

from sympy import Matrix

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
    RetainedBasisPairingTransform,
)
import picard_base_rows_retained as retained_bundle  # noqa: E402

SCHEMA = "STAGE32_BRIDGE_BR102_KRES_PICARD64_COVECTOR_ADAPTER_V1"
PAIRING_PREFIX = RESIDUAL / "pairing_prefix_engine.py"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"
SOURCE_LOCKS = {
    "pairing_prefix_engine_blob_sha1": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    "picard_bundle_source_blob_sha1": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    "picard_bundle_canonical_sha256": "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c",
}
FIXED_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
KRES_TERMS = {24: -1, 25: 1, 26: -1, 27: 1, 32: -1, 33: 1, 34: -1, 35: 1}

G = tuple[int, int]
ZERO: G = (0, 0)
ONE: G = (1, 0)
II: G = (0, 1)


def gadd(a: G, b: G) -> G:
    return (a[0] + b[0], a[1] + b[1])


def gscale(a: G, q: int) -> G:
    return (q * a[0], q * a[1])


def gmul(a: G, b: G) -> G:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


Coeff = tuple[G, G]
R1: Coeff = (ONE, ZERO)
RI: Coeff = (II, ZERO)
S1: Coeff = (ZERO, ONE)
SI: Coeff = (ZERO, II)


def cscale(c: Coeff, q: int) -> Coeff:
    return (gscale(c[0], q), gscale(c[1], q))


def eval_form(node: tuple[G, ...], terms: list[tuple[Coeff, int]]) -> tuple[G, G]:
    a = ZERO
    b = ZERO
    for coeff, pos in terms:
        z = node[pos]
        a = gadd(a, gmul(coeff[0], z))
        b = gadd(b, gmul(coeff[1], z))
    return a, b


def form(*terms: tuple[Coeff, int]) -> list[tuple[Coeff, int]]:
    return list(terms)


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
    assert len(out) == 48
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
        add([form(r(1,0)), form(r(1,1),r(e1,5)), form(r(1,2),r(e2,4)), form(r(1,3),r(e3,6))])
    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1,1)), form(r(1,2),r(e1,3)), form(r(1,0),r(e2,5)), form(r(1,4),r(e3,6))])
    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1,2)), form(r(1,0),r(e1,4)), form(r(1,1),r(e2,3)), form(r(1,5),r(e3,6))])
    for e3, e2, e1 in product((1, -1), repeat=3):
        add([form(r(1,6)), form(im(1,0),r(e1,3)), form(im(1,1),r(e2,4)), form(im(1,2),r(e3,5))])
    assert len(curves) == 32

    for e1, e2 in product((1, -1), repeat=2):
        add([form(r(1,3)), form(im(1,1),r(e1,2)), form(r(1,0),r(e2,6))])
    for e1, e2 in product((1, -1), repeat=2):
        add([form(r(1,4)), form(im(1,2),r(e1,0)), form(r(1,1),r(e2,6))])
    for e1, e2 in product((1, -1), repeat=2):
        add([form(r(1,5)), form(im(1,0),r(e1,1)), form(r(1,2),r(e2,6))])
    assert len(curves) == 44

    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1,0),r(e1,1)), form(sq(1,0),r(e2,5)), form(r(1,3),r(e3,4))])
    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1,1),r(e1,2)), form(sq(1,1),r(e2,3)), form(r(1,4),r(e3,5))])
    for e1, e2, e3 in product((1, -1), repeat=3):
        add([form(r(1,2),r(e1,0)), form(sq(1,2),r(e2,4)), form(r(1,5),r(e3,3))])
    for e3, e2, e1 in product((1, -1), repeat=3):
        add([form(im(1,0),r(e1,6)), form(im(1,4),r(e2,5)), form(isq(1,0),r(e3,3))])
    for e3, e2, e1 in product((1, -1), repeat=3):
        add([form(im(1,1),r(e1,6)), form(im(1,5),r(e2,3)), form(isq(1,1),r(e3,4))])
    for e3, e2, e1 in product((1, -1), repeat=3):
        add([form(im(1,2),r(e1,6)), form(im(1,3),r(e2,4)), form(isq(1,2),r(e3,5))])
    assert len(curves) == 92
    return curves


def on_curve(node: tuple[G, ...], curve: list[list[tuple[Coeff, int]]]) -> int:
    return int(all(eval_form(node, eq) == (ZERO, ZERO) for eq in curve))


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def nonzero_labels(fp: tuple[int, ...], curve_labels: list[int]) -> list[int]:
    return [label for label, value in zip(curve_labels, fp) if value]


def main() -> int:
    if git_blob(PAIRING_PREFIX) != SOURCE_LOCKS["pairing_prefix_engine_blob_sha1"]:
        raise SystemExit("pairing_prefix_engine source-lock drift")
    if git_blob(BUNDLE_SOURCE) != SOURCE_LOCKS["picard_bundle_source_blob_sha1"]:
        raise SystemExit("retained Picard bundle source-lock drift")

    bundle = retained_bundle.load()
    if bundle["canonical_sha256"] != SOURCE_LOCKS["picard_bundle_canonical_sha256"]:
        raise SystemExit("retained Picard bundle canonical drift")
    gram = Matrix(bundle["picard_gram_64x64"])
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    nodes = node_model()
    curves = source_curves()
    curve_labels = [INDLIST[p] for p in CURVE_BASIS_POSITIONS]
    exceptional_labels = [INDLIST[p] for p in EXCEPTIONAL_BASIS_POSITIONS]

    node_fp = {
        i: tuple(on_curve(node, curves[label - 1]) for label in curve_labels)
        for i, node in enumerate(nodes)
    }
    retained_fp = {
        label: tuple(int(gram[p, q]) for q in CURVE_BASIS_POSITIONS)
        for label, p in zip(exceptional_labels, EXCEPTIONAL_BASIS_POSITIONS)
    }

    label_to_node: dict[int, int] = {}
    for label, fp in retained_fp.items():
        matches = [i for i, candidate in node_fp.items() if candidate == fp]
        if len(matches) != 1:
            ranked = sorted(
                (
                    sum(int(a != b) for a, b in zip(fp, candidate)),
                    i,
                    nonzero_labels(candidate, curve_labels),
                )
                for i, candidate in node_fp.items()
            )[:8]
            diag = {
                "label": label,
                "retained_nonzero_curve_labels": nonzero_labels(fp, curve_labels),
                "retained_values": {str(cl): int(v) for cl, v in zip(curve_labels, fp) if v},
                "exact_matches": matches,
                "closest_nodes": [
                    {"hamming": h, "node": i, "node_nonzero_curve_labels": labels}
                    for h, i, labels in ranked
                ],
            }
            raise SystemExit("exceptional fingerprint mismatch diagnostic=" + json.dumps(diag, sort_keys=True, separators=(",", ":")))
        label_to_node[label] = matches[0]
    if len(set(label_to_node.values())) != len(label_to_node):
        raise SystemExit("retained exceptional fingerprint matching is not injective")
    node_to_label = {node: label for label, node in label_to_node.items()}

    selected_labels = transform.certificate["selected_known_indices_1based"]
    selected_exceptional_labels = selected_labels[:29]
    selected_curve_labels = selected_labels[29:]
    assert selected_exceptional_labels == exceptional_labels
    assert selected_curve_labels == curve_labels

    def exceptional_selected_pairings(node_index: int) -> list[int]:
        vals = []
        own = node_to_label.get(node_index)
        for label in selected_exceptional_labels:
            vals.append(-2 if label == own else 0)
        vals.extend(node_fp[node_index])
        return vals

    yk = [0] * 64
    for node_index, sign in KRES_TERMS.items():
        y = exceptional_selected_pairings(node_index)
        yk = [a + sign * b for a, b in zip(yk, y)]
    xk = transform.reconstruct_picard_basis(yk)
    k2 = int((Matrix(xk).T * gram * Matrix(xk))[0])
    if k2 != -16:
        raise SystemExit(f"K_res square mismatch: {k2} != -16")

    order = EXCEPTIONAL_BASIS_POSITIONS + CURVE_BASIS_POSITIONS
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
        "retained_exceptional_to_mb104_node": {str(k): v for k, v in sorted(label_to_node.items())},
        "kres_terms": {str(k): v for k, v in sorted(KRES_TERMS.items())},
        "kres_selected_pairings": yk,
        "kres_primitive_picard64": xk,
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
