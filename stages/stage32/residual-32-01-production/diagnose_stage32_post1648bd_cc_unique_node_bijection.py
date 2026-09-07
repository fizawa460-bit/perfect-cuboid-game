#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
AZ_PATH = HERE / "diagnose_stage32_post1648az_full_48node_equivariant_bijection.py"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
sys.path.insert(0, str(HERE))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_retained(path: Path, name: str) -> dict:
    return load_module(path, name).load()


def recover_known140_perm(coords: Matrix, action: Matrix) -> list[int]:
    lut = {tuple(int(coords[i, j]) for j in range(64)): i for i in range(140)}
    if len(lut) != 140:
        raise ValueError("known140 coordinate rows are not unique")
    out = []
    for i in range(140):
        r = Matrix([[int(coords[i, j]) for j in range(64)]]) * action
        key = tuple(int(r[0, j]) for j in range(64))
        if key not in lut:
            raise ValueError(f"Picard action exits known140 at row {i}")
        out.append(lut[key])
    if sorted(out) != list(range(140)):
        raise ValueError("recovered known140 action is not bijective")
    return out


def source_cc_perm(az, nodes) -> tuple[int, ...]:
    idx = {v: i for i, v in enumerate(nodes)}
    out = []
    for v in nodes:
        w = az.canon(tuple(z.conjugate() for z in v))
        out.append(idx[w])
    return tuple(out)


def is_projectively_rational(v: tuple[complex, ...]) -> bool:
    # az.canon normalizes the first nonzero coordinate to 1, so Q-rationality
    # for these {0, +/-1, +/-i} nodes is exactly all coordinates real.
    return all(abs(z.imag) < 0.5 for z in v)


def propagate_one(src_gens, ret_gens, s0: int, e0: int) -> dict[int, int] | None:
    f = {s0: e0}
    inv = {e0: s0}
    queue = [s0]
    while queue:
        s = queue.pop()
        e = f[s]
        for sg, rg in zip(src_gens, ret_gens):
            s2 = sg[s]
            e2 = rg[e - 1] + 1
            if s2 in f and f[s2] != e2:
                return None
            if e2 in inv and inv[e2] != s2:
                return None
            if s2 not in f:
                f[s2] = e2
                inv[e2] = s2
                queue.append(s2)
    if len(f) != 48 or set(f.values()) != set(range(93, 141)):
        return None
    return f


