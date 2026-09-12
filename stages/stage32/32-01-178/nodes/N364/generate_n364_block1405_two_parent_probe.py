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
from z3 import Int, Or, SolverFor, Sum, sat, unknown

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
STATE = HERE / "STATE.json"
N363_STATE = HERE.parent / "N363/STATE.json"
N363_RESULT = HERE.parent / "N363/RESULT.json"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
HPERP = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"

N361_HEAD = "caf92557103de0bfce1faebb88062dd5e731a430"
CUT196_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
N357_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_CANON = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
N363_STATE_BLOB = "7deaa4084bc64e29c971f61168504e7b1ed7426c"
N363_STATE_CANON = "870d38bfe309ad79ca8bde307107e6692f545f6136d79756b80bbd6a8dab1cb6"
N363_RESULT_BLOB = "cf81550d326e1e7f290994a126268cdf7a479416"
N363_RESULT_CANON = "8c0e31204928570f3dd7161edfd4e676325df4a10008cb7d19aa7255320152c3"
STATE_BLOB = "ee76313b8fc3a6c901038fa76b0b1ba0630681af"
STATE_CANON = "e5f8bb5510d96ce02226850e7aa0c6585e69b910df189b885891a21a17696a50"
HPERP_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
BLOCK, OFFSET = 1405, 980
PARENTS = [2, 4]
D = E = 8
NORMAL_COUNT, NORMAL_MASS, WIDTH = 92, 112, 113
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
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return csha(q)


