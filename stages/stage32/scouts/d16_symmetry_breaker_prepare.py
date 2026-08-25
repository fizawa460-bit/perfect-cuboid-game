#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

MAGIC = "S32_D16_CONSTRAINED_HPERP_V1"
AUT_SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
SEED = "stage32-d16-aut-a"
N = 63
M = 140


def sha_weights(seed: str) -> list[int]:
    out: list[int] = []
    for i in range(M):
        d = hashlib.sha256(f"{seed}:{i}".encode()).digest()
        out.append(int.from_bytes(d[:4], "big") % 2000003 - 1000001)
    return out


def load_hperp(path: pathlib.Path) -> tuple[str, list[int], list[list[int]]]:
    with path.open() as f:
        if f.readline().rstrip("\n") != MAGIC:
            raise RuntimeError("bad Hperp magic")
        _core_sha = f.readline().strip()
        source_blob = f.readline().strip()
        input_sha = f.readline().strip()
        n, m = map(int, f.readline().split())
        if (n, m) != (N, M):
            raise RuntimeError("unexpected Hperp dimensions")
        for _ in range(N):
            row = list(map(int, f.readline().split()))
            if len(row) != N:
                raise RuntimeError("truncated Gram matrix")
        p0: list[int] = []
        lin: list[list[int]] = []
        for _ in range(M):
            row = list(map(int, f.readline().split()))
            if len(row) != N + 2:
                raise RuntimeError("truncated pairing row")
            p0.append(row[0])
            lin.append(row[2:])
        if source_blob != EXPECTED_SOURCE_BLOB:
            raise RuntimeError("source blob mismatch")
    return input_sha, p0, lin


def load_aut(path: pathlib.Path) -> tuple[str, list[list[int]]]:
    payload = json.loads(path.read_text())
    if payload.get("schema") != AUT_SCHEMA:
        raise RuntimeError("bad Aut schema")
    if payload.get("source", {}).get("git_blob_sha1") != EXPECTED_SOURCE_BLOB:
        raise RuntimeError("Aut source blob mismatch")
    raw = payload.get("permutations_1based")
    if not isinstance(raw, list) or len(raw) != 9:
        raise RuntimeError("expected nine geometric generators")
    perms: list[list[int]] = []
    for perm1 in raw:
        if not isinstance(perm1, list) or sorted(perm1) != list(range(1, M + 1)):
            raise RuntimeError("bad 140-class permutation")
        p = [int(x) - 1 for x in perm1]
        if any((i < 92) != (p[i] < 92) for i in range(M)):
            raise RuntimeError("Aut generator mixes cap types")
        perms.append(p)
    return str(payload["canonical_sha256_without_this_field"]), perms


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=pathlib.Path, required=True)
    ap.add_argument("--aut", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    input_sha, p0, lin = load_hperp(args.input)
    aut_sha, perms = load_aut(args.aut)
    weights = sha_weights(SEED)
    rows: list[tuple[int, tuple[int, ...]]] = []
    for p in perms:
        # apply_perm writes out[p[old]] = v[old], hence
        # score(g v)-score(v) = sum_old (w[p[old]]-w[old]) v[old].
        dw = [weights[p[i]] - weights[i] for i in range(M)]
        c0 = sum(dw[i] * p0[i] for i in range(M))
        coeff = tuple(sum(dw[i] * lin[i][j] for i in range(M)) for j in range(N))
        if c0 == 0 and not any(coeff):
            continue
        rows.append((c0, coeff))
    rows = sorted(set(rows))
    if not (1 <= len(rows) <= 9):
        raise RuntimeError(f"unexpected deduplicated breaker count {len(rows)}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        f.write("S32_D16_SYMMETRY_BREAKERS_V1\n")
        f.write(input_sha + "\n")
        f.write(aut_sha + "\n")
        f.write(SEED + "\n")
        f.write(f"{N} {len(rows)}\n")
        for c0, coeff in rows:
            f.write(str(c0) + " " + " ".join(map(str, coeff)) + "\n")

    print(json.dumps({
        "seed": SEED,
        "weight_max_abs": max(abs(x) for x in weights),
        "generator_count": len(perms),
        "deduplicated_breaker_count": len(rows),
        "prepared_input_sha256": input_sha,
        "aut_canonical_sha256": aut_sha,
        "semantics": "FOR_EACH_LOCKED_GENERATOR_REQUIRE_SCORE_V_LE_SCORE_GV",
        "orbit_preservation_argument": "GLOBAL_SCORE_MINIMUM_IN_EACH_FINITE_ORBIT_SATISFIES_ALL_GENERATOR_INEQUALITIES",
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
