#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
C1 = HERE / "e3-v91c1x-r5b3b3c1-offboundary-norm-factorization.json"
C2B = HERE / "e3-v91c1x-r5b3b3c2b-novel20-surface-action-orbit-preflight.json"
D11 = S33 / "33-11d" / "stage33-11d-source-lock.json"
OUT = HERE / "e3-v91c1x-r5b3b3c2c-orbit-representative-strict-prime-decomposition-and-transport.json"

B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
C1_SHA = "5c092fcec6720d0097d6e7509ce37b1506d7a099015a1a6a004250513d0f29f3"
C2B_SHA = "784819b81121cc9fdd36e904efb2778e6a474079e84e2d82987c972620b32831"
D11_SHA = "a7989a2e0bd58371f7eb4692a5f905c55007606d01b6b364f25558823ca52852"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"

# These 13 representatives have irreducible degree-16 full sign norm.
# A split-prime modular specialization certifies irreducibility exactly.
WITNESSES = {
    "LIN_001": {"p":29,"i_image":12,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":5,"degree":16,"norm_terms_mod_p":148,"norm_total_degree_mod_p":16},
    "LIN_004": {"p":13,"i_image":5,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":6,"degree":14,"norm_terms_mod_p":136,"norm_total_degree_mod_p":16},
    "LIN_005": {"p":13,"i_image":5,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":2,"degree":14,"norm_terms_mod_p":136,"norm_total_degree_mod_p":16},
    "LIN_007": {"p":13,"i_image":5,"dehom":"a1","polyvar":"a2","specialized_var":"a3","specialization":7,"degree":12,"norm_terms_mod_p":68,"norm_total_degree_mod_p":16},
    "LIN_009": {"p":29,"i_image":12,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":5,"degree":16,"norm_terms_mod_p":148,"norm_total_degree_mod_p":16},
    "LIN_010": {"p":13,"i_image":5,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":11,"degree":14,"norm_terms_mod_p":136,"norm_total_degree_mod_p":16},
    "LIN_011": {"p":13,"i_image":5,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":2,"degree":14,"norm_terms_mod_p":136,"norm_total_degree_mod_p":16},
    "LIN_016": {"p":13,"i_image":5,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":7,"degree":14,"norm_terms_mod_p":136,"norm_total_degree_mod_p":16},
    "LIN_017": {"p":13,"i_image":8,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":7,"degree":14,"norm_terms_mod_p":138,"norm_total_degree_mod_p":16},
    "LIN_021": {"p":13,"i_image":5,"dehom":"a1","polyvar":"a2","specialized_var":"a3","specialization":7,"degree":12,"norm_terms_mod_p":68,"norm_total_degree_mod_p":16},
    "LIN_022": {"p":13,"i_image":5,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":11,"degree":14,"norm_terms_mod_p":136,"norm_total_degree_mod_p":16},
    "LIN_025": {"p":17,"i_image":4,"dehom":"a1","polyvar":"a2","specialized_var":"a3","specialization":3,"degree":12,"norm_terms_mod_p":110,"norm_total_degree_mod_p":16},
    "LIN_026": {"p":13,"i_image":8,"dehom":"a3","polyvar":"a1","specialized_var":"a2","specialization":2,"degree":14,"norm_terms_mod_p":138,"norm_total_degree_mod_p":16},
}

# C1 proves each of these has full sign norm a1^2 * F14 up to Q(i)^*,
# with F14 irreducible. The explicit boundary prime below contributes the
# entire a1^2 determinant valuation (residue degree 2, local multiplicity 1),
# leaving one reduced residual prime over F14.
SPECIAL = {
    "LIN_008": {"b2_sign": -1, "b3_sign": -1, "c_over_b1_sign": 1},
    "LIN_015": {"b2_sign": 1, "b3_sign": -1, "c_over_b1_sign": 1},
    "LIN_020": {"b2_sign": -1, "b3_sign": 1, "c_over_b1_sign": 1},
}
SPECIAL_FULL_NORM_SHA = "7f6274634f622b0e675111085ed050e65e4207f3f327d2c9b7a615f5f5dbf064"
SPECIAL_LINEAR_FACTOR_SHA = "44afff33ba591a11904229fe7936cb41caa700bd759cda0a5106218250561491"
SPECIAL_RESIDUAL_FACTOR_SHA = "da9c1c762b7deb1ac7c630325bcfa1ee9b1a44916f5bd9df410bf16c9effd5b4"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical hash mismatch: {path}")
    if claimed != expected:
        raise SystemExit(f"source lock moved: {path}: {claimed} != {expected}")
    return obj


def qi(z):
    return Fraction(int(z[0]), int(z[1])), Fraction(int(z[2]), int(z[3]))


def qadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def qscale(x, n):
    return x[0] * n, x[1] * n


def qmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def qinv(x):
    d = x[0] * x[0] + x[1] * x[1]
    if not d:
        raise SystemExit("zero projective coefficient pivot")
    return x[0] / d, -x[1] / d


def qenc(x):
    return (x[0].numerator, x[0].denominator, x[1].numerator, x[1].denominator)


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


def apply_word(sig, word, perms):
    out = sig
    for name in word:
        if name == "cc":
            out = cc(out)
        elif name in ("swap12", "swap13"):
            out = swap(out, perms[name])
        else:
            raise SystemExit(f"unexpected transport generator: {name}")
    return out


def coeff_mod_qi(z, p, r):
    rn, rd, inn, ind = map(int, z)
    if rd % p == 0 or ind % p == 0:
        raise SystemExit("modular witness divides a coefficient denominator")
    return (rn * pow(rd, -1, p) + r * inn * pow(ind, -1, p)) % p


def norm_mod(sig, p, r):
    a1, a2, a3, b1, b2, b3, c = vars7 = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    squares = {
        b1: a2**2 + a3**2,
        b2: a1**2 + a3**2,
        b3: a1**2 + a2**2,
        c: a1**2 + a2**2 + a3**2,
    }
    expr = sum(coeff_mod_qi(z, p, r) * v for z, v in zip(sig, vars7))
    active = list(vars7)
    for v in (b1, b2, b3, c):
        expr = sp.expand(expr * expr.xreplace({v: -v}))
        poly = sp.Poly(expr, *active, modulus=p)
        idx = active.index(v)
        out = 0
        for mon, coef in poly.terms():
            e = mon[idx]
            if e & 1:
                raise SystemExit("sign norm failed to eliminate an odd root power")
            mon2 = list(mon)
            mon2[idx] = 0
            term = int(coef)
            for vv, ee in zip(active, mon2):
                if ee:
                    term *= vv**ee
            term *= squares[v] ** (e // 2)
            out += term
        active.remove(v)
        expr = sp.Poly(sp.expand(out), *active, modulus=p).as_expr()
    return sp.Poly(expr, a1, a2, a3, modulus=p)


def poly_hash(poly, p):
    return csha([[list(mon), int(coef) % p] for mon, coef in poly.terms()])


def proof_row(cid, sig):
    w = dict(WITNESSES[cid])
    p, r = int(w["p"]), int(w["i_image"])
    if not sp.isprime(p) or p % 4 != 1 or (r * r + 1) % p != 0:
        raise SystemExit(f"invalid split Gaussian prime witness: {cid}")
    P = norm_mod(sig, p, r)
    if P.total_degree() != 16 or len(P.terms()) != int(w["norm_terms_mod_p"]):
        raise SystemExit(f"norm degree/term count moved: {cid}")
    names = {str(v): v for v in P.gens}
    dh, x, y = names[w["dehom"]], names[w["polyvar"]], names[w["specialized_var"]]
    remaining = [v for v in P.gens if v != dh]
    if sp.Poly(P.as_expr().subs(dh, 0), *remaining, modulus=p).is_zero:
        raise SystemExit(f"modular norm acquired dehomogenizing-variable factor: {cid}")
    F = sp.Poly(P.as_expr().subs(dh, 1), x, y, modulus=p)
    px = sp.Poly(F.as_expr(), x)
    g = None
    for co in px.all_coeffs():
        q = sp.Poly(co, y, modulus=p)
        g = q if g is None else sp.gcd(g, q)
    if g is None or g.degree() != 0:
        raise SystemExit(f"dehomogenized norm not primitive in polynomial variable: {cid}")
    deg = sp.Poly(F.as_expr(), x).degree()
    if deg != int(w["degree"]):
        raise SystemExit(f"dehomogenized x-degree moved: {cid}")
    un = sp.Poly(F.eval(y, int(w["specialization"])), x, modulus=p)
    if un.degree() != deg:
        raise SystemExit(f"specialization dropped polynomial degree: {cid}")
    _unit, factors = sp.factor_list(un.as_expr(), modulus=p)
    factor_shape = [[sp.Poly(f, x, modulus=p).degree(), int(e)] for f, e in factors]
    if factor_shape != [[deg, 1]]:
        raise SystemExit(f"specialized univariate witness reducible: {cid}: {factor_shape}")
    coeffs = [int(z) % p for z in un.all_coeffs()]
    w.update({
        "norm_mod_p_sha256": poly_hash(P, p),
        "norm_not_divisible_by_dehomogenizing_variable": True,
        "dehom_x_content_gcd_degree": 0,
        "specialized_univariate_coefficients_mod_p": coeffs,
        "specialized_univariate_sha256": csha(coeffs),
        "specialized_factor_degrees_exponents": factor_shape,
    })
    return w


def sign_relation(var, sign, base):
    return f"{var}-({base})" if sign == 1 else f"{var}+({base})"


def special_boundary_proof(cid, sig, c1_row):
    spec = dict(SPECIAL[cid])
    vals = [qi(z) for z in sig]
    if len(vals) != 7:
        raise SystemExit(f"unexpected carrier arity: {cid}")
    s2 = int(spec["b2_sign"])
    s3 = int(spec["b3_sign"])
    sc = int(spec["c_over_b1_sign"])
    # On a1=0, impose b2=s2*a3, b3=s3*a2, c=sc*b1.
    a2_coeff = qadd(vals[1], qscale(vals[5], s3))
    a3_coeff = qadd(vals[2], qscale(vals[4], s2))
    b1_coeff = qadd(vals[3], qscale(vals[6], sc))
    if any(z != (0, 0) for z in (a2_coeff, a3_coeff, b1_coeff)):
        raise SystemExit(f"explicit boundary prime not contained in carrier section: {cid}")

    if c1_row["normalized_full_sign_norm_sha256"] != SPECIAL_FULL_NORM_SHA:
        raise SystemExit(f"special full norm SHA moved: {cid}")
    if c1_row["factor_degree_multiset"] != [1, 1, 14]:
        raise SystemExit(f"special C1 factor-degree pattern moved: {cid}")
    factors = {int(f["factor_total_degree"]): f for f in c1_row["factors"]}
    if set(factors) != {1, 14}:
        raise SystemExit(f"special C1 distinct factor degrees moved: {cid}")
    lin, residual = factors[1], factors[14]
    if (int(lin["multiplicity"]), lin["normalized_factor_sha256"]) != (2, SPECIAL_LINEAR_FACTOR_SHA):
        raise SystemExit(f"special a1^2 factor lock moved: {cid}")
    if (int(residual["multiplicity"]), residual["normalized_factor_sha256"]) != (1, SPECIAL_RESIDUAL_FACTOR_SHA):
        raise SystemExit(f"special residual degree-14 factor lock moved: {cid}")

    normalized_a1 = [{"monomial_exponents": [1, 0, 0], "coefficient_Qi": [1, 1, 0, 1]}]
    if csha(normalized_a1) != SPECIAL_LINEAR_FACTOR_SHA:
        raise SystemExit("internal normalized a1 factor hash mismatch")

    boundary_ideal = [
        "a1",
        sign_relation("b2", s2, "a3"),
        sign_relation("b3", s3, "a2"),
        sign_relation("c", sc, "b1"),
    ]
    return {
        "method": "C1_EXACT_A1_SQUARED_TIMES_IRREDUCIBLE_DEGREE14_NORM_PLUS_EXPLICIT_BOUNDARY_PRIME_LENGTH_ACCOUNTING",
        "c1_normalized_full_sign_norm_sha256": SPECIAL_FULL_NORM_SHA,
        "c1_factorization": [
            {"base_factor": "a1", "normalized_factor_sha256": SPECIAL_LINEAR_FACTOR_SHA, "degree": 1, "determinant_valuation": 2},
            {"base_factor": "F14", "normalized_factor_sha256": SPECIAL_RESIDUAL_FACTOR_SHA, "degree": 14, "determinant_valuation": 1},
        ],
        "boundary_prime": {
            "ideal_generators_on_singular_surface": boundary_ideal,
            "carrier_vanishes_identically_mod_boundary_ideal": True,
            "quotient_model": "Q(i)[a2,a3,b1]/(b1^2-a2^2-a3^2)",
            "quotient_is_domain": True,
            "irreducibility_reason": "the homogeneous quadratic b1^2-a2^2-a3^2 has rank 3, so it cannot factor into linear forms",
            "residue_degree_over_Frac_Qi_a2_a3": 2,
            "local_multiplicity_in_carrier_section": 1,
            "determinant_length_contribution_at_a1": 2,
            "exhausts_c1_a1_determinant_valuation": True,
        },
        "residual_prime": {
            "base_factor": "F14",
            "base_factor_irreducible_by_C1_singular_factorization": True,
            "determinant_valuation": 1,
            "unique_minimal_prime_above_factor": True,
            "residue_degree": 1,
            "local_multiplicity": 1,
        },
        "principal_section_is_cohen_macaulay_unmixed": True,
        "strict_prime_count": 2,
        "strict_prime_multiplicities": [1, 1],
    }


def build_certificate():
    b3b2 = load_checked(B3B2, B3B2_SHA)
    c1 = load_checked(C1, C1_SHA)
    c2b = load_checked(C2B, C2B_SHA)
    d11 = load_checked(D11, D11_SHA)
    if c2b["source_locks"]["stage33_11d_source_lock_sha256"] != D11_SHA:
        raise SystemExit("C2B no longer locks the audited 33-11d source")
    if c2b["source_locks"]["stage33_11d_hostile_audit_verdict"] != "PASS_STAGE33_11D_CARRIER_PRIME_REFINEMENT":
        raise SystemExit("33-11d hostile-audit provenance moved")
    perms = {k: [int(x) for x in d11["certified_actions"][k]] for k in ("swap12", "swap13")}
    if perms != c2b["certified_action_model"]["coordinate_permutation_generators"]:
        raise SystemExit("C2B certified action model moved from 33-11d")

    carrier_rows = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    by_id = {row["carrier_id"]: row for row in carrier_rows}
    c1_by_id = {row["carrier_id"]: row for row in c1["exact_factorization"]["carrier_rows"]}
    reps = list(c2b["novel20_orbit_partition"]["orbit_representative_carrier_ids"])
    if len(reps) != 16 or set(reps) != set(WITNESSES) | set(SPECIAL):
        raise SystemExit("C2B representative16 set moved")
    orbit_rows = c2b["novel20_orbit_partition"]["orbits"]
    orbit_by_rep = {row["representative_carrier_id"]: row for row in orbit_rows}
    if set(orbit_by_rep) != set(reps):
        raise SystemExit("C2B orbit rows moved")

    rep_rows = []
    transport_rows = []
    covered = []
    for cid in reps:
        row = by_id[cid]
        sig = normalize(row["normalized_coefficients_Qi"])
        if sid(sig) != row["projective_linear_form_Qi_sha256"]:
            raise SystemExit(f"carrier signature/hash mismatch: {cid}")

        if cid in SPECIAL:
            decomposition = special_boundary_proof(cid, sig, c1_by_id[cid])
            strict_count = 2
            mults = [1, 1]
            proof_field = {"special_reducible_norm_prime_decomposition_certificate": decomposition}
        else:
            proof = proof_row(cid, sig)
            strict_count = 1
            mults = [1]
            proof_field = {"modular_norm_irreducibility_certificate": proof}

        rep_rows.append({
            "carrier_id": cid,
            "projective_linear_form_Qi_sha256": row["projective_linear_form_Qi_sha256"],
            "normalized_coefficients_Qi": [list(z) for z in sig],
            "singular_surface_section_ideal": ["Q1", "Q2", "Q3", "Q4", f"L_{cid}"],
            "strict_prime_count": strict_count,
            "strict_prime_multiplicities": mults,
            **proof_field,
            "strict_transform_on_resolution": {
                "irreducible_strict_prime_count": strict_count,
                "strict_transform_multiplicities": mults,
                "exceptional_total_transform_orders_attached_in_this_leaf": False,
            },
        })

        orbit = orbit_by_rep[cid]
        words = orbit["transport_words_from_representative"]
        if cid in SPECIAL and orbit["novel20_member_ids"] != [cid]:
            raise SystemExit(f"special two-prime representative unexpectedly has nontrivial C2B orbit: {cid}")
        for member in orbit["novel20_member_ids"]:
            target = by_id[member]
            target_sig = normalize(target["normalized_coefficients_Qi"])
            image = apply_word(sig, words[member], perms)
            if image != target_sig or sid(image) != target["projective_linear_form_Qi_sha256"]:
                raise SystemExit(f"certified transport mismatch: {cid} -> {member}")
            covered.append(member)
            transport_rows.append({
                "carrier_id": member,
                "projective_linear_form_Qi_sha256": target["projective_linear_form_Qi_sha256"],
                "representative_carrier_id": cid,
                "transport_word_from_representative": list(words[member]),
                "transport_verified_against_C2B_projective_signature": True,
                "strict_prime_count": strict_count,
                "strict_prime_multiplicities": mults,
            })

    novel_ids = sorted(cid for row in orbit_rows for cid in row["novel20_member_ids"])
    if sorted(covered) != novel_ids or len(covered) != len(set(covered)) or len(covered) != 20:
        raise SystemExit("transported novel20 coverage is not exact")
    single_ids = sorted(row["carrier_id"] for row in transport_rows if row["strict_prime_count"] == 1)
    double_ids = sorted(row["carrier_id"] for row in transport_rows if row["strict_prime_count"] == 2)
    if len(single_ids) != 17 or double_ids != sorted(SPECIAL):
        raise SystemExit(f"novel20 strict-prime count partition moved: single={single_ids} double={double_ids}")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c2c.orbit_representative_strict_prime_decomposition_and_transport.v2",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C2C_ORBIT_REPRESENTATIVE_STRICT_PRIME_DECOMPOSITION_AND_TRANSPORT",
        "role": "EXACT_NONCREDIT_STRICT_PRIME_DECOMPOSITION_OF_16_C2B_ORBIT_REPRESENTATIVES_USING_IRREDUCIBLE_NORMS_FOR_13_AND_C1_A1_SQUARED_BOUNDARY_PLUS_RESIDUAL_DECOMPOSITION_FOR_3_THEN_CERTIFIED_TRANSPORT_TO_ALL_NOVEL20",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "r5b3b3c1_offboundary_norm_factorization_sha256": C1_SHA,
            "r5b3b3c2b_novel20_surface_action_orbit_preflight_sha256": C2B_SHA,
            "stage33_11d_source_lock_sha256": D11_SHA,
            "stage33_11d_hostile_audit_verdict": c2b["source_locks"]["stage33_11d_hostile_audit_verdict"],
            "stage33_11d_hostile_audited_head": c2b["source_locks"]["stage33_11d_hostile_audited_head"],
            "stage33_11d_pr": int(c2b["source_locks"]["stage33_11d_pr"]),
        },
        "finite_free_surface_model": {
            "base_field": "Q(i)",
            "base_ring": "Q(i)[a1,a2,a3]",
            "radicands": {
                "b1^2": "a2^2+a3^2",
                "b2^2": "a1^2+a3^2",
                "b3^2": "a1^2+a2^2",
                "c^2": "a1^2+a2^2+a3^2",
            },
            "chosen_squareclass_valuation_primes": ["a2+i*a3", "a1+i*a3", "a1+i*a2", "a1^2+a2^2+a3^2"],
            "squareclass_valuation_matrix_mod2": [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
            "squareclass_rank_f2": 4,
            "generic_multiquadratic_degree": 16,
            "homogeneous_surface_coordinate_ring_is_domain": True,
            "finite_free_rank_over_base_ring": 16,
            "surface_coordinate_ring_is_cohen_macaulay": True,
        },
        "finite_free_norm_prime_lemma": {
            "irreducible_norm_case": "For finite-free Cohen-Macaulay domain R over UFD A, if ell is a nonzerodivisor and det(m_ell) is irreducible with valuation one, R/(ell) has one reduced minimal prime; CM removes embedded primes.",
            "factored_norm_length_accounting_case": "If det(m_ell)=q^2*F with q,F distinct irreducibles, an explicit prime over q with residue degree 2 and local multiplicity at least one exhausts the q-adic determinant length 2; valuation one at F forces one residual prime of residue degree and multiplicity one. CM/unmixedness leaves exactly those minimal primes.",
            "application_ring": "Q(i)[a1,a2,a3,b1,b2,b3,c]/(b1^2-a2^2-a3^2,b2^2-a1^2-a3^2,b3^2-a1^2-a2^2,c^2-a1^2-a2^2-a3^2)",
            "rank_over_base": 16,
        },
        "representative_strict_prime_decompositions": {
            "representative_count": 16,
            "single_prime_representative_count": 13,
            "two_prime_representative_count": 3,
            "two_prime_representative_ids": sorted(SPECIAL),
            "rows": rep_rows,
        },
        "transported_novel20_strict_prime_decompositions": {
            "novel20_carrier_count": 20,
            "all_20_covered_exactly_once": True,
            "single_reduced_strict_prime_carrier_count": 17,
            "two_reduced_strict_prime_carrier_count": 3,
            "two_reduced_strict_prime_carrier_ids": double_ids,
            "rows": transport_rows,
        },
        "construction_status": {
            "orbit_representative_prime_decompositions_materialized": True,
            "transported_prime_decompositions_materialized_for_all_novel20": True,
            "c1_factor_adapter_materialized_for_special_a1_squared_norm_group": True,
            "c1_base_factor_to_strict_prime_adapter_materialized_for_all_21_unique_factors": False,
            "exceptional_prime_attachment_for_all_offboundary_carriers_materialized": False,
            "combined_tame_residue_squareclasses_audited": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
        },
        "exact_consequence": {
            "new_exact_prime_decomposition_work_for_novel20_is_complete": True,
            "seventeen_novel_carrier_hyperplane_sections_have_one_reduced_strict_prime": True,
            "lin008_lin015_lin020_each_have_one_boundary_prime_and_one_reduced_residual_prime": True,
            "the_four_nontrivial_C2B_pairs_are_transported_by_certified_actions": True,
            "strict_prime_decomposition_does_not_supply_exceptional_total_transform_orders": True,
            "no_unramifiedness_or_residue_cancellation_credit_follows_yet": True,
        },
        "next_missing_object": "MATCH_ALL_C1_BASE_NORM_FACTORS_TO_THE_REUSED_AND_NEW_STRICT_PRIMES_THEN_ATTACH_R5B3B1_EXCEPTIONAL_VALUATIONS_AND_COMPUTE_COMBINED_TAME_RESIDUE_SQUARECLASSES",
        "next_exact_leaf": "V91C1X_R5B3B3C3_C1_FACTOR_TO_STRICT_PRIME_MATCH_AND_EXCEPTIONAL_ATTACHMENT",
        "credit_firewall": {
            "authority_promotion": False, "hostile_audit_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False, "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False, "mask20_credit": False,
            "source_bound_dim5_credit": False, "stage33_close_credit": False,
            "stage33_release_credit": False, "theorem_credit": False,
            "receiver_credit": False, "endpoint_credit": False, "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
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
            raise SystemExit("checked-in C2C certificate differs from exact rebuild")
    print("PASS V91C1X R5B3B3C2C strict-prime decomposition and transport")
    print("REPRESENTATIVES=16")
    print("NOVEL20=20")
    print("SINGLE_PRIME_CARRIERS=17")
    print("TWO_PRIME_CARRIERS=3")
    print("CERTIFICATE_SHA256=" + cert["canonical_sha256"])


if __name__ == "__main__":
    main()
