#!/usr/bin/env python3
"""Exact arithmetic replay for the Stage35EX row368 Ward transfer.

Requires Python 3.10+ and SymPy. The accompanying proof supplies the general
division-polynomial identity, the rank arguments, and the inherited C118 input.
"""
from functools import lru_cache
from json import dumps
from pathlib import Path

import sympy as sp


Z = sp.Symbol("z")
P = sp.Poly(Z**3 + 5*Z**2 + 11*Z - 1, Z)
Q = sp.Poly(Z**3 + Z**2 - 13*Z - 5, Z)
W1 = sp.Poly(1, Z)
W2 = sp.Poly(-2, Z)
W3 = sp.Poly((1-Z)*(3+Z), Z)
W4 = sp.Poly(-4*(1-3*Z-5*Z**2-Z**3), Z)
W5 = W4*W2**3 - W3**3
W6 = (W3*(W5*W2**2 - W4**2)).exquo(W2)
PHI = {3: W3**2 - W2*W4, 5: W5**2 - W4*W6}
WARD = {3: W3, 5: W5}
PRIM = {
    3: (sp.Poly(Z-1, Z), sp.Poly(Z+3, Z)),
    5: (P, Q),
}
TARGET3 = [32, 80, 88, 92, 122, 128, 152]
TARGET5 = [24, 36, 54, 56, 64, 66, 84, 94, 96, 104, 114, 124, 126, 144]


def factor(n):
    assert n > 0
    result = {}
    for p in range(2, n+1):
        if p*p > n:
            break
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
    if n > 1:
        result[n] = 1
    return result


def sf_primes(n):
    return {p for p, e in factor(n).items() if e % 2}


