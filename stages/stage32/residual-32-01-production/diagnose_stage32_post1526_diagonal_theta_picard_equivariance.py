#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "stages/stage33/33-07"
sys.path.insert(0, str(HELPER))
from stage32_picard_marking_retained import load as load_marking  # type: ignore

HERE = Path(__file__).resolve().parent
WITNESS = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
FSM_ADAPTER = HERE / "post1529-fsm-stoll-diagonal-action-source-lock.json"
H_DECK = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json"

EXPECTED_FSM_ADAPTER_CANONICAL = "5726289d8948beaaf3ed4e2dc260f49d1b3b3054642f3460b6b1e53c77ea23bc"
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


def compose(p, q):
    return [q[p[j] - 1] for j in range(len(p))]


def inverse(p):
    out = [0] * len(p)
    for j, v in enumerate(p, start=1):
        out[v - 1] = j
    return out


def transform(pairings, perm):
    pinv = inverse(perm)
    return tuple(pairings[pinv[j] - 1] for j in range(len(pairings)))


def mm2(A, B):
    return (
        A[0] * B[0] + A[1] * B[2],
        A[0] * B[1] + A[1] * B[3],
        A[2] * B[0] + A[3] * B[2],
        A[2] * B[1] + A[3] * B[3],
    )


def comm_rows(A):
    a, b, c, d = A
    return [[0, c, -b, 0], [b, d - a, 0, -b], [-c, 0, a - d, c], [0, -c, b, 0]]


def rank_q(rows):
    M = [[Fraction(x) for x in r] for r in rows]
    r = 0
    for c in range(4):
        p = next((i for i in range(r, len(M)) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        v = M[r][c]
        M[r] = [x / v for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                v = M[i][c]
                M[i] = [x - v * y for x, y in zip(M[i], M[r])]
        r += 1
    return r


def perm_for_word(word: str, perms: list[list[int]]) -> list[int]:
    out = list(range(1, 141))
    if word == "1":
        return out
    for token in word.split("*"):
        if not token.startswith("g") or not token[1:].isdigit():
            raise SystemExit(f"bad Stoll word token: {token}")
        j = int(token[1:])
        if not (1 <= j <= len(perms)):
            raise SystemExit(f"Stoll generator out of range: {token}")
        out = compose(out, perms[j - 1])
    return out


def compose_symbolic(action: list[str], generator: list[str], coords: list[str]) -> list[str]:
    gmap = dict(zip(coords, generator))
    out = []
    for expr in action:
        sign = -1 if expr.startswith("-") else 1
        var = expr[1:] if sign == -1 else expr
        repl = gmap[var]
        sign2 = -1 if repl.startswith("-") else 1
        var2 = repl[1:] if sign2 == -1 else repl
        out.append(("-" if sign * sign2 == -1 else "") + var2)
    return out


def symbolic_word_action(word: str, adapter: dict) -> list[str]:
    coords = adapter["coordinate_order"]
    gens = adapter["stoll_generators_used"]
    out = list(coords)
    for token in word.split("*"):
        out = compose_symbolic(out, gens[token], coords)
    return out


def main():
    marking = load_marking()
    aut = marking["aut_action"]
    assert aut["schema"] == "STAGE32_AUT_PERM_SOURCELOCK_V1"
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    b = json.loads(WITNESS.read_text())["witness"]["all140_pairings"]
    assert len(perms) == 9 and len(b) == 140

    adapter = json.loads(FSM_ADAPTER.read_text())
    if adapter["schema"] != "STAGE32_POST1529_FSM_STOLL_DIAGONAL_ACTION_SOURCE_LOCK_V1":
        raise SystemExit("FSM/Stoll adapter schema moved")
    if canonical_sha(adapter) != EXPECTED_FSM_ADAPTER_CANONICAL:
        raise SystemExit("FSM/Stoll adapter canonical moved")

    fsm_actions = adapter["fsm_section2_actions"]
    for name in ("U", "S"):
        row = fsm_actions[name]
        got = symbolic_word_action(row["stoll_word"], adapter)
        if got != row["normalized_box_action"]:
            raise SystemExit(f"{name} FSM/Stoll coordinate adapter mismatch: {got}")

    # Reconstruct the two diagonal theta actions from the source-locked adapter.
    pU = perm_for_word(fsm_actions["U"]["stoll_word"], perms)
    pS = perm_for_word(fsm_actions["S"]["stoll_word"], perms)

    hdeck = json.loads(H_DECK.read_text())
    if hdeck["schema"] != "STAGE32_POST1490_O210_Q4_EQUIVARIANT_BEAUVILLE_DECK_CROSS_EXCLUSION_V1":
        raise SystemExit("post1490 H-deck asset schema moved")
    if canonical_sha(hdeck) != EXPECTED_H_DECK_CANONICAL:
        raise SystemExit("post1490 H-deck asset canonical moved")
    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    if hwords != {"u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"}:
        raise SystemExit("post1490 H-deck modular_to_stoll map moved")

    # Reconstruct the H-deck orbit from the exact post1490 retained asset.
    pid = list(range(1, 141))
    H = {"id": pid}
    for name in ("u", "v", "uv"):
        H[name] = perm_for_word(hwords[name], perms)
    Hvec = {name: transform(b, p) for name, p in H.items()}

    # Projective differential matrices on <omega4,omega5>. Scalars are irrelevant
    # for centralizers; this bounded analytic input is inherited from the #1526 leaf.
    gens = [("U", pU, (1, 0, 0, -1)), ("S", pS, (1, 1, 1, -1))]
    identity = tuple(pid)
    seen = {identity: ("1", (1, 0, 0, 1))}
    queue = [identity]
    while queue:
        p = queue.pop(0)
        word, M = seen[p]
        for name, gp, gM in gens:
            q = tuple(compose(list(p), gp))
            if q not in seen:
                seen[q] = (word + name, mm2(M, gM))
                queue.append(q)

    preserving = []
    print("STAGE32_POST1529_DIAGONAL_THETA_PICARD_DIAGNOSTIC_V4")
    print("source_locked_U_word=" + fsm_actions["U"]["stoll_word"])
    print("source_locked_S_word=" + fsm_actions["S"]["stoll_word"])
    print("source_locked_H_words=" + repr({k: hwords[k] for k in ("u", "v", "uv")}))
    print(f"diag_theta_group_order_on_140={len(seen)}")
    for p, (word, M) in sorted(seen.items(), key=lambda kv: (len(kv[1][0]), kv[1][0])):
        vec = transform(b, list(p))
        matches = [h for h, hv in Hvec.items() if vec == hv]
        if matches:
            preserving.append((word, M, matches))
        print(f"word={word} H_orbit_matches={matches} diff_matrix={M}")

    scalar_pair = None
    for i in range(len(preserving)):
        for j in range(i + 1, len(preserving)):
            w1, A, _ = preserving[i]
            w2, B, _ = preserving[j]
            if rank_q(comm_rows(A) + comm_rows(B)) == 3:
                scalar_pair = (w1, w2, A, B)
                break
        if scalar_pair:
            break

    print(f"H_orbit_preserving_count={len(preserving)}")
    print("H_orbit_preserving_words=" + [x[0] for x in preserving].__repr__())
    print(f"scalar_joint_centralizer_pair_exists={scalar_pair is not None}")
    print(f"scalar_pair={scalar_pair}")


if __name__ == "__main__":
    main()
