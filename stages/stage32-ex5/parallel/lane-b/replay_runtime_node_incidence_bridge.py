#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

# Exact coefficient ring Z[i,s]/(i^2+1,s^2-2), represented as
# a + b*i + c*s + d*i*s.  All source-side node/curve checks below stay in
# this ring; no floating-point arithmetic is used.
F = tuple[int, int, int, int]
ZERO: F = (0, 0, 0, 0)
ONE: F = (1, 0, 0, 0)
NEG_ONE: F = (-1, 0, 0, 0)
I: F = (0, 1, 0, 0)
S: F = (0, 0, 1, 0)
IS: F = (0, 0, 0, 1)

STOLL_REPOSITORY = "MichaelStollBayreuth/Verification"
STOLL_COMMIT = "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
STOLL_PATH = "Cuboids/cuboids.magma"
EXPECTED_CURVES = 92
EXPECTED_NODES = 48
EXPECTED_ALL140 = 140
EXPECTED_INCIDENCE_WEIGHT = 10
EXPECTED_HPERP_SHA256 = "af373f16d6ab2bb8aed6ca09e0a15c8b28d565cbec6f242a8b76c590df81bb4f"


def add(x: F, y: F) -> F:
    return tuple(x[j] + y[j] for j in range(4))  # type: ignore[return-value]


def neg(x: F) -> F:
    return tuple(-v for v in x)  # type: ignore[return-value]


def scale(n: int, x: F) -> F:
    return tuple(n * v for v in x)  # type: ignore[return-value]


def mul(x: F, y: F) -> F:
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e - b * f + 2 * c * g - 2 * d * h,
        a * f + b * e + 2 * c * h + 2 * d * g,
        a * g - b * h + c * e - d * f,
        a * h + b * g + c * f + d * e,
    )


def fsum(values: list[F] | tuple[F, ...]) -> F:
    out = ZERO
    for value in values:
        out = add(out, value)
    return out


def sq(x: F) -> F:
    return mul(x, x)


def linear(*terms: tuple[F, int]) -> tuple[F, ...]:
    coeffs = [ZERO for _ in range(7)]
    for coeff, var in terms:
        coeffs[var] = add(coeffs[var], coeff)
    return tuple(coeffs)


def evaluate_linear(coeffs: tuple[F, ...], point: tuple[F, ...]) -> F:
    return fsum([mul(coeffs[j], point[j]) for j in range(7)])


def determinant(matrix: list[list[F]]) -> F:
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    out = ZERO
    for j in range(n):
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        term = mul(matrix[0][j], determinant(minor))
        out = add(out, term if j % 2 == 0 else neg(term))
    return out


def normalize_sort_key(point: tuple[F, ...]) -> tuple[int, ...]:
    return tuple(v for coord in point for v in coord)


def verify_surface_and_singularity(point: tuple[F, ...]) -> None:
    a1, a2, a3, b1, b2, b3, c = point
    equations = [
        add(add(sq(a1), sq(a2)), neg(sq(b3))),
        add(add(sq(a2), sq(a3)), neg(sq(b1))),
        add(add(sq(a1), sq(a3)), neg(sq(b2))),
        add(add(add(sq(a1), sq(a2)), sq(a3)), neg(sq(c))),
    ]
    if any(v != ZERO for v in equations):
        raise ValueError(f"generated point misses Stoll surface: {point}")

    two = lambda x: scale(2, x)
    jac = [
        [two(a1), two(a2), ZERO, ZERO, ZERO, neg(two(b3)), ZERO],
        [ZERO, two(a2), two(a3), neg(two(b1)), ZERO, ZERO, ZERO],
        [two(a1), ZERO, two(a3), ZERO, neg(two(b2)), ZERO, ZERO],
        [two(a1), two(a2), two(a3), ZERO, ZERO, ZERO, neg(two(c))],
    ]
    for cols in itertools.combinations(range(7), 4):
        minor = [[jac[r][j] for j in cols] for r in range(4)]
        if determinant(minor) != ZERO:
            raise ValueError(f"generated point is nonsingular: {point}; cols={cols}")


