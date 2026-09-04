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
POST1566 = HERE / "post1563-ambient-symmetry-exhaustion-batch.json"
POST1532 = HERE / "post1532-q602-single-b3-commutator.json"

EXPECTED_AUT_GROUP_ORDER = 1536
EXPECTED_H_GROUP_ORDER = 4
EXPECTED_WITNESS_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_H_DECK_CANONICAL = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"
EXPECTED_POST1566_CANONICAL = "9dbf0bcb144824a14497b663da2200f94d7250bfc755a37d1d65ca0b565fbb2e"
EXPECTED_POST1532_CANONICAL = "a374defb3a888c131ce92db9416702f34a03eb780b76d1dd6c26ab019f3c5064"


def canonical_sha(obj: dict) -> str:
    core = dict(obj)
    got = core.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
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


def main() -> None:
    marking = load_marking()
    aut = marking["aut_action"]
    if aut["schema"] != "STAGE32_AUT_PERM_SOURCELOCK_V1":
        raise SystemExit("retained Aut action schema moved")
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != 140 for p in perms):
        raise SystemExit("retained Stoll generator permutation shape moved")

    witness = json.loads(WITNESS.read_text())
    if canonical_sha(witness) != EXPECTED_WITNESS_CANONICAL:
        raise SystemExit("recovered V6 witness canonical moved")
    b = [int(x) for x in witness["witness"]["all140_pairings"]]
    if len(b) != 140:
        raise SystemExit("V6 all140 pairing vector moved")

    hdeck = json.loads(H_DECK.read_text())
    if canonical_sha(hdeck) != EXPECTED_H_DECK_CANONICAL:
        raise SystemExit("post1490 H-deck canonical moved")
    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    if hwords != {"u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"}:
        raise SystemExit("post1490 H-deck map moved")

    post1566 = json.loads(POST1566.read_text())
    if canonical_sha(post1566) != EXPECTED_POST1566_CANONICAL:
        raise SystemExit("merged #1566 canonical moved")
    dec1566 = post1566["decision"]
    route_c = post1566["routes"]["C_principal_b3_membership"]
    if not dec1566["retained_stoll_full_aut_equality_proved"]:
        raise SystemExit("#1566 full-Aut equality credit moved")
    if not route_c["beta_B_in_retained_stoll_group"] or route_c["beta_B_in_H"]:
        raise SystemExit("#1566 beta_B membership/outside-H predicate moved")

    post1532 = json.loads(POST1532.read_text())
    if canonical_sha(post1532) != EXPECTED_POST1532_CANONICAL:
        raise SystemExit("post1532 canonical moved")
    if post1532["audited_q602_residues"] != [73, 97, 235]:
        raise SystemExit("Q602 residue set moved")
    if not post1532["finite_mod2_check"]["all_audited_q602_residues_fail_b3_commutation"]:
        raise SystemExit("post1532 b3 commutator result moved")

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
    hperms = {tuple(p) for p in H.values()}
    stabilizer: list[dict] = []
    for p_tuple, word in group.items():
        if transform(orbit_sum, list(p_tuple)) == orbit_sum:
            stabilizer.append({"word": word, "is_H_deck_element": p_tuple in hperms})

    stabilizer.sort(key=lambda row: (row["word"].count("*"), len(row["word"]), row["word"]))
    if len(stabilizer) != 4 or any(not row["is_H_deck_element"] for row in stabilizer):
        raise SystemExit(f"orbit-sum stabilizer no longer exactly H: {stabilizer}")

    result = {
        "schema": "STAGE32_POST1566_ORBIT_SUM_COMMUTATOR_DIAGNOSTIC_V1",
        "retained_stoll_group_order": len(group),
        "h_deck_group_order": len(hgroup),
        "h_orbit_sum_stabilizer_count": len(stabilizer),
        "h_orbit_sum_stabilizer_outside_h_count": sum(not row["is_H_deck_element"] for row in stabilizer),
        "h_orbit_sum_stabilizer_elements": stabilizer,
        "beta_B_in_full_stoll": True,
        "beta_B_in_H": False,
        "beta_B_fixes_h_orbit_sum": False,
        "q602_residues": post1532["audited_q602_residues"],
        "all_q602_residues_noncommuting_mod2": True,
        "scope": "EXACT_CURRENT_MAIN_NUMERICAL_PICARD_ORBIT_SUM_PLUS_POST1566_MEMBERSHIP",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
