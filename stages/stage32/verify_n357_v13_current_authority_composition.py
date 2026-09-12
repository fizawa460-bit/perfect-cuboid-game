#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"

INDEXER = RESIDUAL / "compressed_terminal_indexer.py"
FAMILY = RESIDUAL / "compressed_terminal_family.py"
N220 = ROOT / "stages/stage32/32-01-178/nodes/N220/STATE-AUDITED.json"
N355 = ROOT / "stages/stage32/32-01-178/nodes/N355/FULL-PREFIX-RESULT.json"
CUT191 = ROOT / "stages/stage32/full178-cut/CUT191-first-block-closure-checkpoint.json"
CUT194 = ROOT / "stages/stage32/full178-cut/CUT194-e8-common-adapter-wave2-result.json"
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
REPLAY = HERE / "management/N357-V13-CURRENT-AUTHORITY-COMPOSITION.json"

LOCKS = {
    INDEXER: "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    FAMILY: "90ff82ed312dcc0cb32cf207935945f550e29170",
    N220: "f5f0e902062c9fafc9f03fe8a203d744cf58281e",
    N355: "0f30517cc5007ea435f4183201fc6cad699dd635",
    CUT191: "a90042ec931cb487ae6be852524db5a4537862f4",
    CUT194: "dab1a28f55918b617112799f11ac9614eb8a481c",
}
N355_CANONICAL = "7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775"
CUT191_CANONICAL = "1e681c456dc30342346d134f5e0d89150573f8a756cbd808c309d2af89821fdd"
CUT194_CANONICAL = "c63f6da3dd0ec443572f8561bb7774491ce7d7c09ce319a322fb52e5b1e08cd4"
REPLAY_CANONICAL = "3a9d29b97ccc663a92cc4c0463d1e77c00a518450b65d8d9ece0054734eeebd8"

ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
X4_LABEL = 49
N355_GROUPS = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
G, D, E = 1, 8, 8
BLOCK_WIDTH = 113
CURRENT_BLOCK_COUNT = 7596
CURRENT_BLOCK_STREAM = "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3"
CURRENT_V13_TERMINALS = 65396964990500233609659
N357_REJECT = 17797986705435299826016
POST_COMPOSITION = 47598978285064933783643


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")


def prefix_survives(base: tuple[int, ...]) -> bool:
    by = {label: int(value) for label, value in zip(ASSIGNMENT_ORDER, base)}
    fixed = {label: value for label, value in by.items() if label != X4_LABEL}
    mass = sum(fixed.values())
    support = sum(1 for value in fixed.values() if value > 0)
    k = math.ceil((D - 16 * G + 16) / 4)
    n220 = support + min(38, E - mass) >= k
    group_sums = [sum(fixed[label] for label in group) for group in N355_GROUPS]
    n355 = max(group_sums) <= D // 2
    return n220 and n355


def support_suffix_capacity(x: tuple[int, ...]) -> int:
    a = x[2] + x[3] + x[7]
    b = x[1] + x[5] + x[9]
    c = x[0] + x[6] + x[8] + x[10]
    h = D // 2
    s0 = min(16, D)
    sa = min(13, D - a, D - 2 * a + 4, h + 5)
    s3 = min(9, D - b - c, D - 2 * b, D - 2 * c + 1)
    return s0 + sa + s3


def n357_accepts(base: tuple[int, ...]) -> bool:
    mass = sum(base[i] for i in range(11) if i != 4)
    support = sum(1 for i in range(11) if i != 4 and base[i] > 0)
    k = math.ceil((D - 16 * G + 16) / 4)
    srem = support_suffix_capacity(base)
    return support + min(E - mass, srem) >= k


