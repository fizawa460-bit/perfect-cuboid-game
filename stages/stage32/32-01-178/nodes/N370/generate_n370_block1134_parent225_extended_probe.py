#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
STATE = HERE / "STATE.json"
N369_RESULT = HERE.parent / "N369/RESULT.json"
N365_GENERATOR = HERE.parent / "N365/generate_n365_block1265_three_parent_probe.py"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"

CUT196_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
N357_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_CANON = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
STATE_BLOB = "0804fccbe3882a0753c4bd1b53a1492ea1f46c41"
STATE_CANON = "19ec1eaa9bc4bdf63702f7fa41251e561edd11b419de3cefbcbc40f6c82e2980"
N369_RESULT_BLOB = "31bc2959d91077cfd388f82b1c528050b770efe9"
N369_RESULT_CANON = "44f16998c7697d2817f6a42236e69c902d33b8db4d9dab5070e9b7576f3d6ed7"
N365_GENERATOR_BLOB = "9641ac7b75cf714dc660e5cb34105dd54918185f"
BLOCK, OFFSET, WIDTH = 1134, 793, 113
PARENT_ORDINAL = 225
EXPECTED_PARENT_COUNT = 1560


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
    n369 = checked(N369_RESULT, N369_RESULT_BLOB, N369_RESULT_CANON)
    main = checked(MAIN_STATE, MAIN_BLOB, MAIN_CANON)
    req(blob(N365_GENERATOR) == N365_GENERATOR_BLOB, "N365 exact solver generator drift")
    req(n369["status"] == "UNKNOWN_REMAINS_IN_INDEPENDENT_RESIDUAL_PROBE" and n369["witness"] is None, "N369 result drift")
    unknowns = [a for a in n369["attempts"] if a["exact_result"] == "unknown"]
    req(len(unknowns) == 1 and unknowns[0]["parent_ordinal"] == PARENT_ORDINAL and unknowns[0]["reason_unknown"] == "timeout", "N369 unique timeout drift")
    req(n369["target"]["block_index"] == BLOCK and PARENT_ORDINAL in n369["target"]["parent_ordinals"], "N369 target drift")
    req(state["target"]["parent_ordinal"] == PARENT_ORDINAL and state["method"]["per_parent_timeout_ms"] == 60000, "N370 state drift")
    f = main["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN V15 terminal drift")
    req(f["n357_main_pruning_credit"] is True and f["cut195_main_pruning_credit"] is True, "MAIN consumed authority drift")
    req(f["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")
    comp_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(comp_path) == N357_VERIFIER_BLOB, "N357 verifier drift")
    p = subprocess.run([sys.executable, str(comp_path)], cwd=comp_root, text=True, capture_output=True)
    req(p.returncode == 0 and "PASS_N357_CURRENT_V13_AUTHORITY_COMPOSITION_REPLAY" in p.stdout, "N357 replay failed")
    cut196 = load_module(cut_root / "stages/stage32/full178-cut/cut196_e8_common_adapter_wave4.py", "n370_cut196")
    cut196.preflight()
    comp = load_module(comp_path, "n370_n357comp")
    n365 = load_module(N365_GENERATOR, "n370_n365_solver")
    return state, cut196, comp, n365


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    state, cut196, comp, n365 = preflight(args.cut196_root.resolve(), args.n357_composition_root.resolve())
    core = cut196.core
    P, blocks, g = core.load_picard_interface()
    req(g.den == 8, "selected64 denominator drift")
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

    n365.BLOCK = BLOCK
    n365.OFFSET = OFFSET
    n365.EXPECTED_PARENT_COUNT = EXPECTED_PARENT_COUNT
    attempt, witness = n365.solve_parent(state, core, P, blocks, g, idx, PARENT_ORDINAL)
    if witness is not None:
        witness["schema"] = "STAGE32_32_01_178_N370_CURRENT_V15_SELECTED64_WITNESS_V1"
        witness["canonical_sha256_without_this_field"] = csha({k: v for k, v in witness.items() if k != "canonical_sha256_without_this_field"})
        status = "SAT_CURRENT_V15_WITNESS_CANDIDATE"
    elif attempt["exact_result"] == "unsat":
        status = "UNSAT_PARENT225_EXTENDED_EXACT"
    else:
        status = "UNKNOWN_PARENT225_EXTENDED_EXACT"

    body = {
        "schema": "STAGE32_32_01_178_N370_BLOCK1134_PARENT225_EXTENDED_EXACT_RESULT_V1",
        "status": status,
        "target": {"block_index": BLOCK, "survivor_offset": OFFSET, "parent_ordinal": PARENT_ORDINAL},
        "attempt": attempt,
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
    print(json.dumps({"status": status, "attempt": attempt, "terminal_identity": witness["terminal_identity"] if witness else None, "canonical": body["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
