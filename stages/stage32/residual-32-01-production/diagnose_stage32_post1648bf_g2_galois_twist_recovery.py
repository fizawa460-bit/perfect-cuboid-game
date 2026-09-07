#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
AZ_PATH = HERE / "diagnose_stage32_post1648az_full_48node_equivariant_bijection.py"
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


def compose(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a[b[i]] for i in range(len(a)))


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(n))


def power(a: tuple[int, ...], n: int) -> tuple[int, ...]:
    r = identity(len(a))
    for _ in range(n):
        r = compose(a, r)
    return r


def recover_known140_perm(coords: Matrix, action: Matrix) -> list[int]:
    lut = {tuple(int(coords[i, j]) for j in range(64)): i for i in range(140)}
    if len(lut) != 140:
        raise ValueError("known140 coordinates not unique")
    out = []
    for i in range(140):
        r = Matrix([[int(coords[i, j]) for j in range(64)]]) * action
        key = tuple(int(r[0, j]) for j in range(64))
        if key not in lut:
            raise ValueError(f"action exits known140 at {i}")
        out.append(lut[key])
    return out


def propagate(src_gens, ret_gens, s0: int, e0: int):
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


def source_cc_perm(az, nodes):
    idx = {v: i for i, v in enumerate(nodes)}
    return tuple(idx[az.canon(tuple(z.conjugate() for z in v))] for v in nodes)


def main() -> None:
    az = load_module(AZ_PATH, "s32_bf_az")
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_bf_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_bf_base")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)

    raw = [tuple(x - 1 for x in g) for g in marking["aut_action"]["permutations_1based"]]
    if len(raw) != 9:
        raise ValueError("retained raw generator count regression")

    nodes = az.source_nodes()
    if len(nodes) != 48:
        raise ValueError("source node count regression")
    t12 = az.perm_from_map(nodes, "t12")
    t13 = az.perm_from_map(nodes, "t13")
    sigma = az.perm_from_map(nodes, "sigma")
    sigma13 = az.perm_conjugate(t13, sigma)
    signs = [az.perm_from_map(nodes, f"sign_{k}") for k in range(6)]
    scc = source_cc_perm(az, nodes)

    cc140 = recover_known140_perm(coords, Matrix(bundle["picard_action_cc_64x64"]))
    retained_cc = tuple(cc140[e - 1] - 92 for e in range(93, 141))
    # retained_cc is a 0..47 permutation after subtracting the exceptional offset.
    if sorted(retained_cc) != list(range(48)):
        raise ValueError("retained cc does not preserve exceptional 48")

    # The first two raw generators and six sign generators are source-bound by
    # quotient/signature data and are Q-defined.  Only raw g2 needs a sign-kernel
    # twist inside its exact S4 quotient coset.  Enumerate all 64 projective sign
    # twists k*sigma13 with c-sign gauge fixed to zero.
    candidates = []
    base = identity(48)
    for bits in itertools.product((0, 1), repeat=6):
        k = base
        for j, bit in enumerate(bits):
            if bit:
                k = compose(signs[j], k)
        g2 = compose(k, sigma13)
        candidates.append((bits, g2))
    if len({g for _, g in candidates}) != 64:
        raise ValueError("source g2 sign-twist coset cardinality regression")

    source_basepoint = 0
    aut_hits = []
    cc_hits = []
    candidate_summaries = []
    for bits, g2 in candidates:
        src = [t12, t13, g2] + signs
        local_aut = []
        local_cc = []
        for e0 in range(93, 141):
            f = propagate(src, raw, source_basepoint, e0)
            if f is None:
                continue
            local_aut.append(f)
            if all(
                f[scc[s]] - 93 == retained_cc[f[s] - 93]
                for s in range(48)
            ):
                local_cc.append(f)
        if local_aut:
            aut_hits.extend((bits, f) for f in local_aut)
        if local_cc:
            cc_hits.extend((bits, f) for f in local_cc)
        candidate_summaries.append({
            "twist_bits_a1_a2_a3_b1_b2_b3": list(bits),
            "g2_order": next(n for n in range(1, 17) if power(g2, n) == base),
            "g2_fixed_source_node_count": sum(g2[i] == i for i in range(48)),
            "aut_equivariant_bijection_count": len(local_aut),
            "aut_plus_cc_equivariant_bijection_count": len(local_cc),
        })

    unique_cc_twists = sorted({bits for bits, _ in cc_hits})
    unique_aut_twists = sorted({bits for bits, _ in aut_hits})
    if not cc_hits:
        raise ValueError("no source g2 sign twist restores Galois-equivariant node action")

    # Deduplicate actual bijections independent of source twist record.
    def fkey(f):
        return tuple(f[i] for i in range(48))
    distinct_cc_maps = {fkey(f): (bits, f) for bits, f in cc_hits}
    distinct_aut_maps = {fkey(f): (bits, f) for bits, f in aut_hits}

    chosen_bits = None
    chosen_map = None
    if len(distinct_cc_maps) == 1:
        chosen_bits, chosen_map = next(iter(distinct_cc_maps.values()))

    print(json.dumps({
        "mode": "SCRATCH_POST1648BF_G2_GALOIS_TWIST_RECOVERY",
        "source_g2_coset_candidate_count": 64,
        "source_basepoint_zero_based": source_basepoint,
        "twists_with_any_aut_equivariant_bijection_count": len(unique_aut_twists),
        "twists_with_any_aut_plus_cc_equivariant_bijection_count": len(unique_cc_twists),
        "distinct_aut_equivariant_bijection_count_across_all_twists": len(distinct_aut_maps),
        "distinct_aut_plus_cc_equivariant_bijection_count_across_all_twists": len(distinct_cc_maps),
        "unique_cc_compatible_twist_bits": list(unique_cc_twists[0]) if len(unique_cc_twists) == 1 else None,
        "unique_full_node_bijection_obtained": len(distinct_cc_maps) == 1,
        "candidate_summaries_with_signal": [x for x in candidate_summaries if x["aut_equivariant_bijection_count"] or x["aut_plus_cc_equivariant_bijection_count"]],
        "chosen_mapping_retained_labels_by_source_index": [chosen_map[i] for i in range(48)] if chosen_map is not None else None,
        "decision": {
            "az_g2_untwisted_semantic_identification_corrected": True,
            "g0_t12_g1_t13_and_six_sign_generators_kept_fixed": True,
            "next_exact_route": "LOCK_UNIQUE_SOURCE_TO_RETAINED_48NODE_ADAPTER_AND_TRANSLATE_V6_MASS_VECTOR_TO_SOURCE_NODE_COORDINATES" if len(distinct_cc_maps) == 1 else "USE_CT_OR_ANOTHER_SOURCE_BOUND_STRUCTURE_TO_BREAK_REMAINING_G2_TWIST_OR_NODE_MAP_AMBIGUITY",
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
