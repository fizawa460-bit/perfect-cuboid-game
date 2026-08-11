from fractions import Fraction


def avg(xs):
    return sum(xs, Fraction(0, 1)) / len(xs)


# 1. Finite-dictionary pigeonhole model.
# J[p][e] are elementary-boundary masses, I[p] is an exact influence
# majorized by the sum of the common packet-wide dictionary entries.
J = [
    [Fraction(1, 8), Fraction(0), Fraction(1, 16), Fraction(0)],
    [Fraction(0), Fraction(1, 4), Fraction(0), Fraction(1, 16)],
    [Fraction(1, 16), Fraction(1, 16), Fraction(1, 8), Fraction(0)],
    [Fraction(0), Fraction(1, 8), Fraction(1, 16), Fraction(1, 16)],
    [Fraction(1, 8), Fraction(0), Fraction(0), Fraction(1, 8)],
]
I = [sum(row) for row in J]
r = len(I)
K = len(J[0])
ibar = avg(I)
label_avgs = [avg([J[p][e] for p in range(r)]) for e in range(K)]
assert max(label_avgs) >= ibar / K

# 2. Common-skeleton support, energy and heavy-support inequalities.
rho = [Fraction(0), Fraction(1, 5), Fraction(1, 10), Fraction(3, 10), Fraction(2, 5)]
rho_bar = avg(rho)
support_fraction = Fraction(sum(x > 0 for x in rho), len(rho))
energy = avg([x * x for x in rho])
heavy_fraction = Fraction(sum(x >= rho_bar / 2 for x in rho), len(rho))
assert support_fraction >= rho_bar
assert energy >= rho_bar * rho_bar
assert heavy_fraction >= rho_bar / (2 - rho_bar)

# 3. Exact two-level Bernoulli variance decomposition.
# Rows are primes; columns are states x.
b = [
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
]
rho_p = [Fraction(sum(row), len(row)) for row in b]
rho_bar = avg(rho_p)

lhs = avg([
    (Fraction(v, 1) - rho_bar) ** 2
    for row in b
    for v in row
])
var_between = avg([(x - rho_bar) ** 2 for x in rho_p])
var_within = avg([x * (1 - x) for x in rho_p])
assert lhs == var_between + var_within

for p, row in enumerate(b):
    assert avg([Fraction(v, 1) - rho_p[p] for v in row]) == 0
assert avg([x - rho_bar for x in rho_p]) == 0

# 4. SIGN common-form identity: prime dependence only through A,B.
for A, B, S, D in [(3, 2, 5, 7), (5, 4, -3, 8), (7, 1, 9, -2)]:
    lp = A * S + B * D
    lm = A * S - B * D
    assert lp * lm == A * A * S * S - B * B * D * D

print({
    "stage": "14-t103",
    "dictionary_pigeonhole_checked": True,
    "common_skeleton_support_checked": True,
    "common_skeleton_energy_checked": True,
    "heavy_support_checked": True,
    "two_level_variance_checked": True,
    "sign_common_form_checked": True,
    "status": "ok",
})
