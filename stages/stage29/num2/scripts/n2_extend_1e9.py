#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import bz2
import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
A8_PATH = ROOT / "stages/stage14/scripts/14-num-alpha8/segmented_production_census.py"
BASE_MANIFEST = ROOT / "stages/stage14/data/14-num-alpha11/b500m_manifest.json"
BASE_OBJECTS = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"
BASE_BOUND = 500_000_000
DEFAULT_BOUND = 1_000_000_000
CHECKPOINTS = (1_000_000, 5_000_000, 10_000_000, 50_000_000,
               100_000_000, 200_000_000, 500_000_000, 600_000_000,
               700_000_000, 800_000_000, 900_000_000, 1_000_000_000)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A8 = load_module("stage14_num_alpha8_reuse", A8_PATH)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_frozen_base():
    manifest = json.loads(BASE_MANIFEST.read_text(encoding="utf-8"))
    b64_bytes = BASE_OBJECTS.read_bytes()
    expected = manifest["object_source"]
    if sha256(b64_bytes) != expected["base64_file_sha256"]:
        raise ArithmeticError("B500m base64 file SHA mismatch")
    compressed = base64.b64decode(b64_bytes)
    if sha256(compressed) != expected["bz2_sha256"]:
        raise ArithmeticError("B500m bz2 SHA mismatch")
    raw = bz2.decompress(compressed)
    if sha256(raw) != expected["csv_sha256"]:
        raise ArithmeticError("B500m CSV SHA mismatch")

    objects = set()
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8")))
    for row in reader:
        rec = tuple(int(row[k]) for k in ("a", "b", "c", "d", "mask"))
        objects.add(rec)
    if len(objects) != expected["rows"]:
        raise ArithmeticError(f"B500m row mismatch: {len(objects)} != {expected['rows']}")
    summary = A8.NUM3.summarize(objects)
    want = manifest["exact_cutoff_B500m"]
    checks = A8.compare_summary(summary, want)
    if not all(checks.values()):
        raise ArithmeticError(f"B500m frozen summary mismatch: {checks}")
    if summary["counts"]["total"] != 3495 or summary["counts"]["triple"] != 0:
        raise ArithmeticError("B500m canonical N2 regression mismatch")
    return objects, manifest, checks


def checkpoint_summary(objects, B: int):
    s = A8.NUM3.summarize({r for r in objects if r[3] <= B})
    return {
        "B": B,
        "N2": s["counts"]["total"],
        "T": s["counts"]["triple"],
        "directional": {k: s["counts"][k] for k in ("a", "b", "c")},
        "distinct_at_least_two": s["distinct_physical_cuboids"],
        "object_key_sha256": s["object_key_sha256"],
        "object_key_mask_sha256": s["object_key_mask_sha256"],
    }


def cmd_scan(args):
    if args.lo <= BASE_BOUND:
        raise ValueError("num2 shell scan must start strictly above frozen B500m")
    objects, profile = A8.scan_range(args.lo, args.hi, args.segment_size, args.cache_limit)
    payload = {
        "algorithm": "stage29-num2-reuse-alpha8-diagonal-shard-v1",
        "range": [args.lo, args.hi],
        "objects": [list(r) for r in sorted(objects)],
        "profile": profile,
        "finite_data_is_not_asymptotic_theorem": True,
        "perfect_cuboid_nonexistence_claim": False,
    }
    args.output.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({"range": payload["range"], "objects": len(objects), "profile": profile}, indent=2, sort_keys=True))


