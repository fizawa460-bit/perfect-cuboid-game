#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import pathlib
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UPSTREAM_COMMIT = "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
UPSTREAM_RAW = f"https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/{UPSTREAM_COMMIT}/Cuboids/cuboids.magma"
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"
SCHEMA = "STAGE32_AUT_ACTION_SOURCELOCK_V1"


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def fetch_locked_source() -> bytes:
    req = urllib.request.Request(UPSTREAM_RAW, headers={"User-Agent": "perfect-cuboid-stage32/3.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    got = git_blob_sha1(raw)
    if got != UPSTREAM_BLOB:
        raise RuntimeError(f"upstream git-blob mismatch: {got} != {UPSTREAM_BLOB}")
    return raw


def build_magma_program(raw: bytes) -> str:
    text = raw.decode("utf-8")
    marker = "// Set up complex conjugation."
    if marker not in text:
        raise RuntimeError("source-lock marker missing")
    prefix = text.split(marker, 1)[0]
    suffix = r'''
SetColumns(0);
printf "STAGE32_AUT_GROUP_ORDER=%o\n", #AutS;
printf "STAGE32_AUT_GENERATOR_COUNT=%o\n", #action;
for k in [1..#action] do
  for r in [1..64] do
    printf "STAGE32_AUT_ROW k=%o r=%o ", k, r;
    print [ action[k][r,c] : c in [1..64] ];
  end for;
end for;
printf "STAGE32_AUT_DONE\n";
'''
    return prefix + "\n" + suffix


def post_magma(program: str) -> tuple[list[str], float]:
    data = urllib.parse.urlencode({"input": program}).encode()
    req = urllib.request.Request(
        MAGMA_URL,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": REFERER,
            "User-Agent": "perfect-cuboid-stage32/3.0",
        },
        method="POST",
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=120) as resp:
        rawxml = resp.read().decode("utf-8", "replace")
    root = ET.fromstring(rawxml)
    lines = ["".join(line.itertext()) for result in root.findall(".//results") for line in result.findall(".//line")]
    out = "\n".join(lines)
    if any(x in out for x in ("Runtime error", "User error", "Internal error")):
        raise RuntimeError(out[-4000:])
    if "STAGE32_AUT_DONE" not in out:
        raise RuntimeError("Magma action export incomplete")
    return lines, time.time() - t0


def parse(lines: list[str]) -> tuple[int, list[list[list[int]]]]:
    order = None
    count = None
    rows: dict[tuple[int, int], list[int]] = {}
    for line in lines:
        if line.startswith("STAGE32_AUT_GROUP_ORDER="):
            order = int(line.split("=", 1)[1])
        elif line.startswith("STAGE32_AUT_GENERATOR_COUNT="):
            count = int(line.split("=", 1)[1])
        elif line.startswith("STAGE32_AUT_ROW "):
            head, payload = line.split(" [", 1)
            fields = {part.split("=")[0]: int(part.split("=")[1]) for part in head.split()[1:]}
            row = ast.literal_eval("[" + payload)
            if len(row) != 64:
                raise RuntimeError("bad action row width")
            rows[(fields["k"], fields["r"])] = [int(x) for x in row]
    if order is None or count is None:
        raise RuntimeError("missing action metadata")
    if count != 9:
        raise RuntimeError(f"unexpected generator count {count}")
    generators = []
    for k in range(1, count + 1):
        matrix = []
        for r in range(1, 65):
            key = (k, r)
            if key not in rows:
                raise RuntimeError(f"missing action row {key}")
            matrix.append(rows[key])
        generators.append(matrix)
    return order, generators


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    raw = fetch_locked_source()
    program = build_magma_program(raw)
    last_error = None
    lines = None
    elapsed = None
    for attempt in range(2):
        try:
            lines, elapsed = post_magma(program)
            break
        except Exception as exc:
            last_error = exc
            if attempt == 0:
                time.sleep(2)
    if lines is None or elapsed is None:
        raise RuntimeError(f"Magma action export failed: {last_error!r}")

    order, generators = parse(lines)
    payload = {
        "schema": SCHEMA,
        "source": {
            "repository": "MichaelStollBayreuth/Verification",
            "commit": UPSTREAM_COMMIT,
            "path": "Cuboids/cuboids.magma",
            "git_blob_sha1": UPSTREAM_BLOB,
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
        },
        "magma_group_order": order,
        "generator_count": len(generators),
        "generators": generators,
        "magma_elapsed_seconds": round(elapsed, 6),
        "transcript_sha256": hashlib.sha256("\n".join(lines).encode()).hexdigest(),
        "theorem_credit": False,
        "receiver_credit": False,
    }
    payload["canonical_sha256_without_this_field"] = canonical_sha256(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "group_order": order,
        "generator_count": len(generators),
        "source_blob": UPSTREAM_BLOB,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
        "elapsed_seconds": elapsed,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
