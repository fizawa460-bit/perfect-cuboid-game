#!/usr/bin/env python3
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
STATE = ROOT / "stages/stage32/final-chain/32-03-multibranch/STATE.json"
HANDOFF = Path(__file__).with_name("MB104-COMPACT-AUDIT-RESTART-20260920.md")

EXPECTED = {
    "base_main": "659ba93b9eba657b49a728f549c6bb6028398e08",
    "predecessor_pr": 1825,
    "predecessor_boundary": "d13afbb1a693a5547bebd31ec6fbcc04a7648f05",
    "substantive_freeze_boundary": "37e70e06635892ff29970e58f26efec0f498432b",
    "pair_map": {
        "restriction_certificate_blob": "7b65e7845e0a5028f61afbd85777c541d9eff305",
        "restriction_note_blob": "186173988d6d3d99839d39b7c6b07863e31ba894",
        "discriminant_certificate_blob": "3ee982baf491ecce19b1e49707e66e1edacf812f",
        "discriminant_note_blob": "0e1f7d60276c4e8aa23d1a3236149454cecec7b0",
        "verifier_blob": "6238d8f6c1977dbe88ff78ade09cb5bc5f4b019b",
    },
    "r4": {
        "note_blob": "7fbe74fbab2a0b4c848a1c5c1910b603f72b0adf",
        "certificate_blob": "024ac0e4f1b1caed527e01becd60cea41c27409b",
        "verifier_blob": "df5355623736f188059d0f1c04ce718eef0ef3f6",
    },
    "isotropic": {
        "note_blob": "c65e9daa8f29a4ba525742116c9995cdc9cc504d",
        "certificate_blob": "67e897bd2d46b3382282449b301235af2497109b",
        "runkey_blob": "9dcd460c5d7a73a87e4ed24569c742cac42ea511",
    },
}

def req(ok, msg):
    if not ok:
        raise SystemExit("FAIL: " + msg)

