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
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
HPERP = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"

N361_AUDITED_HEAD = "caf92557103de0bfce1faebb88062dd5e731a430"
N361_AUDIT_REVIEW = 5186044497
CUT196_COMPUTE_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_COMPOSITION_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
N357_COMPOSITION_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
MAIN_STATE_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_STATE_CANONICAL = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
STATE_BLOB = "f78bbc76acb2ecdaf055bb2f554734de86330056"
STATE_CANONICAL = "37c756c5f9cb5e928b6e4dbff581c576d8588cc3b03731a3f61ea51502e6b711"
HPERP_BLOB = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
TARGETS = [
    (1141, 0, 798),
    (1195, 1, 840),
    (1145, 30, 801),
    (1209, 18, 851),
    (1261, 25, 889),
    (1140, 290, 797),
    (1190, 242, 837),
]
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
ROW_ID = "g1-d008"
D = 8
E = 8
BLOCK_WIDTH = 113
NORMAL_COUNT = 92
NORMAL_MASS = 112


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


def base_preflight(cut_root: Path, comp_root: Path):
    req(exact_head(cut_root) == CUT196_COMPUTE_HEAD, "CUT196 compute head drift")
    req(exact_head(comp_root) == N357_COMPOSITION_HEAD, "N357 composition head drift")
    subprocess.run(["git", "merge-base", "--is-ancestor", N361_AUDITED_HEAD, "HEAD"], cwd=ROOT, check=True)

    req(git_blob(STATE) == STATE_BLOB, "N362 state blob drift")
    state = json.loads(STATE.read_text())
    req(state["canonical_sha256_without_this_field"] == STATE_CANONICAL, "N362 state stored canonical drift")
    req(canonical(state) == STATE_CANONICAL, "N362 state canonical drift")
    req(state["parent"]["n361_hostile_audit_review_id"] == N361_AUDIT_REVIEW, "N361 audit review drift")

    req(git_blob(MAIN_STATE) == MAIN_STATE_BLOB, "MAIN V15 state blob drift")
    main = json.loads(MAIN_STATE.read_text())
    req(main["canonical_sha256_without_this_field"] == MAIN_STATE_CANONICAL, "MAIN V15 stored canonical drift")
    req(canonical(main) == MAIN_STATE_CANONICAL, "MAIN V15 canonical drift")
    f = main["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN V15 strata drift")
    req(f["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN V15 terminal drift")
    req(f["n357_main_pruning_credit"] is True, "N357 MAIN credit missing")
    req(f["cut191_main_pruning_credit"] is True, "CUT191 MAIN credit missing")
    req(f["cut194_main_pruning_credit"] is True, "CUT194 MAIN credit missing")
    req(f["cut195_main_pruning_credit"] is True, "CUT195 MAIN credit missing")
    req(f["cut193_main_pruning_credit"] is False, "CUT193 unexpectedly credited")
    req(f["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")

    comp_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(git_blob(comp_path) == N357_COMPOSITION_VERIFIER_BLOB, "N357 composition verifier blob drift")
    proc = subprocess.run([sys.executable, str(comp_path)], cwd=comp_root, text=True, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise RuntimeError("audited N357 composition replay failed")
    req("PASS_N357_CURRENT_V13_AUTHORITY_COMPOSITION_REPLAY" in proc.stdout, "N357 composition replay verdict missing")

    cut196_path = cut_root / "stages/stage32/full178-cut/cut196_e8_common_adapter_wave4.py"
    cut196 = load_module(cut196_path, "n362_cut196")
    cut196.preflight()
    comp = load_module(comp_path, "n362_n357comp")
    return state, main, cut196, comp


def exact_solver_for_parent(core, P: Matrix, blocks, g, block_index: int, parent: dict, timeout_ms: int):
    c = [Int(f"c_{block_index}_{j}") for j in range(64)]
    y = [Sum([int(P[i, j]) * c[j] for j in range(64)]) for i in range(140)]
    s = SolverFor("QF_LIA")
    s.set(timeout=timeout_ms)

    for i in range(NORMAL_COUNT):
        s.add(y[i] >= 0, y[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT, 140):
        s.add(y[i] >= 0, y[i] <= E)
    s.add(Sum(y[:NORMAL_COUNT]) == NORMAL_MASS)
    s.add(Sum(y[NORMAL_COUNT:]) == E)

    fibre = []
    for pack, factor_blocks in zip(core.PACKS, blocks):
        vals = [2 * y[b - 1] + Sum([y[j - 1] for j in block]) for b, block in zip(pack, factor_blocks)]
        for v in vals[1:]:
            s.add(v == vals[0])
        fibre.append(vals[0])
    n1, n2 = fibre
    s.add(n1 + n2 == D, n1 >= 0, n1 <= D, n2 >= 0, n2 <= D)
    for label in range(93, 141):
        s.add(y[label - 1] <= D // 2)
    for b1 in blocks[0]:
        a = Sum([y[j - 1] for j in b1])
        for b2 in blocks[1]:
            s.add(a + Sum([y[j - 1] for j in b2]) <= D)

    fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, parent["selected_exceptional_pairings"])}
    for label, value in fixed.items():
        s.add(y[label - 1] == value)
    allowed = [int(v) for v in parent["x4_allowed_residues_mod8"]]
    req(allowed, "parent has empty x4 residue set")
    s.add(Or(*[(y[48] % 8) == r for r in allowed]))
    return s, c, y, fixed, allowed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    cut_root = args.cut196_root.resolve()
    comp_root = args.n357_composition_root.resolve()

    state, main_state, cut196, comp = base_preflight(cut_root, comp_root)
    core = cut196.core
    P, blocks, g = core.load_picard_interface()
    idx = core.e8.indexer()
    survivors = core.e8.current_main_survivor_block_indices()
    req(len(survivors) == 7596, "e8 current-prefix survivor count drift")

    hperp = load_module(HPERP, "n362_hperp")
    req(git_blob(HPERP) == HPERP_BLOB, "current Hperp adapter blob drift")
    bundle = core.e8.d18.load_retained(core.e8.d18.RETAINED, "n362_bundle")
    marking = core.e8.d18.load_retained(core.e8.d18.MARKING, "n362_marking")
    G = Matrix(bundle["picard_gram_64x64"])
    _, known_degree, _, _, hmeta = hperp._parse_hperp(marking["hperp_text"])
    basis_labels = [int(v) for v in hperp.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    degree_coeffs = [int(known_degree[v - 1]) for v in basis_labels]

    attempts = []
    witness = None
    timeout_ms = int(state["probe"]["per_exact_solve_timeout_ms"])
    for block_index, parent_ordinal, expected_offset in TARGETS:
        actual_offset = survivors.index(block_index)
        req(actual_offset == expected_offset, f"block {block_index} survivor offset drift")
        req(actual_offset > 765, f"block {block_index} overlaps consumed CUT191/CUT194/CUT195 target offsets")
        sig = core.e8.block_signature(block_index, idx)
        req(sig["current_main_audited_prefix_survivor"] is True, f"block {block_index} lost N220/N355 prefix survival")
        base = tuple(int(v) for v in idx.unrank(block_index * BLOCK_WIDTH))
        req(comp.prefix_survives(base), f"block {block_index} prefix replay failed")
        req(comp.n357_accepts(base), f"block {block_index} rejected by consumed N357")
        sums = [int(v) for v in sig["n355_known_group_sums"]]
        req(sums[1] - sums[2] <= 3 * D - E, f"block {block_index} rejected by consumed N356")

        parents = list(core.e8.iter_parent_population(block_index, g))
        req(0 <= parent_ordinal < len(parents), f"parent ordinal outside population for block {block_index}")
        parent = parents[parent_ordinal]
        s, cvars, yexpr, fixed, allowed = exact_solver_for_parent(core, P, blocks, g, block_index, parent, timeout_ms)
        r = s.check()
        attempt = {
            "block_index": block_index,
            "survivor_offset": actual_offset,
            "terminal_rank_range": sig["terminal_rank_range"],
            "parent_ordinal": parent_ordinal,
            "parent_population_count": len(parents),
            "selected_exceptional_pairings_sha256": csha(parent["selected_exceptional_pairings"]),
            "x4_allowed_residues_mod8": allowed,
            "exact_result": str(r),
        }
        if r == unknown:
            attempt["reason_unknown"] = s.reason_unknown()
        attempts.append(attempt)
        if r != sat:
            continue

        m = s.model()
        coords = [int(m.eval(v, model_completion=True).as_long()) for v in cvars]
        pairings = [int(m.eval(v, model_completion=True).as_long()) for v in yexpr]
        x4 = pairings[48]
        req(0 <= x4 <= NORMAL_MASS, "SAT x4 outside canonical block width")
        terminal = [pairings[label - 1] for label in ASSIGNMENT_ORDER]
        rank = int(idx.rank(tuple(terminal)))
        req(rank == block_index * BLOCK_WIDTH + x4, "canonical terminal rank mismatch")
        req(list(idx.unrank(rank)) == terminal, "canonical terminal rank roundtrip failed")
        req(comp.n357_accepts(tuple(int(v) for v in idx.unrank(block_index * BLOCK_WIDTH))), "N357 block-constant replay failed")

        cv = Matrix(coords)
        selected_labels = [int(v) for v in g.selected_labels]
        selected64 = [pairings[label - 1] for label in selected_labels]
        Psel = P.extract([label - 1 for label in selected_labels], list(range(64)))
        req([int(v) for v in (Psel * cv)] == selected64, "selected64 replay mismatch")
        req([int(v) for v in (P * cv)] == pairings, "all140 replay mismatch")
        degree = sum(degree_coeffs[j] * coords[j] for j in range(64))
        req(degree == D, f"degree replay mismatch: {degree}")
        self_square = int((cv.T * G * cv)[0])
        scale = 16 // math.gcd(D, 16)
        numerator = scale * scale * D * D - 16 * scale * scale * self_square
        req(numerator % 16 == 0, "Hperp scalar integrality failed")
        neg_hperp_n = numerator // 16

        psel_plain = [[int(Psel[i, j]) for j in range(64)] for i in range(64)]
        gram_plain = [[int(G[i, j]) for j in range(64)] for i in range(64)]
        witness = {
            "schema": "STAGE32_32_01_178_N362_CURRENT_V15_SELECTED64_WITNESS_V1",
            "row_id": ROW_ID,
            "g": 1,
            "d": D,
            "e": E,
            "block_index": block_index,
            "survivor_offset": actual_offset,
            "parent_ordinal": parent_ordinal,
            "terminal_rank": rank,
            "terminal_identity": f"{ROW_ID}|e={E}|rank={rank}",
            "compressed_terminal_pairings": terminal,
            "selected64_pairings": selected64,
            "picard64_coordinates": coords,
            "all140_pairings_sha256": csha(pairings),
            "selected_pairing_matrix_sha256": csha(psel_plain),
            "gram64_sha256": csha(gram_plain),
            "picard64_coordinates_sha256": csha(coords),
            "self_square": self_square,
            "negative_hperp_square_N": neg_hperp_n,
            "hperp_text_sha256": hmeta["hperp_text_sha256"],
            "current_v15_membership": {
                "n220_n355_prefix_survivor": True,
                "n356_accepts": True,
                "n357_accepts": True,
                "outside_consumed_cut_offset_prefix_0_765": True,
                "cut196_not_consumed_into_main": True,
            },
            "coverage_source": {
                "identity_contract": "N104_CANONICAL_INDEXED_TERMINAL_RANK",
                "current_v15_membership_replayed": True,
                "creates_full178_coverage": False,
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
                "merge_authorized": False,
            },
        }
        witness["canonical_sha256_without_this_field"] = csha(witness)
        break

    body = {
        "schema": "STAGE32_32_01_178_N362_CURRENT_V15_WITNESS_PROBE_RESULT_V1",
        "status": "SAT_CURRENT_V15_WITNESS_CANDIDATE" if witness else "NO_SAT_IN_SINGLE_PARENT_PROBE",
        "parent": {
            "n361_audited_exact_head": N361_AUDITED_HEAD,
            "n361_hostile_audit_review_id": N361_AUDIT_REVIEW,
            "main_v15_state_blob_sha1": MAIN_STATE_BLOB,
            "main_v15_state_canonical_sha256": MAIN_STATE_CANONICAL,
        },
        "external_replays": {
            "cut196_compute_head": CUT196_COMPUTE_HEAD,
            "n357_composition_audited_head": N357_COMPOSITION_HEAD,
            "cut196_is_route_selection_only_and_unconsumed": True,
        },
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
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": body["status"],
        "attempts": len(attempts),
        "witness_terminal_identity": witness["terminal_identity"] if witness else None,
        "self_square": witness["self_square"] if witness else None,
        "negative_hperp_square_N": witness["negative_hperp_square_N"] if witness else None,
        "canonical": body["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
