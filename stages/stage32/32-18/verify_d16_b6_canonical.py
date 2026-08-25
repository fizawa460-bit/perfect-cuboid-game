#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib

AUT_SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
SEED = "stage32-d16-aut-a"
M = 140


def sha_weights(seed: str) -> list[int]:
    out: list[int] = []
    for i in range(M):
        d = hashlib.sha256(f"{seed}:{i}".encode()).digest()
        out.append(int.from_bytes(d[:4], "big") % 2000003 - 1000001)
    return out


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(q[p[i]] for i in range(M))


def load_group(path: pathlib.Path) -> list[tuple[int, ...]]:
    payload = json.loads(path.read_text())
    if payload.get("schema") != AUT_SCHEMA:
        raise RuntimeError("bad Aut schema")
    if payload.get("source", {}).get("git_blob_sha1") != EXPECTED_SOURCE_BLOB:
        raise RuntimeError("Aut source blob mismatch")
    raw = payload.get("permutations_1based")
    if not isinstance(raw, list) or len(raw) != 9:
        raise RuntimeError("expected nine source-locked generators")
    gens = [tuple(int(x) - 1 for x in row) for row in raw]
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
        raise RuntimeError(f"Aut closure order mismatch {len(seen)}")
    return sorted(seen)


def canonical_key(v: tuple[int, ...], p: tuple[int, ...], weights: list[int]) -> tuple[int, tuple[int, ...]]:
    out = [0] * M
    for old in range(M):
        out[p[old]] = v[old]
    t = tuple(out)
    return sum(weights[i] * t[i] for i in range(M)), t


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--aut", type=pathlib.Path, required=True)
    ap.add_argument("--dump", type=pathlib.Path, required=True)
    ap.add_argument("--enum-json", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    group = load_group(args.aut)
    weights = sha_weights(SEED)
    raw = args.dump.read_bytes()
    if raw[:8] != b"S32D16C1":
        raise RuntimeError("bad canonical dump magic")
    body = raw[8:]
    rec_size = 1 + M
    if len(body) % rec_size:
        raise RuntimeError("truncated canonical dump")
    records: list[tuple[int, tuple[int, ...]]] = []
    for off in range(0, len(body), rec_size):
        norm = body[off]
        pairing = tuple(body[off + 1:off + rec_size])
        records.append((norm, pairing))

    enum = json.loads(args.enum_json.read_text())
    if enum.get("schema") != "STAGE32_18_D16_AUT_CANONICAL_ENUM_V1":
        raise RuntimeError("bad enum schema")
    if enum.get("aut_group_order") != EXPECTED_GROUP_ORDER:
        raise RuntimeError("enum group order mismatch")
    if enum.get("canonical_seed") != SEED:
        raise RuntimeError("enum seed mismatch")
    if enum.get("canonical_survivors_including_zero") != len(records):
        raise RuntimeError("dump/result count mismatch")

    pairings = [v for _, v in records]
    if len(pairings) != len(set(pairings)):
        raise RuntimeError("duplicate canonical pairing")

    for v in pairings:
        base = (sum(weights[i] * v[i] for i in range(M)), v)
        best = min(canonical_key(v, p, weights) for p in group)
        if base != best:
            raise RuntimeError("noncanonical pairing emitted")

    norm_hist: dict[str, int] = {}
    for norm, _ in records:
        norm_hist[str(norm)] = norm_hist.get(str(norm), 0) + 1

    passed = (
        enum.get("bound") == 6
        and enum.get("status") == "COMPLETE"
        and enum.get("dfs_symmetry_breaker_count") == 64
        and enum.get("precanonical_survivors") == 232
        and enum.get("canonical_survivors_including_zero") == 37
        and enum.get("canonical_nonzero_survivors") == 36
        and len(records) == 37
    )
    if not passed:
        raise RuntimeError("b6 production regression mismatch")

    out = {
        "schema": "STAGE32_18_D16_B6_CANONICAL_VERIFY_V1",
        "aut_group_order": len(group),
        "canonical_record_count": len(records),
        "canonical_pairings_unique": True,
        "every_emitted_pairing_is_full_group_score_then_lex_minimum": True,
        "precanonical_survivors": enum["precanonical_survivors"],
        "canonical_survivors_including_zero": enum["canonical_survivors_including_zero"],
        "canonical_nonzero_survivors": enum["canonical_nonzero_survivors"],
        "norm_histogram": norm_hist,
        "b6_matches_independently_profiled_orbit_count_37": True,
        "MAIN_IMPLEMENTATION_ROUTE": "AUT_SYMMETRY_BREAKING_PLUS_FULL_GROUP_CANONICAL_AUGMENTATION",
        "FLOATING_REACH_PRUNING_COMPLETENESS_AUDIT_PENDING": True,
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
    }
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
