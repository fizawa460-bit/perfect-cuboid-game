#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib

MAGIC = b"S32D16V1"
WIDTH = 141
AUT_SCHEMA = "STAGE32_AUT_PERM_SOURCELOCK_V1"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_GROUP_ORDER = 1536
EXPECTED_B6_SURVIVORS = 17833


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Old index i --p--> p[i] --q--> q[p[i]]."""
    return tuple(q[p[i]] for i in range(len(p)))


def close_group(gens: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    ident = tuple(range(140))
    seen = {ident}
    queue = collections.deque([ident])
    while queue:
        cur = queue.popleft()
        for gen in gens:
            nxt = compose(cur, gen)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
                if len(seen) > EXPECTED_GROUP_ORDER:
                    raise RuntimeError("Aut closure exceeded locked order 1536")
    return sorted(seen)


def apply_perm(v: tuple[int, ...], p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * 140
    for old, new in enumerate(p):
        out[new] = v[old]
    return tuple(out)


def load_survivors(path: pathlib.Path) -> tuple[dict[tuple[int, ...], int], str]:
    raw = path.read_bytes()
    if raw[: len(MAGIC)] != MAGIC:
        raise RuntimeError("bad survivor dump magic")
    body = raw[len(MAGIC) :]
    if len(body) % WIDTH:
        raise RuntimeError("truncated survivor dump")
    rows: dict[tuple[int, ...], int] = {}
    for off in range(0, len(body), WIDTH):
        rec = body[off : off + WIDTH]
        norm = rec[0]
        v = tuple(rec[1:])
        if norm > 6:
            raise RuntimeError(f"unexpected b6 norm {norm}")
        if any(x > 8 for x in v[:92]) or any(x > 4 for x in v[92:]):
            raise RuntimeError("survivor violates frozen cap type")
        if v in rows:
            raise RuntimeError("duplicate 140-pairing survivor vector")
        rows[v] = norm
    if len(rows) != EXPECTED_B6_SURVIVORS:
        raise RuntimeError(f"unexpected b6 survivor count {len(rows)}")
    return rows, hashlib.sha256(raw).hexdigest()


def load_aut(path: pathlib.Path) -> tuple[list[tuple[int, ...]], dict[str, object]]:
    payload = json.loads(path.read_text())
    if payload.get("schema") != AUT_SCHEMA:
        raise RuntimeError("bad Aut schema")
    if payload.get("source", {}).get("git_blob_sha1") != EXPECTED_SOURCE_BLOB:
        raise RuntimeError("Aut source blob mismatch")
    claimed = payload.get("canonical_sha256_without_this_field")
    unsigned = dict(payload)
    unsigned.pop("canonical_sha256_without_this_field", None)
    if claimed != csha(unsigned):
        raise RuntimeError("Aut canonical SHA mismatch")
    raw = payload.get("permutations_1based")
    if not isinstance(raw, list) or len(raw) != 9:
        raise RuntimeError("expected nine geometric generators")
    gens: list[tuple[int, ...]] = []
    for perm1 in raw:
        if not isinstance(perm1, list) or sorted(perm1) != list(range(1, 141)):
            raise RuntimeError("bad 140-class permutation")
        p = tuple(int(x) - 1 for x in perm1)
        if any((i < 92) != (p[i] < 92) for i in range(140)):
            raise RuntimeError("Aut generator mixes normal/exceptional cap types")
        gens.append(p)
    return gens, payload


def sha_weights(seed: str) -> tuple[int, ...]:
    # Small enough for later int64 linear-cap experiments, but wide enough that
    # accidental equal scores on a finite orbit should be rare. Scout only.
    out = []
    for i in range(140):
        d = hashlib.sha256(f"{seed}:{i}".encode()).digest()
        out.append(int.from_bytes(d[:4], "big") % 2000003 - 1000001)
    return tuple(out)


def score(v: tuple[int, ...], weights: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(v, weights))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--survivors", type=pathlib.Path, required=True)
    ap.add_argument("--aut", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    survivors, dump_sha = load_survivors(args.survivors)
    gens, aut = load_aut(args.aut)
    group = close_group(gens)
    if len(group) != EXPECTED_GROUP_ORDER:
        raise RuntimeError(f"unexpected Aut order {len(group)}")

    weight_schemes = {
        "index_linear": tuple(range(1, 141)),
        "sha_stage32_a": sha_weights("stage32-d16-aut-a"),
        "sha_stage32_b": sha_weights("stage32-d16-aut-b"),
        "sha_stage32_c": sha_weights("stage32-d16-aut-c"),
    }
    score_profiles = {
        name: {
            "selected_survivors": 0,
            "unique_minimum_orbits": 0,
            "tied_minimum_orbits": 0,
            "maximum_minimum_tie": 0,
            "minimum_positive_score_gap": None,
            "max_abs_weight": max(abs(x) for x in weights),
            "weights_sha256": hashlib.sha256(
                ",".join(map(str, weights)).encode()
            ).hexdigest(),
        }
        for name, weights in weight_schemes.items()
    }

    unseen = set(survivors)
    orbit_sizes: collections.Counter[int] = collections.Counter()
    stabilizer_sizes: collections.Counter[int] = collections.Counter()
    per_norm_orbits: dict[int, collections.Counter[int]] = collections.defaultdict(collections.Counter)
    orbit_count = 0
    max_queue = 0

    while unseen:
        seed = min(unseen)
        norm = survivors[seed]
        orbit = {seed}
        queue = collections.deque([seed])
        while queue:
            max_queue = max(max_queue, len(queue))
            cur = queue.popleft()
            for gen in gens:
                nxt = apply_perm(cur, gen)
                got = survivors.get(nxt)
                if got is None:
                    raise RuntimeError("Aut image missing from complete b6 survivor dump")
                if got != norm:
                    raise RuntimeError("Aut image changed exact norm")
                if nxt not in orbit:
                    orbit.add(nxt)
                    queue.append(nxt)
        size = len(orbit)
        if EXPECTED_GROUP_ORDER % size:
            raise RuntimeError(f"orbit size {size} does not divide Aut order")
        unseen.difference_update(orbit)
        orbit_count += 1
        orbit_sizes[size] += 1
        stabilizer_sizes[EXPECTED_GROUP_ORDER // size] += 1
        per_norm_orbits[norm][size] += 1

        for name, weights in weight_schemes.items():
            values = sorted(score(v, weights) for v in orbit)
            minimum = values[0]
            tie = sum(x == minimum for x in values)
            prof = score_profiles[name]
            prof["selected_survivors"] += tie
            prof["maximum_minimum_tie"] = max(prof["maximum_minimum_tie"], tie)
            if tie == 1:
                prof["unique_minimum_orbits"] += 1
            else:
                prof["tied_minimum_orbits"] += 1
            if len(values) > tie:
                gap = values[tie] - minimum
                old = prof["minimum_positive_score_gap"]
                prof["minimum_positive_score_gap"] = gap if old is None else min(old, gap)

    covered = sum(size * count for size, count in orbit_sizes.items())
    if covered != EXPECTED_B6_SURVIVORS:
        raise RuntimeError("orbit accounting mismatch")
    for prof in score_profiles.values():
        prof["compression_ratio_survivors_per_selected"] = (
            len(survivors) / prof["selected_survivors"]
        )
        prof["exactly_one_selected_per_orbit"] = prof["selected_survivors"] == orbit_count

    norm_hist = collections.Counter(survivors.values())
    result = {
        "schema": "STAGE32_SCOUT_D16_AUT_ORBIT_PROFILE_V2",
        "scope": "SCOUT_ONLY_NO_CREDIT",
        "input": {
            "bound": 6,
            "survivor_count": len(survivors),
            "survivor_dump_sha256": dump_sha,
            "aut_schema": AUT_SCHEMA,
            "aut_source_blob_sha1": EXPECTED_SOURCE_BLOB,
            "aut_canonical_sha256": aut["canonical_sha256_without_this_field"],
            "geometric_generator_count": len(gens),
            "group_order": len(group),
        },
        "profile": {
            "orbit_count": orbit_count,
            "compression_ratio_survivors_per_orbit": len(survivors) / orbit_count,
            "orbit_size_histogram": {str(k): v for k, v in sorted(orbit_sizes.items())},
            "stabilizer_size_histogram": {str(k): v for k, v in sorted(stabilizer_sizes.items())},
            "norm_histogram": {str(k): v for k, v in sorted(norm_hist.items())},
            "per_norm_orbit_size_histogram": {
                str(n): {str(k): v for k, v in sorted(hist.items())}
                for n, hist in sorted(per_norm_orbits.items())
            },
            "all_generator_images_present": True,
            "all_generator_images_preserve_norm": True,
            "covered_survivors": covered,
            "max_bfs_queue": max_queue,
        },
        "linear_score_symmetry_breaking": score_profiles,
        "architecture_verdict": "MEASURE_AUT_COMPRESSION_AND_LINEAR_SCORE_BREAKER_BEFORE_TREE_INTEGRATION",
        "materialized_branch_count_constructed": 0,
        "floating_enumerator_remains_scout_only": True,
        "THEOREM_CREDIT": False,
        "RECEIVER_CREDIT": False,
        "FULL_D16_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "survivors": len(survivors),
                "orbits": orbit_count,
                "compression": round(len(survivors) / orbit_count, 6),
                "orbit_sizes": dict(sorted(orbit_sizes.items())),
                "linear_score_breakers": {
                    name: {
                        "selected": prof["selected_survivors"],
                        "unique_orbits": prof["unique_minimum_orbits"],
                        "max_tie": prof["maximum_minimum_tie"],
                    }
                    for name, prof in score_profiles.items()
                },
                "sha": result["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