def checked(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
    req(canonical(obj) == expected_canon, f"canonical drift: {path}")
    return obj


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def preflight(cut_root: Path, comp_root: Path):
    req(exact_head(cut_root) == CUT196_HEAD, "CUT196 head drift")
    req(exact_head(comp_root) == N357_HEAD, "N357 composition head drift")
    subprocess.run(["git", "merge-base", "--is-ancestor", N361_HEAD, "HEAD"], cwd=ROOT, check=True)
    state = checked(STATE, STATE_BLOB, STATE_CANON)
    n363s = checked(N363_STATE, N363_STATE_BLOB, N363_STATE_CANON)
    n363r = checked(N363_RESULT, N363_RESULT_BLOB, N363_RESULT_CANON)
    main = checked(MAIN_STATE, MAIN_BLOB, MAIN_CANON)
    req(n363s["next_bounded_unit"] == "N364_BLOCK1405_TWO_RESIDUAL_PARENTS_SELECTED64_EXACT_WITNESS_PROBE", "N363 route drift")
    req(n363r["status"] == "UNKNOWN_SELECTED64_ELIMINATION" and n363r["reason_unknown"] == "timeout", "N363 result drift")
    req(csha(PARENTS) != state["selection_provenance"]["cut196_residual_parent_ordinal_sha256"], "ordinal digest unexpectedly uses JSON encoding")
    ordinal_stream = hashlib.sha256("".join(f"{v}\n" for v in PARENTS).encode()).hexdigest()
    req(ordinal_stream == state["selection_provenance"]["cut196_residual_parent_ordinal_sha256"], "CUT196 residual ordinal stream drift")
    f = main["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN terminal drift")
    req(f["n357_main_pruning_credit"] is True and f["cut195_main_pruning_credit"] is True, "MAIN consumed authority drift")
    req(f["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")
    comp_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(comp_path) == N357_VERIFIER_BLOB, "N357 verifier drift")
    p = subprocess.run([sys.executable, str(comp_path)], cwd=comp_root, text=True, capture_output=True)
    req(p.returncode == 0 and "PASS_N357_CURRENT_V13_AUTHORITY_COMPOSITION_REPLAY" in p.stdout, "N357 composition replay failed")
    cut196 = load_module(cut_root / "stages/stage32/full178-cut/cut196_e8_common_adapter_wave4.py", "n364_cut196")
    cut196.preflight()
    comp = load_module(comp_path, "n364_n357comp")
    return state, cut196, comp


def solve_parent(state: dict, core, P: Matrix, blocks, g, idx, parent_ordinal: int):
    parents = list(core.e8.iter_parent_population(BLOCK, g))
    req(len(parents) == 30, "block1405 parent population drift")
    parent = parents[parent_ordinal]
    yE = [int(v) for v in parent["selected_exceptional_pairings"]]
    labels = [int(v) for v in g.selected_labels]
    by_pos = {pos: yE[k] for k, pos in enumerate(g.exceptional_positions)}
    ysel = [int(by_pos[pos]) if pos in by_pos else Int(f"p{parent_ordinal}_s_{labels[pos]}") for pos in range(64)]
    s = SolverFor("QF_LIA")
    s.set(timeout=int(state["method"]["per_parent_timeout_ms"]))
    for pos in g.normal_positions:
        s.add(ysel[pos] >= 0, ysel[pos] <= NORMAL_MASS)
    allowed = [int(v) for v in parent["x4_allowed_residues_mod8"]]
    req(allowed, "empty x4 residue set")
    x4pos = g.pos_by_label[49]
    s.add(Or(*[(ysel[x4pos] % g.den) == r for r in allowed]))
    B = Matrix(g.B)
    A = P * B
    cnum = [Sum([int(B[k, j]) * ysel[j] for j in range(64)]) for k in range(64)]
    for v in cnum:
        s.add(v % g.den == 0)
    ynum = [Sum([int(A[i, j]) * ysel[j] for j in range(64)]) for i in range(140)]
    for i in range(NORMAL_COUNT):
        s.add(ynum[i] >= 0, ynum[i] <= NORMAL_MASS * g.den)
    for i in range(NORMAL_COUNT, 140):
        s.add(ynum[i] >= 0, ynum[i] <= E * g.den)
    s.add(Sum(ynum[:NORMAL_COUNT]) == NORMAL_MASS * g.den)
    s.add(Sum(ynum[NORMAL_COUNT:]) == E * g.den)
    fibre = []
    for pack, factor_blocks in zip(core.PACKS, blocks):
        vals = [2 * ynum[b - 1] + Sum([ynum[j - 1] for j in block]) for b, block in zip(pack, factor_blocks)]
        for v in vals[1:]:
            s.add(v == vals[0])
        fibre.append(vals[0])
    n1, n2 = fibre
    s.add(n1 + n2 == D * g.den, n1 >= 0, n1 <= D * g.den, n2 >= 0, n2 <= D * g.den)
    for label in range(93, 141):
        s.add(ynum[label - 1] <= (D // 2) * g.den)
    for b1 in blocks[0]:
        a = Sum([ynum[j - 1] for j in b1])
        for b2 in blocks[1]:
            s.add(a + Sum([ynum[j - 1] for j in b2]) <= D * g.den)
    r = s.check()
    attempt = {
        "parent_ordinal": parent_ordinal,
        "selected_exceptional_pairings_sha256": csha(yE),
        "x4_allowed_residues_mod8": allowed,
        "exact_result": str(r),
        "reason_unknown": s.reason_unknown() if r == unknown else None
    }
    if r != sat:
        return attempt, None
    m = s.model()
    selected = [v if isinstance(v, int) else int(m.eval(v, model_completion=True).as_long()) for v in ysel]
    cnums = [int(m.eval(v, model_completion=True).as_long()) for v in cnum]
    req(all(v % g.den == 0 for v in cnums), "coordinate divisibility failed")
    coords = [v // g.den for v in cnums]
    yn = [int(m.eval(v, model_completion=True).as_long()) for v in ynum]
    req(all(v % g.den == 0 for v in yn), "all140 divisibility failed")
    pairings = [v // g.den for v in yn]
    cv = Matrix(coords)
    req([int(v) for v in P * cv] == pairings, "P*c replay failed")
    req([pairings[label - 1] for label in labels] == selected, "selected64 replay failed")
    terminal = [pairings[label - 1] for label in ASSIGNMENT_ORDER]
    rank = int(idx.rank(tuple(terminal)))
    req(BLOCK * WIDTH <= rank <= BLOCK * WIDTH + 112 and list(idx.unrank(rank)) == terminal, "terminal rank replay failed")
    req(blob(HPERP) == HPERP_BLOB, "Hperp adapter drift")
    hperp = load_module(HPERP, f"n364_hperp_{parent_ordinal}")
    bundle = core.e8.d18.load_retained(core.e8.d18.RETAINED, f"n364_bundle_{parent_ordinal}")
    marking = core.e8.d18.load_retained(core.e8.d18.MARKING, f"n364_marking_{parent_ordinal}")
    G = Matrix(bundle["picard_gram_64x64"])
    _, known_degree, _, _, hmeta = hperp._parse_hperp(marking["hperp_text"])
    basis_labels = [int(v) for v in hperp.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    degree = sum(int(known_degree[label - 1]) * coords[j] for j, label in enumerate(basis_labels))
    req(degree == D, "degree replay failed")
    self_square = int((cv.T * G * cv)[0])
    scale = 16 // math.gcd(D, 16)
    numerator = scale * scale * D * D - 16 * scale * scale * self_square
    req(numerator % 16 == 0, "Hperp scalar integrality failed")
    neg_n = numerator // 16
    Psel = P.extract([label - 1 for label in labels], list(range(64)))
    witness = {
        "schema": "STAGE32_32_01_178_N364_CURRENT_V15_SELECTED64_WITNESS_V1",
        "row_id": "g1-d008", "g": 1, "d": D, "e": E,
        "block_index": BLOCK, "survivor_offset": OFFSET, "parent_ordinal": parent_ordinal,
        "terminal_rank": rank, "terminal_identity": f"g1-d008|e=8|rank={rank}",
        "compressed_terminal_pairings": terminal,
        "selected64_pairings": selected,
        "picard64_coordinates": coords,
        "all140_pairings_sha256": csha(pairings),
        "selected_pairing_matrix_sha256": csha([[int(Psel[i, j]) for j in range(64)] for i in range(64)]),
        "gram64_sha256": csha([[int(G[i, j]) for j in range(64)] for i in range(64)]),
        "picard64_coordinates_sha256": csha(coords),
        "self_square": self_square,
        "negative_hperp_square_N": neg_n,
        "hperp_text_sha256": hmeta["hperp_text_sha256"],
        "current_v15_membership": {
            "n220_n355_prefix_survivor": True,
            "n356_accepts": True,
            "n357_accepts": True,
            "outside_consumed_cut_offset_prefix_0_765": True,
            "cut196_not_consumed_into_main": True
        },
        "credit": {
            "current_v15_single_witness_candidate": True,
            "main_pruning_credit": False,
            "full178_complete": False,
            "n350_registered": False,
            "effectivity_final": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False
        }
    }
    witness["canonical_sha256_without_this_field"] = csha(witness)
    return attempt, witness


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    state, cut196, comp = preflight(args.cut196_root.resolve(), args.n357_composition_root.resolve())
    core = cut196.core
    P, blocks, g = core.load_picard_interface()
    req(g.den == 8, "selected64 denominator drift")
    idx = core.e8.indexer()
    survivors = core.e8.current_main_survivor_block_indices()
    req(survivors[OFFSET] == BLOCK and OFFSET > 765, "block1405 offset drift")
    sig = core.e8.block_signature(BLOCK, idx)
    base = tuple(int(v) for v in idx.unrank(BLOCK * WIDTH))
    req(sig["current_main_audited_prefix_survivor"] is True, "prefix survival drift")
    req(comp.prefix_survives(base) and comp.n357_accepts(base), "prefix/N357 replay failed")
    sums = [int(v) for v in sig["n355_known_group_sums"]]
    req(sums[1] - sums[2] <= 3 * D - E, "N356 replay failed")

    attempts = []
    witness = None
    for parent_ordinal in PARENTS:
        attempt, candidate = solve_parent(state, core, P, blocks, g, idx, parent_ordinal)
        attempts.append(attempt)
        if candidate is not None:
            witness = candidate
            break
    status = "SAT_CURRENT_V15_WITNESS_CANDIDATE" if witness else "NO_SAT_IN_TWO_PARENT_PROBE"
    body = {
        "schema": "STAGE32_32_01_178_N364_BLOCK1405_TWO_PARENT_WITNESS_RESULT_V1",
        "status": status,
        "target": {"block_index": BLOCK, "survivor_offset": OFFSET, "parent_ordinals": PARENTS},
        "attempts": attempts,
        "witness": witness,
        "credit": {
            "main_pruning_credit": False,
            "full178_complete": False,
            "n350_registered": False,
            "effectivity_final": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False
        }
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": status,
        "attempts": attempts,
        "terminal_identity": witness["terminal_identity"] if witness else None,
        "self_square": witness["self_square"] if witness else None,
        "negative_hperp_square_N": witness["negative_hperp_square_N"] if witness else None,
        "canonical": body["canonical_sha256_without_this_field"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
