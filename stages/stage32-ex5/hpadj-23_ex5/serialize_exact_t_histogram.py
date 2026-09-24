#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILDER = HERE / "build_exact_t_joint_histogram.py"
RESULT = HERE / "HPADJ23-COMPACT-SERIALIZATION-BOUNDED-RESULT.json"

BUILDER_BLOB = "c02973cb9d7fdea7584661a9c5935a43e12efe92"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load_builder():
    req(BUILDER.is_file() and blob(BUILDER) == BUILDER_BLOB, "HPADJ23 builder blob drift")
    spec = importlib.util.spec_from_file_location("hpadj23_builder_locked_for_serialization", BUILDER)
    req(spec is not None and spec.loader is not None, "cannot load HPADJ23 builder")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def record_bytes(key, counts) -> bytes:
    b,c,s,r,qbc = key
    pairs = [[int(t), int(v)] for t,v in sorted(counts.items())]
    return (json.dumps([b,c,s,r,qbc,pairs], separators=(",", ":")) + "\n").encode()

def serialize(hist, path: Path | None = None) -> dict:
    sha = hashlib.sha256()
    lines = entries = multiplicity = nbytes = 0
    fh = path.open("wb") if path is not None else None
    try:
        for key in sorted(hist):
            raw = record_bytes(key, hist[key])
            sha.update(raw)
            if fh is not None:
                fh.write(raw)
            lines += 1
            nbytes += len(raw)
            entries += len(hist[key])
            multiplicity += sum(int(v) for v in hist[key].values())
    finally:
        if fh is not None:
            fh.close()
    return {
        "stream_sha256": sha.hexdigest(),
        "line_count": lines,
        "utf8_bytes": nbytes,
        "exact_t_support_entries": entries,
        "canonical_tuple_multiplicity": multiplicity,
    }

def roundtrip(path: Path):
    out = defaultdict(lambda: defaultdict(int))
    with path.open("rb") as fh:
        for lineno, raw in enumerate(fh, 1):
            arr = json.loads(raw)
            req(isinstance(arr, list) and len(arr) == 6, f"record shape line {lineno}")
            b,c,s,r,qbc,pairs = arr
            key = (int(b),int(c),int(s),int(r),int(qbc))
            req(key not in out, f"duplicate key line {lineno}: {key}")
            last = None
            for pair in pairs:
                req(isinstance(pair, list) and len(pair) == 2, f"t pair line {lineno}")
                t,v = int(pair[0]), int(pair[1])
                req(v > 0, f"nonpositive multiplicity line {lineno}")
                req(last is None or t > last, f"unsorted t line {lineno}")
                out[key][t] = v
                last = t
    return out

def normalized(hist):
    return {k: dict(sorted(v.items())) for k,v in hist.items() if v}

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    builder = load_builder()
    hist = builder.build_joint_bc_t(16)

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        metrics = serialize(hist, args.output)
        parsed = roundtrip(args.output)
    else:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "hpadj23-h16.jsonl"
            metrics = serialize(hist, p)
            parsed = roundtrip(p)

    req(normalized(parsed) == normalized(hist), "serialization roundtrip mismatch")

    result = json.loads(RESULT.read_text())
    req(canonical(result) == result["canonical_sha256_without_this_field"],
        "retained serialization result canonical drift")
    expected = result["bounded_H16_stream"]
    for key,value in metrics.items():
        req(expected[key] == value, f"retained stream metric drift {key}: {value} != {expected[key]}")

    # Re-check the historical HPADJ22 marginal through the parsed stream, not
    # only through the in-memory producer.
    parent = builder.load_parent()
    builder.marginal_check(parent, parsed, 16)

    print("PASS: HPADJ23 compact exact-t serialization H=16")
    print(json.dumps(metrics, sort_keys=True))

if __name__ == "__main__":
    main()
