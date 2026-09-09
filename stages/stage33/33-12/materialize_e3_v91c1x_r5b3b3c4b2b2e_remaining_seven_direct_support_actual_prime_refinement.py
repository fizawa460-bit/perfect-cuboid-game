#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
D11 = HERE.parent / "33-11d" / "stage33-11d-prime-refinement-certificate.json"
E11 = HERE.parent / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json"
C1 = HERE / "e3-v91c1x-r5b3b3c4b2b2c1-inherited-direct-support-primality-recheck.json"
C2 = HERE / "e3-v91c1x-r5b3b3c4b2b2c2-lin024-actual-four-component-prime-incidence.json"
D = HERE / "e3-v91c1x-r5b3b3c4b2b2d-offboundary-residue-reconciliation-and-direct-support-repair-scope.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2e-remaining-seven-direct-support-actual-prime-refinement.json"

LOCKS = {
    D11: "b45da57ac9b04b744dbdc44a69b80cc3acca42c30e62db6351903d6be3aafc4d",
    E11: "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426",
    C1: "64e25e200f4f0188731a6c85e1e69e6eae85a759403ac0d984309b3dca881b39",
    C2: "68d1be09543e79e210dc3e1e13d9f3e9cee3eb08d1b576238b5889e2a995e59f",
    D: "8a98066e2667c990291f59dbfd3501f6f32ff010d7b9696a3dc32b339e1dc8a9",
}
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
LIN024 = "437ad2bc8c4c25e8a2078e663cbca3d5523efbdec3e06be6f2c1b8555c6c58f7"
I = sp.I


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    expected = LOCKS[path]
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved: {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def pstr(expr: sp.Expr) -> str:
    return str(sp.expand(expr)).replace("**", "^").replace("I", "i")


def parse_expr(text: str, loc: dict[str, sp.Expr]) -> sp.Expr:
    return sp.expand(sp.sympify(text.replace("^", "**").replace("=0", ""), locals=loc))


def canonical_groebner(gens: list[sp.Expr], variables: tuple[sp.Symbol, ...]) -> tuple[str, list[str]]:
    gb = sp.groebner(gens, *variables, order="grevlex", extension=I)
    basis = [sp.srepr(sp.expand(poly.as_expr())) for poly in gb.polys]
    return csha(basis), basis


def factor_signature(poly: sp.Expr, variables: tuple[sp.Symbol, ...]) -> list[dict]:
    _, facs = sp.factor_list(sp.expand(poly), *variables, extension=I)
    rows = []
    for f, e in facs:
        q = sp.Poly(f, *variables, extension=I)
        rows.append({
            "degree": int(q.total_degree()),
            "exponent": int(e),
            "factor_sha256": csha(sp.srepr(sp.expand(q.as_expr()))),
        })
    return sorted(rows, key=lambda r: (r["degree"], r["factor_sha256"]))


def find_direct_support_records(obj: object) -> list[dict]:
    found: list[dict] = []

    def walk(x: object) -> None:
        if isinstance(x, dict):
            if x.get("kind") == "AUDITED_33_11D_DIRECT_PRIME_SUPPORT":
                if {"carrier_id", "prime_id", "reduced_support"} <= set(x):
                    found.append({
                        "carrier_id": str(x["carrier_id"]),
                        "old_prime_id": str(x["prime_id"]),
                        "reduced_support": str(x["reduced_support"]),
                        "scheme_multiplicity_in_carrier": int(x.get("scheme_multiplicity_in_carrier", 1)),
                    })
            for value in x.values():
                walk(value)
        elif isinstance(x, list):
            for value in x:
                walk(value)

    walk(obj)
    unique = {(r["carrier_id"], r["old_prime_id"], r["reduced_support"]): r for r in found}
    return sorted(unique.values(), key=lambda r: (r["carrier_id"], r["reduced_support"], r["old_prime_id"]))


def diff_domain_proof(residual: sp.Expr, qvars: tuple[sp.Symbol, ...]) -> dict:
    sig = factor_signature(residual, qvars)
    rank = int(sp.hessian(sp.expand(residual), qvars).rank())
    if rank != 3 or len(sig) != 1 or sig[0]["degree"] != 2 or sig[0]["exponent"] != 1:
        raise SystemExit(f"rank-three residual quadric irreducibility gate moved: residual={residual} rank={rank} sig={sig}")
    return {
        "proof_kind": "RANK_THREE_HOMOGENEOUS_QUADRIC_IRREDUCIBLE_OVER_QI",
        "residual_homogeneous_quadratic": pstr(residual),
        "residual_quadratic_rank": rank,
        "factor_signature_over_Qi": sig,
        "rank_three_quadric_cannot_factor_as_two_linear_forms": True,
        "quotient_is_domain_over_Qi": True,
        "actual_component_ideal_is_prime": True,
        "affine_cone_dimension": 2,
        "projective_component_dimension": 1,
        "height_in_surface": 1,
    }


def axis_domain_proof(R: sp.Expr, S: sp.Expr, qvars: tuple[sp.Symbol, ...]) -> dict:
    rf = factor_signature(R, qvars)
    sf = factor_signature(S, qvars)
    rsf = factor_signature(sp.expand(R*S), qvars)
    if len(rf) != 2 or len(sf) != 2 or len(rsf) != 4:
        raise SystemExit(f"axis radicand factor pattern moved: {R=} {S=} {rf=} {sf=} {rsf=}")
    if any(r["degree"] != 1 or r["exponent"] != 1 for r in rf + sf + rsf):
        raise SystemExit("axis radicand odd linear factor proof moved")
    gcd = sp.gcd(sp.Poly(R, *qvars, extension=I), sp.Poly(S, *qvars, extension=I))
    if gcd.total_degree() != 0:
        raise SystemExit(f"axis radicands lost coprimality: {R=} {S=} gcd={gcd}")
    return {
        "proof_kind": "SEQUENTIAL_BIQUADRATIC_DOMAIN_FROM_INDEPENDENT_SQUARECLASSES",
        "first_radicand": pstr(R),
        "second_radicand": pstr(S),
        "first_radicand_factor_signature": rf,
        "second_radicand_factor_signature": sf,
        "product_radicand_factor_signature": rsf,
        "radicands_coprime_over_Qi": True,
        "first_radicand_nonsquare": True,
        "second_radicand_nonsquare": True,
        "second_over_first_squareclass_nonsquare": True,
        "squareclass_rank_two": True,
        "sequential_quadratic_extension_is_domain": True,
        "actual_component_ideal_is_prime": True,
        "affine_cone_dimension": 2,
        "projective_component_dimension": 1,
        "height_in_surface": 1,
    }


def build() -> dict:
    d11 = load(D11)
    e11 = load(E11)
    c1 = load(C1)
    c2 = load(C2)
    d = load(D)

    if d["next_exact_leaf"] != "V91C1X_R5_DIRECT_SUPPORT_PRIME_REPAIR_CHECKPOINT_REFINE_REMAINING_SEVEN_SUPPORT_LABELS_THEN_REPLAY_STAGE33_11E_PRIME_TRANSPORT_BEFORE_FURTHER_LARGE_ACCUMULATION":
        raise SystemExit("C4B2B2D next repair leaf gate moved")
    if d["stage33_11e_direct_support_repair_scope"]["support_labels_still_without_actual_component_refinement"] != 7:
        raise SystemExit("remaining-seven repair count moved")
    if c1["inherited_direct_recheck"]["recorded_support_pseudo_prime_count"] != 9:
        raise SystemExit("C4B2B2C1 nine-support count moved")
    if c2["component_refinement"]["old_support_label_count"] != 2 or c2["component_refinement"]["actual_height_one_prime_count"] != 4:
        raise SystemExit("LIN024 completed refinement count moved")

    direct_records = find_direct_support_records(e11)
    if len(direct_records) != 9:
        raise SystemExit(f"historical 33-11e direct support record count moved: {len(direct_records)}")
    by_carrier: dict[str, list[dict]] = {}
    for row in direct_records:
        by_carrier.setdefault(row["carrier_id"], []).append(row)

    d11_records = list(d11["inherited_direct_refinements"]["records"])
    if len(d11_records) != 6 or d11["inherited_direct_refinements"]["carrier_count"] != 6:
        raise SystemExit("33-11d inherited direct carrier count moved")
    type_by_carrier = {r["carrier_id"]: r["refinement_scout"]["type"] for r in d11_records}
    if type_by_carrier.get(LIN024) != "AXIS_B2_ZERO":
        raise SystemExit("LIN024 direct type moved")

    lin_old = {r["old_support_id"] for r in c2["component_refinement"]["rows"]}
    e11_lin_old = {r["old_prime_id"] for r in by_carrier[LIN024]}
    if lin_old != e11_lin_old or len(lin_old) != 2:
        raise SystemExit("LIN024 old support binding to 33-11e moved")

    a1, a2, a3, b1, b2, b3, cv = variables = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    loc = {str(v): v for v in variables} | {"i": I}
    Q = [
        a1**2 + a2**2 - b3**2,
        a2**2 + a3**2 - b1**2,
        a1**2 + a3**2 - b2**2,
        a1**2 + a2**2 + a3**2 - cv**2,
    ]

    diff_specs = {
        "DIFF_C_MINUS_B1": {
            "carrier": cv-b1, "support": a1,
            "branch_pairs": ((b2, a3), (b3, a2)),
            "residual": b1**2-a2**2-a3**2, "residual_vars": (a2, a3, b1),
        },
        "DIFF_C_MINUS_B2": {
            "carrier": cv-b2, "support": a2,
            "branch_pairs": ((b1, a3), (b3, a1)),
            "residual": b2**2-a1**2-a3**2, "residual_vars": (a1, a3, b2),
        },
        "DIFF_C_MINUS_B3": {
            "carrier": cv-b3, "support": a3,
            "branch_pairs": ((b1, a2), (b2, a1)),
            "residual": b3**2-a1**2-a2**2, "residual_vars": (a1, a2, b3),
        },
    }
    axis_specs = {
        "AXIS_B1_ZERO": {
            "carrier": b1, "cbase": a1,
            "radicands": (a1**2+a3**2, a1**2-a3**2), "radicand_vars": (a1, a3),
        },
        "AXIS_B3_ZERO": {
            "carrier": b3, "cbase": a3,
            "radicands": (a2**2+a3**2, a3**2-a2**2), "radicand_vars": (a2, a3),
        },
    }

    out_rows: list[dict] = []
    repaired_old_ids: set[str] = set()
    for rec in sorted(d11_records, key=lambda r: r["carrier_id"]):
        cid = rec["carrier_id"]
        typ = rec["refinement_scout"]["type"]
        if cid == LIN024:
            continue
        old_rows = by_carrier.get(cid, [])
        if typ in diff_specs:
            if len(old_rows) != 1:
                raise SystemExit(f"historical direct diff support multiplicity moved: {typ}: {len(old_rows)}")
            old = old_rows[0]
            spec = diff_specs[typ]
            if parse_expr(old["reduced_support"], loc) != spec["support"]:
                raise SystemExit(f"historical reduced support moved: {typ}: {old['reduced_support']}")
            domain = diff_domain_proof(spec["residual"], spec["residual_vars"])
            components = []
            for s1 in (1, -1):
                for s2 in (1, -1):
                    (x1, y1), (x2, y2) = spec["branch_pairs"]
                    extra = [sp.expand(x1-s1*y1), sp.expand(x2-s2*y2)]
                    gens = Q + [spec["carrier"], spec["support"]] + extra
                    pid, basis = canonical_groebner(gens, variables)
                    components.append({
                        "actual_prime_id": pid,
                        "canonical_groebner_basis_sha256": csha(basis),
                        "actual_prime_generators": [pstr(g) for g in gens],
                        "branch_relations": [pstr(g) for g in extra],
                        "quotient_domain_proof": domain,
                    })
            if len({r["actual_prime_id"] for r in components}) != 4:
                raise SystemExit(f"diff component prime count moved: {typ}")
        elif typ in axis_specs:
            if len(old_rows) != 2:
                raise SystemExit(f"historical direct axis support multiplicity moved: {typ}: {len(old_rows)}")
            spec = axis_specs[typ]
            allowed = {parse_expr(str(x), loc) for x in rec["refinement_scout"]["reduced_linear_branches_over_Qi"]}
            if {parse_expr(r["reduced_support"], loc) for r in old_rows} != allowed:
                raise SystemExit(f"historical axis support labels moved: {typ}")
            domain = axis_domain_proof(spec["radicands"][0], spec["radicands"][1], spec["radicand_vars"])
            for old in sorted(old_rows, key=lambda r: r["reduced_support"]):
                sup = parse_expr(old["reduced_support"], loc)
                components = []
                for cs in (1, -1):
                    crel = sp.expand(cv-cs*spec["cbase"])
                    gens = Q + [spec["carrier"], sup, crel]
                    pid, basis = canonical_groebner(gens, variables)
                    components.append({
                        "actual_prime_id": pid,
                        "canonical_groebner_basis_sha256": csha(basis),
                        "actual_prime_generators": [pstr(g) for g in gens],
                        "c_branch": pstr(crel),
                        "quotient_domain_proof": domain,
                    })
                if len({r["actual_prime_id"] for r in components}) != 2:
                    raise SystemExit(f"axis component prime count moved: {typ}/{old['reduced_support']}")
                out_rows.append({
                    "carrier_id": cid,
                    "direct_type": typ,
                    "old_support_id": old["old_prime_id"],
                    "old_reduced_support": old["reduced_support"],
                    "old_scheme_multiplicity_in_carrier": old["scheme_multiplicity_in_carrier"],
                    "actual_component_count": 2,
                    "actual_components": components,
                })
                repaired_old_ids.add(old["old_prime_id"])
            continue
        else:
            raise SystemExit(f"unexpected unrepaired direct type: {typ}")

        out_rows.append({
            "carrier_id": cid,
            "direct_type": typ,
            "old_support_id": old["old_prime_id"],
            "old_reduced_support": old["reduced_support"],
            "old_scheme_multiplicity_in_carrier": old["scheme_multiplicity_in_carrier"],
            "actual_component_count": 4,
            "actual_components": components,
        })
        repaired_old_ids.add(old["old_prime_id"])

    remaining_old_ids = {r["old_prime_id"] for r in direct_records} - e11_lin_old
    if repaired_old_ids != remaining_old_ids or len(repaired_old_ids) != 7:
        raise SystemExit(f"remaining-seven old support coverage moved: repaired={len(repaired_old_ids)} expected={len(remaining_old_ids)}")

    new_ids = [c["actual_prime_id"] for row in out_rows for c in row["actual_components"]]
    if len(new_ids) != 20 or len(set(new_ids)) != 20:
        raise SystemExit(f"remaining-seven actual component count/distinctness moved: slots={len(new_ids)} distinct={len(set(new_ids))}")
    lin_ids = [r["actual_prime_id"] for r in c2["component_refinement"]["rows"]]
    if len(lin_ids) != 4 or len(set(lin_ids)) != 4 or set(lin_ids) & set(new_ids):
        raise SystemExit("repaired direct-prime 24-slot distinctness gate moved")
    repaired_24 = set(lin_ids) | set(new_ids)
    if len(repaired_24) != 24:
        raise SystemExit("nine-label to twenty-four-prime repair count moved")

    cert = {
        "schema": "stage33.e3.v91c1x.r5b3b3c4b2b2e.remaining_seven_direct_support_actual_prime_refinement.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2B2E_REMAINING_SEVEN_DIRECT_SUPPORT_ACTUAL_PRIME_REFINEMENT",
        "role": "EXACT_NONCREDIT_REPAIR_REPLACING_THE_SEVEN_UNREFINED_HISTORICAL_33_11E_DIRECT_SUPPORT_PSEUDO_PRIME_LABELS_BY_TWENTY_ACTUAL_HEIGHT_ONE_COMPONENT_PRIMES_BEFORE_PRIME_LEVEL_GALOIS_TRANSPORT_REPLAY",
        "entry": {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "stage33_11d_sha256": LOCKS[D11],
            "stage33_11e_sha256": LOCKS[E11],
            "c4b2b2c1_primality_recheck_sha256": LOCKS[C1],
            "c4b2b2c2_lin024_refinement_sha256": LOCKS[C2],
            "c4b2b2d_repair_scope_sha256": LOCKS[D],
        },
        "surface_model": {
            "base_field": "Q(i)",
            "equations": [pstr(q) for q in Q],
        },
        "historical_direct_support_repair": {
            "historical_pseudo_prime_label_count": 9,
            "already_refined_LIN024_old_label_count": 2,
            "already_refined_LIN024_actual_prime_count": 4,
            "remaining_old_label_count_repaired_here": 7,
            "remaining_actual_prime_count_materialized_here": 20,
            "all_20_actual_component_ideals_prime": True,
            "all_20_actual_prime_ids_pairwise_distinct": True,
            "all_20_disjoint_from_LIN024_four_actual_prime_ids": True,
            "repaired_nine_label_actual_prime_slot_count": 24,
            "repaired_nine_label_actual_prime_ids_pairwise_distinct": True,
            "rows": out_rows,
        },
        "exact_consequence": {
            "all_nine_historical_direct_support_labels_now_have_actual_component_refinement_materialized": True,
            "historical_33_11e_prime_level_transport_certificate_still_requires_replay": True,
            "historical_33_11f_26_column_closure_still_not_reusable_as_prime_exact_repair_evidence_before_replay": True,
            "authority_unchanged": True,
            "stage33_progress_unchanged": True,
            "unramifiedness_verified": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
        },
        "next_exact_leaf": "V91C1X_R5_DIRECT_SUPPORT_PRIME_REPAIR_REPLAY_STAGE33_11E_GALOIS_TRANSPORT_ON_THE_24_ACTUAL_DIRECT_COMPONENT_PRIMES",
        "credit_firewall": {
            "authority_promotion": False,
            "authority_demotion_claim": False,
            "hostile_audit_credit": False,
            "marked_brauer_image_credit": False,
            "offboundary_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "old_labels_repaired": cert["historical_direct_support_repair"]["remaining_old_label_count_repaired_here"],
            "new_actual_primes": cert["historical_direct_support_repair"]["remaining_actual_prime_count_materialized_here"],
            "repaired_direct_actual_primes_total": cert["historical_direct_support_repair"]["repaired_nine_label_actual_prime_slot_count"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists() or json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("materialized C4B2B2E certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