def sqrt_square_unit(x: F) -> F:
    if x == ZERO:
        return ZERO
    if x == ONE:
        return ONE
    if x == NEG_ONE:
        return I
    raise ValueError(f"unexpected node square value {x}")


def generate_canonical_nodes() -> list[tuple[F, ...]]:
    nodes: set[tuple[F, ...]] = set()

    # Type A: exactly one a-coordinate is 1.  The two forced nonzero b's and
    # c are independently signed.  The first nonzero projective coordinate is
    # therefore already normalized to 1.
    nonzero_b = {0: (4, 5), 1: (3, 5), 2: (3, 4)}
    for a_index in range(3):
        for sb0, sb1, sc in itertools.product((1, -1), repeat=3):
            p = [ZERO for _ in range(7)]
            p[a_index] = ONE
            bj0, bj1 = nonzero_b[a_index]
            p[bj0] = scale(sb0, ONE)
            p[bj1] = scale(sb1, ONE)
            p[6] = scale(sc, ONE)
            nodes.add(tuple(p))

    # Type B: one a-coordinate is zero and the other two have ratio +/- i;
    # c=0.  The two nonzero b-coordinates are independent square-root signs.
    for zero_a in range(3):
        others = [j for j in range(3) if j != zero_a]
        pidx, qidx = others
        for ratio_sign in (1, -1):
            a = [ZERO, ZERO, ZERO]
            a[pidx] = ONE
            a[qidx] = scale(ratio_sign, I)
            bsquares = [
                add(sq(a[1]), sq(a[2])),
                add(sq(a[0]), sq(a[2])),
                add(sq(a[0]), sq(a[1])),
            ]
            roots = [sqrt_square_unit(v) for v in bsquares]
            nz = [j for j, root in enumerate(roots) if root != ZERO]
            if len(nz) != 2:
                raise ValueError("type-B node did not produce exactly two nonzero b roots")
            for signs in itertools.product((1, -1), repeat=2):
                b = [ZERO, ZERO, ZERO]
                for pos, j in enumerate(nz):
                    b[j] = scale(signs[pos], roots[j])
                nodes.add(tuple(a + b + [ZERO]))

    ordered = sorted(nodes, key=normalize_sort_key)
    if len(ordered) != EXPECTED_NODES:
        raise ValueError(f"canonical node count regression: {len(ordered)}")
    for point in ordered:
        # All generated representatives are normalized by first nonzero = 1.
        first = next(coord for coord in point if coord != ZERO)
        if first != ONE:
            raise ValueError(f"projective normalization regression: {point}")
        verify_surface_and_singularity(point)
    return ordered


def sign_environments(names: tuple[str, ...], convention: str):
    if convention == "LEFTMOST_OUTERMOST":
        loop_names = names
    elif convention == "LEFTMOST_INNERMOST":
        loop_names = tuple(reversed(names))
    else:
        raise ValueError(convention)
    for values in itertools.product((1, -1), repeat=len(loop_names)):
        yield dict(zip(loop_names, values))


