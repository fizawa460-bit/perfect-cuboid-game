#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass
from itertools import product
from pathlib import Path

COORDS = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
SIGNS = (1, -1)
C1_COUNT = 32
NODE_COUNT = 48
NORMAL_COUNT = 92
ALL140_COUNT = 140

SOURCE_LOCK = {
    "stoll_exact_model": {
        "repo": "MichaelStollBayreuth/Verification",
        "commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "path": "Cuboids/cuboids.magma",
        "blob": "0422b69847f2afb97cb7b3ed02ebef91279f61b1",
        "symbols": ["eqns", "pts", "C1s", "Cpts", "MatCP", "pairingmat"],
    },
    "stoll_testa_geometry": {
        "arxiv": "1009.0388",
        "locator": "Lemma 3 and the paragraph defining b:S->Sbar as the blow-up of the 48 A1 singular points",
    },
    "magma_sequence_iteration": {
        "url": "https://docs.magma-maths.org/SetsSequencesMappings/Sequences/recursion-reduction-iteration.html",
        "locator": "Iteration: with multiple range sequences the first range is the innermost loop",
    },
    "bc2_01a": {
        "path": "stages/stage32-ex5/breadth-cycle-2/bc2-01a-exceptional-pairing-bridge.json",
        "blob": "0a4b6b748bd4f4f94ae70e16cf38a0a2174c55d4",
    },
    "hperp_integral_adapter": {
        "path": "stages/stage32/residual-32-01-production/hperp_integral_adapter.py",
        "blob": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    },
}


@dataclass(frozen=True)
class L:
    """Exact element of Q(i,sqrt(2)) in basis (1,i,s,i*s)."""

    a: int = 0
    b: int = 0
    c: int = 0
    d: int = 0

    def __add__(self, other: object) -> "L":
        o = coerce(other)
        return L(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)

    __radd__ = __add__

    def __neg__(self) -> "L":
        return L(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: object) -> "L":
        return self + (-coerce(other))

    def __rsub__(self, other: object) -> "L":
        return coerce(other) - self

    def __mul__(self, other: object) -> "L":
        o = coerce(other)

        def cmul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
            aa, bb = x
            cc, dd = y
            return aa * cc - bb * dd, aa * dd + bb * cc

        u = (self.a, self.b)
        v = (self.c, self.d)
        U = (o.a, o.b)
        V = (o.c, o.d)
        uu = cmul(u, U)
        vv = cmul(v, V)
        uv = cmul(u, V)
        vu = cmul(v, U)
        return L(
            uu[0] + 2 * vv[0],
            uu[1] + 2 * vv[1],
            uv[0] + vu[0],
            uv[1] + vu[1],
        )

    __rmul__ = __mul__

    def coeffs(self) -> list[int]:
        return [self.a, self.b, self.c, self.d]


def coerce(value: object) -> L:
    if isinstance(value, L):
        return value
    if isinstance(value, int):
        return L(value)
    raise TypeError(value)


ZERO = L()
ONE = L(1)
I = L(0, 1)
S = L(0, 0, 1)


def vec(**terms: object) -> tuple[L, ...]:
    return tuple(coerce(terms.get(name, 0)) for name in COORDS)


def eval_linear(coeffs: tuple[L, ...], point: tuple[L, ...]) -> L:
    total = ZERO
    for coeff, coord in zip(coeffs, point):
        total = total + coeff * coord
    return total


def square(x: L) -> L:
    return x * x


def surface_equations(point: tuple[L, ...]) -> tuple[L, ...]:
    a1, a2, a3, b1, b2, b3, c = point
    return (
        square(a1) + square(a2) - square(b3),
        square(a2) + square(a3) - square(b1),
        square(a1) + square(a3) - square(b2),
        square(a1) + square(a2) + square(a3) - square(c),
    )


