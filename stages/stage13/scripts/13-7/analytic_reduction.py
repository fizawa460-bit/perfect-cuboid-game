#!/usr/bin/env python3
"""Stage13-7d: exact analytic reduction of the parity-resolved pure-G gap.

This is not an asymptotic theorem. It proves/validates an exact finite
reduction of the Stage13 G-neutral observable to:

  * an ordering kernel in the normalized variables theta and t=z/p,
  * a primitive Möbius correction over gcd(p,z), and
  * an angular representation-count discrepancy.

It also verifies that the Stage13-3b archimedean chamber integrals are exactly
the continuum uniform-angle image of the same ordering kernel, and records why
the Stage12 multiplicative machinery does not apply directly to the G-neutral
weight 1/R_all(p).
"""
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

DEFAULT_BOUND = 100_000
OUT = Path("stages/stage13/data/13-7/analytic_reduction_report.json")
CATS = ("ab", "ac", "bc")
LOCK_G_100K = (27355.62607322125, 11689.654887791105, 11666.07864778778)
LOCK_G_OE_AC_BC = 0.9542232763020319
LOCK_G_EE_AC_BC = 1.04546679652665
GEOM_LOCK = (0.659705248705705, 0.302699752672608, 0.271295548757857)


def triples(B: int):
    for m in range(2, math.isqrt(B) + 1):
        mm = m * m
        for n in range(1, m):
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            u, v, w = mm - n * n, 2 * m * n, mm + n * n
            if w > B:
                continue
            if u > v:
                u, v = v, u
            for k in range(1, B // w + 1):
                yield k * u, k * v, k * w


def smallest_prime_factors(N: int):
    spf = list(range(N + 1))
    if N >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(N) + 1):
        if spf[p] != p:
            continue
        for q in range(p * p, N + 1, p):
            if spf[q] == q:
                spf[q] = p
    return spf


def distinct_prime_factors(n: int, spf):
    out = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out


def mobius_squarefree_divisors(n: int, spf):
    """Yield (m, mu(m)) for squarefree m|n."""
    items = [(1, 1)]
    for p in distinct_prime_factors(n, spf):
        items += [(m * p, -mu) for m, mu in items.copy()]
    return items


def classify(x: int, y: int, z: int):
    """x<y is a distinguished face representation; return ab/ac/bc index."""
    if not x < y:
        raise ArithmeticError(("face order", x, y))
    if z > y:
        return 0
    if x < z < y:
        return 1
    if z < x:
        return 2
    return None  # repeated-edge boundary excluded by a<b<c


def geom_probabilities(t: float):
    """Uniform-inner-angle category probabilities for fixed t=z/p."""
    invsqrt2 = 1.0 / math.sqrt(2.0)
    if t < invsqrt2:
        ac = 4.0 * math.asin(t) / math.pi
        return (0.0, ac, 1.0 - ac)
    if t < 1.0:
        ac = 4.0 * math.acos(t) / math.pi
        return (1.0 - ac, ac, 0.0)
    return (1.0, 0.0, 0.0)


def simpson(f, a: float, b: float, n: int = 200_000):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    s += 4.0 * sum(f(a + h * j) for j in range(1, n, 2))
    s += 2.0 * sum(f(a + h * j) for j in range(2, n, 2))
    return s * h / 3.0


def geometry_integrals():
    a, b = 0.0, math.pi / 4.0
    Ibc = simpson(lambda th: math.atan(math.sin(th)), a, b)
    Iac = simpson(
        lambda th: math.atan(math.cos(th)) - math.atan(math.sin(th)), a, b
    )
    Iab = (math.pi / 2.0) * (math.pi / 4.0) - Ibc - Iac
    return (Iab, Iac, Ibc)


def factor_exponents(n: int):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def G_value(n: int):
    G = 1
    for p, e in factor_exponents(n):
        if p % 4 == 1:
            G *= 2 * e + 1
    return G


def R_all_formula(n: int):
    return (G_value(n) - 1) // 2


def vector_stats(v):
    total = sum(v)
    return {
        "weight": dict(zip(CATS, v)),
        "total_weight": total,
        "ratio_bc": {"ab": v[0] / v[2], "ac": v[1] / v[2], "bc": 1.0},
    }


def signed_vector_stats(v):
    return {
        "weight": dict(zip(CATS, v)),
        "sum": sum(v),
        "L1": sum(abs(x) for x in v),
        "ac_minus_bc": v[1] - v[2],
    }


