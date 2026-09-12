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
N367_RESULT = HERE.parent / "N367/RESULT.json"
N365_GENERATOR = HERE.parent / "N365/generate_n365_block1265_three_parent_probe.py"
MAIN_STATE = ROOT / "stages/stage32/MAIN-STATE.json"

CUT196_HEAD = "5403328470df32c65aea9a38efe3916cb87d24a4"
N357_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
N357_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_CANON = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
STATE_BLOB = "1e269473502fd5d6bfb51fd142308faa83c1c340"
STATE_CANON = "060b6c862a39f1ff4193c1bf3d1a7b3d9c1efd1acab0d83c866b5b4253f3079d"
N367_RESULT_BLOB = "45be220b83b93e04e10f335b2fe50df300626d85"
N367_RESULT_CANON = "4aa929b1c67165b38dabf36958512cbfc71fa8bd6af033174b7933b9f4480054"
N365_GENERATOR_BLOB = "9641ac7b75cf714dc660e5cb34105dd54918185f"
BLOCK, OFFSET, WIDTH = 1260, 888, 113
EXPECTED_PARENT_COUNT = 1286
SOURCE_RESIDUAL_COUNT = 11
SOURCE_RESIDUAL_STREAM = "118b353dcd113be3f2d194a1e51765bdb712e3106356f3fa491a7d26b3a796cb"


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


def stream_digest(values: list[int]) -> str:
    return hashlib.sha256("".join(f"{v}\n" for v in values).encode()).hexdigest()


