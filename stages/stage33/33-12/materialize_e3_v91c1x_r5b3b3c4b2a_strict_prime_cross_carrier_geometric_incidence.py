#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b2d2_swap23_317_cover_common_refinement as atlas
import materialize_e3_v91c1x_r5b3b3c2c_orbit_representative_strict_prime_decomposition_and_transport as c2cmod

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C2C = HERE / "e3-v91c1x-r5b3b3c2c-orbit-representative-strict-prime-decomposition-and-transport.json"
C4A = HERE / "e3-v91c1x-r5b3b3c4a-tame-residue-parity-and-cross-carrier-preflight.json"
H2 = HERE / "e3-v91c1x-r5b3b3c4b1e5h2-squareclass-gauge-to-a2-02-representative-binding-audit.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2a-strict-prime-cross-carrier-geometric-incidence.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C2C_SHA = "01fc321272106a1ce7c382783c4dcb128c164d21ee4deedf4060137ef9ed971a"
C4A_SHA = "fab3f7b1235370a3916b99b6909cd6c6363193ff271ee6b51cb9494b0668e525"
H2_SHA = "6fd0fe9ffd666c21c394dc3a0a0fc6e03cea6936af26d4d9e84b3a29cbccbe9c"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
SPECIAL_LINEAR = "44afff33ba591a11904229fe7936cb41caa700bd759cda0a5106218250561491"
SPECIAL_RESIDUAL = "da9c1c762b7deb1ac7c630325bcfa1ee9b1a44916f5bd9df410bf16c9effd5b4"
PAIR_FACTOR = "69623aeb5f2dab057c7c435c9f72d85b6670e7716c1a64d2a2b8ea3b9ec1be1b"
I = sp.I


def clean(x: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.expand(x))


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"canonical source lock moved {path.name}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def surface_quadrics(X: list[sp.Symbol]) -> list[sp.Expr]:
    a1, a2, a3, b1, b2, b3, c = X
    return [
        a1*a1 + a2*a2 - b3*b3,
        a2*a2 + a3*a3 - b1*b1,
        a1*a1 + a3*a3 - b2*b2,
        a1*a1 + a2*a2 + a3*a3 - c*c,
    ]


def carrier_form(row: dict, X: list[sp.Symbol]) -> sp.Expr:
    coeffs = [atlas.decode_element(z) for z in row["normalized_coefficients_Qi"]]
    return clean(sum(coeffs[j] * X[j] for j in range(7)))


def gbasis(gens: list[sp.Expr], X: list[sp.Symbol]) -> list[sp.Expr]:
    G = sp.groebner(gens, *X, order="grevlex", extension=I)
    return [clean(p.as_expr()) for p in G.polys]


def saturation(gens: list[sp.Expr], f: sp.Expr, X: list[sp.Symbol], tag: str) -> list[sp.Expr]:
    y = sp.Symbol(f"sat_{tag}")
    G = sp.groebner(gens + [1 - y*f], y, *X, order="lex", extension=I)
    out = [clean(p.as_expr()) for p in G.polys if not p.as_expr().has(y)]
    if not out:
        raise SystemExit(f"empty saturation basis: {tag}")
    return gbasis(out, X)


def ideals_equal(lhs: list[sp.Expr], rhs: list[sp.Expr], X: list[sp.Symbol]) -> bool:
    Gl = sp.groebner(lhs, *X, order="grevlex", extension=I)
    Gr = sp.groebner(rhs, *X, order="grevlex", extension=I)
    return (
        all(clean(Gr.reduce(sp.expand(f))[1]) == 0 for f in lhs)
        and all(clean(Gl.reduce(sp.expand(f))[1]) == 0 for f in rhs)
    )


def ideal_sha(gens: list[sp.Expr], X: list[sp.Symbol]) -> str:
    basis = gbasis(gens, X)
    return csha([atlas.encode_poly(p, X) for p in basis])


