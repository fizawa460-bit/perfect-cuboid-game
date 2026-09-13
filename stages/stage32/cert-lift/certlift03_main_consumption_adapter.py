#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
AUDIT_RECEIPT = HERE / "CERTLIFT-03-HOSTILE-AUDIT-PASS.json"

AUDITED_CERTLIFT_HEAD = "af41c95b9e952ed6cf913f2187a9d3acd94ddef3"
AUDITED_EVIDENCE_HEAD = "2ea8f9131de81529ad152665df8b637d72092421"
AUDITED_REVIEW_ID = 5188640528
AUDITED_LEMMA_BLOB = "af9f4501f911251d41b813770af6e41a706f2c95"
AUDITED_LEMMA_CANONICAL = "2d1fcfe51420ab01f81d353e0d19a2b1eef467a51e321da953b5cf18aa88e764"
AUDIT_RECEIPT_BLOB = "5a8083c6dfcf67b052966dbbfdf5c29c1767448f"
AUDIT_RECEIPT_CANONICAL = "edfd04fe9c3eb8a8a8b01fb246069924b6c6a8741ebc73ea081ad5578a84306c"

CURRENT_MAIN_HEAD = "4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c"
MAIN_STATE_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
MAIN_STATE_CANONICAL = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
N357_COMPOSITION_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
CUT191_BLOB = "a90042ec931cb487ae6be852524db5a4537862f4"
CUT191_CANONICAL = "1e681c456dc30342346d134f5e0d89150573f8a756cbd808c309d2af89821fdd"
CUT194_BLOB = "dab1a28f55918b617112799f11ac9614eb8a481c"
CUT194_CANONICAL = "c63f6da3dd0ec443572f8561bb7774491ce7d7c09ce319a322fb52e5b1e08cd4"
CUT195_BLOB = "d9fe913dccd41446780dbdde9f0200970ee9129e"
CUT195_CANONICAL = "1a7d802f427761d304ee06451d00ea67a1365d7d2629cdbf2ac88b6b4ff08aed"

EX5_SOURCE_HEAD = "fd00531181228c9f367a49eb61ddc3af6ab84ab3"
CURRENT_PREFIX_BLOCK_COUNT = 7596
CURRENT_PREFIX_STREAM = "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3"
BLOCK_WIDTH = 113
EXPECTED_SYMBOLIC_CURRENT_MAIN_TARGETS = 1677
MAIN_AUTHORITY_REMAINING = 47598978285064933757427
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
X4_LABEL = 49
G3 = [93, 94, 95, 96]


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def exact_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()


def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(isinstance(obj, dict), f"expected object: {path}")
    return obj


def checked_json(path: Path, blob: str, canonical: str) -> dict:
    req(path.is_file(), f"missing source: {path}")
    req(git_blob(path) == blob, f"blob drift: {path}")
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == canonical, f"stored canonical drift: {path}")
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    req(csha(body) == canonical, f"canonical replay drift: {path}")
    return obj


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def stream_sha(values: list[int]) -> str:
    h = hashlib.sha256()
    for value in values:
        h.update(f"{int(value)}\n".encode())
    return h.hexdigest()


