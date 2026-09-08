#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent

B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C2A = HERE / "e3-v91c1x-r5b3b3c2a-reused-prime-refinement-partition.json"
E11_SOURCE = S33 / "33-11e" / "stage33-11e-source-lock.json"
D11_SOURCE = S33 / "33-11d" / "stage33-11d-source-lock.json"
OUT = HERE / "e3-v91c1x-r5b3b3c2b-novel20-surface-action-orbit-preflight.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C2A_SHA = "8eb0f382998f934ec712b79af0900df1f3da401e1a9770b770091577d0bc1c44"
E11_SOURCE_SHA = "a1bce01bb7041d9cc48bfb7ce6e6f6095afc36ef8bc08fcb1588a885ed61e2e2"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
EXPECTED_NOVEL_COUNT = 20


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path: Path, expected: str | None = None):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != actual:
        raise SystemExit(f"canonical hash mismatch: {path}")
    if expected is not None and claimed != expected:
        raise SystemExit(f"source lock moved: {path}: {claimed} != {expected}")
    return obj


def qi(z):
    return Fraction(int(z[0]), int(z[1])), Fraction(int(z[2]), int(z[3]))


def qmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def qinv(x):
    d = x[0] * x[0] + x[1] * x[1]
    if not d:
        raise SystemExit("zero projective coefficient pivot")
    return x[0] / d, -x[1] / d


def qenc(x):
    return (
        x[0].numerator,
        x[0].denominator,
        x[1].numerator,
        x[1].denominator,
    )


def normalize(sig):
    vals = [qi(z) for z in sig]
    pivot = next((x for x in vals if x != (0, 0)), None)
    if pivot is None:
        raise SystemExit("zero projective linear carrier")
    inv = qinv(pivot)
    return tuple(qenc(qmul(x, inv)) for x in vals)


def cc(sig):
    return normalize([(z[0], z[1], -z[2], z[3]) for z in sig])


def swap(sig, perm):
    return normalize([sig[int(j)] for j in perm])


def sid(sig):
    return csha([list(z) for z in sig])


def generated_orbit(rep, perms):
    queue = deque([(rep, [])])
    words = {rep: []}
    while queue:
        sig, word = queue.popleft()
        images = [
            ("cc", cc(sig)),
            ("swap12", swap(sig, perms["swap12"])),
            ("swap13", swap(sig, perms["swap13"])),
        ]
        for name, image in images:
            if image not in words:
                words[image] = word + [name]
                queue.append((image, word + [name]))
                if len(words) > 128:
                    raise SystemExit("certified action orbit unexpectedly exceeded finite guard")
    return words


