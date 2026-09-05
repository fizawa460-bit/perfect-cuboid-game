#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
OLD_DIAG = HERE / "diagnose_stage32_post1566_orbit_sum_commutator.py"
POST1505 = HERE / "post1505-o210-q602-marked-w-line-gauge-orbit.json"
POST1532 = HERE / "post1532-q602-single-b3-commutator.json"
POST1570 = HERE / "post1566-orbit-sum-commutator-batch.json"
WITNESS = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
H_DECK = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json"
NODE_ACTION = HERE / "post1490-o210-q4-bolza-x-relative-h-marked-node-action.json"

EXPECTED_POST1505 = "7ad84e3c0a567119933ee0941b3b125ebcdb80651973033e13dbf12b553bfc92"
EXPECTED_POST1532 = "a374defb3a888c131ce92db9416702f34a03eb780b76d1dd6c26ab019f3c5064"
EXPECTED_POST1570 = "d96ae71a5a863b66160d510ec26c913aeddec8b3f9aa8709305114aecfe2ee9b"
EXPECTED_WITNESS = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_H_DECK = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"
EXPECTED_NODE_ACTION = "d03cfe8c77614943e8d4ab190c046b801bb90aa18f5bb648973bda0a5300c269"


def load_old():
    spec = importlib.util.spec_from_file_location("s32_post1570_old", OLD_DIAG)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot import post1570 diagnostic")
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def mmul(a, b):
    n, m, k = len(a), len(b[0]), len(b)
    return [[sum(a[i][t] * b[t][j] for t in range(k)) & 1 for j in range(m)] for i in range(n)]


def mpow(a, n):
    out = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
    x = a
    while n:
        if n & 1:
            out = mmul(out, x)
        x = mmul(x, x)
        n >>= 1
    return out


def commutes(a, b):
    return mmul(a, b) == mmul(b, a)


def f2_rref(rows):
    a = [[int(x) & 1 for x in row] for row in rows]
    pivots = []
    r = 0
    if not a:
        return [], []
    for c in range(len(a[0])):
        src = next((i for i in range(r, len(a)) if a[i][c]), None)
        if src is None:
            continue
        a[r], a[src] = a[src], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return [row for row in a if any(row)], pivots


def f2_in_span(vec, basis, pivots):
    w = [int(x) & 1 for x in vec]
    for row, c in zip(basis, pivots):
        if w[c]:
            w = [x ^ y for x, y in zip(w, row)]
    return not any(w)