def cmd_aggregate(args):
    base, base_manifest, base_checks = load_frozen_base()
    files = sorted(args.input_dir.glob("shard-*.json"))
    if not files:
        raise RuntimeError("no shard files found")

    shell = set()
    ranges = []
    profiles = []
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        lo, hi = map(int, data["range"])
        ranges.append((lo, hi))
        profiles.append(data["profile"])
        for row in data["objects"]:
            rec = tuple(int(x) for x in row)
            if rec[3] <= BASE_BOUND:
                raise ArithmeticError(f"shell record below base boundary: {rec}")
            if rec in shell:
                raise ArithmeticError(f"duplicate shell record: {rec}")
            shell.add(rec)

    pairs = sorted(zip(ranges, profiles), key=lambda x: x[0])
    expect = BASE_BOUND + 1
    for (lo, hi), _ in pairs:
        if lo != expect:
            raise ArithmeticError(f"shard coverage gap/overlap: expected {expect}, got {lo}")
        expect = hi + 1
    if expect != args.bound + 1:
        raise ArithmeticError(f"shell ends at {expect-1}, expected {args.bound}")

    if base & shell:
        raise ArithmeticError("base/shell object overlap")
    objects = base | shell
    checkpoints = [checkpoint_summary(objects, B) for B in CHECKPOINTS if B <= args.bound]
    cp = {x["B"]: x for x in checkpoints}
    if cp[200_000_000]["N2"] != 2457:
        raise ArithmeticError("B200m Stage14 alpha8 regression failed")
    if cp[500_000_000]["N2"] != 3495:
        raise ArithmeticError("B500m Stage14 alpha11 regression failed")

    full = A8.NUM3.summarize(objects)
    triples = [list(r) for r in sorted(objects) if r[4] == 0b111]
    if full["counts"]["total"] != cp[args.bound]["N2"]:
        raise ArithmeticError("endpoint count mismatch")

    source_profile = A8.write_object_source(objects, args.object_source)
    report = {
        "track": "Stage29-num2",
        "classification": "EXACT_FINITE_CANONICAL_N2_CENSUS_EXTENSION",
        "contract": {
            "population": "primitive canonical cuboids with exactly two integral face diagonals and integral space diagonal",
            "canonical": "0<a<b<c",
            "primitive": "gcd(a,b,c)=1",
            "cutoff": "R=d<=B",
            "space_diagonal_required": True,
            "face_multiplicity": "exactly two; triple-face records tracked separately as T",
        },
        "reuse": {
            "NUM_REUSE_PREFLIGHT": "PASS",
            "assets": ["NUM-R01", "NUM-R02", "NUM-R03"],
            "engine": "stages/stage14/scripts/14-num-alpha8/segmented_production_census.py",
            "frozen_base": "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64",
            "base_bound": BASE_BOUND,
            "base_sha_checks": base_checks,
        },
        "extension": {
            "bound": args.bound,
            "ranges": [list(r) for r, _ in pairs],
            "shell_objects_at_least_two": len(shell),
            "profiles": [p for _, p in pairs],
        },
        "checkpoints": checkpoints,
        "endpoint": {
            "N2": full["counts"]["total"],
            "T": full["counts"]["triple"],
            "directional": {k: full["counts"][k] for k in ("a", "b", "c")},
            "distinct_at_least_two": full["distinct_physical_cuboids"],
            "object_key_sha256": full["object_key_sha256"],
            "object_key_mask_sha256": full["object_key_mask_sha256"],
        },
        "perfect_cuboid_hits": triples,
        "object_source": source_profile,
        "guards": {
            "FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM": True,
            "PERFECT_CUBOID_NONEXISTENCE_CLAIM": False,
            "N2_TRUE_EXPONENT_INFERRED": False,
        },
    }
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("scan")
    sp.add_argument("--lo", type=int, required=True)
    sp.add_argument("--hi", type=int, required=True)
    sp.add_argument("--segment-size", type=int, default=250_000)
    sp.add_argument("--cache-limit", type=int, default=2_000_000)
    sp.add_argument("--output", type=Path, required=True)
    sp.set_defaults(func=cmd_scan)

    ag = sub.add_parser("aggregate")
    ag.add_argument("--input-dir", type=Path, required=True)
    ag.add_argument("--bound", type=int, default=DEFAULT_BOUND)
    ag.add_argument("--output", type=Path, required=True)
    ag.add_argument("--object-source", type=Path, required=True)
    ag.set_defaults(func=cmd_aggregate)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