def generate_stoll_curves(convention: str) -> list[tuple[tuple[F, ...], ...]]:
    # Coordinate indices: a1,a2,a3,b1,b2,b3,c = 0..6.
    curves: list[tuple[tuple[F, ...], ...]] = []

    def append_block(names: tuple[str, ...], builder) -> None:
        for env in sign_environments(names, convention):
            curves.append(tuple(builder(env)))

    # C1s: the four source blocks, preserving their written comprehension
    # variable order (notably e3,e2,e1 in the fourth block).
    append_block(("e1", "e2", "e3"), lambda e: [
        linear((ONE, 0)),
        linear((ONE, 1), (scale(e["e1"], ONE), 5)),
        linear((ONE, 2), (scale(e["e2"], ONE), 4)),
        linear((ONE, 3), (scale(e["e3"], ONE), 6)),
    ])
    append_block(("e1", "e2", "e3"), lambda e: [
        linear((ONE, 1)),
        linear((ONE, 2), (scale(e["e1"], ONE), 3)),
        linear((ONE, 0), (scale(e["e2"], ONE), 5)),
        linear((ONE, 4), (scale(e["e3"], ONE), 6)),
    ])
    append_block(("e1", "e2", "e3"), lambda e: [
        linear((ONE, 2)),
        linear((ONE, 0), (scale(e["e1"], ONE), 4)),
        linear((ONE, 1), (scale(e["e2"], ONE), 3)),
        linear((ONE, 5), (scale(e["e3"], ONE), 6)),
    ])
    append_block(("e3", "e2", "e1"), lambda e: [
        linear((ONE, 6)),
        linear((I, 0), (scale(e["e1"], ONE), 3)),
        linear((I, 1), (scale(e["e2"], ONE), 4)),
        linear((I, 2), (scale(e["e3"], ONE), 5)),
    ])

    # C2s.
    append_block(("e1", "e2"), lambda e: [
        linear((ONE, 3)),
        linear((I, 1), (scale(e["e1"], ONE), 2)),
        linear((ONE, 0), (scale(e["e2"], ONE), 6)),
    ])
    append_block(("e1", "e2"), lambda e: [
        linear((ONE, 4)),
        linear((I, 2), (scale(e["e1"], ONE), 0)),
        linear((ONE, 1), (scale(e["e2"], ONE), 6)),
    ])
    append_block(("e1", "e2"), lambda e: [
        linear((ONE, 5)),
        linear((I, 0), (scale(e["e1"], ONE), 1)),
        linear((ONE, 2), (scale(e["e2"], ONE), 6)),
    ])

    # C3s, again preserving the written variable-order reversal in the last
    # three blocks.
    append_block(("e1", "e2", "e3"), lambda e: [
        linear((ONE, 0), (scale(e["e1"], ONE), 1)),
        linear((S, 0), (scale(e["e2"], ONE), 5)),
        linear((ONE, 3), (scale(e["e3"], ONE), 4)),
    ])
    append_block(("e1", "e2", "e3"), lambda e: [
        linear((ONE, 1), (scale(e["e1"], ONE), 2)),
        linear((S, 1), (scale(e["e2"], ONE), 3)),
        linear((ONE, 4), (scale(e["e3"], ONE), 5)),
    ])
    append_block(("e1", "e2", "e3"), lambda e: [
        linear((ONE, 2), (scale(e["e1"], ONE), 0)),
        linear((S, 2), (scale(e["e2"], ONE), 4)),
        linear((ONE, 5), (scale(e["e3"], ONE), 3)),
    ])
    append_block(("e3", "e2", "e1"), lambda e: [
        linear((I, 0), (scale(e["e1"], ONE), 6)),
        linear((I, 4), (scale(e["e2"], ONE), 5)),
        linear((IS, 0), (scale(e["e3"], ONE), 3)),
    ])
    append_block(("e3", "e2", "e1"), lambda e: [
        linear((I, 1), (scale(e["e1"], ONE), 6)),
        linear((I, 5), (scale(e["e2"], ONE), 3)),
        linear((IS, 1), (scale(e["e3"], ONE), 4)),
    ])
    append_block(("e3", "e2", "e1"), lambda e: [
        linear((I, 2), (scale(e["e1"], ONE), 6)),
        linear((I, 3), (scale(e["e2"], ONE), 4)),
        linear((IS, 2), (scale(e["e3"], ONE), 5)),
    ])

    if len(curves) != EXPECTED_CURVES:
        raise ValueError(f"Stoll known-curve count regression: {len(curves)}")
    return curves


def point_fingerprint(point: tuple[F, ...], curves) -> tuple[int, ...]:
    return tuple(
        1 if all(evaluate_linear(eq, point) == ZERO for eq in curve) else 0
        for curve in curves
    )


