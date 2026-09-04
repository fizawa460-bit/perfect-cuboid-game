#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1555-b3-full-g-box-quotient-normalizer.json"
CONTROLLER = ROOT / "stages/stage32/controller.json"

EXPECTED_CANONICAL = "4d2eacaca1ccb8db9bf0143e57fd39c9d8bb47a7180db8b9cd37533e5d5f7c38"
EXPECTED_BASE = "a96f1920977dd43194f60eb29487c0ec5deff711"


def fail(msg: str) -> None:
    raise SystemExit(msg)


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if claimed != calc:
        fail(f"canonical mismatch: {claimed} != {calc}")
    return calc


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> None:
    cert = load_json(CERT_PATH)
    if cert["schema"] != "STAGE32_POST1555_B3_FULL_G_BOX_QUOTIENT_NORMALIZER_V1":
        fail("certificate schema moved")
    if cert["status"] != "EXACT_FULL_G_BOX_QUOTIENT_NORMALIZER_PENDING_HOSTILE_AUDIT":
        fail("certificate status moved")
    if canonical_sha(cert) != EXPECTED_CANONICAL:
        fail("certificate canonical moved")
    if cert["base_main_sha"] != EXPECTED_BASE:
        fail("base main moved")

    locked = {}
    for name, lock in cert["source_locks"].items():
        path = ROOT / lock["path"]
        if not path.is_file():
            fail(f"missing source lock: {name}")
        got = blob_sha1(path)
        if got != lock["blob_sha1"]:
            fail(f"source blob drift: {name}: {got}")
        if "canonical_sha256" in lock:
            doc = load_json(path)
            if canonical_sha(doc) != lock["canonical_sha256"]:
                fail(f"source canonical drift: {name}")
            locked[name] = doc
        else:
            locked[name] = path.read_text()

    ambient = locked["ambient_v4_normalizer"]
    v4 = locked["v4_cusp_quotient"]
    common = locked["common_double_cover"]
    b3red = locked["single_b3_reduction"]
    note = locked["source_note"]

    if ambient["decision"]["ambient_quotient_normalizer_gate_closed_positive"] is not True:
        fail("parent ambient V4 normalizer moved")
    tn = ambient["torsor_normalizer"]
    if tn["semilinear_lift_exists"] is not True:
        fail("parent semilinear b3 lift moved")
    if tn["same_lift_on_both_factors_normalizes_H_diag"] is not True:
        fail("parent H_diag normalizer moved")
    if tn["covers"] != "b3 x b3 on C0 x C0":
        fail("parent b3 base action moved")

    qg = v4["quotient_geometry"]
    gc = v4["exact_group_checks"]
    if qg["genus_C0"] != 2 or qg["genus_X4"] != 0:
        fail("C0/X4 genus anchor moved")
    if qg["C0_to_X4_degree"] != 2:
        fail("C0->X4 degree moved")
    if qg["C0_to_X4_total_fixed_points"] != 6:
        fail("C0->X4 fixed-point count moved")
    if qg["six_quotient_cusps_are_Weierstrass_points"] is not True:
        fail("Weierstrass identification moved")
    if gc["Gamma_prime_4_over_Gamma8_order"] != 4:
        fail("H order moved")
    if gc["Gamma4_over_Gamma8_order"] != 8:
        fail("G order moved")
    if gc["T4_outside_V4"] is not True:
        fail("nontrivial G/H representative moved")

    square = common["group_quotient_square"]
    if square["Z"] != "X(8)":
        fail("Z anchor moved")
    if square["H"] != "Gamma'[4]/Gamma[8] ~= V4, order 4, normal index 2":
        fail("H normal-index-2 anchor moved")
    if square["G"] != "Gamma[4]/Gamma[8], order 8":
        fail("G anchor moved")
    if square["X"] != "P/H_diag (Beauville cover surface)":
        fail("X quotient moved")
    if square["B"] != "P/G_diag (box surface on the retained open/normalization level)":
        fail("B quotient moved")

    carrier = common["carrier_consequence"]
    if carrier["hypothesis"] != "N is the normalization of a hypothetical integral carrier mapping to B, and Y is the normalization of its Beauville pullback N x_B X.":
        fail("N/Y carrier hypothesis moved")

    if b3red["decision"]["conditional_implication"] != "[T,b3]=0 => Q(T)!=602":
        fail("single-b3 conditional exclusion moved")
    if b3red["decision"]["Q602_excluded_unconditionally"] is not False:
        fail("single-b3 firewall moved")

    qc = cert["quotient_chain"]
    if qc["H_normal_index_in_G"] != 2:
        fail("certificate H index moved")
    if not all((
        qc["C0_genus"] == 2,
        qc["X4_genus"] == 0,
        qc["C0_to_X4_degree"] == 2,
        qc["C0_to_X4_fixed_points"] == 6,
        qc["deck_involution_is_hyperelliptic"] is True,
    )):
        fail("certificate hyperelliptic quotient data moved")

    hc = cert["hyperelliptic_centrality"]
    if hc["b3_is_automorphism_of_C0"] is not True or hc["b3_commutes_with_tau"] is not True:
        fail("hyperelliptic centrality conclusion moved")
    if "unique" not in hc["reason"] or "central" not in hc["reason"]:
        fail("hyperelliptic centrality reason moved")

    norm = cert["full_G_normalizer"]
    for key in (
        "ambient_semilinear_lift_from_parent",
        "tilde_b3_normalizes_H",
        "choose_g_in_G_minus_H_lifting_tau",
        "conjugate_of_g_descends_to_tau",
        "conjugate_differs_from_g_by_H",
        "tilde_b3_normalizes_G",
        "same_lift_normalizes_G_diag",
        "beta_B_exists",
        "beta_X_exists",
        "X_to_B_equivariant",
    ):
        if norm[key] is not True:
            fail(f"full-G normalizer flag moved: {key}")

    boundary = cert["carrier_boundary"]
    if boundary["N"] != "normalization of a hypothetical integral carrier mapping to B":
        fail("N boundary moved")
    if boundary["Y"] != "normalization of N x_B X":
        fail("Y boundary moved")
    for key in (
        "beta_B_N_invariance_proved",
        "beta_X_Y_invariance_proved",
        "intrinsic_beta_Y_proved",
        "Gamma_invariance_proved",
    ):
        if boundary[key] is not False:
            fail(f"carrier firewall leaked: {key}")
    if boundary["conditional_chain"] != "beta_B(N)=N => beta_X(Y)=Y => [T,b3]=0 => Q(T)!=602":
        fail("conditional carrier-to-exclusion chain moved")

    decision = cert["decision"]
    if decision["result"] != "PASS_EXACT_FULL_G_AND_BOX_QUOTIENT_NORMALIZER":
        fail("decision moved")
    if decision["full_G_normalizer_gate_closed_positive"] is not True:
        fail("full-G gate not positive")
    if decision["box_quotient_descent_gate_closed_positive"] is not True:
        fail("box descent gate not positive")
    if decision["next_exact_leaf"] != "PROVE_HYPOTHETICAL_CARRIER_N_INVARIANT_UNDER_BETA_B_OR_DIRECT_GAMMA_INVARIANCE":
        fail("next exact leaf moved")
    for key in (
        "carrier_invariance_proved",
        "correspondence_invariance_proved",
        "actual_T_b3_commutation_proved",
        "actual_T_b3_noncommutation_proved",
        "Q602_excluded",
        "O210_excluded",
        "O212_plus_advance_allowed",
        "controller_change_authorized",
    ):
        if decision[key] is not False:
            fail(f"decision firewall leaked: {key}")

    if any(cert["firewalls"].values()):
        fail("credit firewall leaked")

    for marker in (
        "B3_NORMALIZES_FULL_G=true",
        "B3_DESCENDS_TO_BOX_QUOTIENT_B=true",
        "X_TO_B_B3_EQUIVARIANT=true",
        "beta_B(N)=N",
        "PROVE_HYPOTHETICAL_CARRIER_N_INVARIANT_UNDER_BETA_B_OR_DIRECT_GAMMA_INVARIANCE",
        "The Stage32 controller remains unchanged.",
    ):
        if marker not in note:
            fail(f"source-note marker missing: {marker}")

    ctl = load_json(CONTROLLER)
    if ctl["stage"] != 32 or ctl["stage32_closed"] is not False:
        fail("controller lifecycle moved")
    fixed = ctl["fixed_target"]
    if (fixed["row_id"], fixed["O"], fixed["qprime"], fixed["Q"]) != ("g1-d186", 210, 4, 602):
        fail("controller fixed target moved")

    print("PASS post1555 b3 full-G / box-quotient normalizer")
    print(f"canonical={EXPECTED_CANONICAL}")
    print("b3 normalizes H and full G; diagonal lift descends to X and B")
    print("X->B equivariant=PASS")
    print("beta_B(N)=N / Gamma invariance=UNRESOLVED")
    print("Q602/O210=OPEN O212+=BLOCKED controller=UNCHANGED")


if __name__ == "__main__":
    main()
