#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess

RANK = 63
CONSTRAINTS = 141


def gp_matrix(matrix: list[list[int]]) -> str:
    return "[" + ";".join(",".join(str(v) for v in row) for row in matrix) + "]"


def parse_vec(text: str) -> list[int]:
    text = text.strip()
    assert text.startswith("[") and text.endswith("]")
    body = text[1:-1].strip()
    return [] if not body else [int(x.strip()) for x in body.split(",")]


def load_problem(path: pathlib.Path):
    lines = path.read_text().splitlines()
    assert lines[0] == "S32_D16_CONSTRAINED_HPERP_AGG_V1"
    core_sha, source_blob, prepared_sha = lines[1:4]
    n, m = map(int, lines[4].split())
    assert (n, m) == (RANK, CONSTRAINTS)
    at = 5
    q = [list(map(int, lines[at + i].split())) for i in range(RANK)]
    at += RANK
    p0, caps, lin = [], [], []
    for _ in range(CONSTRAINTS):
        row = list(map(int, lines[at].split()))
        at += 1
        assert len(row) == 2 + RANK
        p0.append(row[0]); caps.append(row[1]); lin.append(row[2:])
    assert at == len(lines)
    return core_sha, source_blob, prepared_sha, q, p0, caps, lin


def exact_ok(z: list[int], p0: list[int], caps: list[int], lin: list[list[int]]) -> bool:
    for r in range(CONSTRAINTS):
        v = p0[r] + sum(lin[r][j] * z[j] for j in range(RANK))
        if v < 0 or v > caps[r]:
            return False
    return True


def enumerate_bound(q: list[list[int]], bound: int, p0, caps, lin) -> dict:
    code = f"""
Q={gp_matrix(q)};
r=qfminim(Q,{bound},5000,0);
V=r[3];c=matsize(V)[2];
print("META|",r[1],"|",r[2],"|",c);
for(i=1,c,print("V|",Vec(V[,i])));
quit;
"""
    proc = subprocess.run(["gp", "-q"], input=code, text=True, capture_output=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr[-4000:])
    meta = None
    reps: list[list[int]] = []
    for raw in proc.stdout.splitlines():
        line = raw.strip()
        if line.startswith("META|"):
            _, total, maxnorm, cols = line.split("|", 3)
            meta = (int(total), int(maxnorm), int(cols))
        elif line.startswith("V|"):
            reps.append(parse_vec(line.split("|", 1)[1]))
    assert meta is not None
    total, maxnorm, cols = meta
    assert cols == len(reps)
    # Known complete lattice-ball counts from the previous PARI scout.
    expected_total = {2: 96, 4: 4608}[bound]
    assert total == expected_total
    assert total == 2 * cols

    count = 1 if exact_ok([0] * RANK, p0, caps, lin) else 0
    nonzero = 0
    for z in reps:
        assert len(z) == RANK
        for sign in (1, -1):
            zz = [sign * x for x in z]
            if exact_ok(zz, p0, caps, lin):
                count += 1
                nonzero += 1
    return {
        "bound": bound,
        "raw_nonzero_vectors": total,
        "representative_pairs": cols,
        "maximum_norm_enumerated": maxnorm,
        "aggregate_filtered_including_zero": count,
        "aggregate_filtered_nonzero": nonzero,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()
    core_sha, source_blob, prepared_sha, q, p0, caps, lin = load_problem(args.input)
    tiers = [enumerate_bound(q, b, p0, caps, lin) for b in (2, 4)]
    report = {
        "schema": "STAGE32_SCOUT_D16_AGGREGATE_LOWBOUND_BASELINE_V1",
        "source_core_canonical_sha256": core_sha,
        "source_blob_sha1": source_blob,
        "prepared_input_sha256": prepared_sha,
        "enumerator": "PARI_QFMINIM_COMPLETE_BALL_THEN_EXACT_141_CONSTRAINT_FILTER",
        "tiers": tiers,
        "SCOUT_ONLY": True,
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"tiers": tiers}, sort_keys=True))


if __name__ == "__main__":
    main()
