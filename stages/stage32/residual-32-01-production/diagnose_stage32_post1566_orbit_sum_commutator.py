#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import contextlib
import hashlib
import importlib.util
import io
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HELPER_DIR = ROOT / "stages/stage33/33-07"
HELPER_FILE = HELPER_DIR / "certify_two_coordinate_swap_picard_rows.py"
HERE = Path(__file__).resolve().parent
WITNESS = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
H_DECK = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json"
NODE_ACTION = HERE / "post1490-o210-q4-bolza-x-relative-h-marked-node-action.json"
POST1566 = HERE / "post1563-ambient-symmetry-exhaustion-batch.json"
POST1532 = HERE / "post1532-q602-single-b3-commutator.json"

EXPECTED_AUT_GROUP_ORDER = 1536
EXPECTED_H_GROUP_ORDER = 4
EXPECTED_HELPER_BLOB = "296e2005f822ae89c1aa085161553fe9ef76d077"
EXPECTED_WITNESS_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_WITNESS_PICARD = "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726"
EXPECTED_H_DECK_CANONICAL = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"
EXPECTED_NODE_ACTION_CANONICAL = "d03cfe8c77614943e8d4ab190c046b801bb90aa18f5bb648973bda0a5300c269"
EXPECTED_POST1566_CANONICAL = "9dbf0bcb144824a14497b663da2200f94d7250bfc755a37d1d65ca0b565fbb2e"
EXPECTED_POST1532_CANONICAL = "a374defb3a888c131ce92db9416702f34a03eb780b76d1dd6c26ab019f3c5064"


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical_sha(obj: dict) -> str:
    core = dict(obj)
    got = core.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if got != calc:
        raise SystemExit(f"canonical mismatch: field={got} calc={calc}")
    return calc


def load_picard_helper():
    if blob_sha1(HELPER_FILE) != EXPECTED_HELPER_BLOB:
        raise SystemExit("retained primitive Picard recovery helper blob moved")
    sys.path.insert(0, str(HELPER_DIR))
    spec = importlib.util.spec_from_file_location("s32_post1570_picard_recovery", HELPER_FILE)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load retained primitive Picard recovery helper")
    mod = importlib.util.module_from_spec(spec)
    # The retained certifier executes its own diagnostic on import. Suppress
    # that historical stdout so this diagnostic emits exactly one JSON object.
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


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


def rref_rows(rows: list[list[int]]) -> tuple[list[list[Fraction]], list[int]]:
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return [], []
    ncols = len(a[0])
    if any(len(row) != ncols for row in a):
        raise SystemExit("ragged row space")
    pivot_row = 0
    pivots: list[int] = []
    for col in range(ncols):
        src = next((r for r in range(pivot_row, len(a)) if a[r][col]), None)
        if src is None:
            continue
        a[pivot_row], a[src] = a[src], a[pivot_row]
        pivot = a[pivot_row][col]
        a[pivot_row] = [x / pivot for x in a[pivot_row]]
        for r in range(len(a)):
            if r == pivot_row:
                continue
            f = a[r][col]
            if f:
                a[r] = [a[r][j] - f * a[pivot_row][j] for j in range(ncols)]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == len(a):
            break
    basis = [row for row in a if any(row)]
    return basis, pivots


def in_row_span(vec: list[int], basis: list[list[Fraction]], pivots: list[int]) -> bool:
    w = [Fraction(x) for x in vec]
    for row, col in zip(basis, pivots):
        f = w[col]
        if f:
            w = [w[j] - f * row[j] for j in range(len(w))]
    return all(x == 0 for x in w)


