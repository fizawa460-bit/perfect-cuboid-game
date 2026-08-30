#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib

from direct_picard_integral_coset_bound import DirectPicardIntegralCosetLowerBound

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
SCHEMA = "STAGE32_RESIDUAL32_01_DIRECT_PICARD_INTEGRAL_COSET_CENSUS_V1"


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
    bundle = load_module_payload(args.retained, "stage32_integral_lb_picard")
    marking = load_module_payload(args.marking, "stage32_integral_lb_marking")
    model = DirectPicardIntegralCosetLowerBound.from_retained(marking, bundle)
    bound = model.bound
    bridge = bound.bridge

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    assert len(rows) == 178 and len(set(rows)) == 178

    prior_image_quadratic = 0
    integral_lb_feasible = 0
    integral_lb_empty_e = 0
    zero_rows = 0
    class_prior_counts = [0] * len(model.class_lower_bounds)
    class_survivor_counts = [0] * len(model.class_lower_bounds)
    row_summaries = []
    stream_hash = hashlib.sha256()

    for row_id in rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_prior = 0
        row_survivors = 0
        row_empty_e = 0
        peak = None
        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            e_prior = 0
            e_survivors = 0
            if interval is not None:
                lo, hi = interval
                for a in range(lo, hi + 1):
                    if not bridge.target_in_image(d, e, a):
                        continue
                    e_prior += 1
                    class_id = model.class_id(d, e, a)
                    class_prior_counts[class_id] += 1
                    if model.can_reach_selfsq_after_integrality_lb(d, e, a, lower):
                        e_survivors += 1
                        class_survivor_counts[class_id] += 1
            if e_survivors == 0:
                row_empty_e += 1
                integral_lb_empty_e += 1
            row_prior += e_prior
            row_survivors += e_survivors
            prior_image_quadratic += e_prior
            integral_lb_feasible += e_survivors
            rec = {
                "row_id": row_id,
                "e": e,
                "prior_image_and_continuous_quadratic_count": e_prior,
                "integral_coset_lower_bound_feasible_count": e_survivors,
            }
            stream_hash.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
            if peak is None or e_survivors > peak[1]:
                peak = (e, e_survivors)
        assert peak is not None
        if row_survivors == 0:
            zero_rows += 1
        row_summaries.append({
            "row_id": row_id,
            "degree": d,
            "genus": g,
            "prior_image_and_continuous_quadratic_slices": row_prior,
            "integral_coset_lower_bound_feasible_slices": row_survivors,
            "pruned_by_integral_coset_lower_bound": row_prior - row_survivors,
            "integral_coset_lower_bound_empty_e_strata": row_empty_e,
            "peak_surviving_e": peak[0],
            "peak_surviving_count": peak[1],
        })

    # Locked cross-check against the immediately preceding exact census.
    if prior_image_quadratic != 2_018_569:
        raise ValueError(f"prior direct quadratic survivor drift: {prior_image_quadratic}")

    active_prior_classes = sum(1 for count in class_prior_counts if count)
    active_survivor_classes = sum(1 for count in class_survivor_counts if count)
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "EXACT_640_CLASS_COORDINATE_INTEGRALITY_LOWER_BOUND_AFTER_DIRECT_QUADRATIC_GATE",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "integral_coset_lower_bound_certificate_sha256": model.certificate["canonical_sha256_without_this_field"],
        "quadratic_bound_certificate_sha256": bound.certificate["canonical_sha256_without_this_field"],
        "row_count": len(rows),
        "e_strata": int(manifest["coarse_strata_count"]),
        "reachable_integrality_class_count": len(model.class_lower_bounds),
        "active_prior_integrality_classes": active_prior_classes,
        "active_survivor_integrality_classes": active_survivor_classes,
        "prior_image_and_continuous_quadratic_feasible_slices": prior_image_quadratic,
        "integral_coset_lower_bound_feasible_slices": integral_lb_feasible,
        "pruned_by_integral_coset_lower_bound": prior_image_quadratic - integral_lb_feasible,
        "integral_coset_lower_bound_empty_e_strata": integral_lb_empty_e,
        "rows_zero_after_integral_coset_lower_bound": zero_rows,
        "class_prior_counts": class_prior_counts,
        "class_survivor_counts": class_survivor_counts,
        "slice_stream_sha256": stream_hash.hexdigest(),
        "row_summaries": row_summaries,
        "semantics": {
            "coordinate_cauchy_integrality_gate_is_safe_necessary_condition": True,
            "target_image_gate_is_exact": True,
            "only_640_reachable_integrality_classes": True,
            "closest_vectors_not_run": True,
            "all140_nonnegativity_not_yet_enumerated": True,
            "numerical_picard_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    if not (0 <= integral_lb_feasible <= prior_image_quadratic):
        raise ValueError("integral-coset lower-bound survivor count regression")
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_DIRECT_PICARD_INTEGRAL_COSET_CENSUS",
        "prior_slices": prior_image_quadratic,
        "surviving_slices": integral_lb_feasible,
        "pruned_slices": prior_image_quadratic - integral_lb_feasible,
        "zero_rows": zero_rows,
        "active_prior_classes": active_prior_classes,
        "active_survivor_classes": active_survivor_classes,
        "lower_bound_sha256": model.certificate["canonical_sha256_without_this_field"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
