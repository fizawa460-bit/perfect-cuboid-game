#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CHECKPOINT = HERE / "CARRIER-ADAPTER.json"

LOCKS = {
    "hpadj01": (
        "stages/stage32/management/hpadj-01/RESULT.json",
        "520b6b0f230e23fb5ea34b80fef591cfa5f9be4b",
        "9773c11e87de149b5b56438fd1c86929aa54a971601bf8306855fd0f8a303506",
    ),
    "hpadj02": (
        "stages/stage32/management/hpadj-02/RESULT.json",
        "2f7b016c9030bdb86071f5b0b4803b4bde210584",
        "d7e653f7e693776730121769c86fc3fa11af0b6a5755dc392d40837c1eb05986",
    ),
    "hpadj03": (
        "stages/stage32/management/hpadj-03/RESULT.json",
        "6f5985f2c2e0995628653a6bc73b9bf6c7256a7c",
        "0840d9ec07f6380e4fdad97ab2d6e32c69d25e7539837fa65bd0c34ca3cb8b49",
    ),
    "hpadj05": (
        "stages/stage32/management/hpadj-05/CONSUMER-REENTRY.json",
        "b6c1fb139fdb4189b8b5dbe351ace27f3a6748ad",
        "a064c6d95aaf19f2b2b0515143722da50fdd307c7fbd608b98bcf0c9f2be9ee1",
    ),
    "interface": (
        "stages/stage32-ex5/hpadj-handoff/INTERFACE.json",
        "8a30e3aa30777460f344eb19836dc725dd442329",
        "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6",
    ),
    "effectivity_gap": (
        "stages/stage32/32-21/post-21bl-effectivity-gap-separation.json",
        "8b46b85a7fe7d1b366d0ada0a7db852f123e77e1",
        "4afeb8a3add7c203fbbaa9ffdb5b4b4d357df8503979ee80617db654df73d4dc",
    ),
    "genus_defect": (
        "stages/stage32/32-21/post-21bl-genus-defect-preflight.json",
        "ecf4e9d20eddcaef9375f4c6b21ecf9bf6b0cd8c",
        "e59e23b2aefb1a3b622f3f3ed4eb0f83fd7bb335125fa3254c7e4e737caaa96c",
    ),
}

ROUTE_PATH = "stages/stage29/29-02c-LG2/route-contract.json"
ROUTE_BLOB = "99752985fd705ee993d052e5bcc622181c7a4cbc"
EXPECTED_CHECKPOINT_CANON = "72144be89761ba82f93fd33ca7647c90a4ba12646d5f63e70537a955d93f106d"


