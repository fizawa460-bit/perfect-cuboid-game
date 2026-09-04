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

EXPECTED_AUT_GROUP_ORDER = 1536
EXPECTED_H_GROUP_ORDER = 4
EXPECTED_H_DECK_CANONICAL = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"


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


def transform(pairings: list[int], perm: list[int]) -> tuple[int, ...]:
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
    if hdeck["schema"] != "STAGE32_POST1490_O210_Q4_EQUIVARIANT_BEAUVILLE_DECK_CROSS_EXCLUSION_V1":
        raise SystemExit("post1490 H-deck asset schema moved")
    if canonical_sha(hdeck) != EXPECTED_H_DECK_CANONICAL:
        raise SystemExit("post1490 H-deck canonical moved")
    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    expected_hwords = {"u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"}
    if hwords != expected_hwords:
        raise SystemExit("post1490 H-deck modular_to_stoll map moved")

    generators = [(f"g{i}", perms[i - 1]) for i in range(1, 10)]
    group = close_group(generators)
    if len(group) != EXPECTED_AUT_GROUP_ORDER:
        raise SystemExit(f"full retained Stoll group order regression: {len(group)}")

    pid = list(range(1, 141))
    H = {"id": pid}
    for name in ("u", "v", "uv"):
        H[name] = perm_for_word(hwords[name], perms)
    hgroup = close_group([(name, H[name]) for name in ("u", "v")])
    if len(hgroup) != EXPECTED_H_GROUP_ORDER:
        raise SystemExit(f"H deck group order regression: {len(hgroup)}")

    hvec = {name: transform(b, perm) for name, perm in H.items()}
    hvec_set = set(hvec.values())
    if len(hvec_set) != EXPECTED_H_GROUP_ORDER:
        raise SystemExit("H orbit of recovered V6 class is not four distinct numerical classes")

    hperms = {tuple(p) for p in H.values()}
    base_hits: list[dict] = []
    setwise_hits: list[dict] = []

    for p_tuple, word in group.items():
        p = list(p_tuple)
        vec = transform(b, p)
        matches = sorted(name for name, hv in hvec.items() if vec == hv)
        if matches:
            base_hits.append(
                {
                    "word": word,
                    "H_matches": matches,
                    "is_H_deck_element": p_tuple in hperms,
                }
            )

        image_orbit = {transform(list(hv), p) for hv in hvec.values()}
        if image_orbit == hvec_set:
            setwise_hits.append(
                {
                    "word": word,
                    "is_H_deck_element": p_tuple in hperms,
                }
            )

    base_hits.sort(key=lambda row: (row["word"].count("*"), len(row["word"]), row["word"]))
    setwise_hits.sort(key=lambda row: (row["word"].count("*"), len(row["word"]), row["word"]))

    result = {
        "schema": "STAGE32_POST1529_FULL_STOLL_H_ORBIT_DIAGNOSTIC_V1",
        "retained_stoll_group_order": len(group),
        "h_deck_group_order": len(hgroup),
        "h_orbit_size": len(hvec_set),
        "base_class_to_h_orbit_count": len(base_hits),
        "base_class_to_h_orbit_outside_h_count": sum(not row["is_H_deck_element"] for row in base_hits),
        "base_class_to_h_orbit_elements": base_hits,
        "setwise_h_orbit_stabilizer_count": len(setwise_hits),
        "setwise_h_orbit_stabilizer_outside_h_count": sum(not row["is_H_deck_element"] for row in setwise_hits),
        "setwise_h_orbit_stabilizer_elements": setwise_hits,
        "scope": "EXACT_NUMERICAL_PICARD_ACTION_ONLY_NO_CORRESPONDENCE_EQUIVARIANCE_CREDIT",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
