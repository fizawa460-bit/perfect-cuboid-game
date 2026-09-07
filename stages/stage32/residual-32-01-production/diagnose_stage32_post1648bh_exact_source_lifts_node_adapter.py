#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
AZ_PATH = HERE / "diagnose_stage32_post1648az_full_48node_equivariant_bijection.py"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
sys.path.insert(0, str(HERE))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402
from pairing_prefix_engine import close_permutation_group  # noqa: E402


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


def inv(a: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(a)
    for i, x in enumerate(a):
        out[x] = i
    return tuple(out)


def power(a: tuple[int, ...], n: int) -> tuple[int, ...]:
    r = tuple(range(len(a)))
    for _ in range(n):
        r = compose(a, r)
    return r


def order(a: tuple[int, ...], cap: int = 64) -> int:
    r = tuple(range(len(a)))
    for n in range(1, cap + 1):
        r = compose(a, r)
        if all(r[i] == i for i in range(len(a))):
            return n
    raise ValueError("order cap exceeded")


def restrict_exceptional_from_140(g140: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for i in range(92, 140):
        y = g140[i]
        if not 92 <= y < 140:
            raise ValueError("140-action exits exceptional 48")
        out.append(y - 92)
    return tuple(out)


def recover_known140_perm(coords: Matrix, action: Matrix) -> list[int]:
    lut = {tuple(int(coords[i, j]) for j in range(64)): i for i in range(140)}
    if len(lut) != 140:
        raise ValueError("known140 coordinate rows not unique")
    out = []
    for i in range(140):
        r = Matrix([[int(coords[i, j]) for j in range(64)]]) * action
        key = tuple(int(r[0, j]) for j in range(64))
        if key not in lut:
            raise ValueError(f"action exits known140 at {i}")
        out.append(lut[key])
    if sorted(out) != list(range(140)):
        raise ValueError("known140 action not bijective")
    return out


def restrict_exceptional_perm140(p140: list[int]) -> tuple[int, ...]:
    out = []
    for i in range(92, 140):
        y = p140[i]
        if not 92 <= y < 140:
            raise ValueError("known140 permutation exits exceptional 48")
        out.append(y - 92)
    return tuple(out)


def block_perm(blocks: list[set[int]], g: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for b in blocks:
        ib = {g[i] for i in b}
        hits = [j for j, c in enumerate(blocks) if ib == c]
        if len(hits) != 1:
            raise ValueError(f"block image ambiguity: {hits}")
        out.append(hits[0])
    return tuple(out)


def source_cc_perm(az, nodes):
    idx = {v: i for i, v in enumerate(nodes)}
    return tuple(idx[az.canon(tuple(z.conjugate() for z in v))] for v in nodes)


def product_from_bits(gens: list[tuple[int, ...]], bits: tuple[int, ...]) -> tuple[int, ...]:
    r = tuple(range(len(gens[0])))
    for j, bit in enumerate(bits):
        if bit:
            r = compose(gens[j], r)
    return r


def kernel_lookup(gens: list[tuple[int, ...]]) -> dict[tuple[int, ...], tuple[int, ...]]:
    out = {}
    for bits in itertools.product((0, 1), repeat=len(gens)):
        g = product_from_bits(gens, bits)
        if g in out and out[g] != bits:
            raise ValueError("kernel basis dependent")
        out[g] = bits
    if len(out) != 2 ** len(gens):
        raise ValueError("kernel cardinality regression")
    return out


def translate_ret_kernel_bits_to_source_raw_order(bits_raw_g3_to_g8: tuple[int, ...], source_raw_signs: list[tuple[int, ...]]) -> tuple[int, ...]:
    return product_from_bits(source_raw_signs, bits_raw_g3_to_g8)


def quotient_word(qgens: list[tuple[int, ...]], word: tuple[int, ...]) -> tuple[int, ...]:
    r = tuple(range(4))
    for j in word:
        r = compose(qgens[j], r)
    return r


def group_word(gens: list[tuple[int, ...]], word: tuple[int, ...]) -> tuple[int, ...]:
    r = tuple(range(len(gens[0])))
    for j in word:
        r = compose(gens[j], r)
    return r


def propagate(src_gens, ret_gens, s0: int, e0: int):
    f = {s0: e0}
    invf = {e0: s0}
    queue = [s0]
    while queue:
        s = queue.pop()
        e = f[s]
        for sg, rg in zip(src_gens, ret_gens):
            s2 = sg[s]
            e2 = rg[e]
            if s2 in f and f[s2] != e2:
                return None
            if e2 in invf and invf[e2] != s2:
                return None
            if s2 not in f:
                f[s2] = e2
                invf[e2] = s2
                queue.append(s2)
    if len(f) != 48 or set(f.values()) != set(range(48)):
        return None
    return f


def main() -> None:
    az = load_module(AZ_PATH, "s32_bh_az")
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_bh_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_bh_base")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)

    raw140 = [tuple(x - 1 for x in g) for g in marking["aut_action"]["permutations_1based"]]
    raw = [restrict_exceptional_from_140(g) for g in raw140]
    if len(raw) != 9:
        raise ValueError("retained generator count regression")
    ret_cc = restrict_exceptional_perm140(recover_known140_perm(coords, Matrix(bundle["picard_action_cc_64x64"])))

    # Canonical representative of the six BG Galois-cocycle-compatible semantic
    # assignments.  The other five differ by simultaneous source side-index S3.
    # retained W0,W1,W2,W3 -> source a1,a2,c,a3
    # retained Z0,Z1,Z2 -> source b2,b1,b3
    ret_to_src_w = (0, 1, 3, 2)
    ret_to_src_z = (1, 0, 2)

    nodes = az.source_nodes()
    if len(nodes) != 48:
        raise ValueError("source node count regression")
    source_cc = source_cc_perm(az, nodes)
    source_base_generators = [
        az.perm_from_map(nodes, "t12"),
        az.perm_from_map(nodes, "t13"),
        az.perm_from_map(nodes, "sigma"),
    ] + [az.perm_from_map(nodes, f"sign_{k}") for k in range(6)]
    SG = close_permutation_group([tuple(x + 1 for x in g) for g in source_base_generators])
    SG0 = [tuple(x for x in g) for g in SG]
    if len(SG0) != 1536:
        raise ValueError("source group order regression")

    # Source W hyperplanes in semantic order a1,a2,a3,c.
    source_W = [{i for i, v in enumerate(nodes) if v[k] == 0} for k in (0, 1, 2, 6)]
    by_wp: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for g in SG0:
        by_wp[block_perm(source_W, g)].append(g)
    if len(by_wp) != 24 or {len(v) for v in by_wp.values()} != {64}:
        raise ValueError("source S4 quotient regression")

    # Translate retained W quotient permutations into source W order.
    ret_q = [
        (1, 0, 2, 3),  # raw g0 swaps W0/W1 -> source a1/a2
        (2, 1, 0, 3),  # raw g1 swaps W0/W2 -> source a1/c
        (3, 1, 2, 0),  # raw g2 swaps W0/W3 -> source a1/a3
    ]
    def translate_q(q):
        out = [None] * 4
        for r in range(4):
            out[ret_to_src_w[r]] = ret_to_src_w[q[r]]
        return tuple(int(x) for x in out)
    source_q = [translate_q(q) for q in ret_q]
    expected_source_q = [
        (1, 0, 2, 3),
        (3, 1, 2, 0),
        (2, 1, 0, 3),
    ]
    if source_q != expected_source_q:
        raise ValueError(f"canonical quotient translation regression: {source_q}")

    # Translate raw retained sign generators g3..g8 to source sign actions.
    # Source sign basis indices are a1,a2,a3,b1,b2,b3; sign(c) is projectively
    # the product of all six non-c signs.
    src_sign_basis = [az.perm_from_map(nodes, f"sign_{k}") for k in range(6)]
    all6 = product_from_bits(src_sign_basis, (1, 1, 1, 1, 1, 1))
    source_raw_signs = [
        src_sign_basis[0],  # g3: W0=a1
        src_sign_basis[1],  # g4: W1=a2
        all6,              # g5: W2=c
        src_sign_basis[4],  # g6: Z0=b2
        src_sign_basis[3],  # g7: Z1=b1
        src_sign_basis[5],  # g8: Z2=b3
    ]
    ret_kernel_gens = raw[3:9]
    ret_kernel = kernel_lookup(ret_kernel_gens)
    source_translated_kernel = kernel_lookup(source_raw_signs)
    if len(ret_kernel) != 64 or len(source_translated_kernel) != 64:
        raise ValueError("translated sign kernel regression")

    # Candidate lifts must lie in the exact source quotient coset and have the
    # same order as the retained raw generator (all three are involutions).
    candidate_lists = []
    for j in range(3):
        oret = order(raw[j])
        cand = [g for g in by_wp[source_q[j]] if order(g) == oret]
        candidate_lists.append(cand)
    candidate_counts = [len(x) for x in candidate_lists]
    if any(n == 0 for n in candidate_counts):
        raise ValueError(f"empty source lift candidate coset: {candidate_counts}")

    # Build exact short-word kernel relations from retained g0,g1,g2.
    # Every quotient-trivial word of length <= 8 is converted to exact raw
    # sign-kernel bits and must be reproduced by the source candidates.
    qgens = source_q
    retained_short_relations = []
    seen_rel = set()
    for L in range(1, 9):
        for word in itertools.product(range(3), repeat=L):
            if quotient_word(qgens, word) != (0, 1, 2, 3):
                continue
            rg = group_word(raw[:3], word)
            if rg not in ret_kernel:
                raise ValueError(f"quotient-trivial retained word exits sign kernel: {word}")
            bits = ret_kernel[rg]
            sk = translate_ret_kernel_bits_to_source_raw_order(bits, source_raw_signs)
            key = (word, sk)
            if key not in seen_rel:
                retained_short_relations.append((word, sk, bits))
                seen_rel.add(key)
    if not retained_short_relations:
        raise ValueError("no short kernel relations materialized")

    # Progressive exact triple filtering.
    triples = list(itertools.product(*candidate_lists))
    initial_triple_count = len(triples)
    relation_filter_trace = []
    for word, want, bits in retained_short_relations:
        triples = [t for t in triples if group_word(list(t), word) == want]
        relation_filter_trace.append({
            "word": list(word),
            "retained_kernel_bits_g3_to_g8": list(bits),
            "surviving_triples": len(triples),
        })
        if not triples:
            break
    if not triples:
        raise ValueError("exact short-word relations eliminate all source lift triples")

    # For each relation-compatible triple, match all nine generators and require
    # full 48-node bijection plus actual complex-conjugation equivariance.
    full_hits = []
    for triple in triples:
        src9 = list(triple) + source_raw_signs
        for e0 in range(48):
            f = propagate(src9, raw, 0, e0)
            if f is None:
                continue
            cc_ok = all(f[source_cc[s]] == ret_cc[f[s]] for s in range(48))
            if cc_ok:
                full_hits.append((triple, f))

    def fmap_key(f):
        return tuple(f[i] for i in range(48))
    distinct_maps = {}
    for triple, f in full_hits:
        distinct_maps[fmap_key(f)] = (triple, f)

    # All six BG semantic assignments should differ only by simultaneous source
    # side-index S3 gauge, so one canonical-gauge map is sufficient for source
    # coordinate records; no claim of intrinsic side-index naming is made.
    unique_canonical_gauge_map = len(distinct_maps) == 1
    chosen_triple = chosen_map = None
    if unique_canonical_gauge_map:
        chosen_triple, chosen_map = next(iter(distinct_maps.values()))

    v6 = json.loads(V6_PATH.read_text())
    masses = [int(x) for x in v6["witness"]["all140_pairings"]][92:]
    if len(masses) != 48 or sum(masses) != 266:
        raise ValueError("V6 exceptional mass regression")

    records = []
    if chosen_map is not None:
        names = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
        for s in range(48):
            e0 = chosen_map[s]
            v = nodes[s]
            records.append({
                "source_node_index_zero_based": s,
                "source_coordinates_a1_a2_a3_b1_b2_b3_c": [az.fmt(z) for z in v],
                "source_zero_coordinates": [names[k] for k, z in enumerate(v) if z == 0],
                "source_cc_fixed": source_cc[s] == s,
                "retained_exceptional_label_1based": e0 + 93,
                "v6_exceptional_intersection_multiplicity": masses[e0],
            })

    source_Q_mass = None
    source_Qi_mass = None
    if records:
        source_Q_mass = sum(r["v6_exceptional_intersection_multiplicity"] for r in records if r["source_cc_fixed"])
        source_Qi_mass = 266 - source_Q_mass

    print(json.dumps({
        "mode": "SCRATCH_POST1648BH_EXACT_SOURCE_LIFTS_NODE_ADAPTER",
        "canonical_BG_semantic_gauge": {
            "retained_W0_W1_W2_W3_to_source_a1_a2_a3_c_indices": list(ret_to_src_w),
            "retained_Z0_Z1_Z2_to_source_b1_b2_b3_indices": list(ret_to_src_z),
            "retained_W2_identified_with_source_c": True,
            "remaining_five_BG_assignments_are_source_side_index_S3_gauge": True,
        },
        "source_quotient_permutations_for_raw_g0_g1_g2": [list(x) for x in source_q],
        "source_lift_involutive_candidate_counts": candidate_counts,
        "initial_source_lift_triple_count": initial_triple_count,
        "short_kernel_relation_count": len(retained_short_relations),
        "relation_filter_trace": relation_filter_trace,
        "relation_compatible_source_lift_triple_count": len(triples),
        "full_aut_plus_cc_hit_count_with_basepoints": len(full_hits),
        "distinct_full_aut_plus_cc_node_bijection_count": len(distinct_maps),
        "unique_canonical_gauge_node_bijection_obtained": unique_canonical_gauge_map,
        "chosen_source_lift_orders": [order(g) for g in chosen_triple] if chosen_triple is not None else None,
        "v6": {
            "exceptional_mass_total": sum(masses),
            "mass_on_source_cc_fixed_Q_nodes": source_Q_mass,
            "mass_on_source_cc_moving_Qi_nodes": source_Qi_mass,
        },
        "records": records,
        "decision": {
            "full_48node_source_adapter_mod_source_S3_naming_gauge_obtained": unique_canonical_gauge_map,
            "next_exact_route": "LOCK_THE_NODE_ADAPTER_AND_TEST_V6_SOURCE_NODE_MULTIPLICITIES_AGAINST_LOCAL_BRANCH_TANGENT/GALOIS_CONSTRAINTS" if unique_canonical_gauge_map else "ADD_LONGER_GROUP_RELATIONS_OR_KNOWN_CURVE_INCIDENCE_TO_RESOLVE_REMAINING_SOURCE_LIFT_OR_NODE_MAP_AMBIGUITY",
        },
        "firewalls": {
            "source_side_index_S3_gauge_not_promoted_to_intrinsic_label_uniqueness": True,
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