def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def locked_json(rel: str, blob: str, canon: str | None = None) -> dict:
    path = ROOT / rel
    req(path.is_file(), f"missing source {rel}")
    req(git_blob(path) == blob, f"blob drift {rel}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == canon, f"stored canonical drift {rel}")
        req(canonical(obj) == canon, f"canonical drift {rel}")
    return obj


def verify_checkpoint() -> dict:
    cp = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    req(cp.get("schema") == "STAGE32_MAIN_HPADJ06_ONE_WAY_ACTUAL_CARRIER_ADAPTER_V1",
        "checkpoint schema")
    req(cp.get("canonical_sha256_without_this_field") == EXPECTED_CHECKPOINT_CANON,
        "checkpoint stored canonical")
    req(canonical(cp) == EXPECTED_CHECKPOINT_CANON, "checkpoint canonical")
    req(cp["predecessor_boundary"]["hostile_audited_exact_head"] ==
        "7846413a1d632646044340c40f57551cf2ff4b0c", "predecessor head")
    req(cp["predecessor_boundary"]["hostile_audit_review_id"] == 5190630517,
        "predecessor audit review")
    req(cp["predecessor_boundary"]["merge_authorized"] is False, "merge firewall")
    return cp


def verify_sources() -> None:
    src = {name: locked_json(*spec) for name, spec in LOCKS.items()}
    route = locked_json(ROUTE_PATH, ROUTE_BLOB)

    h1 = src["hpadj01"]
    req(h1["necessary_condition"]["exact_hodge_bound"] ==
        "C^2 <= d^2/16 - (1/2)*sum_{i=1}^{10} y_i^2", "HPADJ Hodge bound")
    req(h1["necessary_condition"]["group_cauchy_rejection_condition"] ==
        "8*a^2 + 8*b^2 + 6*c^2 > 3*d^2 + 96", "HPADJ rejection predicate")
    req(h1["necessary_condition"]["irreducible_k3_adjunction"] == "C^2 >= -2",
        "HPADJ adjunction floor")
    req(h1["necessary_condition"]["meaning"] ==
        "violation excludes an irreducible K3 carrier for every Picard completion of that compressed terminal",
        "HPADJ carrier meaning")
    req(h1["composition_firewall"]["main_authority_mutated"] is False,
        "HPADJ01 authority firewall")

    h2 = src["hpadj02"]
    req(h2["semantic_gap"]["rr_does_not_conclude_integral_irreducible_representative"] is True,
        "RR semantic firewall")
    req(h2["semantic_gap"]["therefore_existing_rr_material_does_not_supply_irreducible_carrier_adapter"] is True,
        "RR no-carrier-adapter firewall")
    req(h2["firewalls"]["main_pruning_credit"] is False, "HPADJ02 pruning firewall")

    h3 = src["hpadj03"]
    own = h3["ownership_and_next_datum"]
    req(own["main_must_not_identify_exceptional_contact_mass_with_delta"] is True,
        "delta firewall")
    req("32-02 geometry" in own["likely_producer_lane"], "carrier owner boundary")
    req(h3["firewalls"]["main_pruning_credit"] is False, "HPADJ03 pruning firewall")

    h5 = src["hpadj05"]
    reentry = h5["consumer_reentry"]
    req(reentry["operational_handoff_validated"] is True, "consumer re-entry")
    req(reentry["next_mathematical_gap"] == "ACTUAL_INTEGRAL_IRREDUCIBLE_CARRIER_SEMANTICS",
        "consumer next gap")
    iv = h5["interface_validation"]
    req(iv["fixed_plus_free_selected64_partition_complete"] is True, "selected64 partition")
    req(iv["rank_unrank_roundtrip_exact"] is True, "terminal rank/unrank")
    req(iv["retained_picard64_coordinate_count"] == 64, "Picard rank")
    req(iv["selected64_inverse_denominator"] == 8, "selected64 denominator")
    req(iv["terminal_fixed_selected_pairings"] == 11 and iv["free_selected_pairings"] == 53,
        "11+53 partition")
    req(iv["terminal_alone_asserts_completion_exists"] is False, "completion-existence firewall")
    req(h5["credit_firewall"]["hpadj_main_pruning_credit"] is False,
        "consumer credit firewall")

    interface = src["interface"]
    ri = interface["reconstructed_picard64_coordinate_identity"]
    tm = interface["terminal_to_picard64_map"]
    req(ri["fixed_plus_free_affine_fiber_exact"] is True, "exact affine fiber")
    req(ri["unique_coordinate_vector_for_each_integral_selected64_completion"] is True,
        "unique completion coordinate vector")
    req(ri["terminal_alone_asserts_completion_exists"] is False, "interface existence firewall")
    req(tm["inverse_denominator"] == 8, "interface denominator")
    req(tm["terminal_pairing_count"] == 11 and tm["free_pairing_parameter_count"] == 53,
        "interface 11+53")
    req(interface["hpadj01_population_identity"]["affected_rows"] == 178, "FULL178 row identity")
    req(interface["hpadj01_population_identity"]["charged_terminal_lower_bound"] ==
        27104321327305699275487, "charged population identity")

    eff = src["effectivity_gap"]
    req(eff["exact_gap_result"]["actual_effective_curve_certificate_present"] is False,
        "historical effectivity firewall")
    req(eff["exact_gap_result"]["integral_irreducible_curve_certificate_present"] is False,
        "historical irreducibility firewall")
    req(eff["firewalls"]["effectivity_is_not_low_genus_irreducible_carrier_without_adapter"] is True,
        "historical carrier firewall")

    gd = src["genus_defect"]
    req(gd["interpretation"]["actual_effective_integral_curve_certificate_present"] is False,
        "genus-defect effectivity firewall")
    req(gd["interpretation"]["no_formula_equating_exceptional_pairing_profile_to_delta_invariant_is_claimed_here"] is True,
        "genus-defect delta firewall")

    verdicts = route["verdicts"]
    req(verdicts["effectivity_certified"] is False, "Stage29 effectivity firewall")
    req(verdicts["multibranch_cases_covered"] is False, "Stage29 multibranch firewall")
    req(verdicts["isolated_rational_points_excluded"] is False, "Stage29 isolated-point firewall")


def verify_exact_algebra() -> None:
    # 48 times the HPADJ Hodge upper bound after group Cauchy is
    # 3*d^2 - 8*a^2 - 8*b^2 - 6*c^2.
    # The rejection predicate is precisely that this integer is < -96.
    for d in range(0, 25):
        for a in range(0, 25):
            for b in range(0, 25):
                for c in range(0, 25):
                    reject = 8*a*a + 8*b*b + 6*c*c > 3*d*d + 96
                    upper48 = 3*d*d - 8*a*a - 8*b*b - 6*c*c
                    req(reject == (upper48 < -96), "algebraic predicate regression")
    # The equivalence above is coefficient-wise; the finite replay is only a
    # guard against transcription errors, not a bounded mathematical proof.


def verify_firewalls(cp: dict) -> None:
    req(cp["proved_direction"]["conclusion"] ==
        "ACTUAL_MATCHING_INTEGRAL_IRREDUCIBLE_CARRIER -> NOT_HPADJ_REJECTED_TERMINAL",
        "one-way conclusion")
    req(cp["proved_direction"]["contrapositive"] ==
        "HPADJ_REJECTED_TERMINAL -> NO_ACTUAL_MATCHING_INTEGRAL_IRREDUCIBLE_K3_CARRIER",
        "one-way contrapositive")
    pop = cp["population_interface"]
    req(pop["terminal_alone_asserts_integral_completion_exists"] is False,
        "terminal completion firewall")
    req(pop["this_adapter_asserts_every_terminal_has_actual_carrier"] is False,
        "terminal carrier firewall")
    req(pop["this_adapter_asserts_every_numerical_survivor_has_actual_carrier"] is False,
        "numerical carrier firewall")
    req(cp["reverse_realization_gap"]["status"] == "OPEN_LOAD_BEARING",
        "reverse gap must remain open")
    req(cp["scope"]["subtract_hpadj01_from_main_authority"] is False,
        "authority subtraction firewall")
    req(cp["scope"]["change_main_state"] is False, "MAIN state firewall")
    for key, value in cp["firewalls"].items():
        req(value is False, f"credit/firewall unexpectedly true: {key}")


def main() -> None:
    cp = verify_checkpoint()
    verify_sources()
    verify_exact_algebra()
    verify_firewalls(cp)
    print("PASS hpadj06 one-way actual-carrier adapter; reverse realization remains open; no MAIN credit")


if __name__ == "__main__":
    main()
