#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib

from direct_picard_all140_facet_bound import DirectPicardAll140SingleFacetBound

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PRIOR_IMAGE_QUADRATIC_SLICES = 2018569
SCHEMA = "STAGE32_RESIDUAL32_01_DIRECT_PICARD_ALL140_SINGLE_FACET_CENSUS_V1"


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
    bundle = load_module_payload(args.retained, "stage32_all140_facet_picard")
    marking = load_module_payload(args.marking, "stage32_all140_facet_marking")
    model = DirectPicardAll140SingleFacetBound.from_retained(marking, bundle)
    bound = model.bound
    bridge = bound.bridge

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    assert len(rows) == 178 and len(set(rows)) == 178

    prior = 0
    survivors = 0
    violated_unconstrained = 0
    pruned = 0
    zero_rows = 0
    zero_e_strata = 0
    active_rule_ids: set[int] = set()
    pruning_rule_counts = [0] * len(model.rules)
    row_summaries = []

    for row_id in rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_prior = row_survivors = row_pruned = 0
        row_zero_e = 0

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

                    any_violated = False
                    for rule in model.rules:
                        if rule.violated_by_unconstrained_maximizer(d, e, a):
                            any_violated = True
                            active_rule_ids.add(rule.rule_id)
                            if not rule.boundary_can_reach(d, e, a, lower):
                                pruning_rule_counts[rule.rule_id] += 1
                                pruned += 1
                                row_pruned += 1
                                break
                    else:
                        survivors += 1
                        row_survivors += 1
                        e_survivors += 1
                    if any_violated:
                        violated_unconstrained += 1

            if e_prior > 0 and e_survivors == 0:
                zero_e_strata += 1
                row_zero_e += 1

        if row_prior > 0 and row_survivors == 0:
            zero_rows += 1
        row_summaries.append({
            "row_id": row_id,
            "prior_image_quadratic_slices": row_prior,
            "single_facet_surviving_slices": row_survivors,
            "single_facet_pruned_slices": row_pruned,
            "new_zero_e_strata": row_zero_e,
        })

    assert prior == EXPECTED_PRIOR_IMAGE_QUADRATIC_SLICES, prior
    assert survivors + pruned == prior
    rule_summary = []
    for rule in model.rules:
        count = pruning_rule_counts[rule.rule_id]
        if count:
            rule_summary.append({
                "rule_id": rule.rule_id,
                "known_curve_labels_1based": list(rule.known_curve_labels_1based),
                "multiplicity": len(rule.known_curve_labels_1based),
                "first_prune_count": count,
            })
    rule_summary.sort(key=lambda rec: (-rec["first_prune_count"], rec["rule_id"]))

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "FULL178_EXACT_BASE_SLICE_PLUS_ALL140_SINGLE_FACET_CONTINUOUS_UPPER_ENVELOPE",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "all140_single_facet_certificate_sha256": model.certificate["canonical_sha256_without_this_field"],
        "row_count": len(rows),
        "e_strata": int(manifest["coarse_strata_count"]),
        "unique_exact_facet_rule_count": len(model.rules),
        "prior_image_and_continuous_quadratic_feasible_slices": prior,
        "slices_with_at_least_one_violated_unconstrained_facet": violated_unconstrained,
        "single_facet_pruned_slices": pruned,
        "single_facet_surviving_slices": survivors,
        "active_violated_rule_count": len(active_rule_ids),
        "new_zero_e_strata": zero_e_strata,
        "new_zero_rows": zero_rows,
        "pruning_rule_summary": rule_summary,
        "row_summaries": row_summaries,
        "semantics": {
            "all140_pairing_nonnegativity_used_as_individual_halfspaces": True,
            "single_facet_relaxation_is_safe_necessary_condition": True,
            "simultaneous_multifacet_kkt_not_yet_used": True,
            "integral_640_coset_correction_not_used_in_this_gate": True,
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
        "verdict": "PASS_DIRECT_PICARD_ALL140_SINGLE_FACET_CENSUS",
        "unique_rules": len(model.rules),
        "prior_slices": prior,
        "violated_unconstrained_slices": violated_unconstrained,
        "pruned_slices": pruned,
        "surviving_slices": survivors,
        "zero_e_strata": zero_e_strata,
        "zero_rows": zero_rows,
        "bound_sha256": model.certificate["canonical_sha256_without_this_field"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
