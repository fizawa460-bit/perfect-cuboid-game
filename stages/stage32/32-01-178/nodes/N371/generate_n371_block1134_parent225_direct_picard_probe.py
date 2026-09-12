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
from z3 import sat, unknown

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
STATE = HERE / "STATE.json"
N370_RESULT = HERE.parent / "N370/RESULT.json"
N362_GENERATOR = HERE.parent / "N362/generate_n362_current_v15_witness_probe.py"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
HPERP = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"

CUT196_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
N357_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_CANON = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
STATE_BLOB = "dbfd2be93d5f066eb5e892497a94fe100fb4f2d9"
STATE_CANON = "5536d0392ac9993ee6333c674bebfc0f4f15c61471ce9dbea0112c5a40727d06"
N370_RESULT_BLOB = "2993ec4eac0cfbc3d8c43e09de72d1ea17308bf2"
N370_RESULT_CANON = "83156f01f005443d4ed92d845de23b7a9a95882c904a27322c3700df667871f7"
N362_GENERATOR_BLOB = "f2b97ffb52dcf48e8e549cf71eb70a6ffcdebb30"
HPERP_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
BLOCK, OFFSET, WIDTH = 1134, 793, 113
PARENT_ORDINAL = 225
EXPECTED_PARENT_COUNT = 1560
EXPECTED_SELECTED_EXCEPTIONAL_SHA = "f6a44aec7bed74b46a3399221b77664e506316dcdda5f9579c8f1c15ff637f4e"
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
D = E = 8


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
    state = checked(STATE, STATE_BLOB, STATE_CANON)
    n370 = checked(N370_RESULT, N370_RESULT_BLOB, N370_RESULT_CANON)
    main = checked(MAIN_STATE, MAIN_BLOB, MAIN_CANON)
    req(blob(N362_GENERATOR) == N362_GENERATOR_BLOB, "N362 direct generator drift")
    req(n370["status"] == "UNKNOWN_PARENT225_EXTENDED_EXACT" and n370["witness"] is None, "N370 result drift")
    req(n370["attempt"]["parent_ordinal"] == PARENT_ORDINAL and n370["attempt"]["reason_unknown"] == "timeout", "N370 timeout identity drift")
    req(state["method"]["direct_picard64_coordinate_variables"] is True and state["method"]["per_parent_timeout_ms"] == 60000, "N371 method drift")
    f = main["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN V15 terminal drift")
    req(f["n357_main_pruning_credit"] is True and f["cut195_main_pruning_credit"] is True, "MAIN consumed authority drift")
    req(f["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")
    comp_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(comp_path) == N357_VERIFIER_BLOB, "N357 verifier drift")
    p = subprocess.run([sys.executable, str(comp_path)], cwd=comp_root, text=True, capture_output=True)
    req(p.returncode == 0 and "PASS_N357_CURRENT_V13_AUTHORITY_COMPOSITION_REPLAY" in p.stdout, "N357 replay failed")
    cut196 = load_module(cut_root / "stages/stage32/full178-cut/cut196_e8_common_adapter_wave4.py", "n371_cut196")
    cut196.preflight()
    comp = load_module(comp_path, "n371_n357comp")
    n362 = load_module(N362_GENERATOR, "n371_n362_direct")
    return state, cut196, comp, n362


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    state, cut196, comp, n362 = preflight(args.cut196_root.resolve(), args.n357_composition_root.resolve())
    core = cut196.core
    P, blocks, g = core.load_picard_interface()
    idx = core.e8.indexer()
    survivors = core.e8.current_main_survivor_block_indices()
    req(survivors[OFFSET] == BLOCK and OFFSET > 765, "block1134 survivor offset drift")
    sig = core.e8.block_signature(BLOCK, idx)
    base = tuple(int(v) for v in idx.unrank(BLOCK * WIDTH))
    req(sig["current_main_audited_prefix_survivor"] is True, "prefix survival drift")
    req(comp.prefix_survives(base) and comp.n357_accepts(base), "prefix/N357 replay failed")
    sums = [int(v) for v in sig["n355_known_group_sums"]]
    req(sums[1] - sums[2] <= 16, "N356 replay failed")
    parents = list(core.e8.iter_parent_population(BLOCK, g))
    req(len(parents) == EXPECTED_PARENT_COUNT, "block1134 parent population drift")
    parent = parents[PARENT_ORDINAL]
    req(csha(parent["selected_exceptional_pairings"]) == EXPECTED_SELECTED_EXCEPTIONAL_SHA, "parent225 selected exceptional identity drift")

    timeout_ms = int(state["method"]["per_parent_timeout_ms"])
    s, cvars, yexpr, fixed, allowed = n362.exact_solver_for_parent(core, P, blocks, g, BLOCK, parent, timeout_ms)
    r = s.check()
    attempt = {
        "parent_ordinal": PARENT_ORDINAL,
        "selected_exceptional_pairings_sha256": EXPECTED_SELECTED_EXCEPTIONAL_SHA,
        "x4_allowed_residues_mod8": allowed,
        "exact_result": str(r),
        "reason_unknown": s.reason_unknown() if r == unknown else None,
        "formulation": "DIRECT_PICARD64_COORDINATE_VARIABLES"
    }
    witness = None
    if r == sat:
        m = s.model()
        coords = [int(m.eval(v, model_completion=True).as_long()) for v in cvars]
        pairings = [int(m.eval(v, model_completion=True).as_long()) for v in yexpr]
        terminal = [pairings[label - 1] for label in ASSIGNMENT_ORDER]
        rank = int(idx.rank(tuple(terminal)))
        req(BLOCK * WIDTH <= rank <= BLOCK * WIDTH + 112 and list(idx.unrank(rank)) == terminal, "terminal rank replay failed")
        selected_labels = [int(v) for v in g.selected_labels]
        selected64 = [pairings[label - 1] for label in selected_labels]
        cv = Matrix(coords)
        Psel = P.extract([label - 1 for label in selected_labels], list(range(64)))
        req([int(v) for v in Psel * cv] == selected64, "selected64 replay failed")
        req([int(v) for v in P * cv] == pairings, "all140 replay failed")
        req(blob(HPERP) == HPERP_BLOB, "Hperp adapter drift")
        hperp = load_module(HPERP, "n371_hperp")
        bundle = core.e8.d18.load_retained(core.e8.d18.RETAINED, "n371_bundle")
        marking = core.e8.d18.load_retained(core.e8.d18.MARKING, "n371_marking")
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
        witness = {
            "schema": "STAGE32_32_01_178_N371_CURRENT_V15_DIRECT_PICARD64_WITNESS_V1",
            "row_id": "g1-d008",
            "g": 1,
            "d": D,
            "e": E,
            "block_index": BLOCK,
            "survivor_offset": OFFSET,
            "parent_ordinal": PARENT_ORDINAL,
            "terminal_rank": rank,
            "terminal_identity": f"g1-d008|e=8|rank={rank}",
            "compressed_terminal_pairings": terminal,
            "selected64_pairings": selected64,
            "picard64_coordinates": coords,
            "all140_pairings_sha256": csha(pairings),
            "selected_pairing_matrix_sha256": csha([[int(Psel[i,j]) for j in range(64)] for i in range(64)]),
            "gram64_sha256": csha([[int(G[i,j]) for j in range(64)] for i in range(64)]),
            "picard64_coordinates_sha256": csha(coords),
            "self_square": self_square,
            "negative_hperp_square_N": neg_n,
            "hperp_text_sha256": hmeta["hperp_text_sha256"]
        }
        witness["canonical_sha256_without_this_field"] = csha(witness)
        status = "SAT_CURRENT_V15_WITNESS_CANDIDATE"
    elif r == unknown:
        status = "UNKNOWN_PARENT225_DIRECT_PICARD64_EXACT"
    else:
        status = "UNSAT_PARENT225_DIRECT_PICARD64_EXACT"

    body = {
        "schema": "STAGE32_32_01_178_N371_BLOCK1134_PARENT225_DIRECT_PICARD64_RESULT_V1",
        "status": status,
        "target": {"block_index": BLOCK, "survivor_offset": OFFSET, "parent_ordinal": PARENT_ORDINAL},
        "attempt": attempt,
        "witness": witness,
        "credit": {"main_pruning_credit":False,"full178_complete":False,"n350_registered":False,"effectivity_final":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"stage32_closed":False,"merge_authorized":False}
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status":status,"attempt":attempt,"terminal_identity":witness["terminal_identity"] if witness else None,"canonical":body["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
