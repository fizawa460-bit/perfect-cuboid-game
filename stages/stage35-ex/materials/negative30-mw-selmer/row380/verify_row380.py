#!/usr/bin/env python3
"""Replay row380 with exact ideal arithmetic, GF(2), and Arb enclosures."""

from collections import defaultdict
from functools import cache
from hashlib import sha256
from math import gcd, isqrt, prod
from pathlib import Path
import json

from flint import arb, ctx, fmpz_poly, nmod_poly
import row373_local_arithmetic as local
from verify_row374 import scaled_g
from parent_formula_row379 import TestFunction, apply_prime, DISC

HERE = Path(__file__).resolve().parent
X = fmpz_poly([0, 1])
CURVE = json.loads((HERE / "curve_C29.json").read_text())
F, A, B = (fmpz_poly(CURVE[k]) for k in
           ("F_ascending", "A_star_ascending", "B_star_ascending"))
G = A(-X * X) + X * B(-X * X)
assert G.degree() == F.degree() == 105 and G[105] == F[105] == 1
assert F(-X * X) == G * G(-X)

TABLE_HASH = "f4f616732f3985260959bb9751d6cf50810f46cd52d6ad0fb7b4a8a1991f39b4"
TAIL_HASH = "572183b2eccf59e0d6327834b5dc957c6bcdffb37aecabf4a637574ac595bee7"
TABLE = {r["p"]: r for r in
         json.loads((HERE / "row378_exact.json").read_text())["prime_tables"]}
CASES = ("both", "sum", "equal_case", "one_zero_case")


@cache
def is_prime(p):
    return p >= 2 and all(p % q for q in range(2, isqrt(p) + 1))


@cache
def prime_factors(p):
    assert p > 2 and is_prime(p)
    gn, fn = (nmod_poly([int(c) for c in h], p) for h in (G, F))
    factors = sorted((list(map(int, f)) for f, _ in fn.factor()[1]),
                     key=lambda f: (len(f), f))
    if p in TABLE:
        assert factors == TABLE[p]["factors_ascending"]
    gs = []
    rho = nmod_poly([0, 1], p)
    for g, e in gn.factor()[1]:
        t = (-rho * rho) % g
        matches = [j for j, f in enumerate(factors)
                   if nmod_poly(f, p).compose_mod(t, g).is_zero()]
        assert len(matches) == 1 and len(factors[matches[0]]) == g.degree() + 1
        gs.append((g, e, matches[0]))
    assert len(gs) == len(factors) == len({j for _, _, j in gs})
    return gn, gs