def canonical_key(point: tuple[L, ...]) -> tuple[int, ...]:
    # The six explicit node families below are already normalized according to
    # BC2-01 preflight: the first nonzero homogeneous coordinate is exactly 1.
    first = next((x for x in point if x != ZERO), None)
    if first != ONE:
        raise ValueError(f"node is not in canonical first-nonzero=1 scale: {point}")
    return tuple(v for coord in point for v in coord.coeffs())


def node_families() -> list[dict]:
    out: list[dict] = []

    # R_i: singular locus of the rank-three face quadric
    # a_j^2 + a_k^2 - b_i^2 = 0.  The displayed triple vanishes.
    for b2, b3, c in product(SIGNS, repeat=3):
        out.append({"family": "R1", "signs": [b2, b3, c], "point": vec(a1=1, b2=b2, b3=b3, c=c)})
    for b1, b3, c in product(SIGNS, repeat=3):
        out.append({"family": "R2", "signs": [b1, b3, c], "point": vec(a2=1, b1=b1, b3=b3, c=c)})
    for b1, b2, c in product(SIGNS, repeat=3):
        out.append({"family": "R3", "signs": [b1, b2, c], "point": vec(a3=1, b1=b1, b2=b2, c=c)})

    # Q_i: singular locus of a_i^2 + b_i^2 - c^2 = 0.  Here c=a_i=b_i=0.
    for a3i, b2i, b3 in product(SIGNS, repeat=3):
        out.append({"family": "Q1", "signs": [a3i, b2i, b3], "point": vec(a2=1, a3=a3i * I, b2=b2i * I, b3=b3)})
    for a3i, b1i, b3 in product(SIGNS, repeat=3):
        out.append({"family": "Q2", "signs": [a3i, b1i, b3], "point": vec(a1=1, a3=a3i * I, b1=b1i * I, b3=b3)})
    for a2i, b1i, b2 in product(SIGNS, repeat=3):
        out.append({"family": "Q3", "signs": [a2i, b1i, b2], "point": vec(a1=1, a2=a2i * I, b1=b1i * I, b2=b2)})
    return out


def c1_curves() -> list[dict]:
    curves: list[dict] = []

    def add(label: str, equations: list[tuple[L, ...]]) -> None:
        curves.append({"label": label, "equations": equations})

    # Exact Magma sequence-constructor order: with repeated ranges the first
    # range is the innermost loop.  Thus e1 varies fastest in `e1,e2,e3 in`.
    for e3, e2, e1 in product(SIGNS, repeat=3):
        add(
            f"C1A({e1},{e2},{e3})",
            [vec(a1=1), vec(a2=1, b3=e1), vec(a3=1, b2=e2), vec(b1=1, c=e3)],
        )
    for e3, e2, e1 in product(SIGNS, repeat=3):
        add(
            f"C1B({e1},{e2},{e3})",
            [vec(a2=1), vec(a3=1, b1=e1), vec(a1=1, b3=e2), vec(b2=1, c=e3)],
        )
    for e3, e2, e1 in product(SIGNS, repeat=3):
        add(
            f"C1C({e1},{e2},{e3})",
            [vec(a3=1), vec(a1=1, b2=e1), vec(a2=1, b1=e2), vec(b3=1, c=e3)],
        )
    for e1, e2, e3 in product(SIGNS, repeat=3):
        add(
            f"C1D({e1},{e2},{e3})",
            [vec(c=1), vec(a1=I, b1=e1), vec(a2=I, b2=e2), vec(a3=I, b3=e3)],
        )

    if len(curves) != C1_COUNT:
        raise ValueError(f"C1 count regression: {len(curves)}")
    return curves


def incidence_signature(point: tuple[L, ...], curves: list[dict]) -> tuple[int, ...]:
    bits = []
    for curve in curves:
        on = all(eval_linear(eq, point) == ZERO for eq in curve["equations"])
        bits.append(1 if on else 0)
    return tuple(bits)