def enumerate_reduction(B: int):
    all_triples = list(triples(B))
    mark = bytearray(B + 1)
    for u, v, _ in all_triples:
        mark[u] = mark[v] = 1

    faces = defaultdict(list)
    for x, y, p in all_triples:
        if mark[p]:
            faces[p].append((x, y))

    spf = smallest_prime_factors(B)
    layers = (
        "direct",
        "mobius",
        "m1_unfiltered",
        "geom_shell",
        "inner_angular_discrepancy",
        "primitive_correction",
    )
    acc = {
        par: {layer: [0.0, 0.0, 0.0] for layer in layers}
        for par in ("OE", "EE", "ALL")
    }
    diagnostics = {
        "integer_pythagorean_triples": len(all_triples),
        "indexed_p_values": len(faces),
        "oriented_outer_shells_with_faces": 0,
        "strict_order_boundary_hits": 0,
        "face_parity_mismatches": 0,
        "contributing_outer_parity_failures": 0,
        "mobius_shell_mismatches": 0,
        "R_formula_mismatches": 0,
    }

    for p, reps in faces.items():
        if len(reps) != R_all_formula(p):
            diagnostics["R_formula_mismatches"] += 1

    for u, v, d in all_triples:
        for p, z in ((u, v), (v, u)):
            reps = faces.get(p)
            if not reps:
                continue
            diagnostics["oriented_outer_shells_with_faces"] += 1
            R = len(reps)
            parity = "OE" if p & 1 else "EE"

            direct = [0, 0, 0]
            m1 = [0, 0, 0]
            for x, y in reps:
                face_parity = "OE" if ((x ^ y) & 1) else "EE"
                if face_parity != parity:
                    diagnostics["face_parity_mismatches"] += 1
                cat = classify(x, y, z)
                if cat is None:
                    diagnostics["strict_order_boundary_hits"] += 1
                    continue
                m1[cat] += 1
                if math.gcd(math.gcd(x, y), z) == 1:
                    direct[cat] += 1

            if any(direct):
                if (p & 1) == (z & 1):
                    diagnostics["contributing_outer_parity_failures"] += 1
                if math.gcd(p, z) % 2 == 0:
                    diagnostics["contributing_outer_parity_failures"] += 1

            mob = [0, 0, 0]
            for m, mu in mobius_squarefree_divisors(math.gcd(p, z), spf):
                for X, Y in faces.get(p // m, ()):
                    cat = classify(X, Y, z // m)
                    if cat is not None:
                        mob[cat] += mu
            if mob != direct:
                diagnostics["mobius_shell_mismatches"] += 1
                raise ArithmeticError(("Möbius reduction mismatch", p, z, d, direct, mob))

            geom = geom_probabilities(z / p)
            for key in (parity, "ALL"):
                for i in range(3):
                    values = {
                        "direct": direct[i] / R,
                        "mobius": mob[i] / R,
                        "m1_unfiltered": m1[i] / R,
                        "geom_shell": geom[i],
                        "inner_angular_discrepancy": m1[i] / R - geom[i],
                        "primitive_correction": (mob[i] - m1[i]) / R,
                    }
                    for layer, value in values.items():
                        acc[key][layer][i] += value

    for key in ("OE", "EE", "ALL"):
        rec = [
            acc[key]["geom_shell"][i]
            + acc[key]["inner_angular_discrepancy"][i]
            + acc[key]["primitive_correction"][i]
            for i in range(3)
        ]
        acc[key]["reconstructed"] = rec
        acc[key]["reconstruction_max_abs_error"] = max(
            abs(rec[i] - acc[key]["direct"][i]) for i in range(3)
        )

    return acc, diagnostics


def build_report(B: int):
    acc, diagnostics = enumerate_reduction(B)
    geom = geometry_integrals()

    direct = acc["ALL"]["direct"]
    if B == 100_000:
        for got, want in zip(direct, LOCK_G_100K):
            if abs(got - want) > 2e-8:
                raise ArithmeticError(("G-neutral 100k lock", got, want))
        oe_ratio = acc["OE"]["direct"][1] / acc["OE"]["direct"][2]
        ee_ratio = acc["EE"]["direct"][1] / acc["EE"]["direct"][2]
        if (
            abs(oe_ratio - LOCK_G_OE_AC_BC) > 2e-12
            or abs(ee_ratio - LOCK_G_EE_AC_BC) > 2e-12
        ):
            raise ArithmeticError(("parity ratio lock", oe_ratio, ee_ratio))

    for got, want in zip(geom, GEOM_LOCK):
        if abs(got - want) > 2e-12:
            raise ArithmeticError(("geometry lock", got, want))

    example = {
        "R_all_5": R_all_formula(5),
        "R_all_13": R_all_formula(13),
        "R_all_65": R_all_formula(65),
    }
    example["weights"] = {
        "w_5": 1.0 / example["R_all_5"],
        "w_13": 1.0 / example["R_all_13"],
        "w_65": 1.0 / example["R_all_65"],
        "w_5_times_w_13": 1.0 / (example["R_all_5"] * example["R_all_13"]),
    }

    return {
        "metadata": {
            "stage": "13-7d",
            "title": "Exact angular/Mobius reduction of the parity-resolved pure-G directional gap",
            "B_validation": B,
            "scope": "exact finite analytic reduction plus validation; no directional asymptotic limit theorem",
        },
        "definitions": {
            "F_p": "unordered positive face representations (x,y), x<y, x^2+y^2=p^2",
            "R_all_p": "|F_p|=(G(p)-1)/2",
            "outer_shell": "oriented (p,z,d) with p^2+z^2=d^2 and d<=B",
            "G_neutral_q": "sum over outer shells of R_all(p)^(-1) times primitive strict-order face incidences in category q",
            "ordering_kernel": {"ab": "z>y", "ac": "x<z<y", "bc": "z<x"},
            "normalized_angle": "theta=asin(x/p) in (0,pi/4), t=z/p",
        },
        "exact_reduction": {
            "mobius_identity": "G_q(B)=sum_(p,z,d) 1/R(p) * sum_(m|gcd(p,z)) mu(m) N_q(p/m,z/m)",
            "reason": "m|x,y iff the face representation is m times a representation of p/m; category inequalities are scale invariant after z is replaced by z/m",
            "parity_decoupling": "For any surviving primitive incidence, OE iff p is odd and then z is even; EE iff p is even and then z is odd. Hence gcd(p,z) is odd and the Mobius divisors m are odd, so the OE/EE stratum is preserved by p->p/m.",
            "gap_kernel": {
                "0<t<1/sqrt(2)": "K_n(t)=2*A_n^<(asin t)+E_n(asin t)-R(n)",
                "1/sqrt(2)<t<1": "K_n(t)=A_n^<(acos t)",
                "t>1": "K_n(t)=0",
                "A_definition": "A_n^<(phi)=# { (X,Y) in F_n : asin(X/n)<phi }; E_n counts equality/repeated-edge boundary representations",
            },
            "three_layer_identity": "G_neutral = geom_shell + inner_angular_discrepancy + primitive_correction (exact at finite B by definition of the two discrepancy terms)",
        },
        "archimedean_bridge": {
            "uniform_inner_angle_probabilities": {
                "0<t<1/sqrt(2)": "(P_ab,P_ac,P_bc)=(0, 4 asin(t)/pi, 1-4 asin(t)/pi)",
                "1/sqrt(2)<t<1": "(1-4 acos(t)/pi, 4 acos(t)/pi, 0)",
                "t>1": "(1,0,0)",
            },
            "statement": "If theta is replaced by uniform measure on (0,pi/4) and the outer angle phi=atan(z/p) by uniform measure on (0,pi/2), the exact ordering kernel gives exactly the Stage13-3b chamber integrals.",
            "integrals": {
                "I_ab": geom[0],
                "I_ac": geom[1],
                "I_bc": geom[2],
                "sum": sum(geom),
            },
            "ratio_bc": {"ab": geom[0] / geom[2], "ac": geom[1] / geom[2], "bc": 1.0},
        },
        "stage12_direct_transfer_obstruction": {
            "statement": "The G-neutral weight w(p)=1/R_all(p)=2/(G(p)-1) is not multiplicative, while the angular truncation A_n(phi) also retains representation-angle data discarded by the scalar G(p)-1 count. Therefore the frozen Stage12 scalar Selberg-Delange/Euler-product machinery cannot be applied to the Stage13-7d observable without a new refinement.",
            "explicit_counterexample": example,
        },
        "validation": {
            "diagnostics": diagnostics,
            "B100k_G_neutral_lock_matched": B == 100_000,
            "layers": {
                key: {
                    "direct": vector_stats(acc[key]["direct"]),
                    "m1_unfiltered": vector_stats(acc[key]["m1_unfiltered"]),
                    "geom_shell": vector_stats(acc[key]["geom_shell"]),
                    "inner_angular_discrepancy": signed_vector_stats(
                        acc[key]["inner_angular_discrepancy"]
                    ),
                    "primitive_correction": signed_vector_stats(
                        acc[key]["primitive_correction"]
                    ),
                    "reconstructed": vector_stats(acc[key]["reconstructed"]),
                    "reconstruction_max_abs_error": acc[key][
                        "reconstruction_max_abs_error"
                    ],
                }
                for key in ("ALL", "OE", "EE")
            },
        },
        "conclusion": {
            "stage13_7d_status": "COMPLETE_AT_EXACT_ANALYTIC_REDUCTION_LEVEL",
            "what_is_now_exact": "The ac-bc pure-G problem has been reduced to a signed angular representation-count discrepancy plus an odd-divisor primitive Mobius correction over oriented outer Pythagorean shells.",
            "what_is_not_proved": "No decay rate for the angular discrepancy, no asymptotic parity constant, and no limiting directional ratio is proved.",
            "next": "Stage13-7e: estimate the coupled angular discrepancy and primitive-correction averages, likely via a Gaussian-integer/angular refinement rather than the scalar Stage12 Dirichlet series.",
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bound", type=int, default=DEFAULT_BOUND)
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()
    report = build_report(args.bound)
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.stdout:
        print(text, end="")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text, encoding="utf-8")
        print(OUT)


if __name__ == "__main__":
    main()
