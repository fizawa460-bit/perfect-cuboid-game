#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED = {
    "n372_result_blob": "c0267d903fd0b397fcd4766b03964bde788650e7",
    "n372_result_canonical": "b9852fcfa926e77e8c51defe31002e0bf4b281dd1db4b5f320326166932fef48",
    "n372_audit_blob": "6ff80567e922890d0fb4517789537d398b34f761",
    "n372_audit_canonical": "4bead765cb9badfe6fb8ce4b1ae0c74807f541e35879fe1ad44b00f240680454",
    "n372_audited_head": "9fb78a0e0c7b52baca84058dea69b8b083e33774",
    "n372_review": 5187357950,
    "main_state_blob": "b8df16056625db5fbb1947f1e927593de258f1ff",
    "main_state_canonical": "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d",
    "terminal": "g1-d008|e=8|rank=128820",
    "n389_canonical": "66f49dc9ceb3313b461bf5322591c350a8fd678bf72cfb5e38edd698242d88c0",
}


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked_json(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    if git_blob_sha1(path) != expected_blob:
        raise SystemExit(f"blob lock mismatch: {path}")
    x = json.loads(path.read_text())
    body = dict(x)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    if claimed != expected_canonical or csha(body) != expected_canonical:
        raise SystemExit(f"canonical lock mismatch: {path}")
    return x


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main-v24-root", type=Path, required=True)
    args = ap.parse_args()

    repo = Path(__file__).resolve().parents[5]
    result = load_locked_json(
        repo / "stages/stage32/32-01-178/nodes/N372/RESULT.json",
        EXPECTED["n372_result_blob"], EXPECTED["n372_result_canonical"],
    )
    audit = load_locked_json(
        repo / "stages/stage32/32-01-178/nodes/N372/AUDIT-PASS.json",
        EXPECTED["n372_audit_blob"], EXPECTED["n372_audit_canonical"],
    )
    state = json.loads((repo / "stages/stage32/32-01-178/nodes/N389/STATE.json").read_text())
    state_body = dict(state)
    claimed = state_body.pop("canonical_sha256_without_this_field", None)
    if claimed != EXPECTED["n389_canonical"] or csha(state_body) != EXPECTED["n389_canonical"]:
        raise SystemExit("N389 state canonical mismatch")

    main_state = load_locked_json(
        args.main_v24_root / "stages/stage32/MAIN-STATE.json",
        EXPECTED["main_state_blob"], EXPECTED["main_state_canonical"],
    )

    w = result["witness"]
    if w["terminal_identity"] != EXPECTED["terminal"]:
        raise SystemExit("N372 terminal identity moved")
    if [w["g"], w["d"], w["e"], w["terminal_rank"]] != [1, 8, 8, 128820]:
        raise SystemExit("N372 terminal coordinates moved")
    if result["status"] != "SAT_CURRENT_V15_WITNESS_CANDIDATE":
        raise SystemExit("N372 result status moved")
    if audit["audited_exact_head"] != EXPECTED["n372_audited_head"] or int(audit["review_id"]) != EXPECTED["n372_review"]:
        raise SystemExit("N372 hostile audit source lock moved")
    if audit["witness"]["terminal_identity"] != EXPECTED["terminal"]:
        raise SystemExit("N372 audited witness identity moved")

    f = main_state["current_exact_frontier"]
    required_true = (
        "n372_candidate_hostile_audited",
        "n372_current_authority_rebased",
        "n372_current_authority_witness",
        "n372_survives_batch_cut193_cut197_cut198",
        "n372_survives_certlift03",
        "n372_survives_hpadj07",
    )
    if any(f.get(k) is not True for k in required_true):
        raise SystemExit("V24 N372 transport flags are not all true")
    if f["n372_terminal_identity"] != EXPECTED["terminal"]:
        raise SystemExit("V24 N372 terminal identity moved")
    if f["authoritative_remaining_terminals_semantics"] != "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET":
        raise SystemExit("V24 residual semantics moved")
    if f["full178_numerical_census_complete"] is not False or f["stage32_closed"] is not False:
        raise SystemExit("V24 closure firewall moved")
    if f["n372_main_pruning_credit"] is not False or f["n372_full178_credit"] is not False:
        raise SystemExit("V24 N372 credit firewall moved")

    if state["scope"]["terminal_identity"] != EXPECTED["terminal"] or int(state["scope"]["subset_cardinality"]) != 1:
        raise SystemExit("N389 singleton scope moved")
    if state["v24_reentry_contract"]["main_global_residual_feasibility_competition"] is not False:
        raise SystemExit("N389 MAIN competition firewall moved")
    if state["v24_reentry_contract"]["heavy_compute_authorized"] is not False:
        raise SystemExit("N389 heavy firewall moved")
    if state["credit"]["additional_pruning_terminals"] != 0:
        raise SystemExit("N389 unexpected pruning credit")
    if any(state["credit"][k] is not False for k in (
        "main_pruning_credit", "full178_complete", "n101_reopened_credit", "effectivity_final",
        "receiver_credit", "theorem_credit", "endpoint_credit", "stage32_closed",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim", "merge_authorized",
    )):
        raise SystemExit("N389 credit firewall moved")

    print("PASS_N389_V24_SINGLETON_IDENTITY_TRANSPORT")
    print(EXPECTED["terminal"])


if __name__ == "__main__":
    main()
