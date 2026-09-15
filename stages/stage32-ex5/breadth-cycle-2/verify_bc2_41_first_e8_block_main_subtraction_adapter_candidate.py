#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
B2 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
CUT = ROOT / "stages/stage32-ex5/cut-handoff"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"
CAND = B2 / "bc2-41-first-e8-block-main-subtraction-adapter-candidate.json"
PREFLIGHT = CUT / "e8-terminal-population-preflight.json"
ADAPTER = CUT / "e8_terminal_population_adapter.py"
BC231 = B2 / "bc2-31-fresh-all7336-replay-checkpoint.json"
BC240 = B2 / "bc2-40-hostile-audit-pass-consumption.json"

EXPECTED_CANON = "cd40eb0e9b380eb219d94fd75d44b457bcdb3d1edee83f1c9a56cac38415628a"
EXPECTED_BLOBS = {
    MAIN: "b8df16056625db5fbb1947f1e927593de258f1ff",
    PREFLIGHT: "b28539d9d0eafddc181d3bbf6d668261f2ff081e",
    ADAPTER: "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f",
    BC231: "188601efcb99d33fe00fc60dc3c2f40f51e65b20",
    BC240: "40728003e6f56e485fc87642fe3af1ae3740b90d",
}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()


def canon(o: dict) -> str:
    body = dict(o)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    for path, expected in EXPECTED_BLOBS.items():
        req(path.is_file(), f"missing source-lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    c = json.loads(CAND.read_text())
    req(c["schema"] == "STAGE32EX5_BC2_41_FIRST_E8_BLOCK_MAIN_SUBTRACTION_ADAPTER_CANDIDATE_V1", "schema")
    req(c["canonical_sha256_without_this_field"] == EXPECTED_CANON and canon(c) == EXPECTED_CANON, "candidate canonical")
    req(c["status"] == "AUDIT_REQUIRED_NO_MAIN_CREDIT", "candidate status")

    t = c["target"]
    req(t == {"block_index": 0, "current_main_audited_prefix_survivor": True, "d": 8, "e": 8, "g": 1, "row_id": "g1-d008", "terminal_count": 113, "terminal_rank_range": [0, 112]}, "target identity")

    p = json.loads(PREFLIGHT.read_text())
    req(p["adapter_universe"]["terminal_block_width"] == 113, "block width")
    req(p["adapter_semantics"]["first_block_regression_parent_count"] == 7336, "first-block parent count")
    req(p["adapter_semantics"]["first_block_regression_stream_sha256"] == "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7", "first-block stream")

    r31 = json.loads(BC231.read_text())
    req(r31["fresh_replay"]["parents_checked"] == 7336, "BC2-31 all7336 coverage")

    r40 = json.loads(BC240.read_text())
    req(r40["audit"]["exact_head"] == "b3b16f3db20074e3dbdb1851ad123d5c2004b843", "BC2-40 audit head")
    req(r40["audit"]["review_id"] == 5204245683, "BC2-40 audit review")
    co = r40["consumption"]
    req(co["ex5_audited_known_parent_unsat_lower_bound_after"] == 7336, "audited 7336")
    req(co["remaining_unknown_count"] == 0 and co["sat_count"] == 0, "no unknown/sat")
    req(co["first_e8_block_picard64_obstruction_closed"] is True, "first block closed")
    req(co["stage32_main_subtraction_authorized"] is False, "no MAIN subtraction yet")

    cov = c["coverage"]
    req(cov["modular_feasible_parent_count"] == 7336 and cov["bc2_40_audited_unsat_parent_count"] == 7336, "coverage cardinality")
    req(cov["remaining_unknown_count"] == 0 and cov["sat_count"] == 0, "coverage statuses")
    req(cov["coverage_exact_candidate"] is True and cov["gap_count"] == 0 and cov["overlap_count"] == 0, "coverage exactness candidate")

    cc = c["candidate_consequence"]
    req(cc["main_terminal_subtraction_candidate"] == 113, "candidate subtraction cardinality")
    req(cc["main_terminal_subtraction_authorized"] is False, "MAIN subtraction firewall")
    req(cc["whole_g1_d008_e8_stratum_closed"] is False and cc["full178_complete"] is False, "scope firewall")
    req(all(v is False for v in c["firewalls"].values()), "credit firewalls")
    req(c["audit_gate"]["hostile_audit_required_before_main_acceptance"] is True, "hostile audit gate")
    req(c["audit_gate"]["main_acceptance_required_before_subtraction"] is True, "MAIN acceptance gate")
    req(c["audit_gate"]["new_heavy_authorized"] is False and c["audit_gate"]["merge_authorized"] is False, "execution firewall")

    print("PASS: BC2-41 candidate binds audited 7336-parent first-e8-block obstruction to a 113-terminal MAIN subtraction candidate; MAIN credit=NO audit-required=YES")


if __name__ == "__main__":
    main()