def main() -> None:
    h = load_picard_helper()
    aut = h.marking["aut_action"]
    if aut["schema"] != "STAGE32_AUT_PERM_SOURCELOCK_V1":
        raise SystemExit("retained Aut action schema moved")
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    if len(perms) != 9 or any(len(p) != 140 for p in perms):
        raise SystemExit("retained Stoll generator permutation shape moved")

    witness = json.loads(WITNESS.read_text())
    if canonical_sha(witness) != EXPECTED_WITNESS_CANONICAL:
        raise SystemExit("recovered V6 witness canonical moved")
    w = witness["witness"]
    b = [int(x) for x in w["all140_pairings"]]
    if len(b) != 140 or w["picard_coordinates_sha256"] != EXPECTED_WITNESS_PICARD:
        raise SystemExit("V6 exact class moved")

    # Recover C in the exact primitive INDLIST basis. The stored witness
    # coordinate vector uses a different retained convention, so equality of
    # raw coordinate arrays is not a valid gate. Exactness is checked by
    # self-square plus replay of all 140 intersection pairings, matching the
    # hostile-audited post1490 recovery method.
    gram_inv = h.invert_matrix(h.gram)
    c_coords = h.integral_row(
        h.row_times_fraction_matrix([b[j - 1] for j in h.INDLIST], gram_inv),
        "exact V6 class from all140 pairings",
    )
    if h.pairing(c_coords, c_coords, h.gram) != 758:
        raise SystemExit("V6 self-square moved")
    for j in range(140):
        if h.pairing(c_coords, h.known[j], h.gram) != b[j]:
            raise SystemExit(f"V6 all140 replay mismatch at class {j+1}")

    hdeck = json.loads(H_DECK.read_text())
    if canonical_sha(hdeck) != EXPECTED_H_DECK_CANONICAL:
        raise SystemExit("post1490 H-deck canonical moved")
    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    if hwords != {"u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"}:
        raise SystemExit("post1490 H-deck map moved")

    node_action = json.loads(NODE_ACTION.read_text())
    if canonical_sha(node_action) != EXPECTED_NODE_ACTION_CANONICAL:
        raise SystemExit("post1490 marked-node source lock moved")
    if node_action["marked_node_action"]["exceptional_labels"] != [93, 140]:
        raise SystemExit("exceptional label block moved")

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

    # Every retained Stoll generator must preserve the 48 exceptional curves.
    exceptional_labels = set(range(93, 141))
    for i, p in enumerate(perms, start=1):
        if {p[j - 1] for j in exceptional_labels} != exceptional_labels:
            raise SystemExit(f"g{i} does not preserve exceptional block 93..140")

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

    # Resolved Picard stabilizer, retained from the first #1570 head.
    resolved_stabilizer: list[dict] = []
    for p_tuple, word in group.items():
        if transform(orbit_sum, list(p_tuple)) == orbit_sum:
            resolved_stabilizer.append({"word": word, "is_H_deck_element": p_tuple in hperms})
    resolved_stabilizer.sort(key=lambda row: (row["word"].count("*"), len(row["word"]), row["word"]))
    if len(resolved_stabilizer) != 4 or any(not row["is_H_deck_element"] for row in resolved_stabilizer):
        raise SystemExit(f"resolved orbit-sum stabilizer no longer exactly H: {resolved_stabilizer}")

    # Hostile-audit repair: pass to the blow-down numerical class before using
    # pi^*. The kernel of numerical push-forward from the 48-point resolution
    # is the Q-span of the exceptional classes E_93,...,E_140. Therefore g
    # fixes the blow-down class of S_B iff g(S_B)-S_B lies in this exact span.
    exceptional_rows = [[int(x) for x in h.known[j - 1]] for j in range(93, 141)]
    exceptional_basis, exceptional_pivots = rref_rows(exceptional_rows)
    exceptional_rank = len(exceptional_basis)

    orbit_sum_coords = h.integral_row(
        h.row_times_fraction_matrix([orbit_sum[j - 1] for j in h.INDLIST], gram_inv),
        "H-orbit-sum class",
    )
    blowdown_stabilizer: list[dict] = []
    for p_tuple, word in group.items():
        moved = transform(orbit_sum, list(p_tuple))
        moved_coords = h.integral_row(
            h.row_times_fraction_matrix([moved[j - 1] for j in h.INDLIST], gram_inv),
            f"moved H-orbit-sum class ({word})",
        )
        delta = [moved_coords[k] - orbit_sum_coords[k] for k in range(len(orbit_sum_coords))]
        if in_row_span(delta, exceptional_basis, exceptional_pivots):
            blowdown_stabilizer.append({"word": word, "is_H_deck_element": p_tuple in hperms})

    blowdown_stabilizer.sort(key=lambda row: (row["word"].count("*"), len(row["word"]), row["word"]))
    blowdown_stabilizer_equals_H = (
        len(blowdown_stabilizer) == 4
        and all(row["is_H_deck_element"] for row in blowdown_stabilizer)
    )

    result = {
        "schema": "STAGE32_POST1566_ORBIT_SUM_COMMUTATOR_DIAGNOSTIC_V2_BLOWDOWN",
        "retained_stoll_group_order": len(group),
        "h_deck_group_order": len(hgroup),
        "resolved_h_orbit_sum_stabilizer_count": len(resolved_stabilizer),
        "resolved_h_orbit_sum_stabilizer_outside_h_count": sum(not row["is_H_deck_element"] for row in resolved_stabilizer),
        "resolved_h_orbit_sum_stabilizer_elements": resolved_stabilizer,
        "exceptional_labels_1based": [93, 140],
        "exceptional_curve_count": 48,
        "exceptional_span_rank_over_Q": exceptional_rank,
        "blowdown_n1_quotient_rank": 64 - exceptional_rank,
        "blowdown_h_orbit_sum_stabilizer_count": len(blowdown_stabilizer),
        "blowdown_h_orbit_sum_stabilizer_outside_h_count": sum(not row["is_H_deck_element"] for row in blowdown_stabilizer),
        "blowdown_h_orbit_sum_stabilizer_elements": blowdown_stabilizer,
        "blowdown_stabilizer_equals_H": blowdown_stabilizer_equals_H,
        "beta_B_in_full_stoll": True,
        "beta_B_in_H": False,
        "beta_B_fixes_resolved_h_orbit_sum": False,
        "beta_B_blowdown_noninvariance_proved": blowdown_stabilizer_equals_H,
        "q602_residues": post1532["audited_q602_residues"],
        "all_q602_residues_noncommuting_mod2": True,
        "scope": "EXACT_CURRENT_MAIN_RESOLVED_AND_BLOWDOWN_NUMERICAL_PICARD_ORBIT_SUM_PLUS_POST1566_MEMBERSHIP",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
