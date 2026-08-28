#!/usr/bin/env python3
"""Verify cc/ct transport of all 14 divisor packages in the refined prime basis."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
D11 = HERE.parent / "33-11d"
SOURCE = HERE / "stage33-11e-source-lock.json"
OUT = HERE / "stage33-11e-prime-galois-transport-certificate.json"
SOURCE_SHA = "a1bce01bb7041d9cc48bfb7ce6e6f6095afc36ef8bc08fcb1588a885ed61e2e2"
D11_CERT_SHA = "b45da57ac9b04b744dbdc44a69b80cc3acca42c30e62db6351903d6be3aafc4d"
D11_SOURCE_SHA = "a7989a2e0bd58371f7eb4692a5f905c55007606d01b6b364f25558823ca52852"
PERMS = {"swap12": [1, 0, 2, 4, 3, 5, 6], "swap13": [2, 1, 0, 5, 4, 3, 6]}


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path, expected=None):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed or (expected is not None and claimed != expected):
        raise SystemExit(f"canonical lock mismatch: {path}")
    return obj


def qi(z):
    return Fraction(z[0], z[1]), Fraction(z[2], z[3])


def qmul(x, y):
    return x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0]


def qinv(x):
    den = x[0]*x[0] + x[1]*x[1]
    return x[0]/den, -x[1]/den


def qenc(x):
    return x[0].numerator, x[0].denominator, x[1].numerator, x[1].denominator


def normalize_signature(sig):
    vals = [qi(z) for z in sig]
    pivot = next(x for x in vals if x != (0, 0))
    inv = qinv(pivot)
    return tuple(qenc(qmul(x, inv)) for x in vals)


def act_signature(sig, action):
    if action == "cc":
        return normalize_signature([(z[0], z[1], -z[2], z[3]) for z in sig])
    if action in PERMS:
        return normalize_signature([sig[j] for j in PERMS[action]])
    if action == "ct":
        return normalize_signature(sig)
    raise SystemExit(f"unknown signature action: {action}")


def pstr(expr):
    return str(sp.expand(expr)).replace("**", "^").replace("I", "i")


def canonical_ideal(generators, variables):
    gb = sp.groebner(generators, *variables, order="grevlex", extension=sp.I)
    basis = [sp.srepr(sp.expand(poly.as_expr())) for poly in gb.polys]
    return csha(basis), basis


def act_expr(expr, action, variables):
    if action == "cc":
        return sp.expand(expr.xreplace({sp.I: -sp.I}))
    if action in PERMS:
        perm = PERMS[action]
        return sp.expand(expr.xreplace({variables[i]: variables[perm[i]] for i in range(7)}))
    if action == "ct":
        return sp.expand(expr)
    raise SystemExit(action)


def apply_word_expr(expr, word, variables):
    for action in word:
        expr = act_expr(expr, action, variables)
    return sp.expand(expr)


def apply_word_signature(sig, word):
    for action in word:
        sig = act_signature(sig, action)
    return sig


def linear_from_signature(sig, variables):
    out = 0
    for z, var in zip(sig, variables):
        re, im = qi(z)
        out += (sp.Rational(re.numerator, re.denominator)
                + sp.I*sp.Rational(im.numerator, im.denominator))*var
    return sp.expand(out)


def parse_poly(text, local):
    return sp.expand(sp.sympify(text.replace("^", "**"), locals=local))


def canonical_linear(expr, variables):
    poly = sp.Poly(expr, *variables, extension=sp.I)
    terms = poly.terms()
    if not terms:
        raise SystemExit("zero direct support")
    return pstr(sp.expand(expr / terms[0][1]))


def add_vector(out, key, value):
    out[key] = out.get(key, 0) + int(value)
    if out[key] == 0:
        del out[key]


def build_certificate():
    source = load_checked(SOURCE, SOURCE_SHA)
    d11 = load_checked(D11 / "stage33-11d-prime-refinement-certificate.json", D11_CERT_SHA)
    d11_source = load_checked(D11 / "stage33-11d-source-lock.json", D11_SOURCE_SHA)
    if source["audited_stage33_11d"]["hostile_audit_verdict"] != "PASS_STAGE33_11D_CARRIER_PRIME_REFINEMENT":
        raise SystemExit("33-11d audit PASS missing")
    if d11["summary"]["actual_height_one_prime_refinement_coverage"] != "30/30":
        raise SystemExit("33-11d coverage moved")

    inventory = {
        h: tuple(tuple(z) for z in sig)
        for h, sig in source["carrier_inventory"].items()
    }
    by_signature = {sig: h for h, sig in inventory.items()}
    if len(inventory) != 30 or len(by_signature) != 30:
        raise SystemExit("carrier inventory regression")
    carrier_actions = {g: {} for g in ("cc", "ct")}
    for g in carrier_actions:
        for h, sig in inventory.items():
            image = by_signature.get(act_signature(sig, g))
            if image is None:
                raise SystemExit(f"carrier inventory not closed under {g}")
            carrier_actions[g][h] = image

    a1, a2, a3, b1, b2, b3, c = variables = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    local = {str(x): x for x in variables} | {"i": sp.I}
    Q = [
        a1**2 + a2**2 - b3**2,
        a2**2 + a3**2 - b1**2,
        a1**2 + a3**2 - b2**2,
        a1**2 + a2**2 + a3**2 - c**2,
    ]
    orbit_by_rep = {
        row["representative_signature_sha256"]: row
        for row in d11_source["geometric_orbits"]
    }

    refinements = {}
    prime_records = {}
    ideal_generators = {}
    algebraic_carriers = set()
    for row in d11["new_exact_representative_refinements"]:
        rep_hash = row["representative_signature_sha256"]
        rep_sig = tuple(tuple(z) for z in orbit_by_rep[rep_hash]["representative_signature"])
        for carrier_id, word in row["transport_words_from_representative"].items():
            transported_sig = apply_word_signature(rep_sig, word)
            if by_signature.get(transported_sig) != carrier_id:
                raise SystemExit("33-11d transport word/carrier mismatch")
            pieces = []
            for index, component in enumerate(row["components"]):
                raw = component["reduced_height_one_prime_generators"]
                if raw[:4] == ["Q1", "Q2", "Q3", "Q4"]:
                    generators = Q + [linear_from_signature(rep_sig, variables)]
                else:
                    generators = [parse_poly(text, local) for text in raw]
                transported = [apply_word_expr(poly, word, variables) for poly in generators]
                prime_id, basis = canonical_ideal(transported, variables)
                multiplicity = int(component["scheme_theoretic_multiplicity"])
                pieces.append({"prime_id": prime_id, "multiplicity": multiplicity})
                ideal_generators[prime_id] = transported
                prime_records.setdefault(prime_id, {
                    "prime_id": prime_id,
                    "kind": "EXACT_REDUCED_PRIME_IDEAL",
                    "canonical_groebner_basis": basis,
                    "source_representative": rep_hash,
                    "transport_provenance": [],
                })["transport_provenance"].append({
                    "carrier_id": carrier_id,
                    "representative_component_index": index,
                    "transport_word": word,
                    "scheme_multiplicity_in_carrier": multiplicity,
                })
            if carrier_id in refinements:
                raise SystemExit("carrier refined twice")
            refinements[carrier_id] = pieces
            algebraic_carriers.add(carrier_id)

    direct_carriers = set()
    direct_cc_support = {}
    for record in d11["inherited_direct_refinements"]["records"]:
        carrier_id = record["carrier_id"]
        scout = record["refinement_scout"]
        pieces = []
        if "reduced_linear_branches_over_Qi" in scout:
            support_texts = scout["reduced_linear_branches_over_Qi"]
            multiplicity = 1
        else:
            support_texts = [scout["reduced_support"].replace("=0", "")]
            multiplicity = int(scout["scheme_multiplicity_signal"])
        support_to_id = {}
        for support_text in support_texts:
            support_expr = parse_poly(support_text.replace("*", "*"), local)
            support = canonical_linear(support_expr, variables)
            prime_id = csha({"audited_direct_carrier": carrier_id, "support": support})
            support_to_id[support] = prime_id
            pieces.append({"prime_id": prime_id, "multiplicity": multiplicity})
            prime_records[prime_id] = {
                "prime_id": prime_id,
                "kind": "AUDITED_33_11D_DIRECT_PRIME_SUPPORT",
                "carrier_id": carrier_id,
                "reduced_support": support,
                "scheme_multiplicity_in_carrier": multiplicity,
            }
        for support, prime_id in support_to_id.items():
            support_expr = parse_poly(support, local)
            cc_support = canonical_linear(act_expr(support_expr, "cc", variables), variables)
            if cc_support not in support_to_id:
                raise SystemExit("audited direct support not cc-closed")
            direct_cc_support[prime_id] = support_to_id[cc_support]
        refinements[carrier_id] = pieces
        direct_carriers.add(carrier_id)

    if len(refinements) != 30 or algebraic_carriers & direct_carriers:
        raise SystemExit("30-carrier refinement partition failed")
    if set(refinements) != set(inventory):
        raise SystemExit("refinement map does not cover frozen inventory")

    prime_cc = {}
    for prime_id, generators in ideal_generators.items():
        image_id, _basis = canonical_ideal(
            [act_expr(poly, "cc", variables) for poly in generators], variables
        )
        if image_id not in ideal_generators:
            raise SystemExit("cc image prime absent from exact inventory")
        prime_cc[prime_id] = image_id
    prime_cc.update(direct_cc_support)
    prime_ct = {prime_id: prime_id for prime_id in prime_records}
    if set(prime_cc) != set(prime_records) or set(prime_ct) != set(prime_records):
        raise SystemExit("prime action incomplete")
    if any(prime_cc[prime_cc[p]] != p for p in prime_cc):
        raise SystemExit("prime cc action lost involutivity")

    # Check refinement equivariance carrier-by-carrier before consuming packages.
    carrier_refinement_checks = []
    for g, prime_action in (("cc", prime_cc), ("ct", prime_ct)):
        for carrier_id, pieces in sorted(refinements.items()):
            image = sorted(
                (prime_action[piece["prime_id"]], piece["multiplicity"])
                for piece in pieces
            )
            target_id = carrier_actions[g][carrier_id]
            target = sorted(
                (piece["prime_id"], piece["multiplicity"])
                for piece in refinements[target_id]
            )
            if image != target:
                raise SystemExit(f"{g} refinement transport mismatch for {carrier_id}")
            carrier_refinement_checks.append({
                "action": g,
                "carrier_id": carrier_id,
                "target_carrier_id": target_id,
                "prime_multiset_matches_exactly": True,
            })

    def expand(carrier_vector):
        out = {}
        for carrier_id, coefficient in carrier_vector.items():
            for piece in refinements[carrier_id]:
                add_vector(out, piece["prime_id"], coefficient * piece["multiplicity"])
        return dict(sorted(out.items()))

    def act_vector(vector, prime_action):
        out = {}
        for prime_id, coefficient in vector.items():
            add_vector(out, prime_action[prime_id], coefficient)
        return dict(sorted(out.items()))

    generator_rows = []
    total_components = 0
    for record in source["generator_records"]:
        source_direction = record["source_direction"]
        carrier_vectors = record["component_signed_carrier_vectors"]
        prime_vectors = {component: expand(vector) for component, vector in carrier_vectors.items()}
        total_components += len(prime_vectors)
        action_checks = []
        package_vector = {}
        for vector in prime_vectors.values():
            for prime_id, coefficient in vector.items():
                add_vector(package_vector, prime_id, coefficient)
        package_vector = dict(sorted(package_vector.items()))
        package_differences = {}
        for g, prime_action in (("cc", prime_cc), ("ct", prime_ct)):
            for component, vector in prime_vectors.items():
                acted = act_vector(vector, prime_action)
                candidates = record["component_galois_target_candidates"][g][component]
                matches = sorted(target for target in candidates if prime_vectors[target] == acted)
                if not matches:
                    raise SystemExit(f"{source_direction}/{component}: no prime-level {g} target")
                action_checks.append({
                    "action": g,
                    "source_component": component,
                    "matching_target_components": matches,
                    "signed_prime_vector_matches_exactly": True,
                    "source_prime_vector_sha256": csha(vector),
                    "acted_prime_vector_sha256": csha(acted),
                })
            acted_package = act_vector(package_vector, prime_action)
            difference = dict(acted_package)
            for prime_id, coefficient in package_vector.items():
                add_vector(difference, prime_id, -coefficient)
            if difference:
                raise SystemExit(f"{source_direction}: package {g}(D)-D nonzero")
            package_differences[g] = {
                "status": "ZERO_EXACT_PRIME_LEVEL",
                "nonzero_prime_coefficients": 0,
            }
        generator_rows.append({
            "source_direction": source_direction,
            "component_count": len(prime_vectors),
            "distinct_primes_in_package": len(package_vector),
            "component_signed_prime_vectors": prime_vectors,
            "action_checks": action_checks,
            "package_prime_vector_sha256": csha(package_vector),
            "prime_level_galois_differences": package_differences,
            "exact_consequence": "ZERO_EXACT_PRIME_LEVEL_CC_CT",
        })

    if len(generator_rows) != 14:
        raise SystemExit("generator coverage moved")
    cert = {
        "schema": "STAGE33_11E_PRIME_LEVEL_GALOIS_TRANSPORT_V1",
        "stage": "33-11e",
        "branch": "PRIME-LEVEL-GALOIS-TRANSPORT",
        "source_locks": {
            "stage33_11e_source_lock_sha256": source["canonical_sha256"],
            "stage33_11d_certificate_sha256": d11["canonical_sha256"],
            "stage33_11d_audited_head": source["audited_stage33_11d"]["audited_head"],
            "pr1449_carrier_certificate_sha256": source["frozen_pr1449_carrier_evidence"]["certificate_sha256"],
        },
        "prime_inventory": {
            "distinct_prime_ids": len(prime_records),
            "records": [prime_records[p] for p in sorted(prime_records)],
            "carrier_refinements": refinements,
            "carrier_refinement_equivariance_checks": carrier_refinement_checks,
        },
        "prime_actions": {
            "cc": prime_cc,
            "ct": prime_ct,
            "cc_involutive": True,
            "ct_identity_on_frozen_Qi_prime_data": True,
            "actions_total_on_prime_inventory": True,
        },
        "generator_records": generator_rows,
        "summary": {
            "working_generator_coverage": "14/14",
            "component_packages_checked": total_components,
            "carrier_prime_refinement_coverage": "30/30",
            "prime_level_cc_transport": "PASS_ALL_COMPONENTS",
            "prime_level_ct_transport": "PASS_ALL_COMPONENTS",
            "generator_prime_level_galois_difference": "ZERO_EXACT_ALL_14",
            "unresolved_prime_transports": 0,
            "stage33_11e_main_exit_condition_satisfied": True,
            "stage33_11e_status": "MAIN_COMPLETE_PENDING_AUDIT",
            "stage33_11e_audited": False,
            "stage33_11_exact_connecting_progress": "0/26",
            "exact_connecting_columns_promoted": 0,
        },
        "audit_debt": {
            "fresh_stage33_11e_audit_required": True,
            "prime_level_transport_unresolved": False,
            "carrier_only_equality_used_as_prime_substitute": False,
            "next_after_audit": "33-11f_26_COLUMN_EXACT_CLOSURE",
        },
        "actions_preflight": {
            "workflow_kind": "single lightweight exact local verifier",
            "planned_effective_heavy_concurrency": 0,
            "planned_total_jobs": 2,
            "new_actions_artifacts_uploaded": 0,
            "projected_new_artifact_storage_bytes": 0,
            "repository_operating_budget_mb": 500,
            "storage_peak_safe": True,
        },
        "firewalls": {
            "exact_and_main_working_progress_separated": True,
            "stage33_11_closed_exact": False,
            "stage33_12_released": False,
            "stage33_08_released": False,
            "stage33_07_closed": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-certificate", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write_certificate:
        OUT.write_text(text, encoding="utf-8")
    else:
        if not OUT.exists() or load_checked(OUT) != cert:
            raise SystemExit("recorded 33-11e certificate differs")
    print("STAGE33_11E_PRIME_LEVEL_GALOIS_TRANSPORT=PASS")
    print("WORKING_GENERATORS=14/14")
    print("UNRESOLVED_PRIME_TRANSPORTS=0")
    print("GENERATOR_GALOIS_DIFFERENCE=ZERO_EXACT_ALL_14")
    print("STAGE33_11E_STATUS=MAIN_COMPLETE_PENDING_AUDIT")
    print("EXACT_CONNECTING_PROGRESS=0/26")
    print("CERTIFICATE_SHA256=" + cert["canonical_sha256"])


if __name__ == "__main__":
    main()
