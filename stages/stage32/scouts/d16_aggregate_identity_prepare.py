#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

RANK = 63
BASE_CONSTRAINTS = 140
DEGREE = 16
POSITIVE_DUAL_TOTAL = 19 * DEGREE


def canonical_sha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_base(path: pathlib.Path) -> tuple[list[str], list[list[int]], list[int], list[int], list[list[int]]]:
    lines = path.read_text().splitlines()
    if len(lines) < 5:
        raise ValueError("truncated base input")
    if lines[0] != "S32_D16_CONSTRAINED_HPERP_V1":
        raise ValueError("unexpected base magic")
    header = lines[:4]
    n, m = map(int, lines[4].split())
    if (n, m) != (RANK, BASE_CONSTRAINTS):
        raise ValueError(f"unexpected base dimensions {(n, m)}")
    at = 5
    q = [list(map(int, lines[at + i].split())) for i in range(RANK)]
    at += RANK
    if any(len(row) != RANK for row in q):
        raise ValueError("bad Gram row")
    p0: list[int] = []
    caps: list[int] = []
    lin: list[list[int]] = []
    for _ in range(BASE_CONSTRAINTS):
        row = list(map(int, lines[at].split()))
        at += 1
        if len(row) != 2 + RANK:
            raise ValueError("bad constraint row")
        p0.append(row[0])
        caps.append(row[1])
        lin.append(row[2:])
    if at != len(lines):
        raise ValueError("unexpected trailing base input")
    return header, q, p0, caps, lin


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    header, q, p0, caps, lin = load_base(args.input)

    # Stage32 production positive-dual identity:
    #   sum(nonexceptional 92 pairings) + 5*sum(exceptional 48 pairings) = 19*d.
    # Encode it as one additional exact linear constraint equal to zero.
    eq_p0 = sum(p0[:92]) + 5 * sum(p0[92:140]) - POSITIVE_DUAL_TOTAL
    eq_lin = [
        sum(lin[r][j] for r in range(92))
        + 5 * sum(lin[r][j] for r in range(92, 140))
        for j in range(RANK)
    ]
    # H itself (z=0) must satisfy the identity exactly.
    assert eq_p0 == 0

    p0v = p0 + [eq_p0]
    capv = caps + [0]
    linv = lin + [eq_lin]
    payload = {
        "base_core_sha": header[1],
        "base_source_blob": header[2],
        "base_prepared_sha": header[3],
        "q": q,
        "p0": p0v,
        "caps": capv,
        "lin": linv,
        "positive_dual_total": POSITIVE_DUAL_TOTAL,
    }
    prepared_sha = canonical_sha(payload)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        f.write("S32_D16_CONSTRAINED_HPERP_AGG_V1\n")
        f.write(header[1] + "\n")
        f.write(header[2] + "\n")
        f.write(prepared_sha + "\n")
        f.write(f"{RANK} {BASE_CONSTRAINTS + 1}\n")
        for row in q:
            f.write(" ".join(map(str, row)) + "\n")
        for r in range(BASE_CONSTRAINTS + 1):
            f.write(f"{p0v[r]} {capv[r]} " + " ".join(map(str, linv[r])) + "\n")

    print(json.dumps({
        "schema": "STAGE32_SCOUT_D16_POSITIVE_DUAL_IDENTITY_PREP_V1",
        "constraints": BASE_CONSTRAINTS + 1,
        "positive_dual_total": POSITIVE_DUAL_TOTAL,
        "identity_constant_at_H": eq_p0,
        "identity_lin_nonzero": sum(v != 0 for v in eq_lin),
        "prepared_input_sha256": prepared_sha,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