def preflight(cut_root: Path, comp_root: Path):
    req(exact_head(cut_root) == CUT196_HEAD, "CUT196 head drift")
    req(exact_head(comp_root) == N357_HEAD, "N357 composition head drift")
    state = checked(STATE, STATE_BLOB, STATE_CANON)
    n367 = checked(N367_RESULT, N367_RESULT_BLOB, N367_RESULT_CANON)
    main = checked(MAIN_STATE, MAIN_BLOB, MAIN_CANON)
    req(blob(N365_GENERATOR) == N365_GENERATOR_BLOB, "N365 exact solver generator drift")
    req(n367["status"] == "NO_SAT_IN_INDEPENDENT_RESIDUAL_PROBE" and n367["witness"] is None, "N367 result drift")
    req(n367["target"]["block_index"] == 1155, "N367 target drift")
    req(n367["route_replay"]["independent_replay_unresolved_count"] == 6, "N367 replay count drift")
    f = main["current_exact_frontier"]
    req(f["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN V15 terminal drift")
    req(f["n357_main_pruning_credit"] is True and f["cut195_main_pruning_credit"] is True, "MAIN consumed authority drift")
    req(f["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")
    req(state["selection_provenance"]["cut196_source_residual_parent_count"] == SOURCE_RESIDUAL_COUNT, "N368 source residual count drift")
    req(state["selection_provenance"]["cut196_source_residual_parent_ordinal_sha256"] == SOURCE_RESIDUAL_STREAM, "N368 source residual digest drift")

    comp_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(blob(comp_path) == N357_VERIFIER_BLOB, "N357 verifier drift")
    p = subprocess.run([sys.executable, str(comp_path)], cwd=comp_root, text=True, capture_output=True)
    req(p.returncode == 0 and "PASS_N357_CURRENT_V13_AUTHORITY_COMPOSITION_REPLAY" in p.stdout, "N357 replay failed")
    cut196 = load_module(cut_root / "stages/stage32/full178-cut/cut196_e8_common_adapter_wave4.py", "n368_cut196")
    cut196.preflight()
    comp = load_module(comp_path, "n368_n357comp")
    n365 = load_module(N365_GENERATOR, "n368_n365_solver")
    return state, cut196, comp, n365


def independent_unresolved(state: dict, core, P, blocks, g) -> list[int]:
    parents = list(core.e8.iter_parent_population(BLOCK, g))
    req(len(parents) == EXPECTED_PARENT_COUNT, "block1260 parent population drift")
    unresolved = set(range(len(parents)))
    for prime in core.DEFAULT_PRIMES:
        s, y, _ = core.make_solver(P, blocks, prime, 750)
        for ordinal in list(unresolved):
            parent = parents[ordinal]
            fixed = {int(label): int(value) for label, value in zip(g.exceptional_labels, parent["selected_exceptional_pairings"])}
            result, _reason = core.check_with_fixed(s, y, fixed)
            if result == "unsat":
                unresolved.remove(ordinal)
    out = sorted(unresolved)
    gate = int(state["method"]["independent_unresolved_parent_gate_max"])
    req(1 <= len(out) <= gate, f"independent unresolved set outside bounded gate: {len(out)}>{gate}")
    return out


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
    req(survivors[OFFSET] == BLOCK and OFFSET > 765, "block1260 survivor offset drift")
    sig = core.e8.block_signature(BLOCK, idx)
    base = tuple(int(v) for v in idx.unrank(BLOCK * WIDTH))
    req(sig["current_main_audited_prefix_survivor"] is True, "prefix survival drift")
    req(comp.prefix_survives(base) and comp.n357_accepts(base), "prefix/N357 replay failed")
    sums = [int(v) for v in sig["n355_known_group_sums"]]
    req(sums[1] - sums[2] <= 16, "N356 replay failed")

    ordinals = independent_unresolved(state, core, P, blocks, g)
    replay_digest = stream_digest(ordinals)
    replay = {
        "source_cut196_residual_count": SOURCE_RESIDUAL_COUNT,
        "source_cut196_residual_parent_ordinal_sha256": SOURCE_RESIDUAL_STREAM,
        "independent_replay_unresolved_count": len(ordinals),
        "independent_replay_unresolved_ordinals": ordinals,
        "independent_replay_unresolved_sha256": replay_digest,
        "source_digest_reproduced_exactly": replay_digest == SOURCE_RESIDUAL_STREAM,
        "semantics": "CUT196 source residuals are route-selection only; every parent proved finite-ring UNSAT in this exact-head replay is safely excluded by a necessary condition, and every unresolved parent is sent to exact selected64 solve"
    }

    n365.BLOCK = BLOCK
    n365.OFFSET = OFFSET
    n365.EXPECTED_PARENT_COUNT = EXPECTED_PARENT_COUNT
    attempts = []
    witness = None
    for ordinal in ordinals:
        attempt, candidate = n365.solve_parent(state, core, P, blocks, g, idx, ordinal)
        attempts.append(attempt)
        if candidate is not None:
            candidate["schema"] = "STAGE32_32_01_178_N368_CURRENT_V15_SELECTED64_WITNESS_V1"
            candidate["canonical_sha256_without_this_field"] = csha({k: v for k, v in candidate.items() if k != "canonical_sha256_without_this_field"})
            witness = candidate
            break

    if witness is not None:
        status = "SAT_CURRENT_V15_WITNESS_CANDIDATE"
    elif any(a["exact_result"] == "unknown" for a in attempts):
        status = "UNKNOWN_REMAINS_IN_INDEPENDENT_RESIDUAL_PROBE"
    else:
        status = "NO_SAT_IN_INDEPENDENT_RESIDUAL_PROBE"

    body = {
        "schema": "STAGE32_32_01_178_N368_BLOCK1260_INDEPENDENT_FINITE_RING_RESIDUAL_WITNESS_RESULT_V1",
        "status": status,
        "target": {"block_index": BLOCK, "survivor_offset": OFFSET, "parent_ordinals": ordinals},
        "route_replay": replay,
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
        "independent_unresolved_count": len(ordinals),
        "parent_ordinals": ordinals,
        "source_digest_reproduced_exactly": replay["source_digest_reproduced_exactly"],
        "attempts": attempts,
        "terminal_identity": witness["terminal_identity"] if witness else None,
        "canonical": body["canonical_sha256_without_this_field"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
