#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

HPERP_MAGIC = "S32_D16_AUT_CANON_HPERP_V1"
BUNDLE_MAGIC = "S32_D16_AUT_CANONICAL_BUNDLE_V1"
AUT_SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
SEED = "stage32-d16-aut-a"
N = 63
M = 140
BREAKER_COUNT = 64


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def sha_weights(seed: str) -> list[int]:
    out: list[int] = []
    for i in range(M):
        d = hashlib.sha256(f"{seed}:{i}".encode()).digest()
        out.append(int.from_bytes(d[:4], "big") % 2000003 - 1000001)
    return out


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(q[p[i]] for i in range(M))


def full_group(gens: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    ident = tuple(range(M))
    seen = {ident}
    frontier = [ident]
    while frontier:
        nxt_frontier: list[tuple[int, ...]] = []
        for cur in frontier:
            for gen in gens:
                nxt = compose(cur, gen)
                if nxt in seen:
                    continue
                seen.add(nxt)
                nxt_frontier.append(nxt)
        frontier = nxt_frontier
    if len(seen) != EXPECTED_GROUP_ORDER:
        raise RuntimeError(f"Aut closure order mismatch: {len(seen)} != {EXPECTED_GROUP_ORDER}")
    return sorted(seen)


def perm_hash(p: tuple[int, ...]) -> bytes:
    return hashlib.sha256(SEED.encode() + b";spread;" + bytes(p)).digest()


def load_hperp(path: pathlib.Path) -> tuple[str, list[int], list[list[int]]]:
    with path.open() as f:
        if f.readline().rstrip("\n") != HPERP_MAGIC:
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


def load_aut(path: pathlib.Path) -> tuple[str, list[tuple[int, ...]]]:
    payload = json.loads(path.read_text())
    if payload.get("schema") != AUT_SCHEMA:
        raise RuntimeError("bad Aut schema")
    if payload.get("source", {}).get("git_blob_sha1") != EXPECTED_SOURCE_BLOB:
        raise RuntimeError("Aut source blob mismatch")
    raw = payload.get("permutations_1based")
    if not isinstance(raw, list) or len(raw) != 9:
        raise RuntimeError("expected nine geometric generators")
    perms: list[tuple[int, ...]] = []
    for perm1 in raw:
        if not isinstance(perm1, list) or sorted(perm1) != list(range(1, M + 1)):
            raise RuntimeError("bad 140-class permutation")
        p = tuple(int(x) - 1 for x in perm1)
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
    aut_sha, gens = load_aut(args.aut)
    group = full_group(gens)
    ident = tuple(range(M))
    nonidentity = [p for p in group if p != ident]
    selected = sorted(nonidentity, key=lambda p: (perm_hash(p), p))[:BREAKER_COUNT]
    if len(selected) != BREAKER_COUNT:
        raise RuntimeError("could not select 64 nonidentity group elements")

    weights = sha_weights(SEED)
    rows: list[tuple[int, tuple[int, ...]]] = []
    for p in selected:
        # Convention: apply_perm writes out[p[old]] = v[old]. Therefore
        # score(gv)-score(v) = sum_old (w[p[old]]-w[old]) v[old].
        dw = [weights[p[i]] - weights[i] for i in range(M)]
        c0 = sum(dw[i] * p0[i] for i in range(M))
        coeff = tuple(sum(dw[i] * lin[i][j] for i in range(M)) for j in range(N))
        if c0 == 0 and not any(coeff):
            raise RuntimeError("selected breaker restricts trivially on Hperp slice")
        rows.append((c0, coeff))
    if len(set(rows)) != BREAKER_COUNT:
        raise RuntimeError("duplicate restricted breaker rows")

    bundle_payload = {
        "input_sha": input_sha,
        "aut_sha": aut_sha,
        "seed": SEED,
        "weights": weights,
        "breakers": [[c0, list(coeff)] for c0, coeff in rows],
        "group": [list(p) for p in group],
    }
    bundle_sha = csha(bundle_payload)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        f.write(BUNDLE_MAGIC + "\n")
        f.write(input_sha + "\n")
        f.write(aut_sha + "\n")
        f.write(bundle_sha + "\n")
        f.write(SEED + "\n")
        f.write(f"{N} {M} {BREAKER_COUNT} {len(group)}\n")
        f.write(" ".join(map(str, weights)) + "\n")
        for c0, coeff in rows:
            f.write(str(c0) + " " + " ".join(map(str, coeff)) + "\n")
        for p in group:
            f.write(" ".join(map(str, p)) + "\n")

    print(json.dumps({
        "schema": "STAGE32_18_D16_AUT_CANONICAL_PREP_V1",
        "prepared_input_sha256": input_sha,
        "aut_canonical_sha256": aut_sha,
        "bundle_canonical_sha256": bundle_sha,
        "seed": SEED,
        "geometric_generator_count": len(gens),
        "full_group_order": len(group),
        "selected_hash_spread_breakers": BREAKER_COUNT,
        "weight_max_abs": max(abs(x) for x in weights),
        "dfs_pruning_semantics": "SELECTED_SCORE_V_LE_SCORE_GV",
        "leaf_canonical_order": "MINIMIZE_EXACT_SCORE_THEN_LEX_PAIRING_OVER_FULL_AUT_ORBIT",
        "canonical_completeness_argument": "FINITE_GROUP_ORBIT_HAS_A_UNIQUE_LEXICOGRAPHIC_MINIMUM_AMONG_EXACT_SCORE_MINIMA;_PAIRING_MAP_IS_INJECTIVE_ON_HPERP",
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
