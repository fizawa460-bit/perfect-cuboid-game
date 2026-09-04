#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "stages/stage33/33-07"
sys.path.insert(0, str(HELPER))
from stage32_picard_marking_retained import load as load_marking  # type: ignore

HERE = Path(__file__).resolve().parent
WITNESS = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
H_DECK = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json"
GAUGE = HERE / "post1505-o210-q602-marked-w-line-gauge-orbit.json"

EXPECTED_WITNESS_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_H_CANONICAL = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"
EXPECTED_GAUGE_CANONICAL = "7ad84e3c0a567119933ee0941b3b125ebcdb80651973033e13dbf12b553bfc92"
SECOND_BOUNDARIES = [33, 36, 37, 40, 41, 44]


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


def transform(pairings: list[int], perm: list[int]) -> list[int]:
    pinv = inverse(perm)
    return [pairings[pinv[j] - 1] for j in range(len(pairings))]


def perm_for_word(word: str, perms: list[list[int]]) -> list[int]:
    out = list(range(1, 141))
    if word == "1":
        return out
    for token in word.split("*"):
        if not token.startswith("g") or not token[1:].isdigit():
            raise SystemExit(f"bad Stoll word token: {token}")
        idx = int(token[1:])
        out = compose(out, perms[idx - 1])
    return out


def matmul2(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def order_2x2(a: list[list[int]], bound: int = 24) -> int:
    cur = [[1, 0], [0, 1]]
    for n in range(1, bound + 1):
        cur = matmul2(cur, a)
        if cur == [[1, 0], [0, 1]]:
            return n
    raise SystemExit("matrix order exceeds diagnostic bound")


def cycle_lengths(p: tuple[int, ...]) -> list[int]:
    seen: set[int] = set()
    out: list[int] = []
    for i in range(len(p)):
        if i in seen:
            continue
        j = i
        n = 0
        while j not in seen:
            seen.add(j)
            n += 1
            j = p[j]
        out.append(n)
    return sorted(out)


def preserves(values: list[int], p: tuple[int, ...]) -> bool:
    return all(values[i] == values[p[i]] for i in range(len(values)))


def main() -> None:
    witness = json.loads(WITNESS.read_text())
    hdeck = json.loads(H_DECK.read_text())
    gauge = json.loads(GAUGE.read_text())
    if canonical_sha(witness) != EXPECTED_WITNESS_CANONICAL:
        raise SystemExit("V6 witness canonical moved")
    if canonical_sha(hdeck) != EXPECTED_H_CANONICAL:
        raise SystemExit("H-deck canonical moved")
    if canonical_sha(gauge) != EXPECTED_GAUGE_CANONICAL:
        raise SystemExit("marked gauge canonical moved")

    if gauge["source_locks"]["external_bolza_g12"]["arxiv"] != "2509.24605v1":
        raise SystemExit("Cecotti source lock moved")
    if gauge["source_locks"]["external_bolza_g12"]["locator"] != "Appendix B, equations (B.1)-(B.6)":
        raise SystemExit("Cecotti locator moved")
    b3 = [[int(x) for x in row] for row in gauge["principal_automorphisms"]["b3"]]
    if b3 != [[-1, -1], [1, 0]] or order_2x2(b3) != 3:
        raise SystemExit("b3 order-3 matrix moved")

    marking = load_marking()
    aut = marking["aut_action"]
    if aut["schema"] != "STAGE32_AUT_PERM_SOURCELOCK_V1":
        raise SystemExit("retained Stoll action schema moved")
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != 140 for p in perms):
        raise SystemExit("retained Stoll action shape moved")

    pairings = [int(x) for x in witness["witness"]["all140_pairings"]]
    if len(pairings) != 140:
        raise SystemExit("V6 pairing vector moved")
    base_second = [pairings[i - 1] for i in SECOND_BOUNDARIES]
    if base_second != [11, 22, 16, 11, 28, 22]:
        raise SystemExit(f"second-boundary profile moved: {base_second}")

    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    if hwords != {"u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"}:
        raise SystemExit("H word adapter moved")
    H = {"id": "1", "u": hwords["u"], "v": hwords["v"], "uv": hwords["uv"]}

    cycle33 = [p for p in itertools.permutations(range(6)) if cycle_lengths(p) == [3, 3]]
    if len(cycle33) != 40:
        raise SystemExit(f"unexpected (3,3)-cycle count: {len(cycle33)}")

    orbit_rows = []
    for name, word in H.items():
        perm = perm_for_word(word, perms)
        moved = transform(pairings, perm)
        values = [moved[i - 1] for i in SECOND_BOUNDARIES]
        hits = [list(p) for p in cycle33 if preserves(values, p)]
        orbit_rows.append({
            "H_member": name,
            "word": word,
            "second_boundary_values": values,
            "sorted_multiset": sorted(values),
            "preserving_two_3cycle_permutation_count": len(hits),
        })

    if any(row["preserving_two_3cycle_permutation_count"] != 0 for row in orbit_rows):
        raise SystemExit("an H-translate unexpectedly admits a (3,3)-cycle invariant cusp profile")

    result = {
        "schema": "STAGE32_POST1534_B3_CUSP_ORBIT_DIAGNOSTIC_V1",
        "fixed_target": {"row_id": "g1-d186", "O": 210, "Q": 602},
        "b3_order": 3,
        "second_factor_boundary_labels": SECOND_BOUNDARIES,
        "two_3cycle_permutation_count": len(cycle33),
        "h_orbit_rows": orbit_rows,
        "all_h_translates_reject_two_3cycle_invariance": True,
        "scope": "FINITE_PICARD_CUSP_PROFILE_OBSTRUCTION_ONLY_NO_ACTUAL_T_COMMUTATOR_CREDIT",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