def singular_triple_is_zero(family: str, point: tuple[L, ...]) -> bool:
    a1, a2, a3, b1, b2, b3, c = point
    triples = {
        "Q1": (a1, b1, c),
        "Q2": (a2, b2, c),
        "Q3": (a3, b3, c),
        "R1": (a2, a3, b1),
        "R2": (a1, a3, b2),
        "R3": (a1, a2, b3),
    }
    return all(v == ZERO for v in triples[family])


def geometry_certificate() -> dict:
    raw_nodes = node_families()
    if len(raw_nodes) != NODE_COUNT:
        raise ValueError(f"node count regression: {len(raw_nodes)}")
    if any(any(eq != ZERO for eq in surface_equations(row["point"])) for row in raw_nodes):
        raise ValueError("explicit node family left the cuboid surface")

    if any(not singular_triple_is_zero(row["family"], row["point"]) for row in raw_nodes):
        raise ValueError("explicit node family does not lie in its rank-three-quadric singular locus")

    keys = [canonical_key(row["point"]) for row in raw_nodes]
    if len(set(keys)) != NODE_COUNT:
        raise ValueError("explicit node families are not projectively distinct after canonicalization")

    curves = c1_curves()
    ordered = sorted(raw_nodes, key=lambda row: canonical_key(row["point"]))
    records = []
    signatures: dict[tuple[int, ...], str] = {}
    for index, row in enumerate(ordered):
        sig = incidence_signature(row["point"], curves)
        if sum(sig) != 4:
            raise ValueError(f"C1 incidence weight regression at sorted node {index}: {sum(sig)}")
        label = f"N{index:02d}"
        if sig in signatures:
            raise ValueError(f"C1 signature collision: {label} and {signatures[sig]}")
        signatures[sig] = label
        records.append(
            {
                "label": label,
                "family": row["family"],
                "family_signs": row["signs"],
                "coordinates_basis_1_i_s_is": [coord.coeffs() for coord in row["point"]],
                "c1_signature_bits": list(sig),
                "c1_incident_labels": [curves[j]["label"] for j, bit in enumerate(sig) if bit],
            }
        )

    if len(signatures) != NODE_COUNT:
        raise ValueError("C1 signatures do not separate all 48 nodes")

    c1_rows = [
        {
            "magma_row_1based": j + 1,
            "label": curve["label"],
        }
        for j, curve in enumerate(curves)
    ]
    digest_payload = json.dumps(records, sort_keys=True, separators=(",", ":"))
    return {
        "canonical_node_count": NODE_COUNT,
        "canonical_node_labels": [row["label"] for row in records],
        "canonical_nodes": records,
        "canonical_nodes_sha256": hashlib.sha256(digest_payload.encode()).hexdigest(),
        "c1_count": C1_COUNT,
        "c1_rows": c1_rows,
        "c1_signature_weight_all_nodes": 4,
        "c1_signature_unique_count": len(signatures),
        "c1_signature_bijection": True,
    }


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained loader {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    payload = module.load()
    if not isinstance(payload, dict):
        raise ValueError(f"retained loader did not return dict: {path}")
    return payload


def runtime_replay(repo_root: Path, geometry: dict) -> dict:
    hdir = repo_root / "stages/stage32/residual-32-01-production"
    retained_path = repo_root / "stages/stage33/33-07/picard_base_rows_retained.py"
    marking_path = repo_root / "stages/stage33/33-07/stage32_picard_marking_retained.py"
    if str(hdir) not in sys.path:
        sys.path.insert(0, str(hdir))
    from hperp_integral_adapter import HperpIntegralPairingAdapter  # type: ignore
    from sympy import Matrix

    bundle = load_retained(retained_path, "s32ex5_g_picard_rows")
    marking = load_retained(marking_path, "s32ex5_g_picard_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    coords = adapter.class_coordinates_in_retained_basis
    full = coords * gram * coords.T
    if full.shape != (ALL140_COUNT, ALL140_COUNT):
        raise ValueError(f"all140 pairing shape regression: {full.shape}")
    diag = [int(full[j, j]) for j in range(ALL140_COUNT)]
    if diag[:NORMAL_COUNT] != [-4] * NORMAL_COUNT or diag[NORMAL_COUNT:] != [-2] * NODE_COUNT:
        raise ValueError("normal/exceptional self-intersection split regression")

    sig_to_node = {
        tuple(int(v) for v in row["c1_signature_bits"]): row
        for row in geometry["canonical_nodes"]
    }
    mappings = []
    observed = []
    for k in range(NODE_COUNT):
        all140 = NORMAL_COUNT + k
        sig = tuple(int(full[j, all140]) for j in range(C1_COUNT))
        if any(bit not in (0, 1) for bit in sig):
            raise ValueError(f"non-01 C1/exceptional pairing at exceptional offset {k}: {sig}")
        if sum(sig) != 4:
            raise ValueError(f"runtime C1 incidence weight regression at exceptional offset {k}: {sum(sig)}")
        node = sig_to_node.get(sig)
        if node is None:
            raise ValueError(f"runtime exceptional signature has no geometric node match at offset {k}")
        observed.append(node["label"])
        mappings.append(
            {
                "runtime_exceptional_offset_0based": k,
                "all140_index_0based": all140,
                "all140_label_1based": all140 + 1,
                "canonical_node_label": node["label"],
                "coordinates_basis_1_i_s_is": node["coordinates_basis_1_i_s_is"],
                "c1_signature_bits": list(sig),
            }
        )
    if len(set(observed)) != NODE_COUNT or set(observed) != set(geometry["canonical_node_labels"]):
        raise ValueError("runtime exceptional signatures are not a 48/48 bijection onto canonical nodes")

    return {
        "runtime_exceptional_count": NODE_COUNT,
        "runtime_signature_match_count": len(mappings),
        "runtime_to_canonical_bijection": True,
        "points_iteration_order_used_for_identification": False,
        "mapping": mappings,
        "hperp_adapter_certificate_sha256": adapter.certificate["canonical_sha256_without_this_field"],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, default=None)
    ap.add_argument("--geometry-only", action="store_true")
    ap.add_argument("--output", type=Path, default=None)
    args = ap.parse_args()

    geometry = geometry_certificate()
    cert = {
        "schema": "STAGE32EX5_G_GEOMETRIC_EXCEPTIONAL_TO_NODE_REVERSE_ADAPTER_V1",
        "source_lock": SOURCE_LOCK,
        "field_basis": ["1", "i", "s", "i*s"],
        "projective_canonicalization": "first nonzero homogeneous coordinate normalized to 1; flatten exact Q-coefficients in basis (1,i,s,i*s); lexicographically sort to N00..N47",
        "geometry": geometry,
        "adapter_rule": "for an exceptional divisor E, form the 32-vector (C1_j . E) in exact Stoll C1 order; it is the incidence vector of the blow-up center p=b(E), and the 48 canonical nodes have pairwise distinct such vectors",
        "runtime": None,
        "firewalls": {
            "raw_Points_iteration_index_used_as_node_identity": False,
            "numeric_exceptional_slot_alone_used_as_node_identity": False,
            "FULL178_span_replay_performed": False,
            "stage32_main_credit": False,
            "receiver_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
        },
    }

    if not args.geometry_only:
        repo_root = args.repo_root
        if repo_root is None:
            here = Path(__file__).resolve()
            # Intended repository location: stages/stage32-ex5/parallel/lane-g/<this file>
            repo_root = here.parents[4] if len(here.parents) > 4 else None
        if repo_root is None:
            raise ValueError("--repo-root is required outside the repository layout")
        cert["runtime"] = runtime_replay(repo_root.resolve(), geometry)

    canonical = json.dumps(cert, sort_keys=True, separators=(",", ":"))
    cert["canonical_sha256_without_this_field"] = hashlib.sha256(canonical.encode()).hexdigest()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
