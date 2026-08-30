#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

from direct_picard_reynolds_rank2_antifixed_coset_bound import ReynoldsRank2AntiFixedCosetBound

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_AC_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_RESULT_VERDICT = "PASS_STAGE32_21AD_FULL178_16SHARD_ANTIFIXED_COSET_NUMERICAL_CENSUS"
EXPECTED_PRODUCTION_RUN_ID = 33313814094
EXPECTED_AGGREGATE_ARTIFACT_ID = 9732838513
EXPECTED_AGGREGATE_ZIP_SHA256 = "5c2ba19b704f9466ad8bd083a4ad14a2821aad5ab0b5829999dbd9ab3bca98cf"
EXPECTED_AGGREGATE_CERT_SHA256 = "9bf4aba655a6df81e621e3f78e19b16460f1138410ed118f18e25fcb77bf24ad"
EXPECTED_SHARDS = 16
EXPECTED_ROWS = 178
EXPECTED_PRIOR = 2018569
EXPECTED_CONT = 679337
EXPECTED_PRUNED = 0
EXPECTED_SURVIVORS = 679337
EXPECTED_CHECKED_U_TOTAL = 1971035
EXPECTED_CHECKED_U_MAX = 114
EXPECTED_ZERO_E = 0
EXPECTED_ZERO_ROWS = 0
EXPECTED_POSITIVE_COSETS = 127
EXPECTED_ZERO_COSETS = 1
EXPECTED_MIN_POSITIVE = Fraction(1, 572)


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module_payload(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--result", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    result = json.loads(args.result.read_text())
    if result["verdict"] != EXPECTED_RESULT_VERDICT:
        raise ValueError("committed 32-21ad verdict drift")
    if result["status"] != "EXACT_CENSUS_COMPLETE_PENDING_BOUNDARY_AUDIT":
        raise ValueError("32-21ad result is not at the expected pre-audit boundary")
    par = result["exact_parallel_census"]
    result_locks = (
        int(par["run_id"]),
        int(par["aggregate_artifact_id"]),
        str(par["aggregate_artifact_zip_sha256"]),
        str(par["aggregate_certificate_sha256"]),
    )
    expected_locks = (
        EXPECTED_PRODUCTION_RUN_ID,
        EXPECTED_AGGREGATE_ARTIFACT_ID,
        EXPECTED_AGGREGATE_ZIP_SHA256,
        EXPECTED_AGGREGATE_CERT_SHA256,
    )
    if result_locks != expected_locks:
        raise ValueError(f"committed production evidence lock drift: {result_locks}")

    manifest = json.loads(args.manifest.read_text())
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed_manifest or claimed_manifest != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    if len(all_rows) != EXPECTED_ROWS or len(set(all_rows)) != EXPECTED_ROWS:
        raise ValueError("FULL178 row population regression")
    expected_rows_by_shard = {
        idx: [row for j, row in enumerate(all_rows) if j % EXPECTED_SHARDS == idx]
        for idx in range(EXPECTED_SHARDS)
    }

    bundle = load_module_payload(args.retained, "stage32_21ad_audit_picard")
    marking = load_module_payload(args.marking, "stage32_21ad_audit_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    ac_sha = model.certificate["canonical_sha256_without_this_field"]
    if ac_sha != EXPECTED_AC_SHA256:
        raise ValueError("audited 32-21ac evaluator certificate drift")
    lbs = tuple(model.coset_lower_bounds)
    positive = tuple(v for v in lbs if v > 0)
    zero = sum(v == 0 for v in lbs)
    if len(lbs) != 128 or len(positive) != EXPECTED_POSITIVE_COSETS or zero != EXPECTED_ZERO_COSETS:
        raise ValueError("32-21ac coset population drift")
    if min(positive) != EXPECTED_MIN_POSITIVE:
        raise ValueError("32-21ac minimum positive coset penalty drift")

    files = sorted(args.input_dir.rglob("stage32-21ad-shard-*.json"))
    if len(files) != EXPECTED_SHARDS:
        raise ValueError(f"expected {EXPECTED_SHARDS} shard payloads, got {len(files)}")

    shards: dict[int, dict] = {}
    shard_canonical_hashes: list[list[object]] = []
    all_seen_rows: list[str] = []
    reason_counts: Counter[str] = Counter()
    coset_counts: Counter[str] = Counter()
    penalty_counts: Counter[str] = Counter()
    prior = cont = pruned = survivors = checked_total = zero_e = zero_rows = 0
    checked_max = 0

    for path in files:
        payload = json.loads(path.read_text())
        claimed = str(payload.pop("canonical_sha256_without_this_field"))
        recomputed = csha(payload)
        if recomputed != claimed:
            raise ValueError(f"shard canonical hash mismatch: {path}")
        idx = int(payload["shard_index"])
        if idx in shards or not 0 <= idx < EXPECTED_SHARDS:
            raise ValueError(f"duplicate/invalid shard index {idx}")
        if payload["row_shards"] != EXPECTED_SHARDS or payload["full_run"] is not False:
            raise ValueError("shard geometry regression")
        if payload["manifest_canonical_sha256"] != EXPECTED_MANIFEST_SHA256:
            raise ValueError("manifest lock mismatch inside shard")
        if payload["audited_32_21ac_certificate_sha256"] != EXPECTED_AC_SHA256:
            raise ValueError("32-21ac lock mismatch inside shard")
        if payload["selected_rows"] != expected_rows_by_shard[idx]:
            raise ValueError(f"deterministic row partition mismatch on shard {idx}")
        summaries = payload["row_summaries"]
        summary_rows = [row["row_id"] for row in summaries]
        if summary_rows != payload["selected_rows"]:
            raise ValueError(f"row summary order/coverage mismatch on shard {idx}")
        if len(summary_rows) != len(set(summary_rows)):
            raise ValueError(f"duplicate row summary on shard {idx}")

        row_prior = sum(int(row["prior_image_and_unconstrained_quadratic_slices"]) for row in summaries)
        row_cont = sum(int(row["continuous_kkt_surviving_slices"]) for row in summaries)
        row_pruned = sum(int(row["antifixed_coset_pruned_slices"]) for row in summaries)
        row_survivors = sum(int(row["antifixed_coset_surviving_slices"]) for row in summaries)
        row_zero_e = sum(int(row["zero_e_strata_from_continuous_survivor_population"]) for row in summaries)
        if row_prior != int(payload["prior_image_and_unconstrained_quadratic_slices"]):
            raise ValueError(f"row prior total mismatch on shard {idx}")
        if row_cont != int(payload["exact_continuous_kkt_surviving_slices"]):
            raise ValueError(f"row continuous total mismatch on shard {idx}")
        if row_pruned != int(payload["antifixed_coset_pruned_slices"]):
            raise ValueError(f"row prune total mismatch on shard {idx}")
        if row_survivors != int(payload["antifixed_coset_surviving_slices"]):
            raise ValueError(f"row survivor total mismatch on shard {idx}")
        if row_zero_e != int(payload["zero_e_strata_from_continuous_survivor_population"]):
            raise ValueError(f"row zero-e total mismatch on shard {idx}")
        if row_pruned != 0 or row_survivors != row_cont:
            raise ValueError(f"nonzero prune or accounting drift on shard {idx}")
        computed_zero_rows = sum(
            int(row["continuous_kkt_surviving_slices"]) > 0
            and int(row["antifixed_coset_surviving_slices"]) == 0
            for row in summaries
        )
        if computed_zero_rows != int(payload["zero_rows_from_continuous_survivor_population"]):
            raise ValueError(f"row zero-row total mismatch on shard {idx}")

        shard_reason_total = sum(int(v) for v in payload["decision_reason_counts"].values())
        shard_coset_total = sum(int(v) for v in payload["quotient_coset_population_counts"].values())
        shard_penalty_total = sum(int(v) for v in payload["coset_penalty_population_counts"].values())
        if (shard_reason_total, shard_coset_total, shard_penalty_total) != (row_cont, row_cont, row_cont):
            raise ValueError(f"decision/coset/penalty population mismatch on shard {idx}")
        if not payload["decision_stream_sha256"] or not payload["surviving_witness_stream_sha256"]:
            raise ValueError(f"missing decision/witness commitment on shard {idx}")

        sem = payload["semantics"]
        required_false = (
            "terminal_family_materialization_run",
            "legacy_prefix_DFS_run",
            "anti_fixed_59d_closest_vector_search_run",
            "unknown_is_unsat",
            "numerical_row_complete",
            "theorem_credit",
            "receiver_credit",
            "route_credit",
            "perfect_cuboid_existence_claim",
            "perfect_cuboid_nonexistence_claim",
        )
        if any(bool(sem[key]) for key in required_false):
            raise ValueError(f"firewall regression on shard {idx}")
        required_true = (
            "continuous_kkt_problem_exact_under_stabilizer_averaging",
            "audited_32_21ac_evaluator_used_without_formula_change",
            "antifixed_coset_false_decision_safe_for_original_integral_picard_slice",
            "antifixed_coset_true_decision_only_necessary_condition",
        )
        if not all(bool(sem[key]) for key in required_true):
            raise ValueError(f"semantic invariant regression on shard {idx}")

        shards[idx] = payload
        shard_canonical_hashes.append([idx, claimed])
        all_seen_rows.extend(summary_rows)
        prior += row_prior
        cont += row_cont
        pruned += row_pruned
        survivors += row_survivors
        zero_e += row_zero_e
        zero_rows += computed_zero_rows
        checked_total += int(payload["checked_integer_u_total"])
        checked_max = max(checked_max, int(payload["checked_integer_u_max_per_slice"]))
        reason_counts.update({k: int(v) for k, v in payload["decision_reason_counts"].items()})
        coset_counts.update({k: int(v) for k, v in payload["quotient_coset_population_counts"].items()})
        penalty_counts.update({k: int(v) for k, v in payload["coset_penalty_population_counts"].items()})

    if set(shards) != set(range(EXPECTED_SHARDS)):
        raise ValueError("shard index coverage regression")
    if len(all_seen_rows) != EXPECTED_ROWS or set(all_seen_rows) != set(all_rows):
        raise ValueError("FULL178 row coverage mismatch across shard evidence")
    if len(all_seen_rows) != len(set(all_seen_rows)):
        raise ValueError("FULL178 row evidence is not disjoint")

    totals = (prior, cont, pruned, survivors, checked_total, checked_max, zero_e, zero_rows)
    expected_totals = (
        EXPECTED_PRIOR,
        EXPECTED_CONT,
        EXPECTED_PRUNED,
        EXPECTED_SURVIVORS,
        EXPECTED_CHECKED_U_TOTAL,
        EXPECTED_CHECKED_U_MAX,
        EXPECTED_ZERO_E,
        EXPECTED_ZERO_ROWS,
    )
    if totals != expected_totals:
        raise ValueError(f"FULL178 aggregate drift: got {totals}, expected {expected_totals}")
    if sum(reason_counts.values()) != cont or sum(coset_counts.values()) != cont or sum(penalty_counts.values()) != cont:
        raise ValueError("aggregated decision/coset/penalty accounting regression")

    if int(par["prior_image_and_unconstrained_quadratic_slices"]) != prior:
        raise ValueError("committed result prior total disagrees with audited shard evidence")
    if int(par["exact_continuous_kkt_surviving_slices"]) != cont:
        raise ValueError("committed result continuous total disagrees with audited shard evidence")
    if int(par["antifixed_coset_pruned_slices"]) != pruned:
        raise ValueError("committed result prune total disagrees with audited shard evidence")
    if int(par["antifixed_coset_surviving_slices"]) != survivors:
        raise ValueError("committed result survivor total disagrees with audited shard evidence")

    shard_canonical_hashes.sort(key=lambda x: int(x[0]))
    cert = {
        "schema": "STAGE32_21AD_BOUNDARY_AUDIT_V1",
        "verdict": "PASS_STAGE32_21AD_FRESH_ZERO_PRUNE_BOUNDARY_AUDIT",
        "scope": "immutable 16-shard FULL178 evidence integrity, exact row partition, independent aggregation, audited 32-21ac source lock, zero-additional-prune interpretation",
        "production_evidence_lock": {
            "run_id": EXPECTED_PRODUCTION_RUN_ID,
            "aggregate_artifact_id": EXPECTED_AGGREGATE_ARTIFACT_ID,
            "aggregate_artifact_zip_sha256": EXPECTED_AGGREGATE_ZIP_SHA256,
            "aggregate_certificate_sha256": EXPECTED_AGGREGATE_CERT_SHA256,
        },
        "independent_evidence_audit": {
            "all_16_shard_payload_canonical_hashes_recomputed": True,
            "shard_count": len(shards),
            "shard_canonical_sha256s": shard_canonical_hashes,
            "deterministic_mod16_row_partition_rebuilt_from_manifest": True,
            "full178_unique_row_count": len(set(all_seen_rows)),
            "all_row_summary_totals_recomputed": True,
            "decision_reason_population_reconciled": True,
            "quotient_coset_population_reconciled": True,
            "coset_penalty_population_reconciled": True,
        },
        "rederived_32_21ac_lock": {
            "certificate_sha256": ac_sha,
            "coset_count": len(lbs),
            "positive_minimum_coset_count": len(positive),
            "zero_minimum_coset_count": zero,
            "minimum_positive_coset_lower_bound": [min(positive).numerator, min(positive).denominator],
        },
        "full178_exact_totals": {
            "prior_slices": prior,
            "continuous_kkt_survivors": cont,
            "antifixed_coset_pruned": pruned,
            "antifixed_coset_survivors": survivors,
            "additional_prune_rate": 0.0,
            "checked_integer_u_total": checked_total,
            "checked_integer_u_max_per_slice": checked_max,
            "zero_e_strata": zero_e,
            "zero_rows": zero_rows,
        },
        "interpretation": {
            "32_21ac_mathematical_validity_preserved": True,
            "32_21ac_additional_pruning_power_on_this_exact_full178_population": "ZERO",
            "same_full178_census_rearm_without_semantic_change_is_dominated": True,
            "strategy_change_required_before_any_new_heavy_production": True,
            "this_audit_does_not_select_or_precommit_the_next_strategy": True,
        },
        "firewalls": {
            "finite_full178_result_is_not_global_nonexistence": True,
            "unknown_is_unsat": False,
            "numerical_row_complete": False,
            "stage32_closed": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "route_color_change_authorized": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "release": {
            "32_21ad_audited_checkpoint": True,
            "checkpoint_merge_ready": True,
            "automatic_merge_authorized": False,
            "further_heavy_compute_authorized": False,
            "next_strategy_selection_released_only_after_checkpoint_merge": True,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": cert["verdict"],
        "shards": len(shards),
        "rows": len(set(all_seen_rows)),
        "prior_slices": prior,
        "continuous_kkt_survivors": cont,
        "antifixed_pruned": pruned,
        "antifixed_survivors": survivors,
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