def replay_audited_symbolic_lemma(audited_root: Path, ex5_root: Path) -> None:
    req(exact_head(audited_root) == AUDITED_CERTLIFT_HEAD, "audited CERTLIFT exact head drift")
    req(exact_head(ex5_root) == EX5_SOURCE_HEAD, "EX5 source exact head drift")
    lemma = audited_root / "stages/stage32/cert-lift/g3_mass7_symbolic_parity_lemma.py"
    req(git_blob(lemma) == AUDITED_LEMMA_BLOB, "audited symbolic lemma blob drift")
    env = dict(os.environ)
    env["PYTHONPATH"] = str(ex5_root / "stages/stage32-ex5/cut-handoff")
    proc = subprocess.run([sys.executable, str(lemma)], cwd=audited_root, env=env, text=True, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise RuntimeError("audited symbolic lemma replay failed")
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    req(lines, "audited symbolic lemma produced no output")
    out = json.loads(lines[-1])
    req(out.get("status") == "PASS_SYMBOLIC_MASS7_G3_FIBRE_PARITY_LEMMA_D8_E8", "symbolic lemma verdict drift")
    req(out.get("canonical") == AUDITED_LEMMA_CANONICAL, "symbolic lemma canonical drift")


def run() -> dict:
    main_root = Path(os.environ.get("CERTLIFT_CURRENT_MAIN_ROOT", "")).resolve()
    audited_root = Path(os.environ.get("CERTLIFT_AUDITED_ROOT", "")).resolve()
    ex5_root = Path(os.environ.get("CERTLIFT_EX5_SOURCE_ROOT", "")).resolve()
    req(str(main_root) != "." and main_root.is_dir(), "CERTLIFT_CURRENT_MAIN_ROOT missing")
    req(str(audited_root) != "." and audited_root.is_dir(), "CERTLIFT_AUDITED_ROOT missing")
    req(str(ex5_root) != "." and ex5_root.is_dir(), "CERTLIFT_EX5_SOURCE_ROOT missing")
    req(exact_head(main_root) == CURRENT_MAIN_HEAD, "current MAIN exact head drift")

    audit = checked_json(AUDIT_RECEIPT, AUDIT_RECEIPT_BLOB, AUDIT_RECEIPT_CANONICAL)
    req(audit["status"] == "HOSTILE_AUDIT_PASS", "CERTLIFT hostile audit status drift")
    req(audit["review_id"] == AUDITED_REVIEW_ID, "CERTLIFT hostile audit review drift")
    req(audit["reviewed_pr_head"] == AUDITED_CERTLIFT_HEAD, "CERTLIFT reviewed head drift")
    req(audit["mathematical_evidence_exact_head"] == AUDITED_EVIDENCE_HEAD, "CERTLIFT evidence head drift")
    replay_audited_symbolic_lemma(audited_root, ex5_root)

    state_path = main_root / "stages/stage32/MAIN-STATE.json"
    state = checked_json(state_path, MAIN_STATE_BLOB, MAIN_STATE_CANONICAL)
    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_terminals"] == MAIN_AUTHORITY_REMAINING, "MAIN terminal authority drift")
    req(frontier["cut191_main_pruning_credit"] is True, "CUT191 credit drift")
    req(frontier["cut194_main_pruning_credit"] is True, "CUT194 credit drift")
    req(frontier["cut195_main_pruning_credit"] is True, "CUT195 credit drift")
    req(frontier["n357_main_pruning_credit"] is True, "N357 credit drift")
    req(frontier["cut193_main_pruning_credit"] is False, "CUT193 unexpectedly consumed")

    n357_path = main_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(git_blob(n357_path) == N357_COMPOSITION_VERIFIER_BLOB, "N357 composition verifier blob drift")
    n357 = load_module(n357_path, "s32_certlift03_n357")

    cut191 = checked_json(
        main_root / "stages/stage32/full178-cut/CUT191-first-block-closure-checkpoint.json",
        CUT191_BLOB, CUT191_CANONICAL,
    )
    cut194 = checked_json(
        main_root / "stages/stage32/full178-cut/CUT194-e8-common-adapter-wave2-result.json",
        CUT194_BLOB, CUT194_CANONICAL,
    )
    cut195 = checked_json(
        main_root / "stages/stage32/full178-cut/CUT195-e8-common-adapter-wave3-result.json",
        CUT195_BLOB, CUT195_CANONICAL,
    )

    residual = main_root / "stages/stage32/residual-32-01-production"
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == BLOCK_WIDTH, "e8 block width drift")
    survivors: list[int] = []
    for block_index in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block_index * BLOCK_WIDTH))
        req(base[4] == 0, "block base x4 drift")
        if n357.prefix_survives(base):
            survivors.append(block_index)
    req(len(survivors) == CURRENT_PREFIX_BLOCK_COUNT, "current prefix block-count drift")
    req(stream_sha(survivors) == CURRENT_PREFIX_STREAM, "current prefix block-stream drift")

    target: list[int] = []
    n357_rejected: list[int] = []
    for block_index in survivors:
        base = tuple(int(v) for v in idx.unrank(block_index * BLOCK_WIDTH))
        by = {label: int(value) for label, value in zip(ASSIGNMENT_ORDER, base)}
        fixed_mass = sum(value for label, value in by.items() if label != X4_LABEL)
        g3 = sum(by[label] for label in G3)
        if fixed_mass < 7 or g3 != 3:
            continue
        target.append(block_index)
        if not n357.n357_accepts(base):
            n357_rejected.append(block_index)
    req(len(target) == EXPECTED_SYMBOLIC_CURRENT_MAIN_TARGETS, "symbolic current-MAIN target count drift")

    req(cut191["population_preimage"]["first_block_rank_range"] == [0, 112], "CUT191 identity drift")
    cut191_consumed = {int(survivors[0])}
    req(cut191_consumed == {0}, "CUT191 block identity drift")
    cut194_consumed = {int(v) for v in cut194["result"]["candidate_closed_block_indices"]}
    cut195_consumed = {int(v) for v in cut195["result"]["candidate_closed_block_indices"]}
    req(len(cut194_consumed) == 234, "CUT194 consumed block count drift")
    req(len(cut195_consumed) == 232, "CUT195 consumed block count drift")
    req(not (cut191_consumed & cut194_consumed), "CUT191/CUT194 overlap drift")
    req(not (cut191_consumed & cut195_consumed), "CUT191/CUT195 overlap drift")
    req(not (cut194_consumed & cut195_consumed), "CUT194/CUT195 overlap drift")

    target_set = set(target)
    n357_set = set(n357_rejected)
    overlaps = {
        "n357": sorted(target_set & n357_set),
        "cut191": sorted(target_set & cut191_consumed),
        "cut194": sorted(target_set & cut194_consumed),
        "cut195": sorted(target_set & cut195_consumed),
    }
    already_consumed = n357_set | cut191_consumed | cut194_consumed | cut195_consumed
    incremental = sorted(target_set - already_consumed)
    req(not (set(incremental) & already_consumed), "incremental set double-charges prior MAIN authority")
    req(len(incremental) + len(target_set & already_consumed) == len(target), "target partition accounting drift")

    incremental_terminals = len(incremental) * BLOCK_WIDTH
    candidate_remaining = MAIN_AUTHORITY_REMAINING - incremental_terminals
    req(incremental_terminals >= 0 and candidate_remaining >= 0, "candidate terminal arithmetic invalid")

    out = {
        "schema": "STAGE32_CERTLIFT_03_MAIN_CONSUMPTION_ADAPTER_V1",
        "stage": "32",
        "node": "CERTLIFT-03-CONSUME",
        "status": "PASS_EXACT_CURRENT_MAIN_CONSUMPTION_ADAPTER_CANDIDATE",
        "source_locks": {
            "certlift_hostile_audit_review_id": AUDITED_REVIEW_ID,
            "certlift_reviewed_head": AUDITED_CERTLIFT_HEAD,
            "certlift_evidence_head": AUDITED_EVIDENCE_HEAD,
            "current_main_exact_head": CURRENT_MAIN_HEAD,
            "current_main_state_blob_sha1": MAIN_STATE_BLOB,
            "current_main_state_canonical_sha256": MAIN_STATE_CANONICAL,
            "ex5_source_exact_head": EX5_SOURCE_HEAD,
        },
        "predicate": {
            "d": 8,
            "e": 8,
            "fixed_exceptional_mass_lower_bound": 7,
            "g3_labels": G3,
            "g3_sum": 3,
        },
        "population": {
            "current_prefix_blocks": len(survivors),
            "current_prefix_block_stream_sha256": stream_sha(survivors),
            "symbolic_target_blocks_before_prior_consumption": len(target),
            "symbolic_target_block_stream_sha256": stream_sha(target),
            "block_width_terminals": BLOCK_WIDTH,
        },
        "prior_authority_overlap": {
            "n357_blocks": len(overlaps["n357"]),
            "cut191_blocks": len(overlaps["cut191"]),
            "cut194_blocks": len(overlaps["cut194"]),
            "cut195_blocks": len(overlaps["cut195"]),
            "union_blocks": len(target_set & already_consumed),
            "double_charge": False,
        },
        "candidate_increment": {
            "incremental_blocks": len(incremental),
            "incremental_terminals": incremental_terminals,
            "incremental_block_stream_sha256": stream_sha(incremental),
            "authoritative_remaining_terminals_before": MAIN_AUTHORITY_REMAINING,
            "candidate_remaining_terminals_if_later_consumed": candidate_remaining,
            "first_incremental_blocks": incremental[:32],
        },
        "firewall": {
            "adapter_is_main_consumption": False,
            "main_authority_mutated": False,
            "main_pruning_credit": False,
            "hostile_audit_of_adapter_required": True,
            "current_v15_replacement_head_hostile_reaudit_still_required": bool(frontier["cut195_post_sync_reaudit_required"]),
            "full178_complete": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()
    out = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    if args.self_check:
        print(json.dumps({
            "status": out["status"],
            "target_blocks": out["population"]["symbolic_target_blocks_before_prior_consumption"],
            "prior_overlap": out["prior_authority_overlap"],
            "incremental_blocks": out["candidate_increment"]["incremental_blocks"],
            "incremental_terminals": out["candidate_increment"]["incremental_terminals"],
            "candidate_remaining": out["candidate_increment"]["candidate_remaining_terminals_if_later_consumed"],
            "canonical": out["canonical_sha256_without_this_field"],
        }, sort_keys=True))
    elif not args.output:
        print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
