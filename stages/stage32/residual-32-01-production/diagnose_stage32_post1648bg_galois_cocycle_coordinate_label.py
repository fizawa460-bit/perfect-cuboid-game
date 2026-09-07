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


def commutator_involution_left(c: tuple[int, ...], g: tuple[int, ...]) -> tuple[int, ...]:
    # c*g*c^{-1}*g^{-1}; c is involutive but use general inverse for g.
    return compose(c, compose(g, compose(inv(c), inv(g))))


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
    return out


def restrict_exceptional(p140: list[int]) -> tuple[int, ...]:
    if any(p140[i] < 92 or p140[i] >= 140 for i in range(92, 140)):
        raise ValueError("known140 action does not preserve exceptional 48")
    return tuple(p140[i] - 92 for i in range(92, 140))


def restrict_raw_exceptional(g140: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for i in range(92, 140):
        y = g140[i]
        if not (92 <= y < 140):
            raise ValueError("raw automorphism exits exceptional 48")
        out.append(y - 92)
    return tuple(out)


def product_bits(gens: list[tuple[int, ...]]) -> dict[tuple[int, ...], tuple[int, ...]]:
    n = len(gens[0])
    I = tuple(range(n))
    out = {}
    for bits in itertools.product((0, 1), repeat=len(gens)):
        g = I
        for j, bit in enumerate(bits):
            if bit:
                g = compose(gens[j], g)
        if g in out and out[g] != bits:
            raise ValueError("kernel generators not independent")
        out[g] = bits
    return out


def block_perm_zero(blocks: list[set[int]], g: tuple[int, ...]) -> tuple[int, ...]:
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


def source_w_perm_from_ret(wp_ret: tuple[int, ...], ret_to_src: tuple[int, ...]) -> tuple[int, ...]:
    # ret_to_src maps retained W index -> source W index in [a1,a2,a3,c].
    out = [None] * 4
    for r in range(4):
        out[ret_to_src[r]] = ret_to_src[wp_ret[r]]
    return tuple(int(x) for x in out)


def induced_z_map(ret_to_src_w: tuple[int, ...]) -> tuple[int, ...]:
    # Retained Z matchings in recovered W order.
    ret_matchings = [
        {frozenset((0, 3)), frozenset((1, 2))},
        {frozenset((0, 2)), frozenset((1, 3))},
        {frozenset((0, 1)), frozenset((2, 3))},
    ]
    # Source b1,b2,b3 matchings on source W=[a1,a2,a3,c]=[0,1,2,3].
    src_matchings = [
        {frozenset((0, 3)), frozenset((1, 2))},
        {frozenset((1, 3)), frozenset((0, 2))},
        {frozenset((2, 3)), frozenset((0, 1))},
    ]
    out = []
    for m in ret_matchings:
        sm = {frozenset(ret_to_src_w[x] for x in pair) for pair in m}
        hits = [j for j, q in enumerate(src_matchings) if sm == q]
        if len(hits) != 1:
            raise ValueError(f"induced Z map ambiguity: {sm}, {hits}")
        out.append(hits[0])
    return tuple(out)


def translate_ret_kernel_bits_to_source(
    bits_ret6: tuple[int, ...], ret_to_src_w: tuple[int, ...], ret_to_src_z: tuple[int, ...]
) -> tuple[int, ...]:
    # Retained abstract bit order: Z0,Z1,Z2,W0,W1,W2 with W3 gauge 0.
    r7 = list(bits_ret6[:3]) + list(bits_ret6[3:]) + [0]
    # Source full order a1,a2,a3,b1,b2,b3,c.
    s7 = [0] * 7
    # Z signs -> b1,b2,b3 positions 3..5.
    for rz in range(3):
        s7[3 + ret_to_src_z[rz]] = r7[rz]
    # W signs -> a1,a2,a3,c positions 0,1,2,6.
    src_w_pos = [0, 1, 2, 6]
    for rw in range(4):
        s7[src_w_pos[ret_to_src_w[rw]]] = r7[3 + rw]
    # Normalize projectively to c-sign 0 by global sign.
    if s7[6]:
        s7 = [x ^ 1 for x in s7]
    # Source six-bit basis order used below: a1,a2,a3,b1,b2,b3.
    return tuple(s7[:6])


def main() -> None:
    az = load_module(AZ_PATH, "s32_bg_az")
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_bg_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_bg_base")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)

    raw140 = [tuple(x - 1 for x in g) for g in marking["aut_action"]["permutations_1based"]]
    raw = [restrict_raw_exceptional(g) for g in raw140]
    if len(raw) != 9:
        raise ValueError("retained raw generator count regression")
    cc_ret = restrict_exceptional(recover_known140_perm(coords, Matrix(bundle["picard_action_cc_64x64"])))

    # Recovered retained sign basis in abstract coordinate order Z0,Z1,Z2,W0,W1,W2.
    ret_sign_gens = [raw[6], raw[7], raw[8], raw[3], raw[4], raw[5]]
    ret_kernel_lookup = product_bits(ret_sign_gens)
    if len(ret_kernel_lookup) != 64:
        raise ValueError("retained sign kernel order regression")

    raw_comm_bits = []
    for j in range(3):
        c = commutator_involution_left(cc_ret, raw[j])
        if c not in ret_kernel_lookup:
            raise ValueError(f"retained cc commutator for raw g{j} not in sign kernel")
        raw_comm_bits.append(ret_kernel_lookup[c])

    # Source node action and source sign-kernel coordinate system.
    nodes = az.source_nodes()
    t12 = az.perm_from_map(nodes, "t12")
    t13 = az.perm_from_map(nodes, "t13")
    sigma = az.perm_from_map(nodes, "sigma")
    sigma13 = az.perm_conjugate(t13, sigma)
    source_sign_gens = [az.perm_from_map(nodes, f"sign_{k}") for k in range(6)]
    src_kernel_lookup = product_bits(source_sign_gens)
    if len(src_kernel_lookup) != 64:
        raise ValueError("source sign kernel order regression")
    scc = source_cc_perm(az, nodes)

    source_gens = [t12, t13, sigma13] + source_sign_gens
    SG = close_permutation_group([tuple(x + 1 for x in g) for g in source_gens])
    if len(SG) != 1536:
        raise ValueError(f"source group order regression: {len(SG)}")
    SG0 = [tuple(x for x in g) for g in SG]

    # Source W hyperplanes a1,a2,a3,c.
    sw = [
        {i for i, v in enumerate(nodes) if v[k] == 0}
        for k in (0, 1, 2, 6)
    ]
    source_by_wp: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for g in SG0:
        source_by_wp[block_perm_zero(sw, g)].append(g)
    if len(source_by_wp) != 24 or {len(v) for v in source_by_wp.values()} != {64}:
        raise ValueError("source S4 quotient/coset size regression")

    # The cc commutator is constant on each quotient coset because cc fixes the
    # source sign kernel pointwise.  Recover that quotient 1-cocycle exactly.
    source_comm_by_wp = {}
    for wp, els in source_by_wp.items():
        vals = set()
        for g in els:
            c = commutator_involution_left(scc, g)
            if c not in src_kernel_lookup:
                raise ValueError("source cc commutator exits sign kernel")
            vals.add(src_kernel_lookup[c])
        if len(vals) != 1:
            raise ValueError(f"source cc commutator not constant on quotient coset {wp}: {vals}")
        source_comm_by_wp[wp] = next(iter(vals))

    raw_wp_ret = [
        (1, 0, 2, 3),
        (2, 1, 0, 3),
        (3, 1, 2, 0),
    ]

    assignment_records = []
    survivors = []
    for ret_to_src_w in itertools.permutations(range(4)):
        ret_to_src_z = induced_z_map(ret_to_src_w)
        translated = [
            translate_ret_kernel_bits_to_source(bits, ret_to_src_w, ret_to_src_z)
            for bits in raw_comm_bits
        ]
        src_wps = [source_w_perm_from_ret(wp, ret_to_src_w) for wp in raw_wp_ret]
        expected = [source_comm_by_wp[wp] for wp in src_wps]
        ok = translated == expected
        rec = {
            "retained_W0_W1_W2_W3_to_source_a1_a2_a3_c_indices": list(ret_to_src_w),
            "retained_Z0_Z1_Z2_to_source_b1_b2_b3_indices": list(ret_to_src_z),
            "retained_cc_commutator_bits_translated_to_source_a1_a2_a3_b1_b2_b3": [list(x) for x in translated],
            "source_expected_cc_commutator_bits_for_same_S4_quotient_elements": [list(x) for x in expected],
            "matches": ok,
        }
        assignment_records.append(rec)
        if ok:
            survivors.append(rec)

    print(json.dumps({
        "mode": "SCRATCH_POST1648BG_GALOIS_COCYCLE_COORDINATE_LABEL",
        "retained_raw_g0_g1_g2_cc_commutator_bits_abstract_Z0_Z1_Z2_W0_W1_W2": [list(x) for x in raw_comm_bits],
        "semantic_W_label_assignment_count_tested": len(assignment_records),
        "galois_cocycle_compatible_assignment_count": len(survivors),
        "survivors": survivors,
        "all_assignment_records": assignment_records,
        "decision": {
            "previous_AZ_fixed_W_semantic_order_was_source_unlocked": True,
            "galois_cocycle_used_instead_of_fixed_point_signature_only": True,
            "next_exact_route": "FOR_EACH_SURVIVING_COORDINATE_LABEL_ASSIGNMENT_SOLVE_EXACT_SOURCE_LIFTS_OF_RAW_G0_G1_G2_AND_FULL_48NODE_BIJECTION" if survivors else "RECHECK_SOURCE_SIGMA_FORMULA_OR_RETAINED_SIGN_KERNEL_BASIS_BEFORE_ANY_NODE_LABEL_CREDIT",
        },
        "firewalls": {
            "runner_side_import_only": True,
            "giant_retained_payload_whole_fetch_used": False,
            "unique_48node_bijection_obtained": False,
            "v6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
            "scratch_only": True,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
