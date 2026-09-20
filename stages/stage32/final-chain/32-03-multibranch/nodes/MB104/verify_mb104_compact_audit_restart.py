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
        req(freeze["boundary_semantics"] == "COMPACT_RESTART_SUBSTANTIVE_CONTENT_FROZEN", "freeze semantics")
        req(freeze["post_boundary_changes_must_be_bounded_audit_repairs_only"] is True, "bounded audit repair rule")
        req(changed <= allowed, "post-freeze substantive path detected: " + ",".join(sorted(changed - allowed)))
    else:
        req(freeze["boundary_semantics"] == "AUDITED_COMPACT_RESTART_BOUNDARY__POST_AUDIT_RESEARCH_RELEASED", "post-audit boundary semantics")
        req(freeze["post_boundary_changes_must_be_bounded_audit_repairs_only"] is False, "post-audit research release")
        req(set(freeze["post_audit_research_path_allowlist"]) == allowed, "post-audit research path allowlist")
        req(changed <= allowed, "post-audit path detected outside compact research surface: " + ",".join(sorted(changed - allowed)))

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
        qc=d["retained_frontier"]["b3_quotient_collision_accounting"]
        req(qc["source_w4_k3_note_ref"] == "b28adadc95776762754e1415a0ecab0da1d4cd8e", "W4 K3 source ref")
        req(qc["source_w4_k3_note_blob"] == "ff61ae6c06549af194b4f1af611c7d4ea46d0dff", "W4 K3 source blob")
        req(qc["source_w4_root_wall_blob"] == "b28fbeb260250ec2cb97ee45aaaf1933a886909a", "W4 root-wall source blob")
        q=qc["pushdown_class"]
        req(q["H_K_square"] == 8 and q["H_K_dot_Q"] == 112 and q["Q_square"] == 736, "b3 pushdown numerics")
        req(q["support_quotient_node_weights"] == [2,2,2,2,2,2,1,1], "b3 quotient weights")
        req(1568-32*sum(x*x for x in q["support_quotient_node_weights"]) == 736, "b3 pushdown square replay")
        req(qc["image_curve"]["arithmetic_genus_formula"] == "1+368*l^2", "K3 image arithmetic genus")
        req(qc["image_curve"]["delta_formula"] == "368*l^2", "K3 image delta")
        req(qc["branch"]["class"] == "2H_K" and qc["branch"]["D_dot_branch_over_l"] == 224, "double-cover branch class")
        req(qc["branch"]["pullback_branch_divisor_even"] is True and qc["branch"]["normalization_half_branch_degree_over_l"] == 112, "split branch condition")
        req(qc["carrier"]["P_dot_sigmaP"] == 400 and qc["carrier"]["sigma_invariant"] is False, "carrier conjugate data")
        req(qc["collision_identity"]["C_dot_sigmaC_formula"] == "400*l^2", "conjugate intersection")
        req(qc["collision_identity"]["branch_part_of_C_dot_sigmaC_formula"] == "112*l", "branch intersection contribution")
        req(qc["collision_identity"]["off_branch_C_dot_sigmaC_formula"] == "400*l^2-112*l", "off-branch intersection")
        req(qc["collision_identity"]["quotient_added_delta_formula"] == "200*l^2-56*l", "added quotient delta")
        for l in (1,2,3,7):
            delta_c=168*l*l+56*l
            extra=(400*l*l-112*l)//2
            delta_d=368*l*l
            req(delta_c+extra == delta_d, "quotient collision identity")
        req(all(x is False for x in qc["firewalls"].values()), "quotient collision firewalls")
        req(routing["b3_quotient_genus_collision_route"] == "CLOSED_AS_EXACT_EQUALITY", "quotient genus route closed")
        sb=d["retained_frontier"]["b3_split_branch_conductor_nogo"]
        req(sb["source_w4_k3_note_blob"] == "ff61ae6c06549af194b4f1af611c7d4ea46d0dff", "split source lock")
        req(sb["conductor_abel_note_blob"] == "02eb62f926f3f7192e5c642b2a5d874d6086e35a", "conductor Abel source lock")
        req(sb["theta_ratio_nogo_note_blob"] == "bf1d6b96ae6674abe50f42e9a147fb040812c81e", "theta no-go source lock")
        req(sb["ambient_square_root"] == "q^*(a1^2+a2^2)=b3^2", "ambient b3 square root")
        req(sb["branch_half_line"] == "O_E(Z)=H_E", "branch half line")
        req(sb["support_divisor_line"] == "O_E(B_node)=H_E", "support line")
        req(sb["conductor_line"] == "O_E(Delta)=H_E^(3l+1)", "conductor line")
        req(sb["support_nodes_have_b3_nonzero"] is True and sb["Z_disjoint_from_supported_node_divisor"] is True, "b3/support disjointness")
        req(sb["fibration_functions_can_detect_beauville_sheet"] is False, "box functions sheet blind")
        req(all(x is False for x in sb["firewalls"].values()), "split-branch firewalls")

        eta=d["retained_frontier"]["absent_eta_character_line"]
        req(eta["source_exact_grid_note_blob"] == "cf7048489a4bd9c7588ac32c58bb05abbe1c942c", "eta grid source lock")
        req(eta["source_support_factorization_note_blob"] == "3096203416a621e90bfb4d2fc57e038063358edc", "eta support factorization lock")
        req(eta["source_ratio_nogo_note_blob"] == "bf1d6b96ae6674abe50f42e9a147fb040812c81e", "eta ratio no-go lock")
        req(eta["source_fullG_character_note_blob"] == "cbc8307689ae91b08f547fe1c69606086d06dec1", "eta full-G source lock")
        req(eta["factor1_unramified_per_l"] == [32,24,56,0,0,0], "eta factor1 passport")
        req(eta["factor2_unramified_per_l"] == [56,0,24,32,0,0], "eta factor2 passport")
        req(eta["intrinsic_branch_divisors"]["b1_type"] == "U1=B_w=phi_2^(-1)(1)", "eta U1")
        req(eta["intrinsic_branch_divisors"]["b2_type"] == "U2=B_z=phi_1^(-1)(i)", "eta U2")
        req(eta["intrinsic_branch_divisors"]["b3_type"] == "U3=0", "eta U3")
        req(eta["relations"] == ["M^2=H_E","N1^2=M","N2^2=M","eta=N3","eta^2=O_E","N1*N2*eta=M","eta=N1/N2"], "eta line relations")
        req(eta["eta_nontrivial"] is True, "eta nontrivial")
        req(eta["abstract_G_cover_building_data_obstructed"] is False, "eta building data feasible")
        req(all(x is False for x in eta["firewalls"].values()), "eta firewalls")

        req(routing["b3_split_branch_condition_live"] is False, "split branch no longer live")
        req(routing["b3_split_branch_route"] == "CLOSED_TAUTOLOGICAL_BY_AMBIENT_B3", "split branch closure")
        req(routing["absent_eta_character_line_route"] == "CLOSED_FEASIBLE_AT_LINE_BUNDLE_LEVEL", "eta line closure")
        req(routing["anti_invariant_conductor_first_jet_live"] is True, "anti-invariant jet route live")
        req(routing["box_surface_functions_are_sheet_blind"] is True, "box sheet blindness")
        req(routing["f7_second_section_not_a_sheet_detector"] is True, "f7 sheet firewall")
        aw=d["retained_frontier"]["anti_invariant_conductor_source_wall"]
        req(aw["source_ambient_theta_note_blob"] == "de6e17164f0478703bd98f49cd5cd25639753849", "anti-invariant theta source")
        req(aw["source_post_conductor_reaudit_blob"] == "4d931b66f2c0bae598ec70bddc6cca110c435413", "post-conductor re-audit source")
        req(aw["route_disposition"] == "PARK_UNTIL_NEW_ANTI_INVARIANT_MARKED_LIFT_DATA", "anti-invariant source wall")
        req(all(x is False for x in aw["firewalls"].values()), "anti-invariant wall firewalls")

        z12=d["retained_frontier"]["z12_current_main_btva_adapter_check"]
        req(z12["current_main_observed"] == "da573f048a82a63e459be1343fb002e663b60875", "Z12 current-main observation")
        req(z12["main_btva_preflight_blob"] == "68108dfb110c4ea1d9dc0d74564a431bbbffbbde", "MAIN BTVA source")
        req(z12["exact_adapter_exists"] is False, "Z12 adapter mismatch")
        req(z12["firewalls"]["main_btva_credit_imported"] is False, "no MAIN BTVA import")

        sc=d["retained_frontier"]["support_hyperplane_subcanonical_bridge"]
        req(sc["source_complete_null_locus_note_blob"] == "4bf6e651755183d5d5856b7cc3706839f4fe9880", "subcanonical null-locus source")
        req(sc["source_big_nef_note_blob"] == "30885461425a725a5ad8b928686aef0b91d60b89", "subcanonical big-nef source")
        req(sc["source_z33g_gluing_note_blob"] == "14c1661c5a3b1975474c1f983ed08b29c2150731", "subcanonical Z33G source")
        req(sc["source_conductor_regularitiy_preflight_blob"] == "ed97e80bdae255d68e2684bc805a3d229ee2f26e", "conductor regularity source")
        support=set(sc["support_nodes_0based"])
        incidence=set(sc["incidence16_nodes_0based"])
        omitted=set(sc["omitted_incidence_nodes_0based"])
        req(incidence-support == omitted == {27,35}, "incidence/support omitted nodes")
        req(sc["hyperplane_section_on_canonical_surface"] == "2QA+2QB", "size768 doubled quartic section")
        rd=sc["resolution_divisor"]
        req(rd["effective_decomposition"] == "2QA+2QB+E27+E35", "effective D decomposition")
        req(rd["H_dot"] == 16 and rd["square"] == -12 and rd["P_dot"] == 0, "D numerics")
        req(sc["carrier"]["class"] == "C=lP" and sc["carrier"]["C_dot_D"] == 0 and sc["carrier"]["disjoint_from_D"] is True, "carrier disjoint D")
        req(sc["exact_restriction_identities"] == ["O_C(D)=O_C","P=3H+4D","O_C(P)=O_C(3H)","O_C(C)=O_C(3lH)","omega_C=O_C((3l+1)H)"], "subcanonical identities")
        req(sc["firewalls"]["carrier_H_subcanonical"] is True, "H-subcanonical exact")
        req(sc["firewalls"]["carrier_ACM_proved"] is False and sc["firewalls"]["projective_image_AG_proved"] is False, "ACM/AG firewall")

        req(routing["anti_invariant_conductor_first_jet_live"] is False, "anti-invariant no longer live")
        req(routing["anti_invariant_conductor_route"] == "PARKED_BOUNDED_SOURCE_WALL", "anti-invariant parked")
        req(routing["z12_current_main_btva_adapter_available"] is False, "Z12 MAIN adapter absent")
        req(routing["H_polarized_subcanonical_bridge_exact"] is True, "subcanonical bridge routing")
        req(routing["ACM_section_ring_gate_live"] is True, "ACM gate live")
        pc=d["retained_frontier"]["projective_ci_conductor_regularity"]
        req(pc["source_z41_tricanonical_blob"] == "19a7f6dfb82efbaaa68fbd47e45c91eacc7acfd5", "projective CI Z41 source")
        req(pc["source_z48_conductor_blob"] == "69b3e039ebc967c84f7c64d4946a114f09d07fba", "projective CI Z48 source")
        req(pc["source_z48b_hypothesis_wall_blob"] == "ed97e80bdae255d68e2684bc805a3d229ee2f26e", "projective CI Z48B source")
        req(pc["external_theorem"]["arxiv"] == "1302.5752" and pc["external_theorem"]["locator"] == "Theorem 3.1", "Eisenbud-Ulrich source")
        cm=pc["canonical_model"]
        req(cm["projective_curve"] == "Cbar=CI(2,2,2,2,7l)", "canonical-model CI carrier")
        nr=pc["normalization_ring"]
        req(nr["A1_dimension"] == 7 and nr["indeg_B_over_A"] == 1, "normalization indeg")
        nodes=pc["supported_A1_nodes"]
        req(nodes["count"] == 14, "supported A1 count")
        tot=pc["total_projective_conductor"]
        for l in (1,2,3,7):
            req(16*7*l == 112*l, "CI degree")
            req(1 + ((7*l+1)*112*l)//2 == 392*l*l+56*l+1, "CI arithmetic genus")
            req((392*l*l+56*l+1)-(168*l*l+56*l+1) == 224*l*l, "node genus delta")
            req(14*16*l*l == 224*l*l, "node delta replay")
            req((168*l*l+56*l)+(224*l*l) == 392*l*l+56*l, "total delta replay")
            req(2*(392*l*l+56*l) == 784*l*l+112*l, "total different replay")
            req((7*l+4)-1-1 == 7*l+2, "Eisenbud-Ulrich regularity")
            req(112*l-7 > 0, "B/A degree-one dimension")
        req(tot["reg_X_ideal_formula"] == "7*l+4", "CI reg X")
        req(tot["conductor_ambient_ideal_regularity_formula"] == "7*l+2", "conductor reg")
        req(tot["highest_degree_fifth_syzygy_count_formula"] == "112*l-7", "top syzygy count")
        req(pc["firewalls"]["projective_Cbar_AG"] is True and pc["firewalls"]["normalization_ring_CM"] is True and pc["firewalls"]["eisenbud_ulrich_applicable"] is True, "EU hypotheses")
        req(pc["firewalls"]["conductor_geometry_contradiction"] is False, "no premature conductor contradiction")

        req(routing["ACM_section_ring_gate_live"] is False, "old ACM gate closed")
        req(routing["projective_CI_carrier_adapter_exact"] is True, "projective CI adapter")
        req(routing["eisenbud_ulrich_conductor_regularity_live"] is False, "EU route closed")
        req(routing["projective_conductor_decomposition_leaf_live"] is False, "projective conductor leaf closed")
        req(routing["projective_conductor_regularity_route"] == "CLOSED_EXACT_COMPATIBILITY_NO_GO", "projective conductor no-go")
        cl=pc["regularity_decomposition_closure"]
        req(cl["total_different_identity"] == "Delta_total=4l*B_node+Delta_int", "different decomposition")
        req(cl["B_node_line"] == "O_E(B_node)=H_E", "node divisor line")
        req(cl["interior_different_line"] == "O_E(Delta_int)=H_E^(3l+1)", "interior different line")
        req(cl["total_different_line"] == "O_E(Delta_total)=H_E^(7l+1)=nu^*omega_Cbar", "total different line")
        req(cl["minimal_conductor_section_degree_formula"] == "7*l+1", "minimal conductor degree")
        req(cl["conductor_ideal_regularity_formula"] == "7*l+2", "regularity compatibility")
        req(cl["null_quartic_residual_degree"] == 4 and cl["null_quartic_residual_line"] == "H|Q", "quartic residual")
        req(cl["top_syzygy_interpretation"] == "112l-7 equals dim(B_1/A_1), the degree-one normalization defect", "top syzygy interpretation")

        cyc=d["retained_frontier"]["cycle_breadth_audit_20260920"]
        req(cyc["exhaustive_view_audit"] is True and cyc["blind_rediscovery"] is True, "cycle breadth audit")
        req(cyc["split_triggered"] is False, "cycle no split")
        statuses={x["name"]:x["status"] for x in cyc["candidates"]}
        req(statuses["projective conductor regularity decomposition"] == "BLOCKED_NO_NEW_INFORMATION", "cycle conductor status")
        req(statuses["finite normalization-module Betti receiver"] == "LIVE", "cycle live Betti receiver")
        req(statuses["generic finite replacement receiver beyond graded module"] == "UNTESTED", "cycle untested fallback")
        cf=cyc["cycle_fields"]
        req(cf["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True and cf["CYCLE_BLIND_REDISCOVERY"] is True, "cycle fields audit")
        req(cf["CYCLE_NEW_VIEW"] == "normalization-module Hilbert numerator and Gorenstein self-dual Betti constraints", "cycle new view")

        nb=d["retained_frontier"]["normalization_module_betti_preflight"]
        req(nb["codimension_over_S"] == 5 and nb["Cohen_Macaulay"] is True, "normalization module CM codim")
        req(nb["H_E_degree_formula"] == "d=112*l", "normalization degree")
        req(nb["B_hilbert_series"] == "1+d*t/(1-t)^2", "normalization Hilbert series")
        req(nb["B_hilbert_numerator"] == "1+(d-7)t+(21-5d)t^2+(10d-35)t^3+(35-10d)t^4+(5d-21)t^5+(7-d)t^6-t^7", "normalization Hilbert numerator")
        for l in (1,2,3,7):
            dd=112*l
            coeff=[1,dd-7,21-5*dd,10*dd-35,35-10*dd,5*dd-21,7-dd,-1]
            req(coeff[1] > 0 and coeff[2] < 0 and coeff[3] > 0 and coeff[4] < 0 and coeff[5] > 0 and coeff[6] < 0, "Hilbert numerator alternating signs")
        req(nb["candidate_pattern_status"] == "PROVED_UNIQUE_MINIMAL_S_FREE_RESOLUTION_SHAPE", "Betti resolution proved")
        req(nb["regularity_proof"]["result"] == "reg_S(B)=2", "Betti regularity")
        req(nb["canonical_module_proof"]["result"] == "omega_B=B", "Betti canonical module")
        req(nb["canonical_module_proof"]["local_duality"] == "Ext^5_S(B,S(-7))=B", "Betti local duality")
        req(nb["canonical_module_proof"]["betti_symmetry"] == "beta_(i,j)=beta_(5-i,7-j)", "Betti symmetry")
        bt=nb["forced_betti_table"]
        req(bt["F0"] == ["S","S(-1)^(d-7)"], "Betti F0")
        req(bt["F1"] == ["S(-2)^(5d-21)"], "Betti F1")
        req(bt["F2"] == ["S(-3)^(10d-35)"], "Betti F2")
        req(bt["F3"] == ["S(-4)^(10d-35)"], "Betti F3")
        req(bt["F4"] == ["S(-5)^(5d-21)"], "Betti F4")
        req(bt["F5"] == ["S(-6)^(d-7)","S(-7)"], "Betti F5")
        req(nb["compatibility_checks"]["all_multiplicities_positive_for_l_ge_1"] is True, "Betti positivity")
        req(nb["compatibility_checks"]["contradiction"] is False, "Betti no contradiction")
        req(nb["compatibility_checks"]["bounded_receiver_obtained"] is False, "Betti not bounded")
        req(nb["firewalls"]["candidate_betti_table_proved"] is True and nb["firewalls"]["graded_self_duality_shift_proved"] is True, "Betti proof firewalls")
        req(nb["firewalls"]["carrier_excluded"] is False and nb["firewalls"]["finite_degree_window"] is False, "Betti zero exclusion")

        els=d["retained_frontier"]["elliptic_linear_series_syzygy_shallow"]
        req(els["section_space_dimension"] == 7 and els["supported_fibers"] == 14, "linear-series packet")
        req(els["common_support_section"] == "h", "linear-series common section")
        req(els["firewalls"]["new_linear_series_obstruction"] is False, "linear-series no-go")

        req(routing["normalization_module_betti_leaf_live"] is False, "Betti leaf closed")
        req(routing["normalization_module_betti_route"] == "CLOSED_FORCED_COMPATIBLE_SELF_DUAL_RESOLUTION", "Betti route closure")
        req(routing["elliptic_linear_series_shallow_route"] == "CLOSED_EQUIVALENT_DOMINATED", "linear-series closure")

        nu=d["retained_frontier"]["null_union_ambient_lift_shallow"]
        req(nu["source_z33e_note_blob"] == "57fa113b33ed827fd8b5d619b232ec16cdf85a8c", "null-union Z33E source")
        req(nu["source_z33g_note_blob"] == "14c1661c5a3b1975474c1f983ed08b29c2150731", "null-union Z33G source")
        req(nu["union_ideal_regularity_upper_bound"] == 3, "null-union regularity")
        req("surjective for every n>=2" in nu["ambient_restriction_statement"], "null-union ambient surjectivity")
        req(nu["firewalls"]["new_ambient_lift_invariant"] is False, "null-union no new invariant")

        sr=d["retained_frontier"]["equigeneric_semiregularity_preflight"]
        req(sr["source_p6f_note_blob"] == "e89426128010ae97a10fbd908346f6cf07fff109", "semiregularity P6F source")
        req(sr["degree_on_E_formula"] == "deg(phi^*omega_S^(-1))=-112*l", "semiregularity degree")
        req(sr["h0_formula"] == "0" and sr["h1_formula"] == "112*l", "semiregularity cohomology")
        req(sr["target_dimension"] == 7, "semiregularity target dimension")
        req(sr["source_valid_injectivity_known"] is False, "semiregularity injectivity firewall")
        req(sr["route_disposition"] == "PARK_SOURCE_COMPLETE_DIRECTION_MISMATCH", "semiregularity parked")
        req("112l-dimensional" in sr["conclusion"], "semiregularity dimension conclusion")
        req(all(x is False for x in sr["firewalls"].values()), "semiregularity firewalls")

        cc=d["retained_frontier"]["compact_C8_etale_correspondence_preflight"]
        req("degree-56l" in cc["retained_input"], "compact correspondence degree")
        req(cc["route_disposition"] == "LIVE_ONE_SHALLOW_ARITHMETIC_PREFLIGHT", "compact correspondence live")
        req("compact uniformizing" in cc["current_question"], "compact correspondence question")
        req(all(x is False for x in cc["firewalls"].values()), "compact correspondence firewalls")

        statuses={x["name"]:x["status"] for x in cyc["candidates"]}
        req(statuses["null-union ambient hypersurface lift"] == "EQUIVALENT", "cycle null-union status")
        req(statuses["equigeneric conductor-normal semiregularity"] == "BLOCKED", "cycle semiregularity blocked")
        req(statuses["compact C8 etale-correspondence arithmetic double coset"] == "LIVE", "cycle compact correspondence live")
        req(cyc["cycle_fields"]["CYCLE_LIVE_CANDIDATES"] == 1, "cycle live count")
        req(cyc["cycle_fields"]["CYCLE_UNTESTED_CANDIDATES"] == 1, "cycle untested count")

        req(routing["finite_receiver_blind_scan_live"] is False, "finite receiver blind scan transition")
        req(routing["equigeneric_semiregularity_leaf_live"] is False, "semiregularity leaf closed")
        req(routing["equigeneric_semiregularity_route"] == "PARKED_SOURCE_COMPLETE_DIRECTION_MISMATCH", "semiregularity route closure")
        req(routing["null_union_ambient_lift_route"] == "CLOSED_SURJECTIVE_EQUIVALENT_TO_Z33G", "null-union route closed")
        req(routing["compact_C8_commensurator_candidate"] == "LIVE_ONE_SHALLOW_PREFLIGHT", "compact correspondence routing")
        req(routing["finite_receiver_scan_status"] == "NEW_THEOREM_PATTERN_ISOLATED", "finite receiver scan status")
        req(routing["cycle_exhaustive_view_audit_complete"] is True and routing["cycle_blind_rediscovery_complete"] is True, "cycle routing audit")
        req(d["next_obligation"]["active_leaf"] == "MB104-000707-C8-ETALE-CORRESPONDENCE-ARITHMETIC-PREFLIGHT", "post-audit active leaf")
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
