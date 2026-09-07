#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
BH_DIAG = HERE / "diagnose_stage32_post1648bh_exact_source_lifts_node_adapter.py"
BH_RESULT = HERE / "post1648bh-exact-source-lifts-node-adapter-scratch-result.json"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    bh = load_module(BH_DIAG, "s32_bi_bh")
    marking = bh.load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_bi_marking")
    bundle = bh.load_retained(ST33 / "picard_base_rows_retained.py", "s32_bi_base")
    adapter = bh.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    cc_action = Matrix(bundle["picard_action_cc_64x64"])

    p140 = bh.recover_known140_perm(coords, cc_action)
    ret_cc = bh.restrict_exceptional_perm140(p140)
    if bh.order(ret_cc) != 2:
        raise ValueError("retained exceptional cc is not an involution")

    fixed = [i for i in range(48) if ret_cc[i] == i]
    moving_pairs = []
    seen = set(fixed)
    for i in range(48):
        if i in seen:
            continue
        j = ret_cc[i]
        if j == i or ret_cc[j] != i:
            raise ValueError("retained cc cycle regression")
        moving_pairs.append((min(i, j), max(i, j)))
        seen.add(i)
        seen.add(j)
    moving_pairs = sorted(set(moving_pairs))
    if len(seen) != 48:
        raise ValueError("retained cc cycle coverage regression")

    v6 = json.loads(V6_PATH.read_text())
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    masses = pairings[92:]
    if len(masses) != 48 or sum(masses) != 266:
        raise ValueError("V6 exceptional mass regression")

    fixed_mass = sum(masses[i] for i in fixed)
    moving_mass = sum(masses[i] for i in range(48) if i not in set(fixed))
    if fixed_mass + moving_mass != 266:
        raise ValueError("V6 cc partition mass regression")

    pair_mass_records = [
        {
            "exceptional_labels_1based_within_48": [i + 1, j + 1],
            "known140_labels_1based": [i + 93, j + 93],
            "masses": [masses[i], masses[j]],
            "equal": masses[i] == masses[j],
        }
        for i, j in moving_pairs
    ]
    mismatches = [r for r in pair_mass_records if not r["equal"]]

    vcoords = Matrix([[int(x) for x in v6["witness"]["picard_coordinates"]]])
    cc_vcoords = vcoords * cc_action
    v6_cc_invariant = cc_vcoords == vcoords

    # Exact cross-check in the spanning known140 pairing representation.
    cc_pairing_replay = [pairings[p140[i]] for i in range(140)]
    all140_pairings_cc_invariant = cc_pairing_replay == pairings
    if v6_cc_invariant != all140_pairings_cc_invariant:
        raise ValueError("Picard64/all140 cc-invariance disagreement")
    if v6_cc_invariant and mismatches:
        raise ValueError("cc-invariant V6 class has unequal masses on a cc pair")

    bh_result = json.loads(BH_RESULT.read_text())
    if bh_result["distinct_full_aut_plus_cc_node_bijection_count"] <= 0:
        raise ValueError("BH did not materialize any cc-equivariant node bijection")
    if bh_result["unique_canonical_gauge_node_bijection_obtained"]:
        raise ValueError("BI is intended for the nonunique BH adapter case")

    # Any bijection f intertwining source and retained complex conjugation maps
    # Fix(cc_source) bijectively onto Fix(cc_retained). Therefore the total V6
    # mass on source-Q-fixed nodes is independent of which of the BH maps is used.
    cert = {
        "mode": "SCRATCH_POST1648BI_CC_FIXED_MASS_PARTITION",
        "source_locks": {
            "bh_result_path": str(BH_RESULT.relative_to(ROOT)),
            "v6_path": str(V6_PATH.relative_to(ROOT)),
            "v6_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "bh_distinct_cc_equivariant_node_bijections": bh_result["distinct_full_aut_plus_cc_node_bijection_count"],
        },
        "retained_complex_conjugation": {
            "fixed_exceptional_count": len(fixed),
            "moving_pair_count": len(moving_pairs),
            "fixed_exceptional_labels_1based_within_48": [i + 1 for i in fixed],
            "fixed_known140_labels_1based": [i + 93 for i in fixed],
            "moving_pairs": pair_mass_records,
        },
        "v6": {
            "exceptional_mass_total": 266,
            "mass_on_source_cc_fixed_Q_nodes": fixed_mass,
            "mass_on_source_cc_moving_Qi_nodes": moving_mass,
            "moving_cc_pair_mass_mismatch_count": len(mismatches),
            "moving_cc_pair_mass_mismatches": mismatches,
            "picard64_cc_invariant": v6_cc_invariant,
            "all140_pairings_cc_invariant": all140_pairings_cc_invariant,
        },
        "decision": {
            "q_fixed_vs_qi_moving_total_mass_partition_is_adapter_independent": True,
            "node_by_node_source_adapter_still_nonunique": True,
            "v6_gal_qi_over_q_invariance_obtained": v6_cc_invariant,
            "next_exact_route": (
                "IF_V6_CC_INVARIANT_USE_Q_FIXED_QI_MOVING_MASS_PARTITION_IN_LOCAL_BRANCH_GALOIS_CONSTRAINTS"
                if v6_cc_invariant
                else "V6_CLASS_IS_NOT_CC_INVARIANT_SO_DO_NOT_PROMOTE_Q_DEFINED_CARRIER_CONSTRAINTS_WITHOUT_A_SEPARATE_GALOIS_CLASS_ARGUMENT"
            ),
        },
        "firewalls": {
            "node_by_node_adapter_uniqueness_claimed": False,
            "full_Q_definedness_beyond_Gal_Qi_over_Q_claimed": False,
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