def build_member_exponents(carrier_rows: list[dict], components: list[str]):
    pi = {d: defaultdict(int) for d in components}
    ff = {d: defaultdict(int) for d in components}
    for row in carrier_rows:
        cid = row["carrier_id"]
        for app in row["appearances"]:
            d = app["symbol_component"]
            target = pi if app["member"] == "pi_D" else ff if app["member"] == "f_D" else None
            if target is None:
                raise SystemExit(f"unexpected symbol member: {app['member']}")
            target[d][cid] += int(app["exponent"])
    return pi, ff


def residue_parity(carrier_ids: list[str], components: list[str], pi: dict, ff: dict, valuation: dict[str, int]):
    odd = defaultdict(int)
    sign = 0
    for d in components:
        vpi = sum(int(pi[d].get(cid, 0)) * int(valuation.get(cid, 0)) for cid in carrier_ids)
        vf = sum(int(ff[d].get(cid, 0)) * int(valuation.get(cid, 0)) for cid in carrier_ids)
        sign ^= (vpi * vf) & 1
        for cid in carrier_ids:
            e = int(pi[d].get(cid, 0)) * vf - int(ff[d].get(cid, 0)) * vpi
            odd[cid] ^= e & 1
    return sorted(cid for cid in carrier_ids if odd[cid]), sign


def cluster_contexts(contexts: list[dict], X: list[sp.Symbol]) -> list[list[dict]]:
    clusters: list[list[dict]] = []
    for row in contexts:
        placed = False
        for cluster in clusters:
            if ideals_equal(row["_ideal"], cluster[0]["_ideal"], X):
                cluster.append(row)
                placed = True
                break
        if not placed:
            clusters.append([row])
    return clusters


