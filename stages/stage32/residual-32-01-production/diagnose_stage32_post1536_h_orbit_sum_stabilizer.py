#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "stages/stage33/33-07"
sys.path.insert(0, str(HELPER))
from stage32_picard_marking_retained import load as load_marking  # type: ignore

HERE = Path(__file__).resolve().parent
WITNESS = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
H_DECK = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json"
POST1536 = HERE / "post1536-b3-cusp-orbit-ambient-equivariance-negative.json"

EXPECTED_AUT_GROUP_ORDER = 1536
EXPECTED_H_GROUP_ORDER = 4
EXPECTED_H_DECK_CANONICAL = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"
EXPECTED_POST1536_CANONICAL = "3637db0c1e2acda7132b5b4fdc8ba4ee731230c160fa599dbdfeae993fb9e8ba"
SECOND_BOUNDARIES = [33, 36, 37, 40, 41, 44]
EXPECTED_WEIERSTRASS_MAP = {"33": 6, "36": 1, "37": 5, "40": 3, "41": 4, "44": 2}


def canonical_sha(obj: dict) -> str:
    core = dict(obj)
    got = core.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if got != calc:
        raise SystemExit(f"canonical mismatch: field={got} calc={calc}")
    return calc


def compose(p: list[int], q: list[int]) -> list[int]:
    return [q[p[j] - 1] for j in range(len(p))]


def inverse(p: list[int]) -> list[int]:
    out = [0] * len(p)
    for j, value in enumerate(p, start=1):
        out[value - 1] = j
    return out


def transform(pairings: list[int] | tuple[int, ...], perm: list[int]) -> tuple[int, ...]:
    pinv = inverse(perm)
    return tuple(pairings[pinv[j] - 1] for j in range(len(pairings)))


def perm_for_word(word: str, perms: list[list[int]]) -> list[int]:
    out = list(range(1, 141))
    if word == "1":
        return out
    for token in word.split("*"):
        if not token.startswith("g") or not token[1:].isdigit():
            raise SystemExit(f"bad Stoll word token: {token}")
        idx = int(token[1:])
        if not (1 <= idx <= len(perms)):
            raise SystemExit(f"Stoll generator out of range: {token}")
        out = compose(out, perms[idx - 1])
    return out


def close_group(generators: list[tuple[str, list[int]]]) -> dict[tuple[int, ...], str]:
    identity = tuple(range(1, 141))
    seen: dict[tuple[int, ...], str] = {identity: "1"}
    queue: deque[tuple[int, ...]] = deque([identity])
    while queue:
        p = queue.popleft()
        prefix = seen[p]
        for name, gp in generators:
            q = tuple(compose(list(p), gp))
            if q in seen:
                continue
            seen[q] = name if prefix == "1" else prefix + "*" + name
            queue.append(q)
    return seen


def cycle_lengths_on_subset(perm: list[int], labels: list[int]) -> list[int] | None:
    labelset = set(labels)
    if {perm[x - 1] for x in labels} != labelset:
        return None
    seen: set[int] = set()
    lengths: list[int] = []
    for start in labels:
        if start in seen:
            continue
        cur = start
        n = 0
        while cur not in seen:
            seen.add(cur)
            n += 1
            cur = perm[cur - 1]
            if cur not in labelset:
                raise SystemExit("subset-preservation regression")
        lengths.append(n)
    return sorted(lengths)


