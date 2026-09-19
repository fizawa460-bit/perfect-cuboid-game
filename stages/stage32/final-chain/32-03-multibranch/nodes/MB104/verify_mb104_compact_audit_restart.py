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
    req(d["status"] in {"FROZEN_COMPACT_AUDIT_RESTART_NO_CREDIT","ACTIVE_POST_AUDIT_RESEARCH_ZERO_CREDIT"}, "state mode")
    req(d["current_node"] == "MB104", "current node")
    req(d["completed_retained_nodes"] == ["MB101","MB102","MB103"], "completed nodes")
    surf = d["active_surface"]
    req(surf["pr_number"] == 1827, "active PR")
    req(surf["branch"] == "stage32mb-audit-restart-20260920", "active branch")
    req(surf["predecessor_archive_pr"] == 1825, "archive predecessor")
    req(surf["predecessor_archive_status"] == "CLOSED_SUPERSEDED", "archive predecessor status")
    req(surf["alternate_open_mb_pr_allowed"] is False, "single active MB surface")
    hist = d["audit_history"]
    req(hist["prior_pass"]["exact_head"] == "70c2fe772df63362d82df537ea889658eb03f58f", "prior pass head")
    req(hist["prior_pass"]["review_id"] == 5257816963, "prior pass review")
    req(hist["latest_fail"]["exact_head"] == "b8596b038a6687bdec8f400d987bd8a680fea018", "latest fail head")
    req(hist["latest_fail"]["review_id"] == 5257949069, "latest fail review")
    req(hist["current_head_inherits_prior_pass"] is False, "no audit inheritance")

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
    if d["status"] == "FROZEN_COMPACT_AUDIT_RESTART_NO_CREDIT":
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
    routing = d["routing"]
    req(routing["current_branch_is_compact_audit_restart"] is True, "compact restart route")
    req(routing["predecessor_pr_is_archive_only"] is True, "predecessor archive only")
    req(routing["active_pr_number"] == 1827, "routing active PR")
    req(routing["active_branch"] == "stage32mb-audit-restart-20260920", "routing active branch")
    req(routing["isotropic_shell_pilot_authorized"] is False, "pilot blocked")
    req(routing["isotropic_shell_scaleout_authorized"] is False, "scaleout blocked")

    if d["status"] == "FROZEN_COMPACT_AUDIT_RESTART_NO_CREDIT":
        req(nxt["active_leaf"] == "MB104-COMPACT-HOSTILE-REAUDIT-RESTART", "audit leaf")
        req(any("new substantive MB104 mathematics" in x for x in nxt["must_not_repeat"]), "research freeze text")
        req(any("isotropic-shell heavy compute" in x for x in nxt["must_not_repeat"]), "heavy freeze text")
        req(routing["substantive_research_append_blocked_until_reaudit_pass"] is True, "research blocked")
        req(routing["latest_audited_exact_head"] == "70c2fe772df63362d82df537ea889658eb03f58f", "routing last audited head")
        req(routing["current_head_reaudit_required"] is True, "current-head reaudit")
    elif d["status"] == "ACTIVE_POST_AUDIT_RESEARCH_ZERO_CREDIT":
        ar = d["audit_release"]
        req(ar["hostile_audit_status"] == "PASS", "post-audit PASS")
        req(ar["audited_exact_head"] == "37727ad09b62c49b49cfb2e1e428b5a2d4826e88", "post-audit exact head")
        req(ar["hostile_audit_review_id"] == 5258058107, "corrected PASS receipt")
        req(ar["corrected_prior_hold_review_id"] == 5257998935, "corrected prior HOLD receipt")
        req(ar["isotropic_shell_execution_authorized"] is False, "heavy shell remains blocked")
        req(routing["substantive_research_append_blocked_until_reaudit_pass"] is False, "research released")
        req(routing["current_head_reaudit_required"] is False, "ordinary research mode")
        req(routing["ordinary_mb104_research_released_by_review"] == 5258058107, "research release receipt")
        req(routing["fibration_search_below_36_closed"] is True, "fibration lower route closed")
        g7=d["retained_frontier"]["genus7_fibration"]
        req(g7["source_ref"] == EXPECTED["predecessor_boundary"], "genus7 source ref")
        req(g7["note_blob"] == "9f167d28d5945462e436397c1a244133cf6b6a51", "genus7 note lock")
        req(g7["certificate_blob"] == "f3b158df6b9105d863d8174340ba1adb075a7f1a", "genus7 certificate lock")
        req(g7["verifier_blob"] == "fcfa76f662e9575daef87b2da7042159d972a896", "genus7 verifier lock")
        req(g7["degree10_improves_40"] is False, "degree10 closure")
        req(g7["size768_global_fibration_minimum"] == 36, "global fibration minimum")
        req(g7["rank3_pairings"] == [4,4,6,4,4,6], "genus7/rank3 pairings")
        four=d["retained_frontier"]["rank3_fourmap_b3_quotient"]
        req(four["source_ref"] == EXPECTED["predecessor_boundary"], "fourmap source ref")
        req(four["source_six_fibration_note_blob"] == "533757a857887b776d2ad9cdefb5b95133d27df2", "six-fibration source lock")
        req(four["source_full28_verifier_blob"] == "544c85cd468e84671650adaaee84e59d72333243", "full28 source lock")
        req(four["selected_rank3_indices"] == [0,1,3,4], "selected rank3 maps")
        blocks=[set(range(0,8)),set(range(8,16)),set(range(24,32)),set(range(32,40))]
        req([sorted(x) for x in blocks] == four["selected_base_blocks_0based"], "selected base blocks")
        contracted=sorted(set(range(48))-set().union(*blocks))
        req(contracted == list(range(16,24))+list(range(40,48)), "fourmap contracted exceptional set")
        req(contracted == four["common_contracted_exceptional_nodes_0based"], "fourmap contracted exceptional certificate")
        support=set(four["support_nodes_0based"])
        req(support == {0,1,2,3,8,9,10,11,24,25,26,32,33,34}, "fourmap support")
        req(not (support & set(contracted)), "contracted exceptionals avoid support")
        req(four["common_contracted_exceptionals_meeting_support"] == 0, "carrier avoids contracted exceptionals")
        sigma={0:1,1:0,2:3,3:2,4:5,5:4,6:7,7:6,
               8:9,9:8,10:11,11:10,12:13,13:12,14:15,15:14,
               16:16,17:17,18:18,19:19,20:20,21:21,22:22,23:23,
               24:25,25:24,26:27,27:26,28:29,29:28,30:31,31:30,
               32:33,33:32,34:35,35:34,36:37,37:36,38:39,39:38,
               40:40,41:41,42:42,43:43,44:44,45:45,46:46,47:47}
        sigsupp={sigma[i] for i in support}
        req(sorted(sigsupp) == four["sigma_support_nodes_0based"], "b3 sign support image")
        req(len(support & sigsupp) == four["sigma_support_intersection_size"] == 12, "support overlap under b3 sign")
        req(support != sigsupp and four["support_sigma_invariant"] is False, "support not b3 invariant")
        req(49*16 - 32*len(support & sigsupp) == four["P_dot_sigmaP"] == 400, "P dot sigmaP")
        req(four["omitted_coordinate"] == "b3" and four["generic_degree_to_fourmap_image"] == 2, "b3 quotient degree")
        req(four["nonexceptional_common_contracted_curves"] == 0, "nonexceptional common contraction")
        req(four["carrier_invariant_under_sigma"] is False and four["carrier_to_quotient_generic_degree"] == 1, "carrier quotient degree")
        req(all(x is False for x in four["firewalls"].values()), "fourmap credit firewall")
        req(routing["current_leaf_uses_finite_b3_quotient"] is True, "b3 quotient route")
        req(routing["single_pair_stein_correction_still_open"] is True, "single-pair Stein firewall")
        req(routing["fourmap_common_vertical_meets_carrier"] is False, "fourmap carrier finiteness")
        req(d["next_obligation"]["active_leaf"] == "MB104-000707-B3-QUOTIENT-CONDUCTOR-COLLISION", "post-audit active leaf")
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
    print("mode", d["status"])
    print("isotropic-shell heavy compute remains blocked; ordinary research follows live STATE")

if __name__ == "__main__":
    main()
