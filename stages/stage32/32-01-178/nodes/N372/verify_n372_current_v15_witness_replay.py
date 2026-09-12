#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
STATE = HERE / "STATE.json"
RESULT = HERE / "RESULT.json"
N363_RESULT = HERE.parent / "N363/RESULT.json"
N371_RESULT = HERE.parent / "N371/RESULT.json"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"

CUT196_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
E8_ADAPTER_BLOB = "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f"
N357_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
HPERP_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
STATE_BLOB = "e73af40e1433e6ab7227791c9501e51dfca1406c"
STATE_CANON = "ce99f0f14445a2b48c7024bde853470291f604378709fcc7747104efdcd5c6b2"
RESULT_BLOB = "c0267d903fd0b397fcd4766b03964bde788650e7"
RESULT_CANON = "b9852fcfa926e77e8c51defe31002e0bf4b281dd1db4b5f320326166932fef48"
WITNESS_CANON = "751ca10d8c93d15a5a51276f6d00e4572132e0d1fcb1aa65cbbcc854b7d8744f"
N363_RESULT_BLOB = "cf81550d326e1e7f290994a126268cdf7a479416"
N371_RESULT_BLOB = "450c1c4e2e898c45837fe1762a0e788c03f1636a"
MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_CANON = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
BLOCK, OFFSET, WIDTH = 1140, 797, 113
PARENT_ORDINAL = 290
EXPECTED_PARENT_COUNT = 300
PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
NORMAL_COUNT, NORMAL_MASS = 92, 112
D = E = 8
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]


def req(v: bool, msg: str) -> None:
    if not v:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj); q.pop("canonical_sha256_without_this_field", None)
    return csha(q)


def checked(path: Path, expected_blob: str, expected_canon: str | None = None) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
        req(canonical(obj) == expected_canon, f"canonical drift: {path}")
    return obj


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec); sys.modules[name] = mod; spec.loader.exec_module(mod)
    return mod


