#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
STATE = HERE / "STATE.json"
HANDOFF = HERE / "AUDIT-HANDOFF.json"

EXPECTED_MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
EXPECTED_MAIN_CANONICAL = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
EXPECTED_MAIN_HEAD = "fdc372e1666e1176d80953b6303b13b240da84c5"
EXPECTED_MAIN_REAUDIT_REVIEW = 5185987769
EXPECTED_AUTHORITY = (17128, 47598978285064933757427)

EXPECTED_STATE_BLOB = "64c51ba83a234a91bf056915a96fa9a02f68593a"
EXPECTED_STATE_CANONICAL = "e3cb52e0a7bcb35d7d370e7356f036b694c08aebc17829efa380580da2bf3e6b"
EXPECTED_HANDOFF_BLOB = "a0effd04e97828a632c202c92cf4b263eacce54d"
EXPECTED_HANDOFF_CANONICAL = "698a16da0074c9f29967de6107ef170b23c20c64e9462cba15c06a70af7e25f9"

HISTORICAL_FILES = {
    HERE / "GENERATE_SAMPLE_CONTRACT.md": "f9f5229d19e08bb71d923abc7084f0c2a2384124",
    HERE / "RESULT.json": "31ddd705d9d5e163ce58f0a07817ed7012831680",
    HERE / "RETAINED_SAMPLE_CONTRACT.md": "1890830be86d19edbe81990e5633130d0ab7188d",
    HERE / "generate_n361_sample_sidecar.py": "ac157fd14c2f623c27d9d60b935d4715d7367a35",
    HERE / "verify_n361_retained_sample_sidecar.py": "98aa9173d8323ff98b26a81e127cda868c39428f",
}

DEPENDENCY_FILES = {
    ROOT / "stages/stage32/32-01-178/nodes/N342/RESULT.json": "c44a5345e5f88f914023369323fb067ff964a18d",
    ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py": "90ff82ed312dcc0cb32cf207935945f550e29170",
    ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    ROOT / "stages/stage33/33-07/picard_base_rows_retained.py": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
}


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise AssertionError(path)
    return obj


def assert_blob_set(mapping: dict[Path, str]) -> None:
    for path, expected in mapping.items():
        actual = git_blob(path)
        if actual != expected:
            raise AssertionError(f"blob drift {path}: {actual} != {expected}")


def main() -> None:
    assert git_blob(MAIN) == EXPECTED_MAIN_BLOB
    main_state = load(MAIN)
    assert canonical(main_state) == EXPECTED_MAIN_CANONICAL
    assert main_state["canonical_sha256_without_this_field"] == EXPECTED_MAIN_CANONICAL
    assert main_state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED"
    frontier = main_state["current_exact_frontier"]
    assert (frontier["authoritative_remaining_strata"], frontier["authoritative_remaining_terminals"]) == EXPECTED_AUTHORITY
    assert frontier["cut195_main_pruning_credit"] is True
    assert frontier["n357_main_pruning_credit"] is True
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False

    assert git_blob(STATE) == EXPECTED_STATE_BLOB
    state = load(STATE)
    assert canonical(state) == EXPECTED_STATE_CANONICAL
    assert state["canonical_sha256_without_this_field"] == EXPECTED_STATE_CANONICAL
    parent = state["current_main_parent"]
    assert parent["exact_head"] == EXPECTED_MAIN_HEAD
    assert parent["external_hostile_reaudit_status"] == "PASS"
    assert parent["external_hostile_reaudit_review_id"] == EXPECTED_MAIN_REAUDIT_REVIEW
    assert parent["main_state_blob_sha1"] == EXPECTED_MAIN_BLOB
    assert parent["main_state_canonical_sha256"] == EXPECTED_MAIN_CANONICAL
    assert (parent["authoritative_remaining_strata"], parent["authoritative_remaining_terminals"]) == EXPECTED_AUTHORITY

    sample = state["retained_historical_sample"]
    assert sample["source_pr"] == 1782
    assert sample["source_head"] == "91a02613a17b9b6e743e3ae90bc1869acd3ffcbc"
    assert sample["terminal_identity"] == "g0-d176|e=48|rank=37830303724188"
    assert sample["historical_sample_only"] is True
    assert sample["current_v15_survivor_membership_claimed"] is False
    assert sample["self_square"] == -1784
    assert sample["negative_hperp_square_N"] == 3720

    assert git_blob(HANDOFF) == EXPECTED_HANDOFF_BLOB
    handoff = load(HANDOFF)
    assert canonical(handoff) == EXPECTED_HANDOFF_CANONICAL
    assert handoff["canonical_sha256_without_this_field"] == EXPECTED_HANDOFF_CANONICAL
    hp = handoff["current_main_parent"]
    assert hp["exact_head"] == EXPECTED_MAIN_HEAD
    assert hp["external_hostile_reaudit_review_id"] == EXPECTED_MAIN_REAUDIT_REVIEW
    assert hp["main_state_blob_sha1"] == EXPECTED_MAIN_BLOB
    assert hp["main_state_canonical_sha256"] == EXPECTED_MAIN_CANONICAL
    assert handoff["historical_sample_source"]["current_v15_survivor_membership_claimed"] is False
    assert handoff["next_gate"] == "stage32-01-178-audit"

    assert_blob_set(HISTORICAL_FILES)
    assert_blob_set(DEPENDENCY_FILES)

    for key, value in state["credit"].items():
        assert value is False, key

    replay = subprocess.run(
        [sys.executable, str(HERE / "verify_n361_retained_sample_sidecar.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    print(replay.stdout, end="")
    assert "PASS_N361_RETAINED_SELECTED64_SAMPLE_SIDECAR_REPLAY" in replay.stdout
    assert '"negative_hperp_square_N": 3720' in replay.stdout
    assert '"self_square": -1784' in replay.stdout

    print(json.dumps({
        "verdict": "PASS_N361_CURRENT_V15_REBASE_AUDIT_BOUNDARY",
        "current_main_exact_head": EXPECTED_MAIN_HEAD,
        "current_main_external_reaudit_review_id": EXPECTED_MAIN_REAUDIT_REVIEW,
        "authoritative_remaining_strata": EXPECTED_AUTHORITY[0],
        "authoritative_remaining_terminals": EXPECTED_AUTHORITY[1],
        "historical_sample_only": True,
        "current_v15_survivor_membership_claimed": False,
        "main_pruning_credit": False,
        "full178_complete": False,
        "next_gate": "stage32-01-178-audit",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
