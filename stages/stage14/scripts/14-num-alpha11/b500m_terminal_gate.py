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
ALPHA10_MANIFEST = ROOT / "stages/stage14/data/14-num-alpha10/b400m_manifest.json"
NUM3_SCRIPT = ROOT / "stages/stage14/scripts/14-num3/extended_exact_census.py"

B250 = 250_000_000
B300 = 300_000_000
B400 = 400_000_000
B500 = 500_000_000
STABILITY_THRESHOLD = 0.02
PRIMARY_KEYS = (
    "R0_N2_over_sqrt_B",
    "Ra",
    "Rb",
    "Rc",
    "Rg_active_faces_over_N2",
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


NUM3 = load_module("stage14_num3_alpha11", NUM3_SCRIPT)


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


def alpha10_targets():
    m = json.loads(ALPHA10_MANIFEST.read_text(encoding="utf-8"))
    return (
        m["B250m_alpha9_regression"]["summary"],
        m["B300m_alpha9_regression"]["summary"],
        m["exact_cutoff_B400m"],
    )


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
    drift = {k: relative_drift(old[k], new[k]) for k in PRIMARY_KEYS}
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
        (400_000_001, 425_000_000),
        (425_000_001, 450_000_000),
        (450_000_001, 475_000_000),
        (475_000_001, 500_000_000),
    ]
    if ranges != expected:
        raise ArithmeticError(f"new shard coverage mismatch: {ranges}")
    if any(r[3] <= B400 or r[3] > B500 for r in objects):
        raise ArithmeticError("new-shard object outside (B400,B500]")
    return objects, [{"range": list(r), "profile": p} for r, p in zip(ranges, profiles)]


