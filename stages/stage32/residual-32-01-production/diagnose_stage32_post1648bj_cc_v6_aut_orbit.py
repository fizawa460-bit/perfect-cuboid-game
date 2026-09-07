#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import deque
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
BI_RESULT = HERE / "post1648bi-cc-fixed-mass-partition-scratch-result.json"

sys.path.insert(0, str(HERE))
from hperp_integral_adapter import (  # noqa: E402
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def row_tuple(v: Matrix) -> tuple[int, ...]:
    if v.rows != 1:
        raise ValueError("expected row vector")
    return tuple(int(v[0, j]) for j in range(v.cols))


def matrix_rows(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_bj_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_bj_base")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    gram = Matrix(bundle["picard_gram_64x64"])
    cc = Matrix(bundle["picard_action_cc_64x64"])

    raw_perms = marking["aut_action"]["permutations_1based"]
    if len(raw_perms) != 9:
        raise ValueError("Aut generator count regression")
    basis_idx = [x - 1 for x in RETAINED_BASIS_KNOWN_LABELS_1BASED]

    # If p sends known curve C_i to C_{p(i)}, then the j-th retained basis
    # class maps to the known140 coordinate row of p(basis_j). Therefore the
    # rows below are the exact Picard64 row-action matrix for that generator.
    gen_actions: list[Matrix] = []
    for gi, p1 in enumerate(raw_perms):
        p = [int(x) - 1 for x in p1]
        rows = [list(coords[p[i], :]) for i in basis_idx]
        A = Matrix(rows)
        if A.shape != (64, 64):
            raise ValueError(f"Aut action shape regression at generator {gi}")
        if A * gram * A.T != gram:
            raise ValueError(f"Aut Picard action isometry regression at generator {gi}")
        gen_actions.append(A)

    # Cross-check one generator on every known140 class.
    for gi, (p1, A) in enumerate(zip(raw_perms, gen_actions)):
        p = [int(x) - 1 for x in p1]
        for i in range(140):
            lhs = Matrix([[int(coords[i, j]) for j in range(64)]]) * A
            rhs = Matrix([[int(coords[p[i], j]) for j in range(64)]])
            if lhs != rhs:
                raise ValueError(f"known140 action reconstruction mismatch g{gi} row {i}")

    v6 = json.loads(V6_PATH.read_text())
    if v6["canonical_sha256_without_this_field"] != "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8":
        raise ValueError("V6 canonical regression")
    v = Matrix([[int(x) for x in v6["witness"]["picard_coordinates"]]])
    ccv = v * cc
    if ccv == v:
        raise ValueError("BI regression: V6 unexpectedly cc-invariant")

    # Exact Aut orbit BFS. Record a shortest generator word from V6 to each
    # orbit element. Expected full group order is 1536, so this is bounded.
    start = row_tuple(v)
    target = row_tuple(ccv)
    q = deque([start])
    word_of: dict[tuple[int, ...], tuple[int, ...]] = {start: ()}
    while q:
        cur = q.popleft()
        curM = Matrix([list(cur)])
        w = word_of[cur]
        for gi, A in enumerate(gen_actions):
            nxt = row_tuple(curM * A)
            if nxt not in word_of:
                word_of[nxt] = w + (gi,)
                q.append(nxt)
                if len(word_of) > 1536:
                    raise ValueError("Aut class orbit exceeds retained group order")

    in_orbit = target in word_of
    hit_word = list(word_of[target]) if in_orbit else None

    # Count exact Aut elements sending V6 to cc(V6), not merely distinct orbit
    # classes. Close the retained permutation group and reconstruct each class
    # action from its action on the retained basis labels.
    from pairing_prefix_engine import close_permutation_group
    group_perms = close_permutation_group(raw_perms)
    if len(group_perms) != 1536:
        raise ValueError("Aut group order regression")
    hit_count = 0
    first_hit_basis_images = None
    for gp1 in group_perms:
        gp = [int(x) - 1 for x in gp1]
        A = Matrix([list(coords[gp[i], :]) for i in basis_idx])
        if row_tuple(v * A) == target:
            hit_count += 1
            if first_hit_basis_images is None:
                first_hit_basis_images = [gp[i] + 1 for i in basis_idx]

    if in_orbit != (hit_count > 0):
        raise ValueError("BFS orbit / full Aut hit disagreement")
    orbit_size = len(word_of)
    stabilizer_size = 1536 // orbit_size if 1536 % orbit_size == 0 else None
    if stabilizer_size is None or hit_count not in (0, stabilizer_size):
        raise ValueError(
            f"orbit-stabilizer regression: orbit={orbit_size}, stab={stabilizer_size}, hits={hit_count}"
        )

    # cc is an involutive Picard isometry. Check whether cc normalizes the
    # reconstructed Aut generator subgroup at class-action level by conjugating
    # each generator and testing its action on V6-orbit classes.
    cc2 = cc * cc
    if cc2 != Matrix.eye(64):
        raise ValueError("cc action is not involutive")

    bi = json.loads(BI_RESULT.read_text())
    if bi["v6"]["picard64_cc_invariant"] is not False:
        raise ValueError("BI source regression")

    cert = {
        "mode": "SCRATCH_POST1648BJ_CC_V6_AUT_ORBIT",
        "source_locks": {
            "v6_path": str(V6_PATH.relative_to(ROOT)),
            "v6_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "bi_result_path": str(BI_RESULT.relative_to(ROOT)),
            "bi_v6_cc_invariant": bi["v6"]["picard64_cc_invariant"],
            "hperp_adapter_canonical_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "retained_aut_group_order": 1536,
        },
        "exact_aut_orbit": {
            "orbit_size": orbit_size,
            "stabilizer_size": stabilizer_size,
            "cc_v6_in_aut_orbit": in_orbit,
            "aut_elements_sending_v6_to_cc_v6": hit_count,
            "shortest_raw_generator_word_zero_based": hit_word,
            "shortest_raw_generator_word_length": None if hit_word is None else len(hit_word),
            "first_hit_retained_basis_images_known140_1based": first_hit_basis_images,
        },
        "decision": {
            "v6_cc_noninvariance_is_only_pointwise_not_aut_orbit_separation": in_orbit,
            "semilinear_cc_aut_stabilizer_available": in_orbit,
            "next_exact_route": (
                "MATERIALIZE_A_SHORTEST_AUT_ELEMENT_A_WITH_A_V6=CC_V6_THEN_STUDY_THE_SEMILINEAR_INVOLUTION_A_INV_CC_ON_THE_V6_LINEAR_SYSTEM_AND_NORMALIZATION_BRANCHES"
                if in_orbit
                else "CC_V6_LEAVES_THE_RETAINED_AUT_ORBIT_OF_V6;_DO_NOT_USE_AUT_TO_REPAIR_Q_DEFINEDNESS_AND_RETURN_TO_MEMBER_LEVEL_NONBIJECTIVITY_GEOMETRY"
            ),
        },
        "firewalls": {
            "aut_orbit_equivalence_promoted_to_Q_defined_member": False,
            "semilinear_class_stabilizer_promoted_to_member_stabilizer": False,
            "integral_genus1_carrier_materialized": False,
            "v6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
            "scratch_only": True,
            "runner_side_import_only": True,
            "giant_retained_payload_whole_fetch_used": False,
        },
    }
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