def ae181(j):
    return j % 3 == 0 and all(p == 5 or p % 5 in (2, 3) for p in sf_primes(j//3))


def all181(j):
    return j % 3 == 0 and all(p == 5 or p % 20 in (13, 17) for p in sf_primes(j//3))


def ae211(j):
    extra = set(factor(j)) - {3, 5, 7}
    return j % 3 == 0 and len(extra) == 1 and all(p >= 11 and p % 8 in (3, 5) for p in extra)


def mask_flags(n):
    adjacent = (n-1, n+1)
    a181 = any(map(ae181, adjacent))
    a211 = any(map(ae211, adjacent))
    return (
        any(map(all181, adjacent)),
        a211 and n % 8 != 0,
        a181 and n % 8 != 0,
        a181,
        a211,
    )


def reduce_ward(modulus):
    @lru_cache(None)
    def ward(j):
        if j <= 4:
            return [sp.Poly(0, Z), W1, W2, W3, W4][j].rem(modulus)
        m = j//2
        if j % 2:
            return (ward(m+2)*ward(m)**3 - ward(m-1)*ward(m+1)**3).rem(modulus)
        product = ward(m)*(ward(m+2)*ward(m-1)**2 - ward(m-2)*ward(m+1)**2)
        return product.exquo(W2).rem(modulus)
    return ward


def modpow(base, exponent, modulus):
    result = W1
    base = base.rem(modulus)
    while exponent:
        if exponent % 2:
            result = (result*base).rem(modulus)
        base = (base*base).rem(modulus)
        exponent //= 2
    return result


def transfer_checks(d, ns):
    wd = WARD[d]
    ward = reduce_ward(wd**2)
    rows = {}
    for n in ns:
        j, = [j for j in (n-1, n+1) if j % d == 0]
        m = j//d
        quotient = ward(j).exquo(wd)
        expected = m*modpow(PHI[d], (m*m-1)//2, wd)
        assert quotient == expected
        rows[n] = {"j": j, "m": m, "prime_support": sorted(factor(m)), "B_even": n % 8 == 0}
    return rows


def norm_resultant(f, g):
    # A second exact computation for monic f, via multiplication by g in Z[z]/f.
    columns = [(g*sp.Poly(Z**i, Z)).rem(f) for i in range(f.degree())]
    return int(sp.Matrix([[c.nth(i) for c in columns] for i in range(f.degree())]).det())


def primitive_support(p, a_even):
    roots = {"G": [], "F": []}
    for u, v in [(i, 1) for i in range(p)] + [(1, 0)]:
        a, b = 2*u*v, u*u-v*v
        if not a_even:
            a, b = b, a
        d = a*(u*u+v*v) % p
        if not d:
            continue
        z = pow(b, 4, p)*pow(d, -2, p) % p
        for name, poly in (("G", P), ("F", Q)):
            if int(poly.eval(z)) % p == 0:
                roots[name].append([u, v, z])
    return roots


def residues(p):
    return {i*i % p for i in range(1, p)}


def squareclass_candidates(value_mod8, support, positive=False):
    products = [1]
    for p in support:
        products += [p*d for d in products]
    signs = [1] if positive else [-1, 1]
    return sorted(sign*d for sign in signs for d in products if sign*d % 8 == value_mod8)


def point_count(a, p):
    return 1 + sum((y*y-x*(x*x+a*x+1)) % p == 0 for x in range(p) for y in range(p))


def signed_list(cases):
    return sorted(sign*n for n in cases for sign in (-1, 1))


def main():
    assert W5 == P*Q
    resultants = {}
    for d, pair in PRIM.items():
        values = [int(f.resultant(PHI[d])) for f in pair]
        assert values == [norm_resultant(f, PHI[d]) for f in pair]
        assert values == ([64, 64] if d == 3 else [2**50, 2**50])
        resultants[d] = values
    assert int(P.resultant(Q)) == norm_resultant(P, Q) == -2**14
    a = sp.Poly(Z**3-Z**2+3*Z+1, Z)
    b = sp.Poly(Z**3+Z**2+3*Z-1, Z)
    assert a*b == sp.Poly(P.as_expr().subs(Z, Z**2), Z)
    assert int(a.resultant(b)) == norm_resultant(a, b) == -2**7
    assert reduce_ward(sp.Poly(Z, Z))(23).eval(0) == 23
    assert all(sign*23 % 5 not in residues(5) for sign in (-1, 1))

    indices = list(range(12, 155, 2))
    flags = {n: mask_flags(n) for n in indices}
    masks = [[n for n in indices if flags[n][i]] for i in range(3)]
    base_residual = [n for n in indices if not any(flags[n][:3])]
    assert len(indices) == 72 and list(map(len, masks)) == [16, 10, 27]
    assert len(base_residual) == 36 and 12 in base_residual and 18 in base_residual
    prior_signed = sorted(set(signed_list(base_residual)) - {12, -18, 18})
    prior_abs = sorted({abs(n) for n in prior_signed})
    assert len(prior_abs) == 35 and len(prior_signed) == 69
    assert [n for n in prior_abs if (n-1)*(n+1) % 5 == 0] == TARGET5
    assert [n for n in prior_abs if n not in TARGET5 and (n-1)*(n+1) % 3 == 0] == TARGET3

    rank5 = transfer_checks(5, TARGET5)
    support5 = {}
    for p in sorted({p for row in rank5.values() for p in row["prime_support"]}):
        support5[p] = {parity: primitive_support(p, parity == "A_even")
                       for parity in ("A_even", "B_even")}
        expected = {"G": {5} if p == 19 else set(), "F": {0} if p == 5 else {4} if p == 23 else set()}
        for r in support5[p].values():
            assert {name: {z for _, _, z in entries} for name, entries in r.items()} == expected
    split_values = [11*pow(8, -1, 23) % 23, 17*pow(8, -1, 23) % 23]
    assert split_values == [10, 5] and not set(split_values) & residues(23)
    for n, row in rank5.items():
        row["support_A_even"] = {
            name: [p for p in row["prime_support"] if support5[p]["A_even"][name]]
            for name in ("F", "G")
        }
        for name, support in row["support_A_even"].items():
            if name == "F":
                support = [p for p in support if p != 23]
            assert squareclass_candidates(1, support) == [1]
        if row["B_even"]:
            support = [p for p in row["prime_support"] if support5[p]["B_even"]["F"]]
            allowed = squareclass_candidates(3, support)
            assert allowed == ([-5] if n == 24 else [])
            row["B_even_F_candidates"] = allowed

    rank3 = transfer_checks(3, TARGET3)
    assert all(-3 % p not in residues(p) for p in [17, 41])
    assert 5 not in residues(17)
    for n, row in rank3.items():
        support = [p for p in row["prime_support"] if p not in (17, 41)]
        assert squareclass_candidates(1, support, positive=True) == [1]
        row["A_even_L_plus_candidates"] = [1]
        if row["B_even"]:
            support = [p for p in row["prime_support"] if p != 17]
            assert squareclass_candidates(1, support) == [1]
            row["B_even_L_minus_candidates"] = [1]
    counts = {"E1": {p: point_count(1, p) for p in (5, 7)},
              "E3": {p: point_count(3, p) for p in (3, 11)}}
    assert counts == {"E1": {5: 8, 7: 8}, "E3": {3: 4, 11: 8}}

    new_abs = sorted(TARGET3+TARGET5)
    assert len(set(new_abs)) == 21 and set(new_abs) <= set(prior_abs)
    new_signed = signed_list(new_abs)
    remaining_signed = sorted(set(prior_signed) - set(new_signed))
    remaining_abs = sorted({abs(n) for n in remaining_signed})
    assert len(new_signed) == 42 and len(remaining_signed) == 27
    assert remaining_abs == [12, 30, 42, 48, 60, 72, 78, 90, 102, 108, 120, 132, 138, 150]
    assert all(n % 6 == 0 for n in remaining_abs)
    a_even_only_old = [n for n in prior_abs if flags[n][3] or flags[n][4]]
    assert a_even_only_old == [32, 56, 64, 80, 88, 104, 128, 152]

    ledger = []
    for n in indices:
        mask181, mask212, mask_joint, old_a181, old_a211 = flags[n]
        for sign in (-1, 1):
            for parity in ("A_even", "B_even"):
                labels = []
                if mask181:
                    labels.append("C181_all")
                if mask212:
                    labels.append("C212_all")
                if mask_joint:
                    labels.append("C181_Aeven_and_S264")
                if parity == "A_even" and (old_a181 or old_a211):
                    labels.append("C181_or_C211_Aeven")
                if parity == "B_even" and n % 8:
                    labels.append("S264_Beven")
                if n == 12 and sign == 1:
                    labels.append("C183_signed_plus12")
                if n == 18:
                    labels.append("row367_audited_signed18")
                new = n in new_abs and not labels
                ledger.append({"signed_n": sign*n, "parity": parity, "old_exclusions": labels,
                               "row368_new_label_leaf": new,
                               "retained_in_named_mask_ledger": not labels and not new})
    assert {entry["signed_n"] for entry in ledger if entry["retained_in_named_mask_ledger"]} == set(remaining_signed)

    result = {
        "run": "STAGE35EX_R3_07_ROW368_WARD3_WARD5_TRANSFER",
        "status": "AUTHOR_EXACT_REPLAY_PASS_INDEPENDENT_AUDIT_PENDING",
        "basis": "C189/P112 three masks + C183 signed +12 + audited row367 signed +/-18",
        "old_masks": {"C181_all": masks[0], "C212_all": masks[1], "C181_Aeven_and_S264": masks[2]},
        "P112_residual_abs": base_residual,
        "prior_abs": prior_abs, "prior_signed": prior_signed,
        "ward5": rank5, "ward3": rank3, "resultants_phi": resultants,
        "resultant_F_G_abs": 2**14, "resultant_G_split_abs": 2**7,
        "ward5_primitive_support_full_slopes": support5,
        "p23_cubic_split_residues": split_values, "p5_adjacent_residues": [2, 3],
        "rank3_auxiliary_point_counts": counts,
        "new_abs": new_abs, "new_signed": new_signed,
        "remaining_abs": remaining_abs, "remaining_signed": remaining_signed,
        "remaining_B_even_abs": sorted({abs(e["signed_n"]) for e in ledger
                                        if e["parity"] == "B_even" and e["retained_in_named_mask_ledger"]}),
        "old_Aeven_only_on_prior_residual": a_even_only_old,
        "named_mask_index_parity_ledger": ledger,
    }
    Path(__file__).with_name("row368_exact.json").write_text(
        dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(dumps({"status": result["status"], "prior": [len(prior_abs), len(prior_signed)],
                 "new_ward5": len(TARGET5), "new_ward3": len(TARGET3),
                 "remaining": [len(remaining_abs), len(remaining_signed)],
                 "remaining_abs": remaining_abs, "remaining_B_even": result["remaining_B_even_abs"]},
                ensure_ascii=False))


if __name__ == "__main__":
    main()
