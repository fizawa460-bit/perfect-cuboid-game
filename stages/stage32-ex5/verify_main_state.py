#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
B2 = HERE / "breadth-cycle-2"
MODE = "FULL178_AND_FINAL_MILESTONE_CHAIN"
CURRENT_LEAF = "BC2_20_GLOBAL_NORMAL_POSITIVITY_UNION_CHECK"
DEFAULT_MAIN = "5ca6acba4b591d9e2d40057241c850598c1fa1df"
STAGE32_HEAD = "6827e386f9c450414627573ea305b9794f2341bf"
N355_AUDITED_HEAD = "3f3aadd2e5ada2a0a02a69490d6d659c02762682"
N355_RESULT = "7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775"
BC2_17 = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
BC2_18 = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
BC2_18_OUTPUT = "ca53c910b70cb41dd628cd1d428227b4aa91523ed49b74b0e669e89e7e88fe2e"
BC2_18_STREAM = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
BC2_19 = "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
BC2_19_RAW = "fcfecfc4dbd3592095c1c0302991c2b29bee22b6f3652d73612deea7775d7755"
BC2_20_SOURCE_BLOB = "314b5aad015ed3ace997bbb8b4eef2cafd56697e"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_without(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def checked(path: Path, expected: str, label: str, *, replay_whole: bool = True) -> dict:
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == expected, f"{label} canonical field drift")
    if replay_whole:
        req(canonical_without(obj) == expected, f"{label} canonical replay drift")
    return obj


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    s = load(HERE / "MAIN-STATE.json")
    req(s["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC", "state schema drift")
    req(s["bootstrap"]["active_work_pr"] == 1765 and s["bootstrap"]["merge_authorized"] is False, "working surface drift")
    req(s["bootstrap"]["current_main_sha_observed"] == DEFAULT_MAIN, "default main observation drift")

    a = s["stage32_main_authority"]
    req(a["authority_pr"] == 1753 and a["authority_head_observed"] == STAGE32_HEAD, "Stage32 MAIN head drift")
    req(a["control_mode"] == MODE and a["primary_incomplete_id"] == "32-01", "Stage32 route drift")
    req(a["latest_audited_checkpoint_observed"] == "N355_FULL_KNOWN_PREFIX_BLOCK_SUM", "N355 authority drift")
    req(a["latest_audited_checkpoint_result_canonical_observed"] == N355_RESULT, "N355 result drift")
    req(a["n355_full_prefix_hostile_audit_status"] == "PASS" and a["n355_full_prefix_hostile_audit_review_id"] == 5165895301, "N355 audit drift")
    req(a["n355_full_prefix_hostile_audit_exact_head"] == N355_AUDITED_HEAD and a["n355_full_prefix_audit_credit_consumed"] is True, "N355 consumption drift")
    req(a["latest_audited_remaining_strata"] == 17128 and a["latest_audited_remaining_terminals"] == 66462870551188628549910, "N355 residual drift")
    req(a["n356_status"] == "AUDIT_REQUIRED", "N356 audit gate drift")
    req(a["freshness_commits_ahead_observed"] == 8 and a["freshness_commits_behind_observed"] == 0 and a["freshness_freeze_active"] is False, "N355-to-N356 freshness drift")
    for k in ("V6_is_current_attack_target", "O210_is_current_attack_target", "Q602_is_current_attack_target"):
        req(a[k] is False, f"historical target reactivated: {k}")
    req(a["historical_formal_q602_residues"] == [73,97,235] and a["historical_formal_q602_residues_are_current_survivors"] is False, "Q602 provenance drift")

    cur = s["current"]
    req(cur["status"] == "BC2_19_COMPLETE_7100_UNSAT_236_UNKNOWN_BC2_20_ACTIVE", "EX5 status drift")
    req(cur["leaf"] == CURRENT_LEAF and cur["next_route"] == CURRENT_LEAF, "BC2-20 route drift")

    f = s["frontier"]
    req(f["closed_local_e4_terminal_rank_prefix"] == [0,797], "historical e4 prefix drift")
    req(f["whole_g1_d008_e4_stratum_closed"] is False, "e4 prefix promoted")
    req((f["e8_bc2_18_mod8_parent_count"], f["e8_bc2_19_unsat_parent_count"], f["e8_bc2_19_unknown_parent_count"], f["e8_bc2_19_sat_parent_count"]) == (7336,7100,236,0), "BC2-19 frontier partition drift")
    req(f["e8_bc2_19_whole_first_block_unsat"] is False and f["FULL178_complete"] is False, "BC2-19 UNKNOWN promoted")

    c17 = checked(B2 / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json", BC2_17, "BC2-17")
    c18 = checked(B2 / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json", BC2_18, "BC2-18", replay_whole=False)
    c19 = checked(B2 / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json", BC2_19, "BC2-19")
    req(sum(int(v) for v in c17["retarget"]["fixed_exceptional_pairings"].values()) == 2, "BC2-17 fixed mass drift")
    req(c18["source_locks"]["exact_output_canonical"] == BC2_18_OUTPUT, "BC2-18 exact-output lock drift")
    req(c18["exact_decomposition"]["feasible_stream_sha256"] == BC2_18_STREAM, "BC2-18 stream drift")
    req(c18["exact_decomposition"]["enumerated_parent_count"] == 177100 and c18["exact_decomposition"]["mod8_extendable_parent_count"] == 7336, "BC2-18 parent count drift")
    r = c19["result"]
    req((r["parents_checked"],r["unsat_count"],r["unknown_count"],r["sat_count"]) == (7336,7100,236,0), "BC2-19 result drift")
    req(c19["source_locks"]["raw_result_canonical"] == BC2_19_RAW and r["unknown_relabelled_unsat"] is False, "BC2-19 UNKNOWN firewall drift")

    source = B2 / "bc2_20_global_normal_positivity_union_check.py"
    req(git_blob_sha(source) == BC2_20_SOURCE_BLOB, "BC2-20 source blob drift")
    key = load(HERE / "runkeys" / "bc2-20-global-normal-positivity-union.json")
    req(key["schema"] == "STAGE32EX5_BC2_20_GLOBAL_NORMAL_POSITIVITY_UNION_RUNKEY_V1", "BC2-20 runkey schema drift")
    req(key["generation"] == 2 and key["armed"] is True, "BC2-20 runkey arm drift")
    req(key["source_git_blob_sha"] == BC2_20_SOURCE_BLOB and key["bc2_19_checkpoint_canonical"] == BC2_19, "BC2-20 source/checkpoint lock drift")
    ex = key["execution"]
    req(ex["effective_heavy_concurrency"] == 1 and ex["artifact_retention_days"] == 1, "BC2-20 compute safety drift")
    req(ex["projected_peak_artifact_bytes"] <= 100000 and ex["repository_storage_budget_bytes"] == 524288000, "BC2-20 storage preflight drift")

    idle18 = load(HERE / "runkeys" / "bc2-18-exceptional-mod8-decomposition.json")
    req(idle18["schema"] == "STAGE32EX5_BC2_18_DECOMPOSE_RUNKEY_V1", "BC2-18 runkey schema drift")
    req(idle18["generation"] == 0 and idle18["armed"] is False, "BC2-18 must remain cold on BC2-20 synchronization")
    req(idle18["source_git_blob_sha"] == "1e2ed93cae3c5b446c8d90c1ae2250be83289c79", "BC2-18 source lock drift")

    for section in (s["credit"], s["historical_credit_firewall"], s["firewalls"]):
        for key_name, value in section.items():
            if key_name != "level":
                req(value is False, f"unauthorized credit/firewall: {key_name}")
    req(s["full178_interface"]["n350_registered_producer_count_observed"] == 0, "N350 producer drift")

    docs = {
        "README": (HERE / "README.md").read_text(encoding="utf-8"),
        "START": (HERE / "MAIN-START-HERE.md").read_text(encoding="utf-8"),
        "ROADMAP": (HERE / "CURRENT-ROADMAP.md").read_text(encoding="utf-8"),
        "AUDIT": (HERE / "CURRENT-AUDIT-CONTRACT.md").read_text(encoding="utf-8"),
    }
    for name, text in docs.items():
        req(MODE in text and "N355" in text and "N356" in text and "N350" in text, f"{name} Stage32 routing text drift")
        req("0..797" in text and "7100" in text and "236" in text and "7336" in text, f"{name} EX5 frontier text drift")
        req(CURRENT_LEAF in text, f"{name} BC2-20 route missing")
    req("not the current Stage32 survivor population" in docs["README"], "Q602 survivor firewall lost")
    req("historical Cycle1 source-locked roadmap" in docs["ROADMAP"], "historical roadmap protection lost")
    req("historical Cycle1 source-locked contract" in docs["AUDIT"], "historical audit protection lost")

    print("PASS: Stage32EX5 synced to N355-audited/N356-audit-required; BC2-19 retained; BC2-20 generation2 armed; BC2-18 cold-gated")
    print("e4_local_exact_unsat_prefix=0..797")
    print("e8_bc2_19=7100_UNSAT_236_UNKNOWN_0_SAT")
    print("stage32_main_credit=NO_FROM_EX5")
    print("merge=SEPARATE_USER_ACTION")


if __name__ == "__main__":
    main()
