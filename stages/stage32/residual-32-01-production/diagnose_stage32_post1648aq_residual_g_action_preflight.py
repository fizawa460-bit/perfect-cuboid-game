#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter, defaultdict
from math import gcd
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
MARKING_PATH = ST33 / "stage32_picard_marking_retained.py"
BUNDLE_PATH = ST33 / "picard_base_rows_retained.py"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
sys.path.insert(0, str(HERE))

from hperp_integral_adapter import (  # noqa: E402
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
    _parse_hperp,
)


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def perm0(p1: list[int]) -> tuple[int, ...]:
    return tuple(int(x) - 1 for x in p1)


def compose(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a[b[i]] for i in range(len(a)))


def order(p: tuple[int, ...]) -> int:
    n = len(p)
    seen = [False] * n
    out = 1
    for i in range(n):
        if seen[i]:
            continue
        j = i
        k = 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            k += 1
        if k:
            out = out * k // gcd(out, k)
    return out


def cycle_profile(p: tuple[int, ...]) -> dict[str, int]:
    n = len(p)
    seen = [False] * n
    prof: dict[str, int] = {}
    for i in range(n):
        if seen[i]:
            continue
        j = i
        k = 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            k += 1
        prof[str(k)] = prof.get(str(k), 0) + 1
    return prof


def close(gens: list[tuple[int, ...]], cap: int = 200000) -> list[tuple[int, ...]]:
    if not gens:
        return []
    ident = tuple(range(len(gens[0])))
    group = {ident}
    frontier = [ident]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = compose(g, x)
            if y not in group:
                group.add(y)
                frontier.append(y)
                if len(group) > cap:
                    raise RuntimeError(f"group cap exceeded: {cap}")
    return sorted(group)


def orbit(seed: int, group: list[tuple[int, ...]]) -> list[int]:
    return sorted({g[seed] for g in group})


def orbit_partition(indices: set[int], group: list[tuple[int, ...]]) -> list[list[int]]:
    unseen = set(indices)
    out: list[list[int]] = []
    while unseen:
        s = min(unseen)
        o = orbit(s, group)
        if not set(o) <= indices:
            raise ValueError("orbit leaves requested population")
        out.append(o)
        unseen -= set(o)
    return sorted(out, key=lambda x: (len(x), x))


def bounded_meta(v: object) -> object:
    if v is None or isinstance(v, (bool, int, float)):
        return v
    if isinstance(v, str):
        return v if len(v) <= 240 else {"type": "str", "length": len(v), "prefix": v[:120]}
    if isinstance(v, list):
        if len(v) <= 16 and all(isinstance(x, (str, int, bool)) for x in v):
            return v
        return {"type": "list", "length": len(v), "item_types": sorted({type(x).__name__ for x in v})}
    if isinstance(v, dict):
        if len(v) <= 12 and all(isinstance(x, (str, int, float, bool)) or x is None for x in v.values()):
            return v
        return {"type": "dict", "keys": sorted(map(str, v.keys())), "length": len(v)}
    return {"type": type(v).__name__}


def action_matrix(g: tuple[int, ...], coords: Matrix, basis_indices: list[int]) -> Matrix:
    # Rows of M are images of retained basis curves; row-vector classes act by C -> C*M.
    rows = [list(coords.row(g[i])) for i in basis_indices]
    M = Matrix(rows)
    all_images = Matrix.vstack(*[coords.row(g[i]) for i in range(coords.rows)])
    if coords * M != all_images:
        raise ValueError("Picard action orientation does not reproduce all 140 curve images")
    return M


def row_key(v: Matrix) -> tuple[int, ...]:
    return tuple(int(v[0, j]) for j in range(v.cols))


def solve_exceptional_span(T: Matrix, exceptional_coords: Matrix) -> dict:
    # Solve E^T m = T^T. The 48 exceptional curves are expected independent.
    A = exceptional_coords.T
    try:
        sol, params = A.gauss_jordan_solve(T.T)
    except ValueError:
        return {"in_exceptional_span": False}
    if params.rows != 0:
        return {"in_exceptional_span": True, "unique": False, "parameter_count": params.rows}
    vals = []
    for x in sol:
        if getattr(x, "q", 1) != 1:
            return {"in_exceptional_span": True, "unique": True, "integral": False}
        vals.append(int(x))
    return {
        "in_exceptional_span": True,
        "unique": True,
        "integral": True,
        "nonnegative": all(x >= 0 for x in vals),
        "coefficients_exceptional_labels_93_to_140": vals,
        "coefficient_sum": sum(vals),
        "coefficient_max": max(vals),
        "positive_support": sum(x > 0 for x in vals),
    }


