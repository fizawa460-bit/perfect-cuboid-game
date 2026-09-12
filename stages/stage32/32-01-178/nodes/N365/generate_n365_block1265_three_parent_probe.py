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
N364_STATE = HERE.parent / "N364/STATE.json"
N364_RESULT = HERE.parent / "N364/RESULT.json"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
HPERP = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"

CUT196_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
N357_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_CANON = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
N364_STATE_BLOB = "ee76313b8fc3a6c901038fa76b0b1ba0630681af"
N364_STATE_CANON = "e5f8bb5510d96ce02226850e7aa0c6585e69b910df189b885891a21a17696a50"
N364_RESULT_BLOB = "eeafab917537c793e89c4df5656a2e52488dca68"
N364_RESULT_CANON = "2c8cc223a461c33bfa296023745b661a9843aa98ad4a849aa13869f82cf1cd4b"
STATE_BLOB = "13d4b446c3c658dc3f332b3c9432de2eb508cd41"
STATE_CANON = "9e48228b41027de2db435e45ac0724ecef107be35f65608a4b8a5ba6f1cf418b"
HPERP_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
BLOCK, OFFSET, WIDTH = 1265, 891, 113
D = E = 8
NORMAL_COUNT, NORMAL_MASS = 92, 112
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_PARENT_COUNT = 181
EXPECTED_RESIDUAL_COUNT = 3
EXPECTED_RESIDUAL_STREAM = "06638d2743bc21c504dc935a6a7711c0cbe3f82f867a4bab12e7d16567fbaf71"


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
    mod = importlib.util.module_from_spec(spec); sys.modules[name] = mod; spec.loader.exec_module(mod)
    return mod


def preflight(cut_root: Path, comp_root: Path):
    req(exact_head(cut_root) == CUT196_HEAD, "CUT196 head drift")
    req(exact_head(comp_root) == N357_HEAD, "N357 composition head drift")
    state = checked(STATE, STATE_BLOB, STATE_CANON)
    n364s = checked(N364_STATE, N364_STATE_BLOB, N364_STATE_CANON)
    n364r = checked(N364_RESULT, N364_RESULT_BLOB, N364_RESULT_CANON)
    main = checked(MAIN_STATE, MAIN_BLOB, MAIN_CANON)
    req(n364r["status"] == "NO_SAT_IN_TWO_PARENT_PROBE" and n364r["witness"] is None, "N364 result drift")
    req(n364s["target"]["block_index"] == 1405, "N364 state target drift")
    f = main["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN V15 terminal drift")
    req(f["n357_main_pruning_credit"] is True and f["cut195_main_pruning_credit"] is True, "MAIN consumed authority drift")
    req(f["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")
    comp_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(comp_path) == N357_VERIFIER_BLOB, "N357 verifier drift")
    p = subprocess.run([sys.executable, str(comp_path)], cwd=comp_root, text=True, capture_output=True)
    req(p.returncode == 0 and "PASS_N357_CURRENT_V13_AUTHORITY_COMPOSITION_REPLAY" in p.stdout, "N357 replay failed")
    cut196 = load_module(cut_root / "stages/stage32/full178-cut/cut196_e8_common_adapter_wave4.py", "n365_cut196")
    cut196.preflight()
    comp = load_module(comp_path, "n365_n357comp")
    return state, cut196, comp


def residual_ordinals(core, P, blocks, g):
    parents = list(core.e8.iter_parent_population(BLOCK, g))
    req(len(parents) == EXPECTED_PARENT_COUNT, "block1265 parent population drift")
    primes = list(core.DEFAULT_PRIMES)
    solvers = {p: core.make_solver(P, blocks, p, 750) for p in primes}
    unresolved = set(range(len(parents)))
    for prime in primes:
        s, y, _ = solvers[prime]
        for ordinal in list(unresolved):
            parent = parents[ordinal]
            fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, parent["selected_exceptional_pairings"])}
            result, _reason = core.check_with_fixed(s, y, fixed)
            if result == "unsat":
                unresolved.remove(ordinal)
    out = sorted(unresolved)
    req(len(out) == EXPECTED_RESIDUAL_COUNT, f"CUT196 residual count drift: {len(out)}")
    stream = hashlib.sha256("".join(f"{v}\n" for v in out).encode()).hexdigest()
    req(stream == EXPECTED_RESIDUAL_STREAM, "CUT196 residual ordinal stream drift")
    return out