def main() -> None:
    az = load_module(AZ_PATH, "s32_bd_az")
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_bd_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_bd_base")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)

    raw = [tuple(x - 1 for x in g) for g in marking["aut_action"]["permutations_1based"]]
    if len(raw) != 9:
        raise ValueError("retained generator count regression")

    nodes = az.source_nodes()
    if len(nodes) != 48:
        raise ValueError("source node count regression")
    t12 = az.perm_from_map(nodes, "t12")
    t13 = az.perm_from_map(nodes, "t13")
    sigma = az.perm_from_map(nodes, "sigma")
    sigma13 = az.perm_conjugate(t13, sigma)
    src = [t12, t13, sigma13] + [az.perm_from_map(nodes, f"sign_{k}") for k in range(6)]

    # Fix one source basepoint.  For a transitive G-set, distinct valid images
    # of this one point are exactly the distinct generator-by-generator G-set
    # isomorphisms; this avoids the repeated counting present in the AZ 8x8
    # anchor-pair diagnostic.
    source_basepoint = 0
    aut_solutions = []
    for e0 in range(93, 141):
        f = propagate_one(src, raw, source_basepoint, e0)
        if f is not None:
            aut_solutions.append(f)
    if not aut_solutions:
        raise ValueError("no Aut-equivariant source/retained node bijection")

    cc140 = recover_known140_perm(coords, Matrix(bundle["picard_action_cc_64x64"]))
    ct140 = recover_known140_perm(coords, Matrix(bundle["picard_action_ct_64x64"]))
    scc = source_cc_perm(az, nodes)

    cc_solutions = []
    for f in aut_solutions:
        if all(f[scc[s]] == cc140[f[s] - 1] + 1 for s in range(48)):
            cc_solutions.append(f)

    rational_source = [i for i, v in enumerate(nodes) if is_projectively_rational(v)]
    if len(rational_source) != 24:
        raise ValueError(f"source rational node count regression: {len(rational_source)}")
    retained_cc_fixed = [e for e in range(93, 141) if cc140[e - 1] + 1 == e]
    retained_ct_fixed = [e for e in range(93, 141) if ct140[e - 1] + 1 == e]
    if len(retained_cc_fixed) != 24 or len(retained_ct_fixed) != 48:
        raise ValueError("retained Galois exceptional signature regression")

    unique = len(cc_solutions) == 1
    chosen = cc_solutions[0] if unique else None

    v6 = json.loads(V6_PATH.read_text())
    masses = [int(x) for x in v6["witness"]["all140_pairings"]][92:]
    if len(masses) != 48 or sum(masses) != 266:
        raise ValueError("V6 exceptional mass regression")
    vcoords = Matrix([[int(x) for x in v6["witness"]["picard_coordinates"]]])
    cc_class_invariant = (vcoords * Matrix(bundle["picard_action_cc_64x64"]) == vcoords)
    ct_class_invariant = (vcoords * Matrix(bundle["picard_action_ct_64x64"]) == vcoords)
    cc_mass_invariant = all(masses[e - 93] == masses[(cc140[e - 1] + 1) - 93] for e in range(93, 141))

    records = []
    rational_mass = None
    nonrational_mass = None
    if chosen is not None:
        if {chosen[s] for s in rational_source} != set(retained_cc_fixed):
            raise ValueError("unique cc-equivariant bijection fails Q-node fixed-set check")
        for s in range(48):
            e = chosen[s]
            records.append({
                "source_node_index_zero_based": s,
                "source_projective_coordinates_a1_a2_a3_b1_b2_b3_c": [az.fmt(z) for z in nodes[s]],
                "source_defined_over_Q": s in rational_source,
                "retained_exceptional_label_1based": e,
                "retained_cc_fixed": e in retained_cc_fixed,
                "v6_exceptional_intersection_multiplicity": masses[e - 93],
            })
        rational_mass = sum(r["v6_exceptional_intersection_multiplicity"] for r in records if r["source_defined_over_Q"])
        nonrational_mass = 266 - rational_mass

    print(json.dumps({
        "mode": "SCRATCH_POST1648BD_CC_EQUIVARIANT_NODE_BIJECTION",
        "source_node_count": 48,
        "source_basepoint_zero_based": source_basepoint,
        "aut_equivariant_distinct_bijection_count": len(aut_solutions),
        "az_anchor_reported_solution_count_was_not_deduplicated": True,
        "cc_equivariant_bijection_count": len(cc_solutions),
        "unique_full_aut_plus_cc_bijection_obtained": unique,
        "source_Q_defined_node_count": len(rational_source),
        "retained_cc_fixed_exceptional_count": len(retained_cc_fixed),
        "retained_ct_fixed_exceptional_count": len(retained_ct_fixed),
        "v6": {
            "exceptional_mass_total": sum(masses),
            "cc_class_invariant": bool(cc_class_invariant),
            "ct_class_invariant": bool(ct_class_invariant),
            "cc_exceptional_mass_vector_invariant": cc_mass_invariant,
            "mass_on_source_Q_defined_nodes": rational_mass,
            "mass_on_source_Qi_nonrational_nodes": nonrational_mass,
        },
        "records": records,
        "decision": {
            "full_48node_semantic_label_adapter_obtained": unique,
            "next_exact_route": "WITH_UNIQUE_SOURCE_NODE_LABELS,_TEST_V6_EXCEPTIONAL_MULTIPLICITIES_AGAINST_SOURCE_LOCAL_BRANCH/TANGENT_AND_GALOIS_CONSTRAINTS" if unique else "ADD_ANOTHER_INDEPENDENT_SOURCE_STRUCTURE_TO_BREAK_REMAINING_NODE_LABEL_AMBIGUITY",
        },
        "firewalls": {
            "runner_side_import_only": True,
            "giant_retained_payload_whole_fetch_used": False,
            "v6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
            "scratch_only": True,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