def hensel_valuation(h, gn, g, p, upper):
    cofactor, remainder = divmod(gn, g)
    assert remainder.is_zero()
    d, inverse, _ = cofactor.xgcd(g)
    assert d == 1
    a = fmpz_poly(list(map(int, g)))
    b = fmpz_poly(list(map(int, cofactor)))
    modulus = p
    for _ in range(upper):
        error = [int(c) for c in G - a * b]
        assert all(c % modulus == 0 for c in error)
        E = nmod_poly([c // modulus for c in error], p)
        u = (E * inverse) % g
        v, rem = divmod(E - u * cofactor, g)
        assert rem.is_zero() and u.degree() < g.degree() and v.degree() < cofactor.degree()
        a += modulus * fmpz_poly(list(map(int, u)))
        b += modulus * fmpz_poly(list(map(int, v)))
        modulus *= p
    common = gcd(*(int(c) for c in h % a))
    assert common % modulus != 0
    valuation = 0
    while common % p == 0:
        common //= p
        valuation += 1
    return valuation


def exact_relation(row):
    h = fmpz_poly(row["coefficients"])
    norm = abs(int(G.resultant(h)))
    assert norm and h.degree() < 105
    odd_norm = norm // (norm & -norm)
    factorization = row["odd_factorization"]
    assert odd_norm == prod(p**e for p, e in factorization)
    assert len({p for p, _ in factorization}) == len(factorization)
    support = []
    for p, e in factorization:
        assert e > 0
        gn, gs = prime_factors(p)
        common = gn.gcd(nmod_poly(list(map(int, h)), p))
        hits = [(g, m, j) for g, m, j in gs if (common % g).is_zero()]
        assert hits
        if len(hits) == 1:
            g, _, j = hits[0]
            assert e % g.degree() == 0
            if (e // g.degree()) % 2:
                support.append((p, j))
        elif sum(g.degree() for g, _, _ in hits) == e:
            support.extend((p, j) for _, _, j in hits)
        else:
            assert all(m == 1 for _, m, _ in hits)
            vals = [(g.degree(), j, hensel_valuation(h, gn, g, p, e // g.degree()))
                    for g, _, j in hits]
            assert sum(f * v for f, _, v in vals) == e
            support.extend((p, j) for _, j, v in vals if v % 2)
    assert sorted(support) == [tuple(z) for z in row["mod2_labels"]]
    return sorted(support)


def quotient_relations(relations):
    labels = sorted({label for row in relations for label in row})
    index = {label: i for i, label in enumerate(labels)}
    vectors = [sum(1 << index[label] for label in row) for row in relations]
    output = {}
    for case in CASES:
        unknown = sum(1 << i for i, (p, j) in enumerate(labels)
                      if p not in TABLE or TABLE[p]["possible_nonsplit_masks"][case] >> j & 1)
        span = local.Span()
        for vector in vectors:
            span.add(vector & unknown)
        def in_span(v):
            while v:
                pivot = v.bit_length() - 1
                if pivot not in span.rows:
                    return False
                v ^= span.rows[pivot]
            return True
        new = [list(label) for i, label in enumerate(labels)
               if unknown >> i & 1 and in_span(1 << i)]
        output[case] = {"formal_relation_rank": len(span.rows), "new_split": new}
    return output


def value(pair, mask):
    a, b = pair
    return ((a & mask).bit_count() % 2) | (((b & mask).bit_count() % 2) << 1)


def paired_propagation(relations, forced):
    allowed = {p: [tuple(v) for v in row["pairs"]] for p, row in TABLE.items()}
    for p, j in forced:
        if p in allowed:
            allowed[p] = [(a, b) for a, b in allowed[p] if (a | b) >> j & 1 == 0]
    equations = []
    for row in relations:
        equation = defaultdict(int)
        for p, j in row:
            equation[p] ^= 1 << j
        if all(p in allowed for p in equation):
            equations.append(equation)
    while True:
        removed = 0
        for equation in equations:
            for p, mask in equation.items():
                other = {0}
                for q, m in equation.items():
                    if p != q:
                        other = {a ^ b for a in other
                                 for b in {value(pair, m) for pair in allowed[q]}}
                filtered = [v for v in allowed[p] if value(v, mask) in other]
                assert (0, 0) in filtered
                removed += len(allowed[p]) - len(filtered)
                allowed[p] = filtered
        if not removed:
            break

    added = []
    for p, pairs in allowed.items():
        nonzero = 0
        for a, b in pairs:
            nonzero |= a | b
        given = TABLE[p]["possible_nonsplit_masks"]["both"]
        assert given & nonzero == nonzero
        added.extend([p, i] for i in range(given.bit_length()) if (given ^ nonzero) >> i & 1)
    return {"old_pairs": sum(len(row["pairs"]) for row in TABLE.values()),
            "new_pairs": sum(map(len, allowed.values())),
            "new_common_split": added,
            "rows_changed": {p: [len(TABLE[p]["pairs"]), len(v)]
                             for p, v in allowed.items() if len(v) != len(TABLE[p]["pairs"])}}


def w_roots():
    thetas = local.local_roots(F(X - 1))
    roots = []
    for theta in thetas:
        ring = theta.ring
        w = ring.hensel(scaled_g(G(X + 1), ring), ring.zero,
                        ring.sqrt_residue(theta.digit(0)))
        assert theta == -w * w - ring.pi**2 * w and w.valuation() == 0
        roots.append(w)
    return roots


def unit_code(numerator, shift, t_exponent, roots):
    """Evaluate numerator divided by pi^shift * W^t_exponent."""
    terms = [(i, local.v2(int(c)), int(c)) for i, c in enumerate(numerator(X + 1)) if c]
    coords = []
    for w in roots:
        ring = w.ring
        coefficients = [ring.zero for _ in range(numerator.degree() + 1)]
        for i, v, c in terms:
            power = 3 * v + i - shift
            assert power >= 0
            if power < local.PRECISION:
                coefficients[i] = (c >> v) * ring.pi_powers[power]
        z = local.evaluate(coefficients, w) * ring.inverse(w)**t_exponent
        assert z.valuation() == 0
        coords.append(ring.coordinate(z))
    return coords


def unit_obstructions(new_units):
    roots = w_roots()
    assert -int(G(1)) == 2**35
    masks = [int(x, 16) for x in json.loads(
        (HERE / "row373_kummer2_membership.json").read_text())["parity_equations"]]
    assert len(masks) == 54
    span = local.Span()
    for row in json.loads((HERE / "unit_witnesses.json").read_text()):
        num = row["sign"] * fmpz_poly(row["polynomial"])(-X * X)
        m = row["m"]
        assert int(G.resultant(num)) == 2**(35 * m)
        coords = unit_code(num, m, m, roots)
        assert coords == row["coordinates"]
        obs = sum(((local.combine(coords) & mask).bit_count() % 2) << i
                  for i, mask in enumerate(masks))
        assert obs == int(row["obs"], 16) and span.add(obs) is not None
    assert len(span.rows) == 17
    for row in new_units:
        num = row.get("sign", 1) * fmpz_poly(row["coefficients"])
        k, m = row.get("denominator_exponent", 0), row.get("t_exponent", 0)
        assert min(k, m) == 0 and min(k, m) >= 0
        assert int(G.resultant(num)) == 2**(105 * k + 35 * m)
        coords = unit_code(num, 3 * k + m, m, roots)
        assert coords == row["coordinates"]
        obs = sum(((local.combine(coords) & mask).bit_count() % 2) << i
                  for i, mask in enumerate(masks))
        assert obs == int(row["dyadic_obstruction"], 16) and span.add(obs) is not None
    return len(span.rows)


@cache
def tail_counts():
    data = [(int(p), int(k)) for p, k in
            (line.split(",") for line in (HERE / "tail_roots_independent.csv").read_text().splitlines())]
    assert len(data) == 147058 and sum(k for _, k in data) == 147527
    assert all(5003 < p <= 1982760 and 0 <= k <= 105 for p, k in data)
    return data


def field_constant():
    return arb.const_euler() + (8 * arb.pi()).log() + arb.pi() / 30 - arb(DISC).log() / 105


def conditional_bound(new_split):
    fixture = json.loads((HERE / "grh_fixture.json").read_text())
    test = TestFunction(fixture)
    assert test.case == "both" and test.degree == 16 and test.T.exp() < 1982760 < 5003**2
    extra = defaultdict(set)
    for p, j in new_split:
        extra[p].add(j)
    prime_sum = apply_prime(test, arb(2).log(), [7, 28], 0)
    for p, row in TABLE.items():
        degrees = [len(g) - 1 for g in row["factors_ascending"]]
        mask = row["possible_nonsplit_masks"]["both"] & ~sum(1 << j for j in extra[p])
        prime_sum += apply_prime(test, arb(p).log(), degrees, mask)
    _, g199 = prime_factors(199)
    degree199 = {j: f.degree() for f, _, j in g199}
    assert sorted(degree199.values()) == [1, 27, 76]
    prime_sum += apply_prime(test, arb(199).log(), [degree199[j] for j in range(3)],
                             7 & ~sum(1 << j for j in extra[199]))
    for p, k in tail_counts():
        if not k:
            continue
        count = 0
        if p in extra:
            _, pp = prime_factors(p)
            count = sum(g.degree() == 1 and j in extra[p] for g, _, j in pp)
            assert count <= k
        logp = arb(p).log()
        w = 2 * logp * (-logp / 2).exp() * test.value(logp) / 105
        prime_sum += w * (count - arb(k - count) / 15)
    score = field_constant() - test.arch_upper() + prime_sum
    assert score > arb("0.024")
    return {"excluded_degree_under_quadratic_Hecke_GRH": 16,
            "c_S_both_upper_under_quadratic_Hecke_GRH": 3,
            "score_lower_expression_arb": str(score)}


def unconditional_test_envelope():
    cutoff = 1982760
    arch = (arb(2).log() + (arb.pi() / 2 - 1) / 15)
    C = field_constant()
    small = [(2, [7, 28]), (199, [1, 27, 76])]
    small.extend((p, [len(g) - 1 for g in row["factors_ascending"]])
                 for p, row in TABLE.items())
    known = sum(4 * f * arb(p).log() / (105 * (p**f - 1))
                for p, degrees in small for f in degrees)
    degree_one = sum(4 * k * arb(p).log() / (105 * (p - 1))
                     for p, k in tail_counts() if k)
    # Upper bound by the integral of log(x)/x^2 for x >= 5003.
    M = arb(5003)
    remainder = 4 * (M.log() + 1) / (M * (1 - 1 / M**2))
    score = C - arch + known + degree_one + remainder
    assert score < arb("-0.217")
    return {"cutoff_rational_prime": cutoff, "upper_bound": "-0.217",
            "score_upper_expression_arb": str(score)}


def main():
    ctx.prec = 128
    for name, sha in (("row378_exact.json", TABLE_HASH),
                      ("tail_roots_independent.csv", TAIL_HASH)):
        assert sha256((HERE / name).read_bytes()).hexdigest() == sha
    witnesses = json.loads((HERE / "principal_witnesses.json").read_text())
    rel = [exact_relation(w) for w in witnesses]
    assert len({tuple(x) for x in rel}) == len(rel)
    split = quotient_relations(rel)
    pairs = paired_propagation(rel, split["both"]["new_split"])
    units = unit_obstructions(json.loads((HERE / "new_units.json").read_text()))
    print(json.dumps({"witnesses": len(rel), "quotients": split, "paired": pairs,
                      "unit_obstruction_rank": units, "unit_kernel_dimension_at_most": 55 - units,
                      "conditional_improvement": conditional_bound(split["both"]["new_split"]),
                      "unconditional_explicit_formula_envelope": unconditional_test_envelope()},
                     indent=2))


if __name__ == "__main__":
    main()