def build_certificate() -> dict:
    b3b2 = load_locked(B3B2, B3B2_SHA)
    c2c = load_locked(C2C, C2C_SHA)
    c4a = load_locked(C4A, C4A_SHA)
    h2 = load_locked(H2, H2_SHA)
    if h2["next_exact_leaf"] != "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION":
        raise SystemExit("H2 handoff moved")

    repeated = c4a["strict_prime_preflight"]["repeated_factor_groups"]
    if len(repeated) != 3 or c4a["strict_prime_preflight"]["repeated_factor_context_row_count_requiring_cross_carrier_geometric_incidence"] != 10:
        raise SystemExit("C4A repeated-factor inventory moved")
    by_factor = {r["c1_normalized_factor_sha256"]: r for r in repeated}
    if set(by_factor) != {SPECIAL_LINEAR, SPECIAL_RESIDUAL, PAIR_FACTOR}:
        raise SystemExit("C4A repeated factor identities moved")

    formal = b3b2["formal_tame_symbol_sum"]
    components = list(formal["component_ids_in_source_order"])
    carrier_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    carriers = {r["carrier_id"]: r for r in carrier_rows}
    carrier_ids = [r["carrier_id"] for r in carrier_rows]
    pi, ff = build_member_exponents(carrier_rows, components)

    special_rows = {r["carrier_id"]: r for r in c2c["representative_strict_prime_decompositions"]["rows"]}
    for cid in c2cmod.SPECIAL:
        if cid not in special_rows:
            raise SystemExit(f"C2C special representative row missing: {cid}")
        cert = special_rows[cid]["special_reducible_norm_prime_decomposition_certificate"]
        if not cert["residual_prime"]["unique_minimal_prime_above_factor"]:
            raise SystemExit(f"C2C residual prime uniqueness moved: {cid}")
        if not cert["boundary_prime"]["quotient_is_domain"]:
            raise SystemExit(f"C2C boundary prime domain proof moved: {cid}")

    X = list(sp.symbols("a1 a2 a3 b1 b2 b3 c"))
    a1, a2, a3, b1, b2, b3, c = X
    surface = [clean(q) for q in surface_quadrics(X)]
    forms = {cid: carrier_form(carriers[cid], X) for cid in carriers}

    contexts_by_factor: dict[str, list[dict]] = {SPECIAL_LINEAR: [], SPECIAL_RESIDUAL: [], PAIR_FACTOR: []}
    for cid in by_factor[SPECIAL_LINEAR]["carrier_ids"]:
        spec = c2cmod.SPECIAL[cid]
        boundary = surface + [
            a1,
            clean(b2 - int(spec["b2_sign"]) * a3),
            clean(b3 - int(spec["b3_sign"]) * a2),
            clean(c - int(spec["c_over_b1_sign"]) * b1),
        ]
        contexts_by_factor[SPECIAL_LINEAR].append({"carrier_id": cid, "prime_kind": "C2C_EXPLICIT_A1_BOUNDARY_PRIME", "_ideal": gbasis(boundary, X)})

    for cid in by_factor[SPECIAL_RESIDUAL]["carrier_ids"]:
        strict_residual = saturation(surface + [forms[cid]], a1, X, f"res_{cid}")
        if any(clean(sp.groebner(strict_residual, *X, order="grevlex", extension=I).reduce(a1)[1]) == 0 for _ in [0]):
            raise SystemExit(f"residual saturation still contains a1: {cid}")
        contexts_by_factor[SPECIAL_RESIDUAL].append({"carrier_id": cid, "prime_kind": "C2C_UNIQUE_RESIDUAL_PRIME_OVER_F14", "_ideal": strict_residual})

    pair_carriers = by_factor[PAIR_FACTOR]["carrier_ids"]
    if sorted(pair_carriers) != ["LIN_013", "LIN_019"]:
        raise SystemExit("C4A pair repeated carriers moved")
    for cid in pair_carriers:
        direct = gbasis(surface + [forms[cid]], X)
        contexts_by_factor[PAIR_FACTOR].append({"carrier_id": cid, "prime_kind": "C2C_UNIQUE_REDUCED_STRICT_PRIME_OF_LINEAR_SECTION", "_ideal": direct})

    group_rows = []
    total_clusters = 0
    zero_parity_clusters = 0
    nonzero_parity_clusters = 0
    all_cross_vanishing_checks = []

    for fsha in (SPECIAL_LINEAR, SPECIAL_RESIDUAL, PAIR_FACTOR):
        contexts = contexts_by_factor[fsha]
        clusters = cluster_contexts(contexts, X)
        total_clusters += len(clusters)
        cluster_rows = []
        for k, cluster in enumerate(clusters, 1):
            representative_ideal = cluster[0]["_ideal"]
            G = sp.groebner(representative_ideal, *X, order="grevlex", extension=I)
            incident = sorted(r["carrier_id"] for r in cluster)
            exact_vanishing = sorted(cid for cid in by_factor[fsha]["carrier_ids"] if clean(G.reduce(forms[cid])[1]) == 0)
            if exact_vanishing != incident:
                raise SystemExit(f"carrier incidence differs from ideal-equality cluster for {fsha}: {incident} vs {exact_vanishing}")
            valuation = {cid: (1 if cid in incident else 0) for cid in carrier_ids}
            odd, sign = residue_parity(carrier_ids, components, pi, ff, valuation)
            if odd:
                nonzero_parity_clusters += 1
            else:
                zero_parity_clusters += 1
            cluster_rows.append({
                "geometric_prime_cluster_index": k,
                "incident_carrier_ids_exact": incident,
                "incident_carrier_count": len(incident),
                "prime_ideal_groebner_sha256": ideal_sha(representative_ideal, X),
                "combined_tame_residue_odd_linear_carrier_ids": odd,
                "combined_tame_residue_carrier_parity_zero": not odd,
                "tame_sign_parity": sign,
                "minus_one_is_square_in_Qi": True,
                "squareclass_status": "SQUARE_TRIVIAL_BY_EVEN_LINEAR_FACTOR_PARITY" if not odd else "REQUIRES_TARGETED_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
            })
            all_cross_vanishing_checks.append({"factor_sha256": fsha, "cluster_index": k, "incident_carriers": incident})

        group_rows.append({
            "c1_normalized_factor_sha256": fsha,
            "context_carrier_ids": sorted(r["carrier_id"] for r in contexts),
            "context_count": len(contexts),
            "geometrically_distinct_strict_prime_count": len(clusters),
            "all_contexts_pairwise_distinct": len(clusters) == len(contexts),
            "clusters": cluster_rows,
        })

    if sum(r["context_count"] for r in group_rows) != 10:
        raise SystemExit("C4B2A repeated context accounting moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b2a.strict_prime_cross_carrier_geometric_incidence.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B2A_STRICT_PRIME_CROSS_CARRIER_GEOMETRIC_INCIDENCE",
        "role": "EXACT_NONCREDIT_GROEBNER_AND_SATURATION_RESOLUTION_OF_THE_10_C4A_REPEATED_FACTOR_CONTEXTS_WITH_COMBINED_TAME_PARITY_RECOMPUTED_ON_ACTUAL_GEOMETRIC_PRIME_CLUSTERS",
        "entry": {"authority": AUTHORITY, "stage33_progress": "6/11", "successor_pr": 1722},
        "source_locks": {
            "r5b3b2_sha256": B3B2_SHA,
            "r5b3b3c2c_sha256": C2C_SHA,
            "c4a_sha256": C4A_SHA,
            "c4b1e5h2_sha256": H2_SHA,
        },
        "cross_carrier_incidence": {
            "repeated_factor_group_count": 3,
            "repeated_factor_context_count": 10,
            "actual_geometric_prime_cluster_count": total_clusters,
            "group_rows": group_rows,
            "all_incidence_decided_by_exact_ideal_membership_not_local_prime_id_comparison": True,
            "special_a1_boundary_primes_use_C2C_explicit_prime_ideals": True,
            "special_F14_residual_primes_use_exact_saturation_by_a1": True,
            "LIN_013_LIN_019_unique_sections_use_exact_surface_plus_carrier_ideals": True,
            "cross_vanishing_check_commitment_sha256": csha(all_cross_vanishing_checks),
        },
        "strict_prime_tame_parity_after_incidence": {
            "geometric_prime_cluster_count": total_clusters,
            "zero_formal_parity_cluster_count": zero_parity_clusters,
            "nonzero_formal_parity_cluster_count_requiring_residue_field_reduction": nonzero_parity_clusters,
            "the_18_C4A_unique_factor_contexts_remain_nonzero_formal_parity_and_also_require_residue_field_reduction": True,
        },
        "exact_consequence": {
            "C4A_repeated_factor_cross_carrier_geometric_incidence_materialized": True,
            "single_carrier_valuation_is_used_only_when_exact_ideal_incidence_proves_single_carrier_support": True,
            "zero_parity_clusters_if_any_are_exact_squaretriviality_certificates": True,
            "nonzero_parity_clusters_are_not_declared_nonsquare": True,
            "combined_tame_residue_squareclasses_audited_on_every_strict_prime": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "next_exact_leaf": "V91C1X_R5B3B3C4B2B_STRICT_PRIME_TARGETED_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "next_exact_step": "reduce the combined odd-carrier representatives in the residue fields of the 18 unique-factor strict primes plus every nonzero-parity C4B2A geometric repeated-factor prime cluster; do not infer nonsquare from nonzero formal parity",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "offboundary_cancellation_credit": False,
            "unramifiedness_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
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
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        c = cert["cross_carrier_incidence"]
        p = cert["strict_prime_tame_parity_after_incidence"]
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "repeated_contexts": c["repeated_factor_context_count"],
            "geometric_prime_clusters": c["actual_geometric_prime_cluster_count"],
            "zero_parity_clusters": p["zero_formal_parity_cluster_count"],
            "nonzero_parity_clusters": p["nonzero_formal_parity_cluster_count_requiring_residue_field_reduction"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B2A certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
