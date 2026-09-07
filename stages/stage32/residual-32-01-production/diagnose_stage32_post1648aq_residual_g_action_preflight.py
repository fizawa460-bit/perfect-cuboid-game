#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter
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
    rows = [list(coords.row(g[i])) for i in basis_indices]
    return Matrix(rows)


def main() -> None:
    marking = load_retained(MARKING_PATH, "s32_aq_marking")
    bundle = load_retained(BUNDLE_PATH, "s32_aq_bundle")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    if coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("retained Picard shape regression")

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

    generator_summaries = [
        {"index_1based": i + 1, "order": order(g), "cycle_profile": cycle_profile(g)}
        for i, g in enumerate(gens)
    ]

    # Recover the unique 12-element degree-4 normal-curve orbit used by AM.
    _, degree, _, _, _ = _parse_hperp(marking["hperp_text"])
    degrees = [int(degree[i, 0]) for i in range(140)]
    normal_orbits = orbit_partition(set(range(92)), group)
    boundary_candidates = [o for o in normal_orbits if len(o) == 12 and {degrees[i] for i in o} == {4}]
    if len(boundary_candidates) != 1:
        raise ValueError(f"unique boundary orbit regression: {[(len(o), sorted({degrees[i] for i in o})) for o in normal_orbits]}")
    boundary = boundary_candidates[0]

    # Source residual deck G acts trivially on Z x Z, hence fixes each of the
    # six special fibres in both directions and therefore each of the twelve
    # AM-source-bound boundary elliptics. Compute the pointwise stabilizer of
    # those 12 labels inside the retained geometric automorphism group.
    boundary_pointwise = [g for g in group if all(g[i] == i for i in boundary)]
    boundary_setwise = [g for g in group if {g[i] for i in boundary} == set(boundary)]
    bp_orders = Counter(order(g) for g in boundary_pointwise)

    # Build exact Picard action matrices and evaluate the V6 orbit.
    basis_indices = [j - 1 for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    v6 = json.loads(V6_PATH.read_text())
    C = Matrix([[int(x) for x in v6["witness"]["picard_coordinates"]]])
    C2 = int((C * gram * C.T)[0, 0])
    if C2 != 758:
        raise ValueError("V6 self-intersection regression")

    ident = tuple(range(140))
    residual_rows = []
    orbit_classes: set[tuple[int, ...]] = set()
    for g in boundary_pointwise:
        M = action_matrix(g, coords, basis_indices)
        if M * gram * M.T != gram:
            raise ValueError("retained automorphism does not preserve Picard Gram")
        Cg = C * M
        if int((Cg * gram * Cg.T)[0, 0]) != C2:
            raise ValueError("V6 translate self-intersection moved")
        key = tuple(int(x) for x in Cg)
        orbit_classes.add(key)
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

    # AP image D has bidegree (81,105), so D^2=2*81*105.
    image_square = 2 * 81 * 105
    pullback_square = 8 * image_square
    orbit_square_from_intersections = 8 * (C2 + sum_nontriv)

    # Canonical ramification correction for Phi:B~ -> P1xP1.
    # K_B.C=186 from V6; Phi^*K_(P1xP1).C=-2*(81+105)=-372.
    K_dot_C = 186
    pullback_base_K_dot_C = -2 * (81 + 105)
    ramification_dot_C = K_dot_C - pullback_base_K_dot_C
    conductor_from_orbit_and_ramification = (sum_nontriv - ramification_dot_C) // 2
    if (sum_nontriv - ramification_dot_C) % 2:
        raise ValueError("conductor correction parity regression")

    out = {
        "mode": "SCRATCH_POST1648AQ_RESIDUAL_G_ACTION_AND_CONDUCTOR_IDENTITY",
        "retained_marking_path": str(MARKING_PATH.relative_to(ROOT)),
        "retained_aut_source": bounded_meta(aut.get("source")),
        "retained_aut_source_splice": bounded_meta(aut.get("source_splice")),
        "aut_action_canonical": aut.get("canonical_sha256_without_this_field"),
        "full_retained_group": {
            "order": len(group),
            "stored_generator_count": len(gens),
            "stored_generator_summaries": generator_summaries,
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
        },
        "quotient_intersection_identity": {
            "C_square": C2,
            "image_bidegree": [81, 105],
            "image_square": image_square,
            "degree_8_pullback_square_expected": pullback_square,
            "orbit_square_from_C_and_pairwise_intersections": orbit_square_from_intersections,
            "square_identity_holds": pullback_square == orbit_square_from_intersections,
        },
        "canonical_ramification_correction": {
            "K_B_dot_C": K_dot_C,
            "Phi_pullback_K_P1xP1_dot_C": pullback_base_K_dot_C,
            "R_dot_C": ramification_dot_C,
            "half_sum_C_dot_gC": sum_nontriv // 2 if sum_nontriv % 2 == 0 else None,
            "conductor_length_formula": "(sum_{g!=1} C.gC - R.C)/2",
            "conductor_length_from_action": conductor_from_orbit_and_ramification,
            "AP_required_conductor_length": 7847,
            "exactly_matches_AP_demand": conductor_from_orbit_and_ramification == 7847,
        },
        "decision": {
            "candidate_residual_G_semantic_anchor_complete_if_source_inclusion_verified": len(boundary_pointwise) == 8 and bp_orders == Counter({2: 7, 1: 1}),
            "naive_global_conductor_budget_excludes_V6": False,
            "global_intersection_budget_is_adjunction_quotient_identity": conductor_from_orbit_and_ramification == 7847 and pullback_square == orbit_square_from_intersections,
            "next_missing_input": "LOCAL_FIXED_LOCUS_AND_BRANCH_INTERSECTION_ALLOCATION_BEYOND_GLOBAL_INTERSECTION_NUMBERS",
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