def main():
    old = load_old()
    post1505 = json.loads(POST1505.read_text())
    post1532 = json.loads(POST1532.read_text())
    post1570 = json.loads(POST1570.read_text())
    witness = json.loads(WITNESS.read_text())
    hdeck = json.loads(H_DECK.read_text())
    node_action = json.loads(NODE_ACTION.read_text())
    for obj, expected, name in [
        (post1505, EXPECTED_POST1505, "post1505"),
        (post1532, EXPECTED_POST1532, "post1532"),
        (post1570, EXPECTED_POST1570, "post1570"),
        (witness, EXPECTED_WITNESS, "witness"),
        (hdeck, EXPECTED_H_DECK, "H-deck"),
        (node_action, EXPECTED_NODE_ACTION, "node-action"),
    ]:
        if old.canonical_sha(obj) != expected:
            raise SystemExit(f"{name} canonical moved")

    b3 = post1532["principal_automorphisms"]["b3_mod2_4x4"]
    b4 = post1532["principal_automorphisms"]["b4_mod2_4x4"]
    I4 = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    if mpow(b3, 3) != I4 or mpow(b4, 2) != I4:
        raise SystemExit("principal mod2 orders moved")
    b3inv = mpow(b3, 2)
    a0 = b4
    a1 = mmul(mmul(b3, b4), b3inv)
    a2 = mmul(mmul(mpow(b3, 2), b4), b3)
    involutions = {"A0=b4": a0, "A1=b3*b4*b3^-1": a1, "A2=b3^2*b4*b3^-2": a2}
    if any(mpow(a, 2) != I4 for a in involutions.values()):
        raise SystemExit("conjugate involution order regression")
    residues = {str(x): post1532["finite_mod2_check"]["residue_matrices"][str(x)] for x in [73, 97, 235]}
    table = {r: [name for name, a in involutions.items() if commutes(t, a)] for r, t in residues.items()}
    expected_table = {
        "73": ["A0=b4"],
        "97": ["A2=b3^2*b4*b3^-2"],
        "235": ["A1=b3*b4*b3^-1"],
    }
    if table != expected_table:
        raise SystemExit(f"three-involution residue table moved: {table}")

    h = old.load_picard_helper()
    aut = h.marking["aut_action"]
    perms = [[int(x) for x in p] for p in aut["permutations_1based"]]
    group = old.close_group([(f"g{i}", perms[i - 1]) for i in range(1, 10)])
    if len(group) != 1536:
        raise SystemExit(f"Stoll group order moved: {len(group)}")

    b = [int(x) for x in witness["witness"]["all140_pairings"]]
    gram_inv = h.invert_matrix(h.gram)
    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    identity = list(range(1, 141))
    H = {"id": identity}
    for name in ("u", "v", "uv"):
        H[name] = old.perm_for_word(hwords[name], perms)
    hperms = {tuple(p) for p in H.values()}
    if len(old.close_group([(name, H[name]) for name in ("u", "v")])) != 4:
        raise SystemExit("H order moved")
    hvec = {name: old.transform(b, perm) for name, perm in H.items()}
    orbit_sum = tuple(sum(v[j] for v in hvec.values()) for j in range(140))
    orbit_sum_coords = h.integral_row(
        h.row_times_fraction_matrix([orbit_sum[j - 1] for j in h.INDLIST], gram_inv),
        "H-orbit-sum class",
    )

    if node_action["marked_node_action"]["exceptional_labels"] != [93, 140]:
        raise SystemExit("exceptional block moved")
    exceptional_rows = [[int(x) for x in h.known[j - 1]] for j in range(93, 141)]
    f2_basis, f2_pivots = f2_rref(exceptional_rows)

    mod2_stabilizer = []
    for p_tuple, word in group.items():
        moved = old.transform(orbit_sum, list(p_tuple))
        moved_coords = h.integral_row(
            h.row_times_fraction_matrix([moved[j - 1] for j in h.INDLIST], gram_inv),
            f"moved H-orbit-sum class ({word})",
        )
        delta = [moved_coords[k] - orbit_sum_coords[k] for k in range(len(orbit_sum_coords))]
        if f2_in_span(delta, f2_basis, f2_pivots):
            mod2_stabilizer.append({"word": word, "is_H_deck_element": p_tuple in hperms})
    mod2_stabilizer.sort(key=lambda row: (row["word"].count("*"), len(row["word"]), row["word"]))

    result = {
        "schema": "STAGE32_POST1570_THREE_INVOLUTION_Q602_DIAGNOSTIC_V1",
        "q602_residue_commuting_involution_table": table,
        "principal_involutions_mod2": involutions,
        "retained_stoll_group_order": len(group),
        "exceptional_span_rank_mod2": len(f2_basis),
        "blowdown_mod2_quotient_dimension": 64 - len(f2_basis),
        "blowdown_mod2_orbit_sum_stabilizer_count": len(mod2_stabilizer),
        "blowdown_mod2_orbit_sum_stabilizer_outside_h_count": sum(not row["is_H_deck_element"] for row in mod2_stabilizer),
        "blowdown_mod2_orbit_sum_stabilizer_elements": mod2_stabilizer,
        "blowdown_mod2_stabilizer_exactly_H": len(mod2_stabilizer) == 4 and all(row["is_H_deck_element"] for row in mod2_stabilizer),
        "warning": "mod2 residue commutation alone is not an exclusion; exclusion requires geometry to force the corresponding commutator nonzero modulo 2",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
