#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import pathlib

from sympy import Matrix

from direct_picard_slice_stabilizer_orbit_bound import DirectPicardSliceStabilizerOrbitBound
from hperp_integral_adapter import HperpIntegralPairingAdapter


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module_payload(path: pathlib.Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--marking", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    bundle = load_module_payload(args.retained, "stage32_orbit_rank_picard")
    marking = load_module_payload(args.marking, "stage32_orbit_rank_marking")
    model = DirectPicardSliceStabilizerOrbitBound.from_retained(marking, bundle)
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = model.bound.bridge
    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])
    if phi.rank() != 3:
        raise ValueError("slice rank regression")

    nonfixed = [r for r in model.rules if not r.fixed_on_slice]
    rows = []
    for r in nonfixed:
        idx = [v - 1 for v in r.known_curve_labels_1based]
        rows.append([sum(int(adapter.pairing_matrix[i, j]) for i in idx) for j in range(64)])
    L = Matrix(rows)
    augmented = phi.col_join(L)
    aug_rank = int(augmented.rank())
    residual_rank = aug_rank - 3

    selected = []
    current = phi
    current_rank = 3
    for pos, rule in enumerate(nonfixed):
        candidate = current.col_join(Matrix([rows[pos]]))
        rr = int(candidate.rank())
        if rr > current_rank:
            selected.append(rule.orbit_id)
            current = candidate
            current_rank = rr
    if current_rank != aug_rank or len(selected) != residual_rank:
        raise ValueError("greedy quotient-basis rank regression")

    payload = {
        "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_NONFIXED_ORBIT_SUM_RANK_DIAGNOSTIC_V1",
        "mode": "EXACT_RANK_OF_STABILIZER_ORBIT_SUM_FUNCTIONALS_MODULO_D_E_A_SLICE",
        "stabilizer_orbit_certificate_sha256": model.certificate["canonical_sha256_without_this_field"],
        "adapter_certificate_sha256": adapter.certificate["canonical_sha256_without_this_field"],
        "nonfixed_orbit_count": len(nonfixed),
        "nonfixed_orbit_ids": [r.orbit_id for r in nonfixed],
        "nonfixed_orbit_sum_row_rank": int(L.rank()),
        "phi_plus_nonfixed_orbit_sum_rank": aug_rank,
        "orbit_sum_quotient_rank_mod_phi": residual_rank,
        "greedy_independent_orbit_ids_mod_phi": selected,
        "active_set_subset_upper_count": sum(math.comb(len(nonfixed), k) for k in range(residual_rank + 1)),
        "proof": {
            "all_rows_exact_integral_pairing_functionals": True,
            "rank_exact_over_Q": True,
            "no_numerical_qp_run": True,
        },
        "numerical_row_complete": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "route_credit": False,
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_DIRECT_PICARD_NONFIXED_ORBIT_SUM_RANK_DIAGNOSTIC",
        "nonfixed_orbits": len(nonfixed),
        "quotient_rank": residual_rank,
        "augmented_rank": aug_rank,
        "independent_orbits": selected,
        "active_set_subset_upper_count": payload["active_set_subset_upper_count"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
