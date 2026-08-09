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
ALPHA9_MANIFEST = ROOT / "stages/stage14/data/14-num-alpha9/b300m_manifest.json"
NUM3_SCRIPT = ROOT / "stages/stage14/scripts/14-num3/extended_exact_census.py"

B250 = 250_000_000
B300 = 300_000_000
B400 = 400_000_000
STABILITY_THRESHOLD = 0.02


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


NUM3 = load_module("stage14_num3_alpha10", NUM3_SCRIPT)


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


def alpha9_targets():
    m = json.loads(ALPHA9_MANIFEST.read_text(encoding="utf-8"))
    return m["exact_cutoff_B250m"], m["exact_cutoff_B300m"]


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
        data = json.loads(p.read_text(encoding="utf-8"))
        lo, hi = map(int, data["range"])
        ranges.append((lo, hi))
        profiles.append(data["profile"])
        for row in data["objects"]:
            rec = tuple(map(int, row))
            if rec in objects:
                raise ArithmeticError(f"duplicate record across new shards: {rec}")
            objects.add(rec)
    ranges.sort()
    expected = [
        (300_000_001, 325_000_000),
        (325_000_001, 350_000_000),
        (350_000_001, 375_000_000),
        (375_000_001, 400_000_000),
    ]
    if ranges != expected:
        raise ArithmeticError(f"new shard coverage mismatch: {ranges}")
    if any(r[3] <= B300 or r[3] > B400 for r in objects):
        raise ArithmeticError("new-shard object outside (B300,B400]")
    return objects, [{"range": list(r), "profile": p} for r, p in zip(ranges, profiles)]


def build_report(objects, generation: dict, source_profile: dict):
    want250, want300 = alpha9_targets()
    s250 = summary_at(objects, B250)
    s300 = summary_at(objects, B300)
    c250 = compare_summary(s250, want250)
    c300 = compare_summary(s300, want300)
    if not all(c250.values()):
        raise ArithmeticError(f"B250 alpha9 nested regression mismatch: {c250}")
    if not all(c300.values()):
        raise ArithmeticError(f"B300 alpha9 nested regression mismatch: {c300}")

    s400 = summary_at(objects, B400)
    if len(objects) != s400["distinct_physical_cuboids"]:
        raise ArithmeticError("B400 source has rows beyond checkpoint or duplicate keys")

    p250, p300, p400 = panel(s250, B250), panel(s300, B300), panel(s400, B400)
    transitions = [transition(p250, p300), transition(p300, p400)]
    emergency = s400["counts"]["triple"] > 0

    return {
        "stage": "14-num-alpha10",
        "classification": "FINITE_EXACT_ALPHA_B400M_STABILITY_CHECKPOINT",
        "generation": generation,
        "B250m_alpha9_regression": {
            "all_fields_equal": True,
            "checks": c250,
            "summary": s250,
        },
        "B300m_alpha9_regression": {
            "all_fields_equal": True,
            "checks": c300,
            "summary": s300,
        },
        "exact_cutoff_B400m": s400,
        "shell_300m_to_400m_counts": shell_counts(objects, B300, B400),
        "stability_panel": {
            "threshold_relative_drift": STABILITY_THRESHOLD,
            "definition": "abs(R_new-R_old)/max(abs(R_new),1e-30)",
            "checkpoints": [p250, p300, p400],
            "transitions": transitions,
            "terminal_stop_gate_evaluated": False,
            "terminal_stop_gate_reason": "alpha11 still requires the 400m->500m transition before the three-transition terminal gate can be evaluated",
        },
        "object_source": source_profile,
        "decision": {
            "STAGE14_NUM_ALPHA10": "PAUSED_PERFECT_CUBOID_EMERGENCY_PROTOCOL" if emergency else "COMPLETE_EXACT_B400M_CHECKPOINT",
            "B250M_ALPHA9_FULL_HASH_REGRESSION_MATCH": True,
            "B300M_ALPHA9_FULL_HASH_REGRESSION_MATCH": True,
            "B400M_EXACT_CENSUS_FROZEN": True,
            "STABILITY_250M_TO_300M_PRESERVED": transitions[0]["all_primary_at_or_below_2pct"],
            "B300M_TO_B400M_ALL_PRIMARY_DRIFTS_LE_2PCT": transitions[1]["all_primary_at_or_below_2pct"],
            "PERFECT_CUBOID_EMERGENCY": emergency,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "ASYMPTOTIC_CLAIM": False,
            "STABILITY_GATE_IS_HEURISTIC": True,
            "TERMINAL_STOP_GATE_EVALUATED": False,
            "NEXT": "Stage14-num-alpha11 exact B500m terminal checkpoint and stability stop gate",
        },
    }


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--fresh-shard-dir", type=Path)
    src.add_argument("--replay-b400-source", type=Path)
    ap.add_argument("--baseline-b300-source", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--b400-source-out", type=Path)
    args = ap.parse_args()

    if args.fresh_shard_dir:
        if args.baseline_b300_source is None or args.b400_source_out is None:
            raise SystemExit("fresh mode requires --baseline-b300-source and --b400-source-out")
        baseline = decode_source(args.baseline_b300_source)
        new, shard_meta = load_new_shards(args.fresh_shard_dir)
        overlap = baseline.intersection(new)
        if overlap:
            raise ArithmeticError(f"baseline/new overlap: {next(iter(overlap))}")
        objects = baseline | new
        source_profile = write_source(objects, args.b400_source_out)
        generation = {
            "mode": "frozen_alpha9_b300_baseline_plus_four_new_25m_shards",
            "baseline_rows": len(baseline),
            "new_rows": len(new),
            "new_shards": shard_meta,
        }
    else:
        objects = decode_source(args.replay_b400_source)
        tmp = args.output.with_suffix(".tmp.b64")
        source_profile = write_source(objects, tmp)
        tmp.unlink()
        generation = {
            "mode": "frozen_b400_replay",
            "rows": len(objects),
        }

    report = build_report(objects, generation, source_profile)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "decision": report["decision"],
        "B400": report["exact_cutoff_B400m"]["counts"],
        "shell_300m_to_400m": report["shell_300m_to_400m_counts"],
        "stability": report["stability_panel"],
    }, indent=2, sort_keys=True))

    if report["decision"]["PERFECT_CUBOID_EMERGENCY"]:
        raise SystemExit("PERFECT CUBOID EMERGENCY: independent ordinary/reference verification required")


if __name__ == "__main__":
    main()
