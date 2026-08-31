#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXPECTED_LOCK_CANONICAL = "63b3a6d4a1dbbf2900ce97f3ec7c014df970d0be23b3cfe2e0d4f71c0cd23bfe"
EXPECTED_AGGREGATE_CANONICAL = "f9d4ca8c504ed605e7f97bbd306a3d38272e1759e2a2d44d55bb0e8dfb55995d"
EXPECTED_AGGREGATE_JSON_SHA256 = "b51304ac50321aad924187d99016cc5f3c0702e97c6304824bf4970f9f9ba59a"
EXPECTED_MANIFEST_CANONICAL = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_DRIVER_BLOB = "93f7dc6f1b224f61af3f260d09da55bfb5a3460a"
EXPECTED_AGGREGATOR_BLOB = "92561bbc1cac6f2d5c47bf37bfbc9c6bfaba3cdd"
EXPECTED_ROWS = 178
EXPECTED_BEFORE = 64111
EXPECTED_ELIMINATED = 3620
EXPECTED_AFTER = 60491
EXPECTED_AFFECTED = 168
EXPECTED_PRIOR = 1789187
EXPECTED_KKT = 659697
EXPECTED_PRUNED = 0
EXPECTED_OLD_PRIOR = 2018569
EXPECTED_OLD_KKT = 679337


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.get("canonical_sha256_without_this_field")
    body = dict(raw)
    body.pop("canonical_sha256_without_this_field", None)
    got = csha(body)
    if claimed != expected or got != expected:
        raise ValueError(f"canonical mismatch for {path}: claimed={claimed} got={got}")
    return raw


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--lock", type=Path, required=True)
    ap.add_argument("--aggregate", type=Path, required=True)
    ap.add_argument("--driver", type=Path, required=True)
    ap.add_argument("--aggregator", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    lock = load_canonical(args.lock, EXPECTED_LOCK_CANONICAL)
    aggregate_bytes = args.aggregate.read_bytes()
    if hashlib.sha256(aggregate_bytes).hexdigest() != EXPECTED_AGGREGATE_JSON_SHA256:
        raise ValueError("aggregate raw JSON sha256 regression")
    aggregate = load_canonical(args.aggregate, EXPECTED_AGGREGATE_CANONICAL)

    manifest = json.loads(args.manifest.read_text())
    manifest_claimed = manifest.pop("canonical_sha256_without_this_field")
    if manifest_claimed != EXPECTED_MANIFEST_CANONICAL or csha(manifest) != EXPECTED_MANIFEST_CANONICAL:
        raise ValueError("manifest canonical regression")
    if git_blob_sha1(args.driver) != EXPECTED_DRIVER_BLOB:
        raise ValueError("driver git-blob regression")
    if git_blob_sha1(args.aggregator) != EXPECTED_AGGREGATOR_BLOB:
        raise ValueError("aggregator git-blob regression")

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    if len(all_rows) != EXPECTED_ROWS or len(set(all_rows)) != EXPECTED_ROWS:
        raise ValueError("manifest FULL178 population regression")

    rows = aggregate["row_summaries"]
    if len(rows) != EXPECTED_ROWS or len({r["row_id"] for r in rows}) != EXPECTED_ROWS:
        raise ValueError("aggregate row coverage regression")
    by_id = {r["row_id"]: r for r in rows}
    if set(by_id) != set(all_rows):
        raise ValueError("aggregate row-id set differs from manifest")

    before = eliminated = after = affected = 0
    row_prior = row_cont = row_pruned = row_surv = 0
    for row_id in all_rows:
        g, d = parse_row_id(row_id)
        r = by_id[row_id]
        legacy_min = 8 if g == 0 else 4
        emax = (19 * d) // 5
        required = ceil_div(d - 16 * g + 16, 4)
        effective = max(legacy_min, required)
        rb = max(0, emax - legacy_min + 1)
        ra = max(0, emax - effective + 1)
        re = rb - ra
        expected_row = {
            "legacy_e_min": legacy_min,
            "node_mass_required_e_min": required,
            "effective_e_min": effective,
            "e_max": emax,
            "coarse_e_strata_before_cut": rb,
            "coarse_e_strata_eliminated_by_node_mass_cut": re,
            "coarse_e_strata_after_cut": ra,
        }
        for key, value in expected_row.items():
            if int(r[key]) != value:
                raise ValueError(f"row {row_id} {key}: {r[key]} != {value}")
        before += rb
        eliminated += re
        after += ra
        affected += int(re > 0)
        row_prior += int(r["postcut_image_and_unconstrained_quadratic_slices"])
        row_cont += int(r["postcut_continuous_kkt_surviving_slices"])
        row_pruned += int(r["postcut_antifixed_coset_pruned_slices"])
        row_surv += int(r["postcut_antifixed_coset_surviving_slices"])

    if (before, eliminated, after, affected) != (
        EXPECTED_BEFORE, EXPECTED_ELIMINATED, EXPECTED_AFTER, EXPECTED_AFFECTED
    ):
        raise ValueError("independent node-mass row accounting regression")
    if (row_prior, row_cont, row_pruned, row_surv) != (
        EXPECTED_PRIOR, EXPECTED_KKT, EXPECTED_PRUNED, EXPECTED_KKT
    ):
        raise ValueError("row-summary aggregate totals regression")

    top = (
        aggregate["postcut_image_and_unconstrained_quadratic_slices"],
        aggregate["postcut_exact_continuous_kkt_surviving_slices"],
        aggregate["postcut_antifixed_coset_pruned_slices"],
        aggregate["postcut_antifixed_coset_surviving_slices"],
    )
    if top != (EXPECTED_PRIOR, EXPECTED_KKT, EXPECTED_PRUNED, EXPECTED_KKT):
        raise ValueError("aggregate top-level totals regression")
    if aggregate["node_mass_cut"] != {
        "affected_rows": EXPECTED_AFFECTED,
        "coarse_e_strata_after_cut": EXPECTED_AFTER,
        "coarse_e_strata_before_cut": EXPECTED_BEFORE,
        "coarse_e_strata_eliminated": EXPECTED_ELIMINATED,
        "formula": "e >= ceil((d-16g+16)/4)",
    }:
        raise ValueError("aggregate node-mass cut metadata regression")

    exact = lock["exact_result"]
    if exact["postcut_prior_slices"] != EXPECTED_PRIOR or exact["postcut_continuous_kkt_survivors"] != EXPECTED_KKT:
        raise ValueError("tracked lock numerical totals regression")
    cmp = lock["comparison_to_audited_21ad"]
    if cmp["prior_slices_before"] - EXPECTED_PRIOR != cmp["prior_slices_removed"]:
        raise ValueError("prior-slice comparison regression")
    if cmp["continuous_kkt_survivors_before"] - EXPECTED_KKT != cmp["continuous_kkt_survivors_removed"]:
        raise ValueError("KKT comparison regression")
    if cmp["prior_slices_before"] != EXPECTED_OLD_PRIOR or cmp["continuous_kkt_survivors_before"] != EXPECTED_OLD_KKT:
        raise ValueError("audited 21ad baseline regression")

    sem = aggregate["semantics"]
    required_false = [
        "multibranch_closed", "receiver_credit", "route_credit",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
    ]
    if any(sem.get(k) is not False for k in required_false):
        raise ValueError("aggregate research-credit firewall regression")
    if sem.get("bijective_normalization_branch_only") is not True:
        raise ValueError("aggregate branch-scope regression")

    out = {
        "schema": "STAGE32_POST21BL_FULL178_NODE_MASS_CENSUS_FRESH_AUDIT_V1",
        "stage": 32,
        "leaf": "POST_21BL_FULL178_NODE_MASS_CENSUS",
        "status": "PASS_FRESH_AUDIT_FULL178_NODE_MASS_NUMERICAL_CENSUS",
        "source_lock_canonical_sha256": EXPECTED_LOCK_CANONICAL,
        "aggregate_canonical_sha256": EXPECTED_AGGREGATE_CANONICAL,
        "aggregate_json_sha256": EXPECTED_AGGREGATE_JSON_SHA256,
        "independent_row_cut_recomputed": True,
        "driver_git_blob_verified": True,
        "aggregator_git_blob_verified": True,
        "full_population_rows": EXPECTED_ROWS,
        "coarse_e_strata": {
            "before": EXPECTED_BEFORE,
            "eliminated": EXPECTED_ELIMINATED,
            "after": EXPECTED_AFTER,
            "affected_rows": EXPECTED_AFFECTED,
        },
        "postcut": {
            "prior_slices": EXPECTED_PRIOR,
            "continuous_kkt_survivors": EXPECTED_KKT,
            "antifixed_pruned": EXPECTED_PRUNED,
            "antifixed_survivors": EXPECTED_KKT,
        },
        "comparison_to_audited_21ad": {
            "prior_slices_removed": EXPECTED_OLD_PRIOR - EXPECTED_PRIOR,
            "continuous_kkt_survivors_removed": EXPECTED_OLD_KKT - EXPECTED_KKT,
        },
        "credit": {
            "full178_numerical_credit_for_this_necessary_condition_stack": True,
            "full178_geometric_closure": False,
            "multibranch_closed": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": out["status"],
        "canonical": out["canonical_sha256_without_this_field"],
        "rows": EXPECTED_ROWS,
        "prior_removed": EXPECTED_OLD_PRIOR - EXPECTED_PRIOR,
        "kkt_removed": EXPECTED_OLD_KKT - EXPECTED_KKT,
        "antifixed_pruned": EXPECTED_PRUNED,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