def main() -> None:
    # Fail closed before importing the runtime indexer.
    for path, expected in LOCKS.items():
        req(path.is_file(), f"missing source {path}")
        req(git_blob(path) == expected, f"source-lock drift {path}")

    n355 = load(N355)
    req(n355.get("canonical_sha256_without_this_field") == N355_CANONICAL, "N355 stored canonical drift")
    req(canonical(n355) == N355_CANONICAL, "N355 canonical drift")
    cut191 = load(CUT191)
    req(cut191.get("canonical_sha256_without_this_field") == CUT191_CANONICAL, "CUT191 stored canonical drift")
    req(canonical(cut191) == CUT191_CANONICAL, "CUT191 canonical drift")
    cut194 = load(CUT194)
    req(cut194.get("canonical_sha256_without_this_field") == CUT194_CANONICAL, "CUT194 stored canonical drift")
    req(canonical(cut194) == CUT194_CANONICAL, "CUT194 canonical drift")
    replay = load(REPLAY)
    req(replay.get("canonical_sha256_without_this_field") == REPLAY_CANONICAL, "composition stored canonical drift")
    req(canonical(replay) == REPLAY_CANONICAL, "composition canonical drift")

    aud = replay["audited_n357_candidate"]
    req(aud["pr"] == 1782 and aud["hostile_audit_status"] == "PASS", "N357 audit status drift")
    req(aud["audited_exact_head"] == "0d787839b7e0dad4a42108c61d16e7849c50862f", "N357 audited head drift")
    req(aud["hostile_audit_review_id"] == 5183069892, "N357 review drift")
    req(aud["result_blob_sha1"] == "50014d453266ad79101910a943d14388bd3ef6ec", "N357 result blob drift")
    req(aud["result_canonical_sha256"] == "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53", "N357 result canonical drift")
    req(aud["engine_blob_sha1"] == "479c783cb42d0952cc310708106787147b499240", "N357 engine blob drift")
    req(aud["necessary_condition"] == "s + min(e-M,Srem) >= K", "N357 predicate drift")
    req(aud["candidate_incremental_rejected_terminals"] == N357_REJECT, "N357 candidate count drift")
    req(aud["main_pruning_credit"] is False, "N357 external audit self-granted MAIN credit")

    sys.path.insert(0, str(RESIDUAL))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(E, D)
    req(idx.normal_budget + 1 == BLOCK_WIDTH, "e8 block width drift")
    survivors = []
    stream = hashlib.sha256()
    for block_index in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block_index * BLOCK_WIDTH))
        req(base[4] == 0, "block base x4 drift")
        if prefix_survives(base):
            survivors.append(block_index)
            stream.update(f"{block_index}\n".encode())
    req(len(survivors) == CURRENT_BLOCK_COUNT, "current prefix survivor block count drift")
    req(stream.hexdigest() == CURRENT_BLOCK_STREAM, "current prefix survivor stream drift")

    req(cut191["population_preimage"]["first_block_rank_range"] == [0, 112], "CUT191 rank range drift")
    cut191_blocks = [survivors[0]]
    req(cut191_blocks == [0], "CUT191 block identity drift")

    req(cut194["target"]["survivor_offset_range"] == [256, 510], "CUT194 offset range drift")
    req(cut194["target"]["block_indices"] == survivors[256:511], "CUT194 target block identity drift")
    closed = list(cut194["result"]["candidate_closed_block_indices"])
    req(len(closed) == 234 and cut194["result"]["candidate_pruned_terminals"] == 26442, "CUT194 closed count drift")
    req(set(closed).issubset(set(cut194["target"]["block_indices"])), "CUT194 closed block outside target")

    cut191_reject = [b for b in cut191_blocks if not n357_accepts(tuple(int(v) for v in idx.unrank(b * BLOCK_WIDTH)))]
    cut194_reject = [b for b in closed if not n357_accepts(tuple(int(v) for v in idx.unrank(b * BLOCK_WIDTH)))]
    req(cut191_reject == [], f"N357 overlaps CUT191 blocks: {cut191_reject}")
    req(cut194_reject == [], f"N357 overlaps CUT194 blocks: {cut194_reject}")

    comp = replay["e8_overlap_replay"]
    req(comp["n357_rejecting_cut191_terminal_count"] == 0, "recorded CUT191 overlap drift")
    req(comp["n357_rejecting_cut194_terminal_count"] == 0, "recorded CUT194 overlap drift")
    req(comp["n357_overlap_with_current_consumed_terminals"] == 0, "recorded total overlap drift")
    req(comp["composition_incremental_rejected_terminals"] == N357_REJECT, "composition incremental count drift")
    req(CURRENT_V13_TERMINALS - N357_REJECT == POST_COMPOSITION, "composition arithmetic drift")
    req(comp["candidate_remaining_terminals_if_later_consumed"] == POST_COMPOSITION, "recorded post-composition drift")

    state = load(STATE)
    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_terminals"] == CURRENT_V13_TERMINALS, "live V13 authority drift")
    req(frontier["n357_main_pruning_credit"] is False, "N357 MAIN credit granted before consumption audit")
    req(frontier["n357_status"] == "AUDITED_CANDIDATE_CURRENT_V13_COMPOSITION_REPLAYED_NO_MAIN_CREDIT", "live N357 status stale")
    req(state["current"]["next_exact_route"] == "N357_CURRENT_V13_COMPOSITION_EXTERNAL_AUDIT_THEN_MAIN_CONSUMPTION", "live N357 route stale")

    fw = replay["credit_firewall"]
    req(fw["n357_main_pruning_credit"] is False and fw["main_authority_mutated_by_this_replay"] is False, "composition replay granted credit")
    req(fw["separate_main_consumption_required"] is True, "separate MAIN consumption firewall lost")
    req(fw["merge_authorized"] is False, "merge authorized")

    print(json.dumps({
        "verdict": "PASS_N357_CURRENT_V13_AUTHORITY_COMPOSITION_REPLAY",
        "n357_audited_candidate_review": 5183069892,
        "cut191_overlap_terminals": 0,
        "cut194_overlap_terminals": 0,
        "n357_incremental_rejected_terminals_if_later_consumed": N357_REJECT,
        "candidate_remaining_terminals_if_later_consumed": POST_COMPOSITION,
        "n357_main_pruning_credit": False,
        "full178_complete": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