def main() -> None:
    marking = load_marking()
    aut = marking["aut_action"]
    if aut["schema"] != "STAGE32_AUT_PERM_SOURCELOCK_V1":
        raise SystemExit("retained Aut action schema moved")
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != 140 for p in perms):
        raise SystemExit("retained Stoll generator permutation shape moved")

    witness = json.loads(WITNESS.read_text())
    b = [int(x) for x in witness["witness"]["all140_pairings"]]
    if len(b) != 140:
        raise SystemExit("V6 all140 pairing vector moved")

    hdeck = json.loads(H_DECK.read_text())
    if canonical_sha(hdeck) != EXPECTED_H_DECK_CANONICAL:
        raise SystemExit("post1490 H-deck canonical moved")
    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    expected_hwords = {"u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"}
    if hwords != expected_hwords:
        raise SystemExit("post1490 H-deck modular_to_stoll map moved")

    post1536 = json.loads(POST1536.read_text())
    if canonical_sha(post1536) != EXPECTED_POST1536_CANONICAL:
        raise SystemExit("post1536 canonical moved")
    anchor = post1536["semantic_anchor"]
    if anchor["second_boundary_to_weierstrass_id"] != EXPECTED_WEIERSTRASS_MAP:
        raise SystemExit("post1536 boundary/Weierstrass map moved")
    if anchor["weierstrass_id_set"] != [1, 2, 3, 4, 5, 6]:
        raise SystemExit("post1536 Weierstrass id set moved")
    if post1536["finite_result"]["second_factor_boundary_labels"] != SECOND_BOUNDARIES:
        raise SystemExit("post1536 second-boundary labels moved")
    if not anchor["bijection_verified"]:
        raise SystemExit("post1536 Weierstrass adapter no longer verified")

    generators = [(f"g{i}", perms[i - 1]) for i in range(1, 10)]
    group = close_group(generators)
    if len(group) != EXPECTED_AUT_GROUP_ORDER:
        raise SystemExit(f"full retained Stoll group order regression: {len(group)}")

    identity = list(range(1, 141))
    H = {"id": identity}
    for name in ("u", "v", "uv"):
        H[name] = perm_for_word(hwords[name], perms)
    hgroup = close_group([(name, H[name]) for name in ("u", "v")])
    if len(hgroup) != EXPECTED_H_GROUP_ORDER:
        raise SystemExit(f"H deck group order regression: {len(hgroup)}")

    hvec = {name: transform(b, perm) for name, perm in H.items()}
    orbit_sum = tuple(sum(v[j] for v in hvec.values()) for j in range(140))
    if any(transform(orbit_sum, perm) != orbit_sum for perm in H.values()):
        raise SystemExit("H does not stabilize its own orbit-sum class")

    sum_stabilizer: list[dict] = []
    second_set_stabilizer_count = 0
    second_33_count = 0
    second_33_sum_fixed: list[dict] = []

    hperms = {tuple(p) for p in H.values()}
    for p_tuple, word in group.items():
        p = list(p_tuple)
        sum_fixed = transform(orbit_sum, p) == orbit_sum
        if sum_fixed:
            sum_stabilizer.append({"word": word, "is_H_deck_element": p_tuple in hperms})

        cycles = cycle_lengths_on_subset(p, SECOND_BOUNDARIES)
        if cycles is not None:
            second_set_stabilizer_count += 1
        if cycles == [3, 3]:
            second_33_count += 1
            if sum_fixed:
                second_33_sum_fixed.append(
                    {"word": word, "is_H_deck_element": p_tuple in hperms}
                )

    key = lambda row: (row["word"].count("*"), len(row["word"]), row["word"])
    sum_stabilizer.sort(key=key)
    second_33_sum_fixed.sort(key=key)

    result = {
        "schema": "STAGE32_POST1536_H_ORBIT_SUM_STABILIZER_DIAGNOSTIC_V1",
        "retained_stoll_group_order": len(group),
        "h_deck_group_order": len(hgroup),
        "second_boundary_labels": SECOND_BOUNDARIES,
        "h_orbit_sum_stabilizer_count": len(sum_stabilizer),
        "h_orbit_sum_stabilizer_outside_h_count": sum(
            not row["is_H_deck_element"] for row in sum_stabilizer
        ),
        "h_orbit_sum_stabilizer_elements": sum_stabilizer,
        "second_boundary_set_stabilizer_count": second_set_stabilizer_count,
        "second_boundary_cycle_type_3_3_count": second_33_count,
        "cycle_type_3_3_and_h_orbit_sum_fixed_count": len(second_33_sum_fixed),
        "cycle_type_3_3_and_h_orbit_sum_fixed_elements": second_33_sum_fixed,
        "scope": "EXACT_RETAINED_NUMERICAL_PICARD_ORBIT_SUM_ONLY_NO_ACTUAL_T_COMMUTATOR_CREDIT",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
