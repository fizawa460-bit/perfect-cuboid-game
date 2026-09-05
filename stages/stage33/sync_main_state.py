#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at V91C1C user-authorized merged route."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
OUT = H / "MAIN-STATE.json"
CONTROLLER = H / "controller.json"
V91C1A = D / "e3-v91c1a-a2-02-literal-boundary-seed-localization.json"
V91C1B = D / "e3-v91c1b-a2-02-resolved-valuation-carrier-preflight.json"
V91C1C = D / "e3-v91c1c-a2-02-strict-transform-prime-refinement.json"
SCALAR = D / "boundary-function-scalar-descent-certificate.json"
STATE_SHA = "17497a9498ab43ef0d15f0c9a80f099605add68ec98ab4b2fe57c2e712c1862b"
CONTROLLER_SHA = "02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"
LOCKS = {
    V91C1A: "7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403",
    V91C1B: "4398be760e937e1aba279af5fd099b029dc9998675503b5df7130e714ee81387",
    V91C1C: "ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6",
    SCALAR: "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
}
NEXT = "V91C1D_MATERIALIZE_A2_02_PURITY_OFFBOUNDARY_CORRECTION_AND_PRIME_LEVEL_CECH_CARTIER_TRANSITION_DATA"


def csha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path):
    o = json.loads(path.read_text(encoding="utf-8"))
    b = dict(o); h = b.pop("canonical_sha256")
    assert h == LOCKS[path] == csha(b), path
    return o


def validate_sources():
    ctl = json.loads(CONTROLLER.read_text(encoding="utf-8"))
    b = dict(ctl); h = b.pop("projection_canonical_sha256")
    assert h == CONTROLLER_SHA == csha(b)
    assert ctl["merge_allowed"] is False and ctl["execution"]["merge_allowed"] is False
    a, b1, c1, scalar = load(V91C1A), load(V91C1B), load(V91C1C), load(SCALAR)
    assert a["selection_semantics"]["selected_direction_is_claimed_e3_coefficient"] is False
    assert b1["next_exact_leaf"].startswith("V91C1C_REFINE_A2_02_")
    assert c1["exact_consequence"]["resolved_full_surface_height_one_attachment_for_a2_02_complete"] is True
    assert c1["exact_consequence"]["prime_level_cc_ct_transport_complete"] is True
    assert c1["exact_consequence"]["purity_offboundary_correction_materialized"] is False
    assert c1["next_exact_leaf"] == NEXT
    row = next(r for r in scalar["generator_records"] if r["source_direction"] == "A2_02")
    assert row["component_count"] == 8 and row["action_scalar_record_count"] == 16
    assert row["all_candidate_scalar_ratios_one"] is True
    assert scalar["exact_conclusion"]["all_package_divisor_vectors_match_audited_stage33_11e"] is True


def validate_state(s):
    b = dict(s); h = b.pop("canonical_sha256")
    assert h == STATE_SHA == csha(b)
    assert s["schema"] == "STAGE33_MAIN_COMPACT_STATE_V33_V91C1C_USER_AUTHORIZED_MERGED_ROUTE"
    a = s["authority_sync"]
    assert a["frontier_authority"] == "V91C1C_A2_02_STRICT_TRANSFORM_PRIME_REFINEMENT"
    p = s["continuation_provenance"]
    assert p["v91c1c_pr"] == 1620
    assert p["merged_head"] == "75585168c54241591fb29c9271b64e1e95d1f1f6"
    assert p["merge_commit"] == "e2103a2de367a0a6d0826b044b6bb83d24ad6f6f"
    assert p["user_authorized_merge"] is True and p["user_judged_mathematics_pass"] is True
    assert p["hostile_audit_pass_claimed"] is False and p["theorem_credit_from_user_authorized_merge"] is False
    f = s["current_exact_frontier"]
    for k in ("a2_02_resolved_exceptional_valuation_attachment_materialized", "a2_02_strict_transform_carrier_prime_refinement_complete", "a2_02_prime_level_cc_ct_transport_complete", "a2_02_resolved_full_surface_height_one_attachment_complete"):
        assert f[k] is True
    for k in ("a2_02_purity_offboundary_correction_materialized", "a2_02_full_surface_cech_transition_glue_materialized", "a2_02_cartier_transition_binding_materialized", "a2_02_claimed_e3_coefficient", "a2_02_claimed_mask20_image", "e3_marked_brauer_image_from_boundary_functions_materialized", "e3_complete_residue_audit_materialized", "e3_genuine_full_surface_h2_mu2_lift_materialized"):
        assert f[k] is False
    assert s["current"]["next_exact_leaf"] == NEXT
    assert s["execution_gate"]["advance_allowed"] is True
    assert s["execution_gate"]["advance_scope"] == "V91C1D_A2_02_PURITY_CECH_CARTIER_ASSEMBLY"
    assert s["stage33_progress"] == "6/11" and s["firewalls"]["merge_allowed"] is False
    assert s["controller_projection_canonical_sha256"] == CONTROLLER_SHA
    assert s["anti_loop_policy"]["do_not_relabel_v91c1c_user_authorized_merge_as_hostile_audit_pass"] is True


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    validate_sources()
    s = json.loads(OUT.read_text(encoding="utf-8")); validate_state(s)
    if args.write:
        OUT.write_text(json.dumps(s, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    if args.check or not args.write:
        assert OUT.stat().st_size < 9800
        print(json.dumps({"success": True, "marker": "V96_V91C1C_USER_AUTHORIZED_MERGED_ROUTE", "state_sha256": STATE_SHA, "frontier": s["authority_sync"]["frontier_authority"], "next_exact_leaf": NEXT}, sort_keys=True))


if __name__ == "__main__":
    main()
