#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT_FILE = HERE / "post1629-full-g-retained-stoll-extra-involution-gap.json"
POST1473_FILE = HERE / "post1473-x8-v4-cusp-quotient.json"
POST1555_FILE = HERE / "post1555-b3-full-g-box-quotient-normalizer.json"
H_ASSET_FILE = HERE / "post1532-full-stoll-h-orbit-symmetry-negative.json"


def canonical_sha(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if claimed != calc:
        raise SystemExit(f"canonical mismatch: {claimed} != {calc}")
    return calc


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(cond: bool, message: str) -> None:
    if not cond:
        raise SystemExit(message)


def main() -> None:
    cert = json.loads(CERT_FILE.read_text())
    canonical_sha(cert)
    require(cert["schema"] == "STAGE32_POST1629_FULL_G_RETAINED_STOLL_EXTRA_INVOLUTION_GAP_V1", "schema moved")
    require(cert["status"] == "PASS_EXACT_BOUNDED_INTERFACE_GAP_PENDING_HOSTILE_AUDIT", "status moved")

    post1473 = json.loads(POST1473_FILE.read_text())
    post1555 = json.loads(POST1555_FILE.read_text())
    h_asset = json.loads(H_ASSET_FILE.read_text())
    locks = cert["source_locks"]

    require(git_blob_sha1(POST1473_FILE) == locks["v4_cusp_quotient"]["blob_sha1"], "post1473 blob moved")
    require(canonical_sha(post1473) == locks["v4_cusp_quotient"]["canonical_sha256"], "post1473 canonical moved")
    require(git_blob_sha1(POST1555_FILE) == locks["full_G_normalizer"]["blob_sha1"], "post1555 blob moved")
    require(canonical_sha(post1555) == locks["full_G_normalizer"]["canonical_sha256"], "post1555 canonical moved")
    require(canonical_sha(h_asset) == locks["H_retained_stoll"]["canonical_sha256"], "retained H asset moved")

    group = post1473["exact_group_checks"]
    geom = post1473["quotient_geometry"]
    require(group["Gamma_prime_4_over_Gamma8_order"] == 4, "H order moved")
    require(group["Gamma4_over_Gamma8_order"] == 8, "G order moved")
    require(group["T4_outside_V4"] is True, "T4 outside H moved")
    require(geom["C0_to_X4_degree"] == 2, "G/H degree moved")
    require(post1473["firewalls"]["abstract_cusp_orbits_not_yet_retained_boundary_label_identification"] is True, "post1473 boundary identification firewall moved")

    q = post1555["quotient_chain"]
    normalizer = post1555["full_G_normalizer"]
    centrality = post1555["hyperelliptic_centrality"]
    require(q["H_normal_index_in_G"] == 2, "H normal index moved")
    require(q["deck_involution_is_hyperelliptic"] is True, "hyperelliptic deck involution moved")
    require(normalizer["tilde_b3_normalizes_H"] is True, "b3 H normalizer moved")
    require(normalizer["choose_g_in_G_minus_H_lifting_tau"] is True, "abstract extra deck lift moved")
    require(normalizer["tilde_b3_normalizes_G"] is True, "b3 full-G normalizer moved")
    require(centrality["b3_commutes_with_tau"] is True, "b3/tau commutation moved")

    h_words = h_asset["finite_result"]["h_deck_words"]
    require(h_words == cert["retained_positive_input"]["retained_H_words"], "retained H words moved")
    require(h_asset["finite_result"]["h_deck_group_order"] == 4, "retained H group order moved")

    bounded = cert["bounded_interface_status"]
    require(bounded["post1473_abstract_cusp_orbits_not_yet_retained_boundary_label_identification"] is True, "bounded post1473 status moved")
    require(bounded["post1555_extra_G_over_H_lift_is_existential_choice"] == "choose_g_in_G_minus_H_lifting_tau", "bounded post1555 status moved")
    require(bounded["extra_G_over_H_involution_retained_stoll_word_source_locked"] is False, "unexpected retained Stoll word credit")
    require(bounded["extra_G_over_H_involution_140_class_permutation_source_locked"] is False, "unexpected retained permutation credit")
    require(bounded["full_G_character_action_promoted_to_retained_picard64_action"] is False, "unexpected Picard64 action promotion")
    require(bounded["repo_wide_absence_claimed"] is False, "repo-wide absence claim forbidden")

    logical = cert["logical_boundary"]
    require(all(logical.values()), "logical firewall moved")
    decision = cert["decision"]
    require(decision["result"] == "PASS_EXACT_FULL_G_TO_RETAINED_STOLL_EXTRA_INVOLUTION_INTERFACE_GAP", "decision moved")
    require(decision["exact_principal_b3_member_identified"] is False, "unexpected b3 member identification")
    require(decision["marked_picard_action_identified"] is False, "unexpected marked Picard action")
    require(decision["residue_specific_commutator_obtained"] is False, "unexpected commutator credit")
    require(decision["q602_residue_elimination_credit"] is False, "unexpected Q602 elimination credit")
    require(decision["Q602_excluded"] is False and decision["O210_excluded"] is False, "unexpected endpoint credit")
    require(decision["controller_change_authorized"] is False, "unexpected controller promotion")
    require(decision["surviving_residues_decimal"] == [73, 97, 235], "survivors moved")

    print(json.dumps({
        "schema": "STAGE32_POST1629_FULL_G_RETAINED_STOLL_EXTRA_INVOLUTION_GAP_VERIFY_V1",
        "status": "PASS",
        "G_order": group["Gamma4_over_Gamma8_order"],
        "H_order": group["Gamma_prime_4_over_Gamma8_order"],
        "G_over_H_order": q["H_normal_index_in_G"],
        "extra_involution_retained_stoll_word_source_locked": False,
        "surviving_residues_decimal": decision["surviving_residues_decimal"],
        "controller_change_authorized": False,
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
