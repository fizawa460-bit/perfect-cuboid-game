#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
sys.path.insert(0, str(HERE))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def row_tuple(m: Matrix, i: int) -> tuple[int, ...]:
    return tuple(int(m[i, j]) for j in range(m.cols))


def cycle_lengths(perm: list[int]) -> list[int]:
    seen = set()
    out = []
    for i in range(len(perm)):
        if i in seen:
            continue
        j = i
        n = 0
        while j not in seen:
            seen.add(j)
            n += 1
            j = perm[j]
        out.append(n)
    return sorted(out)


def recover_perm(coords: Matrix, action: Matrix) -> dict:
    lut: dict[tuple[int, ...], list[int]] = {}
    for i in range(coords.rows):
        lut.setdefault(row_tuple(coords, i), []).append(i)

    candidates = []
    for name, A in (("row_times_action", action), ("row_times_action_transpose", action.T)):
        perm = []
        ambiguous = []
        misses = []
        for i in range(coords.rows):
            r = Matrix([list(row_tuple(coords, i))]) * A
            key = tuple(int(r[0, j]) for j in range(r.cols))
            hits = lut.get(key, [])
            if len(hits) == 1:
                perm.append(hits[0])
            else:
                perm.append(-1)
                if not hits:
                    misses.append(i)
                else:
                    ambiguous.append({"source": i, "hits": hits})
        candidates.append({
            "orientation": name,
            "match_count": sum(x >= 0 for x in perm),
            "miss_count": len(misses),
            "ambiguous_count": len(ambiguous),
            "is_bijection": sorted(x for x in perm if x >= 0) == list(range(coords.rows)),
            "perm": perm,
            "misses": misses[:20],
            "ambiguous": ambiguous[:20],
        })
    good = [x for x in candidates if x["match_count"] == coords.rows and x["is_bijection"]]
    if len(good) != 1:
        raise ValueError(f"expected unique action orientation preserving known140, got {[(x['orientation'],x['match_count'],x['is_bijection']) for x in candidates]}")
    return {"chosen": good[0], "candidates": [{k: v for k, v in x.items() if k != "perm"} for x in candidates]}


def exceptional_summary(perm140: list[int]) -> dict:
    # known140 labels 93..140 are the 48 exceptional curves.
    ex = list(range(92, 140))
    if any(perm140[i] not in ex for i in ex):
        raise ValueError("action does not preserve exceptional 48")
    p48 = [perm140[i] - 92 for i in ex]
    cyc = cycle_lengths(p48)
    return {
        "perm_exceptional_labels_1based": [x + 93 for x in p48],
        "fixed_exceptional_labels_1based": [93 + i for i, x in enumerate(p48) if x == i],
        "fixed_count": sum(x == i for i, x in enumerate(p48)),
        "cycle_length_histogram": dict(sorted(Counter(cyc).items())),
        "is_involution": all(p48[p48[i]] == i for i in range(48)),
    }


def main() -> None:
    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_bc_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "s32_bc_base")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    if coords.shape != (140, 64):
        raise ValueError(f"known140 coordinate shape regression: {coords.shape}")

    cc = Matrix(bundle["picard_action_cc_64x64"])
    ct = Matrix(bundle["picard_action_ct_64x64"])
    if cc.shape != (64, 64) or ct.shape != (64, 64):
        raise ValueError("Picard action matrix shape regression")

    cc_rec = recover_perm(coords, cc)
    ct_rec = recover_perm(coords, ct)
    cc_perm = cc_rec["chosen"]["perm"]
    ct_perm = ct_rec["chosen"]["perm"]
    cc_ex = exceptional_summary(cc_perm)
    ct_ex = exceptional_summary(ct_perm)

    # Stoll--Testa list: among 48 exceptional curves, 24 are defined over Q and
    # 24 over Q(i).  Complex conjugation therefore has 24 fixed curves and 12
    # transposed pairs on the remaining 24.  We do not identify 'cc' semantically
    # until this exact cycle signature is observed.
    cc_matches_stoll_testa_complex_conjugation = (
        cc_ex["fixed_count"] == 24
        and cc_ex["cycle_length_histogram"] == {1: 24, 2: 12}
        and cc_ex["is_involution"]
    )

    print(json.dumps({
        "mode": "SCRATCH_POST1648BC_CC_EXCEPTIONAL_PERMUTATION_RECOVERY",
        "known140_coordinate_shape": [coords.rows, coords.cols],
        "cc": {
            "orientation": cc_rec["chosen"]["orientation"],
            "orientation_candidates": cc_rec["candidates"],
            "known140_cycle_length_histogram": dict(sorted(Counter(cycle_lengths(cc_perm)).items())),
            "exceptional": cc_ex,
            "matches_stoll_testa_24Q_24Qi_signature": cc_matches_stoll_testa_complex_conjugation,
        },
        "ct": {
            "orientation": ct_rec["chosen"]["orientation"],
            "orientation_candidates": ct_rec["candidates"],
            "known140_cycle_length_histogram": dict(sorted(Counter(cycle_lengths(ct_perm)).items())),
            "exceptional": ct_ex,
        },
        "source_reference_lock": {
            "paper": "Michael Stoll and Damiano Testa, The surface parametrizing cuboids, arXiv:1009.0388",
            "fact": "48 exceptional curves: 24 defined over Q, 24 defined over Q(i)",
            "paper_section": "Section 3 list of known curves, item (1)",
        },
        "decision": {
            "retained_cc_identified_as_complex_conjugation_on_exceptional_nodes": cc_matches_stoll_testa_complex_conjugation,
            "next_exact_route": "COUPLE_RETAINED_CC_EXCEPTIONAL_PERMUTATION_WITH_THE_16_AZ_EQUIVARIANT_BIJECTIONS_AND_SOURCE_COORDINATE_COMPLEX_CONJUGATION",
        },
        "firewalls": {
            "runner_side_import_only": True,
            "giant_retained_payload_whole_fetch_used": False,
            "explicit_unique_48node_bijection_obtained": False,
            "v6_carrier_excluded": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
            "scratch_only": True,
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
