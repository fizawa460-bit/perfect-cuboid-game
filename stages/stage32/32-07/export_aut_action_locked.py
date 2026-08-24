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
SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def fetch_locked_source() -> bytes:
    req = urllib.request.Request(
        UPSTREAM_RAW, headers={"User-Agent": "perfect-cuboid-stage32/3.1"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    got = git_blob_sha1(raw)
    if got != UPSTREAM_BLOB:
        raise RuntimeError(f"upstream git-blob mismatch: {got} != {UPSTREAM_BLOB}")
    return raw


def build_magma_program(raw: bytes) -> tuple[str, dict[str, str]]:
    """Build only the geometric permutation computation from the locked source.

    The previous exporter evaluated the full upstream prefix through Picard-lattice
    construction and repeatedly hit the Magma Online calculator wall.  The nine
    geometric permutations are defined before the Picard descent and need only
    S, the 92 known curves, the 48 singular points, and the exact upstream
    substitution/action block.  We therefore splice those two verbatim regions
    from the source-locked file and derive the 64x64 Picard matrices later from
    the locked Stage32 core over Z.
    """
    text = raw.decode("utf-8")
    prefix_end_marker = "// Set up the intersection pairing"
    aut_start_marker = "substs :="
    aut_end_marker = "// Descend the action to the Picard group."
    if prefix_end_marker not in text or aut_start_marker not in text or aut_end_marker not in text:
        raise RuntimeError("source-lock splice marker missing")

    geometry_prefix = text.split(prefix_end_marker, 1)[0]
    aut_tail = text.split(aut_start_marker, 1)[1]
    aut_block = aut_start_marker + aut_tail.split(aut_end_marker, 1)[0]

    suffix = r'''
SetColumns(0);
printf "STAGE32_AUT_PERM_COUNT=%o\n", #perms;
for k in [1..#perms] do
  printf "STAGE32_AUT_PERM k=%o ", k;
  print perms[k];
end for;
printf "STAGE32_AUT_DONE\n";
'''
    program = geometry_prefix + "\n" + aut_block + "\n" + suffix
    hashes = {
        "geometry_prefix_sha256": hashlib.sha256(geometry_prefix.encode()).hexdigest(),
        "aut_block_sha256": hashlib.sha256(aut_block.encode()).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }
    return program, hashes


def post_magma(program: str) -> tuple[list[str], float]:
    data = urllib.parse.urlencode({"input": program}).encode()
    req = urllib.request.Request(
        MAGMA_URL,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": REFERER,
            "User-Agent": "perfect-cuboid-stage32/3.1",
        },
        method="POST",
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=90) as resp:
        rawxml = resp.read().decode("utf-8", "replace")
    root = ET.fromstring(rawxml)
    lines = [
        "".join(line.itertext())
        for result in root.findall(".//results")
        for line in result.findall(".//line")
    ]
    out = "\n".join(lines)
    if any(x in out for x in ("Runtime error", "User error", "Internal error")):
        raise RuntimeError(out[-4000:])
    if "STAGE32_AUT_DONE" not in out:
        raise RuntimeError("Magma permutation export incomplete: " + out[-2000:])
    return lines, time.time() - t0


def parse(lines: list[str]) -> list[list[int]]:
    count = None
    permutations: dict[int, list[int]] = {}
    for line in lines:
        if line.startswith("STAGE32_AUT_PERM_COUNT="):
            count = int(line.split("=", 1)[1])
        elif line.startswith("STAGE32_AUT_PERM "):
            head, payload = line.split(" [", 1)
            fields = {
                part.split("=")[0]: int(part.split("=")[1])
                for part in head.split()[1:]
            }
            perm = ast.literal_eval("[" + payload)
            if len(perm) != 140 or sorted(perm) != list(range(1, 141)):
                raise RuntimeError("bad 140-class geometric permutation")
            permutations[fields["k"]] = [int(x) for x in perm]
    if count != 9:
        raise RuntimeError(f"unexpected permutation count {count}")
    if sorted(permutations) != list(range(1, 10)):
        raise RuntimeError("missing geometric permutation")
    return [permutations[k] for k in range(1, 10)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    raw = fetch_locked_source()
    program, splice_hashes = build_magma_program(raw)
    lines, elapsed = post_magma(program)
    permutations = parse(lines)

    payload = {
        "schema": SCHEMA,
        "source": {
            "repository": "MichaelStollBayreuth/Verification",
            "commit": UPSTREAM_COMMIT,
            "path": "Cuboids/cuboids.magma",
            "git_blob_sha1": UPSTREAM_BLOB,
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
        },
        "source_splice": splice_hashes,
        "permutation_count": len(permutations),
        "permutations_1based": permutations,
        "magma_elapsed_seconds": round(elapsed, 6),
        "transcript_sha256": hashlib.sha256("\n".join(lines).encode()).hexdigest(),
        "role": "SOURCE_LOCKED_GEOMETRIC_PERMUTATIONS_ONLY__PICARD_MATRICES_DERIVED_EXACTLY_FROM_STAGE32_CORE",
        "theorem_credit": False,
        "receiver_credit": False,
    }
    payload["canonical_sha256_without_this_field"] = canonical_sha256(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "permutation_count": len(permutations),
                "source_blob": UPSTREAM_BLOB,
                "canonical_sha256": payload["canonical_sha256_without_this_field"],
                "elapsed_seconds": elapsed,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
