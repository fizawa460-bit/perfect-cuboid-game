#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import bz2
import csv
import importlib.util
import io
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ALPHA8_SCRIPT = ROOT / "stages/stage14/scripts/14-num-alpha8/segmented_production_census.py"
ALPHA8_MANIFEST = ROOT / "stages/stage14/data/14-num-alpha8/b200m_manifest.json"
NUM3_SCRIPT = ROOT / "stages/stage14/scripts/14-num3/extended_exact_census.py"

B200 = 200_000_000
B250 = 250_000_000
B300 = 300_000_000
STABILITY_THRESHOLD = 0.02


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A8 = load_module("stage14_num_alpha8_prod", ALPHA8_SCRIPT)
NUM3 = load_module("stage14_num3_alpha9", NUM3_SCRIPT)


def decode_source(path: Path):
    encoded = "".join(path.read_text(encoding="ascii").split())
    raw = bz2.decompress(base64.b64decode(encoded)).decode("utf-8")
    rows = []
    for r in csv.DictReader(io.StringIO(raw)):
        rows.append(tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")))
    if len(rows) != len(set(rows)):
        raise ArithmeticError("duplicate rows in object source")
    return set(rows)


def write_source(objects, path: Path):
    rows = ["a,b,c,d,mask"]
    rows.extend(",".join(map(str, r)) for r in sorted(objects))
    raw = ("\n".join(rows) + "\n").encode("utf-8")
    packed = bz2.compress(raw, compresslevel=9)
    encoded = base64.b64encode(packed).decode("ascii")
    path.write_text(encoded + "\n", encoding="ascii")
    import hashlib
    return {
        "rows": len(objects),
        "raw_bytes": len(raw),
        "bz2_bytes": len(packed),
        "base64_chars": len(encoded),
        "csv_sha256": hashlib.sha256(raw).hexdigest(),
        "bz2_sha256": hashlib.sha256(packed).hexdigest(),
        "base64_file_sha256": hashlib.sha256((encoded + "\n").encode("ascii")).hexdigest(),
    }


def compare_summary(got: dict, want: dict):
    return {
        "counts": got["counts"] == want["counts"],
        "distinct_physical_cuboids": got["distinct_physical_cuboids"] == want["distinct_physical_cuboids"],
        "object_key_sha256": got["object_key_sha256"] == want["object_key_sha256"],
        "object_key_mask_sha256": got["object_key_mask_sha256"] == want["object_key_mask_sha256"],
        "active_oriented_face_vertices": got["graph"]["active_oriented_face_vertices"] == want["graph"]["active_oriented_face_vertices"],
        "raw_pair_edges": got["graph"]["raw_pair_edges"] == want["graph"]["raw_pair_edges"],
        "max_degree": got["graph"]["max_degree"] == want["graph"]["max_degree"],
        "vertex_ledger_sha256": got["graph"]["vertex_ledger_sha256"] == want["graph"]["vertex_ledger_sha256"],
        "edge_ledger_sha256": got["graph"]["edge_ledger_sha256"] == want["graph"]["edge_ledger_sha256"],
    }


def alpha8_target():
    m = json.loads(ALPHA8_MANIFEST.read_text(encoding="utf-8"))
    return m["exact_cutoff_B200m"]


def summary_at(objects, bound: int):
    return NUM3.summarize({r for r in objects if r[3] <= bound})


def panel(summary: dict, bound: int):
    n = summary["counts"]["total"]
    if n <= 0:
        raise ArithmeticError("empty checkpoint")
    return {
        "B": bound,
        "R0_N2_over_sqrt_B": n / math.sqrt(bound),
        "Ra": summary["counts"]["a"] / n,
        "Rb": summary["counts"]["b"] / n,
        "Rc": summary["counts"]["c"] / n,
        "Rg_active_faces_over_N2": summary["graph"]["active_oriented_face_vertices"] / n,
    }


def relative_drift(old: float, new: float):
    return abs(new - old) / max(abs(new), 1e-30)


def transition(old: dict, new: dict):
    keys = ("R0_N2_over_sqrt_B", "Ra", "Rb", "Rc", "Rg_active_faces_over_N2")
    drift = {k: relative_drift(old[k], new[k]) for k in keys}
    return {
        "from_B": old["B"],
        "to_B": new["B"],
        "relative_drift": drift,
        "all_primary_at_or_below_2pct": all(v <= STABILITY_THRESHOLD for v in drift.values()),
    }


def shell_counts(objects, lo: int, hi: int):
    rows = [r for r in objects if lo < r[3] <= hi]
    out = {"a": 0, "b": 0, "c": 0, "total": 0, "triple": 0}
    for r in rows:
        mask = r[4]
        if mask == 0b011:
            q = "a"
        elif mask == 0b101:
            q = "b"
        elif mask == 0b110:
            q = "c"
        elif mask == 0b111:
            q = "triple"
        else:
            raise ArithmeticError(f"unexpected shell mask {mask}")
        out[q] += 1
        if q != "triple":
            out["total"] += 1
    return out


def load_new_shards(root: Path):
    paths = sorted(root.glob("shard-*.json"))
    if len(paths) != 4:
        raise ArithmeticError(f"expected 4 new shards, got {len(paths)}")
    ranges = []
    objects = set()
    profiles = []
    for p in paths:
        d = json.loads(p.read_text(encoding="utf-8"))
        lo, hi = map(int, d["range"])
        ranges.append((lo, hi))
        profiles.append(d["profile"])
        for row in d["objects"]:
            rec = tuple(map(int, row))
            if rec in objects:
                raise ArithmeticError(f"duplicate record across new shards: {rec}")
            objects.add(rec)
    ranges.sort()
    expected = [
        (200_000_001, 225_000_000),
        (225_000_001, 250_000_000),
        (250_000_001, 275_000_000),
        (275_000_001, 300_000_000),
    ]
    if ranges != expected:
        raise ArithmeticError(f"new shard coverage mismatch: {ranges}")
    if any(r[3] <= B200 or r[3] > B300 for r in objects):
        raise ArithmeticError("new-shard object outside (B200,B300]")
    return objects, [{"range": list(r), "profile": p} for r, p in zip(ranges, profiles)]


def build_report(objects, generation: dict, source_profile: dict):
    s200 = summary_at(objects, B200)
    want200 = alpha8_target()
    checks = compare_summary(s200, want200)
    if not all(checks.values()):
        raise ArithmeticError(f"B200 alpha8 nested regression mismatch: {checks}")

    s250 = summary_at(objects, B250)
    s300 = summary_at(objects, B300)
    if len(objects) != s300["distinct_physical_cuboids"]:
        raise ArithmeticError("B300 source has rows beyond checkpoint or duplicate keys")

    p200, p250, p300 = panel(s200, B200), panel(s250, B250), panel(s300, B300)
    transitions = [transition(p200, p250), transition(p250, p300)]
    emergency = any(s["counts"]["triple"] > 0 for s in (s250, s300))

    report = {
        "stage": "14-num-alpha9",
        "classification": "FINITE_EXACT_NESTED_ALPHA_STABILITY_CHECKPOINTS",
        "generation": generation,
        "B200m_alpha8_regression": {
            "all_fields_equal": True,
            "checks": checks,
            "summary": s200,
        },
        "exact_cutoff_B250m": s250,
        "exact_cutoff_B300m": s300,
        "shell_200m_to_250m_counts": shell_counts(objects, B200, B250),
        "shell_250m_to_300m_counts": shell_counts(objects, B250, B300),
        "stability_panel": {
            "threshold_relative_drift": STABILITY_THRESHOLD,
            "definition": "abs(R_new-R_old)/max(abs(R_new),1e-30)",
            "checkpoints": [p200, p250, p300],
            "transitions": transitions,
            "terminal_stop_gate_evaluated": False,
            "terminal_stop_gate_reason": "alpha11 requires 250m->300m, 300m->400m, and 400m->500m",
        },
        "object_source": source_profile,
        "decision": {
            "STAGE14_NUM_ALPHA9": "PAUSED_PERFECT_CUBOID_EMERGENCY_PROTOCOL" if emergency else "COMPLETE_EXACT_B300M_WITH_B250M_CHECKPOINT",
            "B200M_ALPHA8_FULL_HASH_REGRESSION_MATCH": True,
            "B250M_EXACT_CENSUS_FROZEN": True,
            "B300M_EXACT_CENSUS_FROZEN": True,
            "FIRST_POST_B200M_STABILITY_PANEL_PUBLISHED": True,
            "PERFECT_CUBOID_EMERGENCY": emergency,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "ASYMPTOTIC_CLAIM": False,
            "STABILITY_GATE_IS_HEURISTIC": True,
            "NEXT": "Stage14-num-alpha10 exact B400m checkpoint",
        },
    }
    return report


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--fresh-shard-dir", type=Path)
    src.add_argument("--replay-b300-source", type=Path)
    ap.add_argument("--baseline-b200-source", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--b300-source-out", type=Path)
    args = ap.parse_args()

    if args.fresh_shard_dir:
        if args.baseline_b200_source is None or args.b300_source_out is None:
            raise SystemExit("fresh mode requires --baseline-b200-source and --b300-source-out")
        baseline = decode_source(args.baseline_b200_source)
        new, shard_meta = load_new_shards(args.fresh_shard_dir)
        overlap = baseline.intersection(new)
        if overlap:
            raise ArithmeticError(f"baseline/new overlap: {next(iter(overlap))}")
        objects = baseline | new
        source_profile = write_source(objects, args.b300_source_out)
        generation = {
            "mode": "alpha8_artifact_baseline_plus_four_new_25m_shards",
            "baseline_rows": len(baseline),
            "new_rows": len(new),
            "new_shards": shard_meta,
        }
    else:
        objects = decode_source(args.replay_b300_source)
        tmp = args.output.with_suffix(".tmp.b64")
        source_profile = write_source(objects, tmp)
        tmp.unlink()
        generation = {
            "mode": "frozen_b300_replay",
            "rows": len(objects),
        }

    report = build_report(objects, generation, source_profile)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "decision": report["decision"],
        "B250": report["exact_cutoff_B250m"]["counts"],
        "B300": report["exact_cutoff_B300m"]["counts"],
        "stability": report["stability_panel"],
    }, indent=2, sort_keys=True))

    if report["decision"]["PERFECT_CUBOID_EMERGENCY"]:
        raise SystemExit("PERFECT CUBOID EMERGENCY: independent ordinary/reference verification required")


if __name__ == "__main__":
    main()
