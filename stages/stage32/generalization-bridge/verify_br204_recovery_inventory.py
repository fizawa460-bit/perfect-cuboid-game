#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import tempfile
from pathlib import Path

UNIT_JOB_RE = re.compile(r"^units b(\d+) d(\d+)-(\d+)$")
COMPLETE_STEP = "Upload validated complete recovery payload"
PARTIAL_STEP = "Upload validated partial recovery payload"
PREFIX_STEP = "Upload validated carried complete prefix"
PARTIALS_STEP = "Upload validated carried partial bundle"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def unit_key(row: dict) -> tuple[int, int, int]:
    return int(row["b"]), int(row["d_lo"]), int(row["d_hi"])


def parse_jobs(path: Path) -> list[tuple[str, set[str]]]:
    out = []
    if not path.exists():
        return out
    for raw in path.read_text().splitlines():
        if not raw:
            continue
        parts = raw.split("\t", 1)
        name = parts[0]
        steps = set(parts[1].split("\x1f")) if len(parts) == 2 and parts[1] else set()
        out.append((name, steps))
    return out


def parse_artifacts(path: Path) -> list[dict]:
    out = []
    if not path.exists():
        return out
    for raw in path.read_text().splitlines():
        if not raw:
            continue
        aid, name, expired = raw.split("\t")
        out.append({"id": int(aid), "name": name, "expired": expired == "true"})
    return out


def load_complete(path: Path) -> set[tuple[int, int, int]]:
    if not path.exists():
        return set()
    x = json.loads(path.read_text())
    req(x.get("schema") == "STAGE32_BR204_RECOVERY_PREFIX_V1", f"bad complete manifest schema {path}")
    rows = {unit_key(r) for r in x.get("subunits", [])}
    req(len(rows) == int(x.get("validated_subunit_count", -1)), f"complete manifest count drift {path}")
    return rows


def load_partial(path: Path) -> set[tuple[int, int, int]]:
    if not path.exists():
        return set()
    x = json.loads(path.read_text())
    req(x.get("schema") == "STAGE32_BR204_PARTIAL_BAND_BUNDLE_V3_LINEAGE", f"bad partial manifest schema {path}")
    rows = {unit_key(r) for r in x.get("partial_bands", [])}
    req(len(rows) == int(x.get("validated_partial_band_count", -1)), f"partial manifest count drift {path}")
    return rows


def prior_manifest_units(root: Path, pattern: str, loader) -> set[tuple[int, int, int]]:
    out: set[tuple[int, int, int]] = set()
    if not root.exists():
        return out
    for p in root.rglob(pattern):
        rows = loader(p)
        overlap = out & rows
        req(not overlap, f"duplicate prior manifest units {sorted(overlap)}")
        out |= rows
    return out


