#!/usr/bin/env python3
"""Exact replay of the binary class relations and the GRH certificate."""
from collections import Counter, defaultdict
from hashlib import sha256
from pathlib import Path
import json

from flint import arb, ctx, fmpz_poly
from linear import setup, generic_reduction, coupled_domains
from verify_row380 import TABLE, TABLE_HASH, TAIL_HASH, exact_relation, prime_factors
from verify_row380 import tail_counts, field_constant, G, X, w_roots
from parent_formula_row379 import TestFunction, apply_prime

HERE = Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE / name).read_text())


def decomposition(ps):
    factors = {}
    for p in sorted(ps):
        if p in TABLE:
            ds = [len(f) - 1 for f in TABLE[p]["factors_ascending"]]
            factors[p] = ds, [1] * len(ds)
        else:
            _, ff = prime_factors(p)
            ff = sorted(ff, key=lambda a: a[2])
            factors[p] = [g.degree() for g, _, _ in ff], [e for _, e, _ in ff]
    return factors


def analyse(relations):
    ps = set(TABLE) | {199} | {p for row in relations for p, _ in row}
    factors = decomposition(ps)
    starts, labels, equations = setup(TABLE, factors, relations)
    generic = {
        case: generic_reduction(TABLE, starts, labels, equations, case)[0]
        for case in ("both", "sum", "equal_case", "one_zero_case")
    }
    new = generic["both"]["new_split"]
    common = sum(1 << (starts[p] + j) for p, j in new)
    allowed, span = coupled_domains(TABLE, starts, len(labels), equations, common)
    table_killed = [[], []]
    for p, entries in sorted(allowed.items()):
        m_both = m_sum = 0
        for a, b in entries:
            m_both |= a | b
            m_sum |= a ^ b
        for case, possible, killed in zip(("both", "sum"), (m_both, m_sum), table_killed):
            diff = TABLE[p]["possible_nonsplit_masks"][case] & ~possible
            killed.extend([p, j] for j in range(diff.bit_length()) if diff >> j & 1)
    return {
        "formal_odd_prime_coordinates":len(labels),
        "rational_principal_relations":len(factors),
        "generic_quotients":generic,
        "paired_linear_equation_rank":len(span),
        "paired_table_initial_total":sum(len(r["pairs"]) for r in TABLE.values()),
        "paired_table_new_total":sum(map(len, allowed.values())),
        "paired_table_changed_rational_primes":sum(len(TABLE[p]["pairs"]) != len(ds) for p, ds in allowed.items()),
        "paired_table_new_split":dict(zip(("both","sum"), table_killed)),
    }, factors, generic_reduction({}, starts, labels, equations, 'both')[0]


def explicit_score(factors, split, fixture, use_source_split):
    test = TestFunction(fixture)
    assert test.degree == 2 and test.T == 11
    assert test.T.exp() < 1982760 < 5003**2
    extra = defaultdict(set)
    for p, j in split:
        extra[p].add(j)
    contribution = apply_prime(test, arb(2).log(), [7, 28], 0)
    for p in sorted(TABLE.keys() | {199}):
        degrees, _ = factors[p]
        mask = ((1 << len(degrees)) - 1
                if p == 199 or not use_source_split
                else TABLE[p]["possible_nonsplit_masks"]["both"])
        mask &= ~sum(1 << j for j in extra[p])
        contribution += apply_prime(test, arb(p).log(), degrees, mask)
    for p, k in tail_counts():
        if not k:
            continue
        logp = arb(p).log()
        if logp > test.T:
            break
        count = 0
        if p in extra:
            degrees, _ = factors[p]
            assert degrees.count(1) == k
            count = sum(degrees[j] == 1 for j in extra[p])
        w = 2 * logp * (-logp / 2).exp() * test.value(logp) / 105
        contribution += w * (count - arb(k - count) / (test.degree - 1))
    return field_constant() - test.arch_upper() + contribution


def dyadic_principal():
    h = fmpz_poly(read('dyadic_principal.json')['coefficients'])
    assert h.degree() < 105
    norm = abs(int(G.resultant(h)))
    k, rest = divmod(norm.bit_length() - 1 - 7, 105)
    assert k >= 0 and rest == 0 and norm == 2**(105*k + 7)
    for i,c in enumerate(h(X + 1)):
        assert int(c) % 2**max(0, k - i//3) == 0
    # The integral h(rho)/2^k has norm 2^7, so its ideal is the degree-7 prime.
    # The principal (rho-1) has valuation one at each of the two dyadic primes.
    assert abs(int(G(1))) == 2**35 and all(w.valuation() == 0 for w in w_roots())
    return {'denominator_exponent':k, 'absolute_norm':128, 'both_dyadic_primes_principal':True}


def main():
    ctx.prec = 128
    for name, digest in (("row378_exact.json", TABLE_HASH),
                         ("tail_roots_independent.csv", TAIL_HASH),
                         ("principal_witnesses.json", "c241e01eba863db2b861ee2fbbae9c81fd52a2f4e241f62f0101684840556bce")):
        assert sha256((HERE / name).read_bytes()).hexdigest() == digest
    # The row380 audit has independently verified these parent supports.
    parent = [tuple(map(tuple, row["mod2_labels"])) for row in read("principal_witnesses.json")]
    additions = [tuple(exact_relation(row)) for row in read("new_relations.json")]
    assert len(parent) == 458 and len(additions) == 3682
    assert len(set(parent + additions)) == len(parent + additions)
    data, factors, full = analyse(parent + additions)
    data['dyadic_principal'] = dyadic_principal()
    data["new_principal_witnesses"] = len(additions)
    score = explicit_score(factors, data["generic_quotients"]["both"]["new_split"],
                           read("grh_fixture381.json"), True)
    assert score > arb("0.060")
    data["conditional_score_lower_expression_arb"] = str(score)
    data["c_both_under_unramified_quadratic_hecke_grh"] = 0
    full_score = explicit_score(factors, full['new_split'], read('grh_fixture_full381.json'), False)
    assert full_score > arb('0.039')
    data['full_class_group_vanishing_odd_prime_classes'] = len(full['new_split'])
    data['full_class_group_score_lower_expression_arb'] = str(full_score)
    data['c_Cl_under_unramified_quadratic_hecke_grh'] = 0
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