def build_report(objects, generation: dict, source_profile: dict):
    want250, want300, want400 = alpha10_targets()
    s250 = summary_at(objects, B250)
    s300 = summary_at(objects, B300)
    s400 = summary_at(objects, B400)
    c250 = compare_summary(s250, want250)
    c300 = compare_summary(s300, want300)
    c400 = compare_summary(s400, want400)
    if not all(c250.values()):
        raise ArithmeticError(f"B250 alpha10 nested regression mismatch: {c250}")
    if not all(c300.values()):
        raise ArithmeticError(f"B300 alpha10 nested regression mismatch: {c300}")
    if not all(c400.values()):
        raise ArithmeticError(f"B400 alpha10 nested regression mismatch: {c400}")

    s500 = summary_at(objects, B500)
    if len(objects) != s500["distinct_physical_cuboids"]:
        raise ArithmeticError("B500 source has rows beyond checkpoint or duplicate keys")

    checkpoints = [
        panel(s250, B250),
        panel(s300, B300),
        panel(s400, B400),
        panel(s500, B500),
    ]
    transitions = [transition(checkpoints[i], checkpoints[i + 1]) for i in range(3)]
    terminal_passed = all(t["all_primary_at_or_below_2pct"] for t in transitions)
    failed = [
        {"from_B": t["from_B"], "to_B": t["to_B"]}
        for t in transitions
        if not t["all_primary_at_or_below_2pct"]
    ]
    emergency = s500["counts"]["triple"] > 0
    next_stage = (
        "Stage14-num-alpha observational pause after passed B500m stability gate"
        if terminal_passed
        else "Stage14-num-alpha12 continue exact census beyond B500m after failed stability gate"
    )

    return {
        "stage": "14-num-alpha11",
        "classification": "FINITE_EXACT_ALPHA_B500M_TERMINAL_STABILITY_GATE",
        "generation": generation,
        "B250m_alpha10_regression": {
            "all_fields_equal": True,
            "checks": c250,
            "summary": s250,
        },
        "B300m_alpha10_regression": {
            "all_fields_equal": True,
            "checks": c300,
            "summary": s300,
        },
        "B400m_alpha10_regression": {
            "all_fields_equal": True,
            "checks": c400,
            "summary": s400,
        },
        "exact_cutoff_B500m": s500,
        "shell_400m_to_500m_counts": shell_counts(objects, B400, B500),
        "stability_panel": {
            "threshold_relative_drift": STABILITY_THRESHOLD,
            "definition": "abs(R_new-R_old)/max(abs(R_new),1e-30)",
            "primary_metrics": list(PRIMARY_KEYS),
            "checkpoints": checkpoints,
            "transitions": transitions,
        },
        "terminal_stop_gate": {
            "evaluated": True,
            "rule": "all five primary metrics must have relative drift <=2% on each of 250m->300m, 300m->400m, and 400m->500m",
            "passed": terminal_passed,
            "failed_transitions": failed,
            "interpretation": "operational finite-data stopping convention only; not an asymptotic theorem or confidence interval",
        },
        "object_source": source_profile,
        "decision": {
            "STAGE14_NUM_ALPHA11": "PAUSED_PERFECT_CUBOID_EMERGENCY_PROTOCOL" if emergency else "COMPLETE_EXACT_B500M_TERMINAL_GATE_EVALUATED",
            "B250M_ALPHA10_FULL_HASH_REGRESSION_MATCH": True,
            "B300M_ALPHA10_FULL_HASH_REGRESSION_MATCH": True,
            "B400M_ALPHA10_FULL_HASH_REGRESSION_MATCH": True,
            "B500M_EXACT_CENSUS_FROZEN": True,
            "B250M_TO_B300M_ALL_PRIMARY_DRIFTS_LE_2PCT": transitions[0]["all_primary_at_or_below_2pct"],
            "B300M_TO_B400M_ALL_PRIMARY_DRIFTS_LE_2PCT": transitions[1]["all_primary_at_or_below_2pct"],
            "B400M_TO_B500M_ALL_PRIMARY_DRIFTS_LE_2PCT": transitions[2]["all_primary_at_or_below_2pct"],
            "TERMINAL_STOP_GATE_EVALUATED": True,
            "TERMINAL_STOP_GATE_PASSED": terminal_passed,
            "PERFECT_CUBOID_EMERGENCY": emergency,
            "FINITE_DIAGNOSTIC_ONLY": True,
            "ASYMPTOTIC_CLAIM": False,
            "STABILITY_GATE_IS_HEURISTIC": True,
            "NEXT": next_stage,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--fresh-shard-dir", type=Path)
    src.add_argument("--replay-b500-source", type=Path)
    ap.add_argument("--baseline-b400-source", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--b500-source-out", type=Path)
    args = ap.parse_args()

    if args.fresh_shard_dir:
        if args.baseline_b400_source is None or args.b500_source_out is None:
            raise SystemExit("fresh mode requires --baseline-b400-source and --b500-source-out")
        baseline = decode_source(args.baseline_b400_source)
        new, shard_meta = load_new_shards(args.fresh_shard_dir)
        overlap = baseline.intersection(new)
        if overlap:
            raise ArithmeticError(f"baseline/new overlap: {next(iter(overlap))}")
        objects = baseline | new
        source_profile = write_source(objects, args.b500_source_out)
        generation = {
            "mode": "frozen_alpha10_b400_baseline_plus_four_new_25m_shards",
            "baseline_rows": len(baseline),
            "new_rows": len(new),
            "new_shards": shard_meta,
        }
    else:
        objects = decode_source(args.replay_b500_source)
        tmp = args.output.with_suffix(".tmp.b64")
        source_profile = write_source(objects, tmp)
        tmp.unlink()
        generation = {
            "mode": "frozen_b500_replay",
            "rows": len(objects),
        }

    report = build_report(objects, generation, source_profile)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "decision": report["decision"],
        "B500": report["exact_cutoff_B500m"]["counts"],
        "shell_400m_to_500m": report["shell_400m_to_500m_counts"],
        "stability": report["stability_panel"],
        "terminal_stop_gate": report["terminal_stop_gate"],
    }, indent=2, sort_keys=True))

    if report["decision"]["PERFECT_CUBOID_EMERGENCY"]:
        raise SystemExit("PERFECT CUBOID EMERGENCY: independent ordinary/reference verification required")


if __name__ == "__main__":
    main()