def build_certificate():
    b3b2 = load_checked(B3B2, B3B2_SHA)
    c2a = load_checked(C2A, C2A_SHA)
    e11 = load_checked(E11_SOURCE, E11_SOURCE_SHA)
    d11_expected = e11["audited_stage33_11d"]["source_lock_sha256"]
    d11 = load_checked(D11_SOURCE, d11_expected)

    if e11["audited_stage33_11d"]["hostile_audit_verdict"] != "PASS_STAGE33_11D_CARRIER_PRIME_REFINEMENT":
        raise SystemExit("33-11d hostile-audit provenance moved")

    perms = d11["certified_actions"]
    if set(perms) < {"swap12", "swap13"}:
        raise SystemExit("frozen certified surface actions moved")
    for name in ("swap12", "swap13"):
        p = [int(x) for x in perms[name]]
        if sorted(p) != list(range(7)):
            raise SystemExit(f"{name} is no longer a 7-coordinate permutation")
        if [p[p[j]] for j in range(7)] != list(range(7)):
            raise SystemExit(f"{name} is no longer an involution")

    inv = b3b2["finite_linear_carrier_inventory"]
    current = {row["carrier_id"]: row for row in inv["carrier_rows"]}
    novel_ids = list(c2a["exact_partition"]["novel_carrier_ids_requiring_new_exact_prime_decomposition"])
    if len(novel_ids) != EXPECTED_NOVEL_COUNT or len(set(novel_ids)) != EXPECTED_NOVEL_COUNT:
        raise SystemExit("C2A novel20 partition moved")
    if any(cid not in current for cid in novel_ids):
        raise SystemExit("C2A novel carrier absent from B3B2 inventory")

    by_id = {}
    sig_to_id = {}
    for cid in novel_ids:
        row = current[cid]
        sig = normalize(row["normalized_coefficients_Qi"])
        if sid(sig) != row["projective_linear_form_Qi_sha256"]:
            raise SystemExit(f"carrier signature/hash mismatch: {cid}")
        if sig in sig_to_id:
            raise SystemExit(f"duplicate projective novel carrier: {cid} and {sig_to_id[sig]}")
        by_id[cid] = sig
        sig_to_id[sig] = cid

    unassigned = set(novel_ids)
    orbit_rows = []
    while unassigned:
        seed_id = min(unassigned)
        seed = by_id[seed_id]
        words = generated_orbit(seed, perms)
        members = {
            sig_to_id[sig]: word
            for sig, word in words.items()
            if sig in sig_to_id
        }
        if seed_id not in members:
            raise SystemExit("seed disappeared from its own certified orbit")
        member_ids = sorted(members)
        if any(cid not in unassigned for cid in member_ids):
            raise SystemExit("novel20 orbit partition overlap")
        for cid in member_ids:
            unassigned.remove(cid)
        orbit_rows.append({
            "representative_carrier_id": seed_id,
            "representative_projective_linear_form_Qi_sha256": sid(seed),
            "novel20_member_count": len(member_ids),
            "novel20_member_ids": member_ids,
            "transport_words_from_representative": {
                cid: members[cid] for cid in member_ids
            },
            "full_certified_action_orbit_size_before_novel20_intersection": len(words),
            "transport_generators": ["cc", "swap12", "swap13"],
        })

    covered = [cid for row in orbit_rows for cid in row["novel20_member_ids"]]
    if sorted(covered) != sorted(novel_ids) or len(covered) != len(set(covered)):
        raise SystemExit("novel20 orbit partition is not exact")

    reps = [row["representative_carrier_id"] for row in orbit_rows]
    orbit_hist = {}
    for row in orbit_rows:
        key = str(row["novel20_member_count"])
        orbit_hist[key] = orbit_hist.get(key, 0) + 1

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c2b.novel20_surface_action_orbit_preflight.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C2B_CERTIFIED_SURFACE_ACTION_ORBIT_REDUCTION_OF_NOVEL20",
        "role": "EXACT_NONCREDIT_PREFLIGHT_REDUCING_NOVEL20_STRICT_PRIME_DECOMPOSITIONS_BY_HOSTILE_AUDITED_33_11D_SURFACE_ACTIONS",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "r5b3b3c2a_reused_prime_partition_sha256": C2A_SHA,
            "stage33_11e_source_lock_sha256": E11_SOURCE_SHA,
            "stage33_11d_source_lock_sha256": d11_expected,
            "stage33_11d_hostile_audit_verdict": e11["audited_stage33_11d"]["hostile_audit_verdict"],
            "stage33_11d_hostile_audited_head": e11["audited_stage33_11d"]["audited_head"],
            "stage33_11d_pr": int(e11["audited_stage33_11d"]["pr"]),
        },
        "certified_action_model": {
            "coefficient_field": "Q(i)",
            "semilinear_generator": "cc",
            "coordinate_permutation_generators": {
                "swap12": [int(x) for x in perms["swap12"]],
                "swap13": [int(x) for x in perms["swap13"]],
            },
            "normalization": "FIRST_NONZERO_QI_COEFFICIENT_SCALED_TO_ONE",
            "transport_scope": "HYPERPLANE_SECTION_PRIME_DECOMPOSITIONS_TRANSPORT_UNDER_CERTIFIED_SURFACE_ACTION_OR_FIELD_CONJUGATION",
        },
        "novel20_orbit_partition": {
            "novel_carrier_count": len(novel_ids),
            "orbit_count": len(orbit_rows),
            "orbit_representative_count_requiring_new_exact_prime_decomposition": len(reps),
            "orbit_representative_carrier_ids": reps,
            "orbit_size_histogram_within_novel20": orbit_hist,
            "orbits": orbit_rows,
            "all_20_partitioned_exactly_once": True,
        },
        "construction_status": {
            "novel20_certified_surface_action_orbits_materialized": True,
            "new_exact_prime_decomposition_work_reduced_to_orbit_representatives": True,
            "orbit_representative_prime_decompositions_materialized": False,
            "transported_prime_decompositions_materialized_for_all_novel20": False,
            "c1_base_factor_to_strict_prime_adapter_materialized_for_all_21_unique_factors": False,
            "exceptional_prime_attachment_for_all_offboundary_carriers_materialized": False,
            "combined_tame_residue_squareclasses_audited": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
        },
        "exact_consequence": {
            "all_20_novel_carriers_are_partitioned_by_the_same_certified_actions_used_in_hostile_audited_33_11d": True,
            "one_exact_section_prime_decomposition_per_orbit_representative_suffices_for_transport_to_every_novel20_member": True,
            "this_orbit_preflight_does_not_itself_supply_any_new_prime_decomposition": True,
            "field_conjugation_transport_is_semilinear_and_is_not_relabelled_as_a_Qi_linear_surface_automorphism": True,
            "no_unramifiedness_or_residue_cancellation_follows_from_orbit_reduction_alone": True,
        },
        "next_missing_object": "EXACT_PRIMARY_OR_MINIMAL_PRIME_DECOMPOSITION_OVER_QI_FOR_EACH_C2B_ORBIT_REPRESENTATIVE_SECTION_THEN_CERTIFIED_TRANSPORT_TO_ALL_20_NOVEL_CARRIERS_MATCH_C1_BASE_NORM_FACTORS_TO_STRICT_PRIMES_AND_ATTACH_EXCEPTIONAL_VALUATIONS",
        "next_exact_leaf": "V91C1X_R5B3B3C2C_ORBIT_REPRESENTATIVE_STRICT_PRIME_DECOMPOSITION_AND_TRANSPORT",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    body = dict(cert)
    cert["canonical_sha256"] = csha(body)
    return cert


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT}")
    else:
        if not OUT.exists():
            raise SystemExit(f"certificate missing: {OUT}")
        recorded = json.loads(OUT.read_text(encoding="utf-8"))
        if recorded != cert:
            raise SystemExit("checked-in C2B certificate differs from exact rebuild")
    print("PASS V91C1X R5B3B3C2B novel20 surface-action orbit preflight")
    print(f"NOVEL20_ORBITS={cert['novel20_orbit_partition']['orbit_count']}")
    print("REPRESENTATIVES=" + ",".join(cert["novel20_orbit_partition"]["orbit_representative_carrier_ids"]))
    print("CERTIFICATE_SHA256=" + cert["canonical_sha256"])


if __name__ == "__main__":
    main()
