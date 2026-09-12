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
N362_STATE = HERE.parent / "N362/STATE.json"
N362_RESULT = HERE.parent / "N362/RESULT.json"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
HPERP = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"

N361_AUDITED_HEAD = "caf92557103de0bfce1faebb88062dd5e731a430"
CUT196_COMPUTE_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_COMPOSITION_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
N357_COMPOSITION_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
MAIN_STATE_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_STATE_CANONICAL = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
N362_STATE_BLOB = "78d0aa2537910e675ce4768a66a245534bbfbb8c"
N362_STATE_CANONICAL = "a6df6266455f6431b5ecce9f35f5303d96142fa6e5c9299d29a4c3c0a72557a5"
N362_RESULT_BLOB = "0df825cc7604a177e4235032b03d6a88fbca1a74"
N362_RESULT_CANONICAL = "e7d41b4f610def90e95b4979662dccfe3c878c6481fc35ffbae522413364bfb6"
STATE_BLOB = "7f6daeb12ce57eae6ac1895fdd17df686413b42e"
STATE_CANONICAL = "915baa4b6f254ceb88f89dad83e554aca46064005e5e602b6f15e73cb7af62df"
HPERP_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
BLOCK_INDEX = 1140
PARENT_ORDINAL = 290
SURVIVOR_OFFSET = 797
ROW_ID = "g1-d008"
D = 8
E = 8
BLOCK_WIDTH = 113
NORMAL_COUNT = 92
NORMAL_MASS = 112
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_PARENT_HASH = "5aa6566b20c71e3c7328b0b63a196d45b79fccaae1ca8d6f43e82891c7405474"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return csha(q)


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def checked(path: Path, blob_sha: str, canonical_sha: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob_sha, f"blob drift {path}")
    obj = json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field") == canonical_sha, f"stored canonical drift {path}")
    req(canonical(obj) == canonical_sha, f"canonical drift {path}")
    return obj


