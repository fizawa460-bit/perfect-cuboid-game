#!/usr/bin/env python3
"""Exact first carrier-prime refinement for Stage33-11d.

The verifier works over Q(i), checks the frozen #1449 carrier/orbit handoff,
proves five representative decompositions by exact Groebner ideal
intersections, and records the remaining three representatives without using a
working purity convention.  With --write-certificate it materializes the
deterministic certificate; argumentless execution verifies the checked-in one.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from fractions import Fraction
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "stage33-11d-source-lock.json"
OUT = HERE / "stage33-11d-prime-refinement-certificate.json"
COORD_NAMES = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
EXPECTED_REPS = [
    "2e722a596b0b1bbbae15627fa242d2d40e8c2644af0dc304794b9e56aa0758a7",
    "08ff6ec13783579af6e27191bacb0629b63b5b6a9e8427f82fc89d9a513e5371",
    "3391419a957d94cd764c183c742c7c87bbdcfb5cd19705c9c5cfc6054a3a610b",
    "0b6cf3cef3a98a1d0aaefd163f620a137fc5079e9899a8aabdf2cd40e4821c49",
    "3fccacee6062d9d2a6cd9456589ffeb534cb8e6df2ef8e1c79f3b38cf3f2e145",
    "18ec52da066551e7adeaf9574658f243738c43afc8dd2491ba16207a48841842",
    "07895739ca2cfe72ad76e981568c82eb660f1ff9987003fa766a0309aa857e26",
    "231089ddfcbb0ffdf649192eaea857a1cb8ed3714d8ebef2fdf7b21e05370a0f",
]


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical hash mismatch: {path.name}")
    return obj


def qi(z):
    return Fraction(z[0], z[1]), Fraction(z[2], z[3])


def qmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def qinv(x):
    d = x[0] * x[0] + x[1] * x[1]
    if not d:
        raise SystemExit("zero projective signature")
    return x[0] / d, -x[1] / d


def qenc(x):
    return x[0].numerator, x[0].denominator, x[1].numerator, x[1].denominator


def normalize(sig):
    vals = [qi(z) for z in sig]
    pivot = next(x for x in vals if x != (0, 0))
    inv = qinv(pivot)
    return tuple(qenc(qmul(x, inv)) for x in vals)


def cc(sig):
    return normalize([(z[0], z[1], -z[2], z[3]) for z in sig])


def swap(sig, perm):
    return normalize([sig[j] for j in perm])


def sid(sig):
    return csha([list(z) for z in sig])


def expr_key(expr):
    return sp.srepr(sp.expand(expr))


def ideal_intersection(left, right, variables, selector):
    gb = sp.groebner(
        [selector * f for f in left] + [(1 - selector) * f for f in right],
        selector,
        *variables,
        order="lex",
        extension=sp.I,
    )
    return [p.as_expr() for p in gb.polys if not p.as_expr().has(selector)]


def same_ideal(left, right, variables):
    gl = sp.groebner(left, *variables, order="grevlex", extension=sp.I)
    gr = sp.groebner(right, *variables, order="grevlex", extension=sp.I)
    return (
        all(gr.reduce(f)[1] == 0 for f in left)
        and all(gl.reduce(f)[1] == 0 for f in right)
    )


def intersection_all(ideals, variables, selector):
    result = ideals[0]
    for ideal in ideals[1:]:
        result = ideal_intersection(result, ideal, variables, selector)
    return result


def conic_rank_three(conic, variables):
    matrix = sp.hessian(conic, variables) / 2
    return sp.Poly(conic, *variables).total_degree() == 2 and matrix.rank() == 3


def pstr(expr):
    return str(sp.expand(expr)).replace("**", "^").replace("I", "i")


def component_record(ideal, radical, conic, multiplicity, variables):
    if not conic_rank_three(conic, variables):
        raise SystemExit("residual conic lost rank three")
    return {
        "primary_ideal_generators": [pstr(x) for x in ideal],
        "reduced_height_one_prime_generators": [pstr(x) for x in radical],
        "scheme_theoretic_multiplicity": multiplicity,
        "prime_proof": {
            "triangular_linear_elimination": True,
            "residual_homogeneous_quadratic": pstr(conic),
            "residual_quadratic_rank": 3,
            "rank_three_quadratic_cannot_factor_as_two_linear_forms": True,
            "quotient_is_domain_over_Qi": True,
            "affine_cone_dimension": 2,
            "projective_component_dimension": 1,
            "height_in_surface": 1,
        },
    }


def build_case(case, V, Q, selector):
    a1, a2, a3, b1, b2, b3, c = V
    components = []
    if case == "a1=0":
        l = a1
        for e in (-1, 1):
            for h in (-1, 1):
                for k in (-1, 1):
                    conic = b1**2 - a2**2 - a3**2
                    prime = [a1, b3 - e*a2, b2 - h*a3, c - k*b1, conic]
                    components.append((prime, prime, conic, 1))
    elif case in ("a2+a3+b1=0", "a2-a3-b1=0"):
        is_sum = case.startswith("a2+a3")
        l = a2 + a3 + b1 if is_sum else a2 - a3 - b1
        for e in (-1, 1):
            for k in (-1, 1):
                conic = b2**2 - a1**2 - a3**2
                prime = [l, a2, b1 + a3, b3 - e*a1, c - k*b2, conic]
                components.append((prime, prime, conic, 1))
        for h in (-1, 1):
            for k in (-1, 1):
                conic = b3**2 - a1**2 - a2**2
                b1_relation = b1 + a2 if is_sum else b1 - a2
                prime = [l, a3, b1_relation, b2 - h*a1, c - k*b3, conic]
                components.append((prime, prime, conic, 1))
    elif case == "a1+b3=0":
        l = a1 + b3
        for e in (-1, 1):
            for k in (-1, 1):
                conic = b2**2 - a1**2 - a3**2
                primary = [l, a2**2, b1 - e*a3, c - k*b2, conic]
                radical = [l, a2, b1 - e*a3, c - k*b2, conic]
                components.append((primary, radical, conic, 2))
    elif case == "b3+c=0":
        l = b3 + c
        for e in (-1, 1):
            for h in (-1, 1):
                conic = b3**2 - a1**2 - a2**2
                primary = [l, a3**2, b2 - e*a1, b1 - h*a2, conic]
                radical = [l, a3, b2 - e*a1, b1 - h*a2, conic]
                components.append((primary, radical, conic, 2))
    else:
        raise SystemExit(f"unknown exact case: {case}")

    section = Q + [l]
    intersection = intersection_all([x[0] for x in components], V, selector)
    if not same_ideal(section, intersection, V):
        raise SystemExit(f"primary decomposition failed: {case}")
    records = [component_record(*row, V) for row in components]
    multiplicities = sorted({row[3] for row in components})
    return {
        "carrier_equation": case,
        "section_ideal": ["Q1", "Q2", "Q3", "Q4", case],
        "exact_primary_decomposition_verified_by_ideal_intersection": True,
        "reduced_support_and_scheme_multiplicity_recorded_separately": True,
        "component_count": len(records),
        "component_multiplicities": multiplicities,
        "components": records,
    }


def orbit_words(rep, inventory_by_sig, perms):
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
    return {
        inventory_by_sig[sig]: word
        for sig, word in words.items() if sig in inventory_by_sig
    }


def build_certificate():
    source = load_checked(SOURCE)
    if source["handoff_summary"]["unresolved_geometric_representative_hashes"] != EXPECTED_REPS:
        raise SystemExit("representative order/hash moved")
    inventory = {
        h: tuple(tuple(z) for z in sig)
        for h, sig in source["carrier_inventory"].items()
    }
    if len(inventory) != 30 or any(sid(sig) != h for h, sig in inventory.items()):
        raise SystemExit("carrier signature hash regression")
    inventory_by_sig = {sig: h for h, sig in inventory.items()}
    if len(inventory_by_sig) != 30:
        raise SystemExit("duplicate normalized carrier signature")
    perms = source["certified_actions"]
    orbit_by_rep = {row["representative_signature_sha256"]: row for row in source["geometric_orbits"]}
    if set(EXPECTED_REPS) - set(orbit_by_rep):
        raise SystemExit("representative absent from frozen orbit partition")

    zero = (0, 1, 0, 1)
    one = (1, 1, 0, 1)
    minus_one = (-1, 1, 0, 1)
    minus_i = (0, 1, -1, 1)
    expected_signatures = {
        EXPECTED_REPS[0]: (zero, one, one, one, zero, zero, zero),
        EXPECTED_REPS[1]: (zero, zero, zero, one, zero, minus_one, one),
        EXPECTED_REPS[2]: (zero, zero, zero, zero, one, minus_i, minus_one),
        EXPECTED_REPS[3]: (zero, zero, zero, one, zero, one, minus_one),
        EXPECTED_REPS[4]: (zero, zero, zero, zero, zero, one, one),
        EXPECTED_REPS[5]: (one, zero, zero, zero, zero, one, zero),
        EXPECTED_REPS[6]: (zero, one, minus_one, minus_one, zero, zero, zero),
        EXPECTED_REPS[7]: (one, zero, zero, zero, zero, zero, zero),
    }
    for rep_hash, expected_sig in expected_signatures.items():
        recorded_sig = tuple(tuple(z) for z in orbit_by_rep[rep_hash]["representative_signature"])
        if normalize(recorded_sig) != normalize(expected_sig) or sid(expected_sig) != rep_hash:
            raise SystemExit("representative carrier equation/signature mismatch")

    exact_cases = {
        EXPECTED_REPS[0]: "a2+a3+b1=0",
        EXPECTED_REPS[4]: "b3+c=0",
        EXPECTED_REPS[5]: "a1+b3=0",
        EXPECTED_REPS[6]: "a2-a3-b1=0",
        EXPECTED_REPS[7]: "a1=0",
    }
    unresolved_equations = {
        EXPECTED_REPS[1]: "b1-b3+c=0",
        EXPECTED_REPS[2]: "b2-i*b3-c=0",
        EXPECTED_REPS[3]: "b1+b3-c=0",
    }

    a1, a2, a3, b1, b2, b3, c = V = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    selector = sp.Symbol("decomposition_selector")
    Q = [
        a1**2 + a2**2 - b3**2,
        a2**2 + a3**2 - b1**2,
        a1**2 + a3**2 - b2**2,
        a1**2 + a2**2 + a3**2 - c**2,
    ]
    exact_rows = []
    newly_refined_original = []
    for rep_hash in EXPECTED_REPS:
        if rep_hash not in exact_cases:
            continue
        orbit = orbit_by_rep[rep_hash]
        rep = tuple(tuple(z) for z in orbit["representative_signature"])
        if sid(rep) != rep_hash:
            raise SystemExit("representative signature/hash mismatch")
        words = orbit_words(rep, inventory_by_sig, perms)
        expected_ids = sorted(orbit["original_carrier_ids"])
        if sorted(words) != expected_ids:
            raise SystemExit("certified action transport does not cover original carriers")
        row = build_case(exact_cases[rep_hash], V, Q, selector)
        row.update({
            "representative_signature_sha256": rep_hash,
            "geometric_orbit_id": orbit["orbit_id"],
            "original_carrier_ids": expected_ids,
            "transport_words_from_representative": words,
            "transport_uses_only_certified_surface_automorphisms": True,
        })
        exact_rows.append(row)
        newly_refined_original.extend(expected_ids)

    unresolved_rows = []
    unresolved_original = []
    for rep_hash in EXPECTED_REPS:
        if rep_hash not in unresolved_equations:
            continue
        orbit = orbit_by_rep[rep_hash]
        ids = sorted(orbit["original_carrier_ids"])
        unresolved_original.extend(ids)
        unresolved_rows.append({
            "representative_signature_sha256": rep_hash,
            "carrier_equation": unresolved_equations[rep_hash],
            "geometric_orbit_id": orbit["orbit_id"],
            "original_carrier_ids": ids,
            "status": "UNRESOLVED_PRIMARY_DECOMPOSITION_NOT_PROMOTED",
            "attempted_exact_method": "local substitution plus exact Groebner elimination over Q(i)",
            "reason_for_stop": "no certified irreducibility or complete primary decomposition yet",
        })

    direct_ids = sorted(row["carrier_id"] for row in source["direct_refinement_records"])
    all_ids = set(inventory)
    partition = set(direct_ids) | set(newly_refined_original) | set(unresolved_original)
    if partition != all_ids or sum(map(len, [direct_ids, newly_refined_original, unresolved_original])) != 30:
        raise SystemExit("30-carrier accounting is not a disjoint exact partition")

    cert = {
        "schema": "STAGE33_11D_CARRIER_PRIME_REFINEMENT_V1",
        "stage": "33-11d",
        "branch": "CARRIER-PRIME-REFINEMENT",
        "source_locks": {
            "pr1449_handoff_sha256": source["canonical_sha256"],
            "authoritative_run_id": 33213248650,
            "authoritative_run_number": 92,
            "authoritative_run_head_sha": "532d6047780e89f97813980a43458b1dd3f9b251",
            "carrier_certificate_sha256": source["artifact"]["files"]["stage33-11-all-generator-strict-transform-carriers.json"]["canonical_sha256"],
            "orbit_certificate_sha256": source["artifact"]["files"]["stage33-11-carrier-geometric-orbit-reduction.json"]["canonical_sha256"],
        },
        "exact_algebra": {
            "base_field": "Q(i)",
            "surface_equations": source["surface_model"]["equations"],
            "backend": "SymPy exact QQ_I Groebner bases",
            "remote_CAS_used": False,
            "smith_computation_used": False,
        },
        "inherited_direct_refinements": {
            "carrier_count": len(direct_ids),
            "carrier_ids": direct_ids,
            "records": source["direct_refinement_records"],
            "recomputed_in_33_11d": False,
        },
        "new_exact_representative_refinements": exact_rows,
        "explicit_unresolved_representatives": unresolved_rows,
        "summary": {
            "working_generator_carrier_inventory": "30/30_ACCOUNTED",
            "frozen_unresolved_geometric_representatives": 8,
            "new_exact_representative_refinements": len(exact_rows),
            "remaining_unresolved_geometric_representatives": len(unresolved_rows),
            "inherited_direct_carriers": len(direct_ids),
            "newly_refined_original_carriers_by_certified_orbit_transport": len(newly_refined_original),
            "remaining_unresolved_original_carriers": len(unresolved_original),
            "newly_refined_original_carrier_ids": sorted(newly_refined_original),
            "remaining_unresolved_original_carrier_ids": sorted(unresolved_original),
            "all_30_carriers_disjointly_accounted": True,
            "stage33_11d_status": "OPEN_UNRESOLVED",
            "stage33_11d_closed": False,
            "stage33_11_exact_connecting_progress": "0/26",
            "exact_connecting_columns_promoted": 0,
        },
        "audit_debt": {
            "finite_explicit_unresolved_set": True,
            "next_exact_target_representatives": [row["representative_signature_sha256"] for row in unresolved_rows],
            "working_carrier_purity_convention_used_for_exact_promotion": False,
            "hostile_audit_required_before_33_11_exit": True,
        },
        "actions_preflight": {
            "workflow_kind": "single lightweight exact verifier",
            "planned_effective_heavy_concurrency": 0,
            "planned_total_jobs": 2,
            "new_actions_artifacts_uploaded": 0,
            "projected_new_artifact_storage_bytes": 0,
            "repository_operating_budget_mb": 500,
            "storage_peak_safe": True,
            "dedicated_commit_range_run_key_required": True,
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
        if not OUT.exists():
            raise SystemExit("certificate missing")
        recorded = load_checked(OUT)
        if recorded != cert:
            raise SystemExit("recorded certificate differs from exact regeneration")
    print("STAGE33_11D_FIRST_PRIME_REFINEMENT=PASS")
    print("NEW_EXACT_REPRESENTATIVES=5/8")
    print("REMAINING_UNRESOLVED_REPRESENTATIVES=3/8")
    print("REMAINING_UNRESOLVED_ORIGINAL_CARRIERS=11/30")
    print("STAGE33_11D_CLOSED=false")
    print("EXACT_CONNECTING_PROGRESS=0/26")
    print("CERTIFICATE_SHA256=" + cert["canonical_sha256"])


if __name__ == "__main__":
    main()
