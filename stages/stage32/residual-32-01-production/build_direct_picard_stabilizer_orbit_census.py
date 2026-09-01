#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib

from direct_picard_slice_stabilizer_orbit_bound import DirectPicardSliceStabilizerOrbitBound

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PRIOR_IMAGE_QUADRATIC_SLICES = 2018569
SCHEMA = "STAGE32_RESIDUAL32_01_DIRECT_PICARD_STABILIZER_FIXED_ORBIT_SUM_CENSUS_V1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def load_module_payload(path: pathlib.Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=pathlib.Path, required=True)
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--marking", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    assert csha(manifest) == claimed == EXPECTED_MANIFEST_SHA256
    bundle = load_module_payload(args.retained, "stage32_stabilizer_picard")
    marking = load_module_payload(args.marking, "stage32_stabilizer_marking")
    model = DirectPicardSliceStabilizerOrbitBound.from_retained(marking, bundle)
    bound = model.bound
    bridge = bound.bridge

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    assert len(rows) == 178 and len(set(rows)) == 178

    prior = survivors = pruned = 0
    zero_rows = zero_e_strata = 0
    orbit_prune_counts = [0] * len(model.rules)
    row_summaries = []

    for row_id in rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_prior = row_survivors = row_pruned = row_zero_e = 0

        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            e_prior = e_survivors = 0
            if interval is not None:
                lo, hi = interval
                for a in range(lo, hi + 1):
                    if not bridge.target_in_image(d, e, a):
                        continue
                    prior += 1
                    row_prior += 1
                    e_prior += 1
                    rule = model.first_negative_fixed_orbit(d, e, a)
                    if rule is None:
                        survivors += 1
                        row_survivors += 1
                        e_survivors += 1
                    else:
                        pruned += 1
                        row_pruned += 1
                        orbit_prune_counts[rule.orbit_id] += 1
            if e_prior > 0 and e_survivors == 0:
                zero_e_strata += 1
                row_zero_e += 1

        if row_prior > 0 and row_survivors == 0:
            zero_rows += 1
        row_summaries.append({
            "row_id": row_id,
            "prior_image_quadratic_slices": row_prior,
            "fixed_orbit_sum_surviving_slices": row_survivors,
            "fixed_orbit_sum_pruned_slices": row_pruned,
            "new_zero_e_strata": row_zero_e,
        })

    assert prior == EXPECTED_PRIOR_IMAGE_QUADRATIC_SLICES, prior
    assert survivors + pruned == prior
    prune_summary = []
    for r in model.rules:
        count = orbit_prune_counts[r.orbit_id]
        if count:
            prune_summary.append({
                "orbit_id": r.orbit_id,
                "known_curve_labels_1based": list(r.known_curve_labels_1based),
                "orbit_size": len(r.known_curve_labels_1based),
                "first_prune_count": count,
            })
    prune_summary.sort(key=lambda x: (-x["first_prune_count"], x["orbit_id"]))

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "FULL178_EXACT_BASE_SLICE_PLUS_FIXED_STABILIZER_ORBIT_SUM_NONNEGATIVITY",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "stabilizer_orbit_certificate_sha256": model.certificate["canonical_sha256_without_this_field"],
        "row_count": len(rows),
        "e_strata": int(manifest["coarse_strata_count"]),
        "slice_stabilizer_group_order": model.subgroup_order,
        "orbit_count": len(model.rules),
        "fixed_orbit_sum_count": sum(1 for r in model.rules if r.fixed_on_slice),
        "prior_image_and_continuous_quadratic_feasible_slices": prior,
        "fixed_orbit_sum_pruned_slices": pruned,
        "fixed_orbit_sum_surviving_slices": survivors,
        "new_zero_e_strata": zero_e_strata,
        "new_zero_rows": zero_rows,
        "orbit_prune_summary": prune_summary,
        "row_summaries": row_summaries,
        "semantics": {
            "all140_nonnegativity_used": True,
            "only_fixed_orbit_sum_necessary_conditions_used_in_census": True,
            "nonfixed_orbit_simultaneous_qp_not_yet_used": True,
            "integral_640_coset_correction_not_used": True,
            "numerical_picard_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_DIRECT_PICARD_STABILIZER_FIXED_ORBIT_SUM_CENSUS",
        "stabilizer_order": model.subgroup_order,
        "orbit_count": len(model.rules),
        "fixed_orbits": sum(1 for r in model.rules if r.fixed_on_slice),
        "prior_slices": prior,
        "pruned_slices": pruned,
        "surviving_slices": survivors,
        "zero_e_strata": zero_e_strata,
        "zero_rows": zero_rows,
        "bound_sha256": model.certificate["canonical_sha256_without_this_field"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