def main() -> None:
    marking = load_retained(MARKING_PATH, "s32_aq_marking")
    bundle = load_retained(BUNDLE_PATH, "s32_aq_bundle")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    if coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("retained Picard shape regression")
    full = coords * gram * coords.T

    aut = marking.get("aut_action")
    if not isinstance(aut, dict):
        raise ValueError("retained marking aut_action missing or non-dict")
    p_raw = aut.get("permutations_1based")
    if not isinstance(p_raw, list) or not p_raw:
        raise ValueError("aut_action.permutations_1based missing")
    gens = [perm0(p) for p in p_raw]
    n = len(gens[0])
    if n != 140 or any(len(g) != n for g in gens):
        raise ValueError("generator permutation degree regression")
    group = close(gens)

    _, degree, _, _, _ = _parse_hperp(marking["hperp_text"])
    degrees = [int(degree[i, 0]) for i in range(140)]
    normal_orbits = orbit_partition(set(range(92)), group)
    boundary_candidates = [o for o in normal_orbits if len(o) == 12 and {degrees[i] for i in o} == {4}]
    if len(boundary_candidates) != 1:
        raise ValueError("unique boundary orbit regression")
    boundary = boundary_candidates[0]

    boundary_pointwise = [g for g in group if all(g[i] == i for i in boundary)]
    boundary_setwise = [g for g in group if {g[i] for i in boundary} == set(boundary)]
    bp_orders = Counter(order(g) for g in boundary_pointwise)

    basis_indices = [j - 1 for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    v6 = json.loads(V6_PATH.read_text())
    C = Matrix([[int(x) for x in v6["witness"]["picard_coordinates"]]])
    C2 = int((C * gram * C.T)[0, 0])
    if C2 != 758:
        raise ValueError("V6 self-intersection regression")

    ident = tuple(range(140))
    residual_rows = []
    orbit_classes: set[tuple[int, ...]] = set()
    S = Matrix([[0] * 64])
    for g in boundary_pointwise:
        M = action_matrix(g, coords, basis_indices)
        if M * gram * M.T != gram:
            raise ValueError("retained automorphism does not preserve Picard Gram")
        Cg = C * M
        if int((Cg * gram * Cg.T)[0, 0]) != C2:
            raise ValueError("V6 translate self-intersection moved")
        S += Cg
        orbit_classes.add(row_key(Cg))
        residual_rows.append({
            "identity": g == ident,
            "element_order": order(g),
            "cycle_profile_140": cycle_profile(g),
            "C_dot_gC": int((C * gram * Cg.T)[0, 0]),
            "C_class_fixed": Cg == C,
        })
    residual_rows.sort(key=lambda r: (not r["identity"], r["C_dot_gC"], json.dumps(r["cycle_profile_140"], sort_keys=True)))
    nontriv_intersections = sorted(r["C_dot_gC"] for r in residual_rows if not r["identity"])
    sum_nontriv = sum(nontriv_intersections)

    # Reconstruct the two AM fibre classes directly from the 12 source-bound boundary elliptics.
    fibre_classes: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for i in boundary:
        inc = [int(full[i, j]) for j in range(92, 140)]
        if sum(inc) != 8 or sum(x > 0 for x in inc) != 8 or any(x not in (0, 1) for x in inc):
            raise ValueError("boundary exceptional incidence regression")
        B = 2 * coords.row(i)
        for off, mult in enumerate(inc):
            if mult:
                B += coords.row(92 + off)
        fibre_classes[row_key(B)].append(i + 1)
    if len(fibre_classes) != 2 or sorted(map(len, fibre_classes.values())) != [6, 6]:
        raise ValueError("AM 6+6 fibre-class regression")

    fibres = []
    for k, labels in sorted(fibre_classes.items(), key=lambda kv: kv[1]):
        F = Matrix([list(k)])
        fibres.append({
            "F": F,
            "labels_1based": labels,
            "C_dot_F": int((C * gram * F.T)[0, 0]),
            "F_square": int((F * gram * F.T)[0, 0]),
        })
    if sorted(f["C_dot_F"] for f in fibres) != [81, 105]:
        raise ValueError("AM V6 factor-degree regression")
    F81 = next(f["F"] for f in fibres if f["C_dot_F"] == 81)
    F105 = next(f["F"] for f in fibres if f["C_dot_F"] == 105)

    # For a bidegree-(81,105) image, the base divisor class pulls back with the
    # opposite fibre coefficients relative to projection degrees: P=105*F81+81*F105.
    P = 105 * F81 + 81 * F105
    P_wrong = 81 * F81 + 105 * F105
    image_square = 2 * 81 * 105
    pullback_square = int((P * gram * P.T)[0, 0])
    if pullback_square != 8 * image_square:
        raise ValueError("factor pullback square regression")
    if int((C * gram * P.T)[0, 0]) != image_square:
        raise ValueError("opposite-coefficient bidegree orientation regression")

    E = coords[92:140, :]
    T = P - S
    T_wrong = P_wrong - S
    exc_solution = solve_exceptional_span(T, E)
    exc_solution_wrong = solve_exceptional_span(T_wrong, E)
    if exc_solution.get("in_exceptional_span") and exc_solution.get("integral"):
        m = exc_solution["coefficients_exceptional_labels_93_to_140"]
        e = [int(x) for x in v6["witness"]["all140_pairings"][92:]]
        exc_solution["C_dot_exceptional_correction_from_coefficients"] = sum(mi * ei for mi, ei in zip(m, e))
        exc_solution["C_dot_exceptional_correction_direct"] = int((C * gram * T.T)[0, 0])
        exc_solution["T_square"] = int((T * gram * T.T)[0, 0])
        exc_solution["S_dot_T"] = int((S * gram * T.T)[0, 0])
        exc_solution["S_square"] = int((S * gram * S.T)[0, 0])
        exc_solution["P_square"] = int((P * gram * P.T)[0, 0])
        exc_solution["square_decomposition_holds"] = (
            exc_solution["P_square"] == exc_solution["S_square"] + 2 * exc_solution["S_dot_T"] + exc_solution["T_square"]
        )

    out = {
        "mode": "SCRATCH_POST1648AQ_RESIDUAL_G_ACTION_EXCEPTIONAL_CORRECTION",
        "retained_marking_path": str(MARKING_PATH.relative_to(ROOT)),
        "retained_aut_source": bounded_meta(aut.get("source")),
        "retained_aut_source_splice": bounded_meta(aut.get("source_splice")),
        "aut_action_canonical": aut.get("canonical_sha256_without_this_field"),
        "full_retained_group": {
            "order": len(group),
            "stored_generator_count": len(gens),
            "element_order_histogram": dict(sorted(Counter(order(g) for g in group).items())),
        },
        "boundary_anchor": {
            "labels_1based": [i + 1 for i in boundary],
            "pointwise_stabilizer_order": len(boundary_pointwise),
            "pointwise_stabilizer_element_order_histogram": dict(sorted(bp_orders.items())),
            "setwise_stabilizer_order": len(boundary_setwise),
            "source_residual_G_order": 8,
            "source_residual_G_type": "(Z/2)^3",
            "candidate_exact_order_and_exponent_match": len(boundary_pointwise) == 8 and bp_orders == Counter({2: 7, 1: 1}),
        },
        "v6_residual_orbit": {
            "class_orbit_size": len(orbit_classes),
            "class_stabilizer_trivial_in_candidate_G": len(orbit_classes) == len(boundary_pointwise),
            "rows": residual_rows,
            "nontrivial_C_dot_gC_sorted": nontriv_intersections,
            "sum_nontrivial_C_dot_gC": sum_nontriv,
            "orbit_sum_square": int((S * gram * S.T)[0, 0]),
            "C_dot_orbit_sum": int((C * gram * S.T)[0, 0]),
        },
        "factor_pullback": {
            "fibre_classes": [
                {"labels_1based": f["labels_1based"], "C_dot_F": f["C_dot_F"], "F_square": f["F_square"]}
                for f in fibres
            ],
            "image_bidegree": [81, 105],
            "image_square": image_square,
            "full_pullback_class_formula": "P=105*F_(C.F=81)+81*F_(C.F=105)",
            "P_square": pullback_square,
            "C_dot_P": int((C * gram * P.T)[0, 0]),
            "degree_8_image_square": 8 * image_square,
        },
        "exceptional_correction": {
            "T_formula": "T=P-sum_{h in H} hC",
            "correct_orientation": exc_solution,
            "same_orientation_control": exc_solution_wrong,
        },
        "decision": {
            "candidate_subgroup_has_residual_G_numerical_signature": len(boundary_pointwise) == 8 and bp_orders == Counter({2: 7, 1: 1}),
            "strict_transform_orbit_alone_is_full_pullback": T == Matrix([[0] * 64]),
            "full_pullback_minus_orbit_is_exact_exceptional_class": bool(exc_solution.get("in_exceptional_span") and exc_solution.get("unique") and exc_solution.get("integral")),
            "full_pullback_minus_orbit_is_effective_exceptional": bool(exc_solution.get("nonnegative")),
            "naive_AP_conductor_upper_bound_route_closes": False,
            "next_missing_input": "INTERPRET_EXCEPTIONAL_CORRECTION_LOCALLY_AND_SOURCE_BIND_BOUNDARY_POINTWISE_SUBGROUP_TO_RESIDUAL_G",
        },
        "firewalls": {
            "scratch_only": True,
            "retained_payload_emitted": False,
            "residual_G_semantic_identification_granted": False,
            "V6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