def reconcile(
    jobs_tsv: Path,
    artifacts_tsv: Path,
    complete_manifest: Path,
    partial_manifest: Path,
    prior_prefix_dir: Path,
    prior_partials_dir: Path,
) -> dict:
    jobs = parse_jobs(jobs_tsv)
    artifacts = parse_artifacts(artifacts_tsv)

    expected_names: set[str] = set()
    expected_complete: set[tuple[int, int, int]] = set()
    expected_partial: set[tuple[int, int, int]] = set()

    for name, steps in jobs:
        complete_ok = COMPLETE_STEP in steps
        partial_ok = PARTIAL_STEP in steps
        req(not (complete_ok and partial_ok), f"both complete and partial uploads succeeded in job {name}")

        if name == "carry":
            if PREFIX_STEP in steps:
                expected_names.add("br204-prefix")
            if PARTIALS_STEP in steps:
                expected_names.add("br204-partials")
            continue

        if name == "pilot_low":
            key = (0, 8, 54)
        elif name == "pilot_high":
            key = (96, 148, 192)
        else:
            m = UNIT_JOB_RE.match(name)
            if not m:
                continue
            key = tuple(map(int, m.groups()))

        b, d_lo, d_hi = key
        if complete_ok:
            expected_complete.add(key)
            expected_names.add(f"br204-u-b{b}-d{d_lo}-{d_hi}")
        if partial_ok:
            expected_partial.add(key)
            expected_names.add(f"br204-p-b{b}-d{d_lo}-{d_hi}")

    by_name: dict[str, list[dict]] = {}
    for row in artifacts:
        by_name.setdefault(row["name"], []).append(row)

    missing_names = []
    expired_expected = []
    duplicate_expected = []
    for name in sorted(expected_names):
        rows = by_name.get(name, [])
        if not rows:
            missing_names.append(name)
            continue
        live = [r for r in rows if not r["expired"]]
        expired = [r for r in rows if r["expired"]]
        if expired:
            expired_expected.append(name)
        if len(live) != 1:
            duplicate_expected.append({"name": name, "live_count": len(live), "total_count": len(rows)})

    complete = load_complete(complete_manifest)
    partial = load_partial(partial_manifest)
    prior_complete = prior_manifest_units(prior_prefix_dir, "RECOVERY-MANIFEST.json", load_complete)
    prior_partial = prior_manifest_units(prior_partials_dir, "PARTIAL-MANIFEST.json", load_partial)

    missing_complete_identities = sorted((expected_complete | prior_complete) - complete)
    missing_partial_identities = sorted((expected_partial | prior_partial) - partial - complete)

    relevant_expired = sorted(
        r["name"] for r in artifacts
        if r["expired"] and (
            r["name"] in expected_names
            or r["name"].startswith("br204-u-")
            or r["name"].startswith("br204-p-")
            or r["name"] in {"br204-prefix", "br204-partials"}
        )
    )

    result = {
        "schema": "STAGE32_BR204_RECOVERY_INVENTORY_RECONCILIATION_V1",
        "job_count": len(jobs),
        "discovered_artifact_count": len(artifacts),
        "expected_durable_artifact_count": len(expected_names),
        "retrieved_live_expected_durable_artifact_count": sum(
            1 for n in expected_names
            if len([r for r in by_name.get(n, []) if not r["expired"]]) == 1
        ),
        "expected_direct_complete_unit_count": len(expected_complete),
        "expected_direct_partial_unit_count": len(expected_partial),
        "expected_prior_prefix_unit_count": len(prior_complete),
        "expected_prior_partial_unit_count": len(prior_partial),
        "validated_carried_complete_unit_count": len(complete),
        "validated_carried_partial_unit_count": len(partial),
        "missing_expected_artifact_names": missing_names,
        "expired_expected_artifact_names": sorted(set(expired_expected)),
        "duplicate_expected_artifacts": duplicate_expected,
        "relevant_expired_artifact_names": relevant_expired,
        "missing_expected_complete_identities": [list(x) for x in missing_complete_identities],
        "missing_expected_partial_identities": [list(x) for x in missing_partial_identities],
    }
    result["recovery_inventory_reconciled"] = not any([
        missing_names,
        expired_expected,
        duplicate_expected,
        missing_complete_identities,
        missing_partial_identities,
    ])
    req(result["recovery_inventory_reconciled"], json.dumps(result, sort_keys=True))
    return result


def self_test() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        jobs = root / "jobs.tsv"
        artifacts = root / "artifacts.tsv"
        complete = root / "RECOVERY-MANIFEST.json"
        partial = root / "PARTIAL-MANIFEST.json"
        prior_prefix = root / "prior-prefix"
        prior_partials = root / "prior-partials"
        prior_prefix.mkdir()
        prior_partials.mkdir()

        jobs.write_text(
            "units b1 d56-100\tRun actions/checkout@v4\x1f" + COMPLETE_STEP + "\n"
        )
        artifacts.write_text("7\tbr204-u-b1-d56-100\tfalse\n")
        complete.write_text(json.dumps({
            "schema": "STAGE32_BR204_RECOVERY_PREFIX_V1",
            "validated_subunit_count": 1,
            "subunits": [{"b": 1, "d_lo": 56, "d_hi": 100}],
        }))
        partial.write_text(json.dumps({
            "schema": "STAGE32_BR204_PARTIAL_BAND_BUNDLE_V3_LINEAGE",
            "validated_partial_band_count": 0,
            "partial_bands": [],
        }))
        ok = reconcile(jobs, artifacts, complete, partial, prior_prefix, prior_partials)
        req(ok["recovery_inventory_reconciled"], "positive reconciliation self-test")

        artifacts.write_text("")
        failed = False
        try:
            reconcile(jobs, artifacts, complete, partial, prior_prefix, prior_partials)
        except SystemExit as exc:
            failed = "missing_expected_artifact_names" in str(exc)
        req(failed, "omitted expected durable artifact must fail closed")
    print("PASS BR204 recovery inventory reconciliation self-test")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--jobs-tsv")
    ap.add_argument("--artifacts-tsv")
    ap.add_argument("--complete-manifest")
    ap.add_argument("--partial-manifest")
    ap.add_argument("--prior-prefix-dir")
    ap.add_argument("--prior-partials-dir")
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return
    for k in (
        "jobs_tsv", "artifacts_tsv", "complete_manifest", "partial_manifest",
        "prior_prefix_dir", "prior_partials_dir", "out",
    ):
        req(getattr(a, k) is not None, f"--{k.replace('_','-')} required")
    result = reconcile(
        Path(a.jobs_tsv), Path(a.artifacts_tsv),
        Path(a.complete_manifest), Path(a.partial_manifest),
        Path(a.prior_prefix_dir), Path(a.prior_partials_dir),
    )
    Path(a.out).write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