def format_field(x: F) -> str:
    names = ("", "i", "s", "i*s")
    terms: list[str] = []
    for coeff, name in zip(x, names):
        if coeff == 0:
            continue
        if name == "":
            term = str(abs(coeff))
        elif abs(coeff) == 1:
            term = name
        else:
            term = f"{abs(coeff)}*{name}"
        if not terms:
            terms.append(term if coeff > 0 else f"-{term}")
        else:
            terms.append(("+" if coeff > 0 else "-") + term)
    return "".join(terms) if terms else "0"


def canonical_fingerprint_data(convention: str):
    nodes = generate_canonical_nodes()
    curves = generate_stoll_curves(convention)
    fps = [point_fingerprint(point, curves) for point in nodes]
    weights = [sum(fp) for fp in fps]
    if len(set(fps)) != EXPECTED_NODES:
        raise ValueError(
            f"canonical node fingerprints collide under {convention}: {len(set(fps))}"
        )
    if set(weights) != {EXPECTED_INCIDENCE_WEIGHT}:
        raise ValueError(f"canonical incidence-weight regression under {convention}: {sorted(set(weights))}")
    return nodes, fps


def load_python_mapping(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained source {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    value = module.load()
    if not isinstance(value, dict):
        raise ValueError(f"retained source {path} did not return a mapping")
    return value


def fingerprint_sha256(fps: list[tuple[int, ...]]) -> str:
    payload = [list(fp) for fp in fps]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode()
    ).hexdigest()


def source_only_certificate() -> dict:
    nodes = generate_canonical_nodes()
    convention_data = {}
    for convention in ("LEFTMOST_OUTERMOST", "LEFTMOST_INNERMOST"):
        _, fps = canonical_fingerprint_data(convention)
        convention_data[convention] = {
            "curve_count": EXPECTED_CURVES,
            "node_count": len(nodes),
            "unique_fingerprint_count": len(set(fps)),
            "incidence_weight_set": sorted(set(sum(fp) for fp in fps)),
            "fingerprints_sha256": fingerprint_sha256(fps),
        }
    return {
        "status": "SOURCE_ONLY_PASS",
        "source_lock": {
            "repository": STOLL_REPOSITORY,
            "commit": STOLL_COMMIT,
            "path": STOLL_PATH,
            "runtime_constructor": "pts := Points(SingularSubscheme(S))",
            "runtime_count_assertion": "assert #pts eq 48",
            "all140_order": "Cs[1..92] cat pts[1..48]",
        },
        "coordinate_model": "[a1,a2,a3,b1,b2,b3,c] over Q(i,sqrt(2))",
        "canonical_projective_normalization": "first nonzero coordinate = 1",
        "canonical_node_count": len(nodes),
        "canonical_node_unique_count": len(set(nodes)),
        "all_generated_nodes_exactly_on_surface_and_jacobian_singular": True,
        "convention_diagnostics": convention_data,
    }


def runtime_bridge(repo_root: Path) -> dict:
    residual = repo_root / "stages/stage32/residual-32-01-production"
    marking_path = repo_root / "stages/stage33/33-07/stage32_picard_marking_retained.py"
    sys.path.insert(0, str(residual))
    from hperp_integral_adapter import _parse_hperp, _recover_full_intersection

    marking = load_python_mapping(marking_path, "s32ex5_b_stage32_marking")
    hperp_text = marking.get("hperp_text")
    if not isinstance(hperp_text, str):
        raise ValueError("retained marking has no hperp_text")
    if hashlib.sha256(hperp_text.encode()).hexdigest() != EXPECTED_HPERP_SHA256:
        raise ValueError("retained hperp_text SHA regression")
    q, degree, linear, _caps, hmeta = _parse_hperp(hperp_text)
    full = _recover_full_intersection(q, degree, linear)
    if full.shape != (EXPECTED_ALL140, EXPECTED_ALL140):
        raise ValueError(f"all140 shape regression: {full.shape}")

    runtime_fps = [
        tuple(int(full[j, 92 + k]) for j in range(92))
        for k in range(48)
    ]
    if any(v not in (0, 1) for fp in runtime_fps for v in fp):
        raise ValueError("retained 92x48 curve/exceptional block is not 0/1")
    if len(set(runtime_fps)) != EXPECTED_NODES:
        raise ValueError(f"retained runtime fingerprints collide: {len(set(runtime_fps))}")
    if set(sum(fp) for fp in runtime_fps) != {EXPECTED_INCIDENCE_WEIGHT}:
        raise ValueError("retained runtime incidence-weight regression")

    candidates = []
    for convention in ("LEFTMOST_OUTERMOST", "LEFTMOST_INNERMOST"):
        nodes, canonical_fps = canonical_fingerprint_data(convention)
        if set(canonical_fps) != set(runtime_fps):
            continue
        by_fp = {fp: idx for idx, fp in enumerate(canonical_fps)}
        mapping = tuple(by_fp[fp] for fp in runtime_fps)
        candidates.append((convention, nodes, canonical_fps, mapping))

    if not candidates:
        raise ValueError("no exact source-comprehension convention reproduces retained runtime fingerprints")
    mappings = {candidate[3] for candidate in candidates}
    if len(mappings) != 1:
        raise ValueError(
            "source-comprehension convention ambiguity changes runtime-index/node mapping"
        )
    convention_names = [candidate[0] for candidate in candidates]
    _, nodes, canonical_fps, mapping = candidates[0]

    rows = []
    for runtime_index, canonical_index in enumerate(mapping):
        point = nodes[canonical_index]
        rows.append({
            "runtime_exceptional_index_0based": runtime_index,
            "runtime_pts_index_1based": runtime_index + 1,
            "all140_index_0based": 92 + runtime_index,
            "all140_label_1based": 93 + runtime_index,
            "canonical_node_index_0based": canonical_index,
            "projective_coordinates": [format_field(x) for x in point],
            "projective_coordinates_ring_coefficients_a_bi_cs_dis": [list(x) for x in point],
            "incidence_weight": sum(runtime_fps[runtime_index]),
            "fingerprint_sha256": hashlib.sha256(bytes(runtime_fps[runtime_index])).hexdigest(),
        })

    out = {
        "status": "PASS_EXACT_48_OF_48_RUNTIME_NODE_BRIDGE",
        "source_only_certificate": source_only_certificate(),
        "retained_runtime": {
            "marking_path": str(marking_path.relative_to(repo_root)),
            "hperp_text_sha256": EXPECTED_HPERP_SHA256,
            "hperp_metadata": hmeta,
            "recovered_all140_shape": [int(full.rows), int(full.cols)],
            "runtime_fingerprint_count": len(runtime_fps),
            "runtime_unique_fingerprint_count": len(set(runtime_fps)),
            "runtime_incidence_weight_set": sorted(set(sum(fp) for fp in runtime_fps)),
            "runtime_fingerprints_sha256": fingerprint_sha256(runtime_fps),
        },
        "enumeration_resolution": {
            "matching_source_comprehension_conventions": convention_names,
            "mapping_is_convention_invariant_over_all_matches": True,
            "magma_Points_enumeration_order_reproduction_required": False,
            "reason": "runtime columns are identified by exact 92-curve incidence fingerprints",
        },
        "bijection": {
            "runtime_count": 48,
            "canonical_node_count": 48,
            "matched_count": len(rows),
            "unique": len(set(mapping)) == 48,
            "rows": rows,
        },
    }
    canonical = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
    out["canonical_sha256_without_this_field"] = hashlib.sha256(canonical).hexdigest()
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path)
    parser.add_argument("--source-only", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.source_only:
        out = source_only_certificate()
    else:
        repo_root = args.repo_root
        if repo_root is None:
            repo_root = Path(__file__).resolve().parents[4]
        out = runtime_bridge(repo_root.resolve())

    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