def row_sum(m: Matrix, labels: list[int]) -> Matrix:
    out = Matrix.zeros(1, m.cols)
    for label in labels:
        out += m.row(label - 1)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    args = ap.parse_args()
    cut_root = args.cut196_root.resolve()
    comp_root = args.n357_composition_root.resolve()

    req(not any(k == "z3" or k.startswith("z3.") for k in sys.modules), "z3 imported before replay")
    req(exact_head(cut_root) == CUT196_HEAD, "CUT196 exact head drift")
    req(exact_head(comp_root) == N357_HEAD, "N357 exact head drift")

    state = checked(STATE, STATE_BLOB, STATE_CANON)
    result = checked(RESULT, RESULT_BLOB, RESULT_CANON)
    checked(N363_RESULT, N363_RESULT_BLOB)
    checked(N371_RESULT, N371_RESULT_BLOB)
    main_state = checked(MAIN, MAIN_BLOB, MAIN_CANON)

    req(state["status"].startswith("RETAINED_CURRENT_V15_WITNESS_CANDIDATE"), "N372 retained state drift")
    req(state["next_gate"] == "stage32-01-178-audit", "N372 next gate drift")
    req(result["status"] == "SAT_CURRENT_V15_WITNESS_CANDIDATE", "N372 result status drift")
    req(result["attempt"]["exact_result"] == "sat" and result["attempt"]["parent_ordinal"] == PARENT_ORDINAL, "N372 SAT attempt drift")
    w = result["witness"]
    req(w is not None and w.get("canonical_sha256_without_this_field") == WITNESS_CANON and canonical(w) == WITNESS_CANON, "N372 witness canonical drift")
    req(w["terminal_identity"] == "g1-d008|e=8|rank=128820", "N372 terminal identity drift")

    f = main_state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128 and f["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN V15 authority drift")
    req(f["n357_main_pruning_credit"] is True and f["cut191_main_pruning_credit"] is True and f["cut194_main_pruning_credit"] is True and f["cut195_main_pruning_credit"] is True, "MAIN consumed authority drift")
    req(f["cut193_main_pruning_credit"] is False and f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "MAIN firewall drift")

    e8_path = cut_root / "stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py"
    req(blob(e8_path) == E8_ADAPTER_BLOB, "e8 adapter blob drift")
    e8 = load_module(e8_path, "n372_replay_e8")
    req(not any(k == "z3" or k.startswith("z3.") for k in sys.modules), "e8 replay imported z3")

    comp_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(comp_path) == N357_VERIFIER_BLOB, "N357 verifier blob drift")
    comp = load_module(comp_path, "n372_replay_n357")
    req(not any(k == "z3" or k.startswith("z3.") for k in sys.modules), "N357 replay imported z3")

    idx = e8.indexer()
    survivors = e8.current_main_survivor_block_indices()
    req(len(survivors) == 7596 and survivors[OFFSET] == BLOCK and OFFSET > 765, "current-prefix survivor offset drift")
    sig = e8.block_signature(BLOCK, idx)
    req(sig["current_main_audited_prefix_survivor"] is True, "N220/N355 prefix survival drift")
    req(sig["terminal_rank_range"] == [128820, 128932], "terminal range drift")
    base = tuple(int(v) for v in idx.unrank(BLOCK * WIDTH))
    req(comp.prefix_survives(base), "prefix replay failed")
    req(comp.n357_accepts(base), "consumed N357 rejects witness block")
    sums = [int(v) for v in sig["n355_known_group_sums"]]
    req(sums[1] - sums[2] <= 3 * D - E, "consumed N356 rejects witness block")

    g = e8.load_geometry()
    parents = list(e8.iter_parent_population(BLOCK, g))
    req(len(parents) == EXPECTED_PARENT_COUNT, "block1140 parent population drift")
    parent = parents[PARENT_ORDINAL]
    req(csha(parent["selected_exceptional_pairings"]) == result["attempt"]["selected_exceptional_pairings_sha256"], "parent290 exceptional commitment drift")
    req(parent["x4_allowed_residues_mod8"] == result["attempt"]["x4_allowed_residues_mod8"], "parent290 x4 residues drift")

    bundle = e8.d18.load_retained(e8.d18.RETAINED, "n372_replay_bundle")
    marking = e8.d18.load_retained(e8.d18.MARKING, "n372_replay_marking")
    adapter = e8.d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    G = Matrix(bundle["picard_gram_64x64"])
    req(P.shape == (140, 64) and G.shape == (64, 64), "Picard matrix shape drift")

    coords = [int(v) for v in w["picard64_coordinates"]]
    req(len(coords) == 64 and csha(coords) == w["picard64_coordinates_sha256"], "Picard64 coordinate commitment drift")
    cv = Matrix(coords)
    pairings = [int((P.row(i) * cv)[0]) for i in range(140)]
    req(csha(pairings) == w["all140_pairings_sha256"], "all140 pairing commitment drift")

    selected_labels = [int(v) for v in g.selected_labels]
    Psel = P.extract([label - 1 for label in selected_labels], list(range(64)))
    selected64 = [pairings[label - 1] for label in selected_labels]
    req(selected64 == [int(v) for v in w["selected64_pairings"]], "selected64 replay drift")
    req([int(v) for v in Psel * cv] == selected64, "Psel*c replay drift")
    req(csha([[int(Psel[i,j]) for j in range(64)] for i in range(64)]) == w["selected_pairing_matrix_sha256"], "Psel commitment drift")
    req(csha([[int(G[i,j]) for j in range(64)] for i in range(64)]) == w["gram64_sha256"], "Gram64 commitment drift")

    yE = [selected64[pos] for pos in g.exceptional_positions]
    req(yE == [int(v) for v in parent["selected_exceptional_pairings"]], "parent290 selected-exceptional replay drift")
    x4 = pairings[48]
    req(x4 % g.den in [int(v) for v in parent["x4_allowed_residues_mod8"]], "x4 residue replay drift")

    req(all(0 <= pairings[i] <= NORMAL_MASS for i in range(NORMAL_COUNT)), "normal pairing bounds drift")
    req(all(0 <= pairings[i] <= E for i in range(NORMAL_COUNT, 140)), "exceptional pairing bounds drift")
    req(sum(pairings[:NORMAL_COUNT]) == NORMAL_MASS, "normal mass drift")
    req(sum(pairings[NORMAL_COUNT:]) == E, "exceptional mass drift")

    coords_all = Matrix(adapter.class_coordinates_in_retained_basis)
    full = coords_all * G * coords_all.T
    blocks = []
    fibre_values = []
    for pack in PACKS:
        seen = []; factor_blocks = []
        vals = []
        for boundary in pack:
            inc = [j for j in range(93, 141) if int(full[boundary-1, j-1]) == 1]
            req(len(inc) == 8, f"incidence drift boundary {boundary}")
            seen.extend(inc); factor_blocks.append(inc)
            vals.append(2 * pairings[boundary-1] + sum(pairings[j-1] for j in inc))
        req(sorted(seen) == list(range(93,141)), "fibre partition drift")
        req(all(v == vals[0] for v in vals[1:]), "fibre equality drift")
        blocks.append(factor_blocks); fibre_values.append(vals[0])
    n1, n2 = fibre_values
    req(n1 + n2 == D and 0 <= n1 <= D and 0 <= n2 <= D, "fibre degree split drift")
    req(all(pairings[label-1] <= D//2 for label in range(93,141)), "exceptional D/2 cap drift")
    for b1 in blocks[0]:
        a = sum(pairings[j-1] for j in b1)
        for b2 in blocks[1]:
            req(a + sum(pairings[j-1] for j in b2) <= D, "cross-factor block cap drift")

    terminal = [pairings[label - 1] for label in ASSIGNMENT_ORDER]
    req(terminal == [int(v) for v in w["compressed_terminal_pairings"]], "terminal tuple drift")
    rank = int(idx.rank(tuple(terminal)))
    req(rank == w["terminal_rank"] == 128820, "terminal rank drift")
    req(rank == BLOCK * WIDTH + x4 and list(idx.unrank(rank)) == terminal, "terminal rank roundtrip drift")

    hperp_path = cut_root / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"
    req(blob(hperp_path) == HPERP_BLOB, "Hperp adapter blob drift")
    hperp = load_module(hperp_path, "n372_replay_hperp")
    _, known_degree, _, _, hmeta = hperp._parse_hperp(marking["hperp_text"])
    basis_labels = [int(v) for v in hperp.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    degree = sum(int(known_degree[label-1]) * coords[j] for j, label in enumerate(basis_labels))
    req(degree == D, "degree replay drift")
    req(hmeta["hperp_text_sha256"] == w["hperp_text_sha256"], "Hperp text commitment drift")
    self_square = int((cv.T * G * cv)[0])
    req(self_square == w["self_square"] == -4, "self-square replay drift")
    scale = 16 // math.gcd(D, 16)
    numerator = scale * scale * D * D - 16 * scale * scale * self_square
    req(numerator % 16 == 0 and numerator // 16 == w["negative_hperp_square_N"] == 32, "Hperp scalar replay drift")

    req(not any(k == "z3" or k.startswith("z3.") for k in sys.modules), "solver-independent replay imported z3")
    for key, value in result["credit"].items():
        req(value is False, f"result credit firewall drift: {key}")
    for key, value in state["credit"].items():
        req(value is False, f"state credit firewall drift: {key}")

    print(json.dumps({
        "verdict": "PASS_N372_CURRENT_V15_WITNESS_SOLVER_INDEPENDENT_REPLAY",
        "terminal_identity": w["terminal_identity"],
        "block_index": BLOCK,
        "survivor_offset": OFFSET,
        "parent_ordinal": PARENT_ORDINAL,
        "current_v15_membership_replayed": True,
        "picard64_coordinates_sha256": w["picard64_coordinates_sha256"],
        "all140_pairings_sha256": w["all140_pairings_sha256"],
        "self_square": self_square,
        "negative_hperp_square_N": 32,
        "z3_imported": False,
        "main_pruning_credit": False,
        "full178_complete": False,
        "stage32_closed": False,
        "merge_authorized": False,
        "next_gate": "stage32-01-178-audit"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
