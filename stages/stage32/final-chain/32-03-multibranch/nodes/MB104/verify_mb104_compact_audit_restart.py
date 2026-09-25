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
        req(z12["current_main_observed"] == "e7fd29d24dd21e8529dbdb45b221a53f2cc21ed3", "Z12 current-main observation")
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
        cp=d["retained_frontier"]["conductor_pair_low_degree_pushforward_preflight"]
        req(cp["retained_input"]["delta_formula"] == "168*l^2+56*l", "pair compression delta")
        req(cp["retained_input"]["weighted_cut_lower_bound"] == "W>=84*l^2", "pair compression W lower bound")
        req(cp["double_point_conductor"]["different_degree_formula"] == "336*l^2+112*l", "double-point conductor degree")
        req(cp["double_point_conductor"]["ordered_twisted_pair_length_formula"] == "2*W", "ordered twisted pair length")
        for l in (1,2,3,7):
            req((3*l+1)*(112*l) == 336*l*l+112*l, "pair conductor degree replay")
            req(2*(168*l*l+56*l) == 336*l*l+112*l, "pair different equals 2 delta")
        rz=cp["residual_etale_trace_zero"]
        req(rz["torsion_relation"] == "L^2=O_C" and rz["degree"] == 0, "trace-zero 2-torsion")
        req(rz["normalization_pullback"] == "nu^*L=O_E because the pulled-back residual cover splits as E disjoint-union E", "trace-zero normalization split")
        tests={x["construction"]:x["result"] for x in cp["hostile_tests"]}
        req(tests["double-point scheme / conductor correspondence"] == "FAIL_QUADRATIC", "double-point quadratic no-go")
        req(tests["Fitting ideal of the full conductor quotient"] == "FAIL_CHI_BLIND_AND_QUADRATIC", "Fitting no-go")
        req(tests["determinant of cohomology / determinant of a torsion sheaf retaining the twisted locus"] == "FAIL_LENGTH_PRESERVING", "determinant no-go")
        req(tests["norm of the twisted effective zero-cycle"] == "FAIL_LENGTH_PRESERVING", "norm no-go")
        req(tests["trace-zero line / Prym character"] == "FAIL_WEIGHT_BLIND", "trace-zero weight blindness")
        req(tests["fixed-rank pushforward to E or P1"] == "FAIL_NO_FIXED_RANK_COMPRESSION", "fixed-rank pushforward no-go")
        req(cp["local_stress_test"]["weighted_pair_mass"] == "N", "pair local arbitrary contact")
        req(cp["low_genus_index3_refresh"]["status"] == "NO_REOPEN_TRIGGER", "low-genus index3 refresh")
        req(cp["route_disposition"] == "CLOSED_PAIR_CORRESPONDENCE_LOW_DEGREE_COMPRESSION_NO_GO", "pair compression closure")
        req(all(x is False for x in cp["firewalls"].values()), "pair compression firewalls")

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
        req(cc["arithmeticity_alone_degree_bound"] is False, "arithmeticity no degree bound")
        req(cc["unbounded_hecke_family_exists_in_ambient_arithmetic_commensurator"] is True, "ambient arithmetic Hecke unbounded")
        req(cc["required_G_centralizing_adapter_source_locked"] is False, "G-centralizing adapter wall")
        cmr=cc["size48_CM_reuse"]
        req(cmr["source_cm_adapter_blob"] == "24d48dfc50aca285d8808b95b2685b196511c666", "CM adapter source")
        req(cmr["source_size48_obstruction_blob"] == "5e1f7d4d6db10cd823532b1ac44290621ee2aa99", "size48 obstruction source")
        req(cmr["type_counts_nodes"] == [6,2,6], "mixed node types")
        req(cmr["supported_branches_by_type"] == ["48*l","16*l","48*l"], "branch counts by type")
        req(cmr["fix_Z_by_type"] == ["192*l","64*l","192*l"], "fixed points by type")
        req(cmr["quotient_genera"] == ["64*l+1","96*l+1","64*l+1"], "quotient genera")
        req(cmr["equal_degree_CM_isogeny_pair_available"] is False, "size48 CM nonportable")
        req(cc["route_disposition"] == "PARK_ARITHMETICITY_UNBOUNDED_AND_G_ADAPTER_MISSING", "compact correspondence parked")
        req(all(x is False for x in cc["firewalls"].values()), "compact correspondence firewalls")

        statuses={x["name"]:x["status"] for x in cyc["candidates"]}
        req(statuses["null-union ambient hypersurface lift"] == "EQUIVALENT", "cycle null-union status")
        req(statuses["equigeneric conductor-normal semiregularity"] == "BLOCKED", "cycle semiregularity blocked")
        req(statuses["compact C8 etale-correspondence arithmetic double coset"] == "BLOCKED", "cycle compact correspondence blocked")
        req(statuses["generic finite replacement receiver beyond graded module"] == "UNTESTED", "cycle generic fallback retained")
        req(cyc["cycle_fields"]["CYCLE_LIVE_CANDIDATES"] == 0, "cycle live count")
        req(cyc["cycle_fields"]["CYCLE_UNTESTED_CANDIDATES"] == 1, "cycle untested count")
        req(cyc["cycle_fields"]["CYCLE_PARKING_AUDIT_COMPLETE"] is True, "cycle parking audit")

        recv=d["retained_frontier"]["e2_gfixed_factor_pair_receiver_reopen"]
        req(recv["status"] == "POST_AUDIT_REOPENED_RESEARCH_CANDIDATE_FINITE_128_PAIR_WITH_ALGEBRAIC_5BIT_BASIS_ZERO_CREDIT", "finite receiver reopen status")
        req(recv["scope"]["source_archive_head"] == "ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11", "finite receiver archive head")
        fr=recv["finite_receiver"]
        req(fr["fixed_jacobian_structure"] == "(Z/2)^5" and fr["fixed_jacobian_size"] == 32, "finite receiver fixed Jacobian")
        req(fr["linearizable_kernel_structure"] == "(Z/2)^2" and fr["linearizable_kernel_size"] == 4, "finite receiver linearizable kernel")
        req(fr["ordered_factor_pairs_before_linearization"] == 1024 and fr["ordered_factor_pairs_after_linearization"] == 128, "finite receiver 1024 to 128")
        req(fr["l_independent"] is True, "finite receiver l independent")
        req(recv["reverse_adapter"]["all_pairs_excluded_implies_e2_carrier_excluded"] is True, "finite receiver reverse adapter")
        req(recv["reverse_adapter"]["e4_excluded_by_this_receiver"] is False and recv["reverse_adapter"]["mb104_closed_by_this_receiver_alone"] is False, "finite receiver scope firewall")
        req(recv["blockers"]["inherited_candidate_chain_hostile_audited"] is False, "finite receiver audit firewall")
        req(recv["blockers"]["five_tau_algebraic_theta_realization_materialized"] is False, "finite receiver theta wall")
        req(recv["blockers"]["pair_effectivity_support_test_materialized"] is False, "finite receiver pair-test wall")
        req(recv["blockers"]["determinant_factor_label_blind"] is True, "finite receiver determinant blindness")
        alg=recv["algebraic_fixed_2torsion_basis"]
        req(alg["status"] == "EXACT_PREAUDIT_ALGEBRAIC_BRANCH_PARITY_BASIS_CONSTRUCTED", "algebraic five-bit status")
        req(alg["source_model"]["note_blob"] == "d2e3056137360a9e15ae7c820088d2977a5eb137", "algebraic basis source model")
        req(alg["linearizable_kernel_basis"]["rank"] == 2 and alg["linearizable_kernel_basis"]["order"] == 4, "algebraic basis kernel")
        obs=alg["obstruction_matrix"]
        req(obs["mu_12"] == [1,0,0] and obs["mu_13"] == [0,1,0] and obs["mu_23"] == [0,0,1], "algebraic obstruction basis")
        req(obs["rank_over_F2"] == 3, "algebraic obstruction rank")
        req(alg["obstruction_group"] == "H^2(G,C*)=(Z/2)^3", "algebraic obstruction group")
        req(len(alg["obstruction_basis"]) == 3, "algebraic three obstruction lifts")
        req(all(x["divisor_identity"].startswith("div(h_") for x in alg["obstruction_basis"]), "algebraic divisor doubling")
        req(alg["independent_cas_replay"]["square_identities_verified"] is True and alg["independent_cas_replay"]["commutator_product_signs_verified"] is True, "algebraic CAS replay")
        req(alg["firewalls"]["historical_tau_termwise_identification"] is False and alg["firewalls"]["current_head_hostile_audited"] is False, "algebraic basis audit firewall")
        req(recv["blockers"]["equivalent_algebraic_five_bit_basis_materialized"] is True and recv["blockers"]["historical_tau_termwise_identification_materialized"] is False, "algebraic basis materialized")
        fp=recv["fixed_point_support_pruning"]
        req(fp["status"] == "EXACT_PREAUDIT_CONDITIONAL_FIXEDPOINT_CHARACTER_REDUCTION_128_TO_1_ZERO_CREDIT", "fixed-point pruning status")
        req(fp["group"]["node_types_total_each"] == 16, "fixed-point nodes per type")
        req(fp["group"]["active_support_type_counts"] == {"g1":7,"g2":7,"g3":0}, "fixed-point support counts")
        fc=fp["fixed_cell_lemma"]
        req(fc["branch_value_cells_per_type"] == 4 and fc["diagonal_nodes_per_cell"] == 4 and fc["total_nodes_per_type"] == 16, "fixed-point cell decomposition")
        obp=fp["obstruction_bit_pruning"]
        req(obp["nontrivial_restriction_forced_nodes_per_type"] == 8 and obp["support_capacity_per_used_type"] == 7, "obstruction eight-vs-seven")
        req(obp["pair_count_before"] == 128 and obp["pair_count_after"] == 16, "obstruction pair pruning")
        kp=fp["linearizable_kernel_pruning"]
        req(kp["nonzero_cell_linear_part_forced_nodes"] == 8 and kp["support_capacity_per_used_type"] == 7, "kernel eight-vs-seven")
        req(kp["g1_conclusion"] == "a=c=0" and kp["g2_conclusion"] == "b=d=0", "kernel bit kill")
        req(kp["pair_count_before"] == 16 and kp["pair_count_after"] == 1, "kernel pair pruning")
        req(fp["unique_survivor"]["A"] == "A_ref(l)=pi_H^*O_P1(7*l)" and fp["unique_survivor"]["B"] == "A_ref(l)=pi_H^*O_P1(7*l)", "unique factor pair")
        req(fp["finite_replay"]["replay_pass"] is True and fp["finite_replay"]["nodes_forced_from_nonzero_cell_character"] == 8, "fixed-point finite replay")
        req(all(x is False for x in fp["firewalls"].values()), "fixed-point credit firewalls")
        ew=recv["equivariant_section_effectivity_wall"]
        req(ew["character_section_dimensions"]["trivial"] == "7*l+1" and ew["character_section_dimensions"]["chi1chi2"] == "7*l-3", "equivariant section dimensions")
        req(ew["hdiag_invariant_product_section_dimension"] == "196*l^2-56*l+12" and ew["l1_dimension"] == 152, "equivariant invariant section dimension")
        req(ew["firewalls"]["e2_closed"] is False, "equivariant effectivity no closure")
        req(recv["finite_receiver"]["ordered_factor_pairs_after_fixed_point_support"] == 1, "finite receiver unique survivor count")
        req(recv["blockers"]["fixed_point_support_character_test_materialized"] is True and recv["blockers"]["remaining_unique_pair_exact_support_singularity_test_materialized"] is False, "unique-pair next wall")
        req("4*(7*l+1)" in recv["blockers"]["determinant_blind_reason"], "finite receiver determinant exponent")
        req(recv["cross_lane_alignment"]["mb_fib_head_observed"] == "5760ede53fff75c0d796ccac280418c112028361", "finite receiver MB-FIB alignment")
        req(recv["cross_lane_alignment"]["semantic_match"] is True and recv["cross_lane_alignment"]["audited_B2_handoff_available"] is False, "finite receiver B2 firewall")
        req(all(x is False for x in recv["firewalls"].values()), "finite receiver credit firewalls")
        park=d["retained_frontier"]["parking_reopen_contract"]
        req(park["status"] == "POST_AUDIT_RESEARCH_REOPENED_FINITE_E2_RECEIVER_CANDIDATE_ZERO_CREDIT", "parking/reopen status")
        req(len(park["reopen_triggers"]) >= 6, "parking reopen triggers")
        req(park["reopen_event"]["trigger"] == "new finite l-independent receiver with reverse adapter to carrier nonexistence", "finite receiver reopen event")
        req("size48 inert-7 CM obstruction on the 000707 mixed-type support" in park["must_not_reopen_without_trigger"], "CM no-reopen firewall")
        req("conductor pair norm/determinant/Fitting/trace-zero low-degree compression without a new marked lift" in park["must_not_reopen_without_trigger"], "pair-compression anti-loop firewall")
        chk=park["last_reopen_check"]
        req(chk["checked_at_jst"] == "2026-09-24T22:34:09+09:00", "reopen refresh date")
        req(chk["current_main_observed"] == "e7fd29d24dd21e8529dbdb45b221a53f2cc21ed3", "reopen current main")
        req(chk["cross_lane_checked"]["head_observed"] == "5760ede53fff75c0d796ccac280418c112028361", "reopen MB-FIB head")
        req(chk["current_main_change_since_prior_check"] is False, "reopen main unchanged")
        req(chk["current_main_delta"]["current_repository_main"] == "e7fd29d24dd21e8529dbdb45b221a53f2cc21ed3", "reopen V48 main delta")
        req(chk["current_main_delta"]["mb_reopen_semantic_adapter"] is False, "reopen V48 semantic mismatch")
        req(chk["branch_vs_current_main"]["status"] == "DIVERGED" and chk["branch_vs_current_main"]["rebase_performed"] is False, "reopen divergence no rebase")
        req(chk["cross_lane_checked"]["status_observed"] == "GEN26_ADAPTIVE_X58_CONCURRENCY8_COLD__LIVE_OVERLAP_GATE_REPAIR_READY__CI_BLOCKED_BY_V48_MAIN_DIVERGENCE__ZERO_CREDIT", "reopen MB-FIB status")
        req(chk["cross_lane_checked"]["current_ci_status"] == "NOT_LAUNCHED_PR_CONFLICT", "reopen MB-FIB CI conflict")
        req(chk["cross_lane_checked"]["current_heavy_execution_authorized"] is False, "reopen MB-FIB heavy firewall")
        req(chk["cross_lane_checked"]["latest_pass_exact_head"] == "c771af0b5076460860a116abecce0288d62da011", "reopen MB-FIB prior pass")
        req(chk["external_refresh"]["ancillary_inventory_live_confirmed"] is True, "reopen BTVA ancillary inventory")
        req(chk["external_refresh"]["general_m_support_specific_interface_obtained"] is False and chk["external_refresh"]["reopen_trigger_satisfied"] is False, "reopen BTVA trigger remains false")
        req(chk["cross_lane_checked"]["exact_missing_direct_datum"].startswith("branch-specific conductor transition"), "reopen missing conductor datum")
        req(chk["trigger_matches"]["finite_l_independent_receiver_with_reverse_adapter"] is True, "finite receiver trigger match")
        req(sum(1 for x in chk["trigger_matches"].values() if x is True) == 1, "only finite receiver trigger matched")
        req(chk["disposition"] == "REOPEN_RESEARCH_FINITE_E2_RECEIVER_ZERO_CREDIT", "finite receiver reopen disposition")
        req(chk["firewalls"]["research_leaf_reopened"] is True and chk["firewalls"]["receiver_credit"] is False, "finite receiver reopen credit firewall")

        req(routing["finite_receiver_blind_scan_live"] is False, "finite receiver blind scan transition")
        req(routing["equigeneric_semiregularity_leaf_live"] is False, "semiregularity leaf closed")
        req(routing["equigeneric_semiregularity_route"] == "PARKED_SOURCE_COMPLETE_DIRECTION_MISMATCH", "semiregularity route closure")
        req(routing["null_union_ambient_lift_route"] == "CLOSED_SURJECTIVE_EQUIVALENT_TO_Z33G", "null-union route closed")
        req(routing["compact_C8_commensurator_candidate"] == "PARKED_ARITHMETICITY_UNBOUNDED_G_ADAPTER_MISSING", "compact correspondence routing")
        req(routing["conductor_pair_low_degree_pushforward_route"] == "CLOSED_QUADRATIC_OR_WEIGHT_BLIND_NO_GO", "pair compression routing")
        req(routing["finite_receiver_scan_status"] == "REOPENED_E2_GFIXED_UNIQUE_PAIR_AFTER_FIXEDPOINT_SUPPORT_ZERO_CREDIT", "finite receiver scan reopened")
        req(routing["e2_gfixed_128_pair_receiver_live"] is True and routing["e2_gfixed_128_pair_receiver_audited"] is False, "finite receiver routing audit firewall")
        req(routing["e2_gfixed_128_pair_count"] == 128, "finite receiver routing historical pair count")
        req(routing["e2_gfixed_support_character_survivor_count"] == 1, "finite receiver unique survivor routing")
        req(routing["e2_gfixed_plain_equivariant_effectivity_closes"] is False, "finite receiver effectivity wall")
        req(routing["mb104_parking_audit_complete"] is True and routing["mb104_parked_await_new_adapter"] is False, "MB104 finite receiver reopen")
        req(routing["cycle_exhaustive_view_audit_complete"] is True and routing["cycle_blind_rediscovery_complete"] is True, "cycle routing audit")
        req(routing["e2_gfixed_algebraic_5bit_basis_materialized"] is True and routing["e2_gfixed_historical_tau_termwise_identified"] is False, "algebraic five-bit routing")
        sp=d["retained_frontier"].get("e2_unique_factor_pair_singular_passport")
        if sp is None:
            req(d["next_obligation"]["active_leaf"] == "MB104-000707-E2-UNIQUE-FACTOR-PAIR-SINGULAR-PASSPORT-TEST", "post-audit active leaf")
        else:
            req(sp["status"] == "EXACT_PREAUDIT_UNIQUE_PAIR_SUPPORTED_PRODUCT_PASSPORT_COMPATIBILITY_ZERO_CREDIT", "unique-pair passport status")
            req(sp["support_mask"] == "000707000f0f" and sp["case"] == "e=2", "unique-pair passport scope")
            sl=sp["source_locks"]
            req(sl["product_linearization_note_blob"] == "2c2db567db6a3c33762b2ff3d7f39f885a95b974", "passport product-linearization lock")
            req(sl["rosati_zero_note_blob"] == "24cc729070ab685491fd2659d970da1a9f415891", "passport Rosati lock")
            req(sl["external_product_picard_note_blob"] == "dc2def9e4d0148aa3146a034a2ce0ef331206a29", "passport external-product lock")
            req(sl["etale_basechange_passport_note_blob"] == "d4e5c3b9c598299114f983594be1fac1b01d24d7", "passport etale-basechange lock")
            req(sl["common_h_factor_line_note_blob"] == "1e121116c1591e3b3d9f748f306151ab0e89b580", "passport common-H line lock")
            req(sl["projective_conductor_note_blob"] == "69b3e039ebc967c84f7c64d4946a114f09d07fba", "passport projective-conductor lock")
            req(sl["residual_node_orbit_note_blob"] == "dbfea5a4f62b1388c9810c37ad867076ed4dca6e", "passport residual-node lock")
            req(sp["unique_pair"] == "A=B=pi_H^*O_P1(7*l)", "unique factor pair")
            loc=sp["supported_product_local"]
            req(loc["carrier_different_coefficient_per_E_branch"] == "4*l", "carrier different coefficient")
            req(loc["H_quotient_ramification_coefficient_per_Z_branch"] == 1, "H quotient ramification coefficient")
            req(loc["dualizing_identity"] == "R_p+Delta_Z+I_(Z,TZ)=p^*Delta_C", "local dualizing identity")
            req(loc["branch_identity"] == "c_i+I_i=8*l-1", "local branch identity")
            req(loc["internal_lower_bound"] == "c_i>=r-1", "internal lower bound")
            req(loc["translate_lower_bound"] == "I_i>=8*l-r", "translate lower bound")
            req(loc["forced_equalities"] == ["c_i=r-1","I_i=8*l-r"], "forced supported equalities")
            req(loc["conclusion"] == "all supported product branches are internally ordinary/transverse and meet the residual translate transversely", "supported transversality conclusion")
            # The two lower bounds exactly saturate the pulled-back carrier different.
            for ll in (1,2,3,7):
                for rr in (0,1,2,4*ll,8*ll-2,8*ll):
                    if 0 <= rr <= 8*ll:
                        req((rr-1)+(8*ll-rr) == 8*ll-1, "local saturation arithmetic")
            sd=sp["supported_delta"]
            req(sd["per_box_node_formula"] == "2*a_j^2+32*l^2-8*l, a_j=x_j-4*l", "supported delta per-node formula")
            req(sd["all_14_formula"] == "448*l^2-112*l+2*sum(a_j^2)", "supported delta total formula")
            req(sd["interior_formula"] == "336*l^2+224*l-2*sum(a_j^2)", "interior delta formula")
            req(sd["even_l_bridge"] == "l=2*m,a_j=2*b_j => delta_Z,int=4*(336*m^2+112*m-2*Q)=4*delta_same", "even-l energy bridge")
            for ll in (1,2,5):
                for xx in range(0,8*ll+1,2):
                    aa=xx-4*ll
                    lhs=2*(xx*(xx-1)//2)+2*((8*ll-xx)*(8*ll-xx-1)//2)
                    rhs=2*aa*aa+32*ll*ll-8*ll
                    req(lhs == rhs, "supported product delta replay")
            ci=sp["translate_intersection"]
            req(ci["total_formula"] == "Zbar.TZbar=1568*l^2", "translate total intersection")
            req(ci["supported_formula"] == "896*l^2-4*sum(a_j^2)", "translate supported intersection")
            req(ci["interior_formula"] == "672*l^2+4*sum(a_j^2)", "translate interior intersection")
            lb=sp["conductor_half_line_bridge"]
            req(lb["M_i_degree"] == "28*l", "factor pencil degree")
            req(lb["M_i_fourth_power"] == "M_i^4=H_E", "factor pencil fourth power")
            req(lb["factor_square_relation"] == "M_1^2=M_2^2", "factor square relation")
            req(lb["K_C8"] == "pi_H^*O_P1(2)", "C8 canonical pullback")
            req(lb["Delta_Z_line"] == "O_Z(Delta_Z)=p^*(M_1^(7*l) tensor M_2^(7*l+2))", "product different half-line")
            req(lb["half_square"] == "L_Delta^2=H_E^(7*l+1)=O_E(Delta_C)", "carrier different square-root identity")
            req(lb["degree_L_Delta"] == "392*l^2+56*l", "half-line degree")
            req(lb["degree_Delta_Z"] == "1568*l^2+224*l", "product different degree")
            for ll in (1,2,5,9):
                req((14*ll+2)*28*ll == 392*ll*ll+56*ll, "half-line degree replay")
                req(4*(392*ll*ll+56*ll) == 1568*ll*ll+224*ll, "product different degree replay")
            req(sp["result"] == "the unique factor pair survives the exact supported-node multiplicity/different passport; supported higher-contact is forced absent on the product surface, and the conductor half-line is exactly compatible", "unique-pair supported passport result")
            req(all(v is False for v in sp["firewalls"].values()), "unique-pair passport firewalls")
            req(routing["e2_unique_pair_supported_product_passport_exact"] is True, "unique-pair supported passport routing")
            req(routing["e2_unique_pair_supported_product_passport_closes"] is False, "unique-pair supported passport no closure")
            req(routing["e2_unique_pair_supported_higher_contact_live"] is False, "supported higher contact closed")
            req(routing["e2_unique_pair_conductor_half_line_exact"] is True, "conductor half-line exact")
            fa=d["retained_frontier"].get("e2_unique_pair_saturated_factor_fiber_abel")
            if fa is None:
                req(d["next_obligation"]["active_leaf"] == "MB104-000707-E2-UNIQUE-PAIR-INTERIOR-CONDUCTOR-OR-FIB-RESTRICTION", "post-passport active leaf")
            else:
                req(fa["status"] == "EXACT_PREAUDIT_UNIQUE_PAIR_SATURATED_FACTOR_FIBER_ABEL_MOD8_REFINEMENT_ZERO_CREDIT", "factor-fiber Abel status")
                req(fa["support_mask"] == "000707000f0f" and fa["case"] == "e=2", "factor-fiber Abel scope")
                req(fa["unique_pair"] == "A=B=pi_H^*O_P1(7*l)", "factor-fiber Abel unique pair")
                fsl=fa["source_locks"]
                req(fsl["intermediate_h_model_blob"] == "d2e3056137360a9e15ae7c820088d2977a5eb137", "factor-fiber H-model lock")
                req(fsl["residual_node_orbit_note_blob"] == "dbfea5a4f62b1388c9810c37ad867076ed4dca6e", "factor-fiber node-orbit lock")
                req(fsl["etale_basechange_passport_note_blob"] == "d4e5c3b9c598299114f983594be1fac1b01d24d7", "factor-fiber etale-passport lock")
                req(fsl["external_product_picard_note_blob"] == "dc2def9e4d0148aa3146a034a2ce0ef331206a29", "factor-fiber product-Picard lock")
                req(fsl["picard_descent_parity_certificate_blob"] == "7621932b87a7558d473bc99a09b46bcb04a433a0", "factor-fiber parity lock")
                req(fsl["zero_quartic_torsion_note_blob"] == "544ded0d132dcf4dca0a5a3d52925a88c8c461e2", "factor-fiber old torsion lock")
                req(fsl["low_bidegree_capacity_note_blob"] == "60cd43c94b7d1ab2992f3cd502d1e49ac2c972e6", "factor-fiber capacity lock")

                ell=fa["bielliptic_quotients"]
                req(ell["g1"]["model"] == "Y^2=X^3-X" and ell["g1"]["map"] == "X=u+r^2/2; Y=r*X", "g1 elliptic model")
                req(ell["g2"]["model"] == "Y^2=X^3+X" and ell["g2"]["map"] == "X=v+r^2/2; Y=r*X", "g2 elliptic model")
                req(ell["ramified_pullback_pic0_injective"] is True, "ramified quotient Pic0 injection")
                req(ell["fixed_point_abel_group"] == "(Z/4)^2", "fixed-point Abel group")

                cg=fa["abel_congruences"]
                req(cg["x_mod8"] == [
                    "x0-x1+x2-x3+2*(x25-x24)=4*l mod 8",
                    "x24+x25+x26+2*(x2-x3)=4*l mod 8",
                    "2*(x8+x9)-x32-x34+x33=4*l mod 8",
                    "x8-x9+x10-x11+2*x34=4*l mod 8",
                ], "four factor-fiber mod8 congruences")
                req(cg["strictly_strengthens_old_mod4"] is True, "factor-fiber Abel stronger than old mod4")
                req(cg["balanced_allocation_requires_l_even"] is True, "balanced odd-l exclusion")

                def ff_residues_from_x(xx,ll):
                    yy={k:v//2 for k,v in xx.items()}
                    return [
                        (yy[0]-yy[1]+yy[2]-yy[3]+2*(yy[25]-yy[24])-2*ll) % 4,
                        (yy[24]+yy[25]+yy[26]+2*(yy[2]-yy[3])-2*ll) % 4,
                        (2*(yy[8]+yy[9])-yy[32]-yy[34]+yy[33]-2*ll) % 4,
                        (yy[8]-yy[9]+yy[10]-yy[11]+2*yy[34]-2*ll) % 4,
                    ]

                support_order=[0,1,2,3,8,9,10,11,24,25,26,32,33,34]
                old_x=dict(zip(support_order,[8,0,0,48,42,76,2,80,0,0,0,0,2,78]))
                req(ff_residues_from_x(old_x,10) == [0,0,0,2], "old m5 capacity witness killed by new Abel bit")

                repl=fa["replacement_endpoint_witness"]
                req(repl["m"] == 5 and repl["l"] == 10, "replacement endpoint degree")
                xx=dict(zip(support_order,repl["x"]))
                bb=dict(zip(support_order,repl["b"]))
                req(repl["x"] == [8,0,0,48,38,78,4,80,0,0,0,2,0,78], "replacement endpoint x")
                req(repl["b"] == [-16,-20,-20,4,-1,19,-18,20,-20,-20,-20,-19,-20,19], "replacement endpoint b")
                req(all(xx[j] == 2*(bb[j]+20) for j in support_order), "replacement x/b conversion")
                req(bb[0]-bb[1]+bb[2]-bb[3]-bb[24]+bb[25]-bb[26] == 0, "replacement Q0 centered saturation")
                req(sum(bb[j] for j in (8,9,10,11,32,33,34)) == 0, "replacement Q1 centered saturation")
                Q=sum(v*v for v in bb.values())
                req(Q == 4480 == 168*25+56*5, "replacement endpoint energy")
                req(336*25+112*5-2*Q == 0, "replacement delta_same endpoint")
                req(ff_residues_from_x(xx,10) == [0,0,0,0], "replacement satisfies four Abel congruences")

                # New congruences do not empty the even-l adaptive thin shell.
                q0nodes=(0,1,2,3,24,25,26)
                q1nodes=(8,9,10,11,32,33,34)
                for mm in (1,2,3,4,5,6,7):
                    b2={}
                    for j,v in zip(q0nodes,(-4,4,3,-3,4,3,-3)):
                        b2[j]=mm*v
                    for j,v in zip(q1nodes,(-4,-4,3,3,-4,3,3)):
                        b2[j]=mm*v
                    if mm % 2:
                        b2[10]-=1
                        b2[11]+=1
                    ll=2*mm
                    x2={j:2*(b2[j]+4*mm) for j in support_order}
                    req(all(0 <= x2[j] <= 8*ll for j in support_order), "thin-shell Abel witness bounds")
                    req(b2[0]-b2[1]+b2[2]-b2[3]-b2[24]+b2[25]-b2[26] == 0, "thin-shell Abel Q0 saturation")
                    req(sum(b2[j] for j in q1nodes) == 0, "thin-shell Abel Q1 saturation")
                    req(ff_residues_from_x(x2,ll) == [0,0,0,0], "thin-shell Abel congruences")
                    q2=sum(v*v for v in b2.values())
                    want=168*mm*mm+(2 if mm%2 else 0)
                    req(q2 == want, "thin-shell Abel energy family")
                    ds=336*mm*mm+112*mm-2*q2
                    req(ds == (112*mm-4 if mm%2 else 112*mm), "thin-shell Abel delta family")
                    req(0 <= ds <= 224*mm-12, "thin-shell Abel witness remains in shell")

                masses=repl["special_masses"]
                req(sum(masses.values()) == 1120, "replacement special mass")
                req(repl["capacity_replay"] == {
                    "max_fibre_mass":280,
                    "fibre_capacity":280,
                    "max_11_mass":550,
                    "capacity_11":560,
                    "max_12_mass":624,
                    "capacity_12":840,
                    "max_21_mass":636,
                    "capacity_21":840,
                }, "replacement raw capacity replay")
                tsi=fa["two_slice_interpolation"]
                req(tsi["H_section_decomposition"] == [
                    "V0=H0(P1,O(7*l)), dim=7*l+1",
                    "Vu=u*H0(P1,O(7*l-2)), dim=7*l-1",
                    "Vv=v*H0(P1,O(7*l-2)), dim=7*l-1",
                    "Vuv=u*v*H0(P1,O(7*l-4)), dim=7*l-3",
                ], "two-slice H-section decomposition")
                req(tsi["Hdiag_invariant_dimension"] == "196*l^2-56*l+12", "two-slice invariant dimension")
                req(tsi["horizontal_image"] == "V0+Vu, dimension 14*l", "two-slice horizontal image")
                req(tsi["vertical_image"] == "V0+Vv, dimension 14*l", "two-slice vertical image")
                req(tsi["joint_image"] == "all pairs (s_h,s_v) with s_h(z_g2)=s_v(w_g1), dimension 28*l-1", "two-slice joint image")
                req(tsi["kernel_dimension"] == "196*l^2-84*l+13", "two-slice kernel dimension")
                for ll in (1,2,3,7):
                    d0=7*ll+1
                    du=7*ll-1
                    dv=7*ll-1
                    duv=7*ll-3
                    req(d0*d0+du*du+dv*dv+duv*duv == 196*ll*ll-56*ll+12, "two-slice invariant dimension replay")
                    req((196*ll*ll-56*ll+12)-(28*ll-1) == 196*ll*ll-84*ll+13, "two-slice kernel replay")
                    req(196*ll*ll-84*ll+13 > 0, "two-slice positive kernel")
                req(tsi["saturated_divisor_pair_simultaneously_realizable_as_Hdiag_section"] is True, "two-slice simultaneous section realization")
                req(tsi["irreducibility_or_common_etale_normalization_proved"] is False, "two-slice geometry firewall")
                req(tsi["conclusion"] == "plain Hdiag section existence with the exact two saturated support slices is automatically compatible once the four Abel congruences hold; this section-space route is closed as a standalone obstruction", "two-slice conclusion")
                req(fa["result"] == "unique-pair saturated factor fibers impose four new mod-8 allocation congruences and exclude the previous m=5 endpoint witness, but a replacement delta_same=0 endpoint survives every retained raw low-bidegree capacity", "factor-fiber Abel result")
                req(all(v is False for v in fa["firewalls"].values()), "factor-fiber Abel firewalls")
                req(routing["e2_unique_pair_factor_fiber_abel_exact"] is True, "factor-fiber Abel routing")
                req(routing["e2_unique_pair_factor_fiber_abel_new_mod8_constraints"] == 4, "factor-fiber Abel constraint count")
                req(routing["e2_unique_pair_factor_fiber_abel_closes"] is False, "factor-fiber Abel no closure")
                req(routing["e2_unique_pair_old_capacity_witness_survives"] is False, "old capacity witness removed")
                req(routing["e2_unique_pair_replacement_capacity_endpoint_survives"] is True, "replacement endpoint retained")
                req(routing["e2_unique_pair_supported_section_interpolation_exact"] is True, "supported section interpolation exact")
                req(routing["e2_unique_pair_supported_section_effectivity_closes"] is False, "supported section interpolation no closure")
                req(routing["e2_unique_pair_supported_section_route"] == "CLOSED_EXACT_SURJECTIVE_TWO_SLICE_INTERPOLATION_NO_GO", "supported section route closed")
                my=d["retained_frontier"].get("e2_unique_pair_miyaoka_energy_bound")
                if my is None:
                    req(d["next_obligation"]["active_leaf"] == "MB104-000707-E2-UNIQUE-PAIR-INTERIOR-REALIZATION-AFTER-FIBER-ABEL", "post-Abel active leaf")
                else:
                    req(my["status"] == "EXACT_PREAUDIT_MIYAOKA_INTERMEDIATE_RESOLUTION_ENERGY_BOUND_ZERO_CREDIT", "Miyaoka energy-bound status")
                    req(my["support_mask"] == "000707000f0f" and my["case"] == "e=2", "Miyaoka energy-bound scope")
                    src=my["source_locks"]
                    req(src["a1_lift_energy_note_blob"] == "3fb4152c35b88160f36730fac941f542566664a8", "Miyaoka A1-energy source lock")
                    req(src["product_linearization_note_blob"] == "2c2db567db6a3c33762b2ff3d7f39f885a95b974", "Miyaoka product source lock")
                    ext=src["external_theorem"]
                    req(ext["author"] == "Yoichi Miyaoka" and ext["year"] == 2008, "Miyaoka theorem attribution")
                    req(ext["doi"] == "10.2977/PRIMS/1210167331" and ext["locator"] == "Theorem 1.3(i),(ii)", "Miyaoka theorem locator")
                    req(ext["restated_as"] == "Bauer et al., Negative curves on algebraic surfaces, Theorem 2.4", "Miyaoka restatement lock")
                    req(ext["formula_g1"] == "2*(K.C)^2 <= (3*c2-K^2)*(C^2+3*K.C)", "Miyaoka g=1 formula")

                    surf=my["intermediate_resolution"]
                    req(surf["surface"] == "S=minimum resolution of X_H=(C8 x C8)/H_diag", "Miyaoka surface")
                    req(surf["K_P_square"] == 128 and surf["e_P"] == 64, "product surface invariants")
                    req(surf["H_order"] == 4 and surf["fixed_points_diag_g1"] == 64 and surf["fixed_points_diag_g2"] == 64 and surf["fixed_points_diag_g1g2"] == 0, "H fixed-point counts")
                    req(surf["quotient_euler"] == 48 and surf["A1_count"] == 64, "quotient singularity count")
                    req(surf["c2_S"] == 112 and surf["K_S_square"] == 32 and surf["kappa_S"] == 2, "resolved surface invariants")
                    req(surf["miyaoka_a"] == 304, "Miyaoka surface a")
                    req((64+64+64+0)//4 == 48, "quotient Euler replay")
                    req(48+64 == 112, "A1 resolution Euler replay")
                    req(128//4 == 32, "crepant K-square replay")
                    req(3*112-32 == 304, "Miyaoka a replay")

                    cur=my["curve"]
                    req(cur["curve"] == "C1=strict transform of Gamma=Zbar/H_diag", "Miyaoka curve")
                    req(cur["geometric_genus"] == 1, "Miyaoka genus")
                    req(cur["K_dot_C1"] == "112*l", "Miyaoka canonical degree")
                    req(cur["C1_square"] == "168*l^2-sum(a_j^2)", "Miyaoka self intersection")
                    req(cur["hypothesis_KC_gt_3g_minus_3"] is True, "Miyaoka positive canonical degree hypothesis")
                    req(cur["bound"] == "19*sum(a_j^2)<=1624*l^2+6384*l", "Miyaoka allocation bound")
                    for ll in (1,2,5,10):
                        # 2*(112l)^2 <= 304*(168l^2-A+336l)
                        # is exactly 19*A <= 1624*l^2+6384*l after division by 16.
                        lhs_const=2*(112*ll)**2
                        rhs_const=304*(168*ll*ll+336*ll)
                        req((rhs_const-lhs_const)//16 == 1624*ll*ll+6384*ll, "Miyaoka coefficient replay")

                    ev=my["even_l_reduction"]
                    req(ev["substitution"] == "l=2*m, a_j=2*b_j, Q=sum(b_j^2)", "Miyaoka even-l substitution")
                    req(ev["bound"] == "19*Q<=1624*m^2+3192*m", "Miyaoka Q bound")
                    req(ev["delta_same_lower_bound"] == "delta_same>=(3136/19)*m^2-224*m", "Miyaoka delta lower bound")
                    req(ev["adaptive_shell_lower"] == "Q>=168*m^2-56*m+6", "Miyaoka adaptive shell lower")
                    req(ev["combined_polynomial"] == "1568*m^2-4256*m+114<=0", "Miyaoka shell polynomial")
                    p=lambda mm:1568*mm*mm-4256*mm+114
                    req(p(1) <= 0 and p(2) <= 0 and p(3) > 0, "Miyaoka shell m1/m2 cutoff")
                    req(all(p(mm+1)>p(mm) for mm in range(1,12)), "Miyaoka shell polynomial increasing after m1")
                    req(ev["integer_high_energy_shell_residual_m"] == [1,2], "Miyaoka finite shell residue")
                    req(ev["high_energy_shell_excluded_for_m_ge"] == 3, "Miyaoka large-m shell closure")

                    oldep=my["old_replacement_endpoint"]
                    req(oldep["m"] == 5 and oldep["Q"] == 4480, "Miyaoka old endpoint")
                    req(19*oldep["Q"] > 1624*25+3192*5, "Miyaoka excludes old endpoint")
                    req(oldep["excluded_by_miyaoka_bound"] is True, "Miyaoka old endpoint disposition")

                    small=my["finite_shell_residue"]
                    req([w["m"] for w in small] == [1,2], "Miyaoka finite residue degrees")
                    for w in small:
                        mm=w["m"]
                        bb=w["b"]
                        req(len(bb)==14 and sum(x*x for x in bb)==w["Q"], "Miyaoka finite witness energy")
                        req(19*w["Q"] <= 1624*mm*mm+3192*mm, "Miyaoka finite witness bound")
                        req(w["abel_residues"] == [0,0,0,0], "Miyaoka finite witness Abel")
                        req(w["passes_retained_raw_low_bidegree_capacity"] is True, "Miyaoka finite witness raw capacity")
                    req(small[0]["capacity_maxima"] == {"fibre":56,"11":66,"12":96,"21":100}, "Miyaoka m1 capacity replay")
                    req(small[1]["capacity_maxima"] == {"fibre":112,"11":128,"12":192,"21":192}, "Miyaoka m2 capacity replay")

                    req(my["result"] == "Miyaoka's curve inequality removes the entire adaptive high-energy shell for even l=2m with m>=3 and excludes the former m=5 replacement endpoint; it does not exclude e=2 because bulk allocations remain and m=1,2 shell witnesses survive the retained raw capacities", "Miyaoka result")
                    req(all(v is False for v in my["firewalls"].values()), "Miyaoka credit firewalls")
                    req(routing["e2_unique_pair_miyaoka_surface_bound_exact"] is True, "Miyaoka routing exact")
                    req(routing["e2_unique_pair_miyaoka_high_energy_shell_m_ge_3_closed"] is True, "Miyaoka routing shell closure")
                    req(routing["e2_unique_pair_miyaoka_e2_closes"] is False, "Miyaoka routing no e2 closure")
                    req(routing["e2_unique_pair_miyaoka_high_energy_shell_residual_m"] == [1,2], "Miyaoka routing finite residue")
                    req(routing["e2_unique_pair_replacement_endpoint_survives_current_constraints"] is False, "Miyaoka old endpoint no longer current")

                    ob=d["retained_frontier"].get("e2_unique_pair_etale_immersion_orbifold_bmy")
                    if ob is None:
                        req(d["next_obligation"]["active_leaf"] == "MB104-000707-E2-UNIQUE-PAIR-MIYAOKA-PRUNED-INTERIOR-REALIZATION", "post-Miyaoka active leaf")
                    else:
                        req(ob["status"] == "EXACT_PREAUDIT_HYPERBOLIC_FIRST_JET_TRANSVERSALITY_LANGER_M2_HIGH_SHELL_CLOSED_ZERO_CREDIT", "orbifold-BMY status")
                        req(ob["support_mask"] == "000707000f0f" and ob["case"] == "e=2", "orbifold-BMY scope")
                        osl=ob["source_locks"]
                        req(osl["joint_pair_birationality_note_blob"] == "53608cb51aa49ccde1603b1cb1d136ea497b2324", "orbifold-BMY birationality source")
                        req(osl["etale_basechange_passport_note_blob"] == "d4e5c3b9c598299114f983594be1fac1b01d24d7", "orbifold-BMY etale source")
                        req(osl["residual_node_orbit_note_blob"] == "dbfea5a4f62b1388c9810c37ad867076ed4dca6e", "orbifold-BMY node-orbit source")
                        req(osl["product_linearization_note_blob"] == "2c2db567db6a3c33762b2ff3d7f39f885a95b974", "orbifold-BMY product source")
                        hyp=osl["hyperbolic_covering_first_jet"]
                        req("local Poincare isometry" in hyp["theorem"] and "value and differential" in hyp["theorem"], "hyperbolic first-jet source statement")
                        req(hyp["source_1_url"] == "https://link.springer.com/article/10.1007/s10231-022-01189-8", "hyperbolic covering source URL")
                        ext=osl["external_theorem"]
                        req(ext["author"] == "Adrian Langer" and ext["year"] == 2003, "Langer attribution")
                        req(ext["doi"] == "10.1112/S0024611502013874", "Langer DOI")
                        req(ext["locators"] == ["Theorem 0.1","(0.2.3)","Theorem 0.3"], "Langer theorem locators")
                        req(ext["theorem_03_formula"] == "(K_X+D)^2 <= 3*(c2(X)+sum a_i*(2g(D_i)-2)+sum_P(r_P-m_P+m_P^2/4))", "Langer formula")
                        lct=osl["external_lct_bound"]
                        req(lct["statement"] == "1/mult_P(C) <= lct_P(S,C) <= 2/mult_P(C) for a reduced plane curve germ on a smooth surface", "safe lct multiplicity bound")
                        req(lct["doi"] == "10.1017/S0017089525100827", "safe lct source DOI")

                        imm=ob["etale_immersion"]
                        req(imm["f1_etale"] is True and imm["f2_etale"] is True, "both product projections etale")
                        req(imm["normalization_map_birational"] is True and imm["normalization_map_immersive"] is True, "birational branchwise immersion")
                        req(imm["each_normalization_branch_smooth"] is True, "smooth normalization branches")
                        req(imm["unibranch_cusp_possible"] is False, "no unibranch cusp")
                        req(imm["pairwise_transversality_claimed"] is True, "hyperbolic first-jet transversality claim")
                        req(imm["safe_consequence"] == "every branch is smooth and any two distinct branches at an interior singular point are transverse; hence every interior singularity is an ordinary multiple point", "hyperbolic immersion consequence")
                        req(len(imm["hyperbolic_first_jet_argument"]) == 6, "hyperbolic first-jet proof steps")

                        orb=ob["interior_H_orbit"]
                        req(orb["H_order"] == 4 and orb["nontrivial_fixed_types"] == ["g1","g2"], "interior orbit H data")
                        req(orb["g1g2_fixed_point_free"] is True, "interior orbit free product involution")
                        req(orb["unsupported_H_fixed_points_avoided_by_support_mask"] is True, "support mask excludes other H-fixed points")
                        req(orb["interior_singularity_orbit_size"] == 4, "interior singularity orbit size")
                        req(orb["per_orbit_delta_lower"] == "4*binom(mult,2)", "interior orbit multiplicity charge")

                        num=ob["product_pair_numbers"]
                        req(num == {
                            "c2_P":64,
                            "K_P_square":128,
                            "geometric_genus":"112*l+1",
                            "K_dot_Zbar":"448*l",
                            "Zbar_square":"1568*l^2",
                            "delta_total":"784*l^2+112*l",
                            "supported_branch_incidence":"224*l",
                            "delta_interior":"4*(336*m^2+112*m-2*Q)",
                            "langer_local_quadratic_bracket_upper":"8960*m^2+1792*m-16*Q",
                        }, "orbifold-BMY product numerics")

                        lg=ob["langer_reduction"]
                        req(lg["boundary"] == "D=alpha*Zbar on P=C8 x C8", "Langer boundary")
                        req(lg["lc_sufficient_check"] == "alpha<=1/mult_P(Zbar) at every singular point, using the general lower bound lct_P(Zbar)>=1/mult_P(Zbar)", "Langer safe lc check")
                        req(lg["general_local_term"] == "alpha*(branches-mult)+(alpha^2/4)*mult^2", "Langer general local term")
                        req(lg["interior_local_upper"] == "alpha*(branches-mult)+(alpha^2/4)*mult^2 <= alpha^2*delta_P", "interior local delta upper")
                        req(lg["supported_ordinary_passport_used"] is True, "supported ordinary passport")
                        req(lg["supported_local_quadratic_identity"] == "sum_supp mult^2=2*delta_supp+R_supp", "supported ordinary identity")
                        req(lg["global_upper"] == "(K_P+alpha*Zbar)^2 <= 3*(64+alpha*(2*g(Z)-2)+(alpha^2/4)*(2*delta_total+R_supp+2*delta_int))", "Langer reduced inequality")

                        dp=ob["allocation_energy_dp"]
                        req(dp["q0_block_nodes"] == [0,1,2,3,24,25,26], "BMY no-go q0 nodes")
                        req(dp["q1_block_nodes"] == [8,9,10,11,32,33,34], "BMY no-go q1 nodes")
                        req(dp["q0_state_coefficients"] == {
                            "linear":[1,-1,1,-1,-1,1,-1],
                            "abel1_mod4":[1,-1,1,-1,-2,2,0],
                            "abel2_mod4":[0,0,2,-2,1,1,1],
                        }, "BMY no-go q0 DP coefficients")
                        req(dp["q1_state_coefficients"] == {
                            "linear":[1,1,1,1,1,1,1],
                            "abel3_mod4":[2,2,0,0,-1,1,-1],
                            "abel4_mod4":[1,-1,1,-1,0,0,2],
                        }, "BMY no-go q1 DP coefficients")

                        def block_energy_max(mm, coeffs):
                            states={(0,0,0):0}
                            for a,b,c0 in zip(coeffs["linear"], coeffs[list(coeffs.keys())[1]], coeffs[list(coeffs.keys())[2]]):
                                nxt={}
                                for (ss,r1,r2),qq in states.items():
                                    for vv in range(-4*mm,4*mm+1):
                                        key=(ss+a*vv,(r1+b*vv)%4,(r2+c0*vv)%4)
                                        nq=qq+vv*vv
                                        if nq > nxt.get(key,-1):
                                            nxt[key]=nq
                                states=nxt
                            return states[(0,0,0)]

                        q0c=dp["q0_state_coefficients"]
                        q1c=dp["q1_state_coefficients"]
                        req(block_energy_max(1,q0c) == 96 and block_energy_max(1,q1c) == 96, "m1 exact Abel/saturation energy maxima")
                        req(block_energy_max(2,q0c) == 384 and block_energy_max(2,q1c) == 384, "m2 exact Abel/saturation energy maxima")
                        req(dp["exact_maxima"] == {
                            "m1":{"q0_max":96,"q1_max":96,"Q_max":192},
                            "m2":{"q0_max":384,"q1_max":384,"Q_max":768},
                        }, "BMY no-go stored DP maxima")

                        cmp=ob["safe_lct_comparison"]
                        req(cmp["m1"] == {
                            "retained_abel_saturation_Q_max":192,
                            "safe_lct_langer_first_possible_exclusion_Q":207,
                            "incremental_exclusion":False,
                            "reason":"the safe-LCT Langer contradiction begins strictly above the exact formal allocation maximum",
                        }, "safe-lct BMY m1 dominated")
                        req(cmp["m2"] == {
                            "retained_miyaoka_Q_upper":677,
                            "safe_lct_langer_first_possible_exclusion_Q":708,
                            "retained_formal_witness_Q":672,
                            "incremental_exclusion":False,
                            "reason":"Miyaoka already removes every Q where the safe-LCT Langer inequality would add an exclusion",
                        }, "safe-lct BMY m2 dominated")

                        # Recheck the safe general-lct thresholds.
                        from fractions import Fraction
                        from math import isqrt
                        def max_mult_from_delta(dd):
                            return (1+isqrt(1+8*dd))//2
                        def shell_gap(mm, QQ, aa):
                            ll=2*mm
                            delta_total=784*ll*ll+112*ll
                            delta_int=4*(336*mm*mm+112*mm-2*QQ)
                            local_bracket=2*delta_total+224*ll+2*delta_int
                            lhs=Fraction(128,1)+2*aa*(448*ll)+aa*aa*(1568*ll*ll)
                            eorb=Fraction(64,1)+aa*(224*ll)+aa*aa*Fraction(local_bracket,4)
                            return lhs,3*eorb,lhs-3*eorb
                        ds1=336+112-2*207
                        req(ds1 == 34 and max_mult_from_delta(ds1) == 8, "m1 Q=207 safe lct multiplicity gate")
                        req(shell_gap(1,207,Fraction(1,8))[2] > 0, "m1 Q=207 safe Langer contradiction")
                        ds206=336+112-2*206
                        req(ds206 == 36 and max_mult_from_delta(ds206) == 9, "m1 Q=206 alpha=1/8 not safely authorized")
                        req(192 < 207, "m1 safe-Langer cut is above exact Abel maximum")
                        req(677 < 708, "m2 Miyaoka dominates safe-Langer cut")
                        req(ob["former_m2_witness"]["m"] == 2 and ob["former_m2_witness"]["Q"] == 672, "m2 witness identity")
                        req(ob["former_m2_witness"]["disposition"] == "EXCLUDED_BY_HYPERBOLIC_FIRST_JET_LANGER_BMY", "m2 witness excluded by hyperbolic Langer")
                        ds193=336+112-2*193
                        req(ds193 == 62 and max_mult_from_delta(ds193) == 11, "m1 Q=193 ordinary interior multiplicity gate")
                        req(shell_gap(1,193,Fraction(1,8))[2] == Fraction(3,16), "m1 Q=193 hyperbolic Langer contradiction")
                        ds545=336*4+112*2-2*545
                        req(ds545 == 478 and max_mult_from_delta(ds545) == 31, "m2 Q=545 ordinary interior multiplicity gate")
                        req(shell_gap(2,545,Fraction(1,16))[2] == Fraction(3,64), "m2 Q=545 hyperbolic Langer contradiction")
                        sh=ob["high_energy_shell_pruning"]
                        req(sh["m1"]["retained_abel_saturation_Q_upper"] == 192 and sh["m1"]["exclusion"] == "Q>=193 excluded", "m1 hyperbolic Langer boundary")
                        req(sh["m2"]["shell_Q_lower"] == 566 and sh["m2"]["exclusion"] == "Q>=545 excluded", "m2 hyperbolic Langer boundary")
                        req("hyperbolic first-jet rigidity proves pairwise transversality" in ob["result"] and "Q>=545" in ob["result"], "hyperbolic Langer result")
                        true_fw={k for k,v in ob["firewalls"].items() if v is True}
                        req(true_fw == {"m2_high_energy_shell_closed","pairwise_transversality_proved","incremental_exclusion"}, "orbifold-BMY positive firewalls")
                        req(ob["firewalls"]["e2_closed"] is False and ob["firewalls"]["bulk_closed"] is False, "orbifold-BMY closure firewalls")
                        req(routing["e2_unique_pair_etale_immersion_exact"] is True, "orbifold-BMY immersion routing")
                        req(routing["e2_unique_pair_orbifold_bmy_exact"] is True, "hyperbolic orbifold-BMY route retained")
                        req(routing["e2_unique_pair_orbifold_bmy_safe_lct_exact"] is True, "safe-lct orbifold-BMY routing")
                        req(routing["e2_unique_pair_orbifold_bmy_m2_high_energy_shell_closed"] is True, "m2 shell closed")
                        req(routing["e2_unique_pair_interior_pairwise_transversality_proved"] is True, "interior transversality routing")
                        req(routing["e2_unique_pair_hyperbolic_first_jet_transversality_exact"] is True, "hyperbolic first-jet routing")
                        req(routing["e2_unique_pair_hyperbolic_langer_m1_Q_upper"] == 192, "m1 hyperbolic Langer upper")
                        req(routing["e2_unique_pair_hyperbolic_langer_m2_Q_upper"] == 544, "m2 hyperbolic Langer upper")
                        req(routing["e2_unique_pair_hyperbolic_langer_m1_incremental_exclusion"] is False, "m1 Langer dominated")
                        req(routing["e2_unique_pair_hyperbolic_langer_m2_incremental_exclusion"] is True, "m2 Langer incremental")
                        req(routing["e2_unique_pair_orbifold_bmy_e2_closes"] is False, "orbifold-BMY no e2 closure")
                        req(routing["e2_unique_pair_safe_lct_bmy_incremental_exclusion_count"] == 0, "safe-lct BMY zero incremental exclusion")
                        req(routing["e2_unique_pair_safe_lct_bmy_route"] == "CLOSED_SUPERSEDED_BY_HYPERBOLIC_FIRST_JET_TRANSVERSALITY", "safe-lct BMY route superseded")
                        req(routing["e2_unique_pair_abel_formal_Q_max_m1"] == 192, "m1 formal Q max routing")
                        req(routing["e2_unique_pair_miyaoka_Q_upper_m2"] == 677, "m2 Miyaoka Q max routing")
                        req(routing["e2_unique_pair_safe_lct_bmy_first_cut_m1"] == 207, "m1 safe-Langer first cut")
                        req(routing["e2_unique_pair_safe_lct_bmy_first_cut_m2"] == 708, "m2 safe-Langer first cut")
                        req(routing["e2_unique_pair_m2_formal_Q672_witness_survives"] is False, "m2 Q672 witness killed")
                        req(d["next_obligation"]["active_leaf"] == "MB104-000707-E2-UNIQUE-PAIR-M1-POSTULATION-OR-BULK", "post-hyperbolic-Langer active leaf")
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