def main():
    d = json.loads(STATE.read_text())
    req(d["schema"] == "STAGE32_32_03_MULTIBRANCH_STATE_V1", "state schema")
    req(d["mission_id"] == "stage32-32-03-multibranch", "mission")
    req(d["status"] == "FROZEN_COMPACT_AUDIT_RESTART_NO_CREDIT", "state freeze")
    req(d["current_node"] == "MB104", "current node")
    req(d["completed_retained_nodes"] == ["MB101","MB102","MB103"], "completed nodes")

    freeze = d["audit_freeze"]
    req(freeze["substantive_boundary_head"] == EXPECTED["substantive_freeze_boundary"], "substantive freeze boundary")
    req(freeze["boundary_semantics"] == "COMPACT_RESTART_SUBSTANTIVE_CONTENT_FROZEN", "freeze semantics")
    req(freeze["post_boundary_changes_must_be_bounded_audit_repairs_only"] is True, "bounded audit repair rule")
    allowed = {
        "stages/stage32/final-chain/32-03-multibranch/STATE.json",
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_compact_audit_restart.py",
    }
    req(set(freeze["allowed_post_boundary_paths"]) == allowed, "post-boundary path allowlist")

    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    anc = subprocess.run(
        ["git", "merge-base", "--is-ancestor", EXPECTED["substantive_freeze_boundary"], head],
        cwd=ROOT,
    )
    req(anc.returncode == 0, "freeze boundary must be ancestor of exact HEAD")
    changed = {
        x for x in subprocess.check_output(
            ["git", "diff", "--name-only", EXPECTED["substantive_freeze_boundary"] + ".." + head],
            cwd=ROOT,
            text=True,
        ).splitlines()
        if x
    }
    req(changed <= allowed, "post-freeze substantive path detected: " + ",".join(sorted(changed - allowed)))

    rb = d["restart_boundary"]
    req(rb["base_main"] == EXPECTED["base_main"], "base main")
    req(rb["predecessor_pr"] == EXPECTED["predecessor_pr"], "predecessor PR")
    req(rb["predecessor_retained_boundary"] == EXPECTED["predecessor_boundary"], "predecessor boundary")
    req(rb["predecessor_latest_reaudit_status"] == "FAIL", "predecessor audit status")
    req(rb["local_history_copied"] is False, "history must not be copied")

    pm = d["retained_frontier"]["pair_map"]
    req(pm["status"] == "ARCHIVED_PRE_AUDIT_ZERO_EXCLUSION_CREDIT", "pair-map status")
    req(pm["support_mask"] == "000707000f0f", "support mask")
    for k,v in EXPECTED["pair_map"].items():
        req(pm[k] == v, f"pair-map lock {k}")
    req("all r=1,2,3,4 remain OPEN" in pm["result"], "all restriction degrees open")
    req("no orbit excluded" in pm["result"], "no orbit exclusion")
    req("864" in pm["result"], "support count 864")
    req("Stein/common-vertical correction mandatory" in pm["result"], "Stein correction")

    r4 = d["retained_frontier"]["r4"]
    req(r4["status"] == "ARCHIVED_PRE_AUDIT_NO_CREDIT", "R4 status")
    for k,v in EXPECTED["r4"].items():
        req(r4[k] == v, f"R4 lock {k}")
    req("no finite window or credit" in r4["result"], "R4 zero credit")

    iso = d["retained_frontier"]["isotropic_shell_preflight"]
    req(iso["status"] == "ARCHIVED_COLD_PREFLIGHT_NO_EXECUTION_NO_CREDIT", "isotropic status")
    for k,v in EXPECTED["isotropic"].items():
        req(iso[k] == v, f"isotropic lock {k}")
    req(iso["numerical_execution_completed"] is False, "isotropic execution must be false")
    req("no numerical result" in iso["result"], "isotropic no result")

    nxt = d["next_obligation"]
    req(nxt["active_leaf"] == "MB104-COMPACT-HOSTILE-REAUDIT-RESTART", "audit leaf")
    req(any("new substantive MB104 mathematics" in x for x in nxt["must_not_repeat"]), "research freeze text")
    req(any("isotropic-shell heavy compute" in x for x in nxt["must_not_repeat"]), "heavy freeze text")

    routing = d["routing"]
    req(routing["current_branch_is_compact_audit_restart"] is True, "compact restart route")
    req(routing["predecessor_pr_is_archive_only"] is True, "predecessor archive only")
    req(routing["substantive_research_append_blocked_until_reaudit_pass"] is True, "research blocked")

    req(all(v is False for v in d["credit_firewall"].values()), "credit firewall")

    h = HANDOFF.read_text()
    for needle in (
        EXPECTED["base_main"],
        EXPECTED["predecessor_boundary"],
        "all restriction degrees `r=1,2,3,4` remain OPEN",
        "remaining balanced support count is `48+48+768=864`",
        "No shell execution is consumed",
        "ZERO CREDIT",
    ):
        req(needle in h, f"handoff text: {needle}")

    # All locked blob identities are literal Git SHA-1s.
    for section in ("pair_map","r4","isotropic"):
        for v in EXPECTED[section].values():
            req(re.fullmatch(r"[0-9a-f]{40}", v) is not None, f"blob syntax {section}")

    print("PASS: MB104 compact audit restart")
    print("base main", EXPECTED["base_main"])
    print("substantive freeze boundary", EXPECTED["substantive_freeze_boundary"])
    print("post-freeze changed paths", ",".join(sorted(changed)))
    print("predecessor retained boundary", EXPECTED["predecessor_boundary"])
    print("pair-map: all r open, no excluded orbit, 864 supports")
    print("R4 and isotropic-shell preflight: archived zero-credit only")
    print("substantive research and heavy compute remain blocked until hostile-audit PASS")

if __name__ == "__main__":
    main()
