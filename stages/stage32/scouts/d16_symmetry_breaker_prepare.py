#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

MAGIC = "S32_D16_CONSTRAINED_HPERP_V1"
AUT_SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
SEED = "stage32-d16-aut-a"
N = 63
M = 140


def sha_weights(seed: str) -> list[int]:
    out: list[int] = []
    for i in range(M):
        d = hashlib.sha256(f"{seed}:{i}".encode()).digest()
        out.append(int.from_bytes(d[:4], "big") % 2000003 - 1000001)
    return out


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(q[p[i]] for i in range(M))


def short_word_pool(gens: list[tuple[int, ...]], depth: int, limit: int) -> list[tuple[int, ...]]:
    ident = tuple(range(M))
    seen = {ident}
    frontier = [ident]
    out: list[tuple[int, ...]] = []
    for _ in range(depth):
        nxt_frontier: list[tuple[int, ...]] = []
        for cur in frontier:
            for gen in gens:
                nxt = compose(cur, gen)
                if nxt in seen:
                    continue
                seen.add(nxt)
                out.append(nxt)
                nxt_frontier.append(nxt)
                if len(out) >= limit:
                    return out
        frontier = nxt_frontier
        if not frontier:
            break
    return out


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
    return list(seen)


def perm_hash(p: tuple[int, ...]) -> bytes:
    payload = SEED.encode() + b";spread;" + bytes(p)
    return hashlib.sha256(payload).digest()


def hash_spread_pool(gens: list[tuple[int, ...]], limit: int) -> tuple[list[tuple[int, ...]], int]:
    ident = tuple(range(M))
    group = full_group(gens)
    nonidentity = [p for p in group if p != ident]
    ranked = sorted(nonidentity, key=lambda p: (perm_hash(p), p))
    return ranked[:limit], len(group)


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
    ap.add_argument("--selector", choices=("short", "hash"), default="short")
    ap.add_argument("--word-depth", type=int, default=1, choices=(1, 2, 3))
    ap.add_argument("--max-breakers", type=int, default=9)
    args = ap.parse_args()
    if not (1 <= args.max_breakers <= 64):
        raise RuntimeError("--max-breakers must be in 1..64 for the current scout enumerator")

    input_sha, p0, lin = load_hperp(args.input)
    aut_sha, gens = load_aut(args.aut)
    group_order = None
    if args.selector == "short":
        transforms = short_word_pool(gens, args.word_depth, args.max_breakers)
        descriptor = f"{SEED};selector=short;word_depth={args.word_depth};max_breakers={args.max_breakers}"
        semantics = "FOR_EACH_SELECTED_SHORT_WORD_G_REQUIRE_SCORE_V_LE_SCORE_GV"
    else:
        transforms, group_order = hash_spread_pool(gens, args.max_breakers)
        descriptor = f"{SEED};selector=hash;full_group_order={group_order};max_breakers={args.max_breakers}"
        semantics = "FOR_EACH_HASH_RANKED_FULL_GROUP_ELEMENT_G_REQUIRE_SCORE_V_LE_SCORE_GV"
    if not transforms:
        raise RuntimeError("empty nonidentity Aut transform pool")

    weights = sha_weights(SEED)
    rows: list[tuple[int, tuple[int, ...]]] = []
    for p in transforms:
        # apply_perm writes out[p[old]] = v[old], hence
        # score(g v)-score(v) = sum_old (w[p[old]]-w[old]) v[old].
        dw = [weights[p[i]] - weights[i] for i in range(M)]
        c0 = sum(dw[i] * p0[i] for i in range(M))
        coeff = tuple(sum(dw[i] * lin[i][j] for i in range(M)) for j in range(N))
        if c0 == 0 and not any(coeff):
            continue
        rows.append((c0, coeff))
    # Distinct group elements can only be redundant here if this score difference
    # restricts identically on the Hperp affine slice; deduplicate exactly.
    rows = list(dict.fromkeys(rows))
    if not (1 <= len(rows) <= args.max_breakers):
        raise RuntimeError(f"unexpected deduplicated breaker count {len(rows)}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        f.write("S32_D16_SYMMETRY_BREAKERS_V1\n")
        f.write(input_sha + "\n")
        f.write(aut_sha + "\n")
        f.write(descriptor + "\n")
        f.write(f"{N} {len(rows)}\n")
        for c0, coeff in rows:
            f.write(str(c0) + " " + " ".join(map(str, coeff)) + "\n")

    print(json.dumps({
        "seed": SEED,
        "selector": args.selector,
        "word_depth": args.word_depth if args.selector == "short" else None,
        "max_breakers": args.max_breakers,
        "weight_max_abs": max(abs(x) for x in weights),
        "geometric_generator_count": len(gens),
        "full_group_order": group_order,
        "selected_group_elements": len(transforms),
        "deduplicated_breaker_count": len(rows),
        "prepared_input_sha256": input_sha,
        "aut_canonical_sha256": aut_sha,
        "semantics": semantics,
        "orbit_preservation_argument": "GLOBAL_SCORE_MINIMUM_IN_EACH_FINITE_ORBIT_SATISFIES_EVERY_SELECTED_GROUP_INEQUALITY",
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