def preflight(cut_root: Path, comp_root: Path):
    req(exact_head(cut_root) == CUT196_COMPUTE_HEAD, "CUT196 compute head drift")
    req(exact_head(comp_root) == N357_COMPOSITION_HEAD, "N357 composition head drift")
    subprocess.run(["git", "merge-base", "--is-ancestor", N361_AUDITED_HEAD, "HEAD"], cwd=ROOT, check=True)

    state = checked(STATE, STATE_BLOB, STATE_CANONICAL)
    n362s = checked(N362_STATE, N362_STATE_BLOB, N362_STATE_CANONICAL)
    n362r = checked(N362_RESULT, N362_RESULT_BLOB, N362_RESULT_CANONICAL)
    main = checked(MAIN_STATE, MAIN_STATE_BLOB, MAIN_STATE_CANONICAL)

    req(n362s["next_bounded_unit"] == "N363_BLOCK1140_PARENT290_SELECTED64_PARAMETERIZED_EXACT_WITNESS_DECISION", "N362 route drift")
    req(n362r["status"] == "NO_SAT_IN_SINGLE_PARENT_PROBE" and n362r["witness"] is None, "N362 result status drift")
    attempts = {(a["block_index"], a["parent_ordinal"]): a for a in n362r["attempts"]}
    old = attempts[(BLOCK_INDEX, PARENT_ORDINAL)]
    req(old["exact_result"] == "unknown" and old.get("reason_unknown") == "timeout", "N362 timeout locator drift")
    req(old["selected_exceptional_pairings_sha256"] == EXPECTED_PARENT_HASH, "N362 parent hash drift")

    f = main["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN V15 strata drift")
    req(f["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN V15 terminal drift")
    req(f["n357_main_pruning_credit"] is True and f["cut195_main_pruning_credit"] is True, "consumed authority drift")
    req(f["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")

    comp_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(git_blob(comp_path) == N357_COMPOSITION_VERIFIER_BLOB, "N357 composition verifier drift")
    proc = subprocess.run([sys.executable, str(comp_path)], cwd=comp_root, text=True, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout); sys.stderr.write(proc.stderr)
        raise RuntimeError("N357 audited composition replay failed")
    req("PASS_N357_CURRENT_V13_AUTHORITY_COMPOSITION_REPLAY" in proc.stdout, "N357 composition verdict missing")

    cut196_path = cut_root / "stages/stage32/full178-cut/cut196_e8_common_adapter_wave4.py"
    cut196 = load_module(cut196_path, "n363_cut196")
    cut196.preflight()
    comp = load_module(comp_path, "n363_n357comp")
    return state, cut196, comp


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    state, cut196, comp = preflight(args.cut196_root.resolve(), args.n357_composition_root.resolve())
    core = cut196.core
    P, blocks, g = core.load_picard_interface()
    idx = core.e8.indexer()
    survivors = core.e8.current_main_survivor_block_indices()
    req(survivors[SURVIVOR_OFFSET] == BLOCK_INDEX, "block1140 survivor offset drift")
    req(SURVIVOR_OFFSET > 765, "block1140 overlaps consumed CUT offset prefix")
    sig = core.e8.block_signature(BLOCK_INDEX, idx)
    req(sig["current_main_audited_prefix_survivor"] is True, "block1140 lost N220/N355 survival")
    base = tuple(int(v) for v in idx.unrank(BLOCK_INDEX * BLOCK_WIDTH))
    req(comp.prefix_survives(base), "block1140 prefix replay failed")
    req(comp.n357_accepts(base), "block1140 rejected by consumed N357")
    sums = [int(v) for v in sig["n355_known_group_sums"]]
    req(sums[1] - sums[2] <= 3 * D - E, "block1140 rejected by consumed N356")

    parents = list(core.e8.iter_parent_population(BLOCK_INDEX, g))
    req(len(parents) == 300 and PARENT_ORDINAL < len(parents), "block1140 parent population drift")
    parent = parents[PARENT_ORDINAL]
    yE = [int(v) for v in parent["selected_exceptional_pairings"]]
    req(csha(yE) == EXPECTED_PARENT_HASH, "parent290 selected exceptional hash drift")
    allowed = [int(v) for v in parent["x4_allowed_residues_mod8"]]
    req(allowed == list(range(8)), "parent290 x4 residue set drift")

    labels = [int(v) for v in g.selected_labels]
    req(len(labels) == 64 and g.den == 8, "selected64 geometry drift")
    ysel: list[object] = [None] * 64
    exceptional_by_pos = {pos: yE[k] for k, pos in enumerate(g.exceptional_positions)}
    for pos in range(64):
        if pos in exceptional_by_pos:
            ysel[pos] = int(exceptional_by_pos[pos])
        else:
            ysel[pos] = Int(f"s_{labels[pos]}")

    s = SolverFor("QF_LIA")
    s.set(timeout=int(state["method"]["exact_timeout_ms"]))
    for pos in g.normal_positions:
        s.add(ysel[pos] >= 0, ysel[pos] <= NORMAL_MASS)
    x4pos = g.pos_by_label[49]
    s.add(Or(*[(ysel[x4pos] % 8) == r for r in allowed]))

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
    witness = None
    if r == sat:
        m = s.model()
        selected = [int(v) if isinstance(v, int) else int(m.eval(v, model_completion=True).as_long()) for v in ysel]
        cnums = [int(m.eval(v, model_completion=True).as_long()) for v in cnum]
        req(all(v % g.den == 0 for v in cnums), "coordinate divisibility replay failed")
        coords = [v // g.den for v in cnums]
        yn = [int(m.eval(v, model_completion=True).as_long()) for v in ynum]
        req(all(v % g.den == 0 for v in yn), "all140 divisibility replay failed")
        pairings = [v // g.den for v in yn]
        cv = Matrix(coords)
        req([int(v) for v in (P * cv)] == pairings, "P*c all140 replay failed")
        req([pairings[label - 1] for label in labels] == selected, "selected64 replay failed")
        terminal = [pairings[label - 1] for label in ASSIGNMENT_ORDER]
        rank = int(idx.rank(tuple(terminal)))
        req(BLOCK_INDEX * BLOCK_WIDTH <= rank <= BLOCK_INDEX * BLOCK_WIDTH + 112, "terminal rank left block1140")
        req(list(idx.unrank(rank)) == terminal, "terminal rank roundtrip failed")

        hperp = load_module(HPERP, "n363_hperp")
        req(git_blob(HPERP) == HPERP_BLOB, "Hperp adapter drift")
        bundle = core.e8.d18.load_retained(core.e8.d18.RETAINED, "n363_bundle")
        marking = core.e8.d18.load_retained(core.e8.d18.MARKING, "n363_marking")
        G = Matrix(bundle["picard_gram_64x64"])
        _, known_degree, _, _, hmeta = hperp._parse_hperp(marking["hperp_text"])
        basis_labels = [int(v) for v in hperp.RETAINED_BASIS_KNOWN_LABELS_1BASED]
        degree_coeffs = [int(known_degree[v - 1]) for v in basis_labels]
        degree = sum(degree_coeffs[j] * coords[j] for j in range(64))
        req(degree == D, "degree replay failed")
        self_square = int((cv.T * G * cv)[0])
        scale = 16 // math.gcd(D, 16)
        numerator = scale * scale * D * D - 16 * scale * scale * self_square
        req(numerator % 16 == 0, "Hperp scalar integrality failed")
        neg_n = numerator // 16
        Psel = P.extract([label - 1 for label in labels], list(range(64)))
        psel_plain = [[int(Psel[i, j]) for j in range(64)] for i in range(64)]
        gram_plain = [[int(G[i, j]) for j in range(64)] for i in range(64)]
        witness = {
            "schema": "STAGE32_32_01_178_N363_CURRENT_V15_SELECTED64_WITNESS_V1",
            "row_id": ROW_ID,
            "g": 1,
            "d": D,
            "e": E,
            "block_index": BLOCK_INDEX,
            "survivor_offset": SURVIVOR_OFFSET,
            "parent_ordinal": PARENT_ORDINAL,
            "terminal_rank": rank,
            "terminal_identity": f"{ROW_ID}|e={E}|rank={rank}",
            "compressed_terminal_pairings": terminal,
            "selected64_pairings": selected,
            "picard64_coordinates": coords,
            "all140_pairings_sha256": csha(pairings),
            "selected_pairing_matrix_sha256": csha(psel_plain),
            "gram64_sha256": csha(gram_plain),
            "picard64_coordinates_sha256": csha(coords),
            "self_square": self_square,
            "negative_hperp_square_N": neg_n,
            "hperp_text_sha256": hmeta["hperp_text_sha256"],
            "current_v15_membership": {
                "n220_n355_prefix_survivor": true,
                "n356_accepts": true,
                "n357_accepts": true,
                "outside_consumed_cut_offset_prefix_0_765": true,
                "cut196_not_consumed_into_main": true
            },
            "credit": {
                "current_v15_single_witness_candidate": true,
                "main_pruning_credit": false,
                "full178_complete": false,
                "n350_registered": false,
                "effectivity_final": false,
                "receiver_credit": false,
                "theorem_credit": false,
                "endpoint_credit": false,
                "stage32_closed": false,
                "merge_authorized": false
            }
        }
        witness["canonical_sha256_without_this_field"] = csha(witness)

    body = {
        "schema": "STAGE32_32_01_178_N363_BLOCK1140_SELECTED64_ELIMINATION_RESULT_V1",
        "status": "SAT_CURRENT_V15_WITNESS_CANDIDATE" if r == sat else ("EXACT_UNSAT_SELECTED64_ELIMINATION" if str(r) == "unsat" else "UNKNOWN_SELECTED64_ELIMINATION"),
        "exact_result": str(r),
        "reason_unknown": s.reason_unknown() if r == unknown else null,
        "target": {"block_index": BLOCK_INDEX, "survivor_offset": SURVIVOR_OFFSET, "parent_ordinal": PARENT_ORDINAL},
        "method": state["method"],
        "witness": witness,
        "credit": {
            "main_pruning_credit": false,
            "full178_complete": false,
            "n350_registered": false,
            "effectivity_final": false,
            "receiver_credit": false,
            "theorem_credit": false,
            "endpoint_credit": false,
            "stage32_closed": false,
            "merge_authorized": false
        }
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": body["status"],
        "exact_result": body["exact_result"],
        "reason_unknown": body["reason_unknown"],
        "terminal_identity": witness["terminal_identity"] if witness else None,
        "self_square": witness["self_square"] if witness else None,
        "negative_hperp_square_N": witness["negative_hperp_square_N"] if witness else None,
        "canonical": body["canonical_sha256_without_this_field"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
