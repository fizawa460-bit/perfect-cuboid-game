#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import bc2_40_resume_aggregate as agg
import bc2_40_replay_explicit_fresh_unknown23 as b40

RUNKEY_SCHEMA = "STAGE32EX5_BC2_40_RESUME_RUNKEY_V2"
TARGET_COUNT = 23
TARGET_SHA = "29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02"
TIMEOUT_MS = 180000
UNIT_MAX_BYTES = 131072
AGGREGATE_MAX_BYTES = 524288
RECOVERY_MAX_BYTES = 131072
CARRY_RELATIVE = "stages/stage32-ex5/breadth-cycle-2/bc2-40-resume-carry"

def read_json(path: Path):
    return json.loads(path.read_text())

def load_expected():
    cp = b40.load_target()
    expected = [int(v) for v in cp["replay"]["unknown_parent_indices"]]
    if len(expected) != TARGET_COUNT or agg.csha(expected) != TARGET_SHA:
        raise ValueError("BC2-40 target drift")
    return expected

def validate_runkey(path: Path, expected: list[int]):
    o = read_json(path)
    q = dict(o)
    got = q.pop("canonical_sha256_without_this_field", None)
    if got != agg.csha(q):
        raise ValueError("runkey canonical drift")
    if o.get("schema") != RUNKEY_SCHEMA:
        raise ValueError("runkey schema")
    if o.get("armed") is not True:
        raise ValueError("runkey not armed")
    generation = o.get("generation")
    if not isinstance(generation, int) or generation < 1:
        raise ValueError("runkey generation")
    target = o.get("target", {})
    if target.get("fresh_unknown_parent_count") != TARGET_COUNT:
        raise ValueError("runkey target count")
    if target.get("fresh_unknown_parent_indices_sha256") != TARGET_SHA:
        raise ValueError("runkey target hash")
    ex = o.get("execution", {})
    if ex.get("per_parent_timeout_ms") != TIMEOUT_MS:
        raise ValueError("runkey timeout")
    if ex.get("effective_heavy_concurrency") != 1:
        raise ValueError("runkey concurrency")
    if ex.get("heavy_scaleout_authorized") is not False:
        raise ValueError("runkey scaleout")
    resume = o.get("resume", {})
    if resume.get("partition_key") != "parent_index":
        raise ValueError("runkey partition key")
    if resume.get("carry_dir") != CARRY_RELATIVE:
        raise ValueError("runkey carry dir")
    carried = resume.get("carried_parent_indices")
    missing = resume.get("missing_parent_indices")
    if not isinstance(carried, list) or not isinstance(missing, list):
        raise ValueError("runkey resume lists")
    carried = [int(v) for v in carried]
    missing = [int(v) for v in missing]
    if len(carried) != len(set(carried)) or len(missing) != len(set(missing)):
        raise ValueError("runkey duplicate indices")
    if set(carried) & set(missing):
        raise ValueError("runkey overlap")
    if carried != [i for i in expected if i in set(carried)]:
        raise ValueError("runkey carried order")
    if missing != [i for i in expected if i in set(missing)]:
        raise ValueError("runkey missing order")
    if set(carried) | set(missing) != set(expected):
        raise ValueError("runkey exact union")
    if resume.get("schedule_only_missing_parent_indices") != missing:
        raise ValueError("runkey recovery schedule")
    if generation == 1 and carried:
        raise ValueError("generation1 cannot claim carried units")
    return o, carried, missing

def load_carry(carry_dir: Path, expected_carried: list[int]):
    by_idx = {}
    if carry_dir.exists():
        if not carry_dir.is_dir():
            raise ValueError("carry path is not a directory")
        paths = sorted(carry_dir.glob("parent-*.json"))
    else:
        paths = []
    for p in paths:
        if p.stat().st_size > UNIT_MAX_BYTES:
            raise ValueError(f"carry unit too large: {p}")
        u = agg.checked_unit(p)
        idx = int(u["parent_index"])
        if idx in by_idx:
            raise ValueError(f"duplicate carried parent {idx}")
        by_idx[idx] = p
    actual = [idx for idx in load_expected() if idx in by_idx]
    if actual != expected_carried:
        raise ValueError(f"carry set mismatch: expected {expected_carried}, actual {actual}")
    return by_idx

def run_aggregate(units_dir: Path, output: Path, allow_partial: bool):
    cmd = [
        sys.executable,
        str(Path(__file__).resolve().parent / "bc2_40_resume_aggregate.py"),
        "--units-dir",
        str(units_dir),
        "--output",
        str(output),
    ]
    if allow_partial:
        cmd.append("--allow-partial")
    subprocess.run(cmd, check=True)
    size = output.stat().st_size
    limit = RECOVERY_MAX_BYTES if allow_partial else AGGREGATE_MAX_BYTES
    if size > limit:
        raise ValueError(f"aggregate output too large: {size}>{limit}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runkey", type=Path, required=True)
    ap.add_argument("--carry-dir", type=Path, required=True)
    ap.add_argument("--units-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    expected = load_expected()
    _, carried, missing = validate_runkey(args.runkey, expected)
    if args.carry_dir.as_posix() != CARRY_RELATIVE:
        raise ValueError("unexpected carry directory argument")
    carry = load_carry(args.carry_dir, carried)

    args.units_dir.mkdir(parents=True, exist_ok=True)
    for old in args.units_dir.glob("parent-*.json"):
        old.unlink()
    for idx in carried:
        shutil.copyfile(carry[idx], args.units_dir / f"parent-{idx}.json")

    worker = Path(__file__).resolve().parent / "bc2_40_replay_parent_unit.py"
    failure = None
    for idx in missing:
        out = args.units_dir / f"parent-{idx}.json"
        cmd = [
            sys.executable,
            str(worker),
            "--parent-index",
            str(idx),
            "--output",
            str(out),
            "--per-parent-timeout-ms",
            str(TIMEOUT_MS),
        ]
        try:
            subprocess.run(cmd, check=True)
            if out.stat().st_size > UNIT_MAX_BYTES:
                raise ValueError(f"unit too large: {out}")
            unit = agg.checked_unit(out)
            if int(unit["parent_index"]) != idx:
                raise ValueError(f"worker parent mismatch for {idx}")
        except Exception as exc:
            failure = f"parent {idx}: {type(exc).__name__}: {exc}"
            break

    complete_now = []
    for p in sorted(args.units_dir.glob("parent-*.json")):
        u = agg.checked_unit(p)
        complete_now.append(int(u["parent_index"]))
    complete_now = [idx for idx in expected if idx in set(complete_now)]
    remaining = [idx for idx in expected if idx not in set(complete_now)]

    if remaining:
        run_aggregate(args.units_dir, args.output, allow_partial=True)
        print(json.dumps({
            "status": "PARTIAL_RECOVERABLE",
            "carried": carried,
            "completed_this_generation": [i for i in complete_now if i not in carried],
            "missing": remaining,
            "failure": failure,
        }, sort_keys=True))
        if failure is not None:
            raise SystemExit(2)
        raise SystemExit(3)

    run_aggregate(args.units_dir, args.output, allow_partial=False)
    print(json.dumps({
        "status": "COMPLETE_EXACT_UNION",
        "carried": carried,
        "completed_this_generation": [i for i in complete_now if i not in carried],
        "missing": [],
    }, sort_keys=True))

if __name__ == "__main__":
    main()