def solve_parent(state: dict, core, P: Matrix, blocks, g, idx, parent_ordinal: int):
    parents = list(core.e8.iter_parent_population(BLOCK, g))
    req(len(parents) == EXPECTED_PARENT_COUNT, "block1265 exact parent population drift")
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
        for v in vals[1:]: s.add(v == vals[0])
        fibre.append(vals[0])
    n1, n2 = fibre
    s.add(n1 + n2 == D * g.den, n1 >= 0, n1 <= D * g.den, n2 >= 0, n2 <= D * g.den)
    for label in range(93, 141): s.add(ynum[label - 1] <= (D // 2) * g.den)
    for b1 in blocks[0]:
        a = Sum([ynum[j - 1] for j in b1])
        for b2 in blocks[1]: s.add(a + Sum([ynum[j - 1] for j in b2]) <= D * g.den)
    r = s.check()
    attempt = {"parent_ordinal":parent_ordinal,"selected_exceptional_pairings_sha256":csha(yE),"x4_allowed_residues_mod8":allowed,"exact_result":str(r),"reason_unknown":s.reason_unknown() if r == unknown else None}
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
    hperp = load_module(HPERP, f"n365_hperp_{parent_ordinal}")
    bundle = core.e8.d18.load_retained(core.e8.d18.RETAINED, f"n365_bundle_{parent_ordinal}")
    marking = core.e8.d18.load_retained(core.e8.d18.MARKING, f"n365_marking_{parent_ordinal}")
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
        "schema":"STAGE32_32_01_178_N365_CURRENT_V15_SELECTED64_WITNESS_V1",
        "row_id":"g1-d008","g":1,"d":D,"e":E,"block_index":BLOCK,"survivor_offset":OFFSET,"parent_ordinal":parent_ordinal,
        "terminal_rank":rank,"terminal_identity":f"g1-d008|e=8|rank={rank}","compressed_terminal_pairings":terminal,"selected64_pairings":selected,"picard64_coordinates":coords,
        "all140_pairings_sha256":csha(pairings),"selected_pairing_matrix_sha256":csha([[int(Psel[i,j]) for j in range(64)] for i in range(64)]),
        "gram64_sha256":csha([[int(G[i,j]) for j in range(64)] for i in range(64)]),"picard64_coordinates_sha256":csha(coords),"self_square":self_square,"negative_hperp_square_N":neg_n,"hperp_text_sha256":hmeta["hperp_text_sha256"],
        "current_v15_membership":{"n220_n355_prefix_survivor":True,"n356_accepts":True,"n357_accepts":True,"outside_consumed_cut_offset_prefix_0_765":True,"cut196_not_consumed_into_main":True},
        "credit":{"current_v15_single_witness_candidate":True,"main_pruning_credit":False,"full178_complete":False,"n350_registered":False,"effectivity_final":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"stage32_closed":False,"merge_authorized":False}
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
    req(survivors[OFFSET] == BLOCK and OFFSET > 765, "block1265 offset drift")
    sig = core.e8.block_signature(BLOCK, idx)
    base = tuple(int(v) for v in idx.unrank(BLOCK * WIDTH))
    req(sig["current_main_audited_prefix_survivor"] is True, "prefix survival drift")
    req(comp.prefix_survives(base) and comp.n357_accepts(base), "prefix/N357 replay failed")
    sums = [int(v) for v in sig["n355_known_group_sums"]]
    req(sums[1] - sums[2] <= 3 * D - E, "N356 replay failed")

    ordinals = residual_ordinals(core, P, blocks, g)
    attempts = []
    witness = None
    for ordinal in ordinals:
        attempt, candidate = solve_parent(state, core, P, blocks, g, idx, ordinal)
        attempts.append(attempt)
        if candidate is not None:
            witness = candidate
            break
    if witness:
        status = "SAT_CURRENT_V15_WITNESS_CANDIDATE"
    elif any(a["exact_result"] == "unknown" for a in attempts):
        status = "UNKNOWN_REMAINS_IN_THREE_PARENT_PROBE"
    else:
        status = "NO_SAT_IN_THREE_PARENT_PROBE"
    body = {
        "schema":"STAGE32_32_01_178_N365_BLOCK1265_THREE_PARENT_WITNESS_RESULT_V1","status":status,
        "target":{"block_index":BLOCK,"survivor_offset":OFFSET,"parent_ordinals":ordinals},"cut196_residual_parent_ordinal_sha256":EXPECTED_RESIDUAL_STREAM,
        "attempts":attempts,"witness":witness,
        "credit":{"main_pruning_credit":False,"full178_complete":False,"n350_registered":False,"effectivity_final":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"stage32_closed":False,"merge_authorized":False}
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status":status,"parent_ordinals":ordinals,"attempts":attempts,"terminal_identity":witness["terminal_identity"] if witness else None,"canonical":body["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
