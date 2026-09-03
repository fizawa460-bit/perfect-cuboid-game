#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
HELPER_DIR = ROOT / "stages/stage33/33-07"
HELPER = HELPER_DIR / "certify_two_coordinate_swap_picard_rows.py"
WITNESS = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"

EXPECTED_HELPER_BLOB = "296e2005f822ae89c1aa085161553fe9ef76d077"
EXPECTED_WITNESS_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
EXPECTED_WITNESS_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_WITNESS_PICARD = "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726"
D_SQUARE = 3874
DELTA_D = 2018
EXPECTED_CSUM = 6568
C_LO = 1938
C_HI = 2315


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def csha(obj: object) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i] - 1] for i in range(len(p)))


def load_helper():
    if blob_sha1(HELPER) != EXPECTED_HELPER_BLOB:
        raise SystemExit("Stage33 retained Picard recovery helper blob moved")
    sys.path.insert(0, str(HELPER_DIR))
    spec = importlib.util.spec_from_file_location("s32_post1490_picard_recovery", HELPER)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load retained Picard recovery helper")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    h = load_helper()
    if blob_sha1(WITNESS) != EXPECTED_WITNESS_BLOB:
        raise SystemExit("exact V6 witness blob moved")
    wdoc = json.loads(WITNESS.read_text())
    if csha(wdoc) != EXPECTED_WITNESS_CANONICAL:
        raise SystemExit("exact V6 witness canonical moved")
    w = wdoc["witness"]
    if w["picard_coordinates_sha256"] != EXPECTED_WITNESS_PICARD or w["self_intersection"] != 758:
        raise SystemExit("exact V6 class moved")

    pairings = [int(x) for x in w["all140_pairings"]]
    if len(pairings) != 140:
        raise SystemExit("exact V6 all140 pairing count moved")

    # Recover the exact V6 class in the same primitive INDLIST basis used by
    # the retained automorphism action.  If b_j=C.e_j and G is the INDLIST
    # Gram matrix, then b=C G, hence C=b G^{-1}.
    basis_pairings = [pairings[j - 1] for j in h.INDLIST]
    gram_inv = h.invert_matrix(h.gram)
    c_coords = h.integral_row(
        h.row_times_fraction_matrix(basis_pairings, gram_inv),
        "exact V6 class from all140 pairings",
    )
    if h.pairing(c_coords, c_coords, h.gram) != 758:
        raise SystemExit("recovered exact V6 self-square mismatch")
    for i in range(140):
        if h.pairing(c_coords, h.known[i], h.gram) != pairings[i]:
            raise SystemExit(f"exact V6 all140 replay mismatch at class {i+1}")

    pp = [tuple(int(x) for x in p) for p in h.perms]
    ident = tuple(range(1, 141))
    g7, g8, g9 = pp[6], pp[7], pp[8]
    deck = {
        "u": compose(g7, g9),
        "v": compose(g7, g8),
        "uv": compose(g8, g9),
    }
    if any(compose(p, p) != ident for p in deck.values()):
        raise SystemExit("relative-H deck action ceased to be involutive")
    if compose(deck["u"], deck["v"]) != deck["uv"] or compose(deck["v"], deck["u"]) != deck["uv"]:
        raise SystemExit("relative-H deck action ceased to form V4")

    rows = {}
    masses = pairings[-48:]
    for name, perm in deck.items():
        action = [h.known[perm[j - 1] - 1] for j in h.INDLIST]
        for j in range(140):
            got = h.row_times_matrix(h.known[j], action)
            want = h.known[perm[j] - 1]
            if got != want:
                raise SystemExit(f"{name} all140 Picard transport mismatch at class {j+1}")
        t_coords = h.row_times_matrix(c_coords, action)
        b_cross = h.pairing(c_coords, t_coords, h.gram)

        exc_cross = 0
        exc_perm = []
        for j in range(93, 141):
            image = perm[j - 1]
            if not 93 <= image <= 140:
                raise SystemExit(f"{name} moved exceptional class {j} outside exceptional block")
            exc_perm.append(image)
            exc_cross += pairings[j - 1] * pairings[image - 1]

        # Equivariant bilinear extension of the already-locked self adapter:
        # D.tD = (pi^*C).(pi^*tC) + sum m_j m_{t(j)}
        #       = 2 C.tC + sum m_j m_{t(j)}.
        x_cross = 2 * b_cross + exc_cross
        if x_cross % 2:
            raise SystemExit(f"{name} produced odd X-side deck intersection")
        c_t = x_cross // 2
        r_t = C_HI - c_t
        e_square = 2 * D_SQUARE - 2 * x_cross
        rows[name] = {
            "B_C_dot_tC": b_cross,
            "exceptional_mass_cross": exc_cross,
            "X_D_dot_tD": x_cross,
            "c_t": c_t,
            "r_t": r_t,
            "E_t_square_from_D_minus_tD": e_square,
            "within_locked_hodge_bounds": C_LO <= c_t <= C_HI,
            "exceptional_permutation_1based": exc_perm,
        }

    csum = sum(v["c_t"] for v in rows.values())
    rsum = sum(v["r_t"] for v in rows.values())
    out = {
        "schema": "STAGE32_POST1490_O210_Q4_EQUIVARIANT_BLOWUP_DECK_CROSS_DIAGNOSTIC_V1",
        "status": "PASS_DIAGNOSTIC",
        "fixed": {"D_square": D_SQUARE, "delta_D": DELTA_D, "expected_c_sum": EXPECTED_CSUM, "c_bounds": [C_LO, C_HI]},
        "source_locks": {
            "picard_recovery_helper_blob_sha1": EXPECTED_HELPER_BLOB,
            "exact_v6_witness_blob_sha1": EXPECTED_WITNESS_BLOB,
            "exact_v6_witness_canonical_sha256": EXPECTED_WITNESS_CANONICAL,
            "exact_v6_picard_sha256": EXPECTED_WITNESS_PICARD,
            "modular_to_stoll": {"u": "g7*g9", "v": "g7*g8", "uv": "g8*g9"},
        },
        "exact_v6_recovery": {
            "primitive_indlist_coordinates": c_coords,
            "matches_stored_picard_coordinates": c_coords == [int(x) for x in w["picard_coordinates"]],
            "all140_pairings_replayed": True,
            "self_square": h.pairing(c_coords, c_coords, h.gram),
            "exceptional_masses": masses,
        },
        "deck_cross": rows,
        "checks": {
            "computed_c_sum": csum,
            "computed_r_sum": rsum,
            "matches_locked_c_sum_6568": csum == EXPECTED_CSUM,
            "matches_locked_r_sum_377": rsum == 377,
            "all_componentwise_hodge_bounds": all(v["within_locked_hodge_bounds"] for v in rows.values()),
            "all_E_square_formula_matches": all(v["E_t_square_from_D_minus_tD"] == -8 - 16 * v["r_t"] for v in rows.values()),
        },
        "firewall": "diagnostic only; the bilinear equivariant B->X adapter must be source-locked/certified before these cross intersections receive mathematical credit",
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
